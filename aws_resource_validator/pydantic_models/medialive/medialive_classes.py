from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.medialive.medialive_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AacSettings(BaseValidatorModel):
    Bitrate: Optional[float] = None
    CodingMode: Optional[AacCodingModeType] = None
    InputType: Optional[AacInputTypeType] = None
    Profile: Optional[AacProfileType] = None
    RateControlMode: Optional[AacRateControlModeType] = None
    RawFormat: Optional[AacRawFormatType] = None
    SampleRate: Optional[float] = None
    Spec: Optional[AacSpecType] = None
    VbrQuality: Optional[AacVbrQualityType] = None


class Ac3Settings(BaseValidatorModel):
    Bitrate: Optional[float] = None
    BitstreamMode: Optional[Ac3BitstreamModeType] = None
    CodingMode: Optional[Ac3CodingModeType] = None
    Dialnorm: Optional[int] = None
    DrcProfile: Optional[Ac3DrcProfileType] = None
    LfeFilter: Optional[Ac3LfeFilterType] = None
    MetadataControl: Optional[Ac3MetadataControlType] = None
    AttenuationControl: Optional[Ac3AttenuationControlType] = None


class AcceptInputDeviceTransferRequest(BaseValidatorModel):
    InputDeviceId: str


class AccountConfiguration(BaseValidatorModel):
    KmsKeyId: Optional[str] = None


class AncillarySourceSettings(BaseValidatorModel):
    SourceAncillaryChannelNumber: Optional[int] = None


class AnywhereSettings(BaseValidatorModel):
    ChannelPlacementGroupId: Optional[str] = None
    ClusterId: Optional[str] = None


class ArchiveS3Settings(BaseValidatorModel):
    CannedAcl: Optional[S3CannedAclType] = None


class OutputLocationRef(BaseValidatorModel):
    DestinationRefId: Optional[str] = None


class InputChannelLevel(BaseValidatorModel):
    Gain: int
    InputChannel: int


class Eac3AtmosSettings(BaseValidatorModel):
    Bitrate: Optional[float] = None
    CodingMode: Optional[Eac3AtmosCodingModeType] = None
    Dialnorm: Optional[int] = None
    DrcLine: Optional[Eac3AtmosDrcLineType] = None
    DrcRf: Optional[Eac3AtmosDrcRfType] = None
    HeightTrim: Optional[float] = None
    SurroundTrim: Optional[float] = None


class Eac3Settings(BaseValidatorModel):
    AttenuationControl: Optional[Eac3AttenuationControlType] = None
    Bitrate: Optional[float] = None
    BitstreamMode: Optional[Eac3BitstreamModeType] = None
    CodingMode: Optional[Eac3CodingModeType] = None
    DcFilter: Optional[Eac3DcFilterType] = None
    Dialnorm: Optional[int] = None
    DrcLine: Optional[Eac3DrcLineType] = None
    DrcRf: Optional[Eac3DrcRfType] = None
    LfeControl: Optional[Eac3LfeControlType] = None
    LfeFilter: Optional[Eac3LfeFilterType] = None
    LoRoCenterMixLevel: Optional[float] = None
    LoRoSurroundMixLevel: Optional[float] = None
    LtRtCenterMixLevel: Optional[float] = None
    LtRtSurroundMixLevel: Optional[float] = None
    MetadataControl: Optional[Eac3MetadataControlType] = None
    PassthroughControl: Optional[Eac3PassthroughControlType] = None
    PhaseControl: Optional[Eac3PhaseControlType] = None
    StereoDownmix: Optional[Eac3StereoDownmixType] = None
    SurroundExMode: Optional[Eac3SurroundExModeType] = None
    SurroundMode: Optional[Eac3SurroundModeType] = None


class Mp2Settings(BaseValidatorModel):
    Bitrate: Optional[float] = None
    CodingMode: Optional[Mp2CodingModeType] = None
    SampleRate: Optional[float] = None


class WavSettings(BaseValidatorModel):
    BitDepth: Optional[float] = None
    CodingMode: Optional[WavCodingModeType] = None
    SampleRate: Optional[float] = None


class AudioNormalizationSettings(BaseValidatorModel):
    Algorithm: Optional[AudioNormalizationAlgorithmType] = None
    AlgorithmControl: Optional[Literal['CORRECT_AUDIO']] = None
    TargetLkfs: Optional[float] = None


class AudioDolbyEDecode(BaseValidatorModel):
    ProgramSelection: DolbyEProgramSelectionType


class AudioHlsRenditionSelection(BaseValidatorModel):
    GroupId: str
    Name: str


class AudioLanguageSelection(BaseValidatorModel):
    LanguageCode: str
    LanguageSelectionPolicy: Optional[AudioLanguageSelectionPolicyType] = None


class InputLocation(BaseValidatorModel):
    Uri: str
    PasswordParam: Optional[str] = None
    Username: Optional[str] = None


class AudioPidSelection(BaseValidatorModel):
    Pid: int


class AudioSilenceFailoverSettings(BaseValidatorModel):
    AudioSelectorName: str
    AudioSilenceThresholdMsec: Optional[int] = None


class AudioTrack(BaseValidatorModel):
    Track: int


class Hdr10Settings(BaseValidatorModel):
    MaxCll: Optional[int] = None
    MaxFall: Optional[int] = None


class TimecodeBurninSettings(BaseValidatorModel):
    FontSize: TimecodeBurninFontSizeType
    Position: TimecodeBurninPositionType
    Prefix: Optional[str] = None


class Esam(BaseValidatorModel):
    AcquisitionPointId: str
    PoisEndpoint: str
    AdAvailOffset: Optional[int] = None
    PasswordParam: Optional[str] = None
    Username: Optional[str] = None
    ZoneIdentity: Optional[str] = None


class Scte35SpliceInsert(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    NoRegionalBlackoutFlag: Optional[Scte35SpliceInsertNoRegionalBlackoutBehaviorType] = None
    WebDeliveryAllowedFlag: Optional[Scte35SpliceInsertWebDeliveryAllowedBehaviorType] = None


class Scte35TimeSignalApos(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    NoRegionalBlackoutFlag: Optional[Scte35AposNoRegionalBlackoutBehaviorType] = None
    WebDeliveryAllowedFlag: Optional[Scte35AposWebDeliveryAllowedBehaviorType] = None


class BandwidthReductionFilterSettings(BaseValidatorModel):
    PostFilterSharpening: Optional[BandwidthReductionPostFilterSharpeningType] = None
    Strength: Optional[BandwidthReductionFilterStrengthType] = None


class BatchDeleteRequest(BaseValidatorModel):
    ChannelIds: Optional[List[str]] = None
    InputIds: Optional[List[str]] = None
    InputSecurityGroupIds: Optional[List[str]] = None
    MultiplexIds: Optional[List[str]] = None


class BatchFailedResultModel(BaseValidatorModel):
    Arn: Optional[str] = None
    Code: Optional[str] = None
    Id: Optional[str] = None
    Message: Optional[str] = None


class BatchSuccessfulResultModel(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    State: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchScheduleActionDeleteRequest(BaseValidatorModel):
    ActionNames: List[str]


class BatchStartRequest(BaseValidatorModel):
    ChannelIds: Optional[List[str]] = None
    MultiplexIds: Optional[List[str]] = None


class BatchStopRequest(BaseValidatorModel):
    ChannelIds: Optional[List[str]] = None
    MultiplexIds: Optional[List[str]] = None


class CancelInputDeviceTransferRequest(BaseValidatorModel):
    InputDeviceId: str


class EbuTtDDestinationSettings(BaseValidatorModel):
    CopyrightHolder: Optional[str] = None
    FillLineGap: Optional[EbuTtDFillLineGapControlType] = None
    FontFamily: Optional[str] = None
    StyleControl: Optional[EbuTtDDestinationStyleControlType] = None
    DefaultFontSize: Optional[int] = None
    DefaultLineHeight: Optional[int] = None


class TtmlDestinationSettings(BaseValidatorModel):
    StyleControl: Optional[TtmlDestinationStyleControlType] = None


class WebvttDestinationSettings(BaseValidatorModel):
    StyleControl: Optional[WebvttDestinationStyleControlType] = None


class CaptionLanguageMapping(BaseValidatorModel):
    CaptionChannel: int
    LanguageCode: str
    LanguageDescription: str


class CaptionRectangle(BaseValidatorModel):
    Height: float
    LeftOffset: float
    TopOffset: float
    Width: float


class DvbSubSourceSettings(BaseValidatorModel):
    OcrLanguage: Optional[DvbSubOcrLanguageType] = None
    Pid: Optional[int] = None


class EmbeddedSourceSettings(BaseValidatorModel):
    Convert608To708: Optional[EmbeddedConvert608To708Type] = None
    Scte20Detection: Optional[EmbeddedScte20DetectionType] = None
    Source608ChannelNumber: Optional[int] = None
    Source608TrackNumber: Optional[int] = None


class Scte20SourceSettings(BaseValidatorModel):
    Convert608To708: Optional[Scte20Convert608To708Type] = None
    Source608ChannelNumber: Optional[int] = None


class Scte27SourceSettings(BaseValidatorModel):
    OcrLanguage: Optional[Scte27OcrLanguageType] = None
    Pid: Optional[int] = None


class CdiInputSpecification(BaseValidatorModel):
    Resolution: Optional[CdiInputResolutionType] = None


class ChannelEgressEndpoint(BaseValidatorModel):
    SourceIp: Optional[str] = None


class ChannelEngineVersionRequest(BaseValidatorModel):
    Version: Optional[str] = None


class ChannelEngineVersionResponse(BaseValidatorModel):
    ExpirationDate: Optional[datetime] = None
    Version: Optional[str] = None


class DescribeAnywhereSettings(BaseValidatorModel):
    ChannelPlacementGroupId: Optional[str] = None
    ClusterId: Optional[str] = None


class InputSpecification(BaseValidatorModel):
    Codec: Optional[InputCodecType] = None
    MaximumBitrate: Optional[InputMaximumBitrateType] = None
    Resolution: Optional[InputResolutionType] = None


class MaintenanceStatus(BaseValidatorModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceDeadline: Optional[str] = None
    MaintenanceScheduledDate: Optional[str] = None
    MaintenanceStartTime: Optional[str] = None


class VpcOutputSettingsDescription(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None


class ClaimDeviceRequest(BaseValidatorModel):
    Id: Optional[str] = None


class CloudWatchAlarmTemplateGroupSummary(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Id: str
    Name: str
    TemplateCount: int
    Description: Optional[str] = None
    ModifiedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class CloudWatchAlarmTemplateSummary(BaseValidatorModel):
    Arn: str
    ComparisonOperator: CloudWatchAlarmTemplateComparisonOperatorType
    CreatedAt: datetime
    EvaluationPeriods: int
    GroupId: str
    Id: str
    MetricName: str
    Name: str
    Period: int
    Statistic: CloudWatchAlarmTemplateStatisticType
    TargetResourceType: CloudWatchAlarmTemplateTargetResourceTypeType
    Threshold: float
    TreatMissingData: CloudWatchAlarmTemplateTreatMissingDataType
    DatapointsToAlarm: Optional[int] = None
    Description: Optional[str] = None
    ModifiedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class InterfaceMappingCreateRequest(BaseValidatorModel):
    LogicalInterfaceName: Optional[str] = None
    NetworkId: Optional[str] = None


class InterfaceMapping(BaseValidatorModel):
    LogicalInterfaceName: Optional[str] = None
    NetworkId: Optional[str] = None


class InterfaceMappingUpdateRequest(BaseValidatorModel):
    LogicalInterfaceName: Optional[str] = None
    NetworkId: Optional[str] = None


class CmafIngestOutputSettings(BaseValidatorModel):
    NameModifier: Optional[str] = None


class ColorCorrection(BaseValidatorModel):
    InputColorSpace: ColorSpaceType
    OutputColorSpace: ColorSpaceType
    Uri: str


class CreateChannelPlacementGroupRequest(BaseValidatorModel):
    ClusterId: str
    Name: Optional[str] = None
    Nodes: Optional[List[str]] = None
    RequestId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class MaintenanceCreateSettings(BaseValidatorModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceStartTime: Optional[str] = None


class VpcOutputSettings(BaseValidatorModel):
    SubnetIds: List[str]
    PublicAddressAllocationIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class CreateCloudWatchAlarmTemplateGroupRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    RequestId: Optional[str] = None


class CreateCloudWatchAlarmTemplateRequest(BaseValidatorModel):
    ComparisonOperator: CloudWatchAlarmTemplateComparisonOperatorType
    EvaluationPeriods: int
    GroupIdentifier: str
    MetricName: str
    Name: str
    Period: int
    Statistic: CloudWatchAlarmTemplateStatisticType
    TargetResourceType: CloudWatchAlarmTemplateTargetResourceTypeType
    Threshold: float
    TreatMissingData: CloudWatchAlarmTemplateTreatMissingDataType
    DatapointsToAlarm: Optional[int] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    RequestId: Optional[str] = None


class CreateEventBridgeRuleTemplateGroupRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    RequestId: Optional[str] = None


class EventBridgeRuleTemplateTarget(BaseValidatorModel):
    Arn: str


class InputDeviceSettings(BaseValidatorModel):
    Id: Optional[str] = None


class InputSourceRequest(BaseValidatorModel):
    PasswordParam: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None


class InputVpcRequest(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None


class MediaConnectFlowRequest(BaseValidatorModel):
    FlowArn: Optional[str] = None


class InputWhitelistRuleCidr(BaseValidatorModel):
    Cidr: Optional[str] = None


class MultiplexSettings(BaseValidatorModel):
    TransportStreamBitrate: int
    TransportStreamId: int
    MaximumVideoBufferDelayMilliseconds: Optional[int] = None
    TransportStreamReservedBitrate: Optional[int] = None


class IpPoolCreateRequest(BaseValidatorModel):
    Cidr: Optional[str] = None


class RouteCreateRequest(BaseValidatorModel):
    Cidr: Optional[str] = None
    Gateway: Optional[str] = None


class IpPool(BaseValidatorModel):
    Cidr: Optional[str] = None


class Route(BaseValidatorModel):
    Cidr: Optional[str] = None
    Gateway: Optional[str] = None


class NodeInterfaceMapping(BaseValidatorModel):
    LogicalInterfaceName: Optional[str] = None
    NetworkInterfaceMode: Optional[NetworkInterfaceModeType] = None
    PhysicalInterfaceName: Optional[str] = None


class NodeInterfaceMappingCreateRequest(BaseValidatorModel):
    LogicalInterfaceName: Optional[str] = None
    NetworkInterfaceMode: Optional[NetworkInterfaceModeType] = None
    PhysicalInterfaceName: Optional[str] = None


class CreatePartnerInputRequest(BaseValidatorModel):
    InputId: str
    RequestId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class CreateSignalMapRequest(BaseValidatorModel):
    DiscoveryEntryPointArn: str
    Name: str
    CloudWatchAlarmTemplateGroupIdentifiers: Optional[List[str]] = None
    Description: Optional[str] = None
    EventBridgeRuleTemplateGroupIdentifiers: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None
    RequestId: Optional[str] = None


class MonitorDeployment(BaseValidatorModel):
    Status: SignalMapMonitorDeploymentStatusType
    DetailsUri: Optional[str] = None
    ErrorMessage: Optional[str] = None


class SuccessfulMonitorDeployment(BaseValidatorModel):
    DetailsUri: str
    Status: SignalMapMonitorDeploymentStatusType


class CreateTagsRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Optional[Dict[str, str]] = None


class DeleteChannelPlacementGroupRequest(BaseValidatorModel):
    ChannelPlacementGroupId: str
    ClusterId: str


class DeleteChannelRequest(BaseValidatorModel):
    ChannelId: str


class DeleteCloudWatchAlarmTemplateGroupRequest(BaseValidatorModel):
    Identifier: str


class DeleteCloudWatchAlarmTemplateRequest(BaseValidatorModel):
    Identifier: str


class DeleteClusterRequest(BaseValidatorModel):
    ClusterId: str


class DeleteEventBridgeRuleTemplateGroupRequest(BaseValidatorModel):
    Identifier: str


class DeleteEventBridgeRuleTemplateRequest(BaseValidatorModel):
    Identifier: str


class DeleteInputRequest(BaseValidatorModel):
    InputId: str


class DeleteInputSecurityGroupRequest(BaseValidatorModel):
    InputSecurityGroupId: str


class DeleteMultiplexProgramRequest(BaseValidatorModel):
    MultiplexId: str
    ProgramName: str


class MultiplexProgramPacketIdentifiersMapOutput(BaseValidatorModel):
    AudioPids: Optional[List[int]] = None
    DvbSubPids: Optional[List[int]] = None
    DvbTeletextPid: Optional[int] = None
    EtvPlatformPid: Optional[int] = None
    EtvSignalPid: Optional[int] = None
    KlvDataPids: Optional[List[int]] = None
    PcrPid: Optional[int] = None
    PmtPid: Optional[int] = None
    PrivateMetadataPid: Optional[int] = None
    Scte27Pids: Optional[List[int]] = None
    Scte35Pid: Optional[int] = None
    TimedMetadataPid: Optional[int] = None
    VideoPid: Optional[int] = None
    AribCaptionsPid: Optional[int] = None
    DvbTeletextPids: Optional[List[int]] = None
    EcmPid: Optional[int] = None
    Smpte2038Pid: Optional[int] = None


class MultiplexProgramPipelineDetail(BaseValidatorModel):
    ActiveChannelPipeline: Optional[str] = None
    PipelineId: Optional[str] = None


class DeleteMultiplexRequest(BaseValidatorModel):
    MultiplexId: str


class DeleteNetworkRequest(BaseValidatorModel):
    NetworkId: str


class DeleteNodeRequest(BaseValidatorModel):
    ClusterId: str
    NodeId: str


class DeleteReservationRequest(BaseValidatorModel):
    ReservationId: str


class RenewalSettings(BaseValidatorModel):
    AutomaticRenewal: Optional[ReservationAutomaticRenewalType] = None
    RenewalCount: Optional[int] = None


class ReservationResourceSpecification(BaseValidatorModel):
    ChannelClass: Optional[ChannelClassType] = None
    Codec: Optional[ReservationCodecType] = None
    MaximumBitrate: Optional[ReservationMaximumBitrateType] = None
    MaximumFramerate: Optional[ReservationMaximumFramerateType] = None
    Resolution: Optional[ReservationResolutionType] = None
    ResourceType: Optional[ReservationResourceTypeType] = None
    SpecialFeature: Optional[ReservationSpecialFeatureType] = None
    VideoQuality: Optional[ReservationVideoQualityType] = None


class DeleteScheduleRequest(BaseValidatorModel):
    ChannelId: str


class DeleteSignalMapRequest(BaseValidatorModel):
    Identifier: str


class DeleteTagsRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class DescribeChannelPlacementGroupRequest(BaseValidatorModel):
    ChannelPlacementGroupId: str
    ClusterId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeChannelPlacementGroupSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Channels: Optional[List[str]] = None
    ClusterId: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Nodes: Optional[List[str]] = None
    State: Optional[ChannelPlacementGroupStateType] = None


class DescribeChannelRequest(BaseValidatorModel):
    ChannelId: str


class DescribeClusterRequest(BaseValidatorModel):
    ClusterId: str


class DescribeInputDeviceRequest(BaseValidatorModel):
    InputDeviceId: str


class InputDeviceHdSettings(BaseValidatorModel):
    ActiveInput: Optional[InputDeviceActiveInputType] = None
    ConfiguredInput: Optional[InputDeviceConfiguredInputType] = None
    DeviceState: Optional[InputDeviceStateType] = None
    Framerate: Optional[float] = None
    Height: Optional[int] = None
    MaxBitrate: Optional[int] = None
    ScanType: Optional[InputDeviceScanTypeType] = None
    Width: Optional[int] = None
    LatencyMs: Optional[int] = None


class InputDeviceNetworkSettings(BaseValidatorModel):
    DnsAddresses: Optional[List[str]] = None
    Gateway: Optional[str] = None
    IpAddress: Optional[str] = None
    IpScheme: Optional[InputDeviceIpSchemeType] = None
    SubnetMask: Optional[str] = None


class DescribeInputDeviceThumbnailRequest(BaseValidatorModel):
    InputDeviceId: str
    Accept: Literal['image/jpeg']


class DescribeInputRequest(BaseValidatorModel):
    InputId: str


class InputSource(BaseValidatorModel):
    PasswordParam: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None


class MediaConnectFlow(BaseValidatorModel):
    FlowArn: Optional[str] = None


class DescribeInputSecurityGroupRequest(BaseValidatorModel):
    InputSecurityGroupId: str


class InputWhitelistRule(BaseValidatorModel):
    Cidr: Optional[str] = None


class DescribeMultiplexProgramRequest(BaseValidatorModel):
    MultiplexId: str
    ProgramName: str


class DescribeMultiplexRequest(BaseValidatorModel):
    MultiplexId: str


class DescribeNetworkRequest(BaseValidatorModel):
    NetworkId: str


class DescribeNodeRequest(BaseValidatorModel):
    ClusterId: str
    NodeId: str


class DescribeOfferingRequest(BaseValidatorModel):
    OfferingId: str


class DescribeReservationRequest(BaseValidatorModel):
    ReservationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeScheduleRequest(BaseValidatorModel):
    ChannelId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeThumbnailsRequest(BaseValidatorModel):
    ChannelId: str
    PipelineId: str
    ThumbnailType: str


class DvbNitSettings(BaseValidatorModel):
    NetworkId: int
    NetworkName: str
    RepInterval: Optional[int] = None


class DvbSdtSettings(BaseValidatorModel):
    OutputSdt: Optional[DvbSdtOutputSdtType] = None
    RepInterval: Optional[int] = None
    ServiceName: Optional[str] = None
    ServiceProviderName: Optional[str] = None


class DvbTdtSettings(BaseValidatorModel):
    RepInterval: Optional[int] = None


class FeatureActivations(BaseValidatorModel):
    InputPrepareScheduleActions: Optional[FeatureActivationsInputPrepareScheduleActionsType] = None
    OutputStaticImageOverlayScheduleActions: Optional[FeatureActivationsOutputStaticImageOverlayScheduleActionsType] = None


class NielsenConfiguration(BaseValidatorModel):
    DistributorId: Optional[str] = None
    NielsenPcmToId3Tagging: Optional[NielsenPcmToId3TaggingStateType] = None


class ThumbnailConfiguration(BaseValidatorModel):
    State: ThumbnailStateType


class TimecodeConfig(BaseValidatorModel):
    Source: TimecodeConfigSourceType
    SyncThreshold: Optional[int] = None


class EpochLockingSettings(BaseValidatorModel):
    CustomEpoch: Optional[str] = None
    JamSyncTime: Optional[str] = None


class EventBridgeRuleTemplateGroupSummary(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Id: str
    Name: str
    TemplateCount: int
    Description: Optional[str] = None
    ModifiedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class EventBridgeRuleTemplateSummary(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    EventTargetCount: int
    EventType: EventBridgeRuleTemplateEventTypeType
    GroupId: str
    Id: str
    Name: str
    Description: Optional[str] = None
    ModifiedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class InputLossFailoverSettings(BaseValidatorModel):
    InputLossThresholdMsec: Optional[int] = None


class VideoBlackFailoverSettings(BaseValidatorModel):
    BlackDetectThreshold: Optional[float] = None
    VideoBlackThresholdMsec: Optional[int] = None


class FecOutputSettings(BaseValidatorModel):
    ColumnDepth: Optional[int] = None
    IncludeFec: Optional[FecOutputIncludeFecType] = None
    RowLength: Optional[int] = None


class FixedModeScheduleActionStartSettings(BaseValidatorModel):
    Time: str


class Fmp4HlsSettings(BaseValidatorModel):
    AudioRenditionSets: Optional[str] = None
    NielsenId3Behavior: Optional[Fmp4NielsenId3BehaviorType] = None
    TimedMetadataBehavior: Optional[Fmp4TimedMetadataBehaviorType] = None


class FollowModeScheduleActionStartSettings(BaseValidatorModel):
    FollowPoint: FollowPointType
    ReferenceActionName: str


class FrameCaptureS3Settings(BaseValidatorModel):
    CannedAcl: Optional[S3CannedAclType] = None


class FrameCaptureOutputSettings(BaseValidatorModel):
    NameModifier: Optional[str] = None


class GetCloudWatchAlarmTemplateGroupRequest(BaseValidatorModel):
    Identifier: str


class GetCloudWatchAlarmTemplateRequest(BaseValidatorModel):
    Identifier: str


class GetEventBridgeRuleTemplateGroupRequest(BaseValidatorModel):
    Identifier: str


class GetEventBridgeRuleTemplateRequest(BaseValidatorModel):
    Identifier: str


class GetSignalMapRequest(BaseValidatorModel):
    Identifier: str


class H264ColorSpaceSettingsOutput(BaseValidatorModel):
    ColorSpacePassthroughSettings: Optional[Dict[str, Any]] = None
    Rec601Settings: Optional[Dict[str, Any]] = None
    Rec709Settings: Optional[Dict[str, Any]] = None


class H264ColorSpaceSettings(BaseValidatorModel):
    ColorSpacePassthroughSettings: Optional[Dict[str, Any]] = None
    Rec601Settings: Optional[Dict[str, Any]] = None
    Rec709Settings: Optional[Dict[str, Any]] = None


class TemporalFilterSettings(BaseValidatorModel):
    PostFilterSharpening: Optional[TemporalFilterPostFilterSharpeningType] = None
    Strength: Optional[TemporalFilterStrengthType] = None


class HlsAkamaiSettings(BaseValidatorModel):
    ConnectionRetryInterval: Optional[int] = None
    FilecacheDuration: Optional[int] = None
    HttpTransferMode: Optional[HlsAkamaiHttpTransferModeType] = None
    NumRetries: Optional[int] = None
    RestartDelay: Optional[int] = None
    Salt: Optional[str] = None
    Token: Optional[str] = None


class HlsBasicPutSettings(BaseValidatorModel):
    ConnectionRetryInterval: Optional[int] = None
    FilecacheDuration: Optional[int] = None
    NumRetries: Optional[int] = None
    RestartDelay: Optional[int] = None


class HlsMediaStoreSettings(BaseValidatorModel):
    ConnectionRetryInterval: Optional[int] = None
    FilecacheDuration: Optional[int] = None
    MediaStoreStorageClass: Optional[Literal['TEMPORAL']] = None
    NumRetries: Optional[int] = None
    RestartDelay: Optional[int] = None


class HlsS3Settings(BaseValidatorModel):
    CannedAcl: Optional[S3CannedAclType] = None


class HlsWebdavSettings(BaseValidatorModel):
    ConnectionRetryInterval: Optional[int] = None
    FilecacheDuration: Optional[int] = None
    HttpTransferMode: Optional[HlsWebdavHttpTransferModeType] = None
    NumRetries: Optional[int] = None
    RestartDelay: Optional[int] = None


class HlsId3SegmentTaggingScheduleActionSettings(BaseValidatorModel):
    Tag: Optional[str] = None
    Id3: Optional[str] = None


class HlsInputSettings(BaseValidatorModel):
    Bandwidth: Optional[int] = None
    BufferSegments: Optional[int] = None
    Retries: Optional[int] = None
    RetryInterval: Optional[int] = None
    Scte35Source: Optional[HlsScte35SourceTypeType] = None


class HlsTimedMetadataScheduleActionSettings(BaseValidatorModel):
    Id3: str


class Id3SegmentTaggingScheduleActionSettings(BaseValidatorModel):
    Id3: Optional[str] = None
    Tag: Optional[str] = None


class StartTimecode(BaseValidatorModel):
    Timecode: Optional[str] = None


class StopTimecode(BaseValidatorModel):
    LastFrameClippingBehavior: Optional[LastFrameClippingBehaviorType] = None
    Timecode: Optional[str] = None


class InputRequestDestinationRoute(BaseValidatorModel):
    Cidr: Optional[str] = None
    Gateway: Optional[str] = None


class InputDestinationRoute(BaseValidatorModel):
    Cidr: Optional[str] = None
    Gateway: Optional[str] = None


class InputDestinationVpc(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None


class InputDeviceConfigurableAudioChannelPairConfig(BaseValidatorModel):
    Id: Optional[int] = None
    Profile: Optional[InputDeviceConfigurableAudioChannelPairProfileType] = None


class InputDeviceMediaConnectConfigurableSettings(BaseValidatorModel):
    FlowArn: Optional[str] = None
    RoleArn: Optional[str] = None
    SecretArn: Optional[str] = None
    SourceName: Optional[str] = None


class InputDeviceMediaConnectSettings(BaseValidatorModel):
    FlowArn: Optional[str] = None
    RoleArn: Optional[str] = None
    SecretArn: Optional[str] = None
    SourceName: Optional[str] = None


class InputDeviceRequest(BaseValidatorModel):
    Id: Optional[str] = None


class InputDeviceUhdAudioChannelPairConfig(BaseValidatorModel):
    Id: Optional[int] = None
    Profile: Optional[InputDeviceUhdAudioChannelPairProfileType] = None


class IpPoolUpdateRequest(BaseValidatorModel):
    Cidr: Optional[str] = None


class ListChannelPlacementGroupsRequest(BaseValidatorModel):
    ClusterId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListChannelsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCloudWatchAlarmTemplateGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Scope: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None


class ListCloudWatchAlarmTemplatesRequest(BaseValidatorModel):
    GroupIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Scope: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None


class ListClustersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEventBridgeRuleTemplateGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None


class ListEventBridgeRuleTemplatesRequest(BaseValidatorModel):
    GroupIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None


class ListInputDeviceTransfersRequest(BaseValidatorModel):
    TransferType: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TransferringInputDeviceSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Message: Optional[str] = None
    TargetCustomerId: Optional[str] = None
    TransferType: Optional[InputDeviceTransferTypeType] = None


class ListInputDevicesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInputSecurityGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInputsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMultiplexProgramsRequest(BaseValidatorModel):
    MultiplexId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MultiplexProgramSummary(BaseValidatorModel):
    ChannelId: Optional[str] = None
    ProgramName: Optional[str] = None


class ListMultiplexesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListNetworksRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListNodesRequest(BaseValidatorModel):
    ClusterId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOfferingsRequest(BaseValidatorModel):
    ChannelClass: Optional[str] = None
    ChannelConfiguration: Optional[str] = None
    Codec: Optional[str] = None
    Duration: Optional[str] = None
    MaxResults: Optional[int] = None
    MaximumBitrate: Optional[str] = None
    MaximumFramerate: Optional[str] = None
    NextToken: Optional[str] = None
    Resolution: Optional[str] = None
    ResourceType: Optional[str] = None
    SpecialFeature: Optional[str] = None
    VideoQuality: Optional[str] = None


class ListReservationsRequest(BaseValidatorModel):
    ChannelClass: Optional[str] = None
    Codec: Optional[str] = None
    MaxResults: Optional[int] = None
    MaximumBitrate: Optional[str] = None
    MaximumFramerate: Optional[str] = None
    NextToken: Optional[str] = None
    Resolution: Optional[str] = None
    ResourceType: Optional[str] = None
    SpecialFeature: Optional[str] = None
    VideoQuality: Optional[str] = None


class ListSignalMapsRequest(BaseValidatorModel):
    CloudWatchAlarmTemplateGroupIdentifier: Optional[str] = None
    EventBridgeRuleTemplateGroupIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SignalMapSummary(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Id: str
    MonitorDeploymentStatus: SignalMapMonitorDeploymentStatusType
    Name: str
    Status: SignalMapStatusType
    Description: Optional[str] = None
    ModifiedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class M3u8Settings(BaseValidatorModel):
    AudioFramesPerPes: Optional[int] = None
    AudioPids: Optional[str] = None
    EcmPid: Optional[str] = None
    NielsenId3Behavior: Optional[M3u8NielsenId3BehaviorType] = None
    PatInterval: Optional[int] = None
    PcrControl: Optional[M3u8PcrControlType] = None
    PcrPeriod: Optional[int] = None
    PcrPid: Optional[str] = None
    PmtInterval: Optional[int] = None
    PmtPid: Optional[str] = None
    ProgramNum: Optional[int] = None
    Scte35Behavior: Optional[M3u8Scte35BehaviorType] = None
    Scte35Pid: Optional[str] = None
    TimedMetadataBehavior: Optional[M3u8TimedMetadataBehaviorType] = None
    TimedMetadataPid: Optional[str] = None
    TransportStreamId: Optional[int] = None
    VideoPid: Optional[str] = None
    KlvBehavior: Optional[M3u8KlvBehaviorType] = None
    KlvDataPids: Optional[str] = None


class MaintenanceUpdateSettings(BaseValidatorModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceScheduledDate: Optional[str] = None
    MaintenanceStartTime: Optional[str] = None


class MediaPackageOutputDestinationSettings(BaseValidatorModel):
    ChannelId: Optional[str] = None
    ChannelGroup: Optional[str] = None
    ChannelName: Optional[str] = None


class MediaResourceNeighbor(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None


class MotionGraphicsActivateScheduleActionSettings(BaseValidatorModel):
    Duration: Optional[int] = None
    PasswordParam: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None


class MotionGraphicsSettingsOutput(BaseValidatorModel):
    HtmlMotionGraphicsSettings: Optional[Dict[str, Any]] = None


class MotionGraphicsSettings(BaseValidatorModel):
    HtmlMotionGraphicsSettings: Optional[Dict[str, Any]] = None


class MsSmoothOutputSettings(BaseValidatorModel):
    H265PackagingType: Optional[MsSmoothH265PackagingTypeType] = None
    NameModifier: Optional[str] = None


class MulticastInputSettings(BaseValidatorModel):
    SourceIpAddress: Optional[str] = None


class MulticastSourceCreateRequest(BaseValidatorModel):
    Url: str
    SourceIp: Optional[str] = None


class MulticastSource(BaseValidatorModel):
    Url: str
    SourceIp: Optional[str] = None


class MulticastSourceUpdateRequest(BaseValidatorModel):
    Url: str
    SourceIp: Optional[str] = None


class MultiplexM2tsSettings(BaseValidatorModel):
    AbsentInputAudioBehavior: Optional[M2tsAbsentInputAudioBehaviorType] = None
    Arib: Optional[M2tsAribType] = None
    AudioBufferModel: Optional[M2tsAudioBufferModelType] = None
    AudioFramesPerPes: Optional[int] = None
    AudioStreamType: Optional[M2tsAudioStreamTypeType] = None
    CcDescriptor: Optional[M2tsCcDescriptorType] = None
    Ebif: Optional[M2tsEbifControlType] = None
    EsRateInPes: Optional[M2tsEsRateInPesType] = None
    Klv: Optional[M2tsKlvType] = None
    NielsenId3Behavior: Optional[M2tsNielsenId3BehaviorType] = None
    PcrControl: Optional[M2tsPcrControlType] = None
    PcrPeriod: Optional[int] = None
    Scte35Control: Optional[M2tsScte35ControlType] = None
    Scte35PrerollPullupMilliseconds: Optional[float] = None


class MultiplexMediaConnectOutputDestinationSettings(BaseValidatorModel):
    EntitlementArn: Optional[str] = None


class MultiplexProgramChannelDestinationSettings(BaseValidatorModel):
    MultiplexId: Optional[str] = None
    ProgramName: Optional[str] = None


class MultiplexProgramPacketIdentifiersMap(BaseValidatorModel):
    AudioPids: Optional[List[int]] = None
    DvbSubPids: Optional[List[int]] = None
    DvbTeletextPid: Optional[int] = None
    EtvPlatformPid: Optional[int] = None
    EtvSignalPid: Optional[int] = None
    KlvDataPids: Optional[List[int]] = None
    PcrPid: Optional[int] = None
    PmtPid: Optional[int] = None
    PrivateMetadataPid: Optional[int] = None
    Scte27Pids: Optional[List[int]] = None
    Scte35Pid: Optional[int] = None
    TimedMetadataPid: Optional[int] = None
    VideoPid: Optional[int] = None
    AribCaptionsPid: Optional[int] = None
    DvbTeletextPids: Optional[List[int]] = None
    EcmPid: Optional[int] = None
    Smpte2038Pid: Optional[int] = None


class MultiplexProgramServiceDescriptor(BaseValidatorModel):
    ProviderName: str
    ServiceName: str


class MultiplexSettingsSummary(BaseValidatorModel):
    TransportStreamBitrate: Optional[int] = None


class MultiplexStatmuxVideoSettings(BaseValidatorModel):
    MaximumBitrate: Optional[int] = None
    MinimumBitrate: Optional[int] = None
    Priority: Optional[int] = None


class NielsenCBET(BaseValidatorModel):
    CbetCheckDigitString: str
    CbetStepaside: NielsenWatermarksCbetStepasideType
    Csid: str


class NielsenNaesIiNw(BaseValidatorModel):
    CheckDigitString: str
    Sid: float
    Timezone: Optional[NielsenWatermarkTimezonesType] = None


class OutputDestinationSettings(BaseValidatorModel):
    PasswordParam: Optional[str] = None
    StreamName: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None


class SrtOutputDestinationSettings(BaseValidatorModel):
    EncryptionPassphraseSecretArn: Optional[str] = None
    StreamId: Optional[str] = None
    Url: Optional[str] = None


class RtmpGroupSettingsOutput(BaseValidatorModel):
    AdMarkers: Optional[List[Literal['ON_CUE_POINT_SCTE35']]] = None
    AuthenticationScheme: Optional[AuthenticationSchemeType] = None
    CacheFullBehavior: Optional[RtmpCacheFullBehaviorType] = None
    CacheLength: Optional[int] = None
    CaptionData: Optional[RtmpCaptionDataType] = None
    InputLossAction: Optional[InputLossActionForRtmpOutType] = None
    RestartDelay: Optional[int] = None
    IncludeFillerNalUnits: Optional[IncludeFillerNalUnitsType] = None


class SrtGroupSettings(BaseValidatorModel):
    InputLossAction: Optional[InputLossActionForUdpOutType] = None


class UdpGroupSettings(BaseValidatorModel):
    InputLossAction: Optional[InputLossActionForUdpOutType] = None
    TimedMetadataId3Frame: Optional[UdpTimedMetadataId3FrameType] = None
    TimedMetadataId3Period: Optional[int] = None


class RtmpGroupSettings(BaseValidatorModel):
    AdMarkers: Optional[List[Literal['ON_CUE_POINT_SCTE35']]] = None
    AuthenticationScheme: Optional[AuthenticationSchemeType] = None
    CacheFullBehavior: Optional[RtmpCacheFullBehaviorType] = None
    CacheLength: Optional[int] = None
    CaptionData: Optional[RtmpCaptionDataType] = None
    InputLossAction: Optional[InputLossActionForRtmpOutType] = None
    RestartDelay: Optional[int] = None
    IncludeFillerNalUnits: Optional[IncludeFillerNalUnitsType] = None


class PipelinePauseStateSettings(BaseValidatorModel):
    PipelineId: PipelineIdType


class RebootInputDeviceRequest(BaseValidatorModel):
    InputDeviceId: str
    Force: Optional[RebootInputDeviceForceType] = None


class RejectInputDeviceTransferRequest(BaseValidatorModel):
    InputDeviceId: str


class RestartChannelPipelinesRequest(BaseValidatorModel):
    ChannelId: str
    PipelineIds: Optional[List[ChannelPipelineIdToRestartType]] = None


class RouteUpdateRequest(BaseValidatorModel):
    Cidr: Optional[str] = None
    Gateway: Optional[str] = None


class Scte35InputScheduleActionSettings(BaseValidatorModel):
    Mode: Scte35InputModeType
    InputAttachmentNameReference: Optional[str] = None


class Scte35ReturnToNetworkScheduleActionSettings(BaseValidatorModel):
    SpliceEventId: int


class Scte35SpliceInsertScheduleActionSettings(BaseValidatorModel):
    SpliceEventId: int
    Duration: Optional[int] = None


class StaticImageDeactivateScheduleActionSettings(BaseValidatorModel):
    FadeOut: Optional[int] = None
    Layer: Optional[int] = None


class StaticImageOutputDeactivateScheduleActionSettingsOutput(BaseValidatorModel):
    OutputNames: List[str]
    FadeOut: Optional[int] = None
    Layer: Optional[int] = None


class TimedMetadataScheduleActionSettings(BaseValidatorModel):
    Id3: str


class Scte35DeliveryRestrictions(BaseValidatorModel):
    ArchiveAllowedFlag: Scte35ArchiveAllowedFlagType
    DeviceRestrictions: Scte35DeviceRestrictionsType
    NoRegionalBlackoutFlag: Scte35NoRegionalBlackoutFlagType
    WebDeliveryAllowedFlag: Scte35WebDeliveryAllowedFlagType


class SrtCallerDecryptionRequest(BaseValidatorModel):
    Algorithm: Optional[AlgorithmType] = None
    PassphraseSecretArn: Optional[str] = None


class SrtCallerDecryption(BaseValidatorModel):
    Algorithm: Optional[AlgorithmType] = None
    PassphraseSecretArn: Optional[str] = None


class StartChannelRequest(BaseValidatorModel):
    ChannelId: str


class StartDeleteMonitorDeploymentRequest(BaseValidatorModel):
    Identifier: str


class StartInputDeviceMaintenanceWindowRequest(BaseValidatorModel):
    InputDeviceId: str


class StartInputDeviceRequest(BaseValidatorModel):
    InputDeviceId: str


class StartMonitorDeploymentRequest(BaseValidatorModel):
    Identifier: str
    DryRun: Optional[bool] = None


class StartMultiplexRequest(BaseValidatorModel):
    MultiplexId: str


class StartUpdateSignalMapRequest(BaseValidatorModel):
    Identifier: str
    CloudWatchAlarmTemplateGroupIdentifiers: Optional[List[str]] = None
    Description: Optional[str] = None
    DiscoveryEntryPointArn: Optional[str] = None
    EventBridgeRuleTemplateGroupIdentifiers: Optional[List[str]] = None
    ForceRediscovery: Optional[bool] = None
    Name: Optional[str] = None


class StaticImageOutputDeactivateScheduleActionSettings(BaseValidatorModel):
    OutputNames: List[str]
    FadeOut: Optional[int] = None
    Layer: Optional[int] = None


class StopChannelRequest(BaseValidatorModel):
    ChannelId: str


class StopInputDeviceRequest(BaseValidatorModel):
    InputDeviceId: str


class StopMultiplexRequest(BaseValidatorModel):
    MultiplexId: str


class Thumbnail(BaseValidatorModel):
    Body: Optional[str] = None
    ContentType: Optional[str] = None
    ThumbnailType: Optional[ThumbnailTypeType] = None
    TimeStamp: Optional[datetime] = None


class TransferInputDeviceRequest(BaseValidatorModel):
    InputDeviceId: str
    TargetCustomerId: Optional[str] = None
    TargetRegion: Optional[str] = None
    TransferMessage: Optional[str] = None


class UpdateChannelPlacementGroupRequest(BaseValidatorModel):
    ChannelPlacementGroupId: str
    ClusterId: str
    Name: Optional[str] = None
    Nodes: Optional[List[str]] = None


class UpdateCloudWatchAlarmTemplateGroupRequest(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None


class UpdateCloudWatchAlarmTemplateRequest(BaseValidatorModel):
    Identifier: str
    ComparisonOperator: Optional[CloudWatchAlarmTemplateComparisonOperatorType] = None
    DatapointsToAlarm: Optional[int] = None
    Description: Optional[str] = None
    EvaluationPeriods: Optional[int] = None
    GroupIdentifier: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    Period: Optional[int] = None
    Statistic: Optional[CloudWatchAlarmTemplateStatisticType] = None
    TargetResourceType: Optional[CloudWatchAlarmTemplateTargetResourceTypeType] = None
    Threshold: Optional[float] = None
    TreatMissingData: Optional[CloudWatchAlarmTemplateTreatMissingDataType] = None


class UpdateEventBridgeRuleTemplateGroupRequest(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None


class UpdateNodeRequest(BaseValidatorModel):
    ClusterId: str
    NodeId: str
    Name: Optional[str] = None
    Role: Optional[NodeRoleType] = None


class UpdateNodeStateRequest(BaseValidatorModel):
    ClusterId: str
    NodeId: str
    State: Optional[UpdateNodeStateType] = None


class VideoSelectorPid(BaseValidatorModel):
    Pid: Optional[int] = None


class VideoSelectorProgramId(BaseValidatorModel):
    ProgramId: Optional[int] = None


class UpdateAccountConfigurationRequest(BaseValidatorModel):
    AccountConfiguration: Optional[AccountConfiguration] = None


class ArchiveCdnSettings(BaseValidatorModel):
    ArchiveS3Settings: Optional[ArchiveS3Settings] = None


class CmafIngestGroupSettings(BaseValidatorModel):
    Destination: OutputLocationRef
    NielsenId3Behavior: Optional[CmafNielsenId3BehaviorType] = None
    Scte35Type: Optional[Scte35TypeType] = None
    SegmentLength: Optional[int] = None
    SegmentLengthUnits: Optional[CmafIngestSegmentLengthUnitsType] = None
    SendDelayMs: Optional[int] = None
    KlvBehavior: Optional[CmafKLVBehaviorType] = None
    KlvNameModifier: Optional[str] = None
    NielsenId3NameModifier: Optional[str] = None
    Scte35NameModifier: Optional[str] = None
    Id3Behavior: Optional[CmafId3BehaviorType] = None
    Id3NameModifier: Optional[str] = None


class MediaPackageGroupSettings(BaseValidatorModel):
    Destination: OutputLocationRef


class MsSmoothGroupSettings(BaseValidatorModel):
    Destination: OutputLocationRef
    AcquisitionPointId: Optional[str] = None
    AudioOnlyTimecodeControl: Optional[SmoothGroupAudioOnlyTimecodeControlType] = None
    CertificateMode: Optional[SmoothGroupCertificateModeType] = None
    ConnectionRetryInterval: Optional[int] = None
    EventId: Optional[str] = None
    EventIdMode: Optional[SmoothGroupEventIdModeType] = None
    EventStopBehavior: Optional[SmoothGroupEventStopBehaviorType] = None
    FilecacheDuration: Optional[int] = None
    FragmentLength: Optional[int] = None
    InputLossAction: Optional[InputLossActionForMsSmoothOutType] = None
    NumRetries: Optional[int] = None
    RestartDelay: Optional[int] = None
    SegmentationMode: Optional[SmoothGroupSegmentationModeType] = None
    SendDelayMs: Optional[int] = None
    SparseTrackType: Optional[SmoothGroupSparseTrackTypeType] = None
    StreamManifestBehavior: Optional[SmoothGroupStreamManifestBehaviorType] = None
    TimestampOffset: Optional[str] = None
    TimestampOffsetMode: Optional[SmoothGroupTimestampOffsetModeType] = None


class RtmpOutputSettings(BaseValidatorModel):
    Destination: OutputLocationRef
    CertificateMode: Optional[RtmpOutputCertificateModeType] = None
    ConnectionRetryInterval: Optional[int] = None
    NumRetries: Optional[int] = None


class AudioChannelMappingOutput(BaseValidatorModel):
    InputChannelLevels: List[InputChannelLevel]
    OutputChannel: int


class AudioChannelMapping(BaseValidatorModel):
    InputChannelLevels: List[InputChannelLevel]
    OutputChannel: int


class AudioCodecSettingsOutput(BaseValidatorModel):
    AacSettings: Optional[AacSettings] = None
    Ac3Settings: Optional[Ac3Settings] = None
    Eac3AtmosSettings: Optional[Eac3AtmosSettings] = None
    Eac3Settings: Optional[Eac3Settings] = None
    Mp2Settings: Optional[Mp2Settings] = None
    PassThroughSettings: Optional[Dict[str, Any]] = None
    WavSettings: Optional[WavSettings] = None


class AudioCodecSettings(BaseValidatorModel):
    AacSettings: Optional[AacSettings] = None
    Ac3Settings: Optional[Ac3Settings] = None
    Eac3AtmosSettings: Optional[Eac3AtmosSettings] = None
    Eac3Settings: Optional[Eac3Settings] = None
    Mp2Settings: Optional[Mp2Settings] = None
    PassThroughSettings: Optional[Dict[str, Any]] = None
    WavSettings: Optional[WavSettings] = None


class AudioOnlyHlsSettings(BaseValidatorModel):
    AudioGroupId: Optional[str] = None
    AudioOnlyImage: Optional[InputLocation] = None
    AudioTrackType: Optional[AudioOnlyHlsTrackTypeType] = None
    SegmentType: Optional[AudioOnlyHlsSegmentTypeType] = None


class AvailBlanking(BaseValidatorModel):
    AvailBlankingImage: Optional[InputLocation] = None
    State: Optional[AvailBlankingStateType] = None


class BlackoutSlate(BaseValidatorModel):
    BlackoutSlateImage: Optional[InputLocation] = None
    NetworkEndBlackout: Optional[BlackoutSlateNetworkEndBlackoutType] = None
    NetworkEndBlackoutImage: Optional[InputLocation] = None
    NetworkId: Optional[str] = None
    State: Optional[BlackoutSlateStateType] = None


class BurnInDestinationSettings(BaseValidatorModel):
    Alignment: Optional[BurnInAlignmentType] = None
    BackgroundColor: Optional[BurnInBackgroundColorType] = None
    BackgroundOpacity: Optional[int] = None
    Font: Optional[InputLocation] = None
    FontColor: Optional[BurnInFontColorType] = None
    FontOpacity: Optional[int] = None
    FontResolution: Optional[int] = None
    FontSize: Optional[str] = None
    OutlineColor: Optional[BurnInOutlineColorType] = None
    OutlineSize: Optional[int] = None
    ShadowColor: Optional[BurnInShadowColorType] = None
    ShadowOpacity: Optional[int] = None
    ShadowXOffset: Optional[int] = None
    ShadowYOffset: Optional[int] = None
    TeletextGridControl: Optional[BurnInTeletextGridControlType] = None
    XPosition: Optional[int] = None
    YPosition: Optional[int] = None


class DvbSubDestinationSettings(BaseValidatorModel):
    Alignment: Optional[DvbSubDestinationAlignmentType] = None
    BackgroundColor: Optional[DvbSubDestinationBackgroundColorType] = None
    BackgroundOpacity: Optional[int] = None
    Font: Optional[InputLocation] = None
    FontColor: Optional[DvbSubDestinationFontColorType] = None
    FontOpacity: Optional[int] = None
    FontResolution: Optional[int] = None
    FontSize: Optional[str] = None
    OutlineColor: Optional[DvbSubDestinationOutlineColorType] = None
    OutlineSize: Optional[int] = None
    ShadowColor: Optional[DvbSubDestinationShadowColorType] = None
    ShadowOpacity: Optional[int] = None
    ShadowXOffset: Optional[int] = None
    ShadowYOffset: Optional[int] = None
    TeletextGridControl: Optional[DvbSubDestinationTeletextGridControlType] = None
    XPosition: Optional[int] = None
    YPosition: Optional[int] = None


class InputLossBehavior(BaseValidatorModel):
    BlackFrameMsec: Optional[int] = None
    InputLossImageColor: Optional[str] = None
    InputLossImageSlate: Optional[InputLocation] = None
    InputLossImageType: Optional[InputLossImageTypeType] = None
    RepeatFrameMsec: Optional[int] = None


class StaticImageActivateScheduleActionSettings(BaseValidatorModel):
    Image: InputLocation
    Duration: Optional[int] = None
    FadeIn: Optional[int] = None
    FadeOut: Optional[int] = None
    Height: Optional[int] = None
    ImageX: Optional[int] = None
    ImageY: Optional[int] = None
    Layer: Optional[int] = None
    Opacity: Optional[int] = None
    Width: Optional[int] = None


class StaticImageOutputActivateScheduleActionSettingsOutput(BaseValidatorModel):
    Image: InputLocation
    OutputNames: List[str]
    Duration: Optional[int] = None
    FadeIn: Optional[int] = None
    FadeOut: Optional[int] = None
    Height: Optional[int] = None
    ImageX: Optional[int] = None
    ImageY: Optional[int] = None
    Layer: Optional[int] = None
    Opacity: Optional[int] = None
    Width: Optional[int] = None


class StaticImageOutputActivateScheduleActionSettings(BaseValidatorModel):
    Image: InputLocation
    OutputNames: List[str]
    Duration: Optional[int] = None
    FadeIn: Optional[int] = None
    FadeOut: Optional[int] = None
    Height: Optional[int] = None
    ImageX: Optional[int] = None
    ImageY: Optional[int] = None
    Layer: Optional[int] = None
    Opacity: Optional[int] = None
    Width: Optional[int] = None


class StaticKeySettings(BaseValidatorModel):
    StaticKeyValue: str
    KeyProviderServer: Optional[InputLocation] = None


class AudioTrackSelectionOutput(BaseValidatorModel):
    Tracks: List[AudioTrack]
    DolbyEDecode: Optional[AudioDolbyEDecode] = None


class AudioTrackSelection(BaseValidatorModel):
    Tracks: List[AudioTrack]
    DolbyEDecode: Optional[AudioDolbyEDecode] = None


class Av1ColorSpaceSettingsOutput(BaseValidatorModel):
    ColorSpacePassthroughSettings: Optional[Dict[str, Any]] = None
    Hdr10Settings: Optional[Hdr10Settings] = None
    Rec601Settings: Optional[Dict[str, Any]] = None
    Rec709Settings: Optional[Dict[str, Any]] = None


class Av1ColorSpaceSettings(BaseValidatorModel):
    ColorSpacePassthroughSettings: Optional[Dict[str, Any]] = None
    Hdr10Settings: Optional[Hdr10Settings] = None
    Rec601Settings: Optional[Dict[str, Any]] = None
    Rec709Settings: Optional[Dict[str, Any]] = None


class H265ColorSpaceSettingsOutput(BaseValidatorModel):
    ColorSpacePassthroughSettings: Optional[Dict[str, Any]] = None
    DolbyVision81Settings: Optional[Dict[str, Any]] = None
    Hdr10Settings: Optional[Hdr10Settings] = None
    Rec601Settings: Optional[Dict[str, Any]] = None
    Rec709Settings: Optional[Dict[str, Any]] = None


class H265ColorSpaceSettings(BaseValidatorModel):
    ColorSpacePassthroughSettings: Optional[Dict[str, Any]] = None
    DolbyVision81Settings: Optional[Dict[str, Any]] = None
    Hdr10Settings: Optional[Hdr10Settings] = None
    Rec601Settings: Optional[Dict[str, Any]] = None
    Rec709Settings: Optional[Dict[str, Any]] = None


class VideoSelectorColorSpaceSettings(BaseValidatorModel):
    Hdr10Settings: Optional[Hdr10Settings] = None


class FrameCaptureSettings(BaseValidatorModel):
    CaptureInterval: Optional[int] = None
    CaptureIntervalUnits: Optional[FrameCaptureIntervalUnitType] = None
    TimecodeBurninSettings: Optional[TimecodeBurninSettings] = None


class AvailSettings(BaseValidatorModel):
    Esam: Optional[Esam] = None
    Scte35SpliceInsert: Optional[Scte35SpliceInsert] = None
    Scte35TimeSignalApos: Optional[Scte35TimeSignalApos] = None


class BatchDeleteResponse(BaseValidatorModel):
    Failed: List[BatchFailedResultModel]
    Successful: List[BatchSuccessfulResultModel]
    ResponseMetadata: ResponseMetadata


class BatchStartResponse(BaseValidatorModel):
    Failed: List[BatchFailedResultModel]
    Successful: List[BatchSuccessfulResultModel]
    ResponseMetadata: ResponseMetadata


class BatchStopResponse(BaseValidatorModel):
    Failed: List[BatchFailedResultModel]
    Successful: List[BatchSuccessfulResultModel]
    ResponseMetadata: ResponseMetadata


class CreateChannelPlacementGroupResponse(BaseValidatorModel):
    Arn: str
    Channels: List[str]
    ClusterId: str
    Id: str
    Name: str
    Nodes: List[str]
    State: ChannelPlacementGroupStateType
    ResponseMetadata: ResponseMetadata


class CreateCloudWatchAlarmTemplateGroupResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateCloudWatchAlarmTemplateResponse(BaseValidatorModel):
    Arn: str
    ComparisonOperator: CloudWatchAlarmTemplateComparisonOperatorType
    CreatedAt: datetime
    DatapointsToAlarm: int
    Description: str
    EvaluationPeriods: int
    GroupId: str
    Id: str
    MetricName: str
    ModifiedAt: datetime
    Name: str
    Period: int
    Statistic: CloudWatchAlarmTemplateStatisticType
    Tags: Dict[str, str]
    TargetResourceType: CloudWatchAlarmTemplateTargetResourceTypeType
    Threshold: float
    TreatMissingData: CloudWatchAlarmTemplateTreatMissingDataType
    ResponseMetadata: ResponseMetadata


class CreateEventBridgeRuleTemplateGroupResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateNodeRegistrationScriptResponse(BaseValidatorModel):
    NodeRegistrationScript: str
    ResponseMetadata: ResponseMetadata


class DeleteChannelPlacementGroupResponse(BaseValidatorModel):
    Arn: str
    Channels: List[str]
    ClusterId: str
    Id: str
    Name: str
    Nodes: List[str]
    State: ChannelPlacementGroupStateType
    ResponseMetadata: ResponseMetadata


class DescribeAccountConfigurationResponse(BaseValidatorModel):
    AccountConfiguration: AccountConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeChannelPlacementGroupResponse(BaseValidatorModel):
    Arn: str
    Channels: List[str]
    ClusterId: str
    Id: str
    Name: str
    Nodes: List[str]
    State: ChannelPlacementGroupStateType
    ResponseMetadata: ResponseMetadata


class DescribeInputDeviceThumbnailResponse(BaseValidatorModel):
    Body: StreamingBody
    ContentType: Literal['image/jpeg']
    ContentLength: int
    ETag: str
    LastModified: datetime
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetCloudWatchAlarmTemplateGroupResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetCloudWatchAlarmTemplateResponse(BaseValidatorModel):
    Arn: str
    ComparisonOperator: CloudWatchAlarmTemplateComparisonOperatorType
    CreatedAt: datetime
    DatapointsToAlarm: int
    Description: str
    EvaluationPeriods: int
    GroupId: str
    Id: str
    MetricName: str
    ModifiedAt: datetime
    Name: str
    Period: int
    Statistic: CloudWatchAlarmTemplateStatisticType
    Tags: Dict[str, str]
    TargetResourceType: CloudWatchAlarmTemplateTargetResourceTypeType
    Threshold: float
    TreatMissingData: CloudWatchAlarmTemplateTreatMissingDataType
    ResponseMetadata: ResponseMetadata


class GetEventBridgeRuleTemplateGroupResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateAccountConfigurationResponse(BaseValidatorModel):
    AccountConfiguration: AccountConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateChannelPlacementGroupResponse(BaseValidatorModel):
    Arn: str
    Channels: List[str]
    ClusterId: str
    Id: str
    Name: str
    Nodes: List[str]
    State: ChannelPlacementGroupStateType
    ResponseMetadata: ResponseMetadata


class UpdateCloudWatchAlarmTemplateGroupResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateCloudWatchAlarmTemplateResponse(BaseValidatorModel):
    Arn: str
    ComparisonOperator: CloudWatchAlarmTemplateComparisonOperatorType
    CreatedAt: datetime
    DatapointsToAlarm: int
    Description: str
    EvaluationPeriods: int
    GroupId: str
    Id: str
    MetricName: str
    ModifiedAt: datetime
    Name: str
    Period: int
    Statistic: CloudWatchAlarmTemplateStatisticType
    Tags: Dict[str, str]
    TargetResourceType: CloudWatchAlarmTemplateTargetResourceTypeType
    Threshold: float
    TreatMissingData: CloudWatchAlarmTemplateTreatMissingDataType
    ResponseMetadata: ResponseMetadata


class UpdateEventBridgeRuleTemplateGroupResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class TeletextSourceSettings(BaseValidatorModel):
    OutputRectangle: Optional[CaptionRectangle] = None
    PageNumber: Optional[str] = None


class ListVersionsResponse(BaseValidatorModel):
    Versions: List[ChannelEngineVersionResponse]
    ResponseMetadata: ResponseMetadata


class PipelineDetail(BaseValidatorModel):
    ActiveInputAttachmentName: Optional[str] = None
    ActiveInputSwitchActionName: Optional[str] = None
    ActiveMotionGraphicsActionName: Optional[str] = None
    ActiveMotionGraphicsUri: Optional[str] = None
    PipelineId: Optional[str] = None
    ChannelEngineVersion: Optional[ChannelEngineVersionResponse] = None


class ListCloudWatchAlarmTemplateGroupsResponse(BaseValidatorModel):
    CloudWatchAlarmTemplateGroups: List[CloudWatchAlarmTemplateGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCloudWatchAlarmTemplatesResponse(BaseValidatorModel):
    CloudWatchAlarmTemplates: List[CloudWatchAlarmTemplateSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ClusterNetworkSettingsCreateRequest(BaseValidatorModel):
    DefaultRoute: Optional[str] = None
    InterfaceMappings: Optional[List[InterfaceMappingCreateRequest]] = None


class ClusterNetworkSettings(BaseValidatorModel):
    DefaultRoute: Optional[str] = None
    InterfaceMappings: Optional[List[InterfaceMapping]] = None


class ClusterNetworkSettingsUpdateRequest(BaseValidatorModel):
    DefaultRoute: Optional[str] = None
    InterfaceMappings: Optional[List[InterfaceMappingUpdateRequest]] = None


class ColorCorrectionSettingsOutput(BaseValidatorModel):
    GlobalColorCorrections: List[ColorCorrection]


class ColorCorrectionSettings(BaseValidatorModel):
    GlobalColorCorrections: List[ColorCorrection]


class CreateEventBridgeRuleTemplateRequest(BaseValidatorModel):
    EventType: EventBridgeRuleTemplateEventTypeType
    GroupIdentifier: str
    Name: str
    Description: Optional[str] = None
    EventTargets: Optional[List[EventBridgeRuleTemplateTarget]] = None
    Tags: Optional[Dict[str, str]] = None
    RequestId: Optional[str] = None


class CreateEventBridgeRuleTemplateResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    EventTargets: List[EventBridgeRuleTemplateTarget]
    EventType: EventBridgeRuleTemplateEventTypeType
    GroupId: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetEventBridgeRuleTemplateResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    EventTargets: List[EventBridgeRuleTemplateTarget]
    EventType: EventBridgeRuleTemplateEventTypeType
    GroupId: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateEventBridgeRuleTemplateRequest(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None
    EventTargets: Optional[List[EventBridgeRuleTemplateTarget]] = None
    EventType: Optional[EventBridgeRuleTemplateEventTypeType] = None
    GroupIdentifier: Optional[str] = None
    Name: Optional[str] = None


class UpdateEventBridgeRuleTemplateResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    EventTargets: List[EventBridgeRuleTemplateTarget]
    EventType: EventBridgeRuleTemplateEventTypeType
    GroupId: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateInputSecurityGroupRequest(BaseValidatorModel):
    Tags: Optional[Dict[str, str]] = None
    WhitelistRules: Optional[List[InputWhitelistRuleCidr]] = None


class UpdateInputSecurityGroupRequest(BaseValidatorModel):
    InputSecurityGroupId: str
    Tags: Optional[Dict[str, str]] = None
    WhitelistRules: Optional[List[InputWhitelistRuleCidr]] = None


class CreateMultiplexRequest(BaseValidatorModel):
    AvailabilityZones: List[str]
    MultiplexSettings: MultiplexSettings
    Name: str
    RequestId: str
    Tags: Optional[Dict[str, str]] = None


class CreateNetworkRequest(BaseValidatorModel):
    IpPools: Optional[List[IpPoolCreateRequest]] = None
    Name: Optional[str] = None
    RequestId: Optional[str] = None
    Routes: Optional[List[RouteCreateRequest]] = None
    Tags: Optional[Dict[str, str]] = None


class CreateNetworkResponse(BaseValidatorModel):
    Arn: str
    AssociatedClusterIds: List[str]
    Id: str
    IpPools: List[IpPool]
    Name: str
    Routes: List[Route]
    State: NetworkStateType
    ResponseMetadata: ResponseMetadata


class DeleteNetworkResponse(BaseValidatorModel):
    Arn: str
    AssociatedClusterIds: List[str]
    Id: str
    IpPools: List[IpPool]
    Name: str
    Routes: List[Route]
    State: NetworkStateType
    ResponseMetadata: ResponseMetadata


class DescribeNetworkResponse(BaseValidatorModel):
    Arn: str
    AssociatedClusterIds: List[str]
    Id: str
    IpPools: List[IpPool]
    Name: str
    Routes: List[Route]
    State: NetworkStateType
    ResponseMetadata: ResponseMetadata


class DescribeNetworkSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    AssociatedClusterIds: Optional[List[str]] = None
    Id: Optional[str] = None
    IpPools: Optional[List[IpPool]] = None
    Name: Optional[str] = None
    Routes: Optional[List[Route]] = None
    State: Optional[NetworkStateType] = None


class UpdateNetworkResponse(BaseValidatorModel):
    Arn: str
    AssociatedClusterIds: List[str]
    Id: str
    IpPools: List[IpPool]
    Name: str
    Routes: List[Route]
    State: NetworkStateType
    ResponseMetadata: ResponseMetadata


class CreateNodeRegistrationScriptRequest(BaseValidatorModel):
    ClusterId: str
    Id: Optional[str] = None
    Name: Optional[str] = None
    NodeInterfaceMappings: Optional[List[NodeInterfaceMapping]] = None
    RequestId: Optional[str] = None
    Role: Optional[NodeRoleType] = None


class CreateNodeResponse(BaseValidatorModel):
    Arn: str
    ChannelPlacementGroups: List[str]
    ClusterId: str
    ConnectionState: NodeConnectionStateType
    Id: str
    InstanceArn: str
    Name: str
    NodeInterfaceMappings: List[NodeInterfaceMapping]
    Role: NodeRoleType
    State: NodeStateType
    ResponseMetadata: ResponseMetadata


class DeleteNodeResponse(BaseValidatorModel):
    Arn: str
    ChannelPlacementGroups: List[str]
    ClusterId: str
    ConnectionState: NodeConnectionStateType
    Id: str
    InstanceArn: str
    Name: str
    NodeInterfaceMappings: List[NodeInterfaceMapping]
    Role: NodeRoleType
    State: NodeStateType
    ResponseMetadata: ResponseMetadata


class DescribeNodeResponse(BaseValidatorModel):
    Arn: str
    ChannelPlacementGroups: List[str]
    ClusterId: str
    ConnectionState: NodeConnectionStateType
    Id: str
    InstanceArn: str
    Name: str
    NodeInterfaceMappings: List[NodeInterfaceMapping]
    Role: NodeRoleType
    State: NodeStateType
    ResponseMetadata: ResponseMetadata


class DescribeNodeSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    ChannelPlacementGroups: Optional[List[str]] = None
    ClusterId: Optional[str] = None
    ConnectionState: Optional[NodeConnectionStateType] = None
    Id: Optional[str] = None
    InstanceArn: Optional[str] = None
    ManagedInstanceId: Optional[str] = None
    Name: Optional[str] = None
    NodeInterfaceMappings: Optional[List[NodeInterfaceMapping]] = None
    Role: Optional[NodeRoleType] = None
    State: Optional[NodeStateType] = None


class UpdateNodeResponse(BaseValidatorModel):
    Arn: str
    ChannelPlacementGroups: List[str]
    ClusterId: str
    ConnectionState: NodeConnectionStateType
    Id: str
    InstanceArn: str
    Name: str
    NodeInterfaceMappings: List[NodeInterfaceMapping]
    Role: NodeRoleType
    State: NodeStateType
    ResponseMetadata: ResponseMetadata


class UpdateNodeStateResponse(BaseValidatorModel):
    Arn: str
    ChannelPlacementGroups: List[str]
    ClusterId: str
    ConnectionState: NodeConnectionStateType
    Id: str
    InstanceArn: str
    Name: str
    NodeInterfaceMappings: List[NodeInterfaceMapping]
    Role: NodeRoleType
    State: NodeStateType
    ResponseMetadata: ResponseMetadata


class CreateNodeRequest(BaseValidatorModel):
    ClusterId: str
    Name: Optional[str] = None
    NodeInterfaceMappings: Optional[List[NodeInterfaceMappingCreateRequest]] = None
    RequestId: Optional[str] = None
    Role: Optional[NodeRoleType] = None
    Tags: Optional[Dict[str, str]] = None


class PurchaseOfferingRequest(BaseValidatorModel):
    Count: int
    OfferingId: str
    Name: Optional[str] = None
    RenewalSettings: Optional[RenewalSettings] = None
    RequestId: Optional[str] = None
    Start: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateReservationRequest(BaseValidatorModel):
    ReservationId: str
    Name: Optional[str] = None
    RenewalSettings: Optional[RenewalSettings] = None


class DeleteReservationResponse(BaseValidatorModel):
    Arn: str
    Count: int
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal['MONTHS']
    End: str
    FixedPrice: float
    Name: str
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal['NO_UPFRONT']
    Region: str
    RenewalSettings: RenewalSettings
    ReservationId: str
    ResourceSpecification: ReservationResourceSpecification
    Start: str
    State: ReservationStateType
    Tags: Dict[str, str]
    UsagePrice: float
    ResponseMetadata: ResponseMetadata


class DescribeOfferingResponse(BaseValidatorModel):
    Arn: str
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal['MONTHS']
    FixedPrice: float
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal['NO_UPFRONT']
    Region: str
    ResourceSpecification: ReservationResourceSpecification
    UsagePrice: float
    ResponseMetadata: ResponseMetadata


class DescribeReservationResponse(BaseValidatorModel):
    Arn: str
    Count: int
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal['MONTHS']
    End: str
    FixedPrice: float
    Name: str
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal['NO_UPFRONT']
    Region: str
    RenewalSettings: RenewalSettings
    ReservationId: str
    ResourceSpecification: ReservationResourceSpecification
    Start: str
    State: ReservationStateType
    Tags: Dict[str, str]
    UsagePrice: float
    ResponseMetadata: ResponseMetadata


class Offering(BaseValidatorModel):
    Arn: Optional[str] = None
    CurrencyCode: Optional[str] = None
    Duration: Optional[int] = None
    DurationUnits: Optional[Literal['MONTHS']] = None
    FixedPrice: Optional[float] = None
    OfferingDescription: Optional[str] = None
    OfferingId: Optional[str] = None
    OfferingType: Optional[Literal['NO_UPFRONT']] = None
    Region: Optional[str] = None
    ResourceSpecification: Optional[ReservationResourceSpecification] = None
    UsagePrice: Optional[float] = None


class Reservation(BaseValidatorModel):
    Arn: Optional[str] = None
    Count: Optional[int] = None
    CurrencyCode: Optional[str] = None
    Duration: Optional[int] = None
    DurationUnits: Optional[Literal['MONTHS']] = None
    End: Optional[str] = None
    FixedPrice: Optional[float] = None
    Name: Optional[str] = None
    OfferingDescription: Optional[str] = None
    OfferingId: Optional[str] = None
    OfferingType: Optional[Literal['NO_UPFRONT']] = None
    Region: Optional[str] = None
    RenewalSettings: Optional[RenewalSettings] = None
    ReservationId: Optional[str] = None
    ResourceSpecification: Optional[ReservationResourceSpecification] = None
    Start: Optional[str] = None
    State: Optional[ReservationStateType] = None
    Tags: Optional[Dict[str, str]] = None
    UsagePrice: Optional[float] = None


class DescribeChannelPlacementGroupRequestWaitExtraExtra(BaseValidatorModel):
    ChannelPlacementGroupId: str
    ClusterId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeChannelPlacementGroupRequestWaitExtra(BaseValidatorModel):
    ChannelPlacementGroupId: str
    ClusterId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeChannelPlacementGroupRequestWait(BaseValidatorModel):
    ChannelPlacementGroupId: str
    ClusterId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeChannelRequestWaitExtraExtraExtra(BaseValidatorModel):
    ChannelId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeChannelRequestWaitExtraExtra(BaseValidatorModel):
    ChannelId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeChannelRequestWaitExtra(BaseValidatorModel):
    ChannelId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeChannelRequestWait(BaseValidatorModel):
    ChannelId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClusterRequestWaitExtra(BaseValidatorModel):
    ClusterId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClusterRequestWait(BaseValidatorModel):
    ClusterId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInputRequestWaitExtraExtra(BaseValidatorModel):
    InputId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInputRequestWaitExtra(BaseValidatorModel):
    InputId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInputRequestWait(BaseValidatorModel):
    InputId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeMultiplexRequestWaitExtraExtraExtra(BaseValidatorModel):
    MultiplexId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeMultiplexRequestWaitExtraExtra(BaseValidatorModel):
    MultiplexId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeMultiplexRequestWaitExtra(BaseValidatorModel):
    MultiplexId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeMultiplexRequestWait(BaseValidatorModel):
    MultiplexId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeNodeRequestWaitExtra(BaseValidatorModel):
    ClusterId: str
    NodeId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeNodeRequestWait(BaseValidatorModel):
    ClusterId: str
    NodeId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetSignalMapRequestWaitExtraExtraExtra(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetSignalMapRequestWaitExtraExtra(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetSignalMapRequestWaitExtra(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetSignalMapRequestWait(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class ListChannelPlacementGroupsResponse(BaseValidatorModel):
    ChannelPlacementGroups: List[DescribeChannelPlacementGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInputSecurityGroupResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Inputs: List[str]
    State: InputSecurityGroupStateType
    Tags: Dict[str, str]
    WhitelistRules: List[InputWhitelistRule]
    ResponseMetadata: ResponseMetadata


class InputSecurityGroup(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Inputs: Optional[List[str]] = None
    State: Optional[InputSecurityGroupStateType] = None
    Tags: Optional[Dict[str, str]] = None
    WhitelistRules: Optional[List[InputWhitelistRule]] = None


class DescribeScheduleRequestPaginate(BaseValidatorModel):
    ChannelId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListChannelPlacementGroupsRequestPaginate(BaseValidatorModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListChannelsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCloudWatchAlarmTemplateGroupsRequestPaginate(BaseValidatorModel):
    Scope: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCloudWatchAlarmTemplatesRequestPaginate(BaseValidatorModel):
    GroupIdentifier: Optional[str] = None
    Scope: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClustersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventBridgeRuleTemplateGroupsRequestPaginate(BaseValidatorModel):
    SignalMapIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventBridgeRuleTemplatesRequestPaginate(BaseValidatorModel):
    GroupIdentifier: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInputDeviceTransfersRequestPaginate(BaseValidatorModel):
    TransferType: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInputDevicesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInputSecurityGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInputsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMultiplexProgramsRequestPaginate(BaseValidatorModel):
    MultiplexId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMultiplexesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNetworksRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNodesRequestPaginate(BaseValidatorModel):
    ClusterId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOfferingsRequestPaginate(BaseValidatorModel):
    ChannelClass: Optional[str] = None
    ChannelConfiguration: Optional[str] = None
    Codec: Optional[str] = None
    Duration: Optional[str] = None
    MaximumBitrate: Optional[str] = None
    MaximumFramerate: Optional[str] = None
    Resolution: Optional[str] = None
    ResourceType: Optional[str] = None
    SpecialFeature: Optional[str] = None
    VideoQuality: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReservationsRequestPaginate(BaseValidatorModel):
    ChannelClass: Optional[str] = None
    Codec: Optional[str] = None
    MaximumBitrate: Optional[str] = None
    MaximumFramerate: Optional[str] = None
    Resolution: Optional[str] = None
    ResourceType: Optional[str] = None
    SpecialFeature: Optional[str] = None
    VideoQuality: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSignalMapsRequestPaginate(BaseValidatorModel):
    CloudWatchAlarmTemplateGroupIdentifier: Optional[str] = None
    EventBridgeRuleTemplateGroupIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class M2tsSettings(BaseValidatorModel):
    AbsentInputAudioBehavior: Optional[M2tsAbsentInputAudioBehaviorType] = None
    Arib: Optional[M2tsAribType] = None
    AribCaptionsPid: Optional[str] = None
    AribCaptionsPidControl: Optional[M2tsAribCaptionsPidControlType] = None
    AudioBufferModel: Optional[M2tsAudioBufferModelType] = None
    AudioFramesPerPes: Optional[int] = None
    AudioPids: Optional[str] = None
    AudioStreamType: Optional[M2tsAudioStreamTypeType] = None
    Bitrate: Optional[int] = None
    BufferModel: Optional[M2tsBufferModelType] = None
    CcDescriptor: Optional[M2tsCcDescriptorType] = None
    DvbNitSettings: Optional[DvbNitSettings] = None
    DvbSdtSettings: Optional[DvbSdtSettings] = None
    DvbSubPids: Optional[str] = None
    DvbTdtSettings: Optional[DvbTdtSettings] = None
    DvbTeletextPid: Optional[str] = None
    Ebif: Optional[M2tsEbifControlType] = None
    EbpAudioInterval: Optional[M2tsAudioIntervalType] = None
    EbpLookaheadMs: Optional[int] = None
    EbpPlacement: Optional[M2tsEbpPlacementType] = None
    EcmPid: Optional[str] = None
    EsRateInPes: Optional[M2tsEsRateInPesType] = None
    EtvPlatformPid: Optional[str] = None
    EtvSignalPid: Optional[str] = None
    FragmentTime: Optional[float] = None
    Klv: Optional[M2tsKlvType] = None
    KlvDataPids: Optional[str] = None
    NielsenId3Behavior: Optional[M2tsNielsenId3BehaviorType] = None
    NullPacketBitrate: Optional[float] = None
    PatInterval: Optional[int] = None
    PcrControl: Optional[M2tsPcrControlType] = None
    PcrPeriod: Optional[int] = None
    PcrPid: Optional[str] = None
    PmtInterval: Optional[int] = None
    PmtPid: Optional[str] = None
    ProgramNum: Optional[int] = None
    RateMode: Optional[M2tsRateModeType] = None
    Scte27Pids: Optional[str] = None
    Scte35Control: Optional[M2tsScte35ControlType] = None
    Scte35Pid: Optional[str] = None
    SegmentationMarkers: Optional[M2tsSegmentationMarkersType] = None
    SegmentationStyle: Optional[M2tsSegmentationStyleType] = None
    SegmentationTime: Optional[float] = None
    TimedMetadataBehavior: Optional[M2tsTimedMetadataBehaviorType] = None
    TimedMetadataPid: Optional[str] = None
    TransportStreamId: Optional[int] = None
    VideoPid: Optional[str] = None
    Scte35PrerollPullupMilliseconds: Optional[float] = None


class OutputLockingSettingsOutput(BaseValidatorModel):
    EpochLockingSettings: Optional[EpochLockingSettings] = None
    PipelineLockingSettings: Optional[Dict[str, Any]] = None


class OutputLockingSettings(BaseValidatorModel):
    EpochLockingSettings: Optional[EpochLockingSettings] = None
    PipelineLockingSettings: Optional[Dict[str, Any]] = None


class ListEventBridgeRuleTemplateGroupsResponse(BaseValidatorModel):
    EventBridgeRuleTemplateGroups: List[EventBridgeRuleTemplateGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEventBridgeRuleTemplatesResponse(BaseValidatorModel):
    EventBridgeRuleTemplates: List[EventBridgeRuleTemplateSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FailoverConditionSettings(BaseValidatorModel):
    AudioSilenceSettings: Optional[AudioSilenceFailoverSettings] = None
    InputLossSettings: Optional[InputLossFailoverSettings] = None
    VideoBlackSettings: Optional[VideoBlackFailoverSettings] = None


class ScheduleActionStartSettingsOutput(BaseValidatorModel):
    FixedModeScheduleActionStartSettings: Optional[FixedModeScheduleActionStartSettings] = None
    FollowModeScheduleActionStartSettings: Optional[FollowModeScheduleActionStartSettings] = None
    ImmediateModeScheduleActionStartSettings: Optional[Dict[str, Any]] = None


class ScheduleActionStartSettings(BaseValidatorModel):
    FixedModeScheduleActionStartSettings: Optional[FixedModeScheduleActionStartSettings] = None
    FollowModeScheduleActionStartSettings: Optional[FollowModeScheduleActionStartSettings] = None
    ImmediateModeScheduleActionStartSettings: Optional[Dict[str, Any]] = None


class FrameCaptureCdnSettings(BaseValidatorModel):
    FrameCaptureS3Settings: Optional[FrameCaptureS3Settings] = None


class H264FilterSettings(BaseValidatorModel):
    TemporalFilterSettings: Optional[TemporalFilterSettings] = None
    BandwidthReductionFilterSettings: Optional[BandwidthReductionFilterSettings] = None


class H265FilterSettings(BaseValidatorModel):
    TemporalFilterSettings: Optional[TemporalFilterSettings] = None
    BandwidthReductionFilterSettings: Optional[BandwidthReductionFilterSettings] = None


class Mpeg2FilterSettings(BaseValidatorModel):
    TemporalFilterSettings: Optional[TemporalFilterSettings] = None


class HlsCdnSettings(BaseValidatorModel):
    HlsAkamaiSettings: Optional[HlsAkamaiSettings] = None
    HlsBasicPutSettings: Optional[HlsBasicPutSettings] = None
    HlsMediaStoreSettings: Optional[HlsMediaStoreSettings] = None
    HlsS3Settings: Optional[HlsS3Settings] = None
    HlsWebdavSettings: Optional[HlsWebdavSettings] = None


class InputClippingSettings(BaseValidatorModel):
    InputTimecodeSource: InputTimecodeSourceType
    StartTimecode: Optional[StartTimecode] = None
    StopTimecode: Optional[StopTimecode] = None


class InputDestinationRequest(BaseValidatorModel):
    StreamName: Optional[str] = None
    Network: Optional[str] = None
    NetworkRoutes: Optional[List[InputRequestDestinationRoute]] = None
    StaticIpAddress: Optional[str] = None


class InputDestination(BaseValidatorModel):
    Ip: Optional[str] = None
    Port: Optional[str] = None
    Url: Optional[str] = None
    Vpc: Optional[InputDestinationVpc] = None
    Network: Optional[str] = None
    NetworkRoutes: Optional[List[InputDestinationRoute]] = None


class InputDeviceConfigurableSettings(BaseValidatorModel):
    ConfiguredInput: Optional[InputDeviceConfiguredInputType] = None
    MaxBitrate: Optional[int] = None
    LatencyMs: Optional[int] = None
    Codec: Optional[InputDeviceCodecType] = None
    MediaconnectSettings: Optional[InputDeviceMediaConnectConfigurableSettings] = None
    AudioChannelPairs: Optional[List[InputDeviceConfigurableAudioChannelPairConfig]] = None


class InputDeviceUhdSettings(BaseValidatorModel):
    ActiveInput: Optional[InputDeviceActiveInputType] = None
    ConfiguredInput: Optional[InputDeviceConfiguredInputType] = None
    DeviceState: Optional[InputDeviceStateType] = None
    Framerate: Optional[float] = None
    Height: Optional[int] = None
    MaxBitrate: Optional[int] = None
    ScanType: Optional[InputDeviceScanTypeType] = None
    Width: Optional[int] = None
    LatencyMs: Optional[int] = None
    Codec: Optional[InputDeviceCodecType] = None
    MediaconnectSettings: Optional[InputDeviceMediaConnectSettings] = None
    AudioChannelPairs: Optional[List[InputDeviceUhdAudioChannelPairConfig]] = None


class ListInputDeviceTransfersResponse(BaseValidatorModel):
    InputDeviceTransfers: List[TransferringInputDeviceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMultiplexProgramsResponse(BaseValidatorModel):
    MultiplexPrograms: List[MultiplexProgramSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSignalMapsResponse(BaseValidatorModel):
    SignalMaps: List[SignalMapSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StandardHlsSettings(BaseValidatorModel):
    M3u8Settings: M3u8Settings
    AudioRenditionSets: Optional[str] = None


class MediaResource(BaseValidatorModel):
    Destinations: Optional[List[MediaResourceNeighbor]] = None
    Name: Optional[str] = None
    Sources: Optional[List[MediaResourceNeighbor]] = None


class MotionGraphicsConfigurationOutput(BaseValidatorModel):
    MotionGraphicsSettings: MotionGraphicsSettingsOutput
    MotionGraphicsInsertion: Optional[MotionGraphicsInsertionType] = None


class MotionGraphicsConfiguration(BaseValidatorModel):
    MotionGraphicsSettings: MotionGraphicsSettings
    MotionGraphicsInsertion: Optional[MotionGraphicsInsertionType] = None


class NetworkInputSettings(BaseValidatorModel):
    HlsInputSettings: Optional[HlsInputSettings] = None
    ServerValidation: Optional[NetworkInputServerValidationType] = None
    MulticastInputSettings: Optional[MulticastInputSettings] = None


class MulticastSettingsCreateRequest(BaseValidatorModel):
    Sources: Optional[List[MulticastSourceCreateRequest]] = None


class MulticastSettings(BaseValidatorModel):
    Sources: Optional[List[MulticastSource]] = None


class MulticastSettingsUpdateRequest(BaseValidatorModel):
    Sources: Optional[List[MulticastSourceUpdateRequest]] = None


class MultiplexContainerSettings(BaseValidatorModel):
    MultiplexM2tsSettings: Optional[MultiplexM2tsSettings] = None


class MultiplexOutputDestination(BaseValidatorModel):
    MediaConnectSettings: Optional[MultiplexMediaConnectOutputDestinationSettings] = None

MultiplexProgramPacketIdentifiersMapUnion = Union[MultiplexProgramPacketIdentifiersMap, MultiplexProgramPacketIdentifiersMapOutput]


class MultiplexSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    Id: Optional[str] = None
    MultiplexSettings: Optional[MultiplexSettingsSummary] = None
    Name: Optional[str] = None
    PipelinesRunningCount: Optional[int] = None
    ProgramCount: Optional[int] = None
    State: Optional[MultiplexStateType] = None
    Tags: Optional[Dict[str, str]] = None


class MultiplexVideoSettings(BaseValidatorModel):
    ConstantBitrate: Optional[int] = None
    StatmuxSettings: Optional[MultiplexStatmuxVideoSettings] = None


class NielsenWatermarksSettings(BaseValidatorModel):
    NielsenCbetSettings: Optional[NielsenCBET] = None
    NielsenDistributionType: Optional[NielsenWatermarksDistributionTypesType] = None
    NielsenNaesIiNwSettings: Optional[NielsenNaesIiNw] = None


class OutputDestinationOutput(BaseValidatorModel):
    Id: Optional[str] = None
    MediaPackageSettings: Optional[List[MediaPackageOutputDestinationSettings]] = None
    MultiplexSettings: Optional[MultiplexProgramChannelDestinationSettings] = None
    Settings: Optional[List[OutputDestinationSettings]] = None
    SrtSettings: Optional[List[SrtOutputDestinationSettings]] = None


class OutputDestination(BaseValidatorModel):
    Id: Optional[str] = None
    MediaPackageSettings: Optional[List[MediaPackageOutputDestinationSettings]] = None
    MultiplexSettings: Optional[MultiplexProgramChannelDestinationSettings] = None
    Settings: Optional[List[OutputDestinationSettings]] = None
    SrtSettings: Optional[List[SrtOutputDestinationSettings]] = None


class PauseStateScheduleActionSettingsOutput(BaseValidatorModel):
    Pipelines: Optional[List[PipelinePauseStateSettings]] = None


class PauseStateScheduleActionSettings(BaseValidatorModel):
    Pipelines: Optional[List[PipelinePauseStateSettings]] = None


class UpdateNetworkRequest(BaseValidatorModel):
    NetworkId: str
    IpPools: Optional[List[IpPoolUpdateRequest]] = None
    Name: Optional[str] = None
    Routes: Optional[List[RouteUpdateRequest]] = None


class Scte35SegmentationDescriptor(BaseValidatorModel):
    SegmentationCancelIndicator: Scte35SegmentationCancelIndicatorType
    SegmentationEventId: int
    DeliveryRestrictions: Optional[Scte35DeliveryRestrictions] = None
    SegmentNum: Optional[int] = None
    SegmentationDuration: Optional[int] = None
    SegmentationTypeId: Optional[int] = None
    SegmentationUpid: Optional[str] = None
    SegmentationUpidType: Optional[int] = None
    SegmentsExpected: Optional[int] = None
    SubSegmentNum: Optional[int] = None
    SubSegmentsExpected: Optional[int] = None


class SrtCallerSourceRequest(BaseValidatorModel):
    Decryption: Optional[SrtCallerDecryptionRequest] = None
    MinimumLatency: Optional[int] = None
    SrtListenerAddress: Optional[str] = None
    SrtListenerPort: Optional[str] = None
    StreamId: Optional[str] = None


class SrtCallerSource(BaseValidatorModel):
    Decryption: Optional[SrtCallerDecryption] = None
    MinimumLatency: Optional[int] = None
    SrtListenerAddress: Optional[str] = None
    SrtListenerPort: Optional[str] = None
    StreamId: Optional[str] = None

StaticImageOutputDeactivateScheduleActionSettingsUnion = Union[StaticImageOutputDeactivateScheduleActionSettings, StaticImageOutputDeactivateScheduleActionSettingsOutput]


class ThumbnailDetail(BaseValidatorModel):
    PipelineId: Optional[str] = None
    Thumbnails: Optional[List[Thumbnail]] = None


class VideoSelectorSettings(BaseValidatorModel):
    VideoSelectorPid: Optional[VideoSelectorPid] = None
    VideoSelectorProgramId: Optional[VideoSelectorProgramId] = None


class ArchiveGroupSettings(BaseValidatorModel):
    Destination: OutputLocationRef
    ArchiveCdnSettings: Optional[ArchiveCdnSettings] = None
    RolloverInterval: Optional[int] = None


class RemixSettingsOutput(BaseValidatorModel):
    ChannelMappings: List[AudioChannelMappingOutput]
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None


class RemixSettings(BaseValidatorModel):
    ChannelMappings: List[AudioChannelMapping]
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None


class CaptionDestinationSettingsOutput(BaseValidatorModel):
    AribDestinationSettings: Optional[Dict[str, Any]] = None
    BurnInDestinationSettings: Optional[BurnInDestinationSettings] = None
    DvbSubDestinationSettings: Optional[DvbSubDestinationSettings] = None
    EbuTtDDestinationSettings: Optional[EbuTtDDestinationSettings] = None
    EmbeddedDestinationSettings: Optional[Dict[str, Any]] = None
    EmbeddedPlusScte20DestinationSettings: Optional[Dict[str, Any]] = None
    RtmpCaptionInfoDestinationSettings: Optional[Dict[str, Any]] = None
    Scte20PlusEmbeddedDestinationSettings: Optional[Dict[str, Any]] = None
    Scte27DestinationSettings: Optional[Dict[str, Any]] = None
    SmpteTtDestinationSettings: Optional[Dict[str, Any]] = None
    TeletextDestinationSettings: Optional[Dict[str, Any]] = None
    TtmlDestinationSettings: Optional[TtmlDestinationSettings] = None
    WebvttDestinationSettings: Optional[WebvttDestinationSettings] = None


class CaptionDestinationSettings(BaseValidatorModel):
    AribDestinationSettings: Optional[Dict[str, Any]] = None
    BurnInDestinationSettings: Optional[BurnInDestinationSettings] = None
    DvbSubDestinationSettings: Optional[DvbSubDestinationSettings] = None
    EbuTtDDestinationSettings: Optional[EbuTtDDestinationSettings] = None
    EmbeddedDestinationSettings: Optional[Dict[str, Any]] = None
    EmbeddedPlusScte20DestinationSettings: Optional[Dict[str, Any]] = None
    RtmpCaptionInfoDestinationSettings: Optional[Dict[str, Any]] = None
    Scte20PlusEmbeddedDestinationSettings: Optional[Dict[str, Any]] = None
    Scte27DestinationSettings: Optional[Dict[str, Any]] = None
    SmpteTtDestinationSettings: Optional[Dict[str, Any]] = None
    TeletextDestinationSettings: Optional[Dict[str, Any]] = None
    TtmlDestinationSettings: Optional[TtmlDestinationSettings] = None
    WebvttDestinationSettings: Optional[WebvttDestinationSettings] = None

StaticImageOutputActivateScheduleActionSettingsUnion = Union[StaticImageOutputActivateScheduleActionSettings, StaticImageOutputActivateScheduleActionSettingsOutput]


class KeyProviderSettings(BaseValidatorModel):
    StaticKeySettings: Optional[StaticKeySettings] = None


class AudioSelectorSettingsOutput(BaseValidatorModel):
    AudioHlsRenditionSelection: Optional[AudioHlsRenditionSelection] = None
    AudioLanguageSelection: Optional[AudioLanguageSelection] = None
    AudioPidSelection: Optional[AudioPidSelection] = None
    AudioTrackSelection: Optional[AudioTrackSelectionOutput] = None

AudioTrackSelectionUnion = Union[AudioTrackSelection, AudioTrackSelectionOutput]


class Av1SettingsOutput(BaseValidatorModel):
    FramerateDenominator: int
    FramerateNumerator: int
    AfdSignaling: Optional[AfdSignalingType] = None
    BufSize: Optional[int] = None
    ColorSpaceSettings: Optional[Av1ColorSpaceSettingsOutput] = None
    FixedAfd: Optional[FixedAfdType] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[Av1GopSizeUnitsType] = None
    Level: Optional[Av1LevelType] = None
    LookAheadRateControl: Optional[Av1LookAheadRateControlType] = None
    MaxBitrate: Optional[int] = None
    MinIInterval: Optional[int] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    QvbrQualityLevel: Optional[int] = None
    SceneChangeDetect: Optional[Av1SceneChangeDetectType] = None
    TimecodeBurninSettings: Optional[TimecodeBurninSettings] = None


class Av1Settings(BaseValidatorModel):
    FramerateDenominator: int
    FramerateNumerator: int
    AfdSignaling: Optional[AfdSignalingType] = None
    BufSize: Optional[int] = None
    ColorSpaceSettings: Optional[Av1ColorSpaceSettings] = None
    FixedAfd: Optional[FixedAfdType] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[Av1GopSizeUnitsType] = None
    Level: Optional[Av1LevelType] = None
    LookAheadRateControl: Optional[Av1LookAheadRateControlType] = None
    MaxBitrate: Optional[int] = None
    MinIInterval: Optional[int] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    QvbrQualityLevel: Optional[int] = None
    SceneChangeDetect: Optional[Av1SceneChangeDetectType] = None
    TimecodeBurninSettings: Optional[TimecodeBurninSettings] = None


class AvailConfiguration(BaseValidatorModel):
    AvailSettings: Optional[AvailSettings] = None
    Scte35SegmentationScope: Optional[Scte35SegmentationScopeType] = None


class CaptionSelectorSettingsOutput(BaseValidatorModel):
    AncillarySourceSettings: Optional[AncillarySourceSettings] = None
    AribSourceSettings: Optional[Dict[str, Any]] = None
    DvbSubSourceSettings: Optional[DvbSubSourceSettings] = None
    EmbeddedSourceSettings: Optional[EmbeddedSourceSettings] = None
    Scte20SourceSettings: Optional[Scte20SourceSettings] = None
    Scte27SourceSettings: Optional[Scte27SourceSettings] = None
    TeletextSourceSettings: Optional[TeletextSourceSettings] = None


class CaptionSelectorSettings(BaseValidatorModel):
    AncillarySourceSettings: Optional[AncillarySourceSettings] = None
    AribSourceSettings: Optional[Dict[str, Any]] = None
    DvbSubSourceSettings: Optional[DvbSubSourceSettings] = None
    EmbeddedSourceSettings: Optional[EmbeddedSourceSettings] = None
    Scte20SourceSettings: Optional[Scte20SourceSettings] = None
    Scte27SourceSettings: Optional[Scte27SourceSettings] = None
    TeletextSourceSettings: Optional[TeletextSourceSettings] = None


class CreateClusterRequest(BaseValidatorModel):
    ClusterType: Optional[Literal['ON_PREMISES']] = None
    InstanceRoleArn: Optional[str] = None
    Name: Optional[str] = None
    NetworkSettings: Optional[ClusterNetworkSettingsCreateRequest] = None
    RequestId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class CreateClusterResponse(BaseValidatorModel):
    Arn: str
    ChannelIds: List[str]
    ClusterType: Literal['ON_PREMISES']
    Id: str
    InstanceRoleArn: str
    Name: str
    NetworkSettings: ClusterNetworkSettings
    State: ClusterStateType
    ResponseMetadata: ResponseMetadata


class DeleteClusterResponse(BaseValidatorModel):
    Arn: str
    ChannelIds: List[str]
    ClusterType: Literal['ON_PREMISES']
    Id: str
    InstanceRoleArn: str
    Name: str
    NetworkSettings: ClusterNetworkSettings
    State: ClusterStateType
    ResponseMetadata: ResponseMetadata


class DescribeClusterResponse(BaseValidatorModel):
    Arn: str
    ChannelIds: List[str]
    ClusterType: Literal['ON_PREMISES']
    Id: str
    InstanceRoleArn: str
    Name: str
    NetworkSettings: ClusterNetworkSettings
    State: ClusterStateType
    ResponseMetadata: ResponseMetadata


class DescribeClusterSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    ChannelIds: Optional[List[str]] = None
    ClusterType: Optional[Literal['ON_PREMISES']] = None
    Id: Optional[str] = None
    InstanceRoleArn: Optional[str] = None
    Name: Optional[str] = None
    NetworkSettings: Optional[ClusterNetworkSettings] = None
    State: Optional[ClusterStateType] = None


class UpdateClusterResponse(BaseValidatorModel):
    Arn: str
    ChannelIds: List[str]
    ClusterType: Literal['ON_PREMISES']
    Id: str
    Name: str
    NetworkSettings: ClusterNetworkSettings
    State: ClusterStateType
    ResponseMetadata: ResponseMetadata


class UpdateClusterRequest(BaseValidatorModel):
    ClusterId: str
    Name: Optional[str] = None
    NetworkSettings: Optional[ClusterNetworkSettingsUpdateRequest] = None


class ListNetworksResponse(BaseValidatorModel):
    Networks: List[DescribeNetworkSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNodesResponse(BaseValidatorModel):
    Nodes: List[DescribeNodeSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOfferingsResponse(BaseValidatorModel):
    Offerings: List[Offering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListReservationsResponse(BaseValidatorModel):
    Reservations: List[Reservation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PurchaseOfferingResponse(BaseValidatorModel):
    Reservation: Reservation
    ResponseMetadata: ResponseMetadata


class UpdateReservationResponse(BaseValidatorModel):
    Reservation: Reservation
    ResponseMetadata: ResponseMetadata


class CreateInputSecurityGroupResponse(BaseValidatorModel):
    SecurityGroup: InputSecurityGroup
    ResponseMetadata: ResponseMetadata


class ListInputSecurityGroupsResponse(BaseValidatorModel):
    InputSecurityGroups: List[InputSecurityGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateInputSecurityGroupResponse(BaseValidatorModel):
    SecurityGroup: InputSecurityGroup
    ResponseMetadata: ResponseMetadata


class ArchiveContainerSettingsOutput(BaseValidatorModel):
    M2tsSettings: Optional[M2tsSettings] = None
    RawSettings: Optional[Dict[str, Any]] = None


class ArchiveContainerSettings(BaseValidatorModel):
    M2tsSettings: Optional[M2tsSettings] = None
    RawSettings: Optional[Dict[str, Any]] = None


class UdpContainerSettings(BaseValidatorModel):
    M2tsSettings: Optional[M2tsSettings] = None


class GlobalConfigurationOutput(BaseValidatorModel):
    InitialAudioGain: Optional[int] = None
    InputEndAction: Optional[GlobalConfigurationInputEndActionType] = None
    InputLossBehavior: Optional[InputLossBehavior] = None
    OutputLockingMode: Optional[GlobalConfigurationOutputLockingModeType] = None
    OutputTimingSource: Optional[GlobalConfigurationOutputTimingSourceType] = None
    SupportLowFramerateInputs: Optional[GlobalConfigurationLowFramerateInputsType] = None
    OutputLockingSettings: Optional[OutputLockingSettingsOutput] = None


class GlobalConfiguration(BaseValidatorModel):
    InitialAudioGain: Optional[int] = None
    InputEndAction: Optional[GlobalConfigurationInputEndActionType] = None
    InputLossBehavior: Optional[InputLossBehavior] = None
    OutputLockingMode: Optional[GlobalConfigurationOutputLockingModeType] = None
    OutputTimingSource: Optional[GlobalConfigurationOutputTimingSourceType] = None
    SupportLowFramerateInputs: Optional[GlobalConfigurationLowFramerateInputsType] = None
    OutputLockingSettings: Optional[OutputLockingSettings] = None


class FailoverCondition(BaseValidatorModel):
    FailoverConditionSettings: Optional[FailoverConditionSettings] = None

ScheduleActionStartSettingsUnion = Union[ScheduleActionStartSettings, ScheduleActionStartSettingsOutput]


class FrameCaptureGroupSettings(BaseValidatorModel):
    Destination: OutputLocationRef
    FrameCaptureCdnSettings: Optional[FrameCaptureCdnSettings] = None


class H264SettingsOutput(BaseValidatorModel):
    AdaptiveQuantization: Optional[H264AdaptiveQuantizationType] = None
    AfdSignaling: Optional[AfdSignalingType] = None
    Bitrate: Optional[int] = None
    BufFillPct: Optional[int] = None
    BufSize: Optional[int] = None
    ColorMetadata: Optional[H264ColorMetadataType] = None
    ColorSpaceSettings: Optional[H264ColorSpaceSettingsOutput] = None
    EntropyEncoding: Optional[H264EntropyEncodingType] = None
    FilterSettings: Optional[H264FilterSettings] = None
    FixedAfd: Optional[FixedAfdType] = None
    FlickerAq: Optional[H264FlickerAqType] = None
    ForceFieldPictures: Optional[H264ForceFieldPicturesType] = None
    FramerateControl: Optional[H264FramerateControlType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    GopBReference: Optional[H264GopBReferenceType] = None
    GopClosedCadence: Optional[int] = None
    GopNumBFrames: Optional[int] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[H264GopSizeUnitsType] = None
    Level: Optional[H264LevelType] = None
    LookAheadRateControl: Optional[H264LookAheadRateControlType] = None
    MaxBitrate: Optional[int] = None
    MinIInterval: Optional[int] = None
    NumRefFrames: Optional[int] = None
    ParControl: Optional[H264ParControlType] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    Profile: Optional[H264ProfileType] = None
    QualityLevel: Optional[H264QualityLevelType] = None
    QvbrQualityLevel: Optional[int] = None
    RateControlMode: Optional[H264RateControlModeType] = None
    ScanType: Optional[H264ScanTypeType] = None
    SceneChangeDetect: Optional[H264SceneChangeDetectType] = None
    Slices: Optional[int] = None
    Softness: Optional[int] = None
    SpatialAq: Optional[H264SpatialAqType] = None
    SubgopLength: Optional[H264SubGopLengthType] = None
    Syntax: Optional[H264SyntaxType] = None
    TemporalAq: Optional[H264TemporalAqType] = None
    TimecodeInsertion: Optional[H264TimecodeInsertionBehaviorType] = None
    TimecodeBurninSettings: Optional[TimecodeBurninSettings] = None
    MinQp: Optional[int] = None


class H264Settings(BaseValidatorModel):
    AdaptiveQuantization: Optional[H264AdaptiveQuantizationType] = None
    AfdSignaling: Optional[AfdSignalingType] = None
    Bitrate: Optional[int] = None
    BufFillPct: Optional[int] = None
    BufSize: Optional[int] = None
    ColorMetadata: Optional[H264ColorMetadataType] = None
    ColorSpaceSettings: Optional[H264ColorSpaceSettings] = None
    EntropyEncoding: Optional[H264EntropyEncodingType] = None
    FilterSettings: Optional[H264FilterSettings] = None
    FixedAfd: Optional[FixedAfdType] = None
    FlickerAq: Optional[H264FlickerAqType] = None
    ForceFieldPictures: Optional[H264ForceFieldPicturesType] = None
    FramerateControl: Optional[H264FramerateControlType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    GopBReference: Optional[H264GopBReferenceType] = None
    GopClosedCadence: Optional[int] = None
    GopNumBFrames: Optional[int] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[H264GopSizeUnitsType] = None
    Level: Optional[H264LevelType] = None
    LookAheadRateControl: Optional[H264LookAheadRateControlType] = None
    MaxBitrate: Optional[int] = None
    MinIInterval: Optional[int] = None
    NumRefFrames: Optional[int] = None
    ParControl: Optional[H264ParControlType] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    Profile: Optional[H264ProfileType] = None
    QualityLevel: Optional[H264QualityLevelType] = None
    QvbrQualityLevel: Optional[int] = None
    RateControlMode: Optional[H264RateControlModeType] = None
    ScanType: Optional[H264ScanTypeType] = None
    SceneChangeDetect: Optional[H264SceneChangeDetectType] = None
    Slices: Optional[int] = None
    Softness: Optional[int] = None
    SpatialAq: Optional[H264SpatialAqType] = None
    SubgopLength: Optional[H264SubGopLengthType] = None
    Syntax: Optional[H264SyntaxType] = None
    TemporalAq: Optional[H264TemporalAqType] = None
    TimecodeInsertion: Optional[H264TimecodeInsertionBehaviorType] = None
    TimecodeBurninSettings: Optional[TimecodeBurninSettings] = None
    MinQp: Optional[int] = None


class H265SettingsOutput(BaseValidatorModel):
    FramerateDenominator: int
    FramerateNumerator: int
    AdaptiveQuantization: Optional[H265AdaptiveQuantizationType] = None
    AfdSignaling: Optional[AfdSignalingType] = None
    AlternativeTransferFunction: Optional[H265AlternativeTransferFunctionType] = None
    Bitrate: Optional[int] = None
    BufSize: Optional[int] = None
    ColorMetadata: Optional[H265ColorMetadataType] = None
    ColorSpaceSettings: Optional[H265ColorSpaceSettingsOutput] = None
    FilterSettings: Optional[H265FilterSettings] = None
    FixedAfd: Optional[FixedAfdType] = None
    FlickerAq: Optional[H265FlickerAqType] = None
    GopClosedCadence: Optional[int] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[H265GopSizeUnitsType] = None
    Level: Optional[H265LevelType] = None
    LookAheadRateControl: Optional[H265LookAheadRateControlType] = None
    MaxBitrate: Optional[int] = None
    MinIInterval: Optional[int] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    Profile: Optional[H265ProfileType] = None
    QvbrQualityLevel: Optional[int] = None
    RateControlMode: Optional[H265RateControlModeType] = None
    ScanType: Optional[H265ScanTypeType] = None
    SceneChangeDetect: Optional[H265SceneChangeDetectType] = None
    Slices: Optional[int] = None
    Tier: Optional[H265TierType] = None
    TimecodeInsertion: Optional[H265TimecodeInsertionBehaviorType] = None
    TimecodeBurninSettings: Optional[TimecodeBurninSettings] = None
    MvOverPictureBoundaries: Optional[H265MvOverPictureBoundariesType] = None
    MvTemporalPredictor: Optional[H265MvTemporalPredictorType] = None
    TileHeight: Optional[int] = None
    TilePadding: Optional[H265TilePaddingType] = None
    TileWidth: Optional[int] = None
    TreeblockSize: Optional[H265TreeblockSizeType] = None
    MinQp: Optional[int] = None
    Deblocking: Optional[H265DeblockingType] = None


class H265Settings(BaseValidatorModel):
    FramerateDenominator: int
    FramerateNumerator: int
    AdaptiveQuantization: Optional[H265AdaptiveQuantizationType] = None
    AfdSignaling: Optional[AfdSignalingType] = None
    AlternativeTransferFunction: Optional[H265AlternativeTransferFunctionType] = None
    Bitrate: Optional[int] = None
    BufSize: Optional[int] = None
    ColorMetadata: Optional[H265ColorMetadataType] = None
    ColorSpaceSettings: Optional[H265ColorSpaceSettings] = None
    FilterSettings: Optional[H265FilterSettings] = None
    FixedAfd: Optional[FixedAfdType] = None
    FlickerAq: Optional[H265FlickerAqType] = None
    GopClosedCadence: Optional[int] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[H265GopSizeUnitsType] = None
    Level: Optional[H265LevelType] = None
    LookAheadRateControl: Optional[H265LookAheadRateControlType] = None
    MaxBitrate: Optional[int] = None
    MinIInterval: Optional[int] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    Profile: Optional[H265ProfileType] = None
    QvbrQualityLevel: Optional[int] = None
    RateControlMode: Optional[H265RateControlModeType] = None
    ScanType: Optional[H265ScanTypeType] = None
    SceneChangeDetect: Optional[H265SceneChangeDetectType] = None
    Slices: Optional[int] = None
    Tier: Optional[H265TierType] = None
    TimecodeInsertion: Optional[H265TimecodeInsertionBehaviorType] = None
    TimecodeBurninSettings: Optional[TimecodeBurninSettings] = None
    MvOverPictureBoundaries: Optional[H265MvOverPictureBoundariesType] = None
    MvTemporalPredictor: Optional[H265MvTemporalPredictorType] = None
    TileHeight: Optional[int] = None
    TilePadding: Optional[H265TilePaddingType] = None
    TileWidth: Optional[int] = None
    TreeblockSize: Optional[H265TreeblockSizeType] = None
    MinQp: Optional[int] = None
    Deblocking: Optional[H265DeblockingType] = None


class Mpeg2Settings(BaseValidatorModel):
    FramerateDenominator: int
    FramerateNumerator: int
    AdaptiveQuantization: Optional[Mpeg2AdaptiveQuantizationType] = None
    AfdSignaling: Optional[AfdSignalingType] = None
    ColorMetadata: Optional[Mpeg2ColorMetadataType] = None
    ColorSpace: Optional[Mpeg2ColorSpaceType] = None
    DisplayAspectRatio: Optional[Mpeg2DisplayRatioType] = None
    FilterSettings: Optional[Mpeg2FilterSettings] = None
    FixedAfd: Optional[FixedAfdType] = None
    GopClosedCadence: Optional[int] = None
    GopNumBFrames: Optional[int] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[Mpeg2GopSizeUnitsType] = None
    ScanType: Optional[Mpeg2ScanTypeType] = None
    SubgopLength: Optional[Mpeg2SubGopLengthType] = None
    TimecodeInsertion: Optional[Mpeg2TimecodeInsertionBehaviorType] = None
    TimecodeBurninSettings: Optional[TimecodeBurninSettings] = None


class InputPrepareScheduleActionSettingsOutput(BaseValidatorModel):
    InputAttachmentNameReference: Optional[str] = None
    InputClippingSettings: Optional[InputClippingSettings] = None
    UrlPath: Optional[List[str]] = None


class InputPrepareScheduleActionSettings(BaseValidatorModel):
    InputAttachmentNameReference: Optional[str] = None
    InputClippingSettings: Optional[InputClippingSettings] = None
    UrlPath: Optional[List[str]] = None


class InputSwitchScheduleActionSettingsOutput(BaseValidatorModel):
    InputAttachmentNameReference: str
    InputClippingSettings: Optional[InputClippingSettings] = None
    UrlPath: Optional[List[str]] = None


class InputSwitchScheduleActionSettings(BaseValidatorModel):
    InputAttachmentNameReference: str
    InputClippingSettings: Optional[InputClippingSettings] = None
    UrlPath: Optional[List[str]] = None


class UpdateInputDeviceRequest(BaseValidatorModel):
    InputDeviceId: str
    HdDeviceSettings: Optional[InputDeviceConfigurableSettings] = None
    Name: Optional[str] = None
    UhdDeviceSettings: Optional[InputDeviceConfigurableSettings] = None
    AvailabilityZone: Optional[str] = None


class DescribeInputDeviceResponse(BaseValidatorModel):
    Arn: str
    ConnectionState: InputDeviceConnectionStateType
    DeviceSettingsSyncState: DeviceSettingsSyncStateType
    DeviceUpdateStatus: DeviceUpdateStatusType
    HdDeviceSettings: InputDeviceHdSettings
    Id: str
    MacAddress: str
    Name: str
    NetworkSettings: InputDeviceNetworkSettings
    SerialNumber: str
    Type: InputDeviceTypeType
    UhdDeviceSettings: InputDeviceUhdSettings
    Tags: Dict[str, str]
    AvailabilityZone: str
    MedialiveInputArns: List[str]
    OutputType: InputDeviceOutputTypeType
    ResponseMetadata: ResponseMetadata


class InputDeviceSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectionState: Optional[InputDeviceConnectionStateType] = None
    DeviceSettingsSyncState: Optional[DeviceSettingsSyncStateType] = None
    DeviceUpdateStatus: Optional[DeviceUpdateStatusType] = None
    HdDeviceSettings: Optional[InputDeviceHdSettings] = None
    Id: Optional[str] = None
    MacAddress: Optional[str] = None
    Name: Optional[str] = None
    NetworkSettings: Optional[InputDeviceNetworkSettings] = None
    SerialNumber: Optional[str] = None
    Type: Optional[InputDeviceTypeType] = None
    UhdDeviceSettings: Optional[InputDeviceUhdSettings] = None
    Tags: Optional[Dict[str, str]] = None
    AvailabilityZone: Optional[str] = None
    MedialiveInputArns: Optional[List[str]] = None
    OutputType: Optional[InputDeviceOutputTypeType] = None


class UpdateInputDeviceResponse(BaseValidatorModel):
    Arn: str
    ConnectionState: InputDeviceConnectionStateType
    DeviceSettingsSyncState: DeviceSettingsSyncStateType
    DeviceUpdateStatus: DeviceUpdateStatusType
    HdDeviceSettings: InputDeviceHdSettings
    Id: str
    MacAddress: str
    Name: str
    NetworkSettings: InputDeviceNetworkSettings
    SerialNumber: str
    Type: InputDeviceTypeType
    UhdDeviceSettings: InputDeviceUhdSettings
    Tags: Dict[str, str]
    AvailabilityZone: str
    MedialiveInputArns: List[str]
    OutputType: InputDeviceOutputTypeType
    ResponseMetadata: ResponseMetadata


class HlsSettingsOutput(BaseValidatorModel):
    AudioOnlyHlsSettings: Optional[AudioOnlyHlsSettings] = None
    Fmp4HlsSettings: Optional[Fmp4HlsSettings] = None
    FrameCaptureHlsSettings: Optional[Dict[str, Any]] = None
    StandardHlsSettings: Optional[StandardHlsSettings] = None


class HlsSettings(BaseValidatorModel):
    AudioOnlyHlsSettings: Optional[AudioOnlyHlsSettings] = None
    Fmp4HlsSettings: Optional[Fmp4HlsSettings] = None
    FrameCaptureHlsSettings: Optional[Dict[str, Any]] = None
    StandardHlsSettings: Optional[StandardHlsSettings] = None


class CreateSignalMapResponse(BaseValidatorModel):
    Arn: str
    CloudWatchAlarmTemplateGroupIds: List[str]
    CreatedAt: datetime
    Description: str
    DiscoveryEntryPointArn: str
    ErrorMessage: str
    EventBridgeRuleTemplateGroupIds: List[str]
    FailedMediaResourceMap: Dict[str, MediaResource]
    Id: str
    LastDiscoveredAt: datetime
    LastSuccessfulMonitorDeployment: SuccessfulMonitorDeployment
    MediaResourceMap: Dict[str, MediaResource]
    ModifiedAt: datetime
    MonitorChangesPendingDeployment: bool
    MonitorDeployment: MonitorDeployment
    Name: str
    Status: SignalMapStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSignalMapResponse(BaseValidatorModel):
    Arn: str
    CloudWatchAlarmTemplateGroupIds: List[str]
    CreatedAt: datetime
    Description: str
    DiscoveryEntryPointArn: str
    ErrorMessage: str
    EventBridgeRuleTemplateGroupIds: List[str]
    FailedMediaResourceMap: Dict[str, MediaResource]
    Id: str
    LastDiscoveredAt: datetime
    LastSuccessfulMonitorDeployment: SuccessfulMonitorDeployment
    MediaResourceMap: Dict[str, MediaResource]
    ModifiedAt: datetime
    MonitorChangesPendingDeployment: bool
    MonitorDeployment: MonitorDeployment
    Name: str
    Status: SignalMapStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartDeleteMonitorDeploymentResponse(BaseValidatorModel):
    Arn: str
    CloudWatchAlarmTemplateGroupIds: List[str]
    CreatedAt: datetime
    Description: str
    DiscoveryEntryPointArn: str
    ErrorMessage: str
    EventBridgeRuleTemplateGroupIds: List[str]
    FailedMediaResourceMap: Dict[str, MediaResource]
    Id: str
    LastDiscoveredAt: datetime
    LastSuccessfulMonitorDeployment: SuccessfulMonitorDeployment
    MediaResourceMap: Dict[str, MediaResource]
    ModifiedAt: datetime
    MonitorChangesPendingDeployment: bool
    MonitorDeployment: MonitorDeployment
    Name: str
    Status: SignalMapStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartMonitorDeploymentResponse(BaseValidatorModel):
    Arn: str
    CloudWatchAlarmTemplateGroupIds: List[str]
    CreatedAt: datetime
    Description: str
    DiscoveryEntryPointArn: str
    ErrorMessage: str
    EventBridgeRuleTemplateGroupIds: List[str]
    FailedMediaResourceMap: Dict[str, MediaResource]
    Id: str
    LastDiscoveredAt: datetime
    LastSuccessfulMonitorDeployment: SuccessfulMonitorDeployment
    MediaResourceMap: Dict[str, MediaResource]
    ModifiedAt: datetime
    MonitorChangesPendingDeployment: bool
    MonitorDeployment: MonitorDeployment
    Name: str
    Status: SignalMapStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartUpdateSignalMapResponse(BaseValidatorModel):
    Arn: str
    CloudWatchAlarmTemplateGroupIds: List[str]
    CreatedAt: datetime
    Description: str
    DiscoveryEntryPointArn: str
    ErrorMessage: str
    EventBridgeRuleTemplateGroupIds: List[str]
    FailedMediaResourceMap: Dict[str, MediaResource]
    Id: str
    LastDiscoveredAt: datetime
    LastSuccessfulMonitorDeployment: SuccessfulMonitorDeployment
    MediaResourceMap: Dict[str, MediaResource]
    ModifiedAt: datetime
    MonitorChangesPendingDeployment: bool
    MonitorDeployment: MonitorDeployment
    Name: str
    Status: SignalMapStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class MultiplexOutputSettings(BaseValidatorModel):
    Destination: OutputLocationRef
    ContainerSettings: Optional[MultiplexContainerSettings] = None


class DeleteMultiplexResponse(BaseValidatorModel):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List[MultiplexOutputDestination]
    Id: str
    MultiplexSettings: MultiplexSettings
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexStateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeMultiplexResponse(BaseValidatorModel):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List[MultiplexOutputDestination]
    Id: str
    MultiplexSettings: MultiplexSettings
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexStateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class Multiplex(BaseValidatorModel):
    Arn: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    Destinations: Optional[List[MultiplexOutputDestination]] = None
    Id: Optional[str] = None
    MultiplexSettings: Optional[MultiplexSettings] = None
    Name: Optional[str] = None
    PipelinesRunningCount: Optional[int] = None
    ProgramCount: Optional[int] = None
    State: Optional[MultiplexStateType] = None
    Tags: Optional[Dict[str, str]] = None


class StartMultiplexResponse(BaseValidatorModel):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List[MultiplexOutputDestination]
    Id: str
    MultiplexSettings: MultiplexSettings
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexStateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StopMultiplexResponse(BaseValidatorModel):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List[MultiplexOutputDestination]
    Id: str
    MultiplexSettings: MultiplexSettings
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexStateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateMultiplexRequest(BaseValidatorModel):
    MultiplexId: str
    MultiplexSettings: Optional[MultiplexSettings] = None
    Name: Optional[str] = None
    PacketIdentifiersMapping: Optional[Dict[str, MultiplexProgramPacketIdentifiersMapUnion]] = None


class ListMultiplexesResponse(BaseValidatorModel):
    Multiplexes: List[MultiplexSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MultiplexProgramSettings(BaseValidatorModel):
    ProgramNumber: int
    PreferredChannelPipeline: Optional[PreferredChannelPipelineType] = None
    ServiceDescriptor: Optional[MultiplexProgramServiceDescriptor] = None
    VideoSettings: Optional[MultiplexVideoSettings] = None


class AudioWatermarkSettings(BaseValidatorModel):
    NielsenWatermarksSettings: Optional[NielsenWatermarksSettings] = None

OutputDestinationUnion = Union[OutputDestination, OutputDestinationOutput]

PauseStateScheduleActionSettingsUnion = Union[PauseStateScheduleActionSettings, PauseStateScheduleActionSettingsOutput]


class Scte35DescriptorSettings(BaseValidatorModel):
    SegmentationDescriptorScte35DescriptorSettings: Scte35SegmentationDescriptor


class SrtSettingsRequest(BaseValidatorModel):
    SrtCallerSources: Optional[List[SrtCallerSourceRequest]] = None


class SrtSettings(BaseValidatorModel):
    SrtCallerSources: Optional[List[SrtCallerSource]] = None


class DescribeThumbnailsResponse(BaseValidatorModel):
    ThumbnailDetails: List[ThumbnailDetail]
    ResponseMetadata: ResponseMetadata


class VideoSelector(BaseValidatorModel):
    ColorSpace: Optional[VideoSelectorColorSpaceType] = None
    ColorSpaceSettings: Optional[VideoSelectorColorSpaceSettings] = None
    ColorSpaceUsage: Optional[VideoSelectorColorSpaceUsageType] = None
    SelectorSettings: Optional[VideoSelectorSettings] = None


class CaptionDescriptionOutput(BaseValidatorModel):
    CaptionSelectorName: str
    Name: str
    Accessibility: Optional[AccessibilityTypeType] = None
    DestinationSettings: Optional[CaptionDestinationSettingsOutput] = None
    LanguageCode: Optional[str] = None
    LanguageDescription: Optional[str] = None
    CaptionDashRoles: Optional[List[DashRoleCaptionType]] = None
    DvbDashAccessibility: Optional[DvbDashAccessibilityType] = None


class CaptionDescription(BaseValidatorModel):
    CaptionSelectorName: str
    Name: str
    Accessibility: Optional[AccessibilityTypeType] = None
    DestinationSettings: Optional[CaptionDestinationSettings] = None
    LanguageCode: Optional[str] = None
    LanguageDescription: Optional[str] = None
    CaptionDashRoles: Optional[List[DashRoleCaptionType]] = None
    DvbDashAccessibility: Optional[DvbDashAccessibilityType] = None


class HlsGroupSettingsOutput(BaseValidatorModel):
    Destination: OutputLocationRef
    AdMarkers: Optional[List[HlsAdMarkersType]] = None
    BaseUrlContent: Optional[str] = None
    BaseUrlContent1: Optional[str] = None
    BaseUrlManifest: Optional[str] = None
    BaseUrlManifest1: Optional[str] = None
    CaptionLanguageMappings: Optional[List[CaptionLanguageMapping]] = None
    CaptionLanguageSetting: Optional[HlsCaptionLanguageSettingType] = None
    ClientCache: Optional[HlsClientCacheType] = None
    CodecSpecification: Optional[HlsCodecSpecificationType] = None
    ConstantIv: Optional[str] = None
    DirectoryStructure: Optional[HlsDirectoryStructureType] = None
    DiscontinuityTags: Optional[HlsDiscontinuityTagsType] = None
    EncryptionType: Optional[HlsEncryptionTypeType] = None
    HlsCdnSettings: Optional[HlsCdnSettings] = None
    HlsId3SegmentTagging: Optional[HlsId3SegmentTaggingStateType] = None
    IFrameOnlyPlaylists: Optional[IFrameOnlyPlaylistTypeType] = None
    IncompleteSegmentBehavior: Optional[HlsIncompleteSegmentBehaviorType] = None
    IndexNSegments: Optional[int] = None
    InputLossAction: Optional[InputLossActionForHlsOutType] = None
    IvInManifest: Optional[HlsIvInManifestType] = None
    IvSource: Optional[HlsIvSourceType] = None
    KeepSegments: Optional[int] = None
    KeyFormat: Optional[str] = None
    KeyFormatVersions: Optional[str] = None
    KeyProviderSettings: Optional[KeyProviderSettings] = None
    ManifestCompression: Optional[HlsManifestCompressionType] = None
    ManifestDurationFormat: Optional[HlsManifestDurationFormatType] = None
    MinSegmentLength: Optional[int] = None
    Mode: Optional[HlsModeType] = None
    OutputSelection: Optional[HlsOutputSelectionType] = None
    ProgramDateTime: Optional[HlsProgramDateTimeType] = None
    ProgramDateTimeClock: Optional[HlsProgramDateTimeClockType] = None
    ProgramDateTimePeriod: Optional[int] = None
    RedundantManifest: Optional[HlsRedundantManifestType] = None
    SegmentLength: Optional[int] = None
    SegmentationMode: Optional[HlsSegmentationModeType] = None
    SegmentsPerSubdirectory: Optional[int] = None
    StreamInfResolution: Optional[HlsStreamInfResolutionType] = None
    TimedMetadataId3Frame: Optional[HlsTimedMetadataId3FrameType] = None
    TimedMetadataId3Period: Optional[int] = None
    TimestampDeltaMilliseconds: Optional[int] = None
    TsFileMode: Optional[HlsTsFileModeType] = None


class HlsGroupSettings(BaseValidatorModel):
    Destination: OutputLocationRef
    AdMarkers: Optional[List[HlsAdMarkersType]] = None
    BaseUrlContent: Optional[str] = None
    BaseUrlContent1: Optional[str] = None
    BaseUrlManifest: Optional[str] = None
    BaseUrlManifest1: Optional[str] = None
    CaptionLanguageMappings: Optional[List[CaptionLanguageMapping]] = None
    CaptionLanguageSetting: Optional[HlsCaptionLanguageSettingType] = None
    ClientCache: Optional[HlsClientCacheType] = None
    CodecSpecification: Optional[HlsCodecSpecificationType] = None
    ConstantIv: Optional[str] = None
    DirectoryStructure: Optional[HlsDirectoryStructureType] = None
    DiscontinuityTags: Optional[HlsDiscontinuityTagsType] = None
    EncryptionType: Optional[HlsEncryptionTypeType] = None
    HlsCdnSettings: Optional[HlsCdnSettings] = None
    HlsId3SegmentTagging: Optional[HlsId3SegmentTaggingStateType] = None
    IFrameOnlyPlaylists: Optional[IFrameOnlyPlaylistTypeType] = None
    IncompleteSegmentBehavior: Optional[HlsIncompleteSegmentBehaviorType] = None
    IndexNSegments: Optional[int] = None
    InputLossAction: Optional[InputLossActionForHlsOutType] = None
    IvInManifest: Optional[HlsIvInManifestType] = None
    IvSource: Optional[HlsIvSourceType] = None
    KeepSegments: Optional[int] = None
    KeyFormat: Optional[str] = None
    KeyFormatVersions: Optional[str] = None
    KeyProviderSettings: Optional[KeyProviderSettings] = None
    ManifestCompression: Optional[HlsManifestCompressionType] = None
    ManifestDurationFormat: Optional[HlsManifestDurationFormatType] = None
    MinSegmentLength: Optional[int] = None
    Mode: Optional[HlsModeType] = None
    OutputSelection: Optional[HlsOutputSelectionType] = None
    ProgramDateTime: Optional[HlsProgramDateTimeType] = None
    ProgramDateTimeClock: Optional[HlsProgramDateTimeClockType] = None
    ProgramDateTimePeriod: Optional[int] = None
    RedundantManifest: Optional[HlsRedundantManifestType] = None
    SegmentLength: Optional[int] = None
    SegmentationMode: Optional[HlsSegmentationModeType] = None
    SegmentsPerSubdirectory: Optional[int] = None
    StreamInfResolution: Optional[HlsStreamInfResolutionType] = None
    TimedMetadataId3Frame: Optional[HlsTimedMetadataId3FrameType] = None
    TimedMetadataId3Period: Optional[int] = None
    TimestampDeltaMilliseconds: Optional[int] = None
    TsFileMode: Optional[HlsTsFileModeType] = None


class AudioSelectorOutput(BaseValidatorModel):
    Name: str
    SelectorSettings: Optional[AudioSelectorSettingsOutput] = None


class AudioSelectorSettings(BaseValidatorModel):
    AudioHlsRenditionSelection: Optional[AudioHlsRenditionSelection] = None
    AudioLanguageSelection: Optional[AudioLanguageSelection] = None
    AudioPidSelection: Optional[AudioPidSelection] = None
    AudioTrackSelection: Optional[AudioTrackSelectionUnion] = None


class CaptionSelectorOutput(BaseValidatorModel):
    Name: str
    LanguageCode: Optional[str] = None
    SelectorSettings: Optional[CaptionSelectorSettingsOutput] = None

CaptionSelectorSettingsUnion = Union[CaptionSelectorSettings, CaptionSelectorSettingsOutput]


class ListClustersResponse(BaseValidatorModel):
    Clusters: List[DescribeClusterSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ArchiveOutputSettingsOutput(BaseValidatorModel):
    ContainerSettings: ArchiveContainerSettingsOutput
    Extension: Optional[str] = None
    NameModifier: Optional[str] = None


class ArchiveOutputSettings(BaseValidatorModel):
    ContainerSettings: ArchiveContainerSettings
    Extension: Optional[str] = None
    NameModifier: Optional[str] = None


class SrtOutputSettings(BaseValidatorModel):
    ContainerSettings: UdpContainerSettings
    Destination: OutputLocationRef
    BufferMsec: Optional[int] = None
    EncryptionType: Optional[SrtEncryptionTypeType] = None
    Latency: Optional[int] = None


class UdpOutputSettings(BaseValidatorModel):
    ContainerSettings: UdpContainerSettings
    Destination: OutputLocationRef
    BufferMsec: Optional[int] = None
    FecOutputSettings: Optional[FecOutputSettings] = None


class AutomaticInputFailoverSettingsOutput(BaseValidatorModel):
    SecondaryInputId: str
    ErrorClearTimeMsec: Optional[int] = None
    FailoverConditions: Optional[List[FailoverCondition]] = None
    InputPreference: Optional[InputPreferenceType] = None


class AutomaticInputFailoverSettings(BaseValidatorModel):
    SecondaryInputId: str
    ErrorClearTimeMsec: Optional[int] = None
    FailoverConditions: Optional[List[FailoverCondition]] = None
    InputPreference: Optional[InputPreferenceType] = None


class VideoCodecSettingsOutput(BaseValidatorModel):
    FrameCaptureSettings: Optional[FrameCaptureSettings] = None
    H264Settings: Optional[H264SettingsOutput] = None
    H265Settings: Optional[H265SettingsOutput] = None
    Mpeg2Settings: Optional[Mpeg2Settings] = None
    Av1Settings: Optional[Av1SettingsOutput] = None


class VideoCodecSettings(BaseValidatorModel):
    FrameCaptureSettings: Optional[FrameCaptureSettings] = None
    H264Settings: Optional[H264Settings] = None
    H265Settings: Optional[H265Settings] = None
    Mpeg2Settings: Optional[Mpeg2Settings] = None
    Av1Settings: Optional[Av1Settings] = None

InputPrepareScheduleActionSettingsUnion = Union[InputPrepareScheduleActionSettings, InputPrepareScheduleActionSettingsOutput]

InputSwitchScheduleActionSettingsUnion = Union[InputSwitchScheduleActionSettings, InputSwitchScheduleActionSettingsOutput]


class ListInputDevicesResponse(BaseValidatorModel):
    InputDevices: List[InputDeviceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class HlsOutputSettingsOutput(BaseValidatorModel):
    HlsSettings: HlsSettingsOutput
    H265PackagingType: Optional[HlsH265PackagingTypeType] = None
    NameModifier: Optional[str] = None
    SegmentModifier: Optional[str] = None


class HlsOutputSettings(BaseValidatorModel):
    HlsSettings: HlsSettings
    H265PackagingType: Optional[HlsH265PackagingTypeType] = None
    NameModifier: Optional[str] = None
    SegmentModifier: Optional[str] = None


class CreateMultiplexResponse(BaseValidatorModel):
    Multiplex: Multiplex
    ResponseMetadata: ResponseMetadata


class UpdateMultiplexResponse(BaseValidatorModel):
    Multiplex: Multiplex
    ResponseMetadata: ResponseMetadata


class CreateMultiplexProgramRequest(BaseValidatorModel):
    MultiplexId: str
    MultiplexProgramSettings: MultiplexProgramSettings
    ProgramName: str
    RequestId: str


class DeleteMultiplexProgramResponse(BaseValidatorModel):
    ChannelId: str
    MultiplexProgramSettings: MultiplexProgramSettings
    PacketIdentifiersMap: MultiplexProgramPacketIdentifiersMapOutput
    PipelineDetails: List[MultiplexProgramPipelineDetail]
    ProgramName: str
    ResponseMetadata: ResponseMetadata


class DescribeMultiplexProgramResponse(BaseValidatorModel):
    ChannelId: str
    MultiplexProgramSettings: MultiplexProgramSettings
    PacketIdentifiersMap: MultiplexProgramPacketIdentifiersMapOutput
    PipelineDetails: List[MultiplexProgramPipelineDetail]
    ProgramName: str
    ResponseMetadata: ResponseMetadata


class MultiplexProgram(BaseValidatorModel):
    ChannelId: Optional[str] = None
    MultiplexProgramSettings: Optional[MultiplexProgramSettings] = None
    PacketIdentifiersMap: Optional[MultiplexProgramPacketIdentifiersMapOutput] = None
    PipelineDetails: Optional[List[MultiplexProgramPipelineDetail]] = None
    ProgramName: Optional[str] = None


class UpdateMultiplexProgramRequest(BaseValidatorModel):
    MultiplexId: str
    ProgramName: str
    MultiplexProgramSettings: Optional[MultiplexProgramSettings] = None


class AudioDescriptionOutput(BaseValidatorModel):
    AudioSelectorName: str
    Name: str
    AudioNormalizationSettings: Optional[AudioNormalizationSettings] = None
    AudioType: Optional[AudioTypeType] = None
    AudioTypeControl: Optional[AudioDescriptionAudioTypeControlType] = None
    AudioWatermarkingSettings: Optional[AudioWatermarkSettings] = None
    CodecSettings: Optional[AudioCodecSettingsOutput] = None
    LanguageCode: Optional[str] = None
    LanguageCodeControl: Optional[AudioDescriptionLanguageCodeControlType] = None
    RemixSettings: Optional[RemixSettingsOutput] = None
    StreamName: Optional[str] = None
    AudioDashRoles: Optional[List[DashRoleAudioType]] = None
    DvbDashAccessibility: Optional[DvbDashAccessibilityType] = None


class AudioDescription(BaseValidatorModel):
    AudioSelectorName: str
    Name: str
    AudioNormalizationSettings: Optional[AudioNormalizationSettings] = None
    AudioType: Optional[AudioTypeType] = None
    AudioTypeControl: Optional[AudioDescriptionAudioTypeControlType] = None
    AudioWatermarkingSettings: Optional[AudioWatermarkSettings] = None
    CodecSettings: Optional[AudioCodecSettings] = None
    LanguageCode: Optional[str] = None
    LanguageCodeControl: Optional[AudioDescriptionLanguageCodeControlType] = None
    RemixSettings: Optional[RemixSettings] = None
    StreamName: Optional[str] = None
    AudioDashRoles: Optional[List[DashRoleAudioType]] = None
    DvbDashAccessibility: Optional[DvbDashAccessibilityType] = None


class UpdateChannelClassRequest(BaseValidatorModel):
    ChannelClass: ChannelClassType
    ChannelId: str
    Destinations: Optional[List[OutputDestinationUnion]] = None


class Scte35Descriptor(BaseValidatorModel):
    Scte35DescriptorSettings: Scte35DescriptorSettings


class CreateInputRequest(BaseValidatorModel):
    Destinations: Optional[List[InputDestinationRequest]] = None
    InputDevices: Optional[List[InputDeviceSettings]] = None
    InputSecurityGroups: Optional[List[str]] = None
    MediaConnectFlows: Optional[List[MediaConnectFlowRequest]] = None
    Name: Optional[str] = None
    RequestId: Optional[str] = None
    RoleArn: Optional[str] = None
    Sources: Optional[List[InputSourceRequest]] = None
    Tags: Optional[Dict[str, str]] = None
    Type: Optional[InputTypeType] = None
    Vpc: Optional[InputVpcRequest] = None
    SrtSettings: Optional[SrtSettingsRequest] = None
    InputNetworkLocation: Optional[InputNetworkLocationType] = None
    MulticastSettings: Optional[MulticastSettingsCreateRequest] = None


class UpdateInputRequest(BaseValidatorModel):
    InputId: str
    Destinations: Optional[List[InputDestinationRequest]] = None
    InputDevices: Optional[List[InputDeviceRequest]] = None
    InputSecurityGroups: Optional[List[str]] = None
    MediaConnectFlows: Optional[List[MediaConnectFlowRequest]] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Sources: Optional[List[InputSourceRequest]] = None
    SrtSettings: Optional[SrtSettingsRequest] = None
    MulticastSettings: Optional[MulticastSettingsUpdateRequest] = None


class DescribeInputResponse(BaseValidatorModel):
    Arn: str
    AttachedChannels: List[str]
    Destinations: List[InputDestination]
    Id: str
    InputClass: InputClassType
    InputDevices: List[InputDeviceSettings]
    InputPartnerIds: List[str]
    InputSourceType: InputSourceTypeType
    MediaConnectFlows: List[MediaConnectFlow]
    Name: str
    RoleArn: str
    SecurityGroups: List[str]
    Sources: List[InputSource]
    State: InputStateType
    Tags: Dict[str, str]
    Type: InputTypeType
    SrtSettings: SrtSettings
    InputNetworkLocation: InputNetworkLocationType
    MulticastSettings: MulticastSettings
    ResponseMetadata: ResponseMetadata


class Input(BaseValidatorModel):
    Arn: Optional[str] = None
    AttachedChannels: Optional[List[str]] = None
    Destinations: Optional[List[InputDestination]] = None
    Id: Optional[str] = None
    InputClass: Optional[InputClassType] = None
    InputDevices: Optional[List[InputDeviceSettings]] = None
    InputPartnerIds: Optional[List[str]] = None
    InputSourceType: Optional[InputSourceTypeType] = None
    MediaConnectFlows: Optional[List[MediaConnectFlow]] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    Sources: Optional[List[InputSource]] = None
    State: Optional[InputStateType] = None
    Tags: Optional[Dict[str, str]] = None
    Type: Optional[InputTypeType] = None
    SrtSettings: Optional[SrtSettings] = None
    InputNetworkLocation: Optional[InputNetworkLocationType] = None
    MulticastSettings: Optional[MulticastSettings] = None


class OutputGroupSettingsOutput(BaseValidatorModel):
    ArchiveGroupSettings: Optional[ArchiveGroupSettings] = None
    FrameCaptureGroupSettings: Optional[FrameCaptureGroupSettings] = None
    HlsGroupSettings: Optional[HlsGroupSettingsOutput] = None
    MediaPackageGroupSettings: Optional[MediaPackageGroupSettings] = None
    MsSmoothGroupSettings: Optional[MsSmoothGroupSettings] = None
    MultiplexGroupSettings: Optional[Dict[str, Any]] = None
    RtmpGroupSettings: Optional[RtmpGroupSettingsOutput] = None
    UdpGroupSettings: Optional[UdpGroupSettings] = None
    CmafIngestGroupSettings: Optional[CmafIngestGroupSettings] = None
    SrtGroupSettings: Optional[SrtGroupSettings] = None


class OutputGroupSettings(BaseValidatorModel):
    ArchiveGroupSettings: Optional[ArchiveGroupSettings] = None
    FrameCaptureGroupSettings: Optional[FrameCaptureGroupSettings] = None
    HlsGroupSettings: Optional[HlsGroupSettings] = None
    MediaPackageGroupSettings: Optional[MediaPackageGroupSettings] = None
    MsSmoothGroupSettings: Optional[MsSmoothGroupSettings] = None
    MultiplexGroupSettings: Optional[Dict[str, Any]] = None
    RtmpGroupSettings: Optional[RtmpGroupSettings] = None
    UdpGroupSettings: Optional[UdpGroupSettings] = None
    CmafIngestGroupSettings: Optional[CmafIngestGroupSettings] = None
    SrtGroupSettings: Optional[SrtGroupSettings] = None

AudioSelectorSettingsUnion = Union[AudioSelectorSettings, AudioSelectorSettingsOutput]


class InputSettingsOutput(BaseValidatorModel):
    AudioSelectors: Optional[List[AudioSelectorOutput]] = None
    CaptionSelectors: Optional[List[CaptionSelectorOutput]] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    FilterStrength: Optional[int] = None
    InputFilter: Optional[InputFilterType] = None
    NetworkInputSettings: Optional[NetworkInputSettings] = None
    Scte35Pid: Optional[int] = None
    Smpte2038DataPreference: Optional[Smpte2038DataPreferenceType] = None
    SourceEndBehavior: Optional[InputSourceEndBehaviorType] = None
    VideoSelector: Optional[VideoSelector] = None


class CaptionSelector(BaseValidatorModel):
    Name: str
    LanguageCode: Optional[str] = None
    SelectorSettings: Optional[CaptionSelectorSettingsUnion] = None

AutomaticInputFailoverSettingsUnion = Union[AutomaticInputFailoverSettings, AutomaticInputFailoverSettingsOutput]


class VideoDescriptionOutput(BaseValidatorModel):
    Name: str
    CodecSettings: Optional[VideoCodecSettingsOutput] = None
    Height: Optional[int] = None
    RespondToAfd: Optional[VideoDescriptionRespondToAfdType] = None
    ScalingBehavior: Optional[VideoDescriptionScalingBehaviorType] = None
    Sharpness: Optional[int] = None
    Width: Optional[int] = None


class VideoDescription(BaseValidatorModel):
    Name: str
    CodecSettings: Optional[VideoCodecSettings] = None
    Height: Optional[int] = None
    RespondToAfd: Optional[VideoDescriptionRespondToAfdType] = None
    ScalingBehavior: Optional[VideoDescriptionScalingBehaviorType] = None
    Sharpness: Optional[int] = None
    Width: Optional[int] = None


class OutputSettingsOutput(BaseValidatorModel):
    ArchiveOutputSettings: Optional[ArchiveOutputSettingsOutput] = None
    FrameCaptureOutputSettings: Optional[FrameCaptureOutputSettings] = None
    HlsOutputSettings: Optional[HlsOutputSettingsOutput] = None
    MediaPackageOutputSettings: Optional[Dict[str, Any]] = None
    MsSmoothOutputSettings: Optional[MsSmoothOutputSettings] = None
    MultiplexOutputSettings: Optional[MultiplexOutputSettings] = None
    RtmpOutputSettings: Optional[RtmpOutputSettings] = None
    UdpOutputSettings: Optional[UdpOutputSettings] = None
    CmafIngestOutputSettings: Optional[CmafIngestOutputSettings] = None
    SrtOutputSettings: Optional[SrtOutputSettings] = None


class OutputSettings(BaseValidatorModel):
    ArchiveOutputSettings: Optional[ArchiveOutputSettings] = None
    FrameCaptureOutputSettings: Optional[FrameCaptureOutputSettings] = None
    HlsOutputSettings: Optional[HlsOutputSettings] = None
    MediaPackageOutputSettings: Optional[Dict[str, Any]] = None
    MsSmoothOutputSettings: Optional[MsSmoothOutputSettings] = None
    MultiplexOutputSettings: Optional[MultiplexOutputSettings] = None
    RtmpOutputSettings: Optional[RtmpOutputSettings] = None
    UdpOutputSettings: Optional[UdpOutputSettings] = None
    CmafIngestOutputSettings: Optional[CmafIngestOutputSettings] = None
    SrtOutputSettings: Optional[SrtOutputSettings] = None


class CreateMultiplexProgramResponse(BaseValidatorModel):
    MultiplexProgram: MultiplexProgram
    ResponseMetadata: ResponseMetadata


class UpdateMultiplexProgramResponse(BaseValidatorModel):
    MultiplexProgram: MultiplexProgram
    ResponseMetadata: ResponseMetadata


class Scte35TimeSignalScheduleActionSettingsOutput(BaseValidatorModel):
    Scte35Descriptors: List[Scte35Descriptor]


class Scte35TimeSignalScheduleActionSettings(BaseValidatorModel):
    Scte35Descriptors: List[Scte35Descriptor]


class CreateInputResponse(BaseValidatorModel):
    Input: Input
    ResponseMetadata: ResponseMetadata


class CreatePartnerInputResponse(BaseValidatorModel):
    Input: Input
    ResponseMetadata: ResponseMetadata


class ListInputsResponse(BaseValidatorModel):
    Inputs: List[Input]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateInputResponse(BaseValidatorModel):
    Input: Input
    ResponseMetadata: ResponseMetadata


class AudioSelector(BaseValidatorModel):
    Name: str
    SelectorSettings: Optional[AudioSelectorSettingsUnion] = None


class InputAttachmentOutput(BaseValidatorModel):
    AutomaticInputFailoverSettings: Optional[AutomaticInputFailoverSettingsOutput] = None
    InputAttachmentName: Optional[str] = None
    InputId: Optional[str] = None
    InputSettings: Optional[InputSettingsOutput] = None
    LogicalInterfaceNames: Optional[List[str]] = None

CaptionSelectorUnion = Union[CaptionSelector, CaptionSelectorOutput]


class Extra(BaseValidatorModel):
    OutputSettings: OutputSettingsOutput
    AudioDescriptionNames: Optional[List[str]] = None
    CaptionDescriptionNames: Optional[List[str]] = None
    OutputName: Optional[str] = None
    VideoDescriptionName: Optional[str] = None


class Output(BaseValidatorModel):
    OutputSettings: OutputSettings
    AudioDescriptionNames: Optional[List[str]] = None
    CaptionDescriptionNames: Optional[List[str]] = None
    OutputName: Optional[str] = None
    VideoDescriptionName: Optional[str] = None


class ScheduleActionSettingsOutput(BaseValidatorModel):
    HlsId3SegmentTaggingSettings: Optional[HlsId3SegmentTaggingScheduleActionSettings] = None
    HlsTimedMetadataSettings: Optional[HlsTimedMetadataScheduleActionSettings] = None
    InputPrepareSettings: Optional[InputPrepareScheduleActionSettingsOutput] = None
    InputSwitchSettings: Optional[InputSwitchScheduleActionSettingsOutput] = None
    MotionGraphicsImageActivateSettings: Optional[MotionGraphicsActivateScheduleActionSettings] = None
    MotionGraphicsImageDeactivateSettings: Optional[Dict[str, Any]] = None
    PauseStateSettings: Optional[PauseStateScheduleActionSettingsOutput] = None
    Scte35InputSettings: Optional[Scte35InputScheduleActionSettings] = None
    Scte35ReturnToNetworkSettings: Optional[Scte35ReturnToNetworkScheduleActionSettings] = None
    Scte35SpliceInsertSettings: Optional[Scte35SpliceInsertScheduleActionSettings] = None
    Scte35TimeSignalSettings: Optional[Scte35TimeSignalScheduleActionSettingsOutput] = None
    StaticImageActivateSettings: Optional[StaticImageActivateScheduleActionSettings] = None
    StaticImageDeactivateSettings: Optional[StaticImageDeactivateScheduleActionSettings] = None
    StaticImageOutputActivateSettings: Optional[StaticImageOutputActivateScheduleActionSettingsOutput] = None
    StaticImageOutputDeactivateSettings: Optional[StaticImageOutputDeactivateScheduleActionSettingsOutput] = None
    Id3SegmentTaggingSettings: Optional[Id3SegmentTaggingScheduleActionSettings] = None
    TimedMetadataSettings: Optional[TimedMetadataScheduleActionSettings] = None

Scte35TimeSignalScheduleActionSettingsUnion = Union[Scte35TimeSignalScheduleActionSettings, Scte35TimeSignalScheduleActionSettingsOutput]

AudioSelectorUnion = Union[AudioSelector, AudioSelectorOutput]


class ChannelSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CdiInputSpecification: Optional[CdiInputSpecification] = None
    ChannelClass: Optional[ChannelClassType] = None
    Destinations: Optional[List[OutputDestinationOutput]] = None
    EgressEndpoints: Optional[List[ChannelEgressEndpoint]] = None
    Id: Optional[str] = None
    InputAttachments: Optional[List[InputAttachmentOutput]] = None
    InputSpecification: Optional[InputSpecification] = None
    LogLevel: Optional[LogLevelType] = None
    Maintenance: Optional[MaintenanceStatus] = None
    Name: Optional[str] = None
    PipelinesRunningCount: Optional[int] = None
    RoleArn: Optional[str] = None
    State: Optional[ChannelStateType] = None
    Tags: Optional[Dict[str, str]] = None
    Vpc: Optional[VpcOutputSettingsDescription] = None
    AnywhereSettings: Optional[DescribeAnywhereSettings] = None
    ChannelEngineVersion: Optional[ChannelEngineVersionResponse] = None
    UsedChannelEngineVersions: Optional[List[ChannelEngineVersionResponse]] = None


class OutputGroupOutput(BaseValidatorModel):
    OutputGroupSettings: OutputGroupSettingsOutput
    Outputs: List[Extra]
    Name: Optional[str] = None


class OutputGroup(BaseValidatorModel):
    OutputGroupSettings: OutputGroupSettings
    Outputs: List[Output]
    Name: Optional[str] = None


class ScheduleActionOutput(BaseValidatorModel):
    ActionName: str
    ScheduleActionSettings: ScheduleActionSettingsOutput
    ScheduleActionStartSettings: ScheduleActionStartSettingsOutput


class ScheduleActionSettings(BaseValidatorModel):
    HlsId3SegmentTaggingSettings: Optional[HlsId3SegmentTaggingScheduleActionSettings] = None
    HlsTimedMetadataSettings: Optional[HlsTimedMetadataScheduleActionSettings] = None
    InputPrepareSettings: Optional[InputPrepareScheduleActionSettingsUnion] = None
    InputSwitchSettings: Optional[InputSwitchScheduleActionSettingsUnion] = None
    MotionGraphicsImageActivateSettings: Optional[MotionGraphicsActivateScheduleActionSettings] = None
    MotionGraphicsImageDeactivateSettings: Optional[Dict[str, Any]] = None
    PauseStateSettings: Optional[PauseStateScheduleActionSettingsUnion] = None
    Scte35InputSettings: Optional[Scte35InputScheduleActionSettings] = None
    Scte35ReturnToNetworkSettings: Optional[Scte35ReturnToNetworkScheduleActionSettings] = None
    Scte35SpliceInsertSettings: Optional[Scte35SpliceInsertScheduleActionSettings] = None
    Scte35TimeSignalSettings: Optional[Scte35TimeSignalScheduleActionSettingsUnion] = None
    StaticImageActivateSettings: Optional[StaticImageActivateScheduleActionSettings] = None
    StaticImageDeactivateSettings: Optional[StaticImageDeactivateScheduleActionSettings] = None
    StaticImageOutputActivateSettings: Optional[StaticImageOutputActivateScheduleActionSettingsUnion] = None
    StaticImageOutputDeactivateSettings: Optional[StaticImageOutputDeactivateScheduleActionSettingsUnion] = None
    Id3SegmentTaggingSettings: Optional[Id3SegmentTaggingScheduleActionSettings] = None
    TimedMetadataSettings: Optional[TimedMetadataScheduleActionSettings] = None


class InputSettings(BaseValidatorModel):
    AudioSelectors: Optional[List[AudioSelectorUnion]] = None
    CaptionSelectors: Optional[List[CaptionSelectorUnion]] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    FilterStrength: Optional[int] = None
    InputFilter: Optional[InputFilterType] = None
    NetworkInputSettings: Optional[NetworkInputSettings] = None
    Scte35Pid: Optional[int] = None
    Smpte2038DataPreference: Optional[Smpte2038DataPreferenceType] = None
    SourceEndBehavior: Optional[InputSourceEndBehaviorType] = None
    VideoSelector: Optional[VideoSelector] = None


class ListChannelsResponse(BaseValidatorModel):
    Channels: List[ChannelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EncoderSettingsOutput(BaseValidatorModel):
    AudioDescriptions: List[AudioDescriptionOutput]
    OutputGroups: List[OutputGroupOutput]
    TimecodeConfig: TimecodeConfig
    VideoDescriptions: List[VideoDescriptionOutput]
    AvailBlanking: Optional[AvailBlanking] = None
    AvailConfiguration: Optional[AvailConfiguration] = None
    BlackoutSlate: Optional[BlackoutSlate] = None
    CaptionDescriptions: Optional[List[CaptionDescriptionOutput]] = None
    FeatureActivations: Optional[FeatureActivations] = None
    GlobalConfiguration: Optional[GlobalConfigurationOutput] = None
    MotionGraphicsConfiguration: Optional[MotionGraphicsConfigurationOutput] = None
    NielsenConfiguration: Optional[NielsenConfiguration] = None
    ThumbnailConfiguration: Optional[ThumbnailConfiguration] = None
    ColorCorrectionSettings: Optional[ColorCorrectionSettingsOutput] = None


class EncoderSettings(BaseValidatorModel):
    AudioDescriptions: List[AudioDescription]
    OutputGroups: List[OutputGroup]
    TimecodeConfig: TimecodeConfig
    VideoDescriptions: List[VideoDescription]
    AvailBlanking: Optional[AvailBlanking] = None
    AvailConfiguration: Optional[AvailConfiguration] = None
    BlackoutSlate: Optional[BlackoutSlate] = None
    CaptionDescriptions: Optional[List[CaptionDescription]] = None
    FeatureActivations: Optional[FeatureActivations] = None
    GlobalConfiguration: Optional[GlobalConfiguration] = None
    MotionGraphicsConfiguration: Optional[MotionGraphicsConfiguration] = None
    NielsenConfiguration: Optional[NielsenConfiguration] = None
    ThumbnailConfiguration: Optional[ThumbnailConfiguration] = None
    ColorCorrectionSettings: Optional[ColorCorrectionSettings] = None


class BatchScheduleActionCreateResult(BaseValidatorModel):
    ScheduleActions: List[ScheduleActionOutput]


class BatchScheduleActionDeleteResult(BaseValidatorModel):
    ScheduleActions: List[ScheduleActionOutput]


class DescribeScheduleResponse(BaseValidatorModel):
    ScheduleActions: List[ScheduleActionOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

ScheduleActionSettingsUnion = Union[ScheduleActionSettings, ScheduleActionSettingsOutput]

InputSettingsUnion = Union[InputSettings, InputSettingsOutput]


class Channel(BaseValidatorModel):
    Arn: Optional[str] = None
    CdiInputSpecification: Optional[CdiInputSpecification] = None
    ChannelClass: Optional[ChannelClassType] = None
    Destinations: Optional[List[OutputDestinationOutput]] = None
    EgressEndpoints: Optional[List[ChannelEgressEndpoint]] = None
    EncoderSettings: Optional[EncoderSettingsOutput] = None
    Id: Optional[str] = None
    InputAttachments: Optional[List[InputAttachmentOutput]] = None
    InputSpecification: Optional[InputSpecification] = None
    LogLevel: Optional[LogLevelType] = None
    Maintenance: Optional[MaintenanceStatus] = None
    Name: Optional[str] = None
    PipelineDetails: Optional[List[PipelineDetail]] = None
    PipelinesRunningCount: Optional[int] = None
    RoleArn: Optional[str] = None
    State: Optional[ChannelStateType] = None
    Tags: Optional[Dict[str, str]] = None
    Vpc: Optional[VpcOutputSettingsDescription] = None
    AnywhereSettings: Optional[DescribeAnywhereSettings] = None
    ChannelEngineVersion: Optional[ChannelEngineVersionResponse] = None


class DeleteChannelResponse(BaseValidatorModel):
    Arn: str
    CdiInputSpecification: CdiInputSpecification
    ChannelClass: ChannelClassType
    Destinations: List[OutputDestinationOutput]
    EgressEndpoints: List[ChannelEgressEndpoint]
    EncoderSettings: EncoderSettingsOutput
    Id: str
    InputAttachments: List[InputAttachmentOutput]
    InputSpecification: InputSpecification
    LogLevel: LogLevelType
    Maintenance: MaintenanceStatus
    Name: str
    PipelineDetails: List[PipelineDetail]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelStateType
    Tags: Dict[str, str]
    Vpc: VpcOutputSettingsDescription
    AnywhereSettings: DescribeAnywhereSettings
    ChannelEngineVersion: ChannelEngineVersionResponse
    ResponseMetadata: ResponseMetadata


class DescribeChannelResponse(BaseValidatorModel):
    Arn: str
    CdiInputSpecification: CdiInputSpecification
    ChannelClass: ChannelClassType
    Destinations: List[OutputDestinationOutput]
    EgressEndpoints: List[ChannelEgressEndpoint]
    EncoderSettings: EncoderSettingsOutput
    Id: str
    InputAttachments: List[InputAttachmentOutput]
    InputSpecification: InputSpecification
    LogLevel: LogLevelType
    Maintenance: MaintenanceStatus
    Name: str
    PipelineDetails: List[PipelineDetail]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelStateType
    Tags: Dict[str, str]
    Vpc: VpcOutputSettingsDescription
    AnywhereSettings: DescribeAnywhereSettings
    ChannelEngineVersion: ChannelEngineVersionResponse
    ResponseMetadata: ResponseMetadata


class RestartChannelPipelinesResponse(BaseValidatorModel):
    Arn: str
    CdiInputSpecification: CdiInputSpecification
    ChannelClass: ChannelClassType
    Destinations: List[OutputDestinationOutput]
    EgressEndpoints: List[ChannelEgressEndpoint]
    EncoderSettings: EncoderSettingsOutput
    Id: str
    InputAttachments: List[InputAttachmentOutput]
    InputSpecification: InputSpecification
    LogLevel: LogLevelType
    Maintenance: MaintenanceStatus
    MaintenanceStatus: str
    Name: str
    PipelineDetails: List[PipelineDetail]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelStateType
    Tags: Dict[str, str]
    Vpc: VpcOutputSettingsDescription
    AnywhereSettings: DescribeAnywhereSettings
    ChannelEngineVersion: ChannelEngineVersionResponse
    ResponseMetadata: ResponseMetadata


class StartChannelResponse(BaseValidatorModel):
    Arn: str
    CdiInputSpecification: CdiInputSpecification
    ChannelClass: ChannelClassType
    Destinations: List[OutputDestinationOutput]
    EgressEndpoints: List[ChannelEgressEndpoint]
    EncoderSettings: EncoderSettingsOutput
    Id: str
    InputAttachments: List[InputAttachmentOutput]
    InputSpecification: InputSpecification
    LogLevel: LogLevelType
    Maintenance: MaintenanceStatus
    Name: str
    PipelineDetails: List[PipelineDetail]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelStateType
    Tags: Dict[str, str]
    Vpc: VpcOutputSettingsDescription
    AnywhereSettings: DescribeAnywhereSettings
    ChannelEngineVersion: ChannelEngineVersionResponse
    ResponseMetadata: ResponseMetadata


class StopChannelResponse(BaseValidatorModel):
    Arn: str
    CdiInputSpecification: CdiInputSpecification
    ChannelClass: ChannelClassType
    Destinations: List[OutputDestinationOutput]
    EgressEndpoints: List[ChannelEgressEndpoint]
    EncoderSettings: EncoderSettingsOutput
    Id: str
    InputAttachments: List[InputAttachmentOutput]
    InputSpecification: InputSpecification
    LogLevel: LogLevelType
    Maintenance: MaintenanceStatus
    Name: str
    PipelineDetails: List[PipelineDetail]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelStateType
    Tags: Dict[str, str]
    Vpc: VpcOutputSettingsDescription
    AnywhereSettings: DescribeAnywhereSettings
    ChannelEngineVersion: ChannelEngineVersionResponse
    ResponseMetadata: ResponseMetadata

EncoderSettingsUnion = Union[EncoderSettings, EncoderSettingsOutput]


class BatchUpdateScheduleResponse(BaseValidatorModel):
    Creates: BatchScheduleActionCreateResult
    Deletes: BatchScheduleActionDeleteResult
    ResponseMetadata: ResponseMetadata


class ScheduleAction(BaseValidatorModel):
    ActionName: str
    ScheduleActionSettings: ScheduleActionSettingsUnion
    ScheduleActionStartSettings: ScheduleActionStartSettingsUnion


class InputAttachment(BaseValidatorModel):
    AutomaticInputFailoverSettings: Optional[AutomaticInputFailoverSettingsUnion] = None
    InputAttachmentName: Optional[str] = None
    InputId: Optional[str] = None
    InputSettings: Optional[InputSettingsUnion] = None
    LogicalInterfaceNames: Optional[List[str]] = None


class CreateChannelResponse(BaseValidatorModel):
    Channel: Channel
    ResponseMetadata: ResponseMetadata


class UpdateChannelClassResponse(BaseValidatorModel):
    Channel: Channel
    ResponseMetadata: ResponseMetadata


class UpdateChannelResponse(BaseValidatorModel):
    Channel: Channel
    ResponseMetadata: ResponseMetadata

ScheduleActionUnion = Union[ScheduleAction, ScheduleActionOutput]

InputAttachmentUnion = Union[InputAttachment, InputAttachmentOutput]


class BatchScheduleActionCreateRequest(BaseValidatorModel):
    ScheduleActions: List[ScheduleActionUnion]


class CreateChannelRequest(BaseValidatorModel):
    CdiInputSpecification: Optional[CdiInputSpecification] = None
    ChannelClass: Optional[ChannelClassType] = None
    Destinations: Optional[List[OutputDestinationUnion]] = None
    EncoderSettings: Optional[EncoderSettingsUnion] = None
    InputAttachments: Optional[List[InputAttachmentUnion]] = None
    InputSpecification: Optional[InputSpecification] = None
    LogLevel: Optional[LogLevelType] = None
    Maintenance: Optional[MaintenanceCreateSettings] = None
    Name: Optional[str] = None
    RequestId: Optional[str] = None
    Reserved: Optional[str] = None
    RoleArn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    Vpc: Optional[VpcOutputSettings] = None
    AnywhereSettings: Optional[AnywhereSettings] = None
    ChannelEngineVersion: Optional[ChannelEngineVersionRequest] = None
    DryRun: Optional[bool] = None


class UpdateChannelRequest(BaseValidatorModel):
    ChannelId: str
    CdiInputSpecification: Optional[CdiInputSpecification] = None
    Destinations: Optional[List[OutputDestinationUnion]] = None
    EncoderSettings: Optional[EncoderSettingsUnion] = None
    InputAttachments: Optional[List[InputAttachmentUnion]] = None
    InputSpecification: Optional[InputSpecification] = None
    LogLevel: Optional[LogLevelType] = None
    Maintenance: Optional[MaintenanceUpdateSettings] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    ChannelEngineVersion: Optional[ChannelEngineVersionRequest] = None
    DryRun: Optional[bool] = None


class BatchUpdateScheduleRequest(BaseValidatorModel):
    ChannelId: str
    Creates: Optional[BatchScheduleActionCreateRequest] = None
    Deletes: Optional[BatchScheduleActionDeleteRequest] = None