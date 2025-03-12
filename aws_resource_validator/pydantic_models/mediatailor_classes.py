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


class AdConditioningConfigurationTypeDef(BaseValidatorModel):
    StreamingMediaFileConditioning: StreamingMediaFileConditioningType


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
    Mode: Optional[ModeType] = None
    Value: Optional[str] = None
    FillPolicy: Optional[FillPolicyType] = None


class BumperTypeDef(BaseValidatorModel):
    EndUrl: Optional[str] = None
    StartUrl: Optional[str] = None


class CdnConfigurationTypeDef(BaseValidatorModel):
    AdSegmentUrlPrefix: Optional[str] = None
    ContentSegmentUrlPrefix: Optional[str] = None


class LogConfigurationForChannelTypeDef(BaseValidatorModel):
    LogTypes: Optional[List[Literal["AS_RUN"]]] = None


class ConfigureLogsForChannelRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    LogTypes: Sequence[Literal["AS_RUN"]]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ConfigureLogsForPlaybackConfigurationRequestTypeDef(BaseValidatorModel):
    PercentEnabled: int
    PlaybackConfigurationName: str
    EnabledLoggingStrategies: Optional[Sequence[LoggingStrategyType]] = None


class TimeShiftConfigurationTypeDef(BaseValidatorModel):
    MaxTimeDelaySeconds: int


class PrefetchRetrievalOutputTypeDef(BaseValidatorModel):
    EndTime: datetime
    DynamicVariables: Optional[Dict[str, str]] = None
    StartTime: Optional[datetime] = None


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


class DeleteChannelPolicyRequestTypeDef(BaseValidatorModel):
    ChannelName: str


class DeleteChannelRequestTypeDef(BaseValidatorModel):
    ChannelName: str


class DeleteLiveSourceRequestTypeDef(BaseValidatorModel):
    LiveSourceName: str
    SourceLocationName: str


class DeletePlaybackConfigurationRequestTypeDef(BaseValidatorModel):
    Name: str


class DeletePrefetchScheduleRequestTypeDef(BaseValidatorModel):
    Name: str
    PlaybackConfigurationName: str


class DeleteProgramRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    ProgramName: str


class DeleteSourceLocationRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str


class DeleteVodSourceRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str
    VodSourceName: str


class DescribeChannelRequestTypeDef(BaseValidatorModel):
    ChannelName: str


class DescribeLiveSourceRequestTypeDef(BaseValidatorModel):
    LiveSourceName: str
    SourceLocationName: str


class DescribeProgramRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    ProgramName: str


class DescribeSourceLocationRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str


class DescribeVodSourceRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str
    VodSourceName: str


class GetChannelPolicyRequestTypeDef(BaseValidatorModel):
    ChannelName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetChannelScheduleRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    DurationMinutes: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Audience: Optional[str] = None


class GetPlaybackConfigurationRequestTypeDef(BaseValidatorModel):
    Name: str


class HlsConfigurationTypeDef(BaseValidatorModel):
    ManifestEndpointPrefix: Optional[str] = None


class LivePreRollConfigurationTypeDef(BaseValidatorModel):
    AdDecisionServerUrl: Optional[str] = None
    MaxDurationSeconds: Optional[int] = None


class LogConfigurationTypeDef(BaseValidatorModel):
    PercentEnabled: int
    EnabledLoggingStrategies: Optional[List[LoggingStrategyType]] = None


class GetPrefetchScheduleRequestTypeDef(BaseValidatorModel):
    Name: str
    PlaybackConfigurationName: str


class HlsPlaylistSettingsOutputTypeDef(BaseValidatorModel):
    ManifestWindowSeconds: Optional[int] = None
    AdMarkupType: Optional[List[AdMarkupTypeType]] = None


class HlsPlaylistSettingsTypeDef(BaseValidatorModel):
    ManifestWindowSeconds: Optional[int] = None
    AdMarkupType: Optional[Sequence[AdMarkupTypeType]] = None


class ListAlertsRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLiveSourcesRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPlaybackConfigurationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPrefetchSchedulesRequestTypeDef(BaseValidatorModel):
    PlaybackConfigurationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StreamId: Optional[str] = None


class ListSourceLocationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListVodSourcesRequestTypeDef(BaseValidatorModel):
    SourceLocationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PutChannelPolicyRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    Policy: str


class ScheduleAdBreakTypeDef(BaseValidatorModel):
    ApproximateDurationSeconds: Optional[int] = None
    ApproximateStartTime: Optional[datetime] = None
    SourceLocationName: Optional[str] = None
    VodSourceName: Optional[str] = None


class SegmentationDescriptorTypeDef(BaseValidatorModel):
    SegmentationEventId: Optional[int] = None
    SegmentationUpidType: Optional[int] = None
    SegmentationUpid: Optional[str] = None
    SegmentationTypeId: Optional[int] = None
    SegmentNum: Optional[int] = None
    SegmentsExpected: Optional[int] = None
    SubSegmentNum: Optional[int] = None
    SubSegmentsExpected: Optional[int] = None


class StartChannelRequestTypeDef(BaseValidatorModel):
    ChannelName: str


class StopChannelRequestTypeDef(BaseValidatorModel):
    ChannelName: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateProgramTransitionTypeDef(BaseValidatorModel):
    ScheduledStartTimeMillis: Optional[int] = None
    DurationMillis: Optional[int] = None


class AccessConfigurationTypeDef(BaseValidatorModel):
    AccessType: Optional[AccessTypeType] = None
    SecretsManagerAccessTokenConfiguration: Optional[ SecretsManagerAccessTokenConfigurationTypeDef ] = None


class ManifestProcessingRulesTypeDef(BaseValidatorModel):
    AdMarkerPassthrough: Optional[AdMarkerPassthroughTypeDef] = None


class PrefetchConsumptionOutputTypeDef(BaseValidatorModel):
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
    EnabledLoggingStrategies: List[LoggingStrategyType]
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetChannelPolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAlertsResponseTypeDef(BaseValidatorModel):
    Items: List[AlertTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class HttpPackageConfigurationTypeDef(BaseValidatorModel):
    pass


class CreateLiveSourceRequestTypeDef(BaseValidatorModel):
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


class CreateVodSourceRequestTypeDef(BaseValidatorModel):
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


class UpdateLiveSourceRequestTypeDef(BaseValidatorModel):
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


class UpdateVodSourceRequestTypeDef(BaseValidatorModel):
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


class GetChannelScheduleRequestPaginateTypeDef(BaseValidatorModel):
    ChannelName: str
    DurationMinutes: Optional[str] = None
    Audience: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAlertsRequestPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListChannelsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLiveSourcesRequestPaginateTypeDef(BaseValidatorModel):
    SourceLocationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPlaybackConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrefetchSchedulesRequestPaginateTypeDef(BaseValidatorModel):
    PlaybackConfigurationName: str
    StreamId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSourceLocationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVodSourcesRequestPaginateTypeDef(BaseValidatorModel):
    SourceLocationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ResponseOutputItemTypeDef(BaseValidatorModel):
    ManifestName: str
    PlaybackUrl: str
    SourceGroup: str
    DashPlaylistSettings: Optional[DashPlaylistSettingsTypeDef] = None
    HlsPlaylistSettings: Optional[HlsPlaylistSettingsOutputTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


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
    LiveSourceName: Optional[str] = None
    ScheduleAdBreaks: Optional[List[ScheduleAdBreakTypeDef]] = None
    ScheduleEntryType: Optional[ScheduleEntryTypeType] = None
    VodSourceName: Optional[str] = None
    Audiences: Optional[List[str]] = None


class TransitionTypeDef(BaseValidatorModel):
    pass


class ScheduleConfigurationTypeDef(BaseValidatorModel):
    Transition: TransitionTypeDef
    ClipRange: Optional[ClipRangeTypeDef] = None


class TimeSignalMessageOutputTypeDef(BaseValidatorModel):
    SegmentationDescriptors: Optional[List[SegmentationDescriptorTypeDef]] = None


class TimeSignalMessageTypeDef(BaseValidatorModel):
    SegmentationDescriptors: Optional[Sequence[SegmentationDescriptorTypeDef]] = None


class UpdateProgramScheduleConfigurationTypeDef(BaseValidatorModel):
    Transition: Optional[UpdateProgramTransitionTypeDef] = None
    ClipRange: Optional[ClipRangeTypeDef] = None


class CreateSourceLocationRequestTypeDef(BaseValidatorModel):
    HttpConfiguration: HttpConfigurationTypeDef
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfigurationTypeDef] = None
    DefaultSegmentDeliveryConfiguration: Optional[DefaultSegmentDeliveryConfigurationTypeDef] = None
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
    DefaultSegmentDeliveryConfiguration: Optional[DefaultSegmentDeliveryConfigurationTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    SegmentDeliveryConfigurations: Optional[List[SegmentDeliveryConfigurationTypeDef]] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateSourceLocationRequestTypeDef(BaseValidatorModel):
    HttpConfiguration: HttpConfigurationTypeDef
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfigurationTypeDef] = None
    DefaultSegmentDeliveryConfiguration: Optional[DefaultSegmentDeliveryConfigurationTypeDef] = None
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
    AdConditioningConfiguration: AdConditioningConfigurationTypeDef
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
    AdConditioningConfiguration: Optional[AdConditioningConfigurationTypeDef] = None


class PutPlaybackConfigurationRequestTypeDef(BaseValidatorModel):
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
    AdConditioningConfiguration: Optional[AdConditioningConfigurationTypeDef] = None


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
    AdConditioningConfiguration: AdConditioningConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePrefetchScheduleResponseTypeDef(BaseValidatorModel):
    Arn: str
    Consumption: PrefetchConsumptionOutputTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalOutputTypeDef
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPrefetchScheduleResponseTypeDef(BaseValidatorModel):
    Arn: str
    Consumption: PrefetchConsumptionOutputTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalOutputTypeDef
    StreamId: str
    ResponseMetadata: ResponseMetadataTypeDef


class PrefetchScheduleTypeDef(BaseValidatorModel):
    Arn: str
    Consumption: PrefetchConsumptionOutputTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalOutputTypeDef
    StreamId: Optional[str] = None


class ListLiveSourcesResponseTypeDef(BaseValidatorModel):
    Items: List[LiveSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListVodSourcesResponseTypeDef(BaseValidatorModel):
    Items: List[VodSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ChannelTypeDef(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelState: str
    Outputs: List[ResponseOutputItemTypeDef]
    PlaybackMode: str
    Tier: str
    LogConfiguration: LogConfigurationForChannelTypeDef
    CreationTime: Optional[datetime] = None
    FillerSlate: Optional[SlateSourceTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    Audiences: Optional[List[str]] = None


class CreateChannelResponseTypeDef(BaseValidatorModel):
    Arn: str
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
    Audiences: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeChannelResponseTypeDef(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelState: ChannelStateType
    CreationTime: datetime
    FillerSlate: SlateSourceTypeDef
    LastModifiedTime: datetime
    Outputs: List[ResponseOutputItemTypeDef]
    PlaybackMode: str
    Tags: Dict[str, str]
    Tier: str
    LogConfiguration: LogConfigurationForChannelTypeDef
    TimeShiftConfiguration: TimeShiftConfigurationTypeDef
    Audiences: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateChannelResponseTypeDef(BaseValidatorModel):
    Arn: str
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
    Audiences: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class HlsPlaylistSettingsUnionTypeDef(BaseValidatorModel):
    pass


class RequestOutputItemTypeDef(BaseValidatorModel):
    ManifestName: str
    SourceGroup: str
    DashPlaylistSettings: Optional[DashPlaylistSettingsTypeDef] = None
    HlsPlaylistSettings: Optional[HlsPlaylistSettingsUnionTypeDef] = None


class GetChannelScheduleResponseTypeDef(BaseValidatorModel):
    Items: List[ScheduleEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AdBreakOutputTypeDef(BaseValidatorModel):
    OffsetMillis: int
    MessageType: Optional[MessageTypeType] = None
    Slate: Optional[SlateSourceTypeDef] = None
    SpliceInsertMessage: Optional[SpliceInsertMessageTypeDef] = None
    TimeSignalMessage: Optional[TimeSignalMessageOutputTypeDef] = None
    AdBreakMetadata: Optional[List[KeyValuePairTypeDef]] = None


class ListSourceLocationsResponseTypeDef(BaseValidatorModel):
    Items: List[SourceLocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPlaybackConfigurationsResponseTypeDef(BaseValidatorModel):
    Items: List[PlaybackConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPrefetchSchedulesResponseTypeDef(BaseValidatorModel):
    Items: List[PrefetchScheduleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListChannelsResponseTypeDef(BaseValidatorModel):
    Items: List[ChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateChannelRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    Outputs: Sequence[RequestOutputItemTypeDef]
    PlaybackMode: PlaybackModeType
    FillerSlate: Optional[SlateSourceTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Tier: Optional[TierType] = None
    TimeShiftConfiguration: Optional[TimeShiftConfigurationTypeDef] = None
    Audiences: Optional[Sequence[str]] = None


class UpdateChannelRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    Outputs: Sequence[RequestOutputItemTypeDef]
    FillerSlate: Optional[SlateSourceTypeDef] = None
    TimeShiftConfiguration: Optional[TimeShiftConfigurationTypeDef] = None
    Audiences: Optional[Sequence[str]] = None


class PrefetchRetrievalUnionTypeDef(BaseValidatorModel):
    pass


class PrefetchConsumptionUnionTypeDef(BaseValidatorModel):
    pass


class CreatePrefetchScheduleRequestTypeDef(BaseValidatorModel):
    Consumption: PrefetchConsumptionUnionTypeDef
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalUnionTypeDef
    StreamId: Optional[str] = None


class AlternateMediaOutputTypeDef(BaseValidatorModel):
    SourceLocationName: Optional[str] = None
    LiveSourceName: Optional[str] = None
    VodSourceName: Optional[str] = None
    ClipRange: Optional[ClipRangeTypeDef] = None
    ScheduledStartTimeMillis: Optional[int] = None
    AdBreaks: Optional[List[AdBreakOutputTypeDef]] = None
    DurationMillis: Optional[int] = None


class TimeSignalMessageUnionTypeDef(BaseValidatorModel):
    pass


class AdBreakTypeDef(BaseValidatorModel):
    OffsetMillis: int
    MessageType: Optional[MessageTypeType] = None
    Slate: Optional[SlateSourceTypeDef] = None
    SpliceInsertMessage: Optional[SpliceInsertMessageTypeDef] = None
    TimeSignalMessage: Optional[TimeSignalMessageUnionTypeDef] = None
    AdBreakMetadata: Optional[Sequence[KeyValuePairTypeDef]] = None


class AudienceMediaOutputTypeDef(BaseValidatorModel):
    Audience: Optional[str] = None
    AlternateMedia: Optional[List[AlternateMediaOutputTypeDef]] = None


class CreateProgramResponseTypeDef(BaseValidatorModel):
    AdBreaks: List[AdBreakOutputTypeDef]
    Arn: str
    ChannelName: str
    CreationTime: datetime
    LiveSourceName: str
    ProgramName: str
    ScheduledStartTime: datetime
    SourceLocationName: str
    VodSourceName: str
    ClipRange: ClipRangeTypeDef
    DurationMillis: int
    AudienceMedia: List[AudienceMediaOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeProgramResponseTypeDef(BaseValidatorModel):
    AdBreaks: List[AdBreakOutputTypeDef]
    Arn: str
    ChannelName: str
    CreationTime: datetime
    LiveSourceName: str
    ProgramName: str
    ScheduledStartTime: datetime
    SourceLocationName: str
    VodSourceName: str
    ClipRange: ClipRangeTypeDef
    DurationMillis: int
    AudienceMedia: List[AudienceMediaOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProgramResponseTypeDef(BaseValidatorModel):
    AdBreaks: List[AdBreakOutputTypeDef]
    Arn: str
    ChannelName: str
    CreationTime: datetime
    ProgramName: str
    SourceLocationName: str
    VodSourceName: str
    LiveSourceName: str
    ClipRange: ClipRangeTypeDef
    DurationMillis: int
    ScheduledStartTime: datetime
    AudienceMedia: List[AudienceMediaOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AdBreakUnionTypeDef(BaseValidatorModel):
    pass


class AlternateMediaTypeDef(BaseValidatorModel):
    SourceLocationName: Optional[str] = None
    LiveSourceName: Optional[str] = None
    VodSourceName: Optional[str] = None
    ClipRange: Optional[ClipRangeTypeDef] = None
    ScheduledStartTimeMillis: Optional[int] = None
    AdBreaks: Optional[Sequence[AdBreakUnionTypeDef]] = None
    DurationMillis: Optional[int] = None


class AlternateMediaUnionTypeDef(BaseValidatorModel):
    pass


class AudienceMediaTypeDef(BaseValidatorModel):
    Audience: Optional[str] = None
    AlternateMedia: Optional[Sequence[AlternateMediaUnionTypeDef]] = None


class AudienceMediaUnionTypeDef(BaseValidatorModel):
    pass


class CreateProgramRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    ProgramName: str
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    SourceLocationName: str
    AdBreaks: Optional[Sequence[AdBreakUnionTypeDef]] = None
    LiveSourceName: Optional[str] = None
    VodSourceName: Optional[str] = None
    AudienceMedia: Optional[Sequence[AudienceMediaUnionTypeDef]] = None


class UpdateProgramRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    ProgramName: str
    ScheduleConfiguration: UpdateProgramScheduleConfigurationTypeDef
    AdBreaks: Optional[Sequence[AdBreakUnionTypeDef]] = None
    AudienceMedia: Optional[Sequence[AudienceMediaUnionTypeDef]] = None


