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

class ParticipantThumbnailConfigurationOutputTypeDef(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[List[ThumbnailStorageTypeType]] = None
    recordingMode: Optional[ThumbnailRecordingModeType] = None


class ParticipantThumbnailConfigurationTypeDef(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[Sequence[ThumbnailStorageTypeType]] = None
    recordingMode: Optional[ThumbnailRecordingModeType] = None


class ChannelDestinationConfigurationTypeDef(BaseValidatorModel):
    channelArn: str
    encoderConfigurationArn: Optional[str] = None


class CompositionThumbnailConfigurationOutputTypeDef(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[List[ThumbnailStorageTypeType]] = None


class CompositionThumbnailConfigurationTypeDef(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[Sequence[ThumbnailStorageTypeType]] = None


class VideoTypeDef(BaseValidatorModel):
    width: Optional[int] = None
    height: Optional[int] = None
    framerate: Optional[float] = None
    bitrate: Optional[int] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateIngestConfigurationRequestTypeDef(BaseValidatorModel):
    ingestProtocol: IngestProtocolType
    name: Optional[str] = None
    stageArn: Optional[str] = None
    userId: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    insecureIngest: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None


class IngestConfigurationTypeDef(BaseValidatorModel):
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


class CreateParticipantTokenRequestTypeDef(BaseValidatorModel):
    stageArn: str
    duration: Optional[int] = None
    userId: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    capabilities: Optional[Sequence[ParticipantTokenCapabilityType]] = None


class ParticipantTokenTypeDef(BaseValidatorModel):
    participantId: Optional[str] = None
    token: Optional[str] = None
    userId: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    duration: Optional[int] = None
    capabilities: Optional[List[ParticipantTokenCapabilityType]] = None
    expirationTime: Optional[datetime] = None


class ParticipantTokenConfigurationTypeDef(BaseValidatorModel):
    duration: Optional[int] = None
    userId: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    capabilities: Optional[Sequence[ParticipantTokenCapabilityType]] = None


class S3StorageConfigurationTypeDef(BaseValidatorModel):
    bucketName: str


class DeleteEncoderConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteIngestConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str
    force: Optional[bool] = None


class DeletePublicKeyRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteStageRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteStorageConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class S3DetailTypeDef(BaseValidatorModel):
    recordingPrefix: str


class DisconnectParticipantRequestTypeDef(BaseValidatorModel):
    stageArn: str
    participantId: str
    reason: Optional[str] = None


class EncoderConfigurationSummaryTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class EventTypeDef(BaseValidatorModel):
    name: Optional[EventNameType] = None
    participantId: Optional[str] = None
    eventTime: Optional[datetime] = None
    remoteParticipantId: Optional[str] = None
    errorCode: Optional[EventErrorCodeType] = None


class GetCompositionRequestTypeDef(BaseValidatorModel):
    arn: str


class GetEncoderConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class GetIngestConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class GetParticipantRequestTypeDef(BaseValidatorModel):
    stageArn: str
    sessionId: str
    participantId: str


class ParticipantTypeDef(BaseValidatorModel):
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


class GetPublicKeyRequestTypeDef(BaseValidatorModel):
    arn: str


class PublicKeyTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    publicKeyMaterial: Optional[str] = None
    fingerprint: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class GetStageRequestTypeDef(BaseValidatorModel):
    arn: str


class GetStageSessionRequestTypeDef(BaseValidatorModel):
    stageArn: str
    sessionId: str


class StageSessionTypeDef(BaseValidatorModel):
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class GetStorageConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class GridConfigurationTypeDef(BaseValidatorModel):
    featuredParticipantAttribute: Optional[str] = None
    omitStoppedVideo: Optional[bool] = None
    videoAspectRatio: Optional[VideoAspectRatioType] = None
    videoFillMode: Optional[VideoFillModeType] = None
    gridGap: Optional[int] = None


class ImportPublicKeyRequestTypeDef(BaseValidatorModel):
    publicKeyMaterial: str
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class IngestConfigurationSummaryTypeDef(BaseValidatorModel):
    arn: str
    ingestProtocol: IngestProtocolType
    stageArn: str
    participantId: str
    state: IngestConfigurationStateType
    name: Optional[str] = None
    userId: Optional[str] = None


class PipConfigurationTypeDef(BaseValidatorModel):
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


class ListCompositionsRequestTypeDef(BaseValidatorModel):
    filterByStageArn: Optional[str] = None
    filterByEncoderConfigurationArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListEncoderConfigurationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListIngestConfigurationsRequestTypeDef(BaseValidatorModel):
    filterByStageArn: Optional[str] = None
    filterByState: Optional[IngestConfigurationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListParticipantEventsRequestTypeDef(BaseValidatorModel):
    stageArn: str
    sessionId: str
    participantId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListParticipantsRequestTypeDef(BaseValidatorModel):
    stageArn: str
    sessionId: str
    filterByUserId: Optional[str] = None
    filterByPublished: Optional[bool] = None
    filterByState: Optional[ParticipantStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filterByRecordingState: Optional[ParticipantRecordingFilterByRecordingStateType] = None


class ParticipantSummaryTypeDef(BaseValidatorModel):
    participantId: Optional[str] = None
    userId: Optional[str] = None
    state: Optional[ParticipantStateType] = None
    firstJoinTime: Optional[datetime] = None
    published: Optional[bool] = None
    recordingState: Optional[ParticipantRecordingStateType] = None


class ListPublicKeysRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PublicKeySummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListStageSessionsRequestTypeDef(BaseValidatorModel):
    stageArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StageSessionSummaryTypeDef(BaseValidatorModel):
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class ListStagesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StageSummaryTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    activeSessionId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListStorageConfigurationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class StageEndpointsTypeDef(BaseValidatorModel):
    events: Optional[str] = None
    whip: Optional[str] = None
    rtmp: Optional[str] = None
    rtmps: Optional[str] = None


class StopCompositionRequestTypeDef(BaseValidatorModel):
    arn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateIngestConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str
    stageArn: Optional[str] = None


class AutoParticipantRecordingConfigurationOutputTypeDef(BaseValidatorModel):
    storageConfigurationArn: str
    mediaTypes: Optional[List[ParticipantRecordingMediaTypeType]] = None
    thumbnailConfiguration: Optional[ParticipantThumbnailConfigurationOutputTypeDef] = None
    recordingReconnectWindowSeconds: Optional[int] = None


class AutoParticipantRecordingConfigurationTypeDef(BaseValidatorModel):
    storageConfigurationArn: str
    mediaTypes: Optional[Sequence[ParticipantRecordingMediaTypeType]] = None
    thumbnailConfiguration: Optional[ParticipantThumbnailConfigurationTypeDef] = None
    recordingReconnectWindowSeconds: Optional[int] = None


class DestinationSummaryTypeDef(BaseValidatorModel):
    pass


class CompositionSummaryTypeDef(BaseValidatorModel):
    arn: str
    stageArn: str
    destinations: List[DestinationSummaryTypeDef]
    state: CompositionStateType
    tags: Optional[Dict[str, str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class CreateEncoderConfigurationRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    video: Optional[VideoTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class EncoderConfigurationTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    video: Optional[VideoTypeDef] = None
    tags: Optional[Dict[str, str]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIngestConfigurationResponseTypeDef(BaseValidatorModel):
    ingestConfiguration: IngestConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetIngestConfigurationResponseTypeDef(BaseValidatorModel):
    ingestConfiguration: IngestConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIngestConfigurationResponseTypeDef(BaseValidatorModel):
    ingestConfiguration: IngestConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateParticipantTokenResponseTypeDef(BaseValidatorModel):
    participantToken: ParticipantTokenTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStorageConfigurationRequestTypeDef(BaseValidatorModel):
    s3: S3StorageConfigurationTypeDef
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class StorageConfigurationSummaryTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    s3: Optional[S3StorageConfigurationTypeDef] = None
    tags: Optional[Dict[str, str]] = None


class StorageConfigurationTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    s3: Optional[S3StorageConfigurationTypeDef] = None
    tags: Optional[Dict[str, str]] = None


class DestinationDetailTypeDef(BaseValidatorModel):
    s3: Optional[S3DetailTypeDef] = None


class ListEncoderConfigurationsResponseTypeDef(BaseValidatorModel):
    encoderConfigurations: List[EncoderConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListParticipantEventsResponseTypeDef(BaseValidatorModel):
    events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetParticipantResponseTypeDef(BaseValidatorModel):
    participant: ParticipantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPublicKeyResponseTypeDef(BaseValidatorModel):
    publicKey: PublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ImportPublicKeyResponseTypeDef(BaseValidatorModel):
    publicKey: PublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetStageSessionResponseTypeDef(BaseValidatorModel):
    stageSession: StageSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListIngestConfigurationsResponseTypeDef(BaseValidatorModel):
    ingestConfigurations: List[IngestConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LayoutConfigurationTypeDef(BaseValidatorModel):
    grid: Optional[GridConfigurationTypeDef] = None
    pip: Optional[PipConfigurationTypeDef] = None


class ListIngestConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    filterByStageArn: Optional[str] = None
    filterByState: Optional[IngestConfigurationStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPublicKeysRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListParticipantsResponseTypeDef(BaseValidatorModel):
    participants: List[ParticipantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPublicKeysResponseTypeDef(BaseValidatorModel):
    publicKeys: List[PublicKeySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStageSessionsResponseTypeDef(BaseValidatorModel):
    stageSessions: List[StageSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStagesResponseTypeDef(BaseValidatorModel):
    stages: List[StageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RecordingConfigurationTypeDef(BaseValidatorModel):
    pass


class S3DestinationConfigurationOutputTypeDef(BaseValidatorModel):
    storageConfigurationArn: str
    encoderConfigurationArns: List[str]
    recordingConfiguration: Optional[RecordingConfigurationTypeDef] = None
    thumbnailConfigurations: Optional[List[CompositionThumbnailConfigurationOutputTypeDef]] = None


class StageTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    activeSessionId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    autoParticipantRecordingConfiguration: Optional[ AutoParticipantRecordingConfigurationOutputTypeDef ] = None
    endpoints: Optional[StageEndpointsTypeDef] = None


class ListCompositionsResponseTypeDef(BaseValidatorModel):
    compositions: List[CompositionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CompositionThumbnailConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class S3DestinationConfigurationTypeDef(BaseValidatorModel):
    storageConfigurationArn: str
    encoderConfigurationArns: Sequence[str]
    recordingConfiguration: Optional[RecordingConfigurationTypeDef] = None
    thumbnailConfigurations: Optional[Sequence[CompositionThumbnailConfigurationUnionTypeDef]] = None


class CreateEncoderConfigurationResponseTypeDef(BaseValidatorModel):
    encoderConfiguration: EncoderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetEncoderConfigurationResponseTypeDef(BaseValidatorModel):
    encoderConfiguration: EncoderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListStorageConfigurationsResponseTypeDef(BaseValidatorModel):
    storageConfigurations: List[StorageConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateStorageConfigurationResponseTypeDef(BaseValidatorModel):
    storageConfiguration: StorageConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetStorageConfigurationResponseTypeDef(BaseValidatorModel):
    storageConfiguration: StorageConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DestinationConfigurationOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    channel: Optional[ChannelDestinationConfigurationTypeDef] = None
    s3: Optional[S3DestinationConfigurationOutputTypeDef] = None


class CreateStageResponseTypeDef(BaseValidatorModel):
    stage: StageTypeDef
    participantTokens: List[ParticipantTokenTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetStageResponseTypeDef(BaseValidatorModel):
    stage: StageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateStageResponseTypeDef(BaseValidatorModel):
    stage: StageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AutoParticipantRecordingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateStageRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    participantTokenConfigurations: Optional[Sequence[ParticipantTokenConfigurationTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    autoParticipantRecordingConfiguration: Optional[ AutoParticipantRecordingConfigurationUnionTypeDef ] = None


class UpdateStageRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    autoParticipantRecordingConfiguration: Optional[ AutoParticipantRecordingConfigurationUnionTypeDef ] = None


class S3DestinationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class DestinationConfigurationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    channel: Optional[ChannelDestinationConfigurationTypeDef] = None
    s3: Optional[S3DestinationConfigurationUnionTypeDef] = None


class DestinationTypeDef(BaseValidatorModel):
    pass


class CompositionTypeDef(BaseValidatorModel):
    arn: str
    stageArn: str
    state: CompositionStateType
    layout: LayoutConfigurationTypeDef
    destinations: List[DestinationTypeDef]
    tags: Optional[Dict[str, str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class GetCompositionResponseTypeDef(BaseValidatorModel):
    composition: CompositionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartCompositionResponseTypeDef(BaseValidatorModel):
    composition: CompositionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DestinationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class StartCompositionRequestTypeDef(BaseValidatorModel):
    stageArn: str
    destinations: Sequence[DestinationConfigurationUnionTypeDef]
    idempotencyToken: Optional[str] = None
    layout: Optional[LayoutConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


