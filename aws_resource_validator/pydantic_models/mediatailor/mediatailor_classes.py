from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mediatailor.mediatailor_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class SecretsManagerAccessTokenConfiguration(BaseValidatorModel):
    HeaderName: Optional[str] = None
    SecretArn: Optional[str] = None
    SecretStringKey: Optional[str] = None


class AdBreakOpportunity(BaseValidatorModel):
    OffsetMillis: int


class KeyValuePair(BaseValidatorModel):
    Key: str
    Value: str


class SlateSource(BaseValidatorModel):
    SourceLocationName: Optional[str] = None
    VodSourceName: Optional[str] = None


class SpliceInsertMessage(BaseValidatorModel):
    AvailNum: Optional[int] = None
    AvailsExpected: Optional[int] = None
    SpliceEventId: Optional[int] = None
    UniqueProgramId: Optional[int] = None


class AdConditioningConfiguration(BaseValidatorModel):
    StreamingMediaFileConditioning: StreamingMediaFileConditioningType


class AdMarkerPassthrough(BaseValidatorModel):
    Enabled: Optional[bool] = None


class Alert(BaseValidatorModel):
    AlertCode: str
    AlertMessage: str
    LastModifiedTime: datetime
    RelatedResourceArns: List[str]
    ResourceArn: str
    Category: Optional[AlertCategoryType] = None


class ClipRange(BaseValidatorModel):
    EndOffsetMillis: Optional[int] = None
    StartOffsetMillis: Optional[int] = None


class AvailMatchingCriteria(BaseValidatorModel):
    DynamicVariable: str
    Operator: Literal['EQUALS']


class AvailSuppression(BaseValidatorModel):
    Mode: Optional[ModeType] = None
    Value: Optional[str] = None
    FillPolicy: Optional[FillPolicyType] = None


class Bumper(BaseValidatorModel):
    EndUrl: Optional[str] = None
    StartUrl: Optional[str] = None


class CdnConfiguration(BaseValidatorModel):
    AdSegmentUrlPrefix: Optional[str] = None
    ContentSegmentUrlPrefix: Optional[str] = None


class LogConfigurationForChannel(BaseValidatorModel):
    LogTypes: Optional[List[Literal['AS_RUN']]] = None


class ConfigureLogsForChannelRequest(BaseValidatorModel):
    ChannelName: str
    LogTypes: List[Literal['AS_RUN']]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ConfigureLogsForPlaybackConfigurationRequest(BaseValidatorModel):
    PercentEnabled: int
    PlaybackConfigurationName: str
    EnabledLoggingStrategies: Optional[List[LoggingStrategyType]] = None


class TimeShiftConfiguration(BaseValidatorModel):
    MaxTimeDelaySeconds: int


class HttpPackageConfiguration(BaseValidatorModel):
    Path: str
    SourceGroup: str
    Type: TypeType


class PrefetchRetrievalOutput(BaseValidatorModel):
    EndTime: datetime
    DynamicVariables: Optional[Dict[str, str]] = None
    StartTime: Optional[datetime] = None


class DefaultSegmentDeliveryConfiguration(BaseValidatorModel):
    BaseUrl: Optional[str] = None


class HttpConfiguration(BaseValidatorModel):
    BaseUrl: str


class SegmentDeliveryConfiguration(BaseValidatorModel):
    BaseUrl: Optional[str] = None
    Name: Optional[str] = None


class DashConfigurationForPut(BaseValidatorModel):
    MpdLocation: Optional[str] = None
    OriginManifestType: Optional[OriginManifestTypeType] = None


class DashConfiguration(BaseValidatorModel):
    ManifestEndpointPrefix: Optional[str] = None
    MpdLocation: Optional[str] = None
    OriginManifestType: Optional[OriginManifestTypeType] = None


class DashPlaylistSettings(BaseValidatorModel):
    ManifestWindowSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None


class DeleteChannelPolicyRequest(BaseValidatorModel):
    ChannelName: str


class DeleteChannelRequest(BaseValidatorModel):
    ChannelName: str


class DeleteLiveSourceRequest(BaseValidatorModel):
    LiveSourceName: str
    SourceLocationName: str


class DeletePlaybackConfigurationRequest(BaseValidatorModel):
    Name: str


class DeletePrefetchScheduleRequest(BaseValidatorModel):
    Name: str
    PlaybackConfigurationName: str


class DeleteProgramRequest(BaseValidatorModel):
    ChannelName: str
    ProgramName: str


class DeleteSourceLocationRequest(BaseValidatorModel):
    SourceLocationName: str


class DeleteVodSourceRequest(BaseValidatorModel):
    SourceLocationName: str
    VodSourceName: str


class DescribeChannelRequest(BaseValidatorModel):
    ChannelName: str


class DescribeLiveSourceRequest(BaseValidatorModel):
    LiveSourceName: str
    SourceLocationName: str


class DescribeProgramRequest(BaseValidatorModel):
    ChannelName: str
    ProgramName: str


class DescribeSourceLocationRequest(BaseValidatorModel):
    SourceLocationName: str


class DescribeVodSourceRequest(BaseValidatorModel):
    SourceLocationName: str
    VodSourceName: str


class GetChannelPolicyRequest(BaseValidatorModel):
    ChannelName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetChannelScheduleRequest(BaseValidatorModel):
    ChannelName: str
    DurationMinutes: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Audience: Optional[str] = None


class GetPlaybackConfigurationRequest(BaseValidatorModel):
    Name: str


class HlsConfiguration(BaseValidatorModel):
    ManifestEndpointPrefix: Optional[str] = None


class LivePreRollConfiguration(BaseValidatorModel):
    AdDecisionServerUrl: Optional[str] = None
    MaxDurationSeconds: Optional[int] = None


class LogConfiguration(BaseValidatorModel):
    PercentEnabled: int
    EnabledLoggingStrategies: Optional[List[LoggingStrategyType]] = None


class GetPrefetchScheduleRequest(BaseValidatorModel):
    Name: str
    PlaybackConfigurationName: str


class HlsPlaylistSettingsOutput(BaseValidatorModel):
    ManifestWindowSeconds: Optional[int] = None
    AdMarkupType: Optional[List[AdMarkupTypeType]] = None


class HlsPlaylistSettings(BaseValidatorModel):
    ManifestWindowSeconds: Optional[int] = None
    AdMarkupType: Optional[List[AdMarkupTypeType]] = None


class ListAlertsRequest(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLiveSourcesRequest(BaseValidatorModel):
    SourceLocationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPlaybackConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPrefetchSchedulesRequest(BaseValidatorModel):
    PlaybackConfigurationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StreamId: Optional[str] = None


class ListSourceLocationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListVodSourcesRequest(BaseValidatorModel):
    SourceLocationName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

Timestamp = Union[datetime, str]


class PutChannelPolicyRequest(BaseValidatorModel):
    ChannelName: str
    Policy: str


class ScheduleAdBreak(BaseValidatorModel):
    ApproximateDurationSeconds: Optional[int] = None
    ApproximateStartTime: Optional[datetime] = None
    SourceLocationName: Optional[str] = None
    VodSourceName: Optional[str] = None


class Transition(BaseValidatorModel):
    RelativePosition: RelativePositionType
    Type: str
    DurationMillis: Optional[int] = None
    RelativeProgram: Optional[str] = None
    ScheduledStartTimeMillis: Optional[int] = None


class SegmentationDescriptor(BaseValidatorModel):
    SegmentationEventId: Optional[int] = None
    SegmentationUpidType: Optional[int] = None
    SegmentationUpid: Optional[str] = None
    SegmentationTypeId: Optional[int] = None
    SegmentNum: Optional[int] = None
    SegmentsExpected: Optional[int] = None
    SubSegmentNum: Optional[int] = None
    SubSegmentsExpected: Optional[int] = None


class StartChannelRequest(BaseValidatorModel):
    ChannelName: str


class StopChannelRequest(BaseValidatorModel):
    ChannelName: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateProgramTransition(BaseValidatorModel):
    ScheduledStartTimeMillis: Optional[int] = None
    DurationMillis: Optional[int] = None


class AccessConfiguration(BaseValidatorModel):
    AccessType: Optional[AccessTypeType] = None
    SecretsManagerAccessTokenConfiguration: Optional[SecretsManagerAccessTokenConfiguration] = None


class ManifestProcessingRules(BaseValidatorModel):
    AdMarkerPassthrough: Optional[AdMarkerPassthrough] = None


class PrefetchConsumptionOutput(BaseValidatorModel):
    EndTime: datetime
    AvailMatchingCriteria: Optional[List[AvailMatchingCriteria]] = None
    StartTime: Optional[datetime] = None


class ConfigureLogsForChannelResponse(BaseValidatorModel):
    ChannelName: str
    LogTypes: List[Literal['AS_RUN']]
    ResponseMetadata: ResponseMetadata


class ConfigureLogsForPlaybackConfigurationResponse(BaseValidatorModel):
    PercentEnabled: int
    PlaybackConfigurationName: str
    EnabledLoggingStrategies: List[LoggingStrategyType]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetChannelPolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class ListAlertsResponse(BaseValidatorModel):
    Items: List[Alert]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateLiveSourceRequest(BaseValidatorModel):
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    LiveSourceName: str
    SourceLocationName: str
    Tags: Optional[Dict[str, str]] = None


class CreateLiveSourceResponse(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    LastModifiedTime: datetime
    LiveSourceName: str
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateVodSourceRequest(BaseValidatorModel):
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    SourceLocationName: str
    VodSourceName: str
    Tags: Optional[Dict[str, str]] = None


class CreateVodSourceResponse(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str
    ResponseMetadata: ResponseMetadata


class DescribeLiveSourceResponse(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    LastModifiedTime: datetime
    LiveSourceName: str
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeVodSourceResponse(BaseValidatorModel):
    AdBreakOpportunities: List[AdBreakOpportunity]
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str
    ResponseMetadata: ResponseMetadata


class LiveSource(BaseValidatorModel):
    Arn: str
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    LiveSourceName: str
    SourceLocationName: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateLiveSourceRequest(BaseValidatorModel):
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    LiveSourceName: str
    SourceLocationName: str


class UpdateLiveSourceResponse(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    LastModifiedTime: datetime
    LiveSourceName: str
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateVodSourceRequest(BaseValidatorModel):
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    SourceLocationName: str
    VodSourceName: str


class UpdateVodSourceResponse(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str
    ResponseMetadata: ResponseMetadata


class VodSource(BaseValidatorModel):
    Arn: str
    HttpPackageConfigurations: List[HttpPackageConfiguration]
    SourceLocationName: str
    VodSourceName: str
    CreationTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class GetChannelScheduleRequestPaginate(BaseValidatorModel):
    ChannelName: str
    DurationMinutes: Optional[str] = None
    Audience: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAlertsRequestPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListChannelsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLiveSourcesRequestPaginate(BaseValidatorModel):
    SourceLocationName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPlaybackConfigurationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPrefetchSchedulesRequestPaginate(BaseValidatorModel):
    PlaybackConfigurationName: str
    StreamId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSourceLocationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVodSourcesRequestPaginate(BaseValidatorModel):
    SourceLocationName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ResponseOutputItem(BaseValidatorModel):
    ManifestName: str
    PlaybackUrl: str
    SourceGroup: str
    DashPlaylistSettings: Optional[DashPlaylistSettings] = None
    HlsPlaylistSettings: Optional[HlsPlaylistSettingsOutput] = None

HlsPlaylistSettingsUnion = Union[HlsPlaylistSettings, HlsPlaylistSettingsOutput]


class PrefetchConsumption(BaseValidatorModel):
    EndTime: Timestamp
    AvailMatchingCriteria: Optional[List[AvailMatchingCriteria]] = None
    StartTime: Optional[Timestamp] = None


class PrefetchRetrieval(BaseValidatorModel):
    EndTime: Timestamp
    DynamicVariables: Optional[Dict[str, str]] = None
    StartTime: Optional[Timestamp] = None


class ScheduleEntry(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ProgramName: str
    SourceLocationName: str
    ApproximateDurationSeconds: Optional[int] = None
    ApproximateStartTime: Optional[datetime] = None
    LiveSourceName: Optional[str] = None
    ScheduleAdBreaks: Optional[List[ScheduleAdBreak]] = None
    ScheduleEntryType: Optional[ScheduleEntryTypeType] = None
    VodSourceName: Optional[str] = None
    Audiences: Optional[List[str]] = None


class ScheduleConfiguration(BaseValidatorModel):
    Transition: Transition
    ClipRange: Optional[ClipRange] = None


class TimeSignalMessageOutput(BaseValidatorModel):
    SegmentationDescriptors: Optional[List[SegmentationDescriptor]] = None


class TimeSignalMessage(BaseValidatorModel):
    SegmentationDescriptors: Optional[List[SegmentationDescriptor]] = None


class UpdateProgramScheduleConfiguration(BaseValidatorModel):
    Transition: Optional[UpdateProgramTransition] = None
    ClipRange: Optional[ClipRange] = None


class CreateSourceLocationRequest(BaseValidatorModel):
    HttpConfiguration: HttpConfiguration
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfiguration] = None
    DefaultSegmentDeliveryConfiguration: Optional[DefaultSegmentDeliveryConfiguration] = None
    SegmentDeliveryConfigurations: Optional[List[SegmentDeliveryConfiguration]] = None
    Tags: Optional[Dict[str, str]] = None


class CreateSourceLocationResponse(BaseValidatorModel):
    AccessConfiguration: AccessConfiguration
    Arn: str
    CreationTime: datetime
    DefaultSegmentDeliveryConfiguration: DefaultSegmentDeliveryConfiguration
    HttpConfiguration: HttpConfiguration
    LastModifiedTime: datetime
    SegmentDeliveryConfigurations: List[SegmentDeliveryConfiguration]
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeSourceLocationResponse(BaseValidatorModel):
    AccessConfiguration: AccessConfiguration
    Arn: str
    CreationTime: datetime
    DefaultSegmentDeliveryConfiguration: DefaultSegmentDeliveryConfiguration
    HttpConfiguration: HttpConfiguration
    LastModifiedTime: datetime
    SegmentDeliveryConfigurations: List[SegmentDeliveryConfiguration]
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class SourceLocation(BaseValidatorModel):
    Arn: str
    HttpConfiguration: HttpConfiguration
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfiguration] = None
    CreationTime: Optional[datetime] = None
    DefaultSegmentDeliveryConfiguration: Optional[DefaultSegmentDeliveryConfiguration] = None
    LastModifiedTime: Optional[datetime] = None
    SegmentDeliveryConfigurations: Optional[List[SegmentDeliveryConfiguration]] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateSourceLocationRequest(BaseValidatorModel):
    HttpConfiguration: HttpConfiguration
    SourceLocationName: str
    AccessConfiguration: Optional[AccessConfiguration] = None
    DefaultSegmentDeliveryConfiguration: Optional[DefaultSegmentDeliveryConfiguration] = None
    SegmentDeliveryConfigurations: Optional[List[SegmentDeliveryConfiguration]] = None


class UpdateSourceLocationResponse(BaseValidatorModel):
    AccessConfiguration: AccessConfiguration
    Arn: str
    CreationTime: datetime
    DefaultSegmentDeliveryConfiguration: DefaultSegmentDeliveryConfiguration
    HttpConfiguration: HttpConfiguration
    LastModifiedTime: datetime
    SegmentDeliveryConfigurations: List[SegmentDeliveryConfiguration]
    SourceLocationName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetPlaybackConfigurationResponse(BaseValidatorModel):
    AdDecisionServerUrl: str
    AvailSuppression: AvailSuppression
    Bumper: Bumper
    CdnConfiguration: CdnConfiguration
    ConfigurationAliases: Dict[str, Dict[str, str]]
    DashConfiguration: DashConfiguration
    HlsConfiguration: HlsConfiguration
    InsertionMode: InsertionModeType
    LivePreRollConfiguration: LivePreRollConfiguration
    LogConfiguration: LogConfiguration
    ManifestProcessingRules: ManifestProcessingRules
    Name: str
    PersonalizationThresholdSeconds: int
    PlaybackConfigurationArn: str
    PlaybackEndpointPrefix: str
    SessionInitializationEndpointPrefix: str
    SlateAdUrl: str
    Tags: Dict[str, str]
    TranscodeProfileName: str
    VideoContentSourceUrl: str
    AdConditioningConfiguration: AdConditioningConfiguration
    ResponseMetadata: ResponseMetadata


class PlaybackConfiguration(BaseValidatorModel):
    AdDecisionServerUrl: Optional[str] = None
    AvailSuppression: Optional[AvailSuppression] = None
    Bumper: Optional[Bumper] = None
    CdnConfiguration: Optional[CdnConfiguration] = None
    ConfigurationAliases: Optional[Dict[str, Dict[str, str]]] = None
    DashConfiguration: Optional[DashConfiguration] = None
    HlsConfiguration: Optional[HlsConfiguration] = None
    InsertionMode: Optional[InsertionModeType] = None
    LivePreRollConfiguration: Optional[LivePreRollConfiguration] = None
    LogConfiguration: Optional[LogConfiguration] = None
    ManifestProcessingRules: Optional[ManifestProcessingRules] = None
    Name: Optional[str] = None
    PersonalizationThresholdSeconds: Optional[int] = None
    PlaybackConfigurationArn: Optional[str] = None
    PlaybackEndpointPrefix: Optional[str] = None
    SessionInitializationEndpointPrefix: Optional[str] = None
    SlateAdUrl: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    TranscodeProfileName: Optional[str] = None
    VideoContentSourceUrl: Optional[str] = None
    AdConditioningConfiguration: Optional[AdConditioningConfiguration] = None


class PutPlaybackConfigurationRequest(BaseValidatorModel):
    Name: str
    AdDecisionServerUrl: Optional[str] = None
    AvailSuppression: Optional[AvailSuppression] = None
    Bumper: Optional[Bumper] = None
    CdnConfiguration: Optional[CdnConfiguration] = None
    ConfigurationAliases: Optional[Dict[str, Dict[str, str]]] = None
    DashConfiguration: Optional[DashConfigurationForPut] = None
    InsertionMode: Optional[InsertionModeType] = None
    LivePreRollConfiguration: Optional[LivePreRollConfiguration] = None
    ManifestProcessingRules: Optional[ManifestProcessingRules] = None
    PersonalizationThresholdSeconds: Optional[int] = None
    SlateAdUrl: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    TranscodeProfileName: Optional[str] = None
    VideoContentSourceUrl: Optional[str] = None
    AdConditioningConfiguration: Optional[AdConditioningConfiguration] = None


class PutPlaybackConfigurationResponse(BaseValidatorModel):
    AdDecisionServerUrl: str
    AvailSuppression: AvailSuppression
    Bumper: Bumper
    CdnConfiguration: CdnConfiguration
    ConfigurationAliases: Dict[str, Dict[str, str]]
    DashConfiguration: DashConfiguration
    HlsConfiguration: HlsConfiguration
    InsertionMode: InsertionModeType
    LivePreRollConfiguration: LivePreRollConfiguration
    LogConfiguration: LogConfiguration
    ManifestProcessingRules: ManifestProcessingRules
    Name: str
    PersonalizationThresholdSeconds: int
    PlaybackConfigurationArn: str
    PlaybackEndpointPrefix: str
    SessionInitializationEndpointPrefix: str
    SlateAdUrl: str
    Tags: Dict[str, str]
    TranscodeProfileName: str
    VideoContentSourceUrl: str
    AdConditioningConfiguration: AdConditioningConfiguration
    ResponseMetadata: ResponseMetadata


class CreatePrefetchScheduleResponse(BaseValidatorModel):
    Arn: str
    Consumption: PrefetchConsumptionOutput
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalOutput
    StreamId: str
    ResponseMetadata: ResponseMetadata


class GetPrefetchScheduleResponse(BaseValidatorModel):
    Arn: str
    Consumption: PrefetchConsumptionOutput
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalOutput
    StreamId: str
    ResponseMetadata: ResponseMetadata


class PrefetchSchedule(BaseValidatorModel):
    Arn: str
    Consumption: PrefetchConsumptionOutput
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalOutput
    StreamId: Optional[str] = None


class ListLiveSourcesResponse(BaseValidatorModel):
    Items: List[LiveSource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListVodSourcesResponse(BaseValidatorModel):
    Items: List[VodSource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Channel(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelState: str
    Outputs: List[ResponseOutputItem]
    PlaybackMode: str
    Tier: str
    LogConfiguration: LogConfigurationForChannel
    CreationTime: Optional[datetime] = None
    FillerSlate: Optional[SlateSource] = None
    LastModifiedTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    Audiences: Optional[List[str]] = None


class CreateChannelResponse(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelState: ChannelStateType
    CreationTime: datetime
    FillerSlate: SlateSource
    LastModifiedTime: datetime
    Outputs: List[ResponseOutputItem]
    PlaybackMode: str
    Tags: Dict[str, str]
    Tier: str
    TimeShiftConfiguration: TimeShiftConfiguration
    Audiences: List[str]
    ResponseMetadata: ResponseMetadata


class DescribeChannelResponse(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelState: ChannelStateType
    CreationTime: datetime
    FillerSlate: SlateSource
    LastModifiedTime: datetime
    Outputs: List[ResponseOutputItem]
    PlaybackMode: str
    Tags: Dict[str, str]
    Tier: str
    LogConfiguration: LogConfigurationForChannel
    TimeShiftConfiguration: TimeShiftConfiguration
    Audiences: List[str]
    ResponseMetadata: ResponseMetadata


class UpdateChannelResponse(BaseValidatorModel):
    Arn: str
    ChannelName: str
    ChannelState: ChannelStateType
    CreationTime: datetime
    FillerSlate: SlateSource
    LastModifiedTime: datetime
    Outputs: List[ResponseOutputItem]
    PlaybackMode: str
    Tags: Dict[str, str]
    Tier: str
    TimeShiftConfiguration: TimeShiftConfiguration
    Audiences: List[str]
    ResponseMetadata: ResponseMetadata


class RequestOutputItem(BaseValidatorModel):
    ManifestName: str
    SourceGroup: str
    DashPlaylistSettings: Optional[DashPlaylistSettings] = None
    HlsPlaylistSettings: Optional[HlsPlaylistSettingsUnion] = None

PrefetchConsumptionUnion = Union[PrefetchConsumption, PrefetchConsumptionOutput]

PrefetchRetrievalUnion = Union[PrefetchRetrieval, PrefetchRetrievalOutput]


class GetChannelScheduleResponse(BaseValidatorModel):
    Items: List[ScheduleEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AdBreakOutput(BaseValidatorModel):
    OffsetMillis: int
    MessageType: Optional[MessageTypeType] = None
    Slate: Optional[SlateSource] = None
    SpliceInsertMessage: Optional[SpliceInsertMessage] = None
    TimeSignalMessage: Optional[TimeSignalMessageOutput] = None
    AdBreakMetadata: Optional[List[KeyValuePair]] = None

TimeSignalMessageUnion = Union[TimeSignalMessage, TimeSignalMessageOutput]


class ListSourceLocationsResponse(BaseValidatorModel):
    Items: List[SourceLocation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPlaybackConfigurationsResponse(BaseValidatorModel):
    Items: List[PlaybackConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPrefetchSchedulesResponse(BaseValidatorModel):
    Items: List[PrefetchSchedule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListChannelsResponse(BaseValidatorModel):
    Items: List[Channel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateChannelRequest(BaseValidatorModel):
    ChannelName: str
    Outputs: List[RequestOutputItem]
    PlaybackMode: PlaybackModeType
    FillerSlate: Optional[SlateSource] = None
    Tags: Optional[Dict[str, str]] = None
    Tier: Optional[TierType] = None
    TimeShiftConfiguration: Optional[TimeShiftConfiguration] = None
    Audiences: Optional[List[str]] = None


class UpdateChannelRequest(BaseValidatorModel):
    ChannelName: str
    Outputs: List[RequestOutputItem]
    FillerSlate: Optional[SlateSource] = None
    TimeShiftConfiguration: Optional[TimeShiftConfiguration] = None
    Audiences: Optional[List[str]] = None


class CreatePrefetchScheduleRequest(BaseValidatorModel):
    Consumption: PrefetchConsumptionUnion
    Name: str
    PlaybackConfigurationName: str
    Retrieval: PrefetchRetrievalUnion
    StreamId: Optional[str] = None


class AlternateMediaOutput(BaseValidatorModel):
    SourceLocationName: Optional[str] = None
    LiveSourceName: Optional[str] = None
    VodSourceName: Optional[str] = None
    ClipRange: Optional[ClipRange] = None
    ScheduledStartTimeMillis: Optional[int] = None
    AdBreaks: Optional[List[AdBreakOutput]] = None
    DurationMillis: Optional[int] = None


class AdBreak(BaseValidatorModel):
    OffsetMillis: int
    MessageType: Optional[MessageTypeType] = None
    Slate: Optional[SlateSource] = None
    SpliceInsertMessage: Optional[SpliceInsertMessage] = None
    TimeSignalMessage: Optional[TimeSignalMessageUnion] = None
    AdBreakMetadata: Optional[List[KeyValuePair]] = None


class AudienceMediaOutput(BaseValidatorModel):
    Audience: Optional[str] = None
    AlternateMedia: Optional[List[AlternateMediaOutput]] = None

AdBreakUnion = Union[AdBreak, AdBreakOutput]


class CreateProgramResponse(BaseValidatorModel):
    AdBreaks: List[AdBreakOutput]
    Arn: str
    ChannelName: str
    CreationTime: datetime
    LiveSourceName: str
    ProgramName: str
    ScheduledStartTime: datetime
    SourceLocationName: str
    VodSourceName: str
    ClipRange: ClipRange
    DurationMillis: int
    AudienceMedia: List[AudienceMediaOutput]
    ResponseMetadata: ResponseMetadata


class DescribeProgramResponse(BaseValidatorModel):
    AdBreaks: List[AdBreakOutput]
    Arn: str
    ChannelName: str
    CreationTime: datetime
    LiveSourceName: str
    ProgramName: str
    ScheduledStartTime: datetime
    SourceLocationName: str
    VodSourceName: str
    ClipRange: ClipRange
    DurationMillis: int
    AudienceMedia: List[AudienceMediaOutput]
    ResponseMetadata: ResponseMetadata


class UpdateProgramResponse(BaseValidatorModel):
    AdBreaks: List[AdBreakOutput]
    Arn: str
    ChannelName: str
    CreationTime: datetime
    ProgramName: str
    SourceLocationName: str
    VodSourceName: str
    LiveSourceName: str
    ClipRange: ClipRange
    DurationMillis: int
    ScheduledStartTime: datetime
    AudienceMedia: List[AudienceMediaOutput]
    ResponseMetadata: ResponseMetadata


class AlternateMedia(BaseValidatorModel):
    SourceLocationName: Optional[str] = None
    LiveSourceName: Optional[str] = None
    VodSourceName: Optional[str] = None
    ClipRange: Optional[ClipRange] = None
    ScheduledStartTimeMillis: Optional[int] = None
    AdBreaks: Optional[List[AdBreakUnion]] = None
    DurationMillis: Optional[int] = None

AlternateMediaUnion = Union[AlternateMedia, AlternateMediaOutput]


class AudienceMedia(BaseValidatorModel):
    Audience: Optional[str] = None
    AlternateMedia: Optional[List[AlternateMediaUnion]] = None

AudienceMediaUnion = Union[AudienceMedia, AudienceMediaOutput]


class CreateProgramRequest(BaseValidatorModel):
    ChannelName: str
    ProgramName: str
    ScheduleConfiguration: ScheduleConfiguration
    SourceLocationName: str
    AdBreaks: Optional[List[AdBreakUnion]] = None
    LiveSourceName: Optional[str] = None
    VodSourceName: Optional[str] = None
    AudienceMedia: Optional[List[AudienceMediaUnion]] = None


class UpdateProgramRequest(BaseValidatorModel):
    ChannelName: str
    ProgramName: str
    ScheduleConfiguration: UpdateProgramScheduleConfiguration
    AdBreaks: Optional[List[AdBreakUnion]] = None
    AudienceMedia: Optional[List[AudienceMediaUnion]] = None