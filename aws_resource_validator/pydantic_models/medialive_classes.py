from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.medialive_constants import *

class AacSettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[float] = None
    CodingMode: Optional[AacCodingModeType] = None
    InputType: Optional[AacInputTypeType] = None
    Profile: Optional[AacProfileType] = None
    RateControlMode: Optional[AacRateControlModeType] = None
    RawFormat: Optional[AacRawFormatType] = None
    SampleRate: Optional[float] = None
    Spec: Optional[AacSpecType] = None
    VbrQuality: Optional[AacVbrQualityType] = None

class Ac3SettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[float] = None
    BitstreamMode: Optional[Ac3BitstreamModeType] = None
    CodingMode: Optional[Ac3CodingModeType] = None
    Dialnorm: Optional[int] = None
    DrcProfile: Optional[Ac3DrcProfileType] = None
    LfeFilter: Optional[Ac3LfeFilterType] = None
    MetadataControl: Optional[Ac3MetadataControlType] = None
    AttenuationControl: Optional[Ac3AttenuationControlType] = None

class AcceptInputDeviceTransferRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str

class AccountConfigurationTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None

class AncillarySourceSettingsTypeDef(BaseValidatorModel):
    SourceAncillaryChannelNumber: Optional[int] = None

class ArchiveS3SettingsTypeDef(BaseValidatorModel):
    CannedAcl: Optional[S3CannedAclType] = None

class OutputLocationRefTypeDef(BaseValidatorModel):
    DestinationRefId: Optional[str] = None

class InputChannelLevelTypeDef(BaseValidatorModel):
    Gain: int
    InputChannel: int

class Eac3AtmosSettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[float] = None
    CodingMode: Optional[Eac3AtmosCodingModeType] = None
    Dialnorm: Optional[int] = None
    DrcLine: Optional[Eac3AtmosDrcLineType] = None
    DrcRf: Optional[Eac3AtmosDrcRfType] = None
    HeightTrim: Optional[float] = None
    SurroundTrim: Optional[float] = None

class Eac3SettingsTypeDef(BaseValidatorModel):
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

class Mp2SettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[float] = None
    CodingMode: Optional[Mp2CodingModeType] = None
    SampleRate: Optional[float] = None

class WavSettingsTypeDef(BaseValidatorModel):
    BitDepth: Optional[float] = None
    CodingMode: Optional[WavCodingModeType] = None
    SampleRate: Optional[float] = None

class AudioNormalizationSettingsTypeDef(BaseValidatorModel):
    Algorithm: Optional[AudioNormalizationAlgorithmType] = None
    AlgorithmControl: Optional[Literal["CORRECT_AUDIO"]] = None
    TargetLkfs: Optional[float] = None

class AudioDolbyEDecodeTypeDef(BaseValidatorModel):
    ProgramSelection: DolbyEProgramSelectionType

class AudioHlsRenditionSelectionTypeDef(BaseValidatorModel):
    GroupId: str
    Name: str

class AudioLanguageSelectionTypeDef(BaseValidatorModel):
    LanguageCode: str
    LanguageSelectionPolicy: Optional[AudioLanguageSelectionPolicyType] = None

class InputLocationTypeDef(BaseValidatorModel):
    Uri: str
    PasswordParam: Optional[str] = None
    Username: Optional[str] = None

class AudioPidSelectionTypeDef(BaseValidatorModel):
    Pid: int

class AudioSilenceFailoverSettingsTypeDef(BaseValidatorModel):
    AudioSelectorName: str
    AudioSilenceThresholdMsec: Optional[int] = None

class AudioTrackTypeDef(BaseValidatorModel):
    Track: int

class EsamTypeDef(BaseValidatorModel):
    AcquisitionPointId: str
    PoisEndpoint: str
    AdAvailOffset: Optional[int] = None
    PasswordParam: Optional[str] = None
    Username: Optional[str] = None
    ZoneIdentity: Optional[str] = None

class Scte35SpliceInsertTypeDef(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    NoRegionalBlackoutFlag: Optional[Scte35SpliceInsertNoRegionalBlackoutBehaviorType] = None
    WebDeliveryAllowedFlag: Optional[Scte35SpliceInsertWebDeliveryAllowedBehaviorType] = None

class Scte35TimeSignalAposTypeDef(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    NoRegionalBlackoutFlag: Optional[Scte35AposNoRegionalBlackoutBehaviorType] = None
    WebDeliveryAllowedFlag: Optional[Scte35AposWebDeliveryAllowedBehaviorType] = None

class BatchDeleteRequestRequestTypeDef(BaseValidatorModel):
    ChannelIds: Optional[Sequence[str]] = None
    InputIds: Optional[Sequence[str]] = None
    InputSecurityGroupIds: Optional[Sequence[str]] = None
    MultiplexIds: Optional[Sequence[str]] = None

class BatchFailedResultModelTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Code: Optional[str] = None
    Id: Optional[str] = None
    Message: Optional[str] = None

class BatchSuccessfulResultModelTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    State: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchScheduleActionDeleteRequestTypeDef(BaseValidatorModel):
    ActionNames: Sequence[str]

class BatchStartRequestRequestTypeDef(BaseValidatorModel):
    ChannelIds: Optional[Sequence[str]] = None
    MultiplexIds: Optional[Sequence[str]] = None

class BatchStopRequestRequestTypeDef(BaseValidatorModel):
    ChannelIds: Optional[Sequence[str]] = None
    MultiplexIds: Optional[Sequence[str]] = None

class CancelInputDeviceTransferRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str

class EbuTtDDestinationSettingsTypeDef(BaseValidatorModel):
    CopyrightHolder: Optional[str] = None
    FillLineGap: Optional[EbuTtDFillLineGapControlType] = None
    FontFamily: Optional[str] = None
    StyleControl: Optional[EbuTtDDestinationStyleControlType] = None

class TtmlDestinationSettingsTypeDef(BaseValidatorModel):
    StyleControl: Optional[TtmlDestinationStyleControlType] = None

class WebvttDestinationSettingsTypeDef(BaseValidatorModel):
    StyleControl: Optional[WebvttDestinationStyleControlType] = None

class CaptionLanguageMappingTypeDef(BaseValidatorModel):
    CaptionChannel: int
    LanguageCode: str
    LanguageDescription: str

class CaptionRectangleTypeDef(BaseValidatorModel):
    Height: float
    LeftOffset: float
    TopOffset: float
    Width: float

class DvbSubSourceSettingsTypeDef(BaseValidatorModel):
    OcrLanguage: Optional[DvbSubOcrLanguageType] = None
    Pid: Optional[int] = None

class EmbeddedSourceSettingsTypeDef(BaseValidatorModel):
    Convert608To708: Optional[EmbeddedConvert608To708Type] = None
    Scte20Detection: Optional[EmbeddedScte20DetectionType] = None
    Source608ChannelNumber: Optional[int] = None
    Source608TrackNumber: Optional[int] = None

class Scte20SourceSettingsTypeDef(BaseValidatorModel):
    Convert608To708: Optional[Scte20Convert608To708Type] = None
    Source608ChannelNumber: Optional[int] = None

class Scte27SourceSettingsTypeDef(BaseValidatorModel):
    OcrLanguage: Optional[Scte27OcrLanguageType] = None
    Pid: Optional[int] = None

class CdiInputSpecificationTypeDef(BaseValidatorModel):
    Resolution: Optional[CdiInputResolutionType] = None

class ChannelEgressEndpointTypeDef(BaseValidatorModel):
    SourceIp: Optional[str] = None

class InputSpecificationTypeDef(BaseValidatorModel):
    Codec: Optional[InputCodecType] = None
    MaximumBitrate: Optional[InputMaximumBitrateType] = None
    Resolution: Optional[InputResolutionType] = None

class MaintenanceStatusTypeDef(BaseValidatorModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceDeadline: Optional[str] = None
    MaintenanceScheduledDate: Optional[str] = None
    MaintenanceStartTime: Optional[str] = None

class VpcOutputSettingsDescriptionTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None

class PipelineDetailTypeDef(BaseValidatorModel):
    ActiveInputAttachmentName: Optional[str] = None
    ActiveInputSwitchActionName: Optional[str] = None
    ActiveMotionGraphicsActionName: Optional[str] = None
    ActiveMotionGraphicsUri: Optional[str] = None
    PipelineId: Optional[str] = None

class ClaimDeviceRequestRequestTypeDef(BaseValidatorModel):
    Id: Optional[str] = None

class CloudWatchAlarmTemplateGroupSummaryTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Id: str
    Name: str
    TemplateCount: int
    Description: Optional[str] = None
    ModifiedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class CloudWatchAlarmTemplateSummaryTypeDef(BaseValidatorModel):
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

class CmafIngestOutputSettingsTypeDef(BaseValidatorModel):
    NameModifier: Optional[str] = None

class ColorCorrectionTypeDef(BaseValidatorModel):
    InputColorSpace: ColorSpaceType
    OutputColorSpace: ColorSpaceType
    Uri: str

class MaintenanceCreateSettingsTypeDef(BaseValidatorModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceStartTime: Optional[str] = None

class VpcOutputSettingsTypeDef(BaseValidatorModel):
    SubnetIds: Sequence[str]
    PublicAddressAllocationIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class CreateCloudWatchAlarmTemplateGroupRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateCloudWatchAlarmTemplateRequestRequestTypeDef(BaseValidatorModel):
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
    Tags: Optional[Mapping[str, str]] = None

class CreateEventBridgeRuleTemplateGroupRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class EventBridgeRuleTemplateTargetTypeDef(BaseValidatorModel):
    Arn: str

class InputDestinationRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None

class InputDeviceSettingsTypeDef(BaseValidatorModel):
    Id: Optional[str] = None

class InputSourceRequestTypeDef(BaseValidatorModel):
    PasswordParam: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None

class InputVpcRequestTypeDef(BaseValidatorModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None

class MediaConnectFlowRequestTypeDef(BaseValidatorModel):
    FlowArn: Optional[str] = None

class InputWhitelistRuleCidrTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None

class MultiplexSettingsTypeDef(BaseValidatorModel):
    TransportStreamBitrate: int
    TransportStreamId: int
    MaximumVideoBufferDelayMilliseconds: Optional[int] = None
    TransportStreamReservedBitrate: Optional[int] = None

class CreatePartnerInputRequestRequestTypeDef(BaseValidatorModel):
    InputId: str
    RequestId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateSignalMapRequestRequestTypeDef(BaseValidatorModel):
    DiscoveryEntryPointArn: str
    Name: str
    CloudWatchAlarmTemplateGroupIdentifiers: Optional[Sequence[str]] = None
    Description: Optional[str] = None
    EventBridgeRuleTemplateGroupIdentifiers: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class MonitorDeploymentTypeDef(BaseValidatorModel):
    Status: SignalMapMonitorDeploymentStatusType
    DetailsUri: Optional[str] = None
    ErrorMessage: Optional[str] = None

class SuccessfulMonitorDeploymentTypeDef(BaseValidatorModel):
    DetailsUri: str
    Status: SignalMapMonitorDeploymentStatusType

class CreateTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Optional[Mapping[str, str]] = None

class DeleteChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: str

class DeleteCloudWatchAlarmTemplateGroupRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class DeleteCloudWatchAlarmTemplateRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class DeleteEventBridgeRuleTemplateGroupRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class DeleteEventBridgeRuleTemplateRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class DeleteInputRequestRequestTypeDef(BaseValidatorModel):
    InputId: str

class DeleteInputSecurityGroupRequestRequestTypeDef(BaseValidatorModel):
    InputSecurityGroupId: str

class DeleteMultiplexProgramRequestRequestTypeDef(BaseValidatorModel):
    MultiplexId: str
    ProgramName: str

class MultiplexProgramPacketIdentifiersMapTypeDef(BaseValidatorModel):
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

class MultiplexProgramPipelineDetailTypeDef(BaseValidatorModel):
    ActiveChannelPipeline: Optional[str] = None
    PipelineId: Optional[str] = None

class DeleteMultiplexRequestRequestTypeDef(BaseValidatorModel):
    MultiplexId: str

class DeleteReservationRequestRequestTypeDef(BaseValidatorModel):
    ReservationId: str

class RenewalSettingsTypeDef(BaseValidatorModel):
    AutomaticRenewal: Optional[ReservationAutomaticRenewalType] = None
    RenewalCount: Optional[int] = None

class ReservationResourceSpecificationTypeDef(BaseValidatorModel):
    ChannelClass: Optional[ChannelClassType] = None
    Codec: Optional[ReservationCodecType] = None
    MaximumBitrate: Optional[ReservationMaximumBitrateType] = None
    MaximumFramerate: Optional[ReservationMaximumFramerateType] = None
    Resolution: Optional[ReservationResolutionType] = None
    ResourceType: Optional[ReservationResourceTypeType] = None
    SpecialFeature: Optional[ReservationSpecialFeatureType] = None
    VideoQuality: Optional[ReservationVideoQualityType] = None

class DeleteScheduleRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: str

class DeleteSignalMapRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class DeleteTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: str

class DescribeInputDeviceRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str

class InputDeviceHdSettingsTypeDef(BaseValidatorModel):
    ActiveInput: Optional[InputDeviceActiveInputType] = None
    ConfiguredInput: Optional[InputDeviceConfiguredInputType] = None
    DeviceState: Optional[InputDeviceStateType] = None
    Framerate: Optional[float] = None
    Height: Optional[int] = None
    MaxBitrate: Optional[int] = None
    ScanType: Optional[InputDeviceScanTypeType] = None
    Width: Optional[int] = None
    LatencyMs: Optional[int] = None

class InputDeviceNetworkSettingsTypeDef(BaseValidatorModel):
    DnsAddresses: Optional[List[str]] = None
    Gateway: Optional[str] = None
    IpAddress: Optional[str] = None
    IpScheme: Optional[InputDeviceIpSchemeType] = None
    SubnetMask: Optional[str] = None

class DescribeInputDeviceThumbnailRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str
    Accept: Literal["image/jpeg"]

class DescribeInputRequestRequestTypeDef(BaseValidatorModel):
    InputId: str

class InputSourceTypeDef(BaseValidatorModel):
    PasswordParam: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None

class MediaConnectFlowTypeDef(BaseValidatorModel):
    FlowArn: Optional[str] = None

class DescribeInputSecurityGroupRequestRequestTypeDef(BaseValidatorModel):
    InputSecurityGroupId: str

class InputWhitelistRuleTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None

class DescribeMultiplexProgramRequestRequestTypeDef(BaseValidatorModel):
    MultiplexId: str
    ProgramName: str

class DescribeMultiplexRequestRequestTypeDef(BaseValidatorModel):
    MultiplexId: str

class DescribeOfferingRequestRequestTypeDef(BaseValidatorModel):
    OfferingId: str

class DescribeReservationRequestRequestTypeDef(BaseValidatorModel):
    ReservationId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeScheduleRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeThumbnailsRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: str
    PipelineId: str
    ThumbnailType: str

class DvbNitSettingsTypeDef(BaseValidatorModel):
    NetworkId: int
    NetworkName: str
    RepInterval: Optional[int] = None

class DvbSdtSettingsTypeDef(BaseValidatorModel):
    OutputSdt: Optional[DvbSdtOutputSdtType] = None
    RepInterval: Optional[int] = None
    ServiceName: Optional[str] = None
    ServiceProviderName: Optional[str] = None

class DvbTdtSettingsTypeDef(BaseValidatorModel):
    RepInterval: Optional[int] = None

class FeatureActivationsTypeDef(BaseValidatorModel):
    InputPrepareScheduleActions: Optional[       FeatureActivationsInputPrepareScheduleActionsType     ] = None
    OutputStaticImageOverlayScheduleActions: Optional[       FeatureActivationsOutputStaticImageOverlayScheduleActionsType     ] = None

class NielsenConfigurationTypeDef(BaseValidatorModel):
    DistributorId: Optional[str] = None
    NielsenPcmToId3Tagging: Optional[NielsenPcmToId3TaggingStateType] = None

class ThumbnailConfigurationTypeDef(BaseValidatorModel):
    State: ThumbnailStateType

class TimecodeConfigTypeDef(BaseValidatorModel):
    Source: TimecodeConfigSourceType
    SyncThreshold: Optional[int] = None

class EpochLockingSettingsTypeDef(BaseValidatorModel):
    CustomEpoch: Optional[str] = None
    JamSyncTime: Optional[str] = None

class EventBridgeRuleTemplateGroupSummaryTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Id: str
    Name: str
    TemplateCount: int
    Description: Optional[str] = None
    ModifiedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class EventBridgeRuleTemplateSummaryTypeDef(BaseValidatorModel):
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

class InputLossFailoverSettingsTypeDef(BaseValidatorModel):
    InputLossThresholdMsec: Optional[int] = None

class VideoBlackFailoverSettingsTypeDef(BaseValidatorModel):
    BlackDetectThreshold: Optional[float] = None
    VideoBlackThresholdMsec: Optional[int] = None

class FecOutputSettingsTypeDef(BaseValidatorModel):
    ColumnDepth: Optional[int] = None
    IncludeFec: Optional[FecOutputIncludeFecType] = None
    RowLength: Optional[int] = None

class FixedModeScheduleActionStartSettingsTypeDef(BaseValidatorModel):
    Time: str

class Fmp4HlsSettingsTypeDef(BaseValidatorModel):
    AudioRenditionSets: Optional[str] = None
    NielsenId3Behavior: Optional[Fmp4NielsenId3BehaviorType] = None
    TimedMetadataBehavior: Optional[Fmp4TimedMetadataBehaviorType] = None

class FollowModeScheduleActionStartSettingsTypeDef(BaseValidatorModel):
    FollowPoint: FollowPointType
    ReferenceActionName: str

class FrameCaptureS3SettingsTypeDef(BaseValidatorModel):
    CannedAcl: Optional[S3CannedAclType] = None

class FrameCaptureOutputSettingsTypeDef(BaseValidatorModel):
    NameModifier: Optional[str] = None

class TimecodeBurninSettingsTypeDef(BaseValidatorModel):
    FontSize: TimecodeBurninFontSizeType
    Position: TimecodeBurninPositionType
    Prefix: Optional[str] = None

class GetCloudWatchAlarmTemplateGroupRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class GetCloudWatchAlarmTemplateRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class GetEventBridgeRuleTemplateGroupRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class GetEventBridgeRuleTemplateRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class GetSignalMapRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class H264ColorSpaceSettingsOutputTypeDef(BaseValidatorModel):
    ColorSpacePassthroughSettings: Optional[Dict[str, Any]] = None
    Rec601Settings: Optional[Dict[str, Any]] = None
    Rec709Settings: Optional[Dict[str, Any]] = None

class H264ColorSpaceSettingsTypeDef(BaseValidatorModel):
    ColorSpacePassthroughSettings: Optional[Mapping[str, Any]] = None
    Rec601Settings: Optional[Mapping[str, Any]] = None
    Rec709Settings: Optional[Mapping[str, Any]] = None

class TemporalFilterSettingsTypeDef(BaseValidatorModel):
    PostFilterSharpening: Optional[TemporalFilterPostFilterSharpeningType] = None
    Strength: Optional[TemporalFilterStrengthType] = None

class Hdr10SettingsTypeDef(BaseValidatorModel):
    MaxCll: Optional[int] = None
    MaxFall: Optional[int] = None

class HlsAkamaiSettingsTypeDef(BaseValidatorModel):
    ConnectionRetryInterval: Optional[int] = None
    FilecacheDuration: Optional[int] = None
    HttpTransferMode: Optional[HlsAkamaiHttpTransferModeType] = None
    NumRetries: Optional[int] = None
    RestartDelay: Optional[int] = None
    Salt: Optional[str] = None
    Token: Optional[str] = None

class HlsBasicPutSettingsTypeDef(BaseValidatorModel):
    ConnectionRetryInterval: Optional[int] = None
    FilecacheDuration: Optional[int] = None
    NumRetries: Optional[int] = None
    RestartDelay: Optional[int] = None

class HlsMediaStoreSettingsTypeDef(BaseValidatorModel):
    ConnectionRetryInterval: Optional[int] = None
    FilecacheDuration: Optional[int] = None
    MediaStoreStorageClass: Optional[Literal["TEMPORAL"]] = None
    NumRetries: Optional[int] = None
    RestartDelay: Optional[int] = None

class HlsS3SettingsTypeDef(BaseValidatorModel):
    CannedAcl: Optional[S3CannedAclType] = None

class HlsWebdavSettingsTypeDef(BaseValidatorModel):
    ConnectionRetryInterval: Optional[int] = None
    FilecacheDuration: Optional[int] = None
    HttpTransferMode: Optional[HlsWebdavHttpTransferModeType] = None
    NumRetries: Optional[int] = None
    RestartDelay: Optional[int] = None

class HlsId3SegmentTaggingScheduleActionSettingsTypeDef(BaseValidatorModel):
    Tag: Optional[str] = None
    Id3: Optional[str] = None

class HlsInputSettingsTypeDef(BaseValidatorModel):
    Bandwidth: Optional[int] = None
    BufferSegments: Optional[int] = None
    Retries: Optional[int] = None
    RetryInterval: Optional[int] = None
    Scte35Source: Optional[HlsScte35SourceTypeType] = None

class HlsTimedMetadataScheduleActionSettingsTypeDef(BaseValidatorModel):
    Id3: str

class StartTimecodeTypeDef(BaseValidatorModel):
    Timecode: Optional[str] = None

class StopTimecodeTypeDef(BaseValidatorModel):
    LastFrameClippingBehavior: Optional[LastFrameClippingBehaviorType] = None
    Timecode: Optional[str] = None

class InputDestinationVpcTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None

class InputDeviceConfigurableAudioChannelPairConfigTypeDef(BaseValidatorModel):
    Id: Optional[int] = None
    Profile: Optional[InputDeviceConfigurableAudioChannelPairProfileType] = None

class InputDeviceMediaConnectConfigurableSettingsTypeDef(BaseValidatorModel):
    FlowArn: Optional[str] = None
    RoleArn: Optional[str] = None
    SecretArn: Optional[str] = None
    SourceName: Optional[str] = None

class InputDeviceMediaConnectSettingsTypeDef(BaseValidatorModel):
    FlowArn: Optional[str] = None
    RoleArn: Optional[str] = None
    SecretArn: Optional[str] = None
    SourceName: Optional[str] = None

class InputDeviceRequestTypeDef(BaseValidatorModel):
    Id: Optional[str] = None

class InputDeviceUhdAudioChannelPairConfigTypeDef(BaseValidatorModel):
    Id: Optional[int] = None
    Profile: Optional[InputDeviceUhdAudioChannelPairProfileType] = None

class ListChannelsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCloudWatchAlarmTemplateGroupsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Scope: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None

class ListCloudWatchAlarmTemplatesRequestRequestTypeDef(BaseValidatorModel):
    GroupIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Scope: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None

class ListEventBridgeRuleTemplateGroupsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None

class ListEventBridgeRuleTemplatesRequestRequestTypeDef(BaseValidatorModel):
    GroupIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None

class ListInputDeviceTransfersRequestRequestTypeDef(BaseValidatorModel):
    TransferType: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TransferringInputDeviceSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Message: Optional[str] = None
    TargetCustomerId: Optional[str] = None
    TransferType: Optional[InputDeviceTransferTypeType] = None

class ListInputDevicesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInputSecurityGroupsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInputsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMultiplexProgramsRequestRequestTypeDef(BaseValidatorModel):
    MultiplexId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MultiplexProgramSummaryTypeDef(BaseValidatorModel):
    ChannelId: Optional[str] = None
    ProgramName: Optional[str] = None

class ListMultiplexesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOfferingsRequestRequestTypeDef(BaseValidatorModel):
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

class ListReservationsRequestRequestTypeDef(BaseValidatorModel):
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

class ListSignalMapsRequestRequestTypeDef(BaseValidatorModel):
    CloudWatchAlarmTemplateGroupIdentifier: Optional[str] = None
    EventBridgeRuleTemplateGroupIdentifier: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SignalMapSummaryTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Id: str
    MonitorDeploymentStatus: SignalMapMonitorDeploymentStatusType
    Name: str
    Status: SignalMapStatusType
    Description: Optional[str] = None
    ModifiedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class M3u8SettingsTypeDef(BaseValidatorModel):
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

class MaintenanceUpdateSettingsTypeDef(BaseValidatorModel):
    MaintenanceDay: Optional[MaintenanceDayType] = None
    MaintenanceScheduledDate: Optional[str] = None
    MaintenanceStartTime: Optional[str] = None

class MediaPackageOutputDestinationSettingsTypeDef(BaseValidatorModel):
    ChannelId: Optional[str] = None

class MediaResourceNeighborTypeDef(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None

class MotionGraphicsActivateScheduleActionSettingsTypeDef(BaseValidatorModel):
    Duration: Optional[int] = None
    PasswordParam: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None

class MotionGraphicsSettingsOutputTypeDef(BaseValidatorModel):
    HtmlMotionGraphicsSettings: Optional[Dict[str, Any]] = None

class MotionGraphicsSettingsTypeDef(BaseValidatorModel):
    HtmlMotionGraphicsSettings: Optional[Mapping[str, Any]] = None

class MsSmoothOutputSettingsTypeDef(BaseValidatorModel):
    H265PackagingType: Optional[MsSmoothH265PackagingTypeType] = None
    NameModifier: Optional[str] = None

class MultiplexMediaConnectOutputDestinationSettingsTypeDef(BaseValidatorModel):
    EntitlementArn: Optional[str] = None

class MultiplexProgramChannelDestinationSettingsTypeDef(BaseValidatorModel):
    MultiplexId: Optional[str] = None
    ProgramName: Optional[str] = None

class MultiplexProgramServiceDescriptorTypeDef(BaseValidatorModel):
    ProviderName: str
    ServiceName: str

class MultiplexSettingsSummaryTypeDef(BaseValidatorModel):
    TransportStreamBitrate: Optional[int] = None

class MultiplexStatmuxVideoSettingsTypeDef(BaseValidatorModel):
    MaximumBitrate: Optional[int] = None
    MinimumBitrate: Optional[int] = None
    Priority: Optional[int] = None

class NielsenCBETTypeDef(BaseValidatorModel):
    CbetCheckDigitString: str
    CbetStepaside: NielsenWatermarksCbetStepasideType
    Csid: str

class NielsenNaesIiNwTypeDef(BaseValidatorModel):
    CheckDigitString: str
    Sid: float
    Timezone: Optional[NielsenWatermarkTimezonesType] = None

class OutputDestinationSettingsTypeDef(BaseValidatorModel):
    PasswordParam: Optional[str] = None
    StreamName: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None

class RtmpGroupSettingsOutputTypeDef(BaseValidatorModel):
    AdMarkers: Optional[List[Literal["ON_CUE_POINT_SCTE35"]]] = None
    AuthenticationScheme: Optional[AuthenticationSchemeType] = None
    CacheFullBehavior: Optional[RtmpCacheFullBehaviorType] = None
    CacheLength: Optional[int] = None
    CaptionData: Optional[RtmpCaptionDataType] = None
    InputLossAction: Optional[InputLossActionForRtmpOutType] = None
    RestartDelay: Optional[int] = None
    IncludeFillerNalUnits: Optional[IncludeFillerNalUnitsType] = None

class UdpGroupSettingsTypeDef(BaseValidatorModel):
    InputLossAction: Optional[InputLossActionForUdpOutType] = None
    TimedMetadataId3Frame: Optional[UdpTimedMetadataId3FrameType] = None
    TimedMetadataId3Period: Optional[int] = None

class RtmpGroupSettingsTypeDef(BaseValidatorModel):
    AdMarkers: Optional[Sequence[Literal["ON_CUE_POINT_SCTE35"]]] = None
    AuthenticationScheme: Optional[AuthenticationSchemeType] = None
    CacheFullBehavior: Optional[RtmpCacheFullBehaviorType] = None
    CacheLength: Optional[int] = None
    CaptionData: Optional[RtmpCaptionDataType] = None
    InputLossAction: Optional[InputLossActionForRtmpOutType] = None
    RestartDelay: Optional[int] = None
    IncludeFillerNalUnits: Optional[IncludeFillerNalUnitsType] = None

class PipelinePauseStateSettingsTypeDef(BaseValidatorModel):
    PipelineId: PipelineIdType

class RebootInputDeviceRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str
    Force: Optional[RebootInputDeviceForceType] = None

class RejectInputDeviceTransferRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str

class RestartChannelPipelinesRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: str
    PipelineIds: Optional[Sequence[ChannelPipelineIdToRestartType]] = None

class Scte35InputScheduleActionSettingsTypeDef(BaseValidatorModel):
    Mode: Scte35InputModeType
    InputAttachmentNameReference: Optional[str] = None

class Scte35ReturnToNetworkScheduleActionSettingsTypeDef(BaseValidatorModel):
    SpliceEventId: int

class Scte35SpliceInsertScheduleActionSettingsTypeDef(BaseValidatorModel):
    SpliceEventId: int
    Duration: Optional[int] = None

class StaticImageDeactivateScheduleActionSettingsTypeDef(BaseValidatorModel):
    FadeOut: Optional[int] = None
    Layer: Optional[int] = None

class StaticImageOutputDeactivateScheduleActionSettingsExtraOutputTypeDef(BaseValidatorModel):
    OutputNames: List[str]
    FadeOut: Optional[int] = None
    Layer: Optional[int] = None

class StaticImageOutputDeactivateScheduleActionSettingsOutputTypeDef(BaseValidatorModel):
    OutputNames: List[str]
    FadeOut: Optional[int] = None
    Layer: Optional[int] = None

class StaticImageOutputDeactivateScheduleActionSettingsTypeDef(BaseValidatorModel):
    OutputNames: Sequence[str]
    FadeOut: Optional[int] = None
    Layer: Optional[int] = None

class Scte35DeliveryRestrictionsTypeDef(BaseValidatorModel):
    ArchiveAllowedFlag: Scte35ArchiveAllowedFlagType
    DeviceRestrictions: Scte35DeviceRestrictionsType
    NoRegionalBlackoutFlag: Scte35NoRegionalBlackoutFlagType
    WebDeliveryAllowedFlag: Scte35WebDeliveryAllowedFlagType

class StartChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: str

class StartDeleteMonitorDeploymentRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class StartInputDeviceMaintenanceWindowRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str

class StartInputDeviceRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str

class StartMonitorDeploymentRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    DryRun: Optional[bool] = None

class StartMultiplexRequestRequestTypeDef(BaseValidatorModel):
    MultiplexId: str

class StartUpdateSignalMapRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    CloudWatchAlarmTemplateGroupIdentifiers: Optional[Sequence[str]] = None
    Description: Optional[str] = None
    DiscoveryEntryPointArn: Optional[str] = None
    EventBridgeRuleTemplateGroupIdentifiers: Optional[Sequence[str]] = None
    ForceRediscovery: Optional[bool] = None
    Name: Optional[str] = None

class StopChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: str

class StopInputDeviceRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str

class StopMultiplexRequestRequestTypeDef(BaseValidatorModel):
    MultiplexId: str

class ThumbnailTypeDef(BaseValidatorModel):
    Body: Optional[str] = None
    ContentType: Optional[str] = None
    ThumbnailType: Optional[ThumbnailTypeType] = None
    TimeStamp: Optional[datetime] = None

class TransferInputDeviceRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str
    TargetCustomerId: Optional[str] = None
    TargetRegion: Optional[str] = None
    TransferMessage: Optional[str] = None

class UpdateCloudWatchAlarmTemplateGroupRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None

class UpdateCloudWatchAlarmTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateEventBridgeRuleTemplateGroupRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None

class VideoSelectorPidTypeDef(BaseValidatorModel):
    Pid: Optional[int] = None

class VideoSelectorProgramIdTypeDef(BaseValidatorModel):
    ProgramId: Optional[int] = None

class UpdateAccountConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AccountConfiguration: Optional[AccountConfigurationTypeDef] = None

class ArchiveCdnSettingsTypeDef(BaseValidatorModel):
    ArchiveS3Settings: Optional[ArchiveS3SettingsTypeDef] = None

class CmafIngestGroupSettingsTypeDef(BaseValidatorModel):
    Destination: OutputLocationRefTypeDef
    NielsenId3Behavior: Optional[CmafNielsenId3BehaviorType] = None
    Scte35Type: Optional[Scte35TypeType] = None
    SegmentLength: Optional[int] = None
    SegmentLengthUnits: Optional[CmafIngestSegmentLengthUnitsType] = None
    SendDelayMs: Optional[int] = None

class MediaPackageGroupSettingsTypeDef(BaseValidatorModel):
    Destination: OutputLocationRefTypeDef

class MsSmoothGroupSettingsTypeDef(BaseValidatorModel):
    Destination: OutputLocationRefTypeDef
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

class MultiplexOutputSettingsTypeDef(BaseValidatorModel):
    Destination: OutputLocationRefTypeDef

class RtmpOutputSettingsTypeDef(BaseValidatorModel):
    Destination: OutputLocationRefTypeDef
    CertificateMode: Optional[RtmpOutputCertificateModeType] = None
    ConnectionRetryInterval: Optional[int] = None
    NumRetries: Optional[int] = None

class AudioChannelMappingOutputTypeDef(BaseValidatorModel):
    InputChannelLevels: List[InputChannelLevelTypeDef]
    OutputChannel: int

class AudioChannelMappingTypeDef(BaseValidatorModel):
    InputChannelLevels: Sequence[InputChannelLevelTypeDef]
    OutputChannel: int

class AudioCodecSettingsOutputTypeDef(BaseValidatorModel):
    AacSettings: Optional[AacSettingsTypeDef] = None
    Ac3Settings: Optional[Ac3SettingsTypeDef] = None
    Eac3AtmosSettings: Optional[Eac3AtmosSettingsTypeDef] = None
    Eac3Settings: Optional[Eac3SettingsTypeDef] = None
    Mp2Settings: Optional[Mp2SettingsTypeDef] = None
    PassThroughSettings: Optional[Dict[str, Any]] = None
    WavSettings: Optional[WavSettingsTypeDef] = None

class AudioCodecSettingsTypeDef(BaseValidatorModel):
    AacSettings: Optional[AacSettingsTypeDef] = None
    Ac3Settings: Optional[Ac3SettingsTypeDef] = None
    Eac3AtmosSettings: Optional[Eac3AtmosSettingsTypeDef] = None
    Eac3Settings: Optional[Eac3SettingsTypeDef] = None
    Mp2Settings: Optional[Mp2SettingsTypeDef] = None
    PassThroughSettings: Optional[Mapping[str, Any]] = None
    WavSettings: Optional[WavSettingsTypeDef] = None

class AudioOnlyHlsSettingsTypeDef(BaseValidatorModel):
    AudioGroupId: Optional[str] = None
    AudioOnlyImage: Optional[InputLocationTypeDef] = None
    AudioTrackType: Optional[AudioOnlyHlsTrackTypeType] = None
    SegmentType: Optional[AudioOnlyHlsSegmentTypeType] = None

class AvailBlankingTypeDef(BaseValidatorModel):
    AvailBlankingImage: Optional[InputLocationTypeDef] = None
    State: Optional[AvailBlankingStateType] = None

class BlackoutSlateTypeDef(BaseValidatorModel):
    BlackoutSlateImage: Optional[InputLocationTypeDef] = None
    NetworkEndBlackout: Optional[BlackoutSlateNetworkEndBlackoutType] = None
    NetworkEndBlackoutImage: Optional[InputLocationTypeDef] = None
    NetworkId: Optional[str] = None
    State: Optional[BlackoutSlateStateType] = None

class BurnInDestinationSettingsTypeDef(BaseValidatorModel):
    Alignment: Optional[BurnInAlignmentType] = None
    BackgroundColor: Optional[BurnInBackgroundColorType] = None
    BackgroundOpacity: Optional[int] = None
    Font: Optional[InputLocationTypeDef] = None
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

class DvbSubDestinationSettingsTypeDef(BaseValidatorModel):
    Alignment: Optional[DvbSubDestinationAlignmentType] = None
    BackgroundColor: Optional[DvbSubDestinationBackgroundColorType] = None
    BackgroundOpacity: Optional[int] = None
    Font: Optional[InputLocationTypeDef] = None
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

class InputLossBehaviorTypeDef(BaseValidatorModel):
    BlackFrameMsec: Optional[int] = None
    InputLossImageColor: Optional[str] = None
    InputLossImageSlate: Optional[InputLocationTypeDef] = None
    InputLossImageType: Optional[InputLossImageTypeType] = None
    RepeatFrameMsec: Optional[int] = None

class StaticImageActivateScheduleActionSettingsTypeDef(BaseValidatorModel):
    Image: InputLocationTypeDef
    Duration: Optional[int] = None
    FadeIn: Optional[int] = None
    FadeOut: Optional[int] = None
    Height: Optional[int] = None
    ImageX: Optional[int] = None
    ImageY: Optional[int] = None
    Layer: Optional[int] = None
    Opacity: Optional[int] = None
    Width: Optional[int] = None

class StaticImageOutputActivateScheduleActionSettingsExtraOutputTypeDef(BaseValidatorModel):
    Image: InputLocationTypeDef
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

class StaticImageOutputActivateScheduleActionSettingsOutputTypeDef(BaseValidatorModel):
    Image: InputLocationTypeDef
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

class StaticImageOutputActivateScheduleActionSettingsTypeDef(BaseValidatorModel):
    Image: InputLocationTypeDef
    OutputNames: Sequence[str]
    Duration: Optional[int] = None
    FadeIn: Optional[int] = None
    FadeOut: Optional[int] = None
    Height: Optional[int] = None
    ImageX: Optional[int] = None
    ImageY: Optional[int] = None
    Layer: Optional[int] = None
    Opacity: Optional[int] = None
    Width: Optional[int] = None

class StaticKeySettingsTypeDef(BaseValidatorModel):
    StaticKeyValue: str
    KeyProviderServer: Optional[InputLocationTypeDef] = None

class AudioTrackSelectionExtraOutputTypeDef(BaseValidatorModel):
    Tracks: List[AudioTrackTypeDef]
    DolbyEDecode: Optional[AudioDolbyEDecodeTypeDef] = None

class AudioTrackSelectionOutputTypeDef(BaseValidatorModel):
    Tracks: List[AudioTrackTypeDef]
    DolbyEDecode: Optional[AudioDolbyEDecodeTypeDef] = None

class AudioTrackSelectionTypeDef(BaseValidatorModel):
    Tracks: Sequence[AudioTrackTypeDef]
    DolbyEDecode: Optional[AudioDolbyEDecodeTypeDef] = None

class AvailSettingsTypeDef(BaseValidatorModel):
    Esam: Optional[EsamTypeDef] = None
    Scte35SpliceInsert: Optional[Scte35SpliceInsertTypeDef] = None
    Scte35TimeSignalApos: Optional[Scte35TimeSignalAposTypeDef] = None

class BatchDeleteResponseTypeDef(BaseValidatorModel):
    Failed: List[BatchFailedResultModelTypeDef]
    Successful: List[BatchSuccessfulResultModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStartResponseTypeDef(BaseValidatorModel):
    Failed: List[BatchFailedResultModelTypeDef]
    Successful: List[BatchSuccessfulResultModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStopResponseTypeDef(BaseValidatorModel):
    Failed: List[BatchFailedResultModelTypeDef]
    Successful: List[BatchSuccessfulResultModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCloudWatchAlarmTemplateGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCloudWatchAlarmTemplateResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventBridgeRuleTemplateGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountConfigurationResponseTypeDef(BaseValidatorModel):
    AccountConfiguration: AccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInputDeviceThumbnailResponseTypeDef(BaseValidatorModel):
    Body: StreamingBody
    ContentType: Literal["image/jpeg"]
    ContentLength: int
    ETag: str
    LastModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCloudWatchAlarmTemplateGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCloudWatchAlarmTemplateResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventBridgeRuleTemplateGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountConfigurationResponseTypeDef(BaseValidatorModel):
    AccountConfiguration: AccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCloudWatchAlarmTemplateGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCloudWatchAlarmTemplateResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventBridgeRuleTemplateGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TeletextSourceSettingsTypeDef(BaseValidatorModel):
    OutputRectangle: Optional[CaptionRectangleTypeDef] = None
    PageNumber: Optional[str] = None

class ListCloudWatchAlarmTemplateGroupsResponseTypeDef(BaseValidatorModel):
    CloudWatchAlarmTemplateGroups: List[CloudWatchAlarmTemplateGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCloudWatchAlarmTemplatesResponseTypeDef(BaseValidatorModel):
    CloudWatchAlarmTemplates: List[CloudWatchAlarmTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ColorCorrectionSettingsOutputTypeDef(BaseValidatorModel):
    GlobalColorCorrections: List[ColorCorrectionTypeDef]

class ColorCorrectionSettingsTypeDef(BaseValidatorModel):
    GlobalColorCorrections: Sequence[ColorCorrectionTypeDef]

class CreateEventBridgeRuleTemplateRequestRequestTypeDef(BaseValidatorModel):
    EventType: EventBridgeRuleTemplateEventTypeType
    GroupIdentifier: str
    Name: str
    Description: Optional[str] = None
    EventTargets: Optional[Sequence[EventBridgeRuleTemplateTargetTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateEventBridgeRuleTemplateResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    EventTargets: List[EventBridgeRuleTemplateTargetTypeDef]
    EventType: EventBridgeRuleTemplateEventTypeType
    GroupId: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventBridgeRuleTemplateResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    EventTargets: List[EventBridgeRuleTemplateTargetTypeDef]
    EventType: EventBridgeRuleTemplateEventTypeType
    GroupId: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventBridgeRuleTemplateRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None
    EventTargets: Optional[Sequence[EventBridgeRuleTemplateTargetTypeDef]] = None
    EventType: Optional[EventBridgeRuleTemplateEventTypeType] = None
    GroupIdentifier: Optional[str] = None
    Name: Optional[str] = None

class UpdateEventBridgeRuleTemplateResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    Description: str
    EventTargets: List[EventBridgeRuleTemplateTargetTypeDef]
    EventType: EventBridgeRuleTemplateEventTypeType
    GroupId: str
    Id: str
    ModifiedAt: datetime
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInputRequestRequestTypeDef(BaseValidatorModel):
    Destinations: Optional[Sequence[InputDestinationRequestTypeDef]] = None
    InputDevices: Optional[Sequence[InputDeviceSettingsTypeDef]] = None
    InputSecurityGroups: Optional[Sequence[str]] = None
    MediaConnectFlows: Optional[Sequence[MediaConnectFlowRequestTypeDef]] = None
    Name: Optional[str] = None
    RequestId: Optional[str] = None
    RoleArn: Optional[str] = None
    Sources: Optional[Sequence[InputSourceRequestTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None
    Type: Optional[InputTypeType] = None
    Vpc: Optional[InputVpcRequestTypeDef] = None

class CreateInputSecurityGroupRequestRequestTypeDef(BaseValidatorModel):
    Tags: Optional[Mapping[str, str]] = None
    WhitelistRules: Optional[Sequence[InputWhitelistRuleCidrTypeDef]] = None

class UpdateInputSecurityGroupRequestRequestTypeDef(BaseValidatorModel):
    InputSecurityGroupId: str
    Tags: Optional[Mapping[str, str]] = None
    WhitelistRules: Optional[Sequence[InputWhitelistRuleCidrTypeDef]] = None

class CreateMultiplexRequestRequestTypeDef(BaseValidatorModel):
    AvailabilityZones: Sequence[str]
    MultiplexSettings: MultiplexSettingsTypeDef
    Name: str
    RequestId: str
    Tags: Optional[Mapping[str, str]] = None

class UpdateMultiplexRequestRequestTypeDef(BaseValidatorModel):
    MultiplexId: str
    MultiplexSettings: Optional[MultiplexSettingsTypeDef] = None
    Name: Optional[str] = None

class PurchaseOfferingRequestRequestTypeDef(BaseValidatorModel):
    Count: int
    OfferingId: str
    Name: Optional[str] = None
    RenewalSettings: Optional[RenewalSettingsTypeDef] = None
    RequestId: Optional[str] = None
    Start: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateReservationRequestRequestTypeDef(BaseValidatorModel):
    ReservationId: str
    Name: Optional[str] = None
    RenewalSettings: Optional[RenewalSettingsTypeDef] = None

class DeleteReservationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Count: int
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    End: str
    FixedPrice: float
    Name: str
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal["NO_UPFRONT"]
    Region: str
    RenewalSettings: RenewalSettingsTypeDef
    ReservationId: str
    ResourceSpecification: ReservationResourceSpecificationTypeDef
    Start: str
    State: ReservationStateType
    Tags: Dict[str, str]
    UsagePrice: float
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOfferingResponseTypeDef(BaseValidatorModel):
    Arn: str
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    FixedPrice: float
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal["NO_UPFRONT"]
    Region: str
    ResourceSpecification: ReservationResourceSpecificationTypeDef
    UsagePrice: float
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReservationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Count: int
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    End: str
    FixedPrice: float
    Name: str
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal["NO_UPFRONT"]
    Region: str
    RenewalSettings: RenewalSettingsTypeDef
    ReservationId: str
    ResourceSpecification: ReservationResourceSpecificationTypeDef
    Start: str
    State: ReservationStateType
    Tags: Dict[str, str]
    UsagePrice: float
    ResponseMetadata: ResponseMetadataTypeDef

class OfferingTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CurrencyCode: Optional[str] = None
    Duration: Optional[int] = None
    DurationUnits: Optional[Literal["MONTHS"]] = None
    FixedPrice: Optional[float] = None
    OfferingDescription: Optional[str] = None
    OfferingId: Optional[str] = None
    OfferingType: Optional[Literal["NO_UPFRONT"]] = None
    Region: Optional[str] = None
    ResourceSpecification: Optional[ReservationResourceSpecificationTypeDef] = None
    UsagePrice: Optional[float] = None

class ReservationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Count: Optional[int] = None
    CurrencyCode: Optional[str] = None
    Duration: Optional[int] = None
    DurationUnits: Optional[Literal["MONTHS"]] = None
    End: Optional[str] = None
    FixedPrice: Optional[float] = None
    Name: Optional[str] = None
    OfferingDescription: Optional[str] = None
    OfferingId: Optional[str] = None
    OfferingType: Optional[Literal["NO_UPFRONT"]] = None
    Region: Optional[str] = None
    RenewalSettings: Optional[RenewalSettingsTypeDef] = None
    ReservationId: Optional[str] = None
    ResourceSpecification: Optional[ReservationResourceSpecificationTypeDef] = None
    Start: Optional[str] = None
    State: Optional[ReservationStateType] = None
    Tags: Optional[Dict[str, str]] = None
    UsagePrice: Optional[float] = None

class DescribeChannelRequestChannelCreatedWaitTypeDef(BaseValidatorModel):
    ChannelId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeChannelRequestChannelDeletedWaitTypeDef(BaseValidatorModel):
    ChannelId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeChannelRequestChannelRunningWaitTypeDef(BaseValidatorModel):
    ChannelId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeChannelRequestChannelStoppedWaitTypeDef(BaseValidatorModel):
    ChannelId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInputRequestInputAttachedWaitTypeDef(BaseValidatorModel):
    InputId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInputRequestInputDeletedWaitTypeDef(BaseValidatorModel):
    InputId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInputRequestInputDetachedWaitTypeDef(BaseValidatorModel):
    InputId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeMultiplexRequestMultiplexCreatedWaitTypeDef(BaseValidatorModel):
    MultiplexId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeMultiplexRequestMultiplexDeletedWaitTypeDef(BaseValidatorModel):
    MultiplexId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeMultiplexRequestMultiplexRunningWaitTypeDef(BaseValidatorModel):
    MultiplexId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeMultiplexRequestMultiplexStoppedWaitTypeDef(BaseValidatorModel):
    MultiplexId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetSignalMapRequestSignalMapCreatedWaitTypeDef(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetSignalMapRequestSignalMapMonitorDeletedWaitTypeDef(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetSignalMapRequestSignalMapMonitorDeployedWaitTypeDef(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetSignalMapRequestSignalMapUpdatedWaitTypeDef(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInputSecurityGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Inputs: List[str]
    State: InputSecurityGroupStateType
    Tags: Dict[str, str]
    WhitelistRules: List[InputWhitelistRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InputSecurityGroupTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Inputs: Optional[List[str]] = None
    State: Optional[InputSecurityGroupStateType] = None
    Tags: Optional[Dict[str, str]] = None
    WhitelistRules: Optional[List[InputWhitelistRuleTypeDef]] = None

class DescribeScheduleRequestDescribeSchedulePaginateTypeDef(BaseValidatorModel):
    ChannelId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCloudWatchAlarmTemplatesRequestListCloudWatchAlarmTemplatesPaginateTypeDef(BaseValidatorModel):
    GroupIdentifier: Optional[str] = None
    Scope: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventBridgeRuleTemplatesRequestListEventBridgeRuleTemplatesPaginateTypeDef(BaseValidatorModel):
    GroupIdentifier: Optional[str] = None
    SignalMapIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInputDeviceTransfersRequestListInputDeviceTransfersPaginateTypeDef(BaseValidatorModel):
    TransferType: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInputDevicesRequestListInputDevicesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInputSecurityGroupsRequestListInputSecurityGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInputsRequestListInputsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMultiplexProgramsRequestListMultiplexProgramsPaginateTypeDef(BaseValidatorModel):
    MultiplexId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMultiplexesRequestListMultiplexesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOfferingsRequestListOfferingsPaginateTypeDef(BaseValidatorModel):
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
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReservationsRequestListReservationsPaginateTypeDef(BaseValidatorModel):
    ChannelClass: Optional[str] = None
    Codec: Optional[str] = None
    MaximumBitrate: Optional[str] = None
    MaximumFramerate: Optional[str] = None
    Resolution: Optional[str] = None
    ResourceType: Optional[str] = None
    SpecialFeature: Optional[str] = None
    VideoQuality: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSignalMapsRequestListSignalMapsPaginateTypeDef(BaseValidatorModel):
    CloudWatchAlarmTemplateGroupIdentifier: Optional[str] = None
    EventBridgeRuleTemplateGroupIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class M2tsSettingsTypeDef(BaseValidatorModel):
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
    DvbNitSettings: Optional[DvbNitSettingsTypeDef] = None
    DvbSdtSettings: Optional[DvbSdtSettingsTypeDef] = None
    DvbSubPids: Optional[str] = None
    DvbTdtSettings: Optional[DvbTdtSettingsTypeDef] = None
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

class OutputLockingSettingsOutputTypeDef(BaseValidatorModel):
    EpochLockingSettings: Optional[EpochLockingSettingsTypeDef] = None
    PipelineLockingSettings: Optional[Dict[str, Any]] = None

class OutputLockingSettingsTypeDef(BaseValidatorModel):
    EpochLockingSettings: Optional[EpochLockingSettingsTypeDef] = None
    PipelineLockingSettings: Optional[Mapping[str, Any]] = None

class ListEventBridgeRuleTemplateGroupsResponseTypeDef(BaseValidatorModel):
    EventBridgeRuleTemplateGroups: List[EventBridgeRuleTemplateGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEventBridgeRuleTemplatesResponseTypeDef(BaseValidatorModel):
    EventBridgeRuleTemplates: List[EventBridgeRuleTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FailoverConditionSettingsTypeDef(BaseValidatorModel):
    AudioSilenceSettings: Optional[AudioSilenceFailoverSettingsTypeDef] = None
    InputLossSettings: Optional[InputLossFailoverSettingsTypeDef] = None
    VideoBlackSettings: Optional[VideoBlackFailoverSettingsTypeDef] = None

class ScheduleActionStartSettingsExtraOutputTypeDef(BaseValidatorModel):
    FixedModeScheduleActionStartSettings: Optional[       FixedModeScheduleActionStartSettingsTypeDef     ] = None
    FollowModeScheduleActionStartSettings: Optional[       FollowModeScheduleActionStartSettingsTypeDef     ] = None
    ImmediateModeScheduleActionStartSettings: Optional[Dict[str, Any]] = None

class ScheduleActionStartSettingsOutputTypeDef(BaseValidatorModel):
    FixedModeScheduleActionStartSettings: Optional[       FixedModeScheduleActionStartSettingsTypeDef     ] = None
    FollowModeScheduleActionStartSettings: Optional[       FollowModeScheduleActionStartSettingsTypeDef     ] = None
    ImmediateModeScheduleActionStartSettings: Optional[Dict[str, Any]] = None

class ScheduleActionStartSettingsTypeDef(BaseValidatorModel):
    FixedModeScheduleActionStartSettings: Optional[       FixedModeScheduleActionStartSettingsTypeDef     ] = None
    FollowModeScheduleActionStartSettings: Optional[       FollowModeScheduleActionStartSettingsTypeDef     ] = None
    ImmediateModeScheduleActionStartSettings: Optional[Mapping[str, Any]] = None

class FrameCaptureCdnSettingsTypeDef(BaseValidatorModel):
    FrameCaptureS3Settings: Optional[FrameCaptureS3SettingsTypeDef] = None

class FrameCaptureSettingsTypeDef(BaseValidatorModel):
    CaptureInterval: Optional[int] = None
    CaptureIntervalUnits: Optional[FrameCaptureIntervalUnitType] = None
    TimecodeBurninSettings: Optional[TimecodeBurninSettingsTypeDef] = None

class H264FilterSettingsTypeDef(BaseValidatorModel):
    TemporalFilterSettings: Optional[TemporalFilterSettingsTypeDef] = None

class H265FilterSettingsTypeDef(BaseValidatorModel):
    TemporalFilterSettings: Optional[TemporalFilterSettingsTypeDef] = None

class Mpeg2FilterSettingsTypeDef(BaseValidatorModel):
    TemporalFilterSettings: Optional[TemporalFilterSettingsTypeDef] = None

class H265ColorSpaceSettingsOutputTypeDef(BaseValidatorModel):
    ColorSpacePassthroughSettings: Optional[Dict[str, Any]] = None
    DolbyVision81Settings: Optional[Dict[str, Any]] = None
    Hdr10Settings: Optional[Hdr10SettingsTypeDef] = None
    Rec601Settings: Optional[Dict[str, Any]] = None
    Rec709Settings: Optional[Dict[str, Any]] = None

class H265ColorSpaceSettingsTypeDef(BaseValidatorModel):
    ColorSpacePassthroughSettings: Optional[Mapping[str, Any]] = None
    DolbyVision81Settings: Optional[Mapping[str, Any]] = None
    Hdr10Settings: Optional[Hdr10SettingsTypeDef] = None
    Rec601Settings: Optional[Mapping[str, Any]] = None
    Rec709Settings: Optional[Mapping[str, Any]] = None

class VideoSelectorColorSpaceSettingsTypeDef(BaseValidatorModel):
    Hdr10Settings: Optional[Hdr10SettingsTypeDef] = None

class HlsCdnSettingsTypeDef(BaseValidatorModel):
    HlsAkamaiSettings: Optional[HlsAkamaiSettingsTypeDef] = None
    HlsBasicPutSettings: Optional[HlsBasicPutSettingsTypeDef] = None
    HlsMediaStoreSettings: Optional[HlsMediaStoreSettingsTypeDef] = None
    HlsS3Settings: Optional[HlsS3SettingsTypeDef] = None
    HlsWebdavSettings: Optional[HlsWebdavSettingsTypeDef] = None

class NetworkInputSettingsTypeDef(BaseValidatorModel):
    HlsInputSettings: Optional[HlsInputSettingsTypeDef] = None
    ServerValidation: Optional[NetworkInputServerValidationType] = None

class InputClippingSettingsTypeDef(BaseValidatorModel):
    InputTimecodeSource: InputTimecodeSourceType
    StartTimecode: Optional[StartTimecodeTypeDef] = None
    StopTimecode: Optional[StopTimecodeTypeDef] = None

class InputDestinationTypeDef(BaseValidatorModel):
    Ip: Optional[str] = None
    Port: Optional[str] = None
    Url: Optional[str] = None
    Vpc: Optional[InputDestinationVpcTypeDef] = None

class InputDeviceConfigurableSettingsTypeDef(BaseValidatorModel):
    ConfiguredInput: Optional[InputDeviceConfiguredInputType] = None
    MaxBitrate: Optional[int] = None
    LatencyMs: Optional[int] = None
    Codec: Optional[InputDeviceCodecType] = None
    MediaconnectSettings: Optional[InputDeviceMediaConnectConfigurableSettingsTypeDef] = None
    AudioChannelPairs: Optional[       Sequence[InputDeviceConfigurableAudioChannelPairConfigTypeDef]     ] = None

class UpdateInputRequestRequestTypeDef(BaseValidatorModel):
    InputId: str
    Destinations: Optional[Sequence[InputDestinationRequestTypeDef]] = None
    InputDevices: Optional[Sequence[InputDeviceRequestTypeDef]] = None
    InputSecurityGroups: Optional[Sequence[str]] = None
    MediaConnectFlows: Optional[Sequence[MediaConnectFlowRequestTypeDef]] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    Sources: Optional[Sequence[InputSourceRequestTypeDef]] = None

class InputDeviceUhdSettingsTypeDef(BaseValidatorModel):
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
    MediaconnectSettings: Optional[InputDeviceMediaConnectSettingsTypeDef] = None
    AudioChannelPairs: Optional[List[InputDeviceUhdAudioChannelPairConfigTypeDef]] = None

class ListInputDeviceTransfersResponseTypeDef(BaseValidatorModel):
    InputDeviceTransfers: List[TransferringInputDeviceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMultiplexProgramsResponseTypeDef(BaseValidatorModel):
    MultiplexPrograms: List[MultiplexProgramSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSignalMapsResponseTypeDef(BaseValidatorModel):
    SignalMaps: List[SignalMapSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StandardHlsSettingsTypeDef(BaseValidatorModel):
    M3u8Settings: M3u8SettingsTypeDef
    AudioRenditionSets: Optional[str] = None

class MediaResourceTypeDef(BaseValidatorModel):
    Destinations: Optional[List[MediaResourceNeighborTypeDef]] = None
    Name: Optional[str] = None
    Sources: Optional[List[MediaResourceNeighborTypeDef]] = None

class MotionGraphicsConfigurationOutputTypeDef(BaseValidatorModel):
    MotionGraphicsSettings: MotionGraphicsSettingsOutputTypeDef
    MotionGraphicsInsertion: Optional[MotionGraphicsInsertionType] = None

class MotionGraphicsConfigurationTypeDef(BaseValidatorModel):
    MotionGraphicsSettings: MotionGraphicsSettingsTypeDef
    MotionGraphicsInsertion: Optional[MotionGraphicsInsertionType] = None

class MultiplexOutputDestinationTypeDef(BaseValidatorModel):
    MediaConnectSettings: Optional[MultiplexMediaConnectOutputDestinationSettingsTypeDef] = None

class MultiplexSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    Id: Optional[str] = None
    MultiplexSettings: Optional[MultiplexSettingsSummaryTypeDef] = None
    Name: Optional[str] = None
    PipelinesRunningCount: Optional[int] = None
    ProgramCount: Optional[int] = None
    State: Optional[MultiplexStateType] = None
    Tags: Optional[Dict[str, str]] = None

class MultiplexVideoSettingsTypeDef(BaseValidatorModel):
    ConstantBitrate: Optional[int] = None
    StatmuxSettings: Optional[MultiplexStatmuxVideoSettingsTypeDef] = None

class NielsenWatermarksSettingsTypeDef(BaseValidatorModel):
    NielsenCbetSettings: Optional[NielsenCBETTypeDef] = None
    NielsenDistributionType: Optional[NielsenWatermarksDistributionTypesType] = None
    NielsenNaesIiNwSettings: Optional[NielsenNaesIiNwTypeDef] = None

class OutputDestinationExtraOutputTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    MediaPackageSettings: Optional[List[MediaPackageOutputDestinationSettingsTypeDef]] = None
    MultiplexSettings: Optional[MultiplexProgramChannelDestinationSettingsTypeDef] = None
    Settings: Optional[List[OutputDestinationSettingsTypeDef]] = None

class OutputDestinationOutputTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    MediaPackageSettings: Optional[List[MediaPackageOutputDestinationSettingsTypeDef]] = None
    MultiplexSettings: Optional[MultiplexProgramChannelDestinationSettingsTypeDef] = None
    Settings: Optional[List[OutputDestinationSettingsTypeDef]] = None

class OutputDestinationTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    MediaPackageSettings: Optional[Sequence[MediaPackageOutputDestinationSettingsTypeDef]] = None
    MultiplexSettings: Optional[MultiplexProgramChannelDestinationSettingsTypeDef] = None
    Settings: Optional[Sequence[OutputDestinationSettingsTypeDef]] = None

class PauseStateScheduleActionSettingsExtraOutputTypeDef(BaseValidatorModel):
    Pipelines: Optional[List[PipelinePauseStateSettingsTypeDef]] = None

class PauseStateScheduleActionSettingsOutputTypeDef(BaseValidatorModel):
    Pipelines: Optional[List[PipelinePauseStateSettingsTypeDef]] = None

class PauseStateScheduleActionSettingsTypeDef(BaseValidatorModel):
    Pipelines: Optional[Sequence[PipelinePauseStateSettingsTypeDef]] = None

class Scte35SegmentationDescriptorTypeDef(BaseValidatorModel):
    SegmentationCancelIndicator: Scte35SegmentationCancelIndicatorType
    SegmentationEventId: int
    DeliveryRestrictions: Optional[Scte35DeliveryRestrictionsTypeDef] = None
    SegmentNum: Optional[int] = None
    SegmentationDuration: Optional[int] = None
    SegmentationTypeId: Optional[int] = None
    SegmentationUpid: Optional[str] = None
    SegmentationUpidType: Optional[int] = None
    SegmentsExpected: Optional[int] = None
    SubSegmentNum: Optional[int] = None
    SubSegmentsExpected: Optional[int] = None

class ThumbnailDetailTypeDef(BaseValidatorModel):
    PipelineId: Optional[str] = None
    Thumbnails: Optional[List[ThumbnailTypeDef]] = None

class VideoSelectorSettingsTypeDef(BaseValidatorModel):
    VideoSelectorPid: Optional[VideoSelectorPidTypeDef] = None
    VideoSelectorProgramId: Optional[VideoSelectorProgramIdTypeDef] = None

class ArchiveGroupSettingsTypeDef(BaseValidatorModel):
    Destination: OutputLocationRefTypeDef
    ArchiveCdnSettings: Optional[ArchiveCdnSettingsTypeDef] = None
    RolloverInterval: Optional[int] = None

class RemixSettingsOutputTypeDef(BaseValidatorModel):
    ChannelMappings: List[AudioChannelMappingOutputTypeDef]
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None

class RemixSettingsTypeDef(BaseValidatorModel):
    ChannelMappings: Sequence[AudioChannelMappingTypeDef]
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None

class CaptionDestinationSettingsOutputTypeDef(BaseValidatorModel):
    AribDestinationSettings: Optional[Dict[str, Any]] = None
    BurnInDestinationSettings: Optional[BurnInDestinationSettingsTypeDef] = None
    DvbSubDestinationSettings: Optional[DvbSubDestinationSettingsTypeDef] = None
    EbuTtDDestinationSettings: Optional[EbuTtDDestinationSettingsTypeDef] = None
    EmbeddedDestinationSettings: Optional[Dict[str, Any]] = None
    EmbeddedPlusScte20DestinationSettings: Optional[Dict[str, Any]] = None
    RtmpCaptionInfoDestinationSettings: Optional[Dict[str, Any]] = None
    Scte20PlusEmbeddedDestinationSettings: Optional[Dict[str, Any]] = None
    Scte27DestinationSettings: Optional[Dict[str, Any]] = None
    SmpteTtDestinationSettings: Optional[Dict[str, Any]] = None
    TeletextDestinationSettings: Optional[Dict[str, Any]] = None
    TtmlDestinationSettings: Optional[TtmlDestinationSettingsTypeDef] = None
    WebvttDestinationSettings: Optional[WebvttDestinationSettingsTypeDef] = None

class CaptionDestinationSettingsTypeDef(BaseValidatorModel):
    AribDestinationSettings: Optional[Mapping[str, Any]] = None
    BurnInDestinationSettings: Optional[BurnInDestinationSettingsTypeDef] = None
    DvbSubDestinationSettings: Optional[DvbSubDestinationSettingsTypeDef] = None
    EbuTtDDestinationSettings: Optional[EbuTtDDestinationSettingsTypeDef] = None
    EmbeddedDestinationSettings: Optional[Mapping[str, Any]] = None
    EmbeddedPlusScte20DestinationSettings: Optional[Mapping[str, Any]] = None
    RtmpCaptionInfoDestinationSettings: Optional[Mapping[str, Any]] = None
    Scte20PlusEmbeddedDestinationSettings: Optional[Mapping[str, Any]] = None
    Scte27DestinationSettings: Optional[Mapping[str, Any]] = None
    SmpteTtDestinationSettings: Optional[Mapping[str, Any]] = None
    TeletextDestinationSettings: Optional[Mapping[str, Any]] = None
    TtmlDestinationSettings: Optional[TtmlDestinationSettingsTypeDef] = None
    WebvttDestinationSettings: Optional[WebvttDestinationSettingsTypeDef] = None

class KeyProviderSettingsTypeDef(BaseValidatorModel):
    StaticKeySettings: Optional[StaticKeySettingsTypeDef] = None

class AudioSelectorSettingsExtraOutputTypeDef(BaseValidatorModel):
    AudioHlsRenditionSelection: Optional[AudioHlsRenditionSelectionTypeDef] = None
    AudioLanguageSelection: Optional[AudioLanguageSelectionTypeDef] = None
    AudioPidSelection: Optional[AudioPidSelectionTypeDef] = None
    AudioTrackSelection: Optional[AudioTrackSelectionExtraOutputTypeDef] = None

class AudioSelectorSettingsOutputTypeDef(BaseValidatorModel):
    AudioHlsRenditionSelection: Optional[AudioHlsRenditionSelectionTypeDef] = None
    AudioLanguageSelection: Optional[AudioLanguageSelectionTypeDef] = None
    AudioPidSelection: Optional[AudioPidSelectionTypeDef] = None
    AudioTrackSelection: Optional[AudioTrackSelectionOutputTypeDef] = None

class AudioSelectorSettingsTypeDef(BaseValidatorModel):
    AudioHlsRenditionSelection: Optional[AudioHlsRenditionSelectionTypeDef] = None
    AudioLanguageSelection: Optional[AudioLanguageSelectionTypeDef] = None
    AudioPidSelection: Optional[AudioPidSelectionTypeDef] = None
    AudioTrackSelection: Optional[AudioTrackSelectionTypeDef] = None

class AvailConfigurationTypeDef(BaseValidatorModel):
    AvailSettings: Optional[AvailSettingsTypeDef] = None
    Scte35SegmentationScope: Optional[Scte35SegmentationScopeType] = None

class CaptionSelectorSettingsExtraOutputTypeDef(BaseValidatorModel):
    AncillarySourceSettings: Optional[AncillarySourceSettingsTypeDef] = None
    AribSourceSettings: Optional[Dict[str, Any]] = None
    DvbSubSourceSettings: Optional[DvbSubSourceSettingsTypeDef] = None
    EmbeddedSourceSettings: Optional[EmbeddedSourceSettingsTypeDef] = None
    Scte20SourceSettings: Optional[Scte20SourceSettingsTypeDef] = None
    Scte27SourceSettings: Optional[Scte27SourceSettingsTypeDef] = None
    TeletextSourceSettings: Optional[TeletextSourceSettingsTypeDef] = None

class CaptionSelectorSettingsOutputTypeDef(BaseValidatorModel):
    AncillarySourceSettings: Optional[AncillarySourceSettingsTypeDef] = None
    AribSourceSettings: Optional[Dict[str, Any]] = None
    DvbSubSourceSettings: Optional[DvbSubSourceSettingsTypeDef] = None
    EmbeddedSourceSettings: Optional[EmbeddedSourceSettingsTypeDef] = None
    Scte20SourceSettings: Optional[Scte20SourceSettingsTypeDef] = None
    Scte27SourceSettings: Optional[Scte27SourceSettingsTypeDef] = None
    TeletextSourceSettings: Optional[TeletextSourceSettingsTypeDef] = None

class CaptionSelectorSettingsTypeDef(BaseValidatorModel):
    AncillarySourceSettings: Optional[AncillarySourceSettingsTypeDef] = None
    AribSourceSettings: Optional[Mapping[str, Any]] = None
    DvbSubSourceSettings: Optional[DvbSubSourceSettingsTypeDef] = None
    EmbeddedSourceSettings: Optional[EmbeddedSourceSettingsTypeDef] = None
    Scte20SourceSettings: Optional[Scte20SourceSettingsTypeDef] = None
    Scte27SourceSettings: Optional[Scte27SourceSettingsTypeDef] = None
    TeletextSourceSettings: Optional[TeletextSourceSettingsTypeDef] = None

class ListOfferingsResponseTypeDef(BaseValidatorModel):
    Offerings: List[OfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListReservationsResponseTypeDef(BaseValidatorModel):
    Reservations: List[ReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseOfferingResponseTypeDef(BaseValidatorModel):
    Reservation: ReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReservationResponseTypeDef(BaseValidatorModel):
    Reservation: ReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInputSecurityGroupResponseTypeDef(BaseValidatorModel):
    SecurityGroup: InputSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInputSecurityGroupsResponseTypeDef(BaseValidatorModel):
    InputSecurityGroups: List[InputSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateInputSecurityGroupResponseTypeDef(BaseValidatorModel):
    SecurityGroup: InputSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ArchiveContainerSettingsTypeDef(BaseValidatorModel):
    M2tsSettings: Optional[M2tsSettingsTypeDef] = None
    RawSettings: Optional[Mapping[str, Any]] = None

class UdpContainerSettingsTypeDef(BaseValidatorModel):
    M2tsSettings: Optional[M2tsSettingsTypeDef] = None

class GlobalConfigurationOutputTypeDef(BaseValidatorModel):
    InitialAudioGain: Optional[int] = None
    InputEndAction: Optional[GlobalConfigurationInputEndActionType] = None
    InputLossBehavior: Optional[InputLossBehaviorTypeDef] = None
    OutputLockingMode: Optional[GlobalConfigurationOutputLockingModeType] = None
    OutputTimingSource: Optional[GlobalConfigurationOutputTimingSourceType] = None
    SupportLowFramerateInputs: Optional[GlobalConfigurationLowFramerateInputsType] = None
    OutputLockingSettings: Optional[OutputLockingSettingsOutputTypeDef] = None

class GlobalConfigurationTypeDef(BaseValidatorModel):
    InitialAudioGain: Optional[int] = None
    InputEndAction: Optional[GlobalConfigurationInputEndActionType] = None
    InputLossBehavior: Optional[InputLossBehaviorTypeDef] = None
    OutputLockingMode: Optional[GlobalConfigurationOutputLockingModeType] = None
    OutputTimingSource: Optional[GlobalConfigurationOutputTimingSourceType] = None
    SupportLowFramerateInputs: Optional[GlobalConfigurationLowFramerateInputsType] = None
    OutputLockingSettings: Optional[OutputLockingSettingsTypeDef] = None

class FailoverConditionTypeDef(BaseValidatorModel):
    FailoverConditionSettings: Optional[FailoverConditionSettingsTypeDef] = None

class FrameCaptureGroupSettingsTypeDef(BaseValidatorModel):
    Destination: OutputLocationRefTypeDef
    FrameCaptureCdnSettings: Optional[FrameCaptureCdnSettingsTypeDef] = None

class H264SettingsOutputTypeDef(BaseValidatorModel):
    AdaptiveQuantization: Optional[H264AdaptiveQuantizationType] = None
    AfdSignaling: Optional[AfdSignalingType] = None
    Bitrate: Optional[int] = None
    BufFillPct: Optional[int] = None
    BufSize: Optional[int] = None
    ColorMetadata: Optional[H264ColorMetadataType] = None
    ColorSpaceSettings: Optional[H264ColorSpaceSettingsOutputTypeDef] = None
    EntropyEncoding: Optional[H264EntropyEncodingType] = None
    FilterSettings: Optional[H264FilterSettingsTypeDef] = None
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
    TimecodeBurninSettings: Optional[TimecodeBurninSettingsTypeDef] = None

class H264SettingsTypeDef(BaseValidatorModel):
    AdaptiveQuantization: Optional[H264AdaptiveQuantizationType] = None
    AfdSignaling: Optional[AfdSignalingType] = None
    Bitrate: Optional[int] = None
    BufFillPct: Optional[int] = None
    BufSize: Optional[int] = None
    ColorMetadata: Optional[H264ColorMetadataType] = None
    ColorSpaceSettings: Optional[H264ColorSpaceSettingsTypeDef] = None
    EntropyEncoding: Optional[H264EntropyEncodingType] = None
    FilterSettings: Optional[H264FilterSettingsTypeDef] = None
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
    TimecodeBurninSettings: Optional[TimecodeBurninSettingsTypeDef] = None

class Mpeg2SettingsTypeDef(BaseValidatorModel):
    FramerateDenominator: int
    FramerateNumerator: int
    AdaptiveQuantization: Optional[Mpeg2AdaptiveQuantizationType] = None
    AfdSignaling: Optional[AfdSignalingType] = None
    ColorMetadata: Optional[Mpeg2ColorMetadataType] = None
    ColorSpace: Optional[Mpeg2ColorSpaceType] = None
    DisplayAspectRatio: Optional[Mpeg2DisplayRatioType] = None
    FilterSettings: Optional[Mpeg2FilterSettingsTypeDef] = None
    FixedAfd: Optional[FixedAfdType] = None
    GopClosedCadence: Optional[int] = None
    GopNumBFrames: Optional[int] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[Mpeg2GopSizeUnitsType] = None
    ScanType: Optional[Mpeg2ScanTypeType] = None
    SubgopLength: Optional[Mpeg2SubGopLengthType] = None
    TimecodeInsertion: Optional[Mpeg2TimecodeInsertionBehaviorType] = None
    TimecodeBurninSettings: Optional[TimecodeBurninSettingsTypeDef] = None

class H265SettingsOutputTypeDef(BaseValidatorModel):
    FramerateDenominator: int
    FramerateNumerator: int
    AdaptiveQuantization: Optional[H265AdaptiveQuantizationType] = None
    AfdSignaling: Optional[AfdSignalingType] = None
    AlternativeTransferFunction: Optional[H265AlternativeTransferFunctionType] = None
    Bitrate: Optional[int] = None
    BufSize: Optional[int] = None
    ColorMetadata: Optional[H265ColorMetadataType] = None
    ColorSpaceSettings: Optional[H265ColorSpaceSettingsOutputTypeDef] = None
    FilterSettings: Optional[H265FilterSettingsTypeDef] = None
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
    TimecodeBurninSettings: Optional[TimecodeBurninSettingsTypeDef] = None
    MvOverPictureBoundaries: Optional[H265MvOverPictureBoundariesType] = None
    MvTemporalPredictor: Optional[H265MvTemporalPredictorType] = None
    TileHeight: Optional[int] = None
    TilePadding: Optional[H265TilePaddingType] = None
    TileWidth: Optional[int] = None
    TreeblockSize: Optional[H265TreeblockSizeType] = None

class H265SettingsTypeDef(BaseValidatorModel):
    FramerateDenominator: int
    FramerateNumerator: int
    AdaptiveQuantization: Optional[H265AdaptiveQuantizationType] = None
    AfdSignaling: Optional[AfdSignalingType] = None
    AlternativeTransferFunction: Optional[H265AlternativeTransferFunctionType] = None
    Bitrate: Optional[int] = None
    BufSize: Optional[int] = None
    ColorMetadata: Optional[H265ColorMetadataType] = None
    ColorSpaceSettings: Optional[H265ColorSpaceSettingsTypeDef] = None
    FilterSettings: Optional[H265FilterSettingsTypeDef] = None
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
    TimecodeBurninSettings: Optional[TimecodeBurninSettingsTypeDef] = None
    MvOverPictureBoundaries: Optional[H265MvOverPictureBoundariesType] = None
    MvTemporalPredictor: Optional[H265MvTemporalPredictorType] = None
    TileHeight: Optional[int] = None
    TilePadding: Optional[H265TilePaddingType] = None
    TileWidth: Optional[int] = None
    TreeblockSize: Optional[H265TreeblockSizeType] = None

class InputPrepareScheduleActionSettingsExtraOutputTypeDef(BaseValidatorModel):
    InputAttachmentNameReference: Optional[str] = None
    InputClippingSettings: Optional[InputClippingSettingsTypeDef] = None
    UrlPath: Optional[List[str]] = None

class InputPrepareScheduleActionSettingsOutputTypeDef(BaseValidatorModel):
    InputAttachmentNameReference: Optional[str] = None
    InputClippingSettings: Optional[InputClippingSettingsTypeDef] = None
    UrlPath: Optional[List[str]] = None

class InputPrepareScheduleActionSettingsTypeDef(BaseValidatorModel):
    InputAttachmentNameReference: Optional[str] = None
    InputClippingSettings: Optional[InputClippingSettingsTypeDef] = None
    UrlPath: Optional[Sequence[str]] = None

class InputSwitchScheduleActionSettingsExtraOutputTypeDef(BaseValidatorModel):
    InputAttachmentNameReference: str
    InputClippingSettings: Optional[InputClippingSettingsTypeDef] = None
    UrlPath: Optional[List[str]] = None

class InputSwitchScheduleActionSettingsOutputTypeDef(BaseValidatorModel):
    InputAttachmentNameReference: str
    InputClippingSettings: Optional[InputClippingSettingsTypeDef] = None
    UrlPath: Optional[List[str]] = None

class InputSwitchScheduleActionSettingsTypeDef(BaseValidatorModel):
    InputAttachmentNameReference: str
    InputClippingSettings: Optional[InputClippingSettingsTypeDef] = None
    UrlPath: Optional[Sequence[str]] = None

class DescribeInputResponseTypeDef(BaseValidatorModel):
    Arn: str
    AttachedChannels: List[str]
    Destinations: List[InputDestinationTypeDef]
    Id: str
    InputClass: InputClassType
    InputDevices: List[InputDeviceSettingsTypeDef]
    InputPartnerIds: List[str]
    InputSourceType: InputSourceTypeType
    MediaConnectFlows: List[MediaConnectFlowTypeDef]
    Name: str
    RoleArn: str
    SecurityGroups: List[str]
    Sources: List[InputSourceTypeDef]
    State: InputStateType
    Tags: Dict[str, str]
    Type: InputTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class InputTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AttachedChannels: Optional[List[str]] = None
    Destinations: Optional[List[InputDestinationTypeDef]] = None
    Id: Optional[str] = None
    InputClass: Optional[InputClassType] = None
    InputDevices: Optional[List[InputDeviceSettingsTypeDef]] = None
    InputPartnerIds: Optional[List[str]] = None
    InputSourceType: Optional[InputSourceTypeType] = None
    MediaConnectFlows: Optional[List[MediaConnectFlowTypeDef]] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    Sources: Optional[List[InputSourceTypeDef]] = None
    State: Optional[InputStateType] = None
    Tags: Optional[Dict[str, str]] = None
    Type: Optional[InputTypeType] = None

class UpdateInputDeviceRequestRequestTypeDef(BaseValidatorModel):
    InputDeviceId: str
    HdDeviceSettings: Optional[InputDeviceConfigurableSettingsTypeDef] = None
    Name: Optional[str] = None
    UhdDeviceSettings: Optional[InputDeviceConfigurableSettingsTypeDef] = None
    AvailabilityZone: Optional[str] = None

class DescribeInputDeviceResponseTypeDef(BaseValidatorModel):
    Arn: str
    ConnectionState: InputDeviceConnectionStateType
    DeviceSettingsSyncState: DeviceSettingsSyncStateType
    DeviceUpdateStatus: DeviceUpdateStatusType
    HdDeviceSettings: InputDeviceHdSettingsTypeDef
    Id: str
    MacAddress: str
    Name: str
    NetworkSettings: InputDeviceNetworkSettingsTypeDef
    SerialNumber: str
    Type: InputDeviceTypeType
    UhdDeviceSettings: InputDeviceUhdSettingsTypeDef
    Tags: Dict[str, str]
    AvailabilityZone: str
    MedialiveInputArns: List[str]
    OutputType: InputDeviceOutputTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class InputDeviceSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectionState: Optional[InputDeviceConnectionStateType] = None
    DeviceSettingsSyncState: Optional[DeviceSettingsSyncStateType] = None
    DeviceUpdateStatus: Optional[DeviceUpdateStatusType] = None
    HdDeviceSettings: Optional[InputDeviceHdSettingsTypeDef] = None
    Id: Optional[str] = None
    MacAddress: Optional[str] = None
    Name: Optional[str] = None
    NetworkSettings: Optional[InputDeviceNetworkSettingsTypeDef] = None
    SerialNumber: Optional[str] = None
    Type: Optional[InputDeviceTypeType] = None
    UhdDeviceSettings: Optional[InputDeviceUhdSettingsTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    AvailabilityZone: Optional[str] = None
    MedialiveInputArns: Optional[List[str]] = None
    OutputType: Optional[InputDeviceOutputTypeType] = None

class UpdateInputDeviceResponseTypeDef(BaseValidatorModel):
    Arn: str
    ConnectionState: InputDeviceConnectionStateType
    DeviceSettingsSyncState: DeviceSettingsSyncStateType
    DeviceUpdateStatus: DeviceUpdateStatusType
    HdDeviceSettings: InputDeviceHdSettingsTypeDef
    Id: str
    MacAddress: str
    Name: str
    NetworkSettings: InputDeviceNetworkSettingsTypeDef
    SerialNumber: str
    Type: InputDeviceTypeType
    UhdDeviceSettings: InputDeviceUhdSettingsTypeDef
    Tags: Dict[str, str]
    AvailabilityZone: str
    MedialiveInputArns: List[str]
    OutputType: InputDeviceOutputTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class HlsSettingsTypeDef(BaseValidatorModel):
    AudioOnlyHlsSettings: Optional[AudioOnlyHlsSettingsTypeDef] = None
    Fmp4HlsSettings: Optional[Fmp4HlsSettingsTypeDef] = None
    FrameCaptureHlsSettings: Optional[Mapping[str, Any]] = None
    StandardHlsSettings: Optional[StandardHlsSettingsTypeDef] = None

class CreateSignalMapResponseTypeDef(BaseValidatorModel):
    Arn: str
    CloudWatchAlarmTemplateGroupIds: List[str]
    CreatedAt: datetime
    Description: str
    DiscoveryEntryPointArn: str
    ErrorMessage: str
    EventBridgeRuleTemplateGroupIds: List[str]
    FailedMediaResourceMap: Dict[str, MediaResourceTypeDef]
    Id: str
    LastDiscoveredAt: datetime
    LastSuccessfulMonitorDeployment: SuccessfulMonitorDeploymentTypeDef
    MediaResourceMap: Dict[str, MediaResourceTypeDef]
    ModifiedAt: datetime
    MonitorChangesPendingDeployment: bool
    MonitorDeployment: MonitorDeploymentTypeDef
    Name: str
    Status: SignalMapStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSignalMapResponseTypeDef(BaseValidatorModel):
    Arn: str
    CloudWatchAlarmTemplateGroupIds: List[str]
    CreatedAt: datetime
    Description: str
    DiscoveryEntryPointArn: str
    ErrorMessage: str
    EventBridgeRuleTemplateGroupIds: List[str]
    FailedMediaResourceMap: Dict[str, MediaResourceTypeDef]
    Id: str
    LastDiscoveredAt: datetime
    LastSuccessfulMonitorDeployment: SuccessfulMonitorDeploymentTypeDef
    MediaResourceMap: Dict[str, MediaResourceTypeDef]
    ModifiedAt: datetime
    MonitorChangesPendingDeployment: bool
    MonitorDeployment: MonitorDeploymentTypeDef
    Name: str
    Status: SignalMapStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDeleteMonitorDeploymentResponseTypeDef(BaseValidatorModel):
    Arn: str
    CloudWatchAlarmTemplateGroupIds: List[str]
    CreatedAt: datetime
    Description: str
    DiscoveryEntryPointArn: str
    ErrorMessage: str
    EventBridgeRuleTemplateGroupIds: List[str]
    FailedMediaResourceMap: Dict[str, MediaResourceTypeDef]
    Id: str
    LastDiscoveredAt: datetime
    LastSuccessfulMonitorDeployment: SuccessfulMonitorDeploymentTypeDef
    MediaResourceMap: Dict[str, MediaResourceTypeDef]
    ModifiedAt: datetime
    MonitorChangesPendingDeployment: bool
    MonitorDeployment: MonitorDeploymentTypeDef
    Name: str
    Status: SignalMapStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMonitorDeploymentResponseTypeDef(BaseValidatorModel):
    Arn: str
    CloudWatchAlarmTemplateGroupIds: List[str]
    CreatedAt: datetime
    Description: str
    DiscoveryEntryPointArn: str
    ErrorMessage: str
    EventBridgeRuleTemplateGroupIds: List[str]
    FailedMediaResourceMap: Dict[str, MediaResourceTypeDef]
    Id: str
    LastDiscoveredAt: datetime
    LastSuccessfulMonitorDeployment: SuccessfulMonitorDeploymentTypeDef
    MediaResourceMap: Dict[str, MediaResourceTypeDef]
    ModifiedAt: datetime
    MonitorChangesPendingDeployment: bool
    MonitorDeployment: MonitorDeploymentTypeDef
    Name: str
    Status: SignalMapStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartUpdateSignalMapResponseTypeDef(BaseValidatorModel):
    Arn: str
    CloudWatchAlarmTemplateGroupIds: List[str]
    CreatedAt: datetime
    Description: str
    DiscoveryEntryPointArn: str
    ErrorMessage: str
    EventBridgeRuleTemplateGroupIds: List[str]
    FailedMediaResourceMap: Dict[str, MediaResourceTypeDef]
    Id: str
    LastDiscoveredAt: datetime
    LastSuccessfulMonitorDeployment: SuccessfulMonitorDeploymentTypeDef
    MediaResourceMap: Dict[str, MediaResourceTypeDef]
    ModifiedAt: datetime
    MonitorChangesPendingDeployment: bool
    MonitorDeployment: MonitorDeploymentTypeDef
    Name: str
    Status: SignalMapStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMultiplexResponseTypeDef(BaseValidatorModel):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List[MultiplexOutputDestinationTypeDef]
    Id: str
    MultiplexSettings: MultiplexSettingsTypeDef
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexStateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMultiplexResponseTypeDef(BaseValidatorModel):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List[MultiplexOutputDestinationTypeDef]
    Id: str
    MultiplexSettings: MultiplexSettingsTypeDef
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexStateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MultiplexTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    Destinations: Optional[List[MultiplexOutputDestinationTypeDef]] = None
    Id: Optional[str] = None
    MultiplexSettings: Optional[MultiplexSettingsTypeDef] = None
    Name: Optional[str] = None
    PipelinesRunningCount: Optional[int] = None
    ProgramCount: Optional[int] = None
    State: Optional[MultiplexStateType] = None
    Tags: Optional[Dict[str, str]] = None

class StartMultiplexResponseTypeDef(BaseValidatorModel):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List[MultiplexOutputDestinationTypeDef]
    Id: str
    MultiplexSettings: MultiplexSettingsTypeDef
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexStateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StopMultiplexResponseTypeDef(BaseValidatorModel):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List[MultiplexOutputDestinationTypeDef]
    Id: str
    MultiplexSettings: MultiplexSettingsTypeDef
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexStateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMultiplexesResponseTypeDef(BaseValidatorModel):
    Multiplexes: List[MultiplexSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MultiplexProgramSettingsTypeDef(BaseValidatorModel):
    ProgramNumber: int
    PreferredChannelPipeline: Optional[PreferredChannelPipelineType] = None
    ServiceDescriptor: Optional[MultiplexProgramServiceDescriptorTypeDef] = None
    VideoSettings: Optional[MultiplexVideoSettingsTypeDef] = None

class AudioWatermarkSettingsTypeDef(BaseValidatorModel):
    NielsenWatermarksSettings: Optional[NielsenWatermarksSettingsTypeDef] = None

class Scte35DescriptorSettingsTypeDef(BaseValidatorModel):
    SegmentationDescriptorScte35DescriptorSettings: Scte35SegmentationDescriptorTypeDef

class DescribeThumbnailsResponseTypeDef(BaseValidatorModel):
    ThumbnailDetails: List[ThumbnailDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VideoSelectorTypeDef(BaseValidatorModel):
    ColorSpace: Optional[VideoSelectorColorSpaceType] = None
    ColorSpaceSettings: Optional[VideoSelectorColorSpaceSettingsTypeDef] = None
    ColorSpaceUsage: Optional[VideoSelectorColorSpaceUsageType] = None
    SelectorSettings: Optional[VideoSelectorSettingsTypeDef] = None

class CaptionDescriptionOutputTypeDef(BaseValidatorModel):
    CaptionSelectorName: str
    Name: str
    Accessibility: Optional[AccessibilityTypeType] = None
    DestinationSettings: Optional[CaptionDestinationSettingsOutputTypeDef] = None
    LanguageCode: Optional[str] = None
    LanguageDescription: Optional[str] = None
    CaptionDashRoles: Optional[List[DashRoleCaptionType]] = None
    DvbDashAccessibility: Optional[DvbDashAccessibilityType] = None

class CaptionDescriptionTypeDef(BaseValidatorModel):
    CaptionSelectorName: str
    Name: str
    Accessibility: Optional[AccessibilityTypeType] = None
    DestinationSettings: Optional[CaptionDestinationSettingsTypeDef] = None
    LanguageCode: Optional[str] = None
    LanguageDescription: Optional[str] = None
    CaptionDashRoles: Optional[Sequence[DashRoleCaptionType]] = None
    DvbDashAccessibility: Optional[DvbDashAccessibilityType] = None

class HlsGroupSettingsOutputTypeDef(BaseValidatorModel):
    Destination: OutputLocationRefTypeDef
    AdMarkers: Optional[List[HlsAdMarkersType]] = None
    BaseUrlContent: Optional[str] = None
    BaseUrlContent1: Optional[str] = None
    BaseUrlManifest: Optional[str] = None
    BaseUrlManifest1: Optional[str] = None
    CaptionLanguageMappings: Optional[List[CaptionLanguageMappingTypeDef]] = None
    CaptionLanguageSetting: Optional[HlsCaptionLanguageSettingType] = None
    ClientCache: Optional[HlsClientCacheType] = None
    CodecSpecification: Optional[HlsCodecSpecificationType] = None
    ConstantIv: Optional[str] = None
    DirectoryStructure: Optional[HlsDirectoryStructureType] = None
    DiscontinuityTags: Optional[HlsDiscontinuityTagsType] = None
    EncryptionType: Optional[HlsEncryptionTypeType] = None
    HlsCdnSettings: Optional[HlsCdnSettingsTypeDef] = None
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
    KeyProviderSettings: Optional[KeyProviderSettingsTypeDef] = None
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

class HlsGroupSettingsTypeDef(BaseValidatorModel):
    Destination: OutputLocationRefTypeDef
    AdMarkers: Optional[Sequence[HlsAdMarkersType]] = None
    BaseUrlContent: Optional[str] = None
    BaseUrlContent1: Optional[str] = None
    BaseUrlManifest: Optional[str] = None
    BaseUrlManifest1: Optional[str] = None
    CaptionLanguageMappings: Optional[Sequence[CaptionLanguageMappingTypeDef]] = None
    CaptionLanguageSetting: Optional[HlsCaptionLanguageSettingType] = None
    ClientCache: Optional[HlsClientCacheType] = None
    CodecSpecification: Optional[HlsCodecSpecificationType] = None
    ConstantIv: Optional[str] = None
    DirectoryStructure: Optional[HlsDirectoryStructureType] = None
    DiscontinuityTags: Optional[HlsDiscontinuityTagsType] = None
    EncryptionType: Optional[HlsEncryptionTypeType] = None
    HlsCdnSettings: Optional[HlsCdnSettingsTypeDef] = None
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
    KeyProviderSettings: Optional[KeyProviderSettingsTypeDef] = None
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

class AudioSelectorExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    SelectorSettings: Optional[AudioSelectorSettingsExtraOutputTypeDef] = None

class AudioSelectorOutputTypeDef(BaseValidatorModel):
    Name: str
    SelectorSettings: Optional[AudioSelectorSettingsOutputTypeDef] = None

class AudioSelectorTypeDef(BaseValidatorModel):
    Name: str
    SelectorSettings: Optional[AudioSelectorSettingsTypeDef] = None

class CaptionSelectorExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    LanguageCode: Optional[str] = None
    SelectorSettings: Optional[CaptionSelectorSettingsExtraOutputTypeDef] = None

class CaptionSelectorOutputTypeDef(BaseValidatorModel):
    Name: str
    LanguageCode: Optional[str] = None
    SelectorSettings: Optional[CaptionSelectorSettingsOutputTypeDef] = None

class CaptionSelectorTypeDef(BaseValidatorModel):
    Name: str
    LanguageCode: Optional[str] = None
    SelectorSettings: Optional[CaptionSelectorSettingsTypeDef] = None

class ArchiveOutputSettingsTypeDef(BaseValidatorModel):
    ContainerSettings: ArchiveContainerSettingsTypeDef
    Extension: Optional[str] = None
    NameModifier: Optional[str] = None

class UdpOutputSettingsTypeDef(BaseValidatorModel):
    ContainerSettings: UdpContainerSettingsTypeDef
    Destination: OutputLocationRefTypeDef
    BufferMsec: Optional[int] = None
    FecOutputSettings: Optional[FecOutputSettingsTypeDef] = None

class AutomaticInputFailoverSettingsExtraOutputTypeDef(BaseValidatorModel):
    SecondaryInputId: str
    ErrorClearTimeMsec: Optional[int] = None
    FailoverConditions: Optional[List[FailoverConditionTypeDef]] = None
    InputPreference: Optional[InputPreferenceType] = None

class AutomaticInputFailoverSettingsOutputTypeDef(BaseValidatorModel):
    SecondaryInputId: str
    ErrorClearTimeMsec: Optional[int] = None
    FailoverConditions: Optional[List[FailoverConditionTypeDef]] = None
    InputPreference: Optional[InputPreferenceType] = None

class AutomaticInputFailoverSettingsTypeDef(BaseValidatorModel):
    SecondaryInputId: str
    ErrorClearTimeMsec: Optional[int] = None
    FailoverConditions: Optional[Sequence[FailoverConditionTypeDef]] = None
    InputPreference: Optional[InputPreferenceType] = None

class VideoCodecSettingsOutputTypeDef(BaseValidatorModel):
    FrameCaptureSettings: Optional[FrameCaptureSettingsTypeDef] = None
    H264Settings: Optional[H264SettingsOutputTypeDef] = None
    H265Settings: Optional[H265SettingsOutputTypeDef] = None
    Mpeg2Settings: Optional[Mpeg2SettingsTypeDef] = None

class VideoCodecSettingsTypeDef(BaseValidatorModel):
    FrameCaptureSettings: Optional[FrameCaptureSettingsTypeDef] = None
    H264Settings: Optional[H264SettingsTypeDef] = None
    H265Settings: Optional[H265SettingsTypeDef] = None
    Mpeg2Settings: Optional[Mpeg2SettingsTypeDef] = None

class CreateInputResponseTypeDef(BaseValidatorModel):
    Input: InputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePartnerInputResponseTypeDef(BaseValidatorModel):
    Input: InputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInputsResponseTypeDef(BaseValidatorModel):
    Inputs: List[InputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateInputResponseTypeDef(BaseValidatorModel):
    Input: InputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInputDevicesResponseTypeDef(BaseValidatorModel):
    InputDevices: List[InputDeviceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class HlsOutputSettingsTypeDef(BaseValidatorModel):
    HlsSettings: HlsSettingsTypeDef
    H265PackagingType: Optional[HlsH265PackagingTypeType] = None
    NameModifier: Optional[str] = None
    SegmentModifier: Optional[str] = None

class CreateMultiplexResponseTypeDef(BaseValidatorModel):
    Multiplex: MultiplexTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMultiplexResponseTypeDef(BaseValidatorModel):
    Multiplex: MultiplexTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMultiplexProgramRequestRequestTypeDef(BaseValidatorModel):
    MultiplexId: str
    MultiplexProgramSettings: MultiplexProgramSettingsTypeDef
    ProgramName: str
    RequestId: str

class DeleteMultiplexProgramResponseTypeDef(BaseValidatorModel):
    ChannelId: str
    MultiplexProgramSettings: MultiplexProgramSettingsTypeDef
    PacketIdentifiersMap: MultiplexProgramPacketIdentifiersMapTypeDef
    PipelineDetails: List[MultiplexProgramPipelineDetailTypeDef]
    ProgramName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMultiplexProgramResponseTypeDef(BaseValidatorModel):
    ChannelId: str
    MultiplexProgramSettings: MultiplexProgramSettingsTypeDef
    PacketIdentifiersMap: MultiplexProgramPacketIdentifiersMapTypeDef
    PipelineDetails: List[MultiplexProgramPipelineDetailTypeDef]
    ProgramName: str
    ResponseMetadata: ResponseMetadataTypeDef

class MultiplexProgramTypeDef(BaseValidatorModel):
    ChannelId: Optional[str] = None
    MultiplexProgramSettings: Optional[MultiplexProgramSettingsTypeDef] = None
    PacketIdentifiersMap: Optional[MultiplexProgramPacketIdentifiersMapTypeDef] = None
    PipelineDetails: Optional[List[MultiplexProgramPipelineDetailTypeDef]] = None
    ProgramName: Optional[str] = None

class UpdateMultiplexProgramRequestRequestTypeDef(BaseValidatorModel):
    MultiplexId: str
    ProgramName: str
    MultiplexProgramSettings: Optional[MultiplexProgramSettingsTypeDef] = None

class AudioDescriptionOutputTypeDef(BaseValidatorModel):
    AudioSelectorName: str
    Name: str
    AudioNormalizationSettings: Optional[AudioNormalizationSettingsTypeDef] = None
    AudioType: Optional[AudioTypeType] = None
    AudioTypeControl: Optional[AudioDescriptionAudioTypeControlType] = None
    AudioWatermarkingSettings: Optional[AudioWatermarkSettingsTypeDef] = None
    CodecSettings: Optional[AudioCodecSettingsOutputTypeDef] = None
    LanguageCode: Optional[str] = None
    LanguageCodeControl: Optional[AudioDescriptionLanguageCodeControlType] = None
    RemixSettings: Optional[RemixSettingsOutputTypeDef] = None
    StreamName: Optional[str] = None
    AudioDashRoles: Optional[List[DashRoleAudioType]] = None
    DvbDashAccessibility: Optional[DvbDashAccessibilityType] = None

class AudioDescriptionTypeDef(BaseValidatorModel):
    AudioSelectorName: str
    Name: str
    AudioNormalizationSettings: Optional[AudioNormalizationSettingsTypeDef] = None
    AudioType: Optional[AudioTypeType] = None
    AudioTypeControl: Optional[AudioDescriptionAudioTypeControlType] = None
    AudioWatermarkingSettings: Optional[AudioWatermarkSettingsTypeDef] = None
    CodecSettings: Optional[AudioCodecSettingsTypeDef] = None
    LanguageCode: Optional[str] = None
    LanguageCodeControl: Optional[AudioDescriptionLanguageCodeControlType] = None
    RemixSettings: Optional[RemixSettingsTypeDef] = None
    StreamName: Optional[str] = None
    AudioDashRoles: Optional[Sequence[DashRoleAudioType]] = None
    DvbDashAccessibility: Optional[DvbDashAccessibilityType] = None

class UpdateChannelClassRequestRequestTypeDef(BaseValidatorModel):
    ChannelClass: ChannelClassType
    ChannelId: str
    Destinations: Optional[Sequence[OutputDestinationUnionTypeDef]] = None

class Scte35DescriptorTypeDef(BaseValidatorModel):
    Scte35DescriptorSettings: Scte35DescriptorSettingsTypeDef

class OutputGroupSettingsOutputTypeDef(BaseValidatorModel):
    ArchiveGroupSettings: Optional[ArchiveGroupSettingsTypeDef] = None
    FrameCaptureGroupSettings: Optional[FrameCaptureGroupSettingsTypeDef] = None
    HlsGroupSettings: Optional[HlsGroupSettingsOutputTypeDef] = None
    MediaPackageGroupSettings: Optional[MediaPackageGroupSettingsTypeDef] = None
    MsSmoothGroupSettings: Optional[MsSmoothGroupSettingsTypeDef] = None
    MultiplexGroupSettings: Optional[Dict[str, Any]] = None
    RtmpGroupSettings: Optional[RtmpGroupSettingsOutputTypeDef] = None
    UdpGroupSettings: Optional[UdpGroupSettingsTypeDef] = None
    CmafIngestGroupSettings: Optional[CmafIngestGroupSettingsTypeDef] = None

class OutputGroupSettingsTypeDef(BaseValidatorModel):
    ArchiveGroupSettings: Optional[ArchiveGroupSettingsTypeDef] = None
    FrameCaptureGroupSettings: Optional[FrameCaptureGroupSettingsTypeDef] = None
    HlsGroupSettings: Optional[HlsGroupSettingsTypeDef] = None
    MediaPackageGroupSettings: Optional[MediaPackageGroupSettingsTypeDef] = None
    MsSmoothGroupSettings: Optional[MsSmoothGroupSettingsTypeDef] = None
    MultiplexGroupSettings: Optional[Mapping[str, Any]] = None
    RtmpGroupSettings: Optional[RtmpGroupSettingsTypeDef] = None
    UdpGroupSettings: Optional[UdpGroupSettingsTypeDef] = None
    CmafIngestGroupSettings: Optional[CmafIngestGroupSettingsTypeDef] = None

class InputSettingsExtraOutputTypeDef(BaseValidatorModel):
    AudioSelectors: Optional[List[AudioSelectorExtraOutputTypeDef]] = None
    CaptionSelectors: Optional[List[CaptionSelectorExtraOutputTypeDef]] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    FilterStrength: Optional[int] = None
    InputFilter: Optional[InputFilterType] = None
    NetworkInputSettings: Optional[NetworkInputSettingsTypeDef] = None
    Scte35Pid: Optional[int] = None
    Smpte2038DataPreference: Optional[Smpte2038DataPreferenceType] = None
    SourceEndBehavior: Optional[InputSourceEndBehaviorType] = None
    VideoSelector: Optional[VideoSelectorTypeDef] = None

class InputSettingsOutputTypeDef(BaseValidatorModel):
    AudioSelectors: Optional[List[AudioSelectorOutputTypeDef]] = None
    CaptionSelectors: Optional[List[CaptionSelectorOutputTypeDef]] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    FilterStrength: Optional[int] = None
    InputFilter: Optional[InputFilterType] = None
    NetworkInputSettings: Optional[NetworkInputSettingsTypeDef] = None
    Scte35Pid: Optional[int] = None
    Smpte2038DataPreference: Optional[Smpte2038DataPreferenceType] = None
    SourceEndBehavior: Optional[InputSourceEndBehaviorType] = None
    VideoSelector: Optional[VideoSelectorTypeDef] = None

class InputSettingsTypeDef(BaseValidatorModel):
    AudioSelectors: Optional[Sequence[AudioSelectorTypeDef]] = None
    CaptionSelectors: Optional[Sequence[CaptionSelectorTypeDef]] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    FilterStrength: Optional[int] = None
    InputFilter: Optional[InputFilterType] = None
    NetworkInputSettings: Optional[NetworkInputSettingsTypeDef] = None
    Scte35Pid: Optional[int] = None
    Smpte2038DataPreference: Optional[Smpte2038DataPreferenceType] = None
    SourceEndBehavior: Optional[InputSourceEndBehaviorType] = None
    VideoSelector: Optional[VideoSelectorTypeDef] = None

class VideoDescriptionOutputTypeDef(BaseValidatorModel):
    Name: str
    CodecSettings: Optional[VideoCodecSettingsOutputTypeDef] = None
    Height: Optional[int] = None
    RespondToAfd: Optional[VideoDescriptionRespondToAfdType] = None
    ScalingBehavior: Optional[VideoDescriptionScalingBehaviorType] = None
    Sharpness: Optional[int] = None
    Width: Optional[int] = None

class VideoDescriptionTypeDef(BaseValidatorModel):
    Name: str
    CodecSettings: Optional[VideoCodecSettingsTypeDef] = None
    Height: Optional[int] = None
    RespondToAfd: Optional[VideoDescriptionRespondToAfdType] = None
    ScalingBehavior: Optional[VideoDescriptionScalingBehaviorType] = None
    Sharpness: Optional[int] = None
    Width: Optional[int] = None

class OutputSettingsTypeDef(BaseValidatorModel):
    ArchiveOutputSettings: Optional[ArchiveOutputSettingsTypeDef] = None
    FrameCaptureOutputSettings: Optional[FrameCaptureOutputSettingsTypeDef] = None
    HlsOutputSettings: Optional[HlsOutputSettingsTypeDef] = None
    MediaPackageOutputSettings: Optional[Mapping[str, Any]] = None
    MsSmoothOutputSettings: Optional[MsSmoothOutputSettingsTypeDef] = None
    MultiplexOutputSettings: Optional[MultiplexOutputSettingsTypeDef] = None
    RtmpOutputSettings: Optional[RtmpOutputSettingsTypeDef] = None
    UdpOutputSettings: Optional[UdpOutputSettingsTypeDef] = None
    CmafIngestOutputSettings: Optional[CmafIngestOutputSettingsTypeDef] = None

class CreateMultiplexProgramResponseTypeDef(BaseValidatorModel):
    MultiplexProgram: MultiplexProgramTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMultiplexProgramResponseTypeDef(BaseValidatorModel):
    MultiplexProgram: MultiplexProgramTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class Scte35TimeSignalScheduleActionSettingsExtraOutputTypeDef(BaseValidatorModel):
    Scte35Descriptors: List[Scte35DescriptorTypeDef]

class Scte35TimeSignalScheduleActionSettingsOutputTypeDef(BaseValidatorModel):
    Scte35Descriptors: List[Scte35DescriptorTypeDef]

class Scte35TimeSignalScheduleActionSettingsTypeDef(BaseValidatorModel):
    Scte35Descriptors: Sequence[Scte35DescriptorTypeDef]

class InputAttachmentExtraOutputTypeDef(BaseValidatorModel):
    AutomaticInputFailoverSettings: Optional[       AutomaticInputFailoverSettingsExtraOutputTypeDef     ] = None
    InputAttachmentName: Optional[str] = None
    InputId: Optional[str] = None
    InputSettings: Optional[InputSettingsExtraOutputTypeDef] = None

class InputAttachmentOutputTypeDef(BaseValidatorModel):
    AutomaticInputFailoverSettings: Optional[AutomaticInputFailoverSettingsOutputTypeDef] = None
    InputAttachmentName: Optional[str] = None
    InputId: Optional[str] = None
    InputSettings: Optional[InputSettingsOutputTypeDef] = None

class InputAttachmentTypeDef(BaseValidatorModel):
    AutomaticInputFailoverSettings: Optional[AutomaticInputFailoverSettingsTypeDef] = None
    InputAttachmentName: Optional[str] = None
    InputId: Optional[str] = None
    InputSettings: Optional[InputSettingsTypeDef] = None

class OutputTypeDef(BaseValidatorModel):
    OutputSettings: OutputSettingsTypeDef
    AudioDescriptionNames: Optional[Sequence[str]] = None
    CaptionDescriptionNames: Optional[Sequence[str]] = None
    OutputName: Optional[str] = None
    VideoDescriptionName: Optional[str] = None

class ScheduleActionSettingsExtraOutputTypeDef(BaseValidatorModel):
    HlsId3SegmentTaggingSettings: Optional[       HlsId3SegmentTaggingScheduleActionSettingsTypeDef     ] = None
    HlsTimedMetadataSettings: Optional[HlsTimedMetadataScheduleActionSettingsTypeDef] = None
    InputPrepareSettings: Optional[InputPrepareScheduleActionSettingsExtraOutputTypeDef] = None
    InputSwitchSettings: Optional[InputSwitchScheduleActionSettingsExtraOutputTypeDef] = None
    MotionGraphicsImageActivateSettings: Optional[       MotionGraphicsActivateScheduleActionSettingsTypeDef     ] = None
    MotionGraphicsImageDeactivateSettings: Optional[Dict[str, Any]] = None
    PauseStateSettings: Optional[PauseStateScheduleActionSettingsExtraOutputTypeDef] = None
    Scte35InputSettings: Optional[Scte35InputScheduleActionSettingsTypeDef] = None
    Scte35ReturnToNetworkSettings: Optional[       Scte35ReturnToNetworkScheduleActionSettingsTypeDef     ] = None
    Scte35SpliceInsertSettings: Optional[Scte35SpliceInsertScheduleActionSettingsTypeDef] = None
    Scte35TimeSignalSettings: Optional[       Scte35TimeSignalScheduleActionSettingsExtraOutputTypeDef     ] = None
    StaticImageActivateSettings: Optional[       StaticImageActivateScheduleActionSettingsTypeDef     ] = None
    StaticImageDeactivateSettings: Optional[       StaticImageDeactivateScheduleActionSettingsTypeDef     ] = None
    StaticImageOutputActivateSettings: Optional[       StaticImageOutputActivateScheduleActionSettingsExtraOutputTypeDef     ] = None
    StaticImageOutputDeactivateSettings: Optional[       StaticImageOutputDeactivateScheduleActionSettingsExtraOutputTypeDef     ] = None

class ScheduleActionSettingsOutputTypeDef(BaseValidatorModel):
    HlsId3SegmentTaggingSettings: Optional[       HlsId3SegmentTaggingScheduleActionSettingsTypeDef     ] = None
    HlsTimedMetadataSettings: Optional[HlsTimedMetadataScheduleActionSettingsTypeDef] = None
    InputPrepareSettings: Optional[InputPrepareScheduleActionSettingsOutputTypeDef] = None
    InputSwitchSettings: Optional[InputSwitchScheduleActionSettingsOutputTypeDef] = None
    MotionGraphicsImageActivateSettings: Optional[       MotionGraphicsActivateScheduleActionSettingsTypeDef     ] = None
    MotionGraphicsImageDeactivateSettings: Optional[Dict[str, Any]] = None
    PauseStateSettings: Optional[PauseStateScheduleActionSettingsOutputTypeDef] = None
    Scte35InputSettings: Optional[Scte35InputScheduleActionSettingsTypeDef] = None
    Scte35ReturnToNetworkSettings: Optional[       Scte35ReturnToNetworkScheduleActionSettingsTypeDef     ] = None
    Scte35SpliceInsertSettings: Optional[Scte35SpliceInsertScheduleActionSettingsTypeDef] = None
    Scte35TimeSignalSettings: Optional[       Scte35TimeSignalScheduleActionSettingsOutputTypeDef     ] = None
    StaticImageActivateSettings: Optional[       StaticImageActivateScheduleActionSettingsTypeDef     ] = None
    StaticImageDeactivateSettings: Optional[       StaticImageDeactivateScheduleActionSettingsTypeDef     ] = None
    StaticImageOutputActivateSettings: Optional[       StaticImageOutputActivateScheduleActionSettingsOutputTypeDef     ] = None
    StaticImageOutputDeactivateSettings: Optional[       StaticImageOutputDeactivateScheduleActionSettingsOutputTypeDef     ] = None

class ScheduleActionSettingsTypeDef(BaseValidatorModel):
    HlsId3SegmentTaggingSettings: Optional[       HlsId3SegmentTaggingScheduleActionSettingsTypeDef     ] = None
    HlsTimedMetadataSettings: Optional[HlsTimedMetadataScheduleActionSettingsTypeDef] = None
    InputPrepareSettings: Optional[InputPrepareScheduleActionSettingsTypeDef] = None
    InputSwitchSettings: Optional[InputSwitchScheduleActionSettingsTypeDef] = None
    MotionGraphicsImageActivateSettings: Optional[       MotionGraphicsActivateScheduleActionSettingsTypeDef     ] = None
    MotionGraphicsImageDeactivateSettings: Optional[Mapping[str, Any]] = None
    PauseStateSettings: Optional[PauseStateScheduleActionSettingsTypeDef] = None
    Scte35InputSettings: Optional[Scte35InputScheduleActionSettingsTypeDef] = None
    Scte35ReturnToNetworkSettings: Optional[       Scte35ReturnToNetworkScheduleActionSettingsTypeDef     ] = None
    Scte35SpliceInsertSettings: Optional[Scte35SpliceInsertScheduleActionSettingsTypeDef] = None
    Scte35TimeSignalSettings: Optional[Scte35TimeSignalScheduleActionSettingsTypeDef] = None
    StaticImageActivateSettings: Optional[       StaticImageActivateScheduleActionSettingsTypeDef     ] = None
    StaticImageDeactivateSettings: Optional[       StaticImageDeactivateScheduleActionSettingsTypeDef     ] = None
    StaticImageOutputActivateSettings: Optional[       StaticImageOutputActivateScheduleActionSettingsTypeDef     ] = None
    StaticImageOutputDeactivateSettings: Optional[       StaticImageOutputDeactivateScheduleActionSettingsTypeDef     ] = None

class ChannelSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CdiInputSpecification: Optional[CdiInputSpecificationTypeDef] = None
    ChannelClass: Optional[ChannelClassType] = None
    Destinations: Optional[List[OutputDestinationOutputTypeDef]] = None
    EgressEndpoints: Optional[List[ChannelEgressEndpointTypeDef]] = None
    Id: Optional[str] = None
    InputAttachments: Optional[List[InputAttachmentOutputTypeDef]] = None
    InputSpecification: Optional[InputSpecificationTypeDef] = None
    LogLevel: Optional[LogLevelType] = None
    Maintenance: Optional[MaintenanceStatusTypeDef] = None
    Name: Optional[str] = None
    PipelinesRunningCount: Optional[int] = None
    RoleArn: Optional[str] = None
    State: Optional[ChannelStateType] = None
    Tags: Optional[Dict[str, str]] = None
    Vpc: Optional[VpcOutputSettingsDescriptionTypeDef] = None

class OutputGroupOutputTypeDef(BaseValidatorModel):
    OutputGroupSettings: OutputGroupSettingsOutputTypeDef
    Outputs: List[OutputTypeDef]
    Name: Optional[str] = None

class OutputGroupTypeDef(BaseValidatorModel):
    OutputGroupSettings: OutputGroupSettingsTypeDef
    Outputs: Sequence[OutputTypeDef]
    Name: Optional[str] = None

class ScheduleActionExtraOutputTypeDef(BaseValidatorModel):
    ActionName: str
    ScheduleActionSettings: ScheduleActionSettingsExtraOutputTypeDef
    ScheduleActionStartSettings: ScheduleActionStartSettingsExtraOutputTypeDef

class ScheduleActionOutputTypeDef(BaseValidatorModel):
    ActionName: str
    ScheduleActionSettings: ScheduleActionSettingsOutputTypeDef
    ScheduleActionStartSettings: ScheduleActionStartSettingsOutputTypeDef

class ScheduleActionTypeDef(BaseValidatorModel):
    ActionName: str
    ScheduleActionSettings: ScheduleActionSettingsTypeDef
    ScheduleActionStartSettings: ScheduleActionStartSettingsTypeDef

class ListChannelsResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EncoderSettingsOutputTypeDef(BaseValidatorModel):
    AudioDescriptions: List[AudioDescriptionOutputTypeDef]
    OutputGroups: List[OutputGroupOutputTypeDef]
    TimecodeConfig: TimecodeConfigTypeDef
    VideoDescriptions: List[VideoDescriptionOutputTypeDef]
    AvailBlanking: Optional[AvailBlankingTypeDef] = None
    AvailConfiguration: Optional[AvailConfigurationTypeDef] = None
    BlackoutSlate: Optional[BlackoutSlateTypeDef] = None
    CaptionDescriptions: Optional[List[CaptionDescriptionOutputTypeDef]] = None
    FeatureActivations: Optional[FeatureActivationsTypeDef] = None
    GlobalConfiguration: Optional[GlobalConfigurationOutputTypeDef] = None
    MotionGraphicsConfiguration: Optional[MotionGraphicsConfigurationOutputTypeDef] = None
    NielsenConfiguration: Optional[NielsenConfigurationTypeDef] = None
    ThumbnailConfiguration: Optional[ThumbnailConfigurationTypeDef] = None
    ColorCorrectionSettings: Optional[ColorCorrectionSettingsOutputTypeDef] = None

class EncoderSettingsTypeDef(BaseValidatorModel):
    AudioDescriptions: Sequence[AudioDescriptionTypeDef]
    OutputGroups: Sequence[OutputGroupTypeDef]
    TimecodeConfig: TimecodeConfigTypeDef
    VideoDescriptions: Sequence[VideoDescriptionTypeDef]
    AvailBlanking: Optional[AvailBlankingTypeDef] = None
    AvailConfiguration: Optional[AvailConfigurationTypeDef] = None
    BlackoutSlate: Optional[BlackoutSlateTypeDef] = None
    CaptionDescriptions: Optional[Sequence[CaptionDescriptionTypeDef]] = None
    FeatureActivations: Optional[FeatureActivationsTypeDef] = None
    GlobalConfiguration: Optional[GlobalConfigurationTypeDef] = None
    MotionGraphicsConfiguration: Optional[MotionGraphicsConfigurationTypeDef] = None
    NielsenConfiguration: Optional[NielsenConfigurationTypeDef] = None
    ThumbnailConfiguration: Optional[ThumbnailConfigurationTypeDef] = None
    ColorCorrectionSettings: Optional[ColorCorrectionSettingsTypeDef] = None

class DescribeScheduleResponseTypeDef(BaseValidatorModel):
    ScheduleActions: List[ScheduleActionExtraOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchScheduleActionCreateResultTypeDef(BaseValidatorModel):
    ScheduleActions: List[ScheduleActionOutputTypeDef]

class BatchScheduleActionDeleteResultTypeDef(BaseValidatorModel):
    ScheduleActions: List[ScheduleActionOutputTypeDef]

class BatchScheduleActionCreateRequestTypeDef(BaseValidatorModel):
    ScheduleActions: Sequence[ScheduleActionTypeDef]

class ChannelTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CdiInputSpecification: Optional[CdiInputSpecificationTypeDef] = None
    ChannelClass: Optional[ChannelClassType] = None
    Destinations: Optional[List[OutputDestinationOutputTypeDef]] = None
    EgressEndpoints: Optional[List[ChannelEgressEndpointTypeDef]] = None
    EncoderSettings: Optional[EncoderSettingsOutputTypeDef] = None
    Id: Optional[str] = None
    InputAttachments: Optional[List[InputAttachmentOutputTypeDef]] = None
    InputSpecification: Optional[InputSpecificationTypeDef] = None
    LogLevel: Optional[LogLevelType] = None
    Maintenance: Optional[MaintenanceStatusTypeDef] = None
    Name: Optional[str] = None
    PipelineDetails: Optional[List[PipelineDetailTypeDef]] = None
    PipelinesRunningCount: Optional[int] = None
    RoleArn: Optional[str] = None
    State: Optional[ChannelStateType] = None
    Tags: Optional[Dict[str, str]] = None
    Vpc: Optional[VpcOutputSettingsDescriptionTypeDef] = None

class DeleteChannelResponseTypeDef(BaseValidatorModel):
    Arn: str
    CdiInputSpecification: CdiInputSpecificationTypeDef
    ChannelClass: ChannelClassType
    Destinations: List[OutputDestinationOutputTypeDef]
    EgressEndpoints: List[ChannelEgressEndpointTypeDef]
    EncoderSettings: EncoderSettingsOutputTypeDef
    Id: str
    InputAttachments: List[InputAttachmentOutputTypeDef]
    InputSpecification: InputSpecificationTypeDef
    LogLevel: LogLevelType
    Maintenance: MaintenanceStatusTypeDef
    Name: str
    PipelineDetails: List[PipelineDetailTypeDef]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelStateType
    Tags: Dict[str, str]
    Vpc: VpcOutputSettingsDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(BaseValidatorModel):
    Arn: str
    CdiInputSpecification: CdiInputSpecificationTypeDef
    ChannelClass: ChannelClassType
    Destinations: List[OutputDestinationOutputTypeDef]
    EgressEndpoints: List[ChannelEgressEndpointTypeDef]
    EncoderSettings: EncoderSettingsOutputTypeDef
    Id: str
    InputAttachments: List[InputAttachmentOutputTypeDef]
    InputSpecification: InputSpecificationTypeDef
    LogLevel: LogLevelType
    Maintenance: MaintenanceStatusTypeDef
    Name: str
    PipelineDetails: List[PipelineDetailTypeDef]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelStateType
    Tags: Dict[str, str]
    Vpc: VpcOutputSettingsDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestartChannelPipelinesResponseTypeDef(BaseValidatorModel):
    Arn: str
    CdiInputSpecification: CdiInputSpecificationTypeDef
    ChannelClass: ChannelClassType
    Destinations: List[OutputDestinationOutputTypeDef]
    EgressEndpoints: List[ChannelEgressEndpointTypeDef]
    EncoderSettings: EncoderSettingsOutputTypeDef
    Id: str
    InputAttachments: List[InputAttachmentOutputTypeDef]
    InputSpecification: InputSpecificationTypeDef
    LogLevel: LogLevelType
    Maintenance: MaintenanceStatusTypeDef
    MaintenanceStatus: str
    Name: str
    PipelineDetails: List[PipelineDetailTypeDef]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelStateType
    Tags: Dict[str, str]
    Vpc: VpcOutputSettingsDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartChannelResponseTypeDef(BaseValidatorModel):
    Arn: str
    CdiInputSpecification: CdiInputSpecificationTypeDef
    ChannelClass: ChannelClassType
    Destinations: List[OutputDestinationOutputTypeDef]
    EgressEndpoints: List[ChannelEgressEndpointTypeDef]
    EncoderSettings: EncoderSettingsOutputTypeDef
    Id: str
    InputAttachments: List[InputAttachmentOutputTypeDef]
    InputSpecification: InputSpecificationTypeDef
    LogLevel: LogLevelType
    Maintenance: MaintenanceStatusTypeDef
    Name: str
    PipelineDetails: List[PipelineDetailTypeDef]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelStateType
    Tags: Dict[str, str]
    Vpc: VpcOutputSettingsDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopChannelResponseTypeDef(BaseValidatorModel):
    Arn: str
    CdiInputSpecification: CdiInputSpecificationTypeDef
    ChannelClass: ChannelClassType
    Destinations: List[OutputDestinationOutputTypeDef]
    EgressEndpoints: List[ChannelEgressEndpointTypeDef]
    EncoderSettings: EncoderSettingsOutputTypeDef
    Id: str
    InputAttachments: List[InputAttachmentOutputTypeDef]
    InputSpecification: InputSpecificationTypeDef
    LogLevel: LogLevelType
    Maintenance: MaintenanceStatusTypeDef
    Name: str
    PipelineDetails: List[PipelineDetailTypeDef]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelStateType
    Tags: Dict[str, str]
    Vpc: VpcOutputSettingsDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelRequestRequestTypeDef(BaseValidatorModel):
    CdiInputSpecification: Optional[CdiInputSpecificationTypeDef] = None
    ChannelClass: Optional[ChannelClassType] = None
    Destinations: Optional[Sequence[OutputDestinationUnionTypeDef]] = None
    EncoderSettings: Optional[EncoderSettingsTypeDef] = None
    InputAttachments: Optional[Sequence[InputAttachmentUnionTypeDef]] = None
    InputSpecification: Optional[InputSpecificationTypeDef] = None
    LogLevel: Optional[LogLevelType] = None
    Maintenance: Optional[MaintenanceCreateSettingsTypeDef] = None
    Name: Optional[str] = None
    RequestId: Optional[str] = None
    Reserved: Optional[str] = None
    RoleArn: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Vpc: Optional[VpcOutputSettingsTypeDef] = None

class UpdateChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: str
    CdiInputSpecification: Optional[CdiInputSpecificationTypeDef] = None
    Destinations: Optional[Sequence[OutputDestinationUnionTypeDef]] = None
    EncoderSettings: Optional[EncoderSettingsTypeDef] = None
    InputAttachments: Optional[Sequence[InputAttachmentUnionTypeDef]] = None
    InputSpecification: Optional[InputSpecificationTypeDef] = None
    LogLevel: Optional[LogLevelType] = None
    Maintenance: Optional[MaintenanceUpdateSettingsTypeDef] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None

class BatchUpdateScheduleResponseTypeDef(BaseValidatorModel):
    Creates: BatchScheduleActionCreateResultTypeDef
    Deletes: BatchScheduleActionDeleteResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateScheduleRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: str
    Creates: Optional[BatchScheduleActionCreateRequestTypeDef] = None
    Deletes: Optional[BatchScheduleActionDeleteRequestTypeDef] = None

class CreateChannelResponseTypeDef(BaseValidatorModel):
    Channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelClassResponseTypeDef(BaseValidatorModel):
    Channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseValidatorModel):
    Channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

