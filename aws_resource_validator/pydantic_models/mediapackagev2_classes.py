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
from aws_resource_validator.pydantic_models.mediapackagev2_constants import *

class CancelHarvestJobRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestJobName: str
    ETag: Optional[str] = None


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


class CreateChannelGroupRequestTypeDef(BaseValidatorModel):
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


class InputSwitchConfigurationTypeDef(BaseValidatorModel):
    MQCSInputSwitching: Optional[bool] = None


class OutputHeaderConfigurationTypeDef(BaseValidatorModel):
    PublishMQCS: Optional[bool] = None


class IngestEndpointTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Url: Optional[str] = None


class DashUtcTimingTypeDef(BaseValidatorModel):
    TimingMode: Optional[DashUtcTimingModeType] = None
    TimingSource: Optional[str] = None


class ScteDashTypeDef(BaseValidatorModel):
    AdMarkerDash: Optional[AdMarkerDashType] = None


class HarvesterScheduleConfigurationOutputTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime


class ScteHlsTypeDef(BaseValidatorModel):
    AdMarkerHls: Optional[Literal["DATERANGE"]] = None


class StartTagTypeDef(BaseValidatorModel):
    TimeOffset: float
    Precise: Optional[bool] = None


class ForceEndpointErrorConfigurationOutputTypeDef(BaseValidatorModel):
    EndpointErrorConditions: Optional[List[EndpointErrorConditionType]] = None


class DeleteChannelGroupRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str


class DeleteChannelPolicyRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str


class DeleteChannelRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str


class DeleteOriginEndpointPolicyRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str


class DeleteOriginEndpointRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str


class S3DestinationConfigTypeDef(BaseValidatorModel):
    BucketName: str
    DestinationPath: str


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
    ClipStartTime: Optional[datetime] = None


class ForceEndpointErrorConfigurationTypeDef(BaseValidatorModel):
    EndpointErrorConditions: Optional[Sequence[EndpointErrorConditionType]] = None


class GetChannelGroupRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str


class GetChannelPolicyRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str


class GetChannelRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str


class GetHarvestJobRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestJobName: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetOriginEndpointPolicyRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str


class GetOriginEndpointRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str


class HarvestedDashManifestTypeDef(BaseValidatorModel):
    ManifestName: str


class HarvestedHlsManifestTypeDef(BaseValidatorModel):
    ManifestName: str


class HarvestedLowLatencyHlsManifestTypeDef(BaseValidatorModel):
    ManifestName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChannelGroupsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDashManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    Url: Optional[str] = None


class ListHarvestJobsRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: Optional[str] = None
    OriginEndpointName: Optional[str] = None
    Status: Optional[HarvestJobStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListHlsManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    Url: Optional[str] = None


class ListLowLatencyHlsManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    Url: Optional[str] = None


class ListOriginEndpointsRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PutChannelPolicyRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    Policy: str


class PutOriginEndpointPolicyRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Policy: str


class ScteOutputTypeDef(BaseValidatorModel):
    ScteFilter: Optional[List[ScteFilterType]] = None


class ScteTypeDef(BaseValidatorModel):
    ScteFilter: Optional[Sequence[ScteFilterType]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateChannelGroupRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
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


class CreateChannelRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    ClientToken: Optional[str] = None
    InputType: Optional[InputTypeType] = None
    Description: Optional[str] = None
    InputSwitchConfiguration: Optional[InputSwitchConfigurationTypeDef] = None
    OutputHeaderConfiguration: Optional[OutputHeaderConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateChannelRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    ETag: Optional[str] = None
    Description: Optional[str] = None
    InputSwitchConfiguration: Optional[InputSwitchConfigurationTypeDef] = None
    OutputHeaderConfiguration: Optional[OutputHeaderConfigurationTypeDef] = None


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
    InputSwitchConfiguration: InputSwitchConfigurationTypeDef
    OutputHeaderConfiguration: OutputHeaderConfigurationTypeDef
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
    InputSwitchConfiguration: InputSwitchConfigurationTypeDef
    OutputHeaderConfiguration: OutputHeaderConfigurationTypeDef
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
    InputSwitchConfiguration: InputSwitchConfigurationTypeDef
    OutputHeaderConfiguration: OutputHeaderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DestinationTypeDef(BaseValidatorModel):
    S3Destination: S3DestinationConfigTypeDef


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
    StartTag: Optional[StartTagTypeDef] = None


class GetLowLatencyHlsManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    Url: str
    ChildManifestName: Optional[str] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    ScteHls: Optional[ScteHlsTypeDef] = None
    FilterConfiguration: Optional[FilterConfigurationOutputTypeDef] = None
    StartTag: Optional[StartTagTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class FilterConfigurationTypeDef(BaseValidatorModel):
    ManifestFilter: Optional[str] = None
    Start: Optional[TimestampTypeDef] = None
    End: Optional[TimestampTypeDef] = None
    TimeDelaySeconds: Optional[int] = None
    ClipStartTime: Optional[TimestampTypeDef] = None


class HarvesterScheduleConfigurationTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef


class GetHarvestJobRequestWaitTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestJobName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class HarvestedManifestsOutputTypeDef(BaseValidatorModel):
    HlsManifests: Optional[List[HarvestedHlsManifestTypeDef]] = None
    DashManifests: Optional[List[HarvestedDashManifestTypeDef]] = None
    LowLatencyHlsManifests: Optional[List[HarvestedLowLatencyHlsManifestTypeDef]] = None


class HarvestedManifestsTypeDef(BaseValidatorModel):
    HlsManifests: Optional[Sequence[HarvestedHlsManifestTypeDef]] = None
    DashManifests: Optional[Sequence[HarvestedDashManifestTypeDef]] = None
    LowLatencyHlsManifests: Optional[Sequence[HarvestedLowLatencyHlsManifestTypeDef]] = None


class ListChannelGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListChannelsRequestPaginateTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHarvestJobsRequestPaginateTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: Optional[str] = None
    OriginEndpointName: Optional[str] = None
    Status: Optional[HarvestJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOriginEndpointsRequestPaginateTypeDef(BaseValidatorModel):
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
    ForceEndpointErrorConfiguration: Optional[ForceEndpointErrorConfigurationOutputTypeDef] = None


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


class CreateHarvestJobResponseTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Destination: DestinationTypeDef
    HarvestJobName: str
    HarvestedManifests: HarvestedManifestsOutputTypeDef
    Description: str
    ScheduleConfiguration: HarvesterScheduleConfigurationOutputTypeDef
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Status: HarvestJobStatusType
    ErrorMessage: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetHarvestJobResponseTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Destination: DestinationTypeDef
    HarvestJobName: str
    HarvestedManifests: HarvestedManifestsOutputTypeDef
    Description: str
    ScheduleConfiguration: HarvesterScheduleConfigurationOutputTypeDef
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Status: HarvestJobStatusType
    ErrorMessage: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class HarvestJobTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Destination: DestinationTypeDef
    HarvestJobName: str
    HarvestedManifests: HarvestedManifestsOutputTypeDef
    ScheduleConfiguration: HarvesterScheduleConfigurationOutputTypeDef
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Status: HarvestJobStatusType
    Description: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ETag: Optional[str] = None


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


class FilterConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDashManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    ManifestWindowSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationUnionTypeDef] = None
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
    StartTag: Optional[StartTagTypeDef] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationUnionTypeDef] = None


class CreateLowLatencyHlsManifestConfigurationTypeDef(BaseValidatorModel):
    ManifestName: str
    ChildManifestName: Optional[str] = None
    ScteHls: Optional[ScteHlsTypeDef] = None
    StartTag: Optional[StartTagTypeDef] = None
    ManifestWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    FilterConfiguration: Optional[FilterConfigurationUnionTypeDef] = None


class ListHarvestJobsResponseTypeDef(BaseValidatorModel):
    Items: List[HarvestJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class HarvestedManifestsUnionTypeDef(BaseValidatorModel):
    pass


class HarvesterScheduleConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateHarvestJobRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestedManifests: HarvestedManifestsUnionTypeDef
    ScheduleConfiguration: HarvesterScheduleConfigurationUnionTypeDef
    Destination: DestinationTypeDef
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    HarvestJobName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


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


class ForceEndpointErrorConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class SegmentUnionTypeDef(BaseValidatorModel):
    pass


class CreateOriginEndpointRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: Optional[SegmentUnionTypeDef] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    StartoverWindowSeconds: Optional[int] = None
    HlsManifests: Optional[Sequence[CreateHlsManifestConfigurationTypeDef]] = None
    LowLatencyHlsManifests: Optional[Sequence[CreateLowLatencyHlsManifestConfigurationTypeDef]] = None
    DashManifests: Optional[Sequence[CreateDashManifestConfigurationTypeDef]] = None
    ForceEndpointErrorConfiguration: Optional[ForceEndpointErrorConfigurationUnionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateOriginEndpointRequestTypeDef(BaseValidatorModel):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: Optional[SegmentUnionTypeDef] = None
    Description: Optional[str] = None
    StartoverWindowSeconds: Optional[int] = None
    HlsManifests: Optional[Sequence[CreateHlsManifestConfigurationTypeDef]] = None
    LowLatencyHlsManifests: Optional[Sequence[CreateLowLatencyHlsManifestConfigurationTypeDef]] = None
    DashManifests: Optional[Sequence[CreateDashManifestConfigurationTypeDef]] = None
    ForceEndpointErrorConfiguration: Optional[ForceEndpointErrorConfigurationUnionTypeDef] = None
    ETag: Optional[str] = None


