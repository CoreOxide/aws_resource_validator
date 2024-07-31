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
from aws_resource_validator.pydantic_models.mediapackagev2_constants import *

class ChannelGroupListConfigurationTypeDef(BaseModel):
    ChannelGroupName: str
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: Optional[str] = None

class ChannelListConfigurationTypeDef(BaseModel):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: Optional[str] = None
    InputType: Optional[InputTypeType] = None

class CreateChannelGroupRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateChannelRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    ClientToken: Optional[str] = None
    InputType: Optional[InputTypeType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class IngestEndpointTypeDef(BaseModel):
    Id: Optional[str] = None
    Url: Optional[str] = None

class DashUtcTimingTypeDef(BaseModel):
    TimingMode: Optional[DashUtcTimingModeType] = None
    TimingSource: Optional[str] = None

class ScteDashTypeDef(BaseModel):
    AdMarkerDash: Optional[AdMarkerDashType] = None

class ScteHlsTypeDef(BaseModel):
    AdMarkerHls: Optional[Literal["DATERANGE"]] = None

class ForceEndpointErrorConfigurationTypeDef(BaseModel):
    EndpointErrorConditions: Optional[Sequence[EndpointErrorConditionType]] = None

class ForceEndpointErrorConfigurationOutputTypeDef(BaseModel):
    EndpointErrorConditions: Optional[List[EndpointErrorConditionType]] = None

class DeleteChannelGroupRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str

class DeleteChannelPolicyRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str

class DeleteChannelRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str

class DeleteOriginEndpointPolicyRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class DeleteOriginEndpointRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class EncryptionContractConfigurationTypeDef(BaseModel):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType

class EncryptionMethodTypeDef(BaseModel):
    TsEncryptionMethod: Optional[TsEncryptionMethodType] = None
    CmafEncryptionMethod: Optional[CmafEncryptionMethodType] = None

class FilterConfigurationOutputTypeDef(BaseModel):
    ManifestFilter: Optional[str] = None
    Start: Optional[datetime] = None
    End: Optional[datetime] = None
    TimeDelaySeconds: Optional[int] = None

class ForceEndpointErrorConfigurationExtraOutputTypeDef(BaseModel):
    EndpointErrorConditions: Optional[List[EndpointErrorConditionType]] = None

class GetChannelGroupRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str

class GetChannelPolicyRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str

class GetChannelRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str

class GetOriginEndpointPolicyRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class GetOriginEndpointRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChannelGroupsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDashManifestConfigurationTypeDef(BaseModel):
    ManifestName: str
    Url: Optional[str] = None

class ListHlsManifestConfigurationTypeDef(BaseModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    Url: Optional[str] = None

class ListLowLatencyHlsManifestConfigurationTypeDef(BaseModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    Url: Optional[str] = None

class ListOriginEndpointsRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class PutChannelPolicyRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    Policy: str

class PutOriginEndpointPolicyRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Policy: str

class ScteOutputTypeDef(BaseModel):
    ScteFilter: Optional[List[ScteFilterType]] = None

class ScteTypeDef(BaseModel):
    ScteFilter: Optional[Sequence[ScteFilterType]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateChannelGroupRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ETag: Optional[str] = None
    Description: Optional[str] = None

class UpdateChannelRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    ETag: Optional[str] = None
    Description: Optional[str] = None

class CreateChannelGroupResponseTypeDef(BaseModel):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    ETag: str
    Description: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelGroupResponseTypeDef(BaseModel):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelPolicyResponseTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOriginEndpointPolicyResponseTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelGroupsResponseTypeDef(BaseModel):
    Items: List[ChannelGroupListConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListChannelsResponseTypeDef(BaseModel):
    Items: List[ChannelListConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelGroupResponseTypeDef(BaseModel):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(BaseModel):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    IngestEndpoints: List[IngestEndpointTypeDef]
    InputType: InputTypeType
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelResponseTypeDef(BaseModel):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    IngestEndpoints: List[IngestEndpointTypeDef]
    InputType: InputTypeType
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseModel):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    IngestEndpoints: List[IngestEndpointTypeDef]
    InputType: InputTypeType
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SpekeKeyProviderOutputTypeDef(BaseModel):
    EncryptionContractConfiguration: EncryptionContractConfigurationTypeDef
    ResourceId: str
    DrmSystems: List[DrmSystemType]
    RoleArn: str
    Url: str

class SpekeKeyProviderTypeDef(BaseModel):
    EncryptionContractConfiguration: EncryptionContractConfigurationTypeDef
    ResourceId: str
    DrmSystems: Sequence[DrmSystemType]
    RoleArn: str
    Url: str

class GetDashManifestConfigurationTypeDef(BaseModel):
    ManifestName: str
    Url: str
    ManifestWindowSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationOutputTypeDef] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[Literal["NUMBER_WITH_TIMELINE"]] = None
    PeriodTriggers: Optional[List[DashPeriodTriggerType]] = None
    ScteDash: Optional[ScteDashTypeDef] = None
    DrmSignaling: Optional[DashDrmSignalingType] = None
    UtcTiming: Optional[DashUtcTimingTypeDef] = None

class GetHlsManifestConfigurationTypeDef(BaseModel):
    ManifestName: str
    Url: str
    ChildManifestName: Optional[str] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    ScteHls: Optional[ScteHlsTypeDef] = None
    FilterConfiguration: Optional[FilterConfigurationOutputTypeDef] = None

class GetLowLatencyHlsManifestConfigurationTypeDef(BaseModel):
    ManifestName: str
    Url: str
    ChildManifestName: Optional[str] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    ScteHls: Optional[ScteHlsTypeDef] = None
    FilterConfiguration: Optional[FilterConfigurationOutputTypeDef] = None

class FilterConfigurationTypeDef(BaseModel):
    ManifestFilter: Optional[str] = None
    Start: Optional[TimestampTypeDef] = None
    End: Optional[TimestampTypeDef] = None
    TimeDelaySeconds: Optional[int] = None

class ListChannelGroupsRequestListChannelGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseModel):
    ChannelGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class OriginEndpointListConfigurationTypeDef(BaseModel):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    ModifiedAt: Optional[datetime] = None
    HlsManifests: Optional[List[ListHlsManifestConfigurationTypeDef]] = None
    LowLatencyHlsManifests: Optional[List[ListLowLatencyHlsManifestConfigurationTypeDef]] = None
    DashManifests: Optional[List[ListDashManifestConfigurationTypeDef]] = None
    ForceEndpointErrorConfiguration: Optional[       ForceEndpointErrorConfigurationOutputTypeDef     ] = None

class EncryptionOutputTypeDef(BaseModel):
    EncryptionMethod: EncryptionMethodTypeDef
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef
    ConstantInitializationVector: Optional[str] = None
    KeyRotationIntervalSeconds: Optional[int] = None

class EncryptionTypeDef(BaseModel):
    EncryptionMethod: EncryptionMethodTypeDef
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: Optional[str] = None
    KeyRotationIntervalSeconds: Optional[int] = None

class CreateDashManifestConfigurationTypeDef(BaseModel):
    ManifestName: str
    ManifestWindowSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationTypeDef] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[Literal["NUMBER_WITH_TIMELINE"]] = None
    PeriodTriggers: Optional[Sequence[DashPeriodTriggerType]] = None
    ScteDash: Optional[ScteDashTypeDef] = None
    DrmSignaling: Optional[DashDrmSignalingType] = None
    UtcTiming: Optional[DashUtcTimingTypeDef] = None

class CreateHlsManifestConfigurationTypeDef(BaseModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    ScteHls: Optional[ScteHlsTypeDef] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationTypeDef] = None

class CreateLowLatencyHlsManifestConfigurationTypeDef(BaseModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    ScteHls: Optional[ScteHlsTypeDef] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationTypeDef] = None

class ListOriginEndpointsResponseTypeDef(BaseModel):
    Items: List[OriginEndpointListConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SegmentOutputTypeDef(BaseModel):
    SegmentDurationSeconds: Optional[int] = None
    SegmentName: Optional[str] = None
    TsUseAudioRenditionGroup: Optional[bool] = None
    IncludeIframeOnlyStreams: Optional[bool] = None
    TsIncludeDvbSubtitles: Optional[bool] = None
    Scte: Optional[ScteOutputTypeDef] = None
    Encryption: Optional[EncryptionOutputTypeDef] = None

class SegmentTypeDef(BaseModel):
    SegmentDurationSeconds: Optional[int] = None
    SegmentName: Optional[str] = None
    TsUseAudioRenditionGroup: Optional[bool] = None
    IncludeIframeOnlyStreams: Optional[bool] = None
    TsIncludeDvbSubtitles: Optional[bool] = None
    Scte: Optional[ScteTypeDef] = None
    Encryption: Optional[EncryptionTypeDef] = None

class CreateOriginEndpointResponseTypeDef(BaseModel):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: SegmentOutputTypeDef
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    StartoverWindowSeconds: int
    HlsManifests: List[GetHlsManifestConfigurationTypeDef]
    LowLatencyHlsManifests: List[GetLowLatencyHlsManifestConfigurationTypeDef]
    DashManifests: List[GetDashManifestConfigurationTypeDef]
    ForceEndpointErrorConfiguration: ForceEndpointErrorConfigurationOutputTypeDef
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetOriginEndpointResponseTypeDef(BaseModel):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: SegmentOutputTypeDef
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    StartoverWindowSeconds: int
    HlsManifests: List[GetHlsManifestConfigurationTypeDef]
    LowLatencyHlsManifests: List[GetLowLatencyHlsManifestConfigurationTypeDef]
    DashManifests: List[GetDashManifestConfigurationTypeDef]
    ForceEndpointErrorConfiguration: ForceEndpointErrorConfigurationOutputTypeDef
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOriginEndpointResponseTypeDef(BaseModel):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: SegmentOutputTypeDef
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    StartoverWindowSeconds: int
    HlsManifests: List[GetHlsManifestConfigurationTypeDef]
    LowLatencyHlsManifests: List[GetLowLatencyHlsManifestConfigurationTypeDef]
    ForceEndpointErrorConfiguration: ForceEndpointErrorConfigurationOutputTypeDef
    ETag: str
    Tags: Dict[str, str]
    DashManifests: List[GetDashManifestConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOriginEndpointRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: Optional[SegmentTypeDef] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    StartoverWindowSeconds: Optional[int] = None
    HlsManifests: Optional[Sequence[CreateHlsManifestConfigurationTypeDef]] = None
    LowLatencyHlsManifests: Optional[       Sequence[CreateLowLatencyHlsManifestConfigurationTypeDef]     ] = None
    DashManifests: Optional[Sequence[CreateDashManifestConfigurationTypeDef]] = None
    ForceEndpointErrorConfiguration: Optional[ForceEndpointErrorConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateOriginEndpointRequestRequestTypeDef(BaseModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: Optional[SegmentTypeDef] = None
    Description: Optional[str] = None
    StartoverWindowSeconds: Optional[int] = None
    HlsManifests: Optional[Sequence[CreateHlsManifestConfigurationTypeDef]] = None
    LowLatencyHlsManifests: Optional[       Sequence[CreateLowLatencyHlsManifestConfigurationTypeDef]     ] = None
    DashManifests: Optional[Sequence[CreateDashManifestConfigurationTypeDef]] = None
    ForceEndpointErrorConfiguration: Optional[ForceEndpointErrorConfigurationTypeDef] = None
    ETag: Optional[str] = None

