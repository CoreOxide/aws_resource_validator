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
from aws_resource_validator.pydantic_models.ivs_realtime_constants import *

class AutoParticipantRecordingConfigurationOutputTypeDef(BaseModel):
    storageConfigurationArn: str
    mediaTypes: Optional[List[ParticipantRecordingMediaTypeType]] = None

class AutoParticipantRecordingConfigurationTypeDef(BaseModel):
    storageConfigurationArn: str
    mediaTypes: Optional[Sequence[ParticipantRecordingMediaTypeType]] = None

class ChannelDestinationConfigurationTypeDef(BaseModel):
    channelArn: str
    encoderConfigurationArn: Optional[str] = None

class DestinationSummaryTypeDef(BaseModel):
    id: str
    state: DestinationStateType
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class VideoTypeDef(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    framerate: Optional[float] = None
    bitrate: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateParticipantTokenRequestRequestTypeDef(BaseModel):
    stageArn: str
    duration: Optional[int] = None
    userId: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    capabilities: Optional[Sequence[ParticipantTokenCapabilityType]] = None

class ParticipantTokenTypeDef(BaseModel):
    participantId: Optional[str] = None
    token: Optional[str] = None
    userId: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    duration: Optional[int] = None
    capabilities: Optional[List[ParticipantTokenCapabilityType]] = None
    expirationTime: Optional[datetime] = None

class ParticipantTokenConfigurationTypeDef(BaseModel):
    duration: Optional[int] = None
    userId: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    capabilities: Optional[Sequence[ParticipantTokenCapabilityType]] = None

class S3StorageConfigurationTypeDef(BaseModel):
    bucketName: str

class DeleteEncoderConfigurationRequestRequestTypeDef(BaseModel):
    arn: str

class DeletePublicKeyRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteStageRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteStorageConfigurationRequestRequestTypeDef(BaseModel):
    arn: str

class S3DetailTypeDef(BaseModel):
    recordingPrefix: str

class DisconnectParticipantRequestRequestTypeDef(BaseModel):
    stageArn: str
    participantId: str
    reason: Optional[str] = None

class EncoderConfigurationSummaryTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class EventTypeDef(BaseModel):
    name: Optional[EventNameType] = None
    participantId: Optional[str] = None
    eventTime: Optional[datetime] = None
    remoteParticipantId: Optional[str] = None
    errorCode: Optional[EventErrorCodeType] = None

class GetCompositionRequestRequestTypeDef(BaseModel):
    arn: str

class GetEncoderConfigurationRequestRequestTypeDef(BaseModel):
    arn: str

class GetParticipantRequestRequestTypeDef(BaseModel):
    stageArn: str
    sessionId: str
    participantId: str

class ParticipantTypeDef(BaseModel):
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

class GetPublicKeyRequestRequestTypeDef(BaseModel):
    arn: str

class PublicKeyTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    publicKeyMaterial: Optional[str] = None
    fingerprint: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class GetStageRequestRequestTypeDef(BaseModel):
    arn: str

class GetStageSessionRequestRequestTypeDef(BaseModel):
    stageArn: str
    sessionId: str

class StageSessionTypeDef(BaseModel):
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class GetStorageConfigurationRequestRequestTypeDef(BaseModel):
    arn: str

class GridConfigurationTypeDef(BaseModel):
    featuredParticipantAttribute: Optional[str] = None
    omitStoppedVideo: Optional[bool] = None
    videoAspectRatio: Optional[VideoAspectRatioType] = None
    videoFillMode: Optional[VideoFillModeType] = None
    gridGap: Optional[int] = None

class ImportPublicKeyRequestRequestTypeDef(BaseModel):
    publicKeyMaterial: str
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class PipConfigurationTypeDef(BaseModel):
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

class ListCompositionsRequestRequestTypeDef(BaseModel):
    filterByStageArn: Optional[str] = None
    filterByEncoderConfigurationArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListEncoderConfigurationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListParticipantEventsRequestRequestTypeDef(BaseModel):
    stageArn: str
    sessionId: str
    participantId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListParticipantsRequestRequestTypeDef(BaseModel):
    stageArn: str
    sessionId: str
    filterByUserId: Optional[str] = None
    filterByPublished: Optional[bool] = None
    filterByState: Optional[ParticipantStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filterByRecordingState: Optional[ParticipantRecordingFilterByRecordingStateType] = None

class ParticipantSummaryTypeDef(BaseModel):
    participantId: Optional[str] = None
    userId: Optional[str] = None
    state: Optional[ParticipantStateType] = None
    firstJoinTime: Optional[datetime] = None
    published: Optional[bool] = None
    recordingState: Optional[ParticipantRecordingStateType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListPublicKeysRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PublicKeySummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListStageSessionsRequestRequestTypeDef(BaseModel):
    stageArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class StageSessionSummaryTypeDef(BaseModel):
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class ListStagesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class StageSummaryTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    activeSessionId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListStorageConfigurationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class RecordingConfigurationTypeDef(BaseModel):
    format: Optional[Literal["HLS"]] = None

class StageEndpointsTypeDef(BaseModel):
    events: Optional[str] = None
    whip: Optional[str] = None

class StopCompositionRequestRequestTypeDef(BaseModel):
    arn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateStageRequestRequestTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    autoParticipantRecordingConfiguration: Optional[       AutoParticipantRecordingConfigurationTypeDef     ] = None

class CompositionSummaryTypeDef(BaseModel):
    arn: str
    stageArn: str
    destinations: List[DestinationSummaryTypeDef]
    state: CompositionStateType
    tags: Optional[Dict[str, str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class CreateEncoderConfigurationRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    video: Optional[VideoTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class EncoderConfigurationTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    video: Optional[VideoTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateParticipantTokenResponseTypeDef(BaseModel):
    participantToken: ParticipantTokenTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStageRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    participantTokenConfigurations: Optional[       Sequence[ParticipantTokenConfigurationTypeDef]     ] = None
    tags: Optional[Mapping[str, str]] = None
    autoParticipantRecordingConfiguration: Optional[       AutoParticipantRecordingConfigurationTypeDef     ] = None

class CreateStorageConfigurationRequestRequestTypeDef(BaseModel):
    s3: S3StorageConfigurationTypeDef
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class StorageConfigurationSummaryTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    s3: Optional[S3StorageConfigurationTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class StorageConfigurationTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    s3: Optional[S3StorageConfigurationTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class DestinationDetailTypeDef(BaseModel):
    s3: Optional[S3DetailTypeDef] = None

class ListEncoderConfigurationsResponseTypeDef(BaseModel):
    encoderConfigurations: List[EncoderConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListParticipantEventsResponseTypeDef(BaseModel):
    events: List[EventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetParticipantResponseTypeDef(BaseModel):
    participant: ParticipantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicKeyResponseTypeDef(BaseModel):
    publicKey: PublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportPublicKeyResponseTypeDef(BaseModel):
    publicKey: PublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStageSessionResponseTypeDef(BaseModel):
    stageSession: StageSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LayoutConfigurationTypeDef(BaseModel):
    grid: Optional[GridConfigurationTypeDef] = None
    pip: Optional[PipConfigurationTypeDef] = None

class ListParticipantsResponseTypeDef(BaseModel):
    participants: List[ParticipantSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPublicKeysRequestListPublicKeysPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPublicKeysResponseTypeDef(BaseModel):
    publicKeys: List[PublicKeySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStageSessionsResponseTypeDef(BaseModel):
    stageSessions: List[StageSessionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStagesResponseTypeDef(BaseModel):
    stages: List[StageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class S3DestinationConfigurationOutputTypeDef(BaseModel):
    storageConfigurationArn: str
    encoderConfigurationArns: List[str]
    recordingConfiguration: Optional[RecordingConfigurationTypeDef] = None

class S3DestinationConfigurationTypeDef(BaseModel):
    storageConfigurationArn: str
    encoderConfigurationArns: Sequence[str]
    recordingConfiguration: Optional[RecordingConfigurationTypeDef] = None

class StageTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    activeSessionId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    autoParticipantRecordingConfiguration: Optional[       AutoParticipantRecordingConfigurationOutputTypeDef     ] = None
    endpoints: Optional[StageEndpointsTypeDef] = None

class ListCompositionsResponseTypeDef(BaseModel):
    compositions: List[CompositionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEncoderConfigurationResponseTypeDef(BaseModel):
    encoderConfiguration: EncoderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEncoderConfigurationResponseTypeDef(BaseModel):
    encoderConfiguration: EncoderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStorageConfigurationsResponseTypeDef(BaseModel):
    storageConfigurations: List[StorageConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorageConfigurationResponseTypeDef(BaseModel):
    storageConfiguration: StorageConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStorageConfigurationResponseTypeDef(BaseModel):
    storageConfiguration: StorageConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationConfigurationOutputTypeDef(BaseModel):
    name: Optional[str] = None
    channel: Optional[ChannelDestinationConfigurationTypeDef] = None
    s3: Optional[S3DestinationConfigurationOutputTypeDef] = None

class DestinationConfigurationTypeDef(BaseModel):
    name: Optional[str] = None
    channel: Optional[ChannelDestinationConfigurationTypeDef] = None
    s3: Optional[S3DestinationConfigurationTypeDef] = None

class CreateStageResponseTypeDef(BaseModel):
    stage: StageTypeDef
    participantTokens: List[ParticipantTokenTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetStageResponseTypeDef(BaseModel):
    stage: StageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStageResponseTypeDef(BaseModel):
    stage: StageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationTypeDef(BaseModel):
    id: str
    state: DestinationStateType
    configuration: DestinationConfigurationOutputTypeDef
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    detail: Optional[DestinationDetailTypeDef] = None

class CompositionTypeDef(BaseModel):
    arn: str
    stageArn: str
    state: CompositionStateType
    layout: LayoutConfigurationTypeDef
    destinations: List[DestinationTypeDef]
    tags: Optional[Dict[str, str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class StartCompositionRequestRequestTypeDef(BaseModel):
    stageArn: str
    destinations: Sequence[DestinationConfigurationUnionTypeDef]
    idempotencyToken: Optional[str] = None
    layout: Optional[LayoutConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class GetCompositionResponseTypeDef(BaseModel):
    composition: CompositionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCompositionResponseTypeDef(BaseModel):
    composition: CompositionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

