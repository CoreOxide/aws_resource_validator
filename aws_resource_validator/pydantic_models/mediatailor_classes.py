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
from aws_resource_validator.pydantic_models.mediatailor_constants import *

class SecretsManagerAccessTokenConfigurationTypeDef(BaseModel):
    HeaderName: Optional[str] = None
    SecretArn: Optional[str] = None
    SecretStringKey: Optional[str] = None

class AdBreakOpportunityTypeDef(BaseModel):
    OffsetMillis: int

class KeyValuePairTypeDef(BaseModel):
    Key: str
    Value: str

class SlateSourceTypeDef(BaseModel):
    SourceLocationName: Optional[str] = None
    VodSourceName: Optional[str] = None

class SpliceInsertMessageTypeDef(BaseModel):
    AvailNum: Optional[int] = None
    AvailsExpected: Optional[int] = None
    SpliceEventId: Optional[int] = None
    UniqueProgramId: Optional[int] = None

class AdMarkerPassthroughTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class AlertTypeDef(BaseModel):
    AlertCode: str
    AlertMessage: str
    LastModifiedTime: datetime
    RelatedResourceArns: List[str]
    ResourceArn: str
    Category: Optional[AlertCategoryType] = None

class ClipRangeTypeDef(BaseModel):
    EndOffsetMillis: Optional[int] = None
    StartOffsetMillis: Optional[int] = None

class AvailMatchingCriteriaTypeDef(BaseModel):
    DynamicVariable: str
    Operator: Literal["EQUALS"]

class AvailSuppressionTypeDef(BaseModel):
    FillPolicy: Optional[FillPolicyType] = None
    Mode: Optional[ModeType] = None
    Value: Optional[str] = None

class BumperTypeDef(BaseModel):
    EndUrl: Optional[str] = None
    StartUrl: Optional[str] = None

class CdnConfigurationTypeDef(BaseModel):
    AdSegmentUrlPrefix: Optional[str] = None
    ContentSegmentUrlPrefix: Optional[str] = None

class LogConfigurationForChannelTypeDef(BaseModel):
    LogTypes: Optional[List[Literal["AS_RUN"]]] = None

class ConfigureLogsForChannelRequestRequestTypeDef(BaseModel):
    ChannelName: str
    LogTypes: Sequence[Literal["AS_RUN"]]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConfigureLogsForPlaybackConfigurationRequestRequestTypeDef(BaseModel):
    PercentEnabled: int
    PlaybackConfigurationName: str

class TimeShiftConfigurationTypeDef(BaseModel):
    MaxTimeDelaySeconds: int

class HttpPackageConfigurationTypeDef(BaseModel):
    Path: str
    SourceGroup: str
    Type: TypeType

class DefaultSegmentDeliveryConfigurationTypeDef(BaseModel):
    BaseUrl: Optional[str] = None

class HttpConfigurationTypeDef(BaseModel):
    BaseUrl: str

class SegmentDeliveryConfigurationTypeDef(BaseModel):
    BaseUrl: Optional[str] = None
    Name: Optional[str] = None

class DashConfigurationForPutTypeDef(BaseModel):
    MpdLocation: Optional[str] = None
    OriginManifestType: Optional[OriginManifestTypeType] = None

class DashConfigurationTypeDef(BaseModel):
    ManifestEndpointPrefix: Optional[str] = None
    MpdLocation: Optional[str] = None
    OriginManifestType: Optional[OriginManifestTypeType] = None

class DashPlaylistSettingsTypeDef(BaseModel):
    ManifestWindowSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None

class DeleteChannelPolicyRequestRequestTypeDef(BaseModel):
    ChannelName: str

class DeleteChannelRequestRequestTypeDef(BaseModel):
    ChannelName: str

class DeleteLiveSourceRequestRequestTypeDef(BaseModel):
    LiveSourceName: str
    SourceLocationName: str

class DeletePlaybackConfigurationRequestRequestTypeDef(BaseModel):
    Name: str

class DeletePrefetchScheduleRequestRequestTypeDef(BaseModel):
    Name: str
    PlaybackConfigurationName: str

class DeleteProgramRequestRequestTypeDef(BaseModel):
    ChannelName: str
    ProgramName: str

class DeleteSourceLocationRequestRequestTypeDef(BaseModel):
    SourceLocationName: str

class DeleteVodSourceRequestRequestTypeDef(BaseModel):
    SourceLocationName: str
    VodSourceName: str

class DescribeChannelRequestRequestTypeDef(BaseModel):
    ChannelName: str

class DescribeLiveSourceRequestRequestTypeDef(BaseModel):
    LiveSourceName: str
    SourceLocationName: str

class DescribeProgramRequestRequestTypeDef(BaseModel):
    ChannelName: str
    ProgramName: str

class DescribeSourceLocationRequestRequestTypeDef(BaseModel):
    SourceLocationName: str

class DescribeVodSourceRequestRequestTypeDef(BaseModel):
    SourceLocationName: str
    VodSourceName: str

class GetChannelPolicyRequestRequestTypeDef(BaseModel):
    ChannelName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetChannelScheduleRequestRequestTypeDef(BaseModel):
    ChannelName: str
    Audience: Optional[str] = None
    DurationMinutes: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetPlaybackConfigurationRequestRequestTypeDef(BaseModel):
    Name: str

class HlsConfigurationTypeDef(BaseModel):
    ManifestEndpointPrefix: Optional[str] = None

class LivePreRollConfigurationTypeDef(BaseModel):
    AdDecisionServerUrl: Optional[str] = None
    MaxDurationSeconds: Optional[int] = None

class LogConfigurationTypeDef(BaseModel):
    PercentEnabled: int

class GetPrefetchScheduleRequestRequestTypeDef(BaseModel):
    Name: str
    PlaybackConfigurationName: str

class HlsPlaylistSettingsPaginatorTypeDef(BaseModel):
    AdMarkupType: Optional[List[AdMarkupTypeType]] = None
    ManifestWindowSeconds: Optional[int] = None

class HlsPlaylistSettingsTypeDef(BaseModel):
    AdMarkupType: Optional[Sequence[AdMarkupTypeType]] = None
    ManifestWindowSeconds: Optional[int] = None

class ListAlertsRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLiveSourcesRequestRequestTypeDef(BaseModel):
    SourceLocationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPlaybackConfigurationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPrefetchSchedulesRequestRequestTypeDef(BaseModel):
    PlaybackConfigurationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StreamId: Optional[str] = None

class ListSourceLocationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListVodSourcesRequestRequestTypeDef(BaseModel):
    SourceLocationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PrefetchRetrievalPaginatorTypeDef(BaseModel):
    EndTime: datetime
    DynamicVariables: Optional[Dict[str, str]] = None
    StartTime: Optional[datetime] = None

class PutChannelPolicyRequestRequestTypeDef(BaseModel):
    ChannelName: str
    Policy: str

class ScheduleAdBreakTypeDef(BaseModel):
    ApproximateDurationSeconds: Optional[int] = None
    ApproximateStartTime: Optional[datetime] = None
    SourceLocationName: Optional[str] = None
    VodSourceName: Optional[str] = None

class TransitionTypeDef(BaseModel):
    RelativePosition: RelativePositionType
    Type: str
    DurationMillis: Optional[int] = None
    RelativeProgram: Optional[str] = None
    ScheduledStartTimeMillis: Optional[int] = None

class SegmentationDescriptorTypeDef(BaseModel):
    SegmentNum: Optional[int] = None
    SegmentationEventId: Optional[int] = None
    SegmentationTypeId: Optional[int] = None
    SegmentationUpid: Optional[str] = None
    SegmentationUpidType: Optional[int] = None
    SegmentsExpected: Optional[int] = None
    SubSegmentNum: Optional[int] = None
    SubSegmentsExpected: Optional[int] = None

class StartChannelRequestRequestTypeDef(BaseModel):
    ChannelName: str

class StopChannelRequestRequestTypeDef(BaseModel):
    ChannelName: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateProgramTransitionTypeDef(BaseModel):
    DurationMillis: Optional[int] = None
    ScheduledStartTimeMillis: Optional[int] = None

class AccessConfigurationTypeDef(BaseModel):
    AccessType: Optional[AccessTypeType] = None
    SecretsManagerAccessTokenConfiguration: Optional[       SecretsManagerAccessTokenConfigurationTypeDef     ] = None

class ManifestProcessingRulesTypeDef(BaseModel):
    AdMarkerPassthrough: Optional[AdMarkerPassthroughTypeDef] = None

class PrefetchConsumptionPaginatorTypeDef(BaseModel):
    EndTime: datetime
    AvailMatchingCriteria: Optional[List[AvailMatchingCriteriaTypeDef]] = None
    StartTime: Optional[datetime] = None

class ConfigureLogsForChannelResponseTypeDef(BaseModel):
    ChannelName: str
    LogTypes: List[Literal["AS_RUN"]]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigureLogsForPlaybackConfigurationResponseTypeDef(BaseModel):
    PercentEnabled: int
    PlaybackConfigurationName: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelPolicyResponseTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAlertsResponseTypeDef(BaseModel):
    Items: List[AlertTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLiveSourceRequestRequestTypeDef(BaseModel):
    HttpPackageConfigurations: Sequence[HttpPackageConfigurationTypeDef]
    LiveSourceName: str
    SourceLocationName: str
    Tags: Optional[Mapping[str, str]] = None

class CreateLiveSourceResponseTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    LiveSourceName: str
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVodSourceRequestRequestTypeDef(BaseModel):
    HttpPackageConfigurations: Sequence[HttpPackageConfigurationTypeDef]
    SourceLocationName: str
    VodSourceName: str
    Tags: Optional[Mapping[str, str]] = None

class CreateVodSourceResponseTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLiveSourceResponseTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    LiveSourceName: str
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVodSourceResponseTypeDef(BaseModel):
    AdBreakOpportunities: List[AdBreakOpportunityTypeDef]
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class LiveSourceTypeDef(BaseModel):
    Arn: str
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LiveSourceName: str
    SourceLocationName: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class UpdateLiveSourceRequestRequestTypeDef(BaseModel):
    HttpPackageConfigurations: Sequence[HttpPackageConfigurationTypeDef]
    LiveSourceName: str
    SourceLocationName: str

class UpdateLiveSourceResponseTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    LiveSourceName: str
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVodSourceRequestRequestTypeDef(BaseModel):
    HttpPackageConfigurations: Sequence[HttpPackageConfigurationTypeDef]
    SourceLocationName: str
    VodSourceName: str

class UpdateVodSourceResponseTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class VodSourceTypeDef(BaseModel):
    Arn: str
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    SourceLocationName: str
    VodSourceName: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class GetChannelScheduleRequestGetChannelSchedulePaginateTypeDef(BaseModel):
    ChannelName: str
    Audience: Optional[str] = None
    DurationMinutes: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAlertsRequestListAlertsPaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLiveSourcesRequestListLiveSourcesPaginateTypeDef(BaseModel):
    SourceLocationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlaybackConfigurationsRequestListPlaybackConfigurationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrefetchSchedulesRequestListPrefetchSchedulesPaginateTypeDef(BaseModel):
    PlaybackConfigurationName: str
    StreamId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSourceLocationsRequestListSourceLocationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVodSourcesRequestListVodSourcesPaginateTypeDef(BaseModel):
    SourceLocationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ResponseOutputItemPaginatorTypeDef(BaseModel):
    ManifestName: str
    PlaybackUrl: str
    SourceGroup: str
    DashPlaylistSettings: Optional[DashPlaylistSettingsTypeDef] = None
    HlsPlaylistSettings: Optional[HlsPlaylistSettingsPaginatorTypeDef] = None

class RequestOutputItemTypeDef(BaseModel):
    ManifestName: str
    SourceGroup: str
    DashPlaylistSettings: Optional[DashPlaylistSettingsTypeDef] = None
    HlsPlaylistSettings: Optional[HlsPlaylistSettingsTypeDef] = None

class ResponseOutputItemTypeDef(BaseModel):
    ManifestName: str
    PlaybackUrl: str
    SourceGroup: str
    DashPlaylistSettings: Optional[DashPlaylistSettingsTypeDef] = None
    HlsPlaylistSettings: Optional[HlsPlaylistSettingsTypeDef] = None

class PrefetchConsumptionTypeDef(BaseModel):
    EndTime: TimestampTypeDef
    AvailMatchingCriteria: Optional[Sequence[AvailMatchingCriteriaTypeDef]] = None
    StartTime: Optional[TimestampTypeDef] = None

class PrefetchRetrievalTypeDef(BaseModel):
    EndTime: TimestampTypeDef
    DynamicVariables: Optional[Mapping[str, str]] = None
    StartTime: Optional[TimestampTypeDef] = None

class ScheduleEntryTypeDef(BaseModel):
    Arn: str
    ChannelName: str
    ProgramName: str
    SourceLocationName: str
    ApproximateDurationSeconds: Optional[int] = None
    ApproximateStartTime: Optional[datetime] = None
    Audiences: Optional[List[str]] = None
    LiveSourceName: Optional[str] = None
    ScheduleAdBreaks: Optional[List[ScheduleAdBreakTypeDef]] = None
    ScheduleEntryType: Optional[ScheduleEntryTypeType] = None
    VodSourceName: Optional[str] = None

class ScheduleConfigurationTypeDef(BaseModel):
    Transition: TransitionTypeDef
    ClipRange: Optional[ClipRangeTypeDef] = None

class TimeSignalMessageTypeDef(BaseModel):
    SegmentationDescriptors: Optional[Sequence[SegmentationDescriptorTypeDef]] = None

class UpdateProgramScheduleConfigurationTypeDef(BaseModel):
    ClipRange: Optional[ClipRangeTypeDef] = None
    Transition: Optional[UpdateProgramTransitionTypeDef] = None

class CreateSourceLocationRequestRequestTypeDef(BaseModel):
    HttpConfiguration: HttpConfigurationTypeDef
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfigurationTypeDef] = None
    DefaultSegmentDeliveryConfiguration: Optional[       DefaultSegmentDeliveryConfigurationTypeDef     ] = None
    SegmentDeliveryConfigurations: Optional[Sequence[SegmentDeliveryConfigurationTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateSourceLocationResponseTypeDef(BaseModel):
    AccessConfiguration: AccessConfigurationTypeDef
    Arn: str
    CreationTime: datetime
    DefaultSegmentDeliveryConfiguration: DefaultSegmentDeliveryConfigurationTypeDef
    HttpConfiguration: HttpConfigurationTypeDef
    LastModifiedTime: datetime
    SegmentDeliveryConfigurations: List[SegmentDeliveryConfigurationTypeDef]
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSourceLocationResponseTypeDef(BaseModel):
    AccessConfiguration: AccessConfigurationTypeDef
    Arn: str
    CreationTime: datetime
    DefaultSegmentDeliveryConfiguration: DefaultSegmentDeliveryConfigurationTypeDef
    HttpConfiguration: HttpConfigurationTypeDef
    LastModifiedTime: datetime
    SegmentDeliveryConfigurations: List[SegmentDeliveryConfigurationTypeDef]
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SourceLocationTypeDef(BaseModel):
    Arn: str
    HttpConfiguration: HttpConfigurationTypeDef
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfigurationTypeDef] = None
    CreationTime: Optional[datetime] = None
    DefaultSegmentDeliveryConfiguration: Optional[       DefaultSegmentDeliveryConfigurationTypeDef     ] = None
    LastModifiedTime: Optional[datetime] = None
    SegmentDeliveryConfigurations: Optional[List[SegmentDeliveryConfigurationTypeDef]] = None
    Tags: Optional[Dict[str, str]] = None

class UpdateSourceLocationRequestRequestTypeDef(BaseModel):
    HttpConfiguration: HttpConfigurationTypeDef
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfigurationTypeDef] = None
    DefaultSegmentDeliveryConfiguration: Optional[       DefaultSegmentDeliveryConfigurationTypeDef     ] = None
    SegmentDeliveryConfigurations: Optional[Sequence[SegmentDeliveryConfigurationTypeDef]] = None

class UpdateSourceLocationResponseTypeDef(BaseModel):
    AccessConfiguration: AccessConfigurationTypeDef
    Arn: str
    CreationTime: datetime
    DefaultSegmentDeliveryConfiguration: DefaultSegmentDeliveryConfigurationTypeDef
    HttpConfiguration: HttpConfigurationTypeDef
    LastModifiedTime: datetime
    SegmentDeliveryConfigurations: List[SegmentDeliveryConfigurationTypeDef]
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPlaybackConfigurationResponseTypeDef(BaseModel):
    AdDecisionServerUrl: str
    AvailSuppression: AvailSuppressionTypeDef
    Bumper: BumperTypeDef
    CdnConfiguration: CdnConfigurationTypeDef
    ConfigurationAliases: Dict[str, Dict[str, str]]
    DashConfiguration: DashConfigurationTypeDef
    HlsConfiguration: HlsConfigurationTypeDef
    InsertionMode: InsertionModeType
    LivePreRollConfiguration: LivePreRollConfigurationTypeDef
    LogConfiguration: LogConfigurationTypeDef
    ManifestProcessingRules: ManifestProcessingRulesTypeDef
    Name: str
    PersonalizationThresholdSeconds: int
    PlaybackConfigurationArn: str
    PlaybackEndpointPrefix: str
    SessionInitializationEndpointPrefix: str
    SlateAdUrl: str
    Tags: Dict[str, str]
    TranscodeProfileName: str
    VideoContentSourceUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class PlaybackConfigurationTypeDef(BaseModel):
    AdDecisionServerUrl: Optional[str] = None
    AvailSuppression: Optional[AvailSuppressionTypeDef] = None
    Bumper: Optional[BumperTypeDef] = None
    CdnConfiguration: Optional[CdnConfigurationTypeDef] = None
    ConfigurationAliases: Optional[Dict[str, Dict[str, str]]] = None
    DashConfiguration: Optional[DashConfigurationTypeDef] = None
    HlsConfiguration: Optional[HlsConfigurationTypeDef] = None
    InsertionMode: Optional[InsertionModeType] = None
    LivePreRollConfiguration: Optional[LivePreRollConfigurationTypeDef] = None
    LogConfiguration: Optional[LogConfigurationTypeDef] = None
    ManifestProcessingRules: Optional[ManifestProcessingRulesTypeDef] = None
    Name: Optional[str] = None
    PersonalizationThresholdSeconds: Optional[int] = None
    PlaybackConfigurationArn: Optional[str] = None
    PlaybackEndpointPrefix: Optional[str] = None
    SessionInitializationEndpointPrefix: Optional[str] = None
    SlateAdUrl: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    TranscodeProfileName: Optional[str] = None
    VideoContentSourceUrl: Optional[str] = None

class PutPlaybackConfigurationRequestRequestTypeDef(BaseModel):
    Name: str
    AdDecisionServerUrl: Optional[str] = None
    AvailSuppression: Optional[AvailSuppressionTypeDef] = None
    Bumper: Optional[BumperTypeDef] = None
    CdnConfiguration: Optional[CdnConfigurationTypeDef] = None
    ConfigurationAliases: Optional[Mapping[str, Mapping[str, str]]] = None
    DashConfiguration: Optional[DashConfigurationForPutTypeDef] = None
    InsertionMode: Optional[InsertionModeType] = None
    LivePreRollConfiguration: Optional[LivePreRollConfigurationTypeDef] = None
    ManifestProcessingRules: Optional[ManifestProcessingRulesTypeDef] = None
    PersonalizationThresholdSeconds: Optional[int] = None
    SlateAdUrl: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    TranscodeProfileName: Optional[str] = None
    VideoContentSourceUrl: Optional[str] = None

class PutPlaybackConfigurationResponseTypeDef(BaseModel):
    AdDecisionServerUrl: str
    AvailSuppression: AvailSuppressionTypeDef
    Bumper: BumperTypeDef
    CdnConfiguration: CdnConfigurationTypeDef
    ConfigurationAliases: Dict[str, Dict[str, str]]
    DashConfiguration: DashConfigurationTypeDef
    HlsConfiguration: HlsConfigurationTypeDef
    InsertionMode: InsertionModeType
    LivePreRollConfiguration: LivePreRollConfigurationTypeDef
    LogConfiguration: LogConfigurationTypeDef
    ManifestProcessingRules: ManifestProcessingRulesTypeDef
    Name: str
    PersonalizationThresholdSeconds: int
    PlaybackConfigurationArn: str
    PlaybackEndpointPrefix: str
    SessionInitializationEndpointPrefix: str
    SlateAdUrl: str
    Tags: Dict[str, str]
    TranscodeProfileName: str
    VideoContentSourceUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class PrefetchSchedulePaginatorTypeDef(BaseModel):
    Arn: str
    Consumption: PrefetchConsumptionPaginatorTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalPaginatorTypeDef
    StreamId: Optional[str] = None

class ListLiveSourcesResponseTypeDef(BaseModel):
    Items: List[LiveSourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVodSourcesResponseTypeDef(BaseModel):
    Items: List[VodSourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelPaginatorTypeDef(BaseModel):
    Arn: str
    ChannelName: str
    ChannelState: str
    LogConfiguration: LogConfigurationForChannelTypeDef
    Outputs: List[ResponseOutputItemPaginatorTypeDef]
    PlaybackMode: str
    Tier: str
    Audiences: Optional[List[str]] = None
    CreationTime: Optional[datetime] = None
    FillerSlate: Optional[SlateSourceTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class CreateChannelRequestRequestTypeDef(BaseModel):
    ChannelName: str
    Outputs: Sequence[RequestOutputItemTypeDef]
    PlaybackMode: PlaybackModeType
    Audiences: Optional[Sequence[str]] = None
    FillerSlate: Optional[SlateSourceTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Tier: Optional[TierType] = None
    TimeShiftConfiguration: Optional[TimeShiftConfigurationTypeDef] = None

class UpdateChannelRequestRequestTypeDef(BaseModel):
    ChannelName: str
    Outputs: Sequence[RequestOutputItemTypeDef]
    Audiences: Optional[Sequence[str]] = None
    FillerSlate: Optional[SlateSourceTypeDef] = None
    TimeShiftConfiguration: Optional[TimeShiftConfigurationTypeDef] = None

class ChannelTypeDef(BaseModel):
    Arn: str
    ChannelName: str
    ChannelState: str
    LogConfiguration: LogConfigurationForChannelTypeDef
    Outputs: List[ResponseOutputItemTypeDef]
    PlaybackMode: str
    Tier: str
    Audiences: Optional[List[str]] = None
    CreationTime: Optional[datetime] = None
    FillerSlate: Optional[SlateSourceTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class CreateChannelResponseTypeDef(BaseModel):
    Arn: str
    Audiences: List[str]
    ChannelName: str
    ChannelState: ChannelStateType
    CreationTime: datetime
    FillerSlate: SlateSourceTypeDef
    LastModifiedTime: datetime
    Outputs: List[ResponseOutputItemTypeDef]
    PlaybackMode: str
    Tags: Dict[str, str]
    Tier: str
    TimeShiftConfiguration: TimeShiftConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(BaseModel):
    Arn: str
    Audiences: List[str]
    ChannelName: str
    ChannelState: ChannelStateType
    CreationTime: datetime
    FillerSlate: SlateSourceTypeDef
    LastModifiedTime: datetime
    LogConfiguration: LogConfigurationForChannelTypeDef
    Outputs: List[ResponseOutputItemTypeDef]
    PlaybackMode: str
    Tags: Dict[str, str]
    Tier: str
    TimeShiftConfiguration: TimeShiftConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseModel):
    Arn: str
    Audiences: List[str]
    ChannelName: str
    ChannelState: ChannelStateType
    CreationTime: datetime
    FillerSlate: SlateSourceTypeDef
    LastModifiedTime: datetime
    Outputs: List[ResponseOutputItemTypeDef]
    PlaybackMode: str
    Tags: Dict[str, str]
    Tier: str
    TimeShiftConfiguration: TimeShiftConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePrefetchScheduleRequestRequestTypeDef(BaseModel):
    Consumption: PrefetchConsumptionTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalTypeDef
    StreamId: Optional[str] = None

class CreatePrefetchScheduleResponseTypeDef(BaseModel):
    Arn: str
    Consumption: PrefetchConsumptionTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalTypeDef
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPrefetchScheduleResponseTypeDef(BaseModel):
    Arn: str
    Consumption: PrefetchConsumptionTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalTypeDef
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PrefetchScheduleTypeDef(BaseModel):
    Arn: str
    Consumption: PrefetchConsumptionTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalTypeDef
    StreamId: Optional[str] = None

class GetChannelScheduleResponseTypeDef(BaseModel):
    Items: List[ScheduleEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AdBreakTypeDef(BaseModel):
    OffsetMillis: int
    AdBreakMetadata: Optional[Sequence[KeyValuePairTypeDef]] = None
    MessageType: Optional[MessageTypeType] = None
    Slate: Optional[SlateSourceTypeDef] = None
    SpliceInsertMessage: Optional[SpliceInsertMessageTypeDef] = None
    TimeSignalMessage: Optional[TimeSignalMessageTypeDef] = None

class ListSourceLocationsResponseTypeDef(BaseModel):
    Items: List[SourceLocationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPlaybackConfigurationsResponseTypeDef(BaseModel):
    Items: List[PlaybackConfigurationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPrefetchSchedulesResponsePaginatorTypeDef(BaseModel):
    Items: List[PrefetchSchedulePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsResponsePaginatorTypeDef(BaseModel):
    Items: List[ChannelPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsResponseTypeDef(BaseModel):
    Items: List[ChannelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPrefetchSchedulesResponseTypeDef(BaseModel):
    Items: List[PrefetchScheduleTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AlternateMediaTypeDef(BaseModel):
    AdBreaks: Optional[Sequence[AdBreakTypeDef]] = None
    ClipRange: Optional[ClipRangeTypeDef] = None
    DurationMillis: Optional[int] = None
    LiveSourceName: Optional[str] = None
    ScheduledStartTimeMillis: Optional[int] = None
    SourceLocationName: Optional[str] = None
    VodSourceName: Optional[str] = None

class AudienceMediaTypeDef(BaseModel):
    AlternateMedia: Optional[Sequence[AlternateMediaTypeDef]] = None
    Audience: Optional[str] = None

class CreateProgramRequestRequestTypeDef(BaseModel):
    ChannelName: str
    ProgramName: str
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    SourceLocationName: str
    AdBreaks: Optional[Sequence[AdBreakTypeDef]] = None
    AudienceMedia: Optional[Sequence[AudienceMediaTypeDef]] = None
    LiveSourceName: Optional[str] = None
    VodSourceName: Optional[str] = None

class CreateProgramResponseTypeDef(BaseModel):
    AdBreaks: List[AdBreakTypeDef]
    Arn: str
    AudienceMedia: List[AudienceMediaTypeDef]
    ChannelName: str
    ClipRange: ClipRangeTypeDef
    CreationTime: datetime
    DurationMillis: int
    LiveSourceName: str
    ProgramName: str
    ScheduledStartTime: datetime
    SourceLocationName: str
    VodSourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProgramResponseTypeDef(BaseModel):
    AdBreaks: List[AdBreakTypeDef]
    Arn: str
    AudienceMedia: List[AudienceMediaTypeDef]
    ChannelName: str
    ClipRange: ClipRangeTypeDef
    CreationTime: datetime
    DurationMillis: int
    LiveSourceName: str
    ProgramName: str
    ScheduledStartTime: datetime
    SourceLocationName: str
    VodSourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProgramRequestRequestTypeDef(BaseModel):
    ChannelName: str
    ProgramName: str
    ScheduleConfiguration: UpdateProgramScheduleConfigurationTypeDef
    AdBreaks: Optional[Sequence[AdBreakTypeDef]] = None
    AudienceMedia: Optional[Sequence[AudienceMediaTypeDef]] = None

class UpdateProgramResponseTypeDef(BaseModel):
    AdBreaks: List[AdBreakTypeDef]
    Arn: str
    AudienceMedia: List[AudienceMediaTypeDef]
    ChannelName: str
    ClipRange: ClipRangeTypeDef
    CreationTime: datetime
    DurationMillis: int
    LiveSourceName: str
    ProgramName: str
    ScheduledStartTime: datetime
    SourceLocationName: str
    VodSourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

