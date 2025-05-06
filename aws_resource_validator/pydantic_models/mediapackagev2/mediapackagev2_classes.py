from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mediapackagev2.mediapackagev2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CancelHarvestJobRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestJobName: str
    ETag: Optional[str] = None


class ChannelGroupListConfiguration(BaseValidatorModel):
    ChannelGroupName: str
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: Optional[str] = None


class ChannelListConfiguration(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: Optional[str] = None
    InputType: Optional[InputTypeType] = None


class CreateChannelGroupRequest(BaseValidatorModel):
    ChannelGroupName: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class InputSwitchConfiguration(BaseValidatorModel):
    MQCSInputSwitching: Optional[bool] = None


class OutputHeaderConfiguration(BaseValidatorModel):
    PublishMQCS: Optional[bool] = None


class IngestEndpoint(BaseValidatorModel):
    Id: Optional[str] = None
    Url: Optional[str] = None


class DashUtcTiming(BaseValidatorModel):
    TimingMode: Optional[DashUtcTimingModeType] = None
    TimingSource: Optional[str] = None


class ScteDash(BaseValidatorModel):
    AdMarkerDash: Optional[AdMarkerDashType] = None


class HarvesterScheduleConfigurationOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime


class ScteHls(BaseValidatorModel):
    AdMarkerHls: Optional[Literal['DATERANGE']] = None


class StartTag(BaseValidatorModel):
    TimeOffset: float
    Precise: Optional[bool] = None


class ForceEndpointErrorConfigurationOutput(BaseValidatorModel):
    EndpointErrorConditions: Optional[List[EndpointErrorConditionType]] = None


class DeleteChannelGroupRequest(BaseValidatorModel):
    ChannelGroupName: str


class DeleteChannelPolicyRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str


class DeleteChannelRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str


class DeleteOriginEndpointPolicyRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str


class DeleteOriginEndpointRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str


class S3DestinationConfig(BaseValidatorModel):
    BucketName: str
    DestinationPath: str


class EncryptionContractConfiguration(BaseValidatorModel):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType


class EncryptionMethod(BaseValidatorModel):
    TsEncryptionMethod: Optional[TsEncryptionMethodType] = None
    CmafEncryptionMethod: Optional[CmafEncryptionMethodType] = None


class FilterConfigurationOutput(BaseValidatorModel):
    ManifestFilter: Optional[str] = None
    Start: Optional[datetime] = None
    End: Optional[datetime] = None
    TimeDelaySeconds: Optional[int] = None
    ClipStartTime: Optional[datetime] = None

Timestamp = Union[datetime, str]


class ForceEndpointErrorConfiguration(BaseValidatorModel):
    EndpointErrorConditions: Optional[List[EndpointErrorConditionType]] = None


class GetChannelGroupRequest(BaseValidatorModel):
    ChannelGroupName: str


class GetChannelPolicyRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str


class GetChannelRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str


class GetHarvestJobRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestJobName: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetOriginEndpointPolicyRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str


class GetOriginEndpointRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str


class HarvestedDashManifest(BaseValidatorModel):
    ManifestName: str


class HarvestedHlsManifest(BaseValidatorModel):
    ManifestName: str


class HarvestedLowLatencyHlsManifest(BaseValidatorModel):
    ManifestName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChannelGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsRequest(BaseValidatorModel):
    ChannelGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDashManifestConfiguration(BaseValidatorModel):
    ManifestName: str
    Url: Optional[str] = None


class ListHarvestJobsRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: Optional[str] = None
    OriginEndpointName: Optional[str] = None
    Status: Optional[HarvestJobStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListHlsManifestConfiguration(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    Url: Optional[str] = None


class ListLowLatencyHlsManifestConfiguration(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    Url: Optional[str] = None


class ListOriginEndpointsRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class PutChannelPolicyRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    Policy: str


class PutOriginEndpointPolicyRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Policy: str


class ScteOutput(BaseValidatorModel):
    ScteFilter: Optional[List[ScteFilterType]] = None


class Scte(BaseValidatorModel):
    ScteFilter: Optional[List[ScteFilterType]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateChannelGroupRequest(BaseValidatorModel):
    ChannelGroupName: str
    ETag: Optional[str] = None
    Description: Optional[str] = None


class CreateChannelGroupResponse(BaseValidatorModel):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    ETag: str
    Description: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetChannelGroupResponse(BaseValidatorModel):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetChannelPolicyResponse(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetOriginEndpointPolicyResponse(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Policy: str
    ResponseMetadata: ResponseMetadata


class ListChannelGroupsResponse(BaseValidatorModel):
    Items: List[ChannelGroupListConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListChannelsResponse(BaseValidatorModel):
    Items: List[ChannelListConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateChannelGroupResponse(BaseValidatorModel):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateChannelRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    ClientToken: Optional[str] = None
    InputType: Optional[InputTypeType] = None
    Description: Optional[str] = None
    InputSwitchConfiguration: Optional[InputSwitchConfiguration] = None
    OutputHeaderConfiguration: Optional[OutputHeaderConfiguration] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateChannelRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    ETag: Optional[str] = None
    Description: Optional[str] = None
    InputSwitchConfiguration: Optional[InputSwitchConfiguration] = None
    OutputHeaderConfiguration: Optional[OutputHeaderConfiguration] = None


class CreateChannelResponse(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    IngestEndpoints: List[IngestEndpoint]
    InputType: InputTypeType
    ETag: str
    Tags: Dict[str, str]
    InputSwitchConfiguration: InputSwitchConfiguration
    OutputHeaderConfiguration: OutputHeaderConfiguration
    ResponseMetadata: ResponseMetadata


class GetChannelResponse(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    IngestEndpoints: List[IngestEndpoint]
    InputType: InputTypeType
    ETag: str
    Tags: Dict[str, str]
    InputSwitchConfiguration: InputSwitchConfiguration
    OutputHeaderConfiguration: OutputHeaderConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateChannelResponse(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    IngestEndpoints: List[IngestEndpoint]
    InputType: InputTypeType
    ETag: str
    Tags: Dict[str, str]
    InputSwitchConfiguration: InputSwitchConfiguration
    OutputHeaderConfiguration: OutputHeaderConfiguration
    ResponseMetadata: ResponseMetadata


class Destination(BaseValidatorModel):
    S3Destination: S3DestinationConfig


class SpekeKeyProviderOutput(BaseValidatorModel):
    EncryptionContractConfiguration: EncryptionContractConfiguration
    ResourceId: str
    DrmSystems: List[DrmSystemType]
    RoleArn: str
    Url: str


class SpekeKeyProvider(BaseValidatorModel):
    EncryptionContractConfiguration: EncryptionContractConfiguration
    ResourceId: str
    DrmSystems: List[DrmSystemType]
    RoleArn: str
    Url: str


class GetDashManifestConfiguration(BaseValidatorModel):
    ManifestName: str
    Url: str
    ManifestWindowSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationOutput] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[Literal['NUMBER_WITH_TIMELINE']] = None
    PeriodTriggers: Optional[List[DashPeriodTriggerType]] = None
    ScteDash: Optional[ScteDash] = None
    DrmSignaling: Optional[DashDrmSignalingType] = None
    UtcTiming: Optional[DashUtcTiming] = None


class GetHlsManifestConfiguration(BaseValidatorModel):
    ManifestName: str
    Url: str
    ChildManifestName: Optional[str] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    ScteHls: Optional[ScteHls] = None
    FilterConfiguration: Optional[FilterConfigurationOutput] = None
    StartTag: Optional[StartTag] = None


class GetLowLatencyHlsManifestConfiguration(BaseValidatorModel):
    ManifestName: str
    Url: str
    ChildManifestName: Optional[str] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    ScteHls: Optional[ScteHls] = None
    FilterConfiguration: Optional[FilterConfigurationOutput] = None
    StartTag: Optional[StartTag] = None


class FilterConfiguration(BaseValidatorModel):
    ManifestFilter: Optional[str] = None
    Start: Optional[Timestamp] = None
    End: Optional[Timestamp] = None
    TimeDelaySeconds: Optional[int] = None
    ClipStartTime: Optional[Timestamp] = None


class HarvesterScheduleConfiguration(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp

ForceEndpointErrorConfigurationUnion = Union[ForceEndpointErrorConfiguration, ForceEndpointErrorConfigurationOutput]


class GetHarvestJobRequestWait(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestJobName: str
    WaiterConfig: Optional[WaiterConfig] = None


class HarvestedManifestsOutput(BaseValidatorModel):
    HlsManifests: Optional[List[HarvestedHlsManifest]] = None
    DashManifests: Optional[List[HarvestedDashManifest]] = None
    LowLatencyHlsManifests: Optional[List[HarvestedLowLatencyHlsManifest]] = None


class HarvestedManifests(BaseValidatorModel):
    HlsManifests: Optional[List[HarvestedHlsManifest]] = None
    DashManifests: Optional[List[HarvestedDashManifest]] = None
    LowLatencyHlsManifests: Optional[List[HarvestedLowLatencyHlsManifest]] = None


class ListChannelGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListChannelsRequestPaginate(BaseValidatorModel):
    ChannelGroupName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHarvestJobsRequestPaginate(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: Optional[str] = None
    OriginEndpointName: Optional[str] = None
    Status: Optional[HarvestJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOriginEndpointsRequestPaginate(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class OriginEndpointListConfiguration(BaseValidatorModel):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    ModifiedAt: Optional[datetime] = None
    HlsManifests: Optional[List[ListHlsManifestConfiguration]] = None
    LowLatencyHlsManifests: Optional[List[ListLowLatencyHlsManifestConfiguration]] = None
    DashManifests: Optional[List[ListDashManifestConfiguration]] = None
    ForceEndpointErrorConfiguration: Optional[ForceEndpointErrorConfigurationOutput] = None


class EncryptionOutput(BaseValidatorModel):
    EncryptionMethod: EncryptionMethod
    SpekeKeyProvider: SpekeKeyProviderOutput
    ConstantInitializationVector: Optional[str] = None
    KeyRotationIntervalSeconds: Optional[int] = None


class Encryption(BaseValidatorModel):
    EncryptionMethod: EncryptionMethod
    SpekeKeyProvider: SpekeKeyProvider
    ConstantInitializationVector: Optional[str] = None
    KeyRotationIntervalSeconds: Optional[int] = None

FilterConfigurationUnion = Union[FilterConfiguration, FilterConfigurationOutput]

HarvesterScheduleConfigurationUnion = Union[HarvesterScheduleConfiguration, HarvesterScheduleConfigurationOutput]


class CreateHarvestJobResponse(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Destination: Destination
    HarvestJobName: str
    HarvestedManifests: HarvestedManifestsOutput
    Description: str
    ScheduleConfiguration: HarvesterScheduleConfigurationOutput
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Status: HarvestJobStatusType
    ErrorMessage: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetHarvestJobResponse(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Destination: Destination
    HarvestJobName: str
    HarvestedManifests: HarvestedManifestsOutput
    Description: str
    ScheduleConfiguration: HarvesterScheduleConfigurationOutput
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Status: HarvestJobStatusType
    ErrorMessage: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class HarvestJob(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Destination: Destination
    HarvestJobName: str
    HarvestedManifests: HarvestedManifestsOutput
    ScheduleConfiguration: HarvesterScheduleConfigurationOutput
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Status: HarvestJobStatusType
    Description: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ETag: Optional[str] = None

HarvestedManifestsUnion = Union[HarvestedManifests, HarvestedManifestsOutput]


class ListOriginEndpointsResponse(BaseValidatorModel):
    Items: List[OriginEndpointListConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SegmentOutput(BaseValidatorModel):
    SegmentDurationSeconds: Optional[int] = None
    SegmentName: Optional[str] = None
    TsUseAudioRenditionGroup: Optional[bool] = None
    IncludeIframeOnlyStreams: Optional[bool] = None
    TsIncludeDvbSubtitles: Optional[bool] = None
    Scte: Optional[ScteOutput] = None
    Encryption: Optional[EncryptionOutput] = None


class Segment(BaseValidatorModel):
    SegmentDurationSeconds: Optional[int] = None
    SegmentName: Optional[str] = None
    TsUseAudioRenditionGroup: Optional[bool] = None
    IncludeIframeOnlyStreams: Optional[bool] = None
    TsIncludeDvbSubtitles: Optional[bool] = None
    Scte: Optional[Scte] = None
    Encryption: Optional[Encryption] = None


class CreateDashManifestConfiguration(BaseValidatorModel):
    ManifestName: str
    ManifestWindowSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationUnion] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[Literal['NUMBER_WITH_TIMELINE']] = None
    PeriodTriggers: Optional[List[DashPeriodTriggerType]] = None
    ScteDash: Optional[ScteDash] = None
    DrmSignaling: Optional[DashDrmSignalingType] = None
    UtcTiming: Optional[DashUtcTiming] = None


class CreateHlsManifestConfiguration(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    ScteHls: Optional[ScteHls] = None
    StartTag: Optional[StartTag] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationUnion] = None


class CreateLowLatencyHlsManifestConfiguration(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    ScteHls: Optional[ScteHls] = None
    StartTag: Optional[StartTag] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationUnion] = None


class ListHarvestJobsResponse(BaseValidatorModel):
    Items: List[HarvestJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateHarvestJobRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestedManifests: HarvestedManifestsUnion
    ScheduleConfiguration: HarvesterScheduleConfigurationUnion
    Destination: Destination
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    HarvestJobName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class CreateOriginEndpointResponse(BaseValidatorModel):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: SegmentOutput
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    StartoverWindowSeconds: int
    HlsManifests: List[GetHlsManifestConfiguration]
    LowLatencyHlsManifests: List[GetLowLatencyHlsManifestConfiguration]
    DashManifests: List[GetDashManifestConfiguration]
    ForceEndpointErrorConfiguration: ForceEndpointErrorConfigurationOutput
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetOriginEndpointResponse(BaseValidatorModel):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: SegmentOutput
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    StartoverWindowSeconds: int
    HlsManifests: List[GetHlsManifestConfiguration]
    LowLatencyHlsManifests: List[GetLowLatencyHlsManifestConfiguration]
    DashManifests: List[GetDashManifestConfiguration]
    ForceEndpointErrorConfiguration: ForceEndpointErrorConfigurationOutput
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateOriginEndpointResponse(BaseValidatorModel):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: SegmentOutput
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    StartoverWindowSeconds: int
    HlsManifests: List[GetHlsManifestConfiguration]
    LowLatencyHlsManifests: List[GetLowLatencyHlsManifestConfiguration]
    ForceEndpointErrorConfiguration: ForceEndpointErrorConfigurationOutput
    ETag: str
    Tags: Dict[str, str]
    DashManifests: List[GetDashManifestConfiguration]
    ResponseMetadata: ResponseMetadata

SegmentUnion = Union[Segment, SegmentOutput]


class CreateOriginEndpointRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: Optional[SegmentUnion] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    StartoverWindowSeconds: Optional[int] = None
    HlsManifests: Optional[List[CreateHlsManifestConfiguration]] = None
    LowLatencyHlsManifests: Optional[List[CreateLowLatencyHlsManifestConfiguration]] = None
    DashManifests: Optional[List[CreateDashManifestConfiguration]] = None
    ForceEndpointErrorConfiguration: Optional[ForceEndpointErrorConfigurationUnion] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateOriginEndpointRequest(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: Optional[SegmentUnion] = None
    Description: Optional[str] = None
    StartoverWindowSeconds: Optional[int] = None
    HlsManifests: Optional[List[CreateHlsManifestConfiguration]] = None
    LowLatencyHlsManifests: Optional[List[CreateLowLatencyHlsManifestConfiguration]] = None
    DashManifests: Optional[List[CreateDashManifestConfiguration]] = None
    ForceEndpointErrorConfiguration: Optional[ForceEndpointErrorConfigurationUnion] = None
    ETag: Optional[str] = None