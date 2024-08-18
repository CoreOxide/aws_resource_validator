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
from aws_resource_validator.pydantic_models.ivs_realtime_constants import *

class AutoParticipantRecordingConfigurationOutputTypeDef(BaseValidatorModel):
    storageConfigurationArn: str
    mediaTypes: Optional[List[ParticipantRecordingMediaTypeType]] = None

class AutoParticipantRecordingConfigurationTypeDef(BaseValidatorModel):
    storageConfigurationArn: str
    mediaTypes: Optional[Sequence[ParticipantRecordingMediaTypeType]] = None

class ChannelDestinationConfigurationTypeDef(BaseValidatorModel):
    channelArn: str
    encoderConfigurationArn: Optional[str] = None

class DestinationSummaryTypeDef(BaseValidatorModel):
    id: str
    state: DestinationStateType
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

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

class CreateParticipantTokenRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteEncoderConfigurationRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeletePublicKeyRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteStageRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteStorageConfigurationRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class S3DetailTypeDef(BaseValidatorModel):
    recordingPrefix: str

class DisconnectParticipantRequestRequestTypeDef(BaseValidatorModel):
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

class GetCompositionRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetEncoderConfigurationRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetParticipantRequestRequestTypeDef(BaseValidatorModel):
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

class GetPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class PublicKeyTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    publicKeyMaterial: Optional[str] = None
    fingerprint: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class GetStageRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetStageSessionRequestRequestTypeDef(BaseValidatorModel):
    stageArn: str
    sessionId: str

class StageSessionTypeDef(BaseValidatorModel):
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class GetStorageConfigurationRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GridConfigurationTypeDef(BaseValidatorModel):
    featuredParticipantAttribute: Optional[str] = None
    omitStoppedVideo: Optional[bool] = None
    videoAspectRatio: Optional[VideoAspectRatioType] = None
    videoFillMode: Optional[VideoFillModeType] = None
    gridGap: Optional[int] = None

class ImportPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    publicKeyMaterial: str
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

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

class ListCompositionsRequestRequestTypeDef(BaseValidatorModel):
    filterByStageArn: Optional[str] = None
    filterByEncoderConfigurationArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListEncoderConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListParticipantEventsRequestRequestTypeDef(BaseValidatorModel):
    stageArn: str
    sessionId: str
    participantId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListParticipantsRequestRequestTypeDef(BaseValidatorModel):
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

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListPublicKeysRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PublicKeySummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListStageSessionsRequestRequestTypeDef(BaseValidatorModel):
    stageArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class StageSessionSummaryTypeDef(BaseValidatorModel):
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class ListStagesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class StageSummaryTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    activeSessionId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListStorageConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class RecordingConfigurationTypeDef(BaseValidatorModel):
    format: Optional[Literal["HLS"]] = None

class StageEndpointsTypeDef(BaseValidatorModel):
    events: Optional[str] = None
    whip: Optional[str] = None

class StopCompositionRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateStageRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    autoParticipantRecordingConfiguration: Optional[       AutoParticipantRecordingConfigurationTypeDef     ] = None

class CompositionSummaryTypeDef(BaseValidatorModel):
    arn: str
    stageArn: str
    destinations: List[DestinationSummaryTypeDef]
    state: CompositionStateType
    tags: Optional[Dict[str, str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class CreateEncoderConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class CreateParticipantTokenResponseTypeDef(BaseValidatorModel):
    participantToken: ParticipantTokenTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStageRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    participantTokenConfigurations: Optional[       Sequence[ParticipantTokenConfigurationTypeDef]     ] = None
    tags: Optional[Mapping[str, str]] = None
    autoParticipantRecordingConfiguration: Optional[       AutoParticipantRecordingConfigurationTypeDef     ] = None

class CreateStorageConfigurationRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListParticipantEventsResponseTypeDef(BaseValidatorModel):
    events: List[EventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class LayoutConfigurationTypeDef(BaseValidatorModel):
    grid: Optional[GridConfigurationTypeDef] = None
    pip: Optional[PipConfigurationTypeDef] = None

class ListParticipantsResponseTypeDef(BaseValidatorModel):
    participants: List[ParticipantSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPublicKeysRequestListPublicKeysPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPublicKeysResponseTypeDef(BaseValidatorModel):
    publicKeys: List[PublicKeySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStageSessionsResponseTypeDef(BaseValidatorModel):
    stageSessions: List[StageSessionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStagesResponseTypeDef(BaseValidatorModel):
    stages: List[StageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class S3DestinationConfigurationOutputTypeDef(BaseValidatorModel):
    storageConfigurationArn: str
    encoderConfigurationArns: List[str]
    recordingConfiguration: Optional[RecordingConfigurationTypeDef] = None

class S3DestinationConfigurationTypeDef(BaseValidatorModel):
    storageConfigurationArn: str
    encoderConfigurationArns: Sequence[str]
    recordingConfiguration: Optional[RecordingConfigurationTypeDef] = None

class StageTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    activeSessionId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    autoParticipantRecordingConfiguration: Optional[       AutoParticipantRecordingConfigurationOutputTypeDef     ] = None
    endpoints: Optional[StageEndpointsTypeDef] = None

class ListCompositionsResponseTypeDef(BaseValidatorModel):
    compositions: List[CompositionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEncoderConfigurationResponseTypeDef(BaseValidatorModel):
    encoderConfiguration: EncoderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEncoderConfigurationResponseTypeDef(BaseValidatorModel):
    encoderConfiguration: EncoderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStorageConfigurationsResponseTypeDef(BaseValidatorModel):
    storageConfigurations: List[StorageConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class DestinationConfigurationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    channel: Optional[ChannelDestinationConfigurationTypeDef] = None
    s3: Optional[S3DestinationConfigurationTypeDef] = None

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

class DestinationTypeDef(BaseValidatorModel):
    id: str
    state: DestinationStateType
    configuration: DestinationConfigurationOutputTypeDef
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    detail: Optional[DestinationDetailTypeDef] = None

class CompositionTypeDef(BaseValidatorModel):
    arn: str
    stageArn: str
    state: CompositionStateType
    layout: LayoutConfigurationTypeDef
    destinations: List[DestinationTypeDef]
    tags: Optional[Dict[str, str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class StartCompositionRequestRequestTypeDef(BaseValidatorModel):
    stageArn: str
    destinations: Sequence[DestinationConfigurationUnionTypeDef]
    idempotencyToken: Optional[str] = None
    layout: Optional[LayoutConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class GetCompositionResponseTypeDef(BaseValidatorModel):
    composition: CompositionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCompositionResponseTypeDef(BaseValidatorModel):
    composition: CompositionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

