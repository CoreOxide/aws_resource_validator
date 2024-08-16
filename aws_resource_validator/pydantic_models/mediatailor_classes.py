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
from aws_resource_validator.pydantic_models.mediatailor_constants import *

class SecretsManagerAccessTokenConfigurationTypeDef(BaseValidatorModel):
    HeaderName: Optional[str] = None
    SecretArn: Optional[str] = None
    SecretStringKey: Optional[str] = None

class AdBreakOpportunityTypeDef(BaseValidatorModel):
    OffsetMillis: int

class KeyValuePairTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class SlateSourceTypeDef(BaseValidatorModel):
    SourceLocationName: Optional[str] = None
    VodSourceName: Optional[str] = None

class SpliceInsertMessageTypeDef(BaseValidatorModel):
    AvailNum: Optional[int] = None
    AvailsExpected: Optional[int] = None
    SpliceEventId: Optional[int] = None
    UniqueProgramId: Optional[int] = None

class AdMarkerPassthroughTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AlertTypeDef(BaseValidatorModel):
    AlertCode: str
    AlertMessage: str
    LastModifiedTime: datetime
    RelatedResourceArns: List[str]
    ResourceArn: str
    Category: Optional[AlertCategoryType] = None

class ClipRangeTypeDef(BaseValidatorModel):
    EndOffsetMillis: Optional[int] = None
    StartOffsetMillis: Optional[int] = None

class AvailMatchingCriteriaTypeDef(BaseValidatorModel):
    DynamicVariable: str
    Operator: Literal["EQUALS"]

class AvailSuppressionTypeDef(BaseValidatorModel):
    FillPolicy: Optional[FillPolicyType] = None
    Mode: Optional[ModeType] = None
    Value: Optional[str] = None

class BumperTypeDef(BaseValidatorModel):
    EndUrl: Optional[str] = None
    StartUrl: Optional[str] = None

class CdnConfigurationTypeDef(BaseValidatorModel):
    AdSegmentUrlPrefix: Optional[str] = None
    ContentSegmentUrlPrefix: Optional[str] = None

class LogConfigurationForChannelTypeDef(BaseValidatorModel):
    LogTypes: Optional[List[Literal["AS_RUN"]]] = None

class ConfigureLogsForChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    LogTypes: Sequence[Literal["AS_RUN"]]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConfigureLogsForPlaybackConfigurationRequestRequestTypeDef(BaseValidatorModel):
    PercentEnabled: int
    PlaybackConfigurationName: str

class TimeShiftConfigurationTypeDef(BaseValidatorModel):
    MaxTimeDelaySeconds: int

class HttpPackageConfigurationTypeDef(BaseValidatorModel):
    Path: str
    SourceGroup: str
    Type: TypeType

class DefaultSegmentDeliveryConfigurationTypeDef(BaseValidatorModel):
    BaseUrl: Optional[str] = None

class HttpConfigurationTypeDef(BaseValidatorModel):
    BaseUrl: str

class SegmentDeliveryConfigurationTypeDef(BaseValidatorModel):
    BaseUrl: Optional[str] = None
    Name: Optional[str] = None

class DashConfigurationForPutTypeDef(BaseValidatorModel):
    MpdLocation: Optional[str] = None
    OriginManifestType: Optional[OriginManifestTypeType] = None

class DashConfigurationTypeDef(BaseValidatorModel):
    ManifestEndpointPrefix: Optional[str] = None
    MpdLocation: Optional[str] = None
    OriginManifestType: Optional[OriginManifestTypeType] = None

class DashPlaylistSettingsTypeDef(BaseValidatorModel):
    ManifestWindowSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None

class DeleteChannelPolicyRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str

class DeleteChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str

class DeleteLiveSourceRequestRequestTypeDef(BaseValidatorModel):
    LiveSourceName: str
    SourceLocationName: str

class DeletePlaybackConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeletePrefetchScheduleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    PlaybackConfigurationName: str

class DeleteProgramRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    ProgramName: str

class DeleteSourceLocationRequestRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str

class DeleteVodSourceRequestRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str
    VodSourceName: str

class DescribeChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str

class DescribeLiveSourceRequestRequestTypeDef(BaseValidatorModel):
    LiveSourceName: str
    SourceLocationName: str

class DescribeProgramRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    ProgramName: str

class DescribeSourceLocationRequestRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str

class DescribeVodSourceRequestRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str
    VodSourceName: str

class GetChannelPolicyRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetChannelScheduleRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    Audience: Optional[str] = None
    DurationMinutes: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetPlaybackConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class HlsConfigurationTypeDef(BaseValidatorModel):
    ManifestEndpointPrefix: Optional[str] = None

class LivePreRollConfigurationTypeDef(BaseValidatorModel):
    AdDecisionServerUrl: Optional[str] = None
    MaxDurationSeconds: Optional[int] = None

class LogConfigurationTypeDef(BaseValidatorModel):
    PercentEnabled: int

class GetPrefetchScheduleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    PlaybackConfigurationName: str

class HlsPlaylistSettingsPaginatorTypeDef(BaseValidatorModel):
    AdMarkupType: Optional[List[AdMarkupTypeType]] = None
    ManifestWindowSeconds: Optional[int] = None

class HlsPlaylistSettingsTypeDef(BaseValidatorModel):
    AdMarkupType: Optional[Sequence[AdMarkupTypeType]] = None
    ManifestWindowSeconds: Optional[int] = None

class ListAlertsRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLiveSourcesRequestRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPlaybackConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPrefetchSchedulesRequestRequestTypeDef(BaseValidatorModel):
    PlaybackConfigurationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StreamId: Optional[str] = None

class ListSourceLocationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListVodSourcesRequestRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PrefetchRetrievalPaginatorTypeDef(BaseValidatorModel):
    EndTime: datetime
    DynamicVariables: Optional[Dict[str, str]] = None
    StartTime: Optional[datetime] = None

class PutChannelPolicyRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    Policy: str

class ScheduleAdBreakTypeDef(BaseValidatorModel):
    ApproximateDurationSeconds: Optional[int] = None
    ApproximateStartTime: Optional[datetime] = None
    SourceLocationName: Optional[str] = None
    VodSourceName: Optional[str] = None

class TransitionTypeDef(BaseValidatorModel):
    RelativePosition: RelativePositionType
    Type: str
    DurationMillis: Optional[int] = None
    RelativeProgram: Optional[str] = None
    ScheduledStartTimeMillis: Optional[int] = None

class SegmentationDescriptorTypeDef(BaseValidatorModel):
    SegmentNum: Optional[int] = None
    SegmentationEventId: Optional[int] = None
    SegmentationTypeId: Optional[int] = None
    SegmentationUpid: Optional[str] = None
    SegmentationUpidType: Optional[int] = None
    SegmentsExpected: Optional[int] = None
    SubSegmentNum: Optional[int] = None
    SubSegmentsExpected: Optional[int] = None

class StartChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str

class StopChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateProgramTransitionTypeDef(BaseValidatorModel):
    DurationMillis: Optional[int] = None
    ScheduledStartTimeMillis: Optional[int] = None

class AccessConfigurationTypeDef(BaseValidatorModel):
    AccessType: Optional[AccessTypeType] = None
    SecretsManagerAccessTokenConfiguration: Optional[       SecretsManagerAccessTokenConfigurationTypeDef     ] = None

class ManifestProcessingRulesTypeDef(BaseValidatorModel):
    AdMarkerPassthrough: Optional[AdMarkerPassthroughTypeDef] = None

class PrefetchConsumptionPaginatorTypeDef(BaseValidatorModel):
    EndTime: datetime
    AvailMatchingCriteria: Optional[List[AvailMatchingCriteriaTypeDef]] = None
    StartTime: Optional[datetime] = None

class ConfigureLogsForChannelResponseTypeDef(BaseValidatorModel):
    ChannelName: str
    LogTypes: List[Literal["AS_RUN"]]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigureLogsForPlaybackConfigurationResponseTypeDef(BaseValidatorModel):
    PercentEnabled: int
    PlaybackConfigurationName: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelPolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAlertsResponseTypeDef(BaseValidatorModel):
    Items: List[AlertTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLiveSourceRequestRequestTypeDef(BaseValidatorModel):
    HttpPackageConfigurations: Sequence[HttpPackageConfigurationTypeDef]
    LiveSourceName: str
    SourceLocationName: str
    Tags: Optional[Mapping[str, str]] = None

class CreateLiveSourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    LiveSourceName: str
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVodSourceRequestRequestTypeDef(BaseValidatorModel):
    HttpPackageConfigurations: Sequence[HttpPackageConfigurationTypeDef]
    SourceLocationName: str
    VodSourceName: str
    Tags: Optional[Mapping[str, str]] = None

class CreateVodSourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLiveSourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    LiveSourceName: str
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVodSourceResponseTypeDef(BaseValidatorModel):
    AdBreakOpportunities: List[AdBreakOpportunityTypeDef]
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class LiveSourceTypeDef(BaseValidatorModel):
    Arn: str
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LiveSourceName: str
    SourceLocationName: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class UpdateLiveSourceRequestRequestTypeDef(BaseValidatorModel):
    HttpPackageConfigurations: Sequence[HttpPackageConfigurationTypeDef]
    LiveSourceName: str
    SourceLocationName: str

class UpdateLiveSourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    LiveSourceName: str
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVodSourceRequestRequestTypeDef(BaseValidatorModel):
    HttpPackageConfigurations: Sequence[HttpPackageConfigurationTypeDef]
    SourceLocationName: str
    VodSourceName: str

class UpdateVodSourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class VodSourceTypeDef(BaseValidatorModel):
    Arn: str
    HttpPackageConfigurations: List[HttpPackageConfigurationTypeDef]
    SourceLocationName: str
    VodSourceName: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class GetChannelScheduleRequestGetChannelSchedulePaginateTypeDef(BaseValidatorModel):
    ChannelName: str
    Audience: Optional[str] = None
    DurationMinutes: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAlertsRequestListAlertsPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLiveSourcesRequestListLiveSourcesPaginateTypeDef(BaseValidatorModel):
    SourceLocationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlaybackConfigurationsRequestListPlaybackConfigurationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrefetchSchedulesRequestListPrefetchSchedulesPaginateTypeDef(BaseValidatorModel):
    PlaybackConfigurationName: str
    StreamId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSourceLocationsRequestListSourceLocationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVodSourcesRequestListVodSourcesPaginateTypeDef(BaseValidatorModel):
    SourceLocationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ResponseOutputItemPaginatorTypeDef(BaseValidatorModel):
    ManifestName: str
    PlaybackUrl: str
    SourceGroup: str
    DashPlaylistSettings: Optional[DashPlaylistSettingsTypeDef] = None
    HlsPlaylistSettings: Optional[HlsPlaylistSettingsPaginatorTypeDef] = None

class RequestOutputItemTypeDef(BaseValidatorModel):
    ManifestName: str
    SourceGroup: str
    DashPlaylistSettings: Optional[DashPlaylistSettingsTypeDef] = None
    HlsPlaylistSettings: Optional[HlsPlaylistSettingsTypeDef] = None

class ResponseOutputItemTypeDef(BaseValidatorModel):
    ManifestName: str
    PlaybackUrl: str
    SourceGroup: str
    DashPlaylistSettings: Optional[DashPlaylistSettingsTypeDef] = None
    HlsPlaylistSettings: Optional[HlsPlaylistSettingsTypeDef] = None

class PrefetchConsumptionTypeDef(BaseValidatorModel):
    EndTime: TimestampTypeDef
    AvailMatchingCriteria: Optional[Sequence[AvailMatchingCriteriaTypeDef]] = None
    StartTime: Optional[TimestampTypeDef] = None

class PrefetchRetrievalTypeDef(BaseValidatorModel):
    EndTime: TimestampTypeDef
    DynamicVariables: Optional[Mapping[str, str]] = None
    StartTime: Optional[TimestampTypeDef] = None

class ScheduleEntryTypeDef(BaseValidatorModel):
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

class ScheduleConfigurationTypeDef(BaseValidatorModel):
    Transition: TransitionTypeDef
    ClipRange: Optional[ClipRangeTypeDef] = None

class TimeSignalMessageTypeDef(BaseValidatorModel):
    SegmentationDescriptors: Optional[Sequence[SegmentationDescriptorTypeDef]] = None

class UpdateProgramScheduleConfigurationTypeDef(BaseValidatorModel):
    ClipRange: Optional[ClipRangeTypeDef] = None
    Transition: Optional[UpdateProgramTransitionTypeDef] = None

class CreateSourceLocationRequestRequestTypeDef(BaseValidatorModel):
    HttpConfiguration: HttpConfigurationTypeDef
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfigurationTypeDef] = None
    DefaultSegmentDeliveryConfiguration: Optional[       DefaultSegmentDeliveryConfigurationTypeDef     ] = None
    SegmentDeliveryConfigurations: Optional[Sequence[SegmentDeliveryConfigurationTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateSourceLocationResponseTypeDef(BaseValidatorModel):
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

class DescribeSourceLocationResponseTypeDef(BaseValidatorModel):
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

class SourceLocationTypeDef(BaseValidatorModel):
    Arn: str
    HttpConfiguration: HttpConfigurationTypeDef
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfigurationTypeDef] = None
    CreationTime: Optional[datetime] = None
    DefaultSegmentDeliveryConfiguration: Optional[       DefaultSegmentDeliveryConfigurationTypeDef     ] = None
    LastModifiedTime: Optional[datetime] = None
    SegmentDeliveryConfigurations: Optional[List[SegmentDeliveryConfigurationTypeDef]] = None
    Tags: Optional[Dict[str, str]] = None

class UpdateSourceLocationRequestRequestTypeDef(BaseValidatorModel):
    HttpConfiguration: HttpConfigurationTypeDef
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfigurationTypeDef] = None
    DefaultSegmentDeliveryConfiguration: Optional[       DefaultSegmentDeliveryConfigurationTypeDef     ] = None
    SegmentDeliveryConfigurations: Optional[Sequence[SegmentDeliveryConfigurationTypeDef]] = None

class UpdateSourceLocationResponseTypeDef(BaseValidatorModel):
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

class GetPlaybackConfigurationResponseTypeDef(BaseValidatorModel):
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

class PlaybackConfigurationTypeDef(BaseValidatorModel):
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

class PutPlaybackConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class PutPlaybackConfigurationResponseTypeDef(BaseValidatorModel):
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

class PrefetchSchedulePaginatorTypeDef(BaseValidatorModel):
    Arn: str
    Consumption: PrefetchConsumptionPaginatorTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalPaginatorTypeDef
    StreamId: Optional[str] = None

class ListLiveSourcesResponseTypeDef(BaseValidatorModel):
    Items: List[LiveSourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVodSourcesResponseTypeDef(BaseValidatorModel):
    Items: List[VodSourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelPaginatorTypeDef(BaseValidatorModel):
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

class CreateChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    Outputs: Sequence[RequestOutputItemTypeDef]
    PlaybackMode: PlaybackModeType
    Audiences: Optional[Sequence[str]] = None
    FillerSlate: Optional[SlateSourceTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Tier: Optional[TierType] = None
    TimeShiftConfiguration: Optional[TimeShiftConfigurationTypeDef] = None

class UpdateChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    Outputs: Sequence[RequestOutputItemTypeDef]
    Audiences: Optional[Sequence[str]] = None
    FillerSlate: Optional[SlateSourceTypeDef] = None
    TimeShiftConfiguration: Optional[TimeShiftConfigurationTypeDef] = None

class ChannelTypeDef(BaseValidatorModel):
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

class CreateChannelResponseTypeDef(BaseValidatorModel):
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

class DescribeChannelResponseTypeDef(BaseValidatorModel):
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

class UpdateChannelResponseTypeDef(BaseValidatorModel):
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

class CreatePrefetchScheduleRequestRequestTypeDef(BaseValidatorModel):
    Consumption: PrefetchConsumptionTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalTypeDef
    StreamId: Optional[str] = None

class CreatePrefetchScheduleResponseTypeDef(BaseValidatorModel):
    Arn: str
    Consumption: PrefetchConsumptionTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalTypeDef
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPrefetchScheduleResponseTypeDef(BaseValidatorModel):
    Arn: str
    Consumption: PrefetchConsumptionTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalTypeDef
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PrefetchScheduleTypeDef(BaseValidatorModel):
    Arn: str
    Consumption: PrefetchConsumptionTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalTypeDef
    StreamId: Optional[str] = None

class GetChannelScheduleResponseTypeDef(BaseValidatorModel):
    Items: List[ScheduleEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AdBreakTypeDef(BaseValidatorModel):
    OffsetMillis: int
    AdBreakMetadata: Optional[Sequence[KeyValuePairTypeDef]] = None
    MessageType: Optional[MessageTypeType] = None
    Slate: Optional[SlateSourceTypeDef] = None
    SpliceInsertMessage: Optional[SpliceInsertMessageTypeDef] = None
    TimeSignalMessage: Optional[TimeSignalMessageTypeDef] = None

class ListSourceLocationsResponseTypeDef(BaseValidatorModel):
    Items: List[SourceLocationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPlaybackConfigurationsResponseTypeDef(BaseValidatorModel):
    Items: List[PlaybackConfigurationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPrefetchSchedulesResponsePaginatorTypeDef(BaseValidatorModel):
    Items: List[PrefetchSchedulePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsResponsePaginatorTypeDef(BaseValidatorModel):
    Items: List[ChannelPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsResponseTypeDef(BaseValidatorModel):
    Items: List[ChannelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPrefetchSchedulesResponseTypeDef(BaseValidatorModel):
    Items: List[PrefetchScheduleTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AlternateMediaTypeDef(BaseValidatorModel):
    AdBreaks: Optional[Sequence[AdBreakTypeDef]] = None
    ClipRange: Optional[ClipRangeTypeDef] = None
    DurationMillis: Optional[int] = None
    LiveSourceName: Optional[str] = None
    ScheduledStartTimeMillis: Optional[int] = None
    SourceLocationName: Optional[str] = None
    VodSourceName: Optional[str] = None

class AudienceMediaTypeDef(BaseValidatorModel):
    AlternateMedia: Optional[Sequence[AlternateMediaTypeDef]] = None
    Audience: Optional[str] = None

class CreateProgramRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    ProgramName: str
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    SourceLocationName: str
    AdBreaks: Optional[Sequence[AdBreakTypeDef]] = None
    AudienceMedia: Optional[Sequence[AudienceMediaTypeDef]] = None
    LiveSourceName: Optional[str] = None
    VodSourceName: Optional[str] = None

class CreateProgramResponseTypeDef(BaseValidatorModel):
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

class DescribeProgramResponseTypeDef(BaseValidatorModel):
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

class UpdateProgramRequestRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    ProgramName: str
    ScheduleConfiguration: UpdateProgramScheduleConfigurationTypeDef
    AdBreaks: Optional[Sequence[AdBreakTypeDef]] = None
    AudienceMedia: Optional[Sequence[AudienceMediaTypeDef]] = None

class UpdateProgramResponseTypeDef(BaseValidatorModel):
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

