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
from aws_resource_validator.pydantic_models.mediapackagev2_constants import *

class ChannelGroupListConfigurationTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: Optional[str] = None

class ChannelListConfigurationTypeDef(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: Optional[str] = None
    InputType: Optional[InputTypeType] = None

class CreateChannelGroupRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    ClientToken: Optional[str] = None
    InputType: Optional[InputTypeType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class IngestEndpointTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Url: Optional[str] = None

class DashUtcTimingTypeDef(BaseValidatorModel):
    TimingMode: Optional[DashUtcTimingModeType] = None
    TimingSource: Optional[str] = None

class ScteDashTypeDef(BaseValidatorModel):
    AdMarkerDash: Optional[AdMarkerDashType] = None

class ScteHlsTypeDef(BaseValidatorModel):
    AdMarkerHls: Optional[Literal["DATERANGE"]] = None

class ForceEndpointErrorConfigurationTypeDef(BaseValidatorModel):
    EndpointErrorConditions: Optional[Sequence[EndpointErrorConditionType]] = None

class ForceEndpointErrorConfigurationOutputTypeDef(BaseValidatorModel):
    EndpointErrorConditions: Optional[List[EndpointErrorConditionType]] = None

class DeleteChannelGroupRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str

class DeleteChannelPolicyRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str

class DeleteChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str

class DeleteOriginEndpointPolicyRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class DeleteOriginEndpointRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class EncryptionContractConfigurationTypeDef(BaseValidatorModel):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType

class EncryptionMethodTypeDef(BaseValidatorModel):
    TsEncryptionMethod: Optional[TsEncryptionMethodType] = None
    CmafEncryptionMethod: Optional[CmafEncryptionMethodType] = None

class FilterConfigurationOutputTypeDef(BaseValidatorModel):
    ManifestFilter: Optional[str] = None
    Start: Optional[datetime] = None
    End: Optional[datetime] = None
    TimeDelaySeconds: Optional[int] = None

class ForceEndpointErrorConfigurationExtraOutputTypeDef(BaseValidatorModel):
    EndpointErrorConditions: Optional[List[EndpointErrorConditionType]] = None

class GetChannelGroupRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str

class GetChannelPolicyRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str

class GetChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str

class GetOriginEndpointPolicyRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class GetOriginEndpointRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChannelGroupsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDashManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    Url: Optional[str] = None

class ListHlsManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    Url: Optional[str] = None

class ListLowLatencyHlsManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    Url: Optional[str] = None

class ListOriginEndpointsRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class PutChannelPolicyRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    Policy: str

class PutOriginEndpointPolicyRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Policy: str

class ScteOutputTypeDef(BaseValidatorModel):
    ScteFilter: Optional[List[ScteFilterType]] = None

class ScteTypeDef(BaseValidatorModel):
    ScteFilter: Optional[Sequence[ScteFilterType]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateChannelGroupRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ETag: Optional[str] = None
    Description: Optional[str] = None

class UpdateChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    ETag: Optional[str] = None
    Description: Optional[str] = None

class CreateChannelGroupResponseTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    ETag: str
    Description: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelGroupResponseTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelPolicyResponseTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOriginEndpointPolicyResponseTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelGroupsResponseTypeDef(BaseValidatorModel):
    Items: List[ChannelGroupListConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListChannelsResponseTypeDef(BaseValidatorModel):
    Items: List[ChannelListConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelGroupResponseTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(BaseValidatorModel):
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

class GetChannelResponseTypeDef(BaseValidatorModel):
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

class UpdateChannelResponseTypeDef(BaseValidatorModel):
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

class SpekeKeyProviderOutputTypeDef(BaseValidatorModel):
    EncryptionContractConfiguration: EncryptionContractConfigurationTypeDef
    ResourceId: str
    DrmSystems: List[DrmSystemType]
    RoleArn: str
    Url: str

class SpekeKeyProviderTypeDef(BaseValidatorModel):
    EncryptionContractConfiguration: EncryptionContractConfigurationTypeDef
    ResourceId: str
    DrmSystems: Sequence[DrmSystemType]
    RoleArn: str
    Url: str

class GetDashManifestConfigurationTypeDef(BaseValidatorModel):
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

class GetHlsManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    Url: str
    ChildManifestName: Optional[str] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    ScteHls: Optional[ScteHlsTypeDef] = None
    FilterConfiguration: Optional[FilterConfigurationOutputTypeDef] = None

class GetLowLatencyHlsManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    Url: str
    ChildManifestName: Optional[str] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    ScteHls: Optional[ScteHlsTypeDef] = None
    FilterConfiguration: Optional[FilterConfigurationOutputTypeDef] = None

class FilterConfigurationTypeDef(BaseValidatorModel):
    ManifestFilter: Optional[str] = None
    Start: Optional[TimestampTypeDef] = None
    End: Optional[TimestampTypeDef] = None
    TimeDelaySeconds: Optional[int] = None

class ListChannelGroupsRequestListChannelGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class OriginEndpointListConfigurationTypeDef(BaseValidatorModel):
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

class EncryptionOutputTypeDef(BaseValidatorModel):
    EncryptionMethod: EncryptionMethodTypeDef
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef
    ConstantInitializationVector: Optional[str] = None
    KeyRotationIntervalSeconds: Optional[int] = None

class EncryptionTypeDef(BaseValidatorModel):
    EncryptionMethod: EncryptionMethodTypeDef
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: Optional[str] = None
    KeyRotationIntervalSeconds: Optional[int] = None

class CreateDashManifestConfigurationTypeDef(BaseValidatorModel):
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

class CreateHlsManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    ScteHls: Optional[ScteHlsTypeDef] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationTypeDef] = None

class CreateLowLatencyHlsManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    ScteHls: Optional[ScteHlsTypeDef] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationTypeDef] = None

class ListOriginEndpointsResponseTypeDef(BaseValidatorModel):
    Items: List[OriginEndpointListConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SegmentOutputTypeDef(BaseValidatorModel):
    SegmentDurationSeconds: Optional[int] = None
    SegmentName: Optional[str] = None
    TsUseAudioRenditionGroup: Optional[bool] = None
    IncludeIframeOnlyStreams: Optional[bool] = None
    TsIncludeDvbSubtitles: Optional[bool] = None
    Scte: Optional[ScteOutputTypeDef] = None
    Encryption: Optional[EncryptionOutputTypeDef] = None

class SegmentTypeDef(BaseValidatorModel):
    SegmentDurationSeconds: Optional[int] = None
    SegmentName: Optional[str] = None
    TsUseAudioRenditionGroup: Optional[bool] = None
    IncludeIframeOnlyStreams: Optional[bool] = None
    TsIncludeDvbSubtitles: Optional[bool] = None
    Scte: Optional[ScteTypeDef] = None
    Encryption: Optional[EncryptionTypeDef] = None

class CreateOriginEndpointResponseTypeDef(BaseValidatorModel):
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

class GetOriginEndpointResponseTypeDef(BaseValidatorModel):
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

class UpdateOriginEndpointResponseTypeDef(BaseValidatorModel):
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

class CreateOriginEndpointRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateOriginEndpointRequestRequestTypeDef(BaseValidatorModel):
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

