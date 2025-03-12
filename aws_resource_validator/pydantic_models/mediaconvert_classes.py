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
from aws_resource_validator.pydantic_models.mediaconvert_constants import *

class AacSettingsTypeDef(BaseValidatorModel):
    AudioDescriptionBroadcasterMix: Optional[AacAudioDescriptionBroadcasterMixType] = None
    Bitrate: Optional[int] = None
    CodecProfile: Optional[AacCodecProfileType] = None
    CodingMode: Optional[AacCodingModeType] = None
    RateControlMode: Optional[AacRateControlModeType] = None
    RawFormat: Optional[AacRawFormatType] = None
    SampleRate: Optional[int] = None
    Specification: Optional[AacSpecificationType] = None
    VbrQuality: Optional[AacVbrQualityType] = None


class Ac3SettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[int] = None
    BitstreamMode: Optional[Ac3BitstreamModeType] = None
    CodingMode: Optional[Ac3CodingModeType] = None
    Dialnorm: Optional[int] = None
    DynamicRangeCompressionLine: Optional[Ac3DynamicRangeCompressionLineType] = None
    DynamicRangeCompressionProfile: Optional[Ac3DynamicRangeCompressionProfileType] = None
    DynamicRangeCompressionRf: Optional[Ac3DynamicRangeCompressionRfType] = None
    LfeFilter: Optional[Ac3LfeFilterType] = None
    MetadataControl: Optional[Ac3MetadataControlType] = None
    SampleRate: Optional[int] = None


class AccelerationSettingsTypeDef(BaseValidatorModel):
    Mode: AccelerationModeType


class AdvancedInputFilterSettingsTypeDef(BaseValidatorModel):
    AddTexture: Optional[AdvancedInputFilterAddTextureType] = None
    Sharpening: Optional[AdvancedInputFilterSharpenType] = None


class AiffSettingsTypeDef(BaseValidatorModel):
    BitDepth: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None


class AncillarySourceSettingsTypeDef(BaseValidatorModel):
    Convert608To708: Optional[AncillaryConvert608To708Type] = None
    SourceAncillaryChannelNumber: Optional[int] = None
    TerminateCaptions: Optional[AncillaryTerminateCaptionsType] = None


class AssociateCertificateRequestTypeDef(BaseValidatorModel):
    Arn: str


class AudioChannelTaggingSettingsOutputTypeDef(BaseValidatorModel):
    ChannelTag: Optional[AudioChannelTagType] = None
    ChannelTags: Optional[List[AudioChannelTagType]] = None


class AudioChannelTaggingSettingsTypeDef(BaseValidatorModel):
    ChannelTag: Optional[AudioChannelTagType] = None
    ChannelTags: Optional[Sequence[AudioChannelTagType]] = None


class Eac3AtmosSettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[int] = None
    BitstreamMode: Optional[Literal["COMPLETE_MAIN"]] = None
    CodingMode: Optional[Eac3AtmosCodingModeType] = None
    DialogueIntelligence: Optional[Eac3AtmosDialogueIntelligenceType] = None
    DownmixControl: Optional[Eac3AtmosDownmixControlType] = None
    DynamicRangeCompressionLine: Optional[Eac3AtmosDynamicRangeCompressionLineType] = None
    DynamicRangeCompressionRf: Optional[Eac3AtmosDynamicRangeCompressionRfType] = None
    DynamicRangeControl: Optional[Eac3AtmosDynamicRangeControlType] = None
    LoRoCenterMixLevel: Optional[float] = None
    LoRoSurroundMixLevel: Optional[float] = None
    LtRtCenterMixLevel: Optional[float] = None
    LtRtSurroundMixLevel: Optional[float] = None
    MeteringMode: Optional[Eac3AtmosMeteringModeType] = None
    SampleRate: Optional[int] = None
    SpeechThreshold: Optional[int] = None
    StereoDownmix: Optional[Eac3AtmosStereoDownmixType] = None
    SurroundExMode: Optional[Eac3AtmosSurroundExModeType] = None


class Eac3SettingsTypeDef(BaseValidatorModel):
    AttenuationControl: Optional[Eac3AttenuationControlType] = None
    Bitrate: Optional[int] = None
    BitstreamMode: Optional[Eac3BitstreamModeType] = None
    CodingMode: Optional[Eac3CodingModeType] = None
    DcFilter: Optional[Eac3DcFilterType] = None
    Dialnorm: Optional[int] = None
    DynamicRangeCompressionLine: Optional[Eac3DynamicRangeCompressionLineType] = None
    DynamicRangeCompressionRf: Optional[Eac3DynamicRangeCompressionRfType] = None
    LfeControl: Optional[Eac3LfeControlType] = None
    LfeFilter: Optional[Eac3LfeFilterType] = None
    LoRoCenterMixLevel: Optional[float] = None
    LoRoSurroundMixLevel: Optional[float] = None
    LtRtCenterMixLevel: Optional[float] = None
    LtRtSurroundMixLevel: Optional[float] = None
    MetadataControl: Optional[Eac3MetadataControlType] = None
    PassthroughControl: Optional[Eac3PassthroughControlType] = None
    PhaseControl: Optional[Eac3PhaseControlType] = None
    SampleRate: Optional[int] = None
    StereoDownmix: Optional[Eac3StereoDownmixType] = None
    SurroundExMode: Optional[Eac3SurroundExModeType] = None
    SurroundMode: Optional[Eac3SurroundModeType] = None


class FlacSettingsTypeDef(BaseValidatorModel):
    BitDepth: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None


class Mp2SettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None


class Mp3SettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[int] = None
    Channels: Optional[int] = None
    RateControlMode: Optional[Mp3RateControlModeType] = None
    SampleRate: Optional[int] = None
    VbrQuality: Optional[int] = None


class OpusSettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None


class VorbisSettingsTypeDef(BaseValidatorModel):
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None
    VbrQuality: Optional[int] = None


class WavSettingsTypeDef(BaseValidatorModel):
    BitDepth: Optional[int] = None
    Channels: Optional[int] = None
    Format: Optional[WavFormatType] = None
    SampleRate: Optional[int] = None


class AudioNormalizationSettingsTypeDef(BaseValidatorModel):
    Algorithm: Optional[AudioNormalizationAlgorithmType] = None
    AlgorithmControl: Optional[AudioNormalizationAlgorithmControlType] = None
    CorrectionGateLevel: Optional[int] = None
    LoudnessLogging: Optional[AudioNormalizationLoudnessLoggingType] = None
    PeakCalculation: Optional[AudioNormalizationPeakCalculationType] = None
    TargetLkfs: Optional[float] = None
    TruePeakLimiterThreshold: Optional[float] = None


class FrameRateTypeDef(BaseValidatorModel):
    Denominator: Optional[int] = None
    Numerator: Optional[int] = None


class AudioSelectorGroupOutputTypeDef(BaseValidatorModel):
    AudioSelectorNames: Optional[List[str]] = None


class AudioSelectorGroupTypeDef(BaseValidatorModel):
    AudioSelectorNames: Optional[Sequence[str]] = None


class HlsRenditionGroupSettingsTypeDef(BaseValidatorModel):
    RenditionGroupId: Optional[str] = None
    RenditionLanguageCode: Optional[LanguageCodeType] = None
    RenditionName: Optional[str] = None


class ForceIncludeRenditionSizeTypeDef(BaseValidatorModel):
    Height: Optional[int] = None
    Width: Optional[int] = None


class MinBottomRenditionSizeTypeDef(BaseValidatorModel):
    Height: Optional[int] = None
    Width: Optional[int] = None


class MinTopRenditionSizeTypeDef(BaseValidatorModel):
    Height: Optional[int] = None
    Width: Optional[int] = None


class Av1QvbrSettingsTypeDef(BaseValidatorModel):
    QvbrQualityLevel: Optional[int] = None
    QvbrQualityLevelFineTune: Optional[float] = None


class AvailBlankingTypeDef(BaseValidatorModel):
    AvailBlankingImage: Optional[str] = None


class AvcIntraUhdSettingsTypeDef(BaseValidatorModel):
    QualityTuningLevel: Optional[AvcIntraUhdQualityTuningLevelType] = None


class BandwidthReductionFilterTypeDef(BaseValidatorModel):
    Sharpening: Optional[BandwidthReductionFilterSharpeningType] = None
    Strength: Optional[BandwidthReductionFilterStrengthType] = None


class BurninDestinationSettingsTypeDef(BaseValidatorModel):
    Alignment: Optional[BurninSubtitleAlignmentType] = None
    ApplyFontColor: Optional[BurninSubtitleApplyFontColorType] = None
    BackgroundColor: Optional[BurninSubtitleBackgroundColorType] = None
    BackgroundOpacity: Optional[int] = None
    FallbackFont: Optional[BurninSubtitleFallbackFontType] = None
    FontColor: Optional[BurninSubtitleFontColorType] = None
    FontFileBold: Optional[str] = None
    FontFileBoldItalic: Optional[str] = None
    FontFileItalic: Optional[str] = None
    FontFileRegular: Optional[str] = None
    FontOpacity: Optional[int] = None
    FontResolution: Optional[int] = None
    FontScript: Optional[FontScriptType] = None
    FontSize: Optional[int] = None
    HexFontColor: Optional[str] = None
    OutlineColor: Optional[BurninSubtitleOutlineColorType] = None
    OutlineSize: Optional[int] = None
    RemoveRubyReserveAttributes: Optional[RemoveRubyReserveAttributesType] = None
    ShadowColor: Optional[BurninSubtitleShadowColorType] = None
    ShadowOpacity: Optional[int] = None
    ShadowXOffset: Optional[int] = None
    ShadowYOffset: Optional[int] = None
    StylePassthrough: Optional[BurnInSubtitleStylePassthroughType] = None
    TeletextSpacing: Optional[BurninSubtitleTeletextSpacingType] = None
    XPosition: Optional[int] = None
    YPosition: Optional[int] = None


class CancelJobRequestTypeDef(BaseValidatorModel):
    Id: str


class DvbSubDestinationSettingsTypeDef(BaseValidatorModel):
    Alignment: Optional[DvbSubtitleAlignmentType] = None
    ApplyFontColor: Optional[DvbSubtitleApplyFontColorType] = None
    BackgroundColor: Optional[DvbSubtitleBackgroundColorType] = None
    BackgroundOpacity: Optional[int] = None
    DdsHandling: Optional[DvbddsHandlingType] = None
    DdsXCoordinate: Optional[int] = None
    DdsYCoordinate: Optional[int] = None
    FallbackFont: Optional[DvbSubSubtitleFallbackFontType] = None
    FontColor: Optional[DvbSubtitleFontColorType] = None
    FontFileBold: Optional[str] = None
    FontFileBoldItalic: Optional[str] = None
    FontFileItalic: Optional[str] = None
    FontFileRegular: Optional[str] = None
    FontOpacity: Optional[int] = None
    FontResolution: Optional[int] = None
    FontScript: Optional[FontScriptType] = None
    FontSize: Optional[int] = None
    Height: Optional[int] = None
    HexFontColor: Optional[str] = None
    OutlineColor: Optional[DvbSubtitleOutlineColorType] = None
    OutlineSize: Optional[int] = None
    ShadowColor: Optional[DvbSubtitleShadowColorType] = None
    ShadowOpacity: Optional[int] = None
    ShadowXOffset: Optional[int] = None
    ShadowYOffset: Optional[int] = None
    StylePassthrough: Optional[DvbSubtitleStylePassthroughType] = None
    SubtitlingType: Optional[DvbSubtitlingTypeType] = None
    TeletextSpacing: Optional[DvbSubtitleTeletextSpacingType] = None
    Width: Optional[int] = None
    XPosition: Optional[int] = None
    YPosition: Optional[int] = None


class EmbeddedDestinationSettingsTypeDef(BaseValidatorModel):
    Destination608ChannelNumber: Optional[int] = None
    Destination708ServiceNumber: Optional[int] = None


class ImscDestinationSettingsTypeDef(BaseValidatorModel):
    Accessibility: Optional[ImscAccessibilitySubsType] = None
    StylePassthrough: Optional[ImscStylePassthroughType] = None


class SccDestinationSettingsTypeDef(BaseValidatorModel):
    Framerate: Optional[SccDestinationFramerateType] = None


class SrtDestinationSettingsTypeDef(BaseValidatorModel):
    StylePassthrough: Optional[SrtStylePassthroughType] = None


class TeletextDestinationSettingsOutputTypeDef(BaseValidatorModel):
    PageNumber: Optional[str] = None
    PageTypes: Optional[List[TeletextPageTypeType]] = None


class TtmlDestinationSettingsTypeDef(BaseValidatorModel):
    StylePassthrough: Optional[TtmlStylePassthroughType] = None


class WebvttDestinationSettingsTypeDef(BaseValidatorModel):
    Accessibility: Optional[WebvttAccessibilitySubsType] = None
    StylePassthrough: Optional[WebvttStylePassthroughType] = None


class TeletextDestinationSettingsTypeDef(BaseValidatorModel):
    PageNumber: Optional[str] = None
    PageTypes: Optional[Sequence[TeletextPageTypeType]] = None


class CaptionSourceFramerateTypeDef(BaseValidatorModel):
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None


class DvbSubSourceSettingsTypeDef(BaseValidatorModel):
    Pid: Optional[int] = None


class EmbeddedSourceSettingsTypeDef(BaseValidatorModel):
    Convert608To708: Optional[EmbeddedConvert608To708Type] = None
    Source608ChannelNumber: Optional[int] = None
    Source608TrackNumber: Optional[int] = None
    TerminateCaptions: Optional[EmbeddedTerminateCaptionsType] = None


class TeletextSourceSettingsTypeDef(BaseValidatorModel):
    PageNumber: Optional[str] = None


class TrackSourceSettingsTypeDef(BaseValidatorModel):
    TrackNumber: Optional[int] = None


class WebvttHlsSourceSettingsTypeDef(BaseValidatorModel):
    RenditionGroupId: Optional[str] = None
    RenditionLanguageCode: Optional[LanguageCodeType] = None
    RenditionName: Optional[str] = None


class OutputChannelMappingOutputTypeDef(BaseValidatorModel):
    InputChannels: Optional[List[int]] = None
    InputChannelsFineTune: Optional[List[float]] = None


class OutputChannelMappingTypeDef(BaseValidatorModel):
    InputChannels: Optional[Sequence[int]] = None
    InputChannelsFineTune: Optional[Sequence[float]] = None


class ClipLimitsTypeDef(BaseValidatorModel):
    MaximumRGBTolerance: Optional[int] = None
    MaximumYUV: Optional[int] = None
    MinimumRGBTolerance: Optional[int] = None
    MinimumYUV: Optional[int] = None


class CmafAdditionalManifestOutputTypeDef(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class CmafAdditionalManifestTypeDef(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[Sequence[str]] = None


class StaticKeyProviderTypeDef(BaseValidatorModel):
    KeyFormat: Optional[str] = None
    KeyFormatVersions: Optional[str] = None
    StaticKeyValue: Optional[str] = None
    Url: Optional[str] = None


class CmafImageBasedTrickPlaySettingsTypeDef(BaseValidatorModel):
    IntervalCadence: Optional[CmafIntervalCadenceType] = None
    ThumbnailHeight: Optional[int] = None
    ThumbnailInterval: Optional[float] = None
    ThumbnailWidth: Optional[int] = None
    TileHeight: Optional[int] = None
    TileWidth: Optional[int] = None


class CmfcSettingsTypeDef(BaseValidatorModel):
    AudioDuration: Optional[CmfcAudioDurationType] = None
    AudioGroupId: Optional[str] = None
    AudioRenditionSets: Optional[str] = None
    AudioTrackType: Optional[CmfcAudioTrackTypeType] = None
    DescriptiveVideoServiceFlag: Optional[CmfcDescriptiveVideoServiceFlagType] = None
    IFrameOnlyManifest: Optional[CmfcIFrameOnlyManifestType] = None
    KlvMetadata: Optional[CmfcKlvMetadataType] = None
    ManifestMetadataSignaling: Optional[CmfcManifestMetadataSignalingType] = None
    Scte35Esam: Optional[CmfcScte35EsamType] = None
    Scte35Source: Optional[CmfcScte35SourceType] = None
    TimedMetadata: Optional[CmfcTimedMetadataType] = None
    TimedMetadataBoxVersion: Optional[CmfcTimedMetadataBoxVersionType] = None
    TimedMetadataSchemeIdUri: Optional[str] = None
    TimedMetadataValue: Optional[str] = None


class ColorConversion3DLUTSettingTypeDef(BaseValidatorModel):
    FileInput: Optional[str] = None
    InputColorSpace: Optional[ColorSpaceType] = None
    InputMasteringLuminance: Optional[int] = None
    OutputColorSpace: Optional[ColorSpaceType] = None
    OutputMasteringLuminance: Optional[int] = None


class Hdr10MetadataTypeDef(BaseValidatorModel):
    BluePrimaryX: Optional[int] = None
    BluePrimaryY: Optional[int] = None
    GreenPrimaryX: Optional[int] = None
    GreenPrimaryY: Optional[int] = None
    MaxContentLightLevel: Optional[int] = None
    MaxFrameAverageLightLevel: Optional[int] = None
    MaxLuminance: Optional[int] = None
    MinLuminance: Optional[int] = None
    RedPrimaryX: Optional[int] = None
    RedPrimaryY: Optional[int] = None
    WhitePointX: Optional[int] = None
    WhitePointY: Optional[int] = None


class F4vSettingsTypeDef(BaseValidatorModel):
    MoovPlacement: Optional[F4vMoovPlacementType] = None


class M3u8SettingsOutputTypeDef(BaseValidatorModel):
    AudioDuration: Optional[M3u8AudioDurationType] = None
    AudioFramesPerPes: Optional[int] = None
    AudioPids: Optional[List[int]] = None
    DataPTSControl: Optional[M3u8DataPtsControlType] = None
    MaxPcrInterval: Optional[int] = None
    NielsenId3: Optional[M3u8NielsenId3Type] = None
    PatInterval: Optional[int] = None
    PcrControl: Optional[M3u8PcrControlType] = None
    PcrPid: Optional[int] = None
    PmtInterval: Optional[int] = None
    PmtPid: Optional[int] = None
    PrivateMetadataPid: Optional[int] = None
    ProgramNumber: Optional[int] = None
    PtsOffset: Optional[int] = None
    PtsOffsetMode: Optional[TsPtsOffsetType] = None
    Scte35Pid: Optional[int] = None
    Scte35Source: Optional[M3u8Scte35SourceType] = None
    TimedMetadata: Optional[TimedMetadataType] = None
    TimedMetadataPid: Optional[int] = None
    TransportStreamId: Optional[int] = None
    VideoPid: Optional[int] = None


class MovSettingsTypeDef(BaseValidatorModel):
    ClapAtom: Optional[MovClapAtomType] = None
    CslgAtom: Optional[MovCslgAtomType] = None
    Mpeg2FourCCControl: Optional[MovMpeg2FourCCControlType] = None
    PaddingControl: Optional[MovPaddingControlType] = None
    Reference: Optional[MovReferenceType] = None


class Mp4SettingsTypeDef(BaseValidatorModel):
    AudioDuration: Optional[CmfcAudioDurationType] = None
    CslgAtom: Optional[Mp4CslgAtomType] = None
    CttsVersion: Optional[int] = None
    FreeSpaceBox: Optional[Mp4FreeSpaceBoxType] = None
    MoovPlacement: Optional[Mp4MoovPlacementType] = None
    Mp4MajorBrand: Optional[str] = None


class MpdSettingsTypeDef(BaseValidatorModel):
    AccessibilityCaptionHints: Optional[MpdAccessibilityCaptionHintsType] = None
    AudioDuration: Optional[MpdAudioDurationType] = None
    CaptionContainerType: Optional[MpdCaptionContainerTypeType] = None
    KlvMetadata: Optional[MpdKlvMetadataType] = None
    ManifestMetadataSignaling: Optional[MpdManifestMetadataSignalingType] = None
    Scte35Esam: Optional[MpdScte35EsamType] = None
    Scte35Source: Optional[MpdScte35SourceType] = None
    TimedMetadata: Optional[MpdTimedMetadataType] = None
    TimedMetadataBoxVersion: Optional[MpdTimedMetadataBoxVersionType] = None
    TimedMetadataSchemeIdUri: Optional[str] = None
    TimedMetadataValue: Optional[str] = None


class M3u8SettingsTypeDef(BaseValidatorModel):
    AudioDuration: Optional[M3u8AudioDurationType] = None
    AudioFramesPerPes: Optional[int] = None
    AudioPids: Optional[Sequence[int]] = None
    DataPTSControl: Optional[M3u8DataPtsControlType] = None
    MaxPcrInterval: Optional[int] = None
    NielsenId3: Optional[M3u8NielsenId3Type] = None
    PatInterval: Optional[int] = None
    PcrControl: Optional[M3u8PcrControlType] = None
    PcrPid: Optional[int] = None
    PmtInterval: Optional[int] = None
    PmtPid: Optional[int] = None
    PrivateMetadataPid: Optional[int] = None
    ProgramNumber: Optional[int] = None
    PtsOffset: Optional[int] = None
    PtsOffsetMode: Optional[TsPtsOffsetType] = None
    Scte35Pid: Optional[int] = None
    Scte35Source: Optional[M3u8Scte35SourceType] = None
    TimedMetadata: Optional[TimedMetadataType] = None
    TimedMetadataPid: Optional[int] = None
    TransportStreamId: Optional[int] = None
    VideoPid: Optional[int] = None


class HopDestinationTypeDef(BaseValidatorModel):
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    WaitMinutes: Optional[int] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ReservationPlanSettingsTypeDef(BaseValidatorModel):
    Commitment: Literal["ONE_YEAR"]
    RenewalType: RenewalTypeType
    ReservedSlots: int


class DashAdditionalManifestOutputTypeDef(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class DashAdditionalManifestTypeDef(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[Sequence[str]] = None


class DashIsoImageBasedTrickPlaySettingsTypeDef(BaseValidatorModel):
    IntervalCadence: Optional[DashIsoIntervalCadenceType] = None
    ThumbnailHeight: Optional[int] = None
    ThumbnailInterval: Optional[float] = None
    ThumbnailWidth: Optional[int] = None
    TileHeight: Optional[int] = None
    TileWidth: Optional[int] = None


class DataPropertiesTypeDef(BaseValidatorModel):
    LanguageCode: Optional[str] = None


class DeinterlacerTypeDef(BaseValidatorModel):
    Algorithm: Optional[DeinterlaceAlgorithmType] = None
    Control: Optional[DeinterlacerControlType] = None
    Mode: Optional[DeinterlacerModeType] = None


class DeleteJobTemplateRequestTypeDef(BaseValidatorModel):
    Name: str


class DeletePresetRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteQueueRequestTypeDef(BaseValidatorModel):
    Name: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeEndpointsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    Mode: Optional[DescribeEndpointsModeType] = None
    NextToken: Optional[str] = None


class EndpointTypeDef(BaseValidatorModel):
    Url: Optional[str] = None


class DisassociateCertificateRequestTypeDef(BaseValidatorModel):
    Arn: str


class DolbyVisionLevel6MetadataTypeDef(BaseValidatorModel):
    MaxCll: Optional[int] = None
    MaxFall: Optional[int] = None


class DvbNitSettingsTypeDef(BaseValidatorModel):
    NetworkId: Optional[int] = None
    NetworkName: Optional[str] = None
    NitInterval: Optional[int] = None


class DvbTdtSettingsTypeDef(BaseValidatorModel):
    TdtInterval: Optional[int] = None


class DynamicAudioSelectorTypeDef(BaseValidatorModel):
    AudioDurationCorrection: Optional[AudioDurationCorrectionType] = None
    ExternalAudioFileInput: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Offset: Optional[int] = None
    SelectorType: Optional[DynamicAudioSelectorTypeType] = None


class EncryptionContractConfigurationTypeDef(BaseValidatorModel):
    SpekeAudioPreset: Optional[PresetSpeke20AudioType] = None
    SpekeVideoPreset: Optional[PresetSpeke20VideoType] = None


class EsamManifestConfirmConditionNotificationTypeDef(BaseValidatorModel):
    MccXml: Optional[str] = None


class EsamSignalProcessingNotificationTypeDef(BaseValidatorModel):
    SccXml: Optional[str] = None


class ExtendedDataServicesTypeDef(BaseValidatorModel):
    CopyProtectionAction: Optional[CopyProtectionActionType] = None
    VchipAction: Optional[VchipActionType] = None


class FrameCaptureSettingsTypeDef(BaseValidatorModel):
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    MaxCaptures: Optional[int] = None
    Quality: Optional[int] = None


class GetJobRequestTypeDef(BaseValidatorModel):
    Id: str


class GetJobTemplateRequestTypeDef(BaseValidatorModel):
    Name: str


class PolicyTypeDef(BaseValidatorModel):
    HttpInputs: Optional[InputPolicyType] = None
    HttpsInputs: Optional[InputPolicyType] = None
    S3Inputs: Optional[InputPolicyType] = None


class GetPresetRequestTypeDef(BaseValidatorModel):
    Name: str


class GetQueueRequestTypeDef(BaseValidatorModel):
    Name: str


class GifSettingsTypeDef(BaseValidatorModel):
    FramerateControl: Optional[GifFramerateControlType] = None
    FramerateConversionAlgorithm: Optional[GifFramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None


class H264QvbrSettingsTypeDef(BaseValidatorModel):
    MaxAverageBitrate: Optional[int] = None
    QvbrQualityLevel: Optional[int] = None
    QvbrQualityLevelFineTune: Optional[float] = None


class H265QvbrSettingsTypeDef(BaseValidatorModel):
    MaxAverageBitrate: Optional[int] = None
    QvbrQualityLevel: Optional[int] = None
    QvbrQualityLevelFineTune: Optional[float] = None


class Hdr10PlusTypeDef(BaseValidatorModel):
    MasteringMonitorNits: Optional[int] = None
    TargetMonitorNits: Optional[int] = None


class HlsAdditionalManifestOutputTypeDef(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class HlsAdditionalManifestTypeDef(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[Sequence[str]] = None


class HlsCaptionLanguageMappingTypeDef(BaseValidatorModel):
    CaptionChannel: Optional[int] = None
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None


class HlsImageBasedTrickPlaySettingsTypeDef(BaseValidatorModel):
    IntervalCadence: Optional[HlsIntervalCadenceType] = None
    ThumbnailHeight: Optional[int] = None
    ThumbnailInterval: Optional[float] = None
    ThumbnailWidth: Optional[int] = None
    TileHeight: Optional[int] = None
    TileWidth: Optional[int] = None


class HlsSettingsTypeDef(BaseValidatorModel):
    AudioGroupId: Optional[str] = None
    AudioOnlyContainer: Optional[HlsAudioOnlyContainerType] = None
    AudioRenditionSets: Optional[str] = None
    AudioTrackType: Optional[HlsAudioTrackTypeType] = None
    DescriptiveVideoServiceFlag: Optional[HlsDescriptiveVideoServiceFlagType] = None
    IFrameOnlyManifest: Optional[HlsIFrameOnlyManifestType] = None
    SegmentModifier: Optional[str] = None


class Id3InsertionTypeDef(BaseValidatorModel):
    Id3: Optional[str] = None
    Timecode: Optional[str] = None


class InsertableImageTypeDef(BaseValidatorModel):
    Duration: Optional[int] = None
    FadeIn: Optional[int] = None
    FadeOut: Optional[int] = None
    Height: Optional[int] = None
    ImageInserterInput: Optional[str] = None
    ImageX: Optional[int] = None
    ImageY: Optional[int] = None
    Layer: Optional[int] = None
    Opacity: Optional[int] = None
    StartTime: Optional[str] = None
    Width: Optional[int] = None


class InputClippingTypeDef(BaseValidatorModel):
    EndTimecode: Optional[str] = None
    StartTimecode: Optional[str] = None


class InputDecryptionSettingsTypeDef(BaseValidatorModel):
    DecryptionMode: Optional[DecryptionModeType] = None
    EncryptedDecryptionKey: Optional[str] = None
    InitializationVector: Optional[str] = None
    KmsKeyRegion: Optional[str] = None


class InputVideoGeneratorTypeDef(BaseValidatorModel):
    Channels: Optional[int] = None
    Duration: Optional[int] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    SampleRate: Optional[int] = None


class RectangleTypeDef(BaseValidatorModel):
    Height: Optional[int] = None
    Width: Optional[int] = None
    X: Optional[int] = None
    Y: Optional[int] = None


class JobEngineVersionTypeDef(BaseValidatorModel):
    ExpirationDate: Optional[datetime] = None
    Version: Optional[str] = None


class KantarWatermarkSettingsTypeDef(BaseValidatorModel):
    ChannelName: Optional[str] = None
    ContentReference: Optional[str] = None
    CredentialsSecretName: Optional[str] = None
    FileOffset: Optional[float] = None
    KantarLicenseId: Optional[int] = None
    KantarServerUrl: Optional[str] = None
    LogDestination: Optional[str] = None
    Metadata3: Optional[str] = None
    Metadata4: Optional[str] = None
    Metadata5: Optional[str] = None
    Metadata6: Optional[str] = None
    Metadata7: Optional[str] = None
    Metadata8: Optional[str] = None


class NielsenConfigurationTypeDef(BaseValidatorModel):
    BreakoutCode: Optional[int] = None
    DistributorId: Optional[str] = None


class NielsenNonLinearWatermarkSettingsTypeDef(BaseValidatorModel):
    ActiveWatermarkProcess: Optional[NielsenActiveWatermarkProcessTypeType] = None
    AdiFilename: Optional[str] = None
    AssetId: Optional[str] = None
    AssetName: Optional[str] = None
    CbetSourceId: Optional[str] = None
    EpisodeId: Optional[str] = None
    MetadataDestination: Optional[str] = None
    SourceId: Optional[int] = None
    SourceWatermarkStatus: Optional[NielsenSourceWatermarkStatusTypeType] = None
    TicServerUrl: Optional[str] = None
    UniqueTicPerAudioTrack: Optional[NielsenUniqueTicPerAudioTrackTypeType] = None


class TimecodeConfigTypeDef(BaseValidatorModel):
    Anchor: Optional[str] = None
    Source: Optional[TimecodeSourceType] = None
    Start: Optional[str] = None
    TimestampOffset: Optional[str] = None


class QueueTransitionTypeDef(BaseValidatorModel):
    DestinationQueue: Optional[str] = None
    SourceQueue: Optional[str] = None
    Timestamp: Optional[datetime] = None


class TimingTypeDef(BaseValidatorModel):
    FinishTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    SubmitTime: Optional[datetime] = None


class WarningGroupTypeDef(BaseValidatorModel):
    Code: int
    Count: int


class ListJobTemplatesRequestTypeDef(BaseValidatorModel):
    Category: Optional[str] = None
    ListBy: Optional[JobTemplateListByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None


class ListPresetsRequestTypeDef(BaseValidatorModel):
    Category: Optional[str] = None
    ListBy: Optional[PresetListByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None


class ListQueuesRequestTypeDef(BaseValidatorModel):
    ListBy: Optional[QueueListByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    Arn: str


class ResourceTagsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ListVersionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class M2tsScte35EsamTypeDef(BaseValidatorModel):
    Scte35EsamPid: Optional[int] = None


class MetadataTypeDef(BaseValidatorModel):
    ETag: Optional[str] = None
    FileSize: Optional[int] = None
    LastModified: Optional[datetime] = None
    MimeType: Optional[str] = None


class MotionImageInsertionFramerateTypeDef(BaseValidatorModel):
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None


class MotionImageInsertionOffsetTypeDef(BaseValidatorModel):
    ImageX: Optional[int] = None
    ImageY: Optional[int] = None


class Mpeg2SettingsTypeDef(BaseValidatorModel):
    AdaptiveQuantization: Optional[Mpeg2AdaptiveQuantizationType] = None
    Bitrate: Optional[int] = None
    CodecLevel: Optional[Mpeg2CodecLevelType] = None
    CodecProfile: Optional[Mpeg2CodecProfileType] = None
    DynamicSubGop: Optional[Mpeg2DynamicSubGopType] = None
    FramerateControl: Optional[Mpeg2FramerateControlType] = None
    FramerateConversionAlgorithm: Optional[Mpeg2FramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    GopClosedCadence: Optional[int] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[Mpeg2GopSizeUnitsType] = None
    HrdBufferFinalFillPercentage: Optional[int] = None
    HrdBufferInitialFillPercentage: Optional[int] = None
    HrdBufferSize: Optional[int] = None
    InterlaceMode: Optional[Mpeg2InterlaceModeType] = None
    IntraDcPrecision: Optional[Mpeg2IntraDcPrecisionType] = None
    MaxBitrate: Optional[int] = None
    MinIInterval: Optional[int] = None
    NumberBFramesBetweenReferenceFrames: Optional[int] = None
    ParControl: Optional[Mpeg2ParControlType] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    QualityTuningLevel: Optional[Mpeg2QualityTuningLevelType] = None
    RateControlMode: Optional[Mpeg2RateControlModeType] = None
    ScanTypeConversionMode: Optional[Mpeg2ScanTypeConversionModeType] = None
    SceneChangeDetect: Optional[Mpeg2SceneChangeDetectType] = None
    SlowPal: Optional[Mpeg2SlowPalType] = None
    Softness: Optional[int] = None
    SpatialAdaptiveQuantization: Optional[Mpeg2SpatialAdaptiveQuantizationType] = None
    Syntax: Optional[Mpeg2SyntaxType] = None
    Telecine: Optional[Mpeg2TelecineType] = None
    TemporalAdaptiveQuantization: Optional[Mpeg2TemporalAdaptiveQuantizationType] = None


class MsSmoothAdditionalManifestOutputTypeDef(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class MsSmoothAdditionalManifestTypeDef(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[Sequence[str]] = None


class MxfXavcProfileSettingsTypeDef(BaseValidatorModel):
    DurationMode: Optional[MxfXavcDurationModeType] = None
    MaxAncDataSize: Optional[int] = None


class NexGuardFileMarkerSettingsTypeDef(BaseValidatorModel):
    License: Optional[str] = None
    Payload: Optional[int] = None
    Preset: Optional[str] = None
    Strength: Optional[WatermarkingStrengthType] = None


class NoiseReducerFilterSettingsTypeDef(BaseValidatorModel):
    Strength: Optional[int] = None


class NoiseReducerSpatialFilterSettingsTypeDef(BaseValidatorModel):
    PostFilterSharpenStrength: Optional[int] = None
    Speed: Optional[int] = None
    Strength: Optional[int] = None


class NoiseReducerTemporalFilterSettingsTypeDef(BaseValidatorModel):
    AggressiveMode: Optional[int] = None
    PostTemporalSharpening: Optional[NoiseFilterPostTemporalSharpeningType] = None
    PostTemporalSharpeningStrength: Optional[NoiseFilterPostTemporalSharpeningStrengthType] = None
    Speed: Optional[int] = None
    Strength: Optional[int] = None


class VideoDetailTypeDef(BaseValidatorModel):
    HeightInPx: Optional[int] = None
    WidthInPx: Optional[int] = None


class ProbeInputFileTypeDef(BaseValidatorModel):
    FileUrl: Optional[str] = None


class TrackMappingTypeDef(BaseValidatorModel):
    AudioTrackIndexes: Optional[List[int]] = None
    DataTrackIndexes: Optional[List[int]] = None
    VideoTrackIndexes: Optional[List[int]] = None


class ProresSettingsTypeDef(BaseValidatorModel):
    ChromaSampling: Optional[ProresChromaSamplingType] = None
    CodecProfile: Optional[ProresCodecProfileType] = None
    FramerateControl: Optional[ProresFramerateControlType] = None
    FramerateConversionAlgorithm: Optional[ProresFramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    InterlaceMode: Optional[ProresInterlaceModeType] = None
    ParControl: Optional[ProresParControlType] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    ScanTypeConversionMode: Optional[ProresScanTypeConversionModeType] = None
    SlowPal: Optional[ProresSlowPalType] = None
    Telecine: Optional[ProresTelecineType] = None


class ReservationPlanTypeDef(BaseValidatorModel):
    Commitment: Optional[Literal["ONE_YEAR"]] = None
    ExpiresAt: Optional[datetime] = None
    PurchasedAt: Optional[datetime] = None
    RenewalType: Optional[RenewalTypeType] = None
    ReservedSlots: Optional[int] = None
    Status: Optional[ReservationPlanStatusType] = None


class ServiceOverrideTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Name: Optional[str] = None
    OverrideValue: Optional[str] = None
    Value: Optional[str] = None


class S3DestinationAccessControlTypeDef(BaseValidatorModel):
    CannedAcl: Optional[S3ObjectCannedAclType] = None


class S3EncryptionSettingsTypeDef(BaseValidatorModel):
    EncryptionType: Optional[S3ServerSideEncryptionTypeType] = None
    KmsEncryptionContext: Optional[str] = None
    KmsKeyArn: Optional[str] = None


class SearchJobsRequestTypeDef(BaseValidatorModel):
    InputFile: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    Arn: str
    Tags: Mapping[str, str]


class TimecodeBurninTypeDef(BaseValidatorModel):
    FontSize: Optional[int] = None
    Position: Optional[TimecodeBurninPositionType] = None
    Prefix: Optional[str] = None


class UncompressedSettingsTypeDef(BaseValidatorModel):
    Fourcc: Optional[UncompressedFourccType] = None
    FramerateControl: Optional[UncompressedFramerateControlType] = None
    FramerateConversionAlgorithm: Optional[UncompressedFramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    InterlaceMode: Optional[UncompressedInterlaceModeType] = None
    ScanTypeConversionMode: Optional[UncompressedScanTypeConversionModeType] = None
    SlowPal: Optional[UncompressedSlowPalType] = None
    Telecine: Optional[UncompressedTelecineType] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    Arn: str
    TagKeys: Optional[Sequence[str]] = None


class Vc3SettingsTypeDef(BaseValidatorModel):
    FramerateControl: Optional[Vc3FramerateControlType] = None
    FramerateConversionAlgorithm: Optional[Vc3FramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    InterlaceMode: Optional[Vc3InterlaceModeType] = None
    ScanTypeConversionMode: Optional[Vc3ScanTypeConversionModeType] = None
    SlowPal: Optional[Vc3SlowPalType] = None
    Telecine: Optional[Vc3TelecineType] = None
    Vc3Class: Optional[Vc3ClassType] = None


class Vp8SettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[int] = None
    FramerateControl: Optional[Vp8FramerateControlType] = None
    FramerateConversionAlgorithm: Optional[Vp8FramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    GopSize: Optional[float] = None
    HrdBufferSize: Optional[int] = None
    MaxBitrate: Optional[int] = None
    ParControl: Optional[Vp8ParControlType] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    QualityTuningLevel: Optional[Vp8QualityTuningLevelType] = None
    RateControlMode: Optional[Literal["VBR"]] = None


class Vp9SettingsTypeDef(BaseValidatorModel):
    Bitrate: Optional[int] = None
    FramerateControl: Optional[Vp9FramerateControlType] = None
    FramerateConversionAlgorithm: Optional[Vp9FramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    GopSize: Optional[float] = None
    HrdBufferSize: Optional[int] = None
    MaxBitrate: Optional[int] = None
    ParControl: Optional[Vp9ParControlType] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    QualityTuningLevel: Optional[Vp9QualityTuningLevelType] = None
    RateControlMode: Optional[Literal["VBR"]] = None


class VideoOverlayInputClippingTypeDef(BaseValidatorModel):
    EndTimecode: Optional[str] = None
    StartTimecode: Optional[str] = None


class VideoOverlayPositionTypeDef(BaseValidatorModel):
    Height: Optional[int] = None
    Unit: Optional[VideoOverlayUnitType] = None
    Width: Optional[int] = None
    XPosition: Optional[int] = None
    YPosition: Optional[int] = None


class Xavc4kIntraCbgProfileSettingsTypeDef(BaseValidatorModel):
    XavcClass: Optional[Xavc4kIntraCbgProfileClassType] = None


class Xavc4kIntraVbrProfileSettingsTypeDef(BaseValidatorModel):
    XavcClass: Optional[Xavc4kIntraVbrProfileClassType] = None


class Xavc4kProfileSettingsTypeDef(BaseValidatorModel):
    BitrateClass: Optional[Xavc4kProfileBitrateClassType] = None
    CodecProfile: Optional[Xavc4kProfileCodecProfileType] = None
    FlickerAdaptiveQuantization: Optional[XavcFlickerAdaptiveQuantizationType] = None
    GopBReference: Optional[XavcGopBReferenceType] = None
    GopClosedCadence: Optional[int] = None
    HrdBufferSize: Optional[int] = None
    QualityTuningLevel: Optional[Xavc4kProfileQualityTuningLevelType] = None
    Slices: Optional[int] = None


class XavcHdIntraCbgProfileSettingsTypeDef(BaseValidatorModel):
    XavcClass: Optional[XavcHdIntraCbgProfileClassType] = None


class XavcHdProfileSettingsTypeDef(BaseValidatorModel):
    BitrateClass: Optional[XavcHdProfileBitrateClassType] = None
    FlickerAdaptiveQuantization: Optional[XavcFlickerAdaptiveQuantizationType] = None
    GopBReference: Optional[XavcGopBReferenceType] = None
    GopClosedCadence: Optional[int] = None
    HrdBufferSize: Optional[int] = None
    InterlaceMode: Optional[XavcInterlaceModeType] = None
    QualityTuningLevel: Optional[XavcHdProfileQualityTuningLevelType] = None
    Slices: Optional[int] = None
    Telecine: Optional[XavcHdProfileTelecineType] = None


class AudioCodecSettingsTypeDef(BaseValidatorModel):
    AacSettings: Optional[AacSettingsTypeDef] = None
    Ac3Settings: Optional[Ac3SettingsTypeDef] = None
    AiffSettings: Optional[AiffSettingsTypeDef] = None
    Codec: Optional[AudioCodecType] = None
    Eac3AtmosSettings: Optional[Eac3AtmosSettingsTypeDef] = None
    Eac3Settings: Optional[Eac3SettingsTypeDef] = None
    FlacSettings: Optional[FlacSettingsTypeDef] = None
    Mp2Settings: Optional[Mp2SettingsTypeDef] = None
    Mp3Settings: Optional[Mp3SettingsTypeDef] = None
    OpusSettings: Optional[OpusSettingsTypeDef] = None
    VorbisSettings: Optional[VorbisSettingsTypeDef] = None
    WavSettings: Optional[WavSettingsTypeDef] = None


class AudioPropertiesTypeDef(BaseValidatorModel):
    BitDepth: Optional[int] = None
    BitRate: Optional[int] = None
    Channels: Optional[int] = None
    FrameRate: Optional[FrameRateTypeDef] = None
    LanguageCode: Optional[str] = None
    SampleRate: Optional[int] = None


class VideoPropertiesTypeDef(BaseValidatorModel):
    BitDepth: Optional[int] = None
    BitRate: Optional[int] = None
    ColorPrimaries: Optional[ColorPrimariesType] = None
    FrameRate: Optional[FrameRateTypeDef] = None
    Height: Optional[int] = None
    MatrixCoefficients: Optional[MatrixCoefficientsType] = None
    TransferCharacteristics: Optional[TransferCharacteristicsType] = None
    Width: Optional[int] = None


class Av1SettingsTypeDef(BaseValidatorModel):
    AdaptiveQuantization: Optional[Av1AdaptiveQuantizationType] = None
    BitDepth: Optional[Av1BitDepthType] = None
    FilmGrainSynthesis: Optional[Av1FilmGrainSynthesisType] = None
    FramerateControl: Optional[Av1FramerateControlType] = None
    FramerateConversionAlgorithm: Optional[Av1FramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    GopSize: Optional[float] = None
    MaxBitrate: Optional[int] = None
    NumberBFramesBetweenReferenceFrames: Optional[int] = None
    QvbrSettings: Optional[Av1QvbrSettingsTypeDef] = None
    RateControlMode: Optional[Literal["QVBR"]] = None
    Slices: Optional[int] = None
    SpatialAdaptiveQuantization: Optional[Av1SpatialAdaptiveQuantizationType] = None


class AvcIntraSettingsTypeDef(BaseValidatorModel):
    AvcIntraClass: Optional[AvcIntraClassType] = None
    AvcIntraUhdSettings: Optional[AvcIntraUhdSettingsTypeDef] = None
    FramerateControl: Optional[AvcIntraFramerateControlType] = None
    FramerateConversionAlgorithm: Optional[AvcIntraFramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    InterlaceMode: Optional[AvcIntraInterlaceModeType] = None
    ScanTypeConversionMode: Optional[AvcIntraScanTypeConversionModeType] = None
    SlowPal: Optional[AvcIntraSlowPalType] = None
    Telecine: Optional[AvcIntraTelecineType] = None


class CaptionDestinationSettingsOutputTypeDef(BaseValidatorModel):
    BurninDestinationSettings: Optional[BurninDestinationSettingsTypeDef] = None
    DestinationType: Optional[CaptionDestinationTypeType] = None
    DvbSubDestinationSettings: Optional[DvbSubDestinationSettingsTypeDef] = None
    EmbeddedDestinationSettings: Optional[EmbeddedDestinationSettingsTypeDef] = None
    ImscDestinationSettings: Optional[ImscDestinationSettingsTypeDef] = None
    SccDestinationSettings: Optional[SccDestinationSettingsTypeDef] = None
    SrtDestinationSettings: Optional[SrtDestinationSettingsTypeDef] = None
    TeletextDestinationSettings: Optional[TeletextDestinationSettingsOutputTypeDef] = None
    TtmlDestinationSettings: Optional[TtmlDestinationSettingsTypeDef] = None
    WebvttDestinationSettings: Optional[WebvttDestinationSettingsTypeDef] = None


class CaptionDestinationSettingsTypeDef(BaseValidatorModel):
    BurninDestinationSettings: Optional[BurninDestinationSettingsTypeDef] = None
    DestinationType: Optional[CaptionDestinationTypeType] = None
    DvbSubDestinationSettings: Optional[DvbSubDestinationSettingsTypeDef] = None
    EmbeddedDestinationSettings: Optional[EmbeddedDestinationSettingsTypeDef] = None
    ImscDestinationSettings: Optional[ImscDestinationSettingsTypeDef] = None
    SccDestinationSettings: Optional[SccDestinationSettingsTypeDef] = None
    SrtDestinationSettings: Optional[SrtDestinationSettingsTypeDef] = None
    TeletextDestinationSettings: Optional[TeletextDestinationSettingsTypeDef] = None
    TtmlDestinationSettings: Optional[TtmlDestinationSettingsTypeDef] = None
    WebvttDestinationSettings: Optional[WebvttDestinationSettingsTypeDef] = None


class FileSourceSettingsTypeDef(BaseValidatorModel):
    ByteRateLimit: Optional[CaptionSourceByteRateLimitType] = None
    Convert608To708: Optional[FileSourceConvert608To708Type] = None
    ConvertPaintToPop: Optional[CaptionSourceConvertPaintOnToPopOnType] = None
    Framerate: Optional[CaptionSourceFramerateTypeDef] = None
    SourceFile: Optional[str] = None
    TimeDelta: Optional[int] = None
    TimeDeltaUnits: Optional[FileSourceTimeDeltaUnitsType] = None


class ChannelMappingOutputTypeDef(BaseValidatorModel):
    OutputChannels: Optional[List[OutputChannelMappingOutputTypeDef]] = None


class ChannelMappingTypeDef(BaseValidatorModel):
    OutputChannels: Optional[Sequence[OutputChannelMappingTypeDef]] = None


class ColorCorrectorTypeDef(BaseValidatorModel):
    Brightness: Optional[int] = None
    ClipLimits: Optional[ClipLimitsTypeDef] = None
    ColorSpaceConversion: Optional[ColorSpaceConversionType] = None
    Contrast: Optional[int] = None
    Hdr10Metadata: Optional[Hdr10MetadataTypeDef] = None
    HdrToSdrToneMapper: Optional[HDRToSDRToneMapperType] = None
    Hue: Optional[int] = None
    MaxLuminance: Optional[int] = None
    SampleRangeConversion: Optional[SampleRangeConversionType] = None
    Saturation: Optional[int] = None
    SdrReferenceWhiteLevel: Optional[int] = None


class VideoSelectorTypeDef(BaseValidatorModel):
    AlphaBehavior: Optional[AlphaBehaviorType] = None
    ColorSpace: Optional[ColorSpaceType] = None
    ColorSpaceUsage: Optional[ColorSpaceUsageType] = None
    EmbeddedTimecodeOverride: Optional[EmbeddedTimecodeOverrideType] = None
    Hdr10Metadata: Optional[Hdr10MetadataTypeDef] = None
    MaxLuminance: Optional[int] = None
    PadVideo: Optional[PadVideoType] = None
    Pid: Optional[int] = None
    ProgramNumber: Optional[int] = None
    Rotate: Optional[InputRotateType] = None
    SampleRange: Optional[InputSampleRangeType] = None


class CreateQueueRequestTypeDef(BaseValidatorModel):
    Name: str
    ConcurrentJobs: Optional[int] = None
    Description: Optional[str] = None
    PricingPlan: Optional[PricingPlanType] = None
    ReservationPlanSettings: Optional[ReservationPlanSettingsTypeDef] = None
    Status: Optional[QueueStatusType] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateQueueRequestTypeDef(BaseValidatorModel):
    Name: str
    ConcurrentJobs: Optional[int] = None
    Description: Optional[str] = None
    ReservationPlanSettings: Optional[ReservationPlanSettingsTypeDef] = None
    Status: Optional[QueueStatusType] = None


class DescribeEndpointsRequestPaginateTypeDef(BaseValidatorModel):
    Mode: Optional[DescribeEndpointsModeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    Category: Optional[str] = None
    ListBy: Optional[JobTemplateListByType] = None
    Order: Optional[OrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsRequestPaginateTypeDef(BaseValidatorModel):
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPresetsRequestPaginateTypeDef(BaseValidatorModel):
    Category: Optional[str] = None
    ListBy: Optional[PresetListByType] = None
    Order: Optional[OrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQueuesRequestPaginateTypeDef(BaseValidatorModel):
    ListBy: Optional[QueueListByType] = None
    Order: Optional[OrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVersionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchJobsRequestPaginateTypeDef(BaseValidatorModel):
    InputFile: Optional[str] = None
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEndpointsResponseTypeDef(BaseValidatorModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SpekeKeyProviderCmafOutputTypeDef(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    DashSignaledSystemIds: Optional[List[str]] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None
    HlsSignaledSystemIds: Optional[List[str]] = None
    ResourceId: Optional[str] = None
    Url: Optional[str] = None


class SpekeKeyProviderCmafTypeDef(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    DashSignaledSystemIds: Optional[Sequence[str]] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None
    HlsSignaledSystemIds: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    Url: Optional[str] = None


class SpekeKeyProviderOutputTypeDef(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None
    ResourceId: Optional[str] = None
    SystemIds: Optional[List[str]] = None
    Url: Optional[str] = None


class SpekeKeyProviderTypeDef(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None
    ResourceId: Optional[str] = None
    SystemIds: Optional[Sequence[str]] = None
    Url: Optional[str] = None


class EsamSettingsTypeDef(BaseValidatorModel):
    ManifestConfirmConditionNotification: Optional[ EsamManifestConfirmConditionNotificationTypeDef ] = None
    ResponseSignalPreroll: Optional[int] = None
    SignalProcessingNotification: Optional[EsamSignalProcessingNotificationTypeDef] = None


class GetPolicyResponseTypeDef(BaseValidatorModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutPolicyRequestTypeDef(BaseValidatorModel):
    Policy: PolicyTypeDef


class PutPolicyResponseTypeDef(BaseValidatorModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class H264SettingsTypeDef(BaseValidatorModel):
    AdaptiveQuantization: Optional[H264AdaptiveQuantizationType] = None
    BandwidthReductionFilter: Optional[BandwidthReductionFilterTypeDef] = None
    Bitrate: Optional[int] = None
    CodecLevel: Optional[H264CodecLevelType] = None
    CodecProfile: Optional[H264CodecProfileType] = None
    DynamicSubGop: Optional[H264DynamicSubGopType] = None
    EndOfStreamMarkers: Optional[H264EndOfStreamMarkersType] = None
    EntropyEncoding: Optional[H264EntropyEncodingType] = None
    FieldEncoding: Optional[H264FieldEncodingType] = None
    FlickerAdaptiveQuantization: Optional[H264FlickerAdaptiveQuantizationType] = None
    FramerateControl: Optional[H264FramerateControlType] = None
    FramerateConversionAlgorithm: Optional[H264FramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    GopBReference: Optional[H264GopBReferenceType] = None
    GopClosedCadence: Optional[int] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[H264GopSizeUnitsType] = None
    HrdBufferFinalFillPercentage: Optional[int] = None
    HrdBufferInitialFillPercentage: Optional[int] = None
    HrdBufferSize: Optional[int] = None
    InterlaceMode: Optional[H264InterlaceModeType] = None
    MaxBitrate: Optional[int] = None
    MinIInterval: Optional[int] = None
    NumberBFramesBetweenReferenceFrames: Optional[int] = None
    NumberReferenceFrames: Optional[int] = None
    ParControl: Optional[H264ParControlType] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    QualityTuningLevel: Optional[H264QualityTuningLevelType] = None
    QvbrSettings: Optional[H264QvbrSettingsTypeDef] = None
    RateControlMode: Optional[H264RateControlModeType] = None
    RepeatPps: Optional[H264RepeatPpsType] = None
    SaliencyAwareEncoding: Optional[H264SaliencyAwareEncodingType] = None
    ScanTypeConversionMode: Optional[H264ScanTypeConversionModeType] = None
    SceneChangeDetect: Optional[H264SceneChangeDetectType] = None
    Slices: Optional[int] = None
    SlowPal: Optional[H264SlowPalType] = None
    Softness: Optional[int] = None
    SpatialAdaptiveQuantization: Optional[H264SpatialAdaptiveQuantizationType] = None
    Syntax: Optional[H264SyntaxType] = None
    Telecine: Optional[H264TelecineType] = None
    TemporalAdaptiveQuantization: Optional[H264TemporalAdaptiveQuantizationType] = None
    UnregisteredSeiTimecode: Optional[H264UnregisteredSeiTimecodeType] = None
    WriteMp4PackagingType: Optional[H264WriteMp4PackagingTypeType] = None


class H265SettingsTypeDef(BaseValidatorModel):
    AdaptiveQuantization: Optional[H265AdaptiveQuantizationType] = None
    AlternateTransferFunctionSei: Optional[H265AlternateTransferFunctionSeiType] = None
    BandwidthReductionFilter: Optional[BandwidthReductionFilterTypeDef] = None
    Bitrate: Optional[int] = None
    CodecLevel: Optional[H265CodecLevelType] = None
    CodecProfile: Optional[H265CodecProfileType] = None
    Deblocking: Optional[H265DeblockingType] = None
    DynamicSubGop: Optional[H265DynamicSubGopType] = None
    EndOfStreamMarkers: Optional[H265EndOfStreamMarkersType] = None
    FlickerAdaptiveQuantization: Optional[H265FlickerAdaptiveQuantizationType] = None
    FramerateControl: Optional[H265FramerateControlType] = None
    FramerateConversionAlgorithm: Optional[H265FramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    GopBReference: Optional[H265GopBReferenceType] = None
    GopClosedCadence: Optional[int] = None
    GopSize: Optional[float] = None
    GopSizeUnits: Optional[H265GopSizeUnitsType] = None
    HrdBufferFinalFillPercentage: Optional[int] = None
    HrdBufferInitialFillPercentage: Optional[int] = None
    HrdBufferSize: Optional[int] = None
    InterlaceMode: Optional[H265InterlaceModeType] = None
    MaxBitrate: Optional[int] = None
    MinIInterval: Optional[int] = None
    NumberBFramesBetweenReferenceFrames: Optional[int] = None
    NumberReferenceFrames: Optional[int] = None
    ParControl: Optional[H265ParControlType] = None
    ParDenominator: Optional[int] = None
    ParNumerator: Optional[int] = None
    QualityTuningLevel: Optional[H265QualityTuningLevelType] = None
    QvbrSettings: Optional[H265QvbrSettingsTypeDef] = None
    RateControlMode: Optional[H265RateControlModeType] = None
    SampleAdaptiveOffsetFilterMode: Optional[H265SampleAdaptiveOffsetFilterModeType] = None
    ScanTypeConversionMode: Optional[H265ScanTypeConversionModeType] = None
    SceneChangeDetect: Optional[H265SceneChangeDetectType] = None
    Slices: Optional[int] = None
    SlowPal: Optional[H265SlowPalType] = None
    SpatialAdaptiveQuantization: Optional[H265SpatialAdaptiveQuantizationType] = None
    Telecine: Optional[H265TelecineType] = None
    TemporalAdaptiveQuantization: Optional[H265TemporalAdaptiveQuantizationType] = None
    TemporalIds: Optional[H265TemporalIdsType] = None
    Tiles: Optional[H265TilesType] = None
    UnregisteredSeiTimecode: Optional[H265UnregisteredSeiTimecodeType] = None
    WriteMp4PackagingType: Optional[H265WriteMp4PackagingTypeType] = None


class OutputSettingsTypeDef(BaseValidatorModel):
    HlsSettings: Optional[HlsSettingsTypeDef] = None


class TimedMetadataInsertionOutputTypeDef(BaseValidatorModel):
    Id3Insertions: Optional[List[Id3InsertionTypeDef]] = None


class TimedMetadataInsertionTypeDef(BaseValidatorModel):
    Id3Insertions: Optional[Sequence[Id3InsertionTypeDef]] = None


class ImageInserterOutputTypeDef(BaseValidatorModel):
    InsertableImages: Optional[List[InsertableImageTypeDef]] = None
    SdrReferenceWhiteLevel: Optional[int] = None


class ImageInserterTypeDef(BaseValidatorModel):
    InsertableImages: Optional[Sequence[InsertableImageTypeDef]] = None
    SdrReferenceWhiteLevel: Optional[int] = None


class ListVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[JobEngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceTags: ResourceTagsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DvbSdtSettingsTypeDef(BaseValidatorModel):
    pass


class M2tsSettingsOutputTypeDef(BaseValidatorModel):
    AudioBufferModel: Optional[M2tsAudioBufferModelType] = None
    AudioDuration: Optional[M2tsAudioDurationType] = None
    AudioFramesPerPes: Optional[int] = None
    AudioPids: Optional[List[int]] = None
    Bitrate: Optional[int] = None
    BufferModel: Optional[M2tsBufferModelType] = None
    DataPTSControl: Optional[M2tsDataPtsControlType] = None
    DvbNitSettings: Optional[DvbNitSettingsTypeDef] = None
    DvbSdtSettings: Optional[DvbSdtSettingsTypeDef] = None
    DvbSubPids: Optional[List[int]] = None
    DvbTdtSettings: Optional[DvbTdtSettingsTypeDef] = None
    DvbTeletextPid: Optional[int] = None
    EbpAudioInterval: Optional[M2tsEbpAudioIntervalType] = None
    EbpPlacement: Optional[M2tsEbpPlacementType] = None
    EsRateInPes: Optional[M2tsEsRateInPesType] = None
    ForceTsVideoEbpOrder: Optional[M2tsForceTsVideoEbpOrderType] = None
    FragmentTime: Optional[float] = None
    KlvMetadata: Optional[M2tsKlvMetadataType] = None
    MaxPcrInterval: Optional[int] = None
    MinEbpInterval: Optional[int] = None
    NielsenId3: Optional[M2tsNielsenId3Type] = None
    NullPacketBitrate: Optional[float] = None
    PatInterval: Optional[int] = None
    PcrControl: Optional[M2tsPcrControlType] = None
    PcrPid: Optional[int] = None
    PmtInterval: Optional[int] = None
    PmtPid: Optional[int] = None
    PreventBufferUnderflow: Optional[M2tsPreventBufferUnderflowType] = None
    PrivateMetadataPid: Optional[int] = None
    ProgramNumber: Optional[int] = None
    PtsOffset: Optional[int] = None
    PtsOffsetMode: Optional[TsPtsOffsetType] = None
    RateMode: Optional[M2tsRateModeType] = None
    Scte35Esam: Optional[M2tsScte35EsamTypeDef] = None
    Scte35Pid: Optional[int] = None
    Scte35Source: Optional[M2tsScte35SourceType] = None
    SegmentationMarkers: Optional[M2tsSegmentationMarkersType] = None
    SegmentationStyle: Optional[M2tsSegmentationStyleType] = None
    SegmentationTime: Optional[float] = None
    TimedMetadataPid: Optional[int] = None
    TransportStreamId: Optional[int] = None
    VideoPid: Optional[int] = None


class M2tsSettingsTypeDef(BaseValidatorModel):
    AudioBufferModel: Optional[M2tsAudioBufferModelType] = None
    AudioDuration: Optional[M2tsAudioDurationType] = None
    AudioFramesPerPes: Optional[int] = None
    AudioPids: Optional[Sequence[int]] = None
    Bitrate: Optional[int] = None
    BufferModel: Optional[M2tsBufferModelType] = None
    DataPTSControl: Optional[M2tsDataPtsControlType] = None
    DvbNitSettings: Optional[DvbNitSettingsTypeDef] = None
    DvbSdtSettings: Optional[DvbSdtSettingsTypeDef] = None
    DvbSubPids: Optional[Sequence[int]] = None
    DvbTdtSettings: Optional[DvbTdtSettingsTypeDef] = None
    DvbTeletextPid: Optional[int] = None
    EbpAudioInterval: Optional[M2tsEbpAudioIntervalType] = None
    EbpPlacement: Optional[M2tsEbpPlacementType] = None
    EsRateInPes: Optional[M2tsEsRateInPesType] = None
    ForceTsVideoEbpOrder: Optional[M2tsForceTsVideoEbpOrderType] = None
    FragmentTime: Optional[float] = None
    KlvMetadata: Optional[M2tsKlvMetadataType] = None
    MaxPcrInterval: Optional[int] = None
    MinEbpInterval: Optional[int] = None
    NielsenId3: Optional[M2tsNielsenId3Type] = None
    NullPacketBitrate: Optional[float] = None
    PatInterval: Optional[int] = None
    PcrControl: Optional[M2tsPcrControlType] = None
    PcrPid: Optional[int] = None
    PmtInterval: Optional[int] = None
    PmtPid: Optional[int] = None
    PreventBufferUnderflow: Optional[M2tsPreventBufferUnderflowType] = None
    PrivateMetadataPid: Optional[int] = None
    ProgramNumber: Optional[int] = None
    PtsOffset: Optional[int] = None
    PtsOffsetMode: Optional[TsPtsOffsetType] = None
    RateMode: Optional[M2tsRateModeType] = None
    Scte35Esam: Optional[M2tsScte35EsamTypeDef] = None
    Scte35Pid: Optional[int] = None
    Scte35Source: Optional[M2tsScte35SourceType] = None
    SegmentationMarkers: Optional[M2tsSegmentationMarkersType] = None
    SegmentationStyle: Optional[M2tsSegmentationStyleType] = None
    SegmentationTime: Optional[float] = None
    TimedMetadataPid: Optional[int] = None
    TransportStreamId: Optional[int] = None
    VideoPid: Optional[int] = None


class MotionImageInserterTypeDef(BaseValidatorModel):
    Framerate: Optional[MotionImageInsertionFramerateTypeDef] = None
    Input: Optional[str] = None
    InsertionMode: Optional[MotionImageInsertionModeType] = None
    Offset: Optional[MotionImageInsertionOffsetTypeDef] = None
    Playback: Optional[MotionImagePlaybackType] = None
    StartTime: Optional[str] = None


class MxfSettingsTypeDef(BaseValidatorModel):
    AfdSignaling: Optional[MxfAfdSignalingType] = None
    Profile: Optional[MxfProfileType] = None
    XavcProfileSettings: Optional[MxfXavcProfileSettingsTypeDef] = None


class PartnerWatermarkingTypeDef(BaseValidatorModel):
    NexguardFileMarkerSettings: Optional[NexGuardFileMarkerSettingsTypeDef] = None


class NoiseReducerTypeDef(BaseValidatorModel):
    Filter: Optional[NoiseReducerFilterType] = None
    FilterSettings: Optional[NoiseReducerFilterSettingsTypeDef] = None
    SpatialFilterSettings: Optional[NoiseReducerSpatialFilterSettingsTypeDef] = None
    TemporalFilterSettings: Optional[NoiseReducerTemporalFilterSettingsTypeDef] = None


class OutputDetailTypeDef(BaseValidatorModel):
    DurationInMs: Optional[int] = None
    VideoDetails: Optional[VideoDetailTypeDef] = None


class ProbeRequestTypeDef(BaseValidatorModel):
    InputFiles: Optional[Sequence[ProbeInputFileTypeDef]] = None


class S3DestinationSettingsTypeDef(BaseValidatorModel):
    AccessControl: Optional[S3DestinationAccessControlTypeDef] = None
    Encryption: Optional[S3EncryptionSettingsTypeDef] = None
    StorageClass: Optional[S3StorageClassType] = None


class VideoOverlayInputOutputTypeDef(BaseValidatorModel):
    FileInput: Optional[str] = None
    InputClippings: Optional[List[VideoOverlayInputClippingTypeDef]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None


class VideoOverlayInputTypeDef(BaseValidatorModel):
    FileInput: Optional[str] = None
    InputClippings: Optional[Sequence[VideoOverlayInputClippingTypeDef]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None


class VideoOverlayTransitionTypeDef(BaseValidatorModel):
    EndPosition: Optional[VideoOverlayPositionTypeDef] = None
    EndTimecode: Optional[str] = None
    StartTimecode: Optional[str] = None


class XavcSettingsTypeDef(BaseValidatorModel):
    AdaptiveQuantization: Optional[XavcAdaptiveQuantizationType] = None
    EntropyEncoding: Optional[XavcEntropyEncodingType] = None
    FramerateControl: Optional[XavcFramerateControlType] = None
    FramerateConversionAlgorithm: Optional[XavcFramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    Profile: Optional[XavcProfileType] = None
    SlowPal: Optional[XavcSlowPalType] = None
    Softness: Optional[int] = None
    SpatialAdaptiveQuantization: Optional[XavcSpatialAdaptiveQuantizationType] = None
    TemporalAdaptiveQuantization: Optional[XavcTemporalAdaptiveQuantizationType] = None
    Xavc4kIntraCbgProfileSettings: Optional[Xavc4kIntraCbgProfileSettingsTypeDef] = None
    Xavc4kIntraVbrProfileSettings: Optional[Xavc4kIntraVbrProfileSettingsTypeDef] = None
    Xavc4kProfileSettings: Optional[Xavc4kProfileSettingsTypeDef] = None
    XavcHdIntraCbgProfileSettings: Optional[XavcHdIntraCbgProfileSettingsTypeDef] = None
    XavcHdProfileSettings: Optional[XavcHdProfileSettingsTypeDef] = None


class TrackTypeDef(BaseValidatorModel):
    AudioProperties: Optional[AudioPropertiesTypeDef] = None
    Codec: Optional[CodecType] = None
    DataProperties: Optional[DataPropertiesTypeDef] = None
    Duration: Optional[float] = None
    Index: Optional[int] = None
    TrackType: Optional[TrackTypeType] = None
    VideoProperties: Optional[VideoPropertiesTypeDef] = None


class AutomatedAbrRuleOutputTypeDef(BaseValidatorModel):
    pass


class AutomatedAbrSettingsOutputTypeDef(BaseValidatorModel):
    MaxAbrBitrate: Optional[int] = None
    MaxRenditions: Optional[int] = None
    MinAbrBitrate: Optional[int] = None
    Rules: Optional[List[AutomatedAbrRuleOutputTypeDef]] = None


class AutomatedAbrRuleTypeDef(BaseValidatorModel):
    pass


class AutomatedAbrSettingsTypeDef(BaseValidatorModel):
    MaxAbrBitrate: Optional[int] = None
    MaxRenditions: Optional[int] = None
    MinAbrBitrate: Optional[int] = None
    Rules: Optional[Sequence[AutomatedAbrRuleTypeDef]] = None


class CaptionDescriptionOutputTypeDef(BaseValidatorModel):
    CaptionSelectorName: Optional[str] = None
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettingsOutputTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None


class CaptionDescriptionPresetOutputTypeDef(BaseValidatorModel):
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettingsOutputTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None


class CaptionDescriptionPresetTypeDef(BaseValidatorModel):
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettingsTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None


class CaptionDescriptionTypeDef(BaseValidatorModel):
    CaptionSelectorName: Optional[str] = None
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettingsTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None


class CaptionSourceSettingsTypeDef(BaseValidatorModel):
    AncillarySourceSettings: Optional[AncillarySourceSettingsTypeDef] = None
    DvbSubSourceSettings: Optional[DvbSubSourceSettingsTypeDef] = None
    EmbeddedSourceSettings: Optional[EmbeddedSourceSettingsTypeDef] = None
    FileSourceSettings: Optional[FileSourceSettingsTypeDef] = None
    SourceType: Optional[CaptionSourceTypeType] = None
    TeletextSourceSettings: Optional[TeletextSourceSettingsTypeDef] = None
    TrackSourceSettings: Optional[TrackSourceSettingsTypeDef] = None
    WebvttHlsSourceSettings: Optional[WebvttHlsSourceSettingsTypeDef] = None


class RemixSettingsOutputTypeDef(BaseValidatorModel):
    AudioDescriptionAudioChannel: Optional[int] = None
    AudioDescriptionDataChannel: Optional[int] = None
    ChannelMapping: Optional[ChannelMappingOutputTypeDef] = None
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None


class RemixSettingsTypeDef(BaseValidatorModel):
    AudioDescriptionAudioChannel: Optional[int] = None
    AudioDescriptionDataChannel: Optional[int] = None
    ChannelMapping: Optional[ChannelMappingTypeDef] = None
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None


class DashIsoEncryptionSettingsOutputTypeDef(BaseValidatorModel):
    PlaybackDeviceCompatibility: Optional[DashIsoPlaybackDeviceCompatibilityType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderOutputTypeDef] = None


class MsSmoothEncryptionSettingsOutputTypeDef(BaseValidatorModel):
    SpekeKeyProvider: Optional[SpekeKeyProviderOutputTypeDef] = None


class DashIsoEncryptionSettingsTypeDef(BaseValidatorModel):
    PlaybackDeviceCompatibility: Optional[DashIsoPlaybackDeviceCompatibilityType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderTypeDef] = None


class MsSmoothEncryptionSettingsTypeDef(BaseValidatorModel):
    SpekeKeyProvider: Optional[SpekeKeyProviderTypeDef] = None


class DolbyVisionTypeDef(BaseValidatorModel):
    pass


class VideoPreprocessorOutputTypeDef(BaseValidatorModel):
    ColorCorrector: Optional[ColorCorrectorTypeDef] = None
    Deinterlacer: Optional[DeinterlacerTypeDef] = None
    DolbyVision: Optional[DolbyVisionTypeDef] = None
    Hdr10Plus: Optional[Hdr10PlusTypeDef] = None
    ImageInserter: Optional[ImageInserterOutputTypeDef] = None
    NoiseReducer: Optional[NoiseReducerTypeDef] = None
    PartnerWatermarking: Optional[PartnerWatermarkingTypeDef] = None
    TimecodeBurnin: Optional[TimecodeBurninTypeDef] = None


class VideoPreprocessorTypeDef(BaseValidatorModel):
    ColorCorrector: Optional[ColorCorrectorTypeDef] = None
    Deinterlacer: Optional[DeinterlacerTypeDef] = None
    DolbyVision: Optional[DolbyVisionTypeDef] = None
    Hdr10Plus: Optional[Hdr10PlusTypeDef] = None
    ImageInserter: Optional[ImageInserterTypeDef] = None
    NoiseReducer: Optional[NoiseReducerTypeDef] = None
    PartnerWatermarking: Optional[PartnerWatermarkingTypeDef] = None
    TimecodeBurnin: Optional[TimecodeBurninTypeDef] = None


class OutputGroupDetailTypeDef(BaseValidatorModel):
    OutputDetails: Optional[List[OutputDetailTypeDef]] = None


class QueueTypeDef(BaseValidatorModel):
    pass


class CreateQueueResponseTypeDef(BaseValidatorModel):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueueResponseTypeDef(BaseValidatorModel):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListQueuesResponseTypeDef(BaseValidatorModel):
    Queues: List[QueueTypeDef]
    TotalConcurrentJobs: int
    UnallocatedConcurrentJobs: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateQueueResponseTypeDef(BaseValidatorModel):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DestinationSettingsTypeDef(BaseValidatorModel):
    S3Settings: Optional[S3DestinationSettingsTypeDef] = None


class VideoOverlayOutputTypeDef(BaseValidatorModel):
    EndTimecode: Optional[str] = None
    InitialPosition: Optional[VideoOverlayPositionTypeDef] = None
    Input: Optional[VideoOverlayInputOutputTypeDef] = None
    Playback: Optional[VideoOverlayPlayBackModeType] = None
    StartTimecode: Optional[str] = None
    Transitions: Optional[List[VideoOverlayTransitionTypeDef]] = None


class VideoOverlayTypeDef(BaseValidatorModel):
    EndTimecode: Optional[str] = None
    InitialPosition: Optional[VideoOverlayPositionTypeDef] = None
    Input: Optional[VideoOverlayInputTypeDef] = None
    Playback: Optional[VideoOverlayPlayBackModeType] = None
    StartTimecode: Optional[str] = None
    Transitions: Optional[Sequence[VideoOverlayTransitionTypeDef]] = None


class VideoCodecSettingsTypeDef(BaseValidatorModel):
    Av1Settings: Optional[Av1SettingsTypeDef] = None
    AvcIntraSettings: Optional[AvcIntraSettingsTypeDef] = None
    Codec: Optional[VideoCodecType] = None
    FrameCaptureSettings: Optional[FrameCaptureSettingsTypeDef] = None
    GifSettings: Optional[GifSettingsTypeDef] = None
    H264Settings: Optional[H264SettingsTypeDef] = None
    H265Settings: Optional[H265SettingsTypeDef] = None
    Mpeg2Settings: Optional[Mpeg2SettingsTypeDef] = None
    ProresSettings: Optional[ProresSettingsTypeDef] = None
    UncompressedSettings: Optional[UncompressedSettingsTypeDef] = None
    Vc3Settings: Optional[Vc3SettingsTypeDef] = None
    Vp8Settings: Optional[Vp8SettingsTypeDef] = None
    Vp9Settings: Optional[Vp9SettingsTypeDef] = None
    XavcSettings: Optional[XavcSettingsTypeDef] = None


class ContainerTypeDef(BaseValidatorModel):
    Duration: Optional[float] = None
    Format: Optional[FormatType] = None
    Tracks: Optional[List[TrackTypeDef]] = None


class AutomatedEncodingSettingsOutputTypeDef(BaseValidatorModel):
    AbrSettings: Optional[AutomatedAbrSettingsOutputTypeDef] = None


class AutomatedEncodingSettingsTypeDef(BaseValidatorModel):
    AbrSettings: Optional[AutomatedAbrSettingsTypeDef] = None


class CaptionSelectorTypeDef(BaseValidatorModel):
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    SourceSettings: Optional[CaptionSourceSettingsTypeDef] = None


class AudioDescriptionOutputTypeDef(BaseValidatorModel):
    AudioChannelTaggingSettings: Optional[AudioChannelTaggingSettingsOutputTypeDef] = None
    AudioNormalizationSettings: Optional[AudioNormalizationSettingsTypeDef] = None
    AudioSourceName: Optional[str] = None
    AudioType: Optional[int] = None
    AudioTypeControl: Optional[AudioTypeControlType] = None
    CodecSettings: Optional[AudioCodecSettingsTypeDef] = None
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageCodeControl: Optional[AudioLanguageCodeControlType] = None
    RemixSettings: Optional[RemixSettingsOutputTypeDef] = None
    StreamName: Optional[str] = None


class AudioSelectorOutputTypeDef(BaseValidatorModel):
    AudioDurationCorrection: Optional[AudioDurationCorrectionType] = None
    CustomLanguageCode: Optional[str] = None
    DefaultSelection: Optional[AudioDefaultSelectionType] = None
    ExternalAudioFileInput: Optional[str] = None
    HlsRenditionGroupSettings: Optional[HlsRenditionGroupSettingsTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Offset: Optional[int] = None
    Pids: Optional[List[int]] = None
    ProgramSelection: Optional[int] = None
    RemixSettings: Optional[RemixSettingsOutputTypeDef] = None
    SelectorType: Optional[AudioSelectorTypeType] = None
    Tracks: Optional[List[int]] = None


class AudioDescriptionTypeDef(BaseValidatorModel):
    AudioChannelTaggingSettings: Optional[AudioChannelTaggingSettingsTypeDef] = None
    AudioNormalizationSettings: Optional[AudioNormalizationSettingsTypeDef] = None
    AudioSourceName: Optional[str] = None
    AudioType: Optional[int] = None
    AudioTypeControl: Optional[AudioTypeControlType] = None
    CodecSettings: Optional[AudioCodecSettingsTypeDef] = None
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageCodeControl: Optional[AudioLanguageCodeControlType] = None
    RemixSettings: Optional[RemixSettingsTypeDef] = None
    StreamName: Optional[str] = None


class AudioSelectorTypeDef(BaseValidatorModel):
    AudioDurationCorrection: Optional[AudioDurationCorrectionType] = None
    CustomLanguageCode: Optional[str] = None
    DefaultSelection: Optional[AudioDefaultSelectionType] = None
    ExternalAudioFileInput: Optional[str] = None
    HlsRenditionGroupSettings: Optional[HlsRenditionGroupSettingsTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Offset: Optional[int] = None
    Pids: Optional[Sequence[int]] = None
    ProgramSelection: Optional[int] = None
    RemixSettings: Optional[RemixSettingsTypeDef] = None
    SelectorType: Optional[AudioSelectorTypeType] = None
    Tracks: Optional[Sequence[int]] = None


class CmafEncryptionSettingsOutputTypeDef(BaseValidatorModel):
    pass


class CmafGroupSettingsOutputTypeDef(BaseValidatorModel):
    AdditionalManifests: Optional[List[CmafAdditionalManifestOutputTypeDef]] = None
    BaseUrl: Optional[str] = None
    ClientCache: Optional[CmafClientCacheType] = None
    CodecSpecification: Optional[CmafCodecSpecificationType] = None
    DashIFrameTrickPlayNameModifier: Optional[str] = None
    DashManifestStyle: Optional[DashManifestStyleType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[CmafEncryptionSettingsOutputTypeDef] = None
    FragmentLength: Optional[int] = None
    ImageBasedTrickPlay: Optional[CmafImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[CmafImageBasedTrickPlaySettingsTypeDef] = None
    ManifestCompression: Optional[CmafManifestCompressionType] = None
    ManifestDurationFormat: Optional[CmafManifestDurationFormatType] = None
    MinBufferTime: Optional[int] = None
    MinFinalSegmentLength: Optional[float] = None
    MpdManifestBandwidthType: Optional[CmafMpdManifestBandwidthTypeType] = None
    MpdProfile: Optional[CmafMpdProfileType] = None
    PtsOffsetHandlingForBFrames: Optional[CmafPtsOffsetHandlingForBFramesType] = None
    SegmentControl: Optional[CmafSegmentControlType] = None
    SegmentLength: Optional[int] = None
    SegmentLengthControl: Optional[CmafSegmentLengthControlType] = None
    StreamInfResolution: Optional[CmafStreamInfResolutionType] = None
    TargetDurationCompatibilityMode: Optional[CmafTargetDurationCompatibilityModeType] = None
    VideoCompositionOffsets: Optional[CmafVideoCompositionOffsetsType] = None
    WriteDashManifest: Optional[CmafWriteDASHManifestType] = None
    WriteHlsManifest: Optional[CmafWriteHLSManifestType] = None
    WriteSegmentTimelineInRepresentation: Optional[CmafWriteSegmentTimelineInRepresentationType] = None


class CmafEncryptionSettingsTypeDef(BaseValidatorModel):
    pass


class CmafGroupSettingsTypeDef(BaseValidatorModel):
    AdditionalManifests: Optional[Sequence[CmafAdditionalManifestTypeDef]] = None
    BaseUrl: Optional[str] = None
    ClientCache: Optional[CmafClientCacheType] = None
    CodecSpecification: Optional[CmafCodecSpecificationType] = None
    DashIFrameTrickPlayNameModifier: Optional[str] = None
    DashManifestStyle: Optional[DashManifestStyleType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[CmafEncryptionSettingsTypeDef] = None
    FragmentLength: Optional[int] = None
    ImageBasedTrickPlay: Optional[CmafImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[CmafImageBasedTrickPlaySettingsTypeDef] = None
    ManifestCompression: Optional[CmafManifestCompressionType] = None
    ManifestDurationFormat: Optional[CmafManifestDurationFormatType] = None
    MinBufferTime: Optional[int] = None
    MinFinalSegmentLength: Optional[float] = None
    MpdManifestBandwidthType: Optional[CmafMpdManifestBandwidthTypeType] = None
    MpdProfile: Optional[CmafMpdProfileType] = None
    PtsOffsetHandlingForBFrames: Optional[CmafPtsOffsetHandlingForBFramesType] = None
    SegmentControl: Optional[CmafSegmentControlType] = None
    SegmentLength: Optional[int] = None
    SegmentLengthControl: Optional[CmafSegmentLengthControlType] = None
    StreamInfResolution: Optional[CmafStreamInfResolutionType] = None
    TargetDurationCompatibilityMode: Optional[CmafTargetDurationCompatibilityModeType] = None
    VideoCompositionOffsets: Optional[CmafVideoCompositionOffsetsType] = None
    WriteDashManifest: Optional[CmafWriteDASHManifestType] = None
    WriteHlsManifest: Optional[CmafWriteHLSManifestType] = None
    WriteSegmentTimelineInRepresentation: Optional[CmafWriteSegmentTimelineInRepresentationType] = None


class DashIsoGroupSettingsOutputTypeDef(BaseValidatorModel):
    AdditionalManifests: Optional[List[DashAdditionalManifestOutputTypeDef]] = None
    AudioChannelConfigSchemeIdUri: Optional[DashIsoGroupAudioChannelConfigSchemeIdUriType] = None
    BaseUrl: Optional[str] = None
    DashIFrameTrickPlayNameModifier: Optional[str] = None
    DashManifestStyle: Optional[DashManifestStyleType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[DashIsoEncryptionSettingsOutputTypeDef] = None
    FragmentLength: Optional[int] = None
    HbbtvCompliance: Optional[DashIsoHbbtvComplianceType] = None
    ImageBasedTrickPlay: Optional[DashIsoImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[DashIsoImageBasedTrickPlaySettingsTypeDef] = None
    MinBufferTime: Optional[int] = None
    MinFinalSegmentLength: Optional[float] = None
    MpdManifestBandwidthType: Optional[DashIsoMpdManifestBandwidthTypeType] = None
    MpdProfile: Optional[DashIsoMpdProfileType] = None
    PtsOffsetHandlingForBFrames: Optional[DashIsoPtsOffsetHandlingForBFramesType] = None
    SegmentControl: Optional[DashIsoSegmentControlType] = None
    SegmentLength: Optional[int] = None
    SegmentLengthControl: Optional[DashIsoSegmentLengthControlType] = None
    VideoCompositionOffsets: Optional[DashIsoVideoCompositionOffsetsType] = None
    WriteSegmentTimelineInRepresentation: Optional[ DashIsoWriteSegmentTimelineInRepresentationType ] = None


class DashIsoGroupSettingsTypeDef(BaseValidatorModel):
    AdditionalManifests: Optional[Sequence[DashAdditionalManifestTypeDef]] = None
    AudioChannelConfigSchemeIdUri: Optional[DashIsoGroupAudioChannelConfigSchemeIdUriType] = None
    BaseUrl: Optional[str] = None
    DashIFrameTrickPlayNameModifier: Optional[str] = None
    DashManifestStyle: Optional[DashManifestStyleType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[DashIsoEncryptionSettingsTypeDef] = None
    FragmentLength: Optional[int] = None
    HbbtvCompliance: Optional[DashIsoHbbtvComplianceType] = None
    ImageBasedTrickPlay: Optional[DashIsoImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[DashIsoImageBasedTrickPlaySettingsTypeDef] = None
    MinBufferTime: Optional[int] = None
    MinFinalSegmentLength: Optional[float] = None
    MpdManifestBandwidthType: Optional[DashIsoMpdManifestBandwidthTypeType] = None
    MpdProfile: Optional[DashIsoMpdProfileType] = None
    PtsOffsetHandlingForBFrames: Optional[DashIsoPtsOffsetHandlingForBFramesType] = None
    SegmentControl: Optional[DashIsoSegmentControlType] = None
    SegmentLength: Optional[int] = None
    SegmentLengthControl: Optional[DashIsoSegmentLengthControlType] = None
    VideoCompositionOffsets: Optional[DashIsoVideoCompositionOffsetsType] = None
    WriteSegmentTimelineInRepresentation: Optional[ DashIsoWriteSegmentTimelineInRepresentationType ] = None


class FileGroupSettingsTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None


class HlsEncryptionSettingsOutputTypeDef(BaseValidatorModel):
    pass


class HlsGroupSettingsOutputTypeDef(BaseValidatorModel):
    AdMarkers: Optional[List[HlsAdMarkersType]] = None
    AdditionalManifests: Optional[List[HlsAdditionalManifestOutputTypeDef]] = None
    AudioOnlyHeader: Optional[HlsAudioOnlyHeaderType] = None
    BaseUrl: Optional[str] = None
    CaptionLanguageMappings: Optional[List[HlsCaptionLanguageMappingTypeDef]] = None
    CaptionLanguageSetting: Optional[HlsCaptionLanguageSettingType] = None
    CaptionSegmentLengthControl: Optional[HlsCaptionSegmentLengthControlType] = None
    ClientCache: Optional[HlsClientCacheType] = None
    CodecSpecification: Optional[HlsCodecSpecificationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    DirectoryStructure: Optional[HlsDirectoryStructureType] = None
    Encryption: Optional[HlsEncryptionSettingsOutputTypeDef] = None
    ImageBasedTrickPlay: Optional[HlsImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[HlsImageBasedTrickPlaySettingsTypeDef] = None
    ManifestCompression: Optional[HlsManifestCompressionType] = None
    ManifestDurationFormat: Optional[HlsManifestDurationFormatType] = None
    MinFinalSegmentLength: Optional[float] = None
    MinSegmentLength: Optional[int] = None
    OutputSelection: Optional[HlsOutputSelectionType] = None
    ProgramDateTime: Optional[HlsProgramDateTimeType] = None
    ProgramDateTimePeriod: Optional[int] = None
    ProgressiveWriteHlsManifest: Optional[HlsProgressiveWriteHlsManifestType] = None
    SegmentControl: Optional[HlsSegmentControlType] = None
    SegmentLength: Optional[int] = None
    SegmentLengthControl: Optional[HlsSegmentLengthControlType] = None
    SegmentsPerSubdirectory: Optional[int] = None
    StreamInfResolution: Optional[HlsStreamInfResolutionType] = None
    TargetDurationCompatibilityMode: Optional[HlsTargetDurationCompatibilityModeType] = None
    TimedMetadataId3Frame: Optional[HlsTimedMetadataId3FrameType] = None
    TimedMetadataId3Period: Optional[int] = None
    TimestampDeltaMilliseconds: Optional[int] = None


class HlsEncryptionSettingsTypeDef(BaseValidatorModel):
    pass


class HlsGroupSettingsTypeDef(BaseValidatorModel):
    AdMarkers: Optional[Sequence[HlsAdMarkersType]] = None
    AdditionalManifests: Optional[Sequence[HlsAdditionalManifestTypeDef]] = None
    AudioOnlyHeader: Optional[HlsAudioOnlyHeaderType] = None
    BaseUrl: Optional[str] = None
    CaptionLanguageMappings: Optional[Sequence[HlsCaptionLanguageMappingTypeDef]] = None
    CaptionLanguageSetting: Optional[HlsCaptionLanguageSettingType] = None
    CaptionSegmentLengthControl: Optional[HlsCaptionSegmentLengthControlType] = None
    ClientCache: Optional[HlsClientCacheType] = None
    CodecSpecification: Optional[HlsCodecSpecificationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    DirectoryStructure: Optional[HlsDirectoryStructureType] = None
    Encryption: Optional[HlsEncryptionSettingsTypeDef] = None
    ImageBasedTrickPlay: Optional[HlsImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[HlsImageBasedTrickPlaySettingsTypeDef] = None
    ManifestCompression: Optional[HlsManifestCompressionType] = None
    ManifestDurationFormat: Optional[HlsManifestDurationFormatType] = None
    MinFinalSegmentLength: Optional[float] = None
    MinSegmentLength: Optional[int] = None
    OutputSelection: Optional[HlsOutputSelectionType] = None
    ProgramDateTime: Optional[HlsProgramDateTimeType] = None
    ProgramDateTimePeriod: Optional[int] = None
    ProgressiveWriteHlsManifest: Optional[HlsProgressiveWriteHlsManifestType] = None
    SegmentControl: Optional[HlsSegmentControlType] = None
    SegmentLength: Optional[int] = None
    SegmentLengthControl: Optional[HlsSegmentLengthControlType] = None
    SegmentsPerSubdirectory: Optional[int] = None
    StreamInfResolution: Optional[HlsStreamInfResolutionType] = None
    TargetDurationCompatibilityMode: Optional[HlsTargetDurationCompatibilityModeType] = None
    TimedMetadataId3Frame: Optional[HlsTimedMetadataId3FrameType] = None
    TimedMetadataId3Period: Optional[int] = None
    TimestampDeltaMilliseconds: Optional[int] = None


class MsSmoothGroupSettingsOutputTypeDef(BaseValidatorModel):
    AdditionalManifests: Optional[List[MsSmoothAdditionalManifestOutputTypeDef]] = None
    AudioDeduplication: Optional[MsSmoothAudioDeduplicationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[MsSmoothEncryptionSettingsOutputTypeDef] = None
    FragmentLength: Optional[int] = None
    FragmentLengthControl: Optional[MsSmoothFragmentLengthControlType] = None
    ManifestEncoding: Optional[MsSmoothManifestEncodingType] = None


class MsSmoothGroupSettingsTypeDef(BaseValidatorModel):
    AdditionalManifests: Optional[Sequence[MsSmoothAdditionalManifestTypeDef]] = None
    AudioDeduplication: Optional[MsSmoothAudioDeduplicationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[MsSmoothEncryptionSettingsTypeDef] = None
    FragmentLength: Optional[int] = None
    FragmentLengthControl: Optional[MsSmoothFragmentLengthControlType] = None
    ManifestEncoding: Optional[MsSmoothManifestEncodingType] = None


class VideoDescriptionOutputTypeDef(BaseValidatorModel):
    AfdSignaling: Optional[AfdSignalingType] = None
    AntiAlias: Optional[AntiAliasType] = None
    ChromaPositionMode: Optional[ChromaPositionModeType] = None
    CodecSettings: Optional[VideoCodecSettingsTypeDef] = None
    ColorMetadata: Optional[ColorMetadataType] = None
    Crop: Optional[RectangleTypeDef] = None
    DropFrameTimecode: Optional[DropFrameTimecodeType] = None
    FixedAfd: Optional[int] = None
    Height: Optional[int] = None
    Position: Optional[RectangleTypeDef] = None
    RespondToAfd: Optional[RespondToAfdType] = None
    ScalingBehavior: Optional[ScalingBehaviorType] = None
    Sharpness: Optional[int] = None
    TimecodeInsertion: Optional[VideoTimecodeInsertionType] = None
    TimecodeTrack: Optional[TimecodeTrackType] = None
    VideoPreprocessors: Optional[VideoPreprocessorOutputTypeDef] = None
    Width: Optional[int] = None


class VideoDescriptionTypeDef(BaseValidatorModel):
    AfdSignaling: Optional[AfdSignalingType] = None
    AntiAlias: Optional[AntiAliasType] = None
    ChromaPositionMode: Optional[ChromaPositionModeType] = None
    CodecSettings: Optional[VideoCodecSettingsTypeDef] = None
    ColorMetadata: Optional[ColorMetadataType] = None
    Crop: Optional[RectangleTypeDef] = None
    DropFrameTimecode: Optional[DropFrameTimecodeType] = None
    FixedAfd: Optional[int] = None
    Height: Optional[int] = None
    Position: Optional[RectangleTypeDef] = None
    RespondToAfd: Optional[RespondToAfdType] = None
    ScalingBehavior: Optional[ScalingBehaviorType] = None
    Sharpness: Optional[int] = None
    TimecodeInsertion: Optional[VideoTimecodeInsertionType] = None
    TimecodeTrack: Optional[TimecodeTrackType] = None
    VideoPreprocessors: Optional[VideoPreprocessorTypeDef] = None
    Width: Optional[int] = None


class InputOutputTypeDef(BaseValidatorModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettingsTypeDef] = None
    AudioSelectorGroups: Optional[Dict[str, AudioSelectorGroupOutputTypeDef]] = None
    AudioSelectors: Optional[Dict[str, AudioSelectorOutputTypeDef]] = None
    CaptionSelectors: Optional[Dict[str, CaptionSelectorTypeDef]] = None
    Crop: Optional[RectangleTypeDef] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DecryptionSettings: Optional[InputDecryptionSettingsTypeDef] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
    DynamicAudioSelectors: Optional[Dict[str, DynamicAudioSelectorTypeDef]] = None
    FileInput: Optional[str] = None
    FilterEnable: Optional[InputFilterEnableType] = None
    FilterStrength: Optional[int] = None
    ImageInserter: Optional[ImageInserterOutputTypeDef] = None
    InputClippings: Optional[List[InputClippingTypeDef]] = None
    InputScanType: Optional[InputScanTypeType] = None
    Position: Optional[RectangleTypeDef] = None
    ProgramNumber: Optional[int] = None
    PsiControl: Optional[InputPsiControlType] = None
    SupplementalImps: Optional[List[str]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None
    VideoGenerator: Optional[InputVideoGeneratorTypeDef] = None
    VideoOverlays: Optional[List[VideoOverlayOutputTypeDef]] = None
    VideoSelector: Optional[VideoSelectorTypeDef] = None


class InputTemplateOutputTypeDef(BaseValidatorModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettingsTypeDef] = None
    AudioSelectorGroups: Optional[Dict[str, AudioSelectorGroupOutputTypeDef]] = None
    AudioSelectors: Optional[Dict[str, AudioSelectorOutputTypeDef]] = None
    CaptionSelectors: Optional[Dict[str, CaptionSelectorTypeDef]] = None
    Crop: Optional[RectangleTypeDef] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
    DynamicAudioSelectors: Optional[Dict[str, DynamicAudioSelectorTypeDef]] = None
    FilterEnable: Optional[InputFilterEnableType] = None
    FilterStrength: Optional[int] = None
    ImageInserter: Optional[ImageInserterOutputTypeDef] = None
    InputClippings: Optional[List[InputClippingTypeDef]] = None
    InputScanType: Optional[InputScanTypeType] = None
    Position: Optional[RectangleTypeDef] = None
    ProgramNumber: Optional[int] = None
    PsiControl: Optional[InputPsiControlType] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None
    VideoOverlays: Optional[List[VideoOverlayOutputTypeDef]] = None
    VideoSelector: Optional[VideoSelectorTypeDef] = None


class InputTemplateTypeDef(BaseValidatorModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettingsTypeDef] = None
    AudioSelectorGroups: Optional[Mapping[str, AudioSelectorGroupTypeDef]] = None
    AudioSelectors: Optional[Mapping[str, AudioSelectorTypeDef]] = None
    CaptionSelectors: Optional[Mapping[str, CaptionSelectorTypeDef]] = None
    Crop: Optional[RectangleTypeDef] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
    DynamicAudioSelectors: Optional[Mapping[str, DynamicAudioSelectorTypeDef]] = None
    FilterEnable: Optional[InputFilterEnableType] = None
    FilterStrength: Optional[int] = None
    ImageInserter: Optional[ImageInserterTypeDef] = None
    InputClippings: Optional[Sequence[InputClippingTypeDef]] = None
    InputScanType: Optional[InputScanTypeType] = None
    Position: Optional[RectangleTypeDef] = None
    ProgramNumber: Optional[int] = None
    PsiControl: Optional[InputPsiControlType] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None
    VideoOverlays: Optional[Sequence[VideoOverlayTypeDef]] = None
    VideoSelector: Optional[VideoSelectorTypeDef] = None


class InputTypeDef(BaseValidatorModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettingsTypeDef] = None
    AudioSelectorGroups: Optional[Mapping[str, AudioSelectorGroupTypeDef]] = None
    AudioSelectors: Optional[Mapping[str, AudioSelectorTypeDef]] = None
    CaptionSelectors: Optional[Mapping[str, CaptionSelectorTypeDef]] = None
    Crop: Optional[RectangleTypeDef] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DecryptionSettings: Optional[InputDecryptionSettingsTypeDef] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
    DynamicAudioSelectors: Optional[Mapping[str, DynamicAudioSelectorTypeDef]] = None
    FileInput: Optional[str] = None
    FilterEnable: Optional[InputFilterEnableType] = None
    FilterStrength: Optional[int] = None
    ImageInserter: Optional[ImageInserterTypeDef] = None
    InputClippings: Optional[Sequence[InputClippingTypeDef]] = None
    InputScanType: Optional[InputScanTypeType] = None
    Position: Optional[RectangleTypeDef] = None
    ProgramNumber: Optional[int] = None
    PsiControl: Optional[InputPsiControlType] = None
    SupplementalImps: Optional[Sequence[str]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None
    VideoGenerator: Optional[InputVideoGeneratorTypeDef] = None
    VideoOverlays: Optional[Sequence[VideoOverlayTypeDef]] = None
    VideoSelector: Optional[VideoSelectorTypeDef] = None


class ContainerSettingsOutputTypeDef(BaseValidatorModel):
    pass


class ExtraTypeDef(BaseValidatorModel):
    AudioDescriptions: Optional[List[AudioDescriptionOutputTypeDef]] = None
    CaptionDescriptions: Optional[List[CaptionDescriptionOutputTypeDef]] = None
    ContainerSettings: Optional[ContainerSettingsOutputTypeDef] = None
    Extension: Optional[str] = None
    NameModifier: Optional[str] = None
    OutputSettings: Optional[OutputSettingsTypeDef] = None
    Preset: Optional[str] = None
    VideoDescription: Optional[VideoDescriptionOutputTypeDef] = None


class PresetSettingsOutputTypeDef(BaseValidatorModel):
    AudioDescriptions: Optional[List[AudioDescriptionOutputTypeDef]] = None
    CaptionDescriptions: Optional[List[CaptionDescriptionPresetOutputTypeDef]] = None
    ContainerSettings: Optional[ContainerSettingsOutputTypeDef] = None
    VideoDescription: Optional[VideoDescriptionOutputTypeDef] = None


class ContainerSettingsTypeDef(BaseValidatorModel):
    pass


class OutputTypeDef(BaseValidatorModel):
    AudioDescriptions: Optional[Sequence[AudioDescriptionTypeDef]] = None
    CaptionDescriptions: Optional[Sequence[CaptionDescriptionTypeDef]] = None
    ContainerSettings: Optional[ContainerSettingsTypeDef] = None
    Extension: Optional[str] = None
    NameModifier: Optional[str] = None
    OutputSettings: Optional[OutputSettingsTypeDef] = None
    Preset: Optional[str] = None
    VideoDescription: Optional[VideoDescriptionTypeDef] = None


class PresetSettingsTypeDef(BaseValidatorModel):
    AudioDescriptions: Optional[Sequence[AudioDescriptionTypeDef]] = None
    CaptionDescriptions: Optional[Sequence[CaptionDescriptionPresetTypeDef]] = None
    ContainerSettings: Optional[ContainerSettingsTypeDef] = None
    VideoDescription: Optional[VideoDescriptionTypeDef] = None


class ProbeResultTypeDef(BaseValidatorModel):
    pass


class ProbeResponseTypeDef(BaseValidatorModel):
    ProbeResults: List[ProbeResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class OutputGroupSettingsOutputTypeDef(BaseValidatorModel):
    pass


class OutputGroupOutputTypeDef(BaseValidatorModel):
    AutomatedEncodingSettings: Optional[AutomatedEncodingSettingsOutputTypeDef] = None
    CustomName: Optional[str] = None
    Name: Optional[str] = None
    OutputGroupSettings: Optional[OutputGroupSettingsOutputTypeDef] = None
    Outputs: Optional[List[ExtraTypeDef]] = None


class OutputGroupSettingsTypeDef(BaseValidatorModel):
    pass


class OutputGroupTypeDef(BaseValidatorModel):
    AutomatedEncodingSettings: Optional[AutomatedEncodingSettingsTypeDef] = None
    CustomName: Optional[str] = None
    Name: Optional[str] = None
    OutputGroupSettings: Optional[OutputGroupSettingsTypeDef] = None
    Outputs: Optional[Sequence[OutputTypeDef]] = None


class JobSettingsOutputTypeDef(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    AvailBlanking: Optional[AvailBlankingTypeDef] = None
    ColorConversion3DLUTSettings: Optional[List[ColorConversion3DLUTSettingTypeDef]] = None
    Esam: Optional[EsamSettingsTypeDef] = None
    ExtendedDataServices: Optional[ExtendedDataServicesTypeDef] = None
    FollowSource: Optional[int] = None
    Inputs: Optional[List[InputOutputTypeDef]] = None
    KantarWatermark: Optional[KantarWatermarkSettingsTypeDef] = None
    MotionImageInserter: Optional[MotionImageInserterTypeDef] = None
    NielsenConfiguration: Optional[NielsenConfigurationTypeDef] = None
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettingsTypeDef] = None
    OutputGroups: Optional[List[OutputGroupOutputTypeDef]] = None
    TimecodeConfig: Optional[TimecodeConfigTypeDef] = None
    TimedMetadataInsertion: Optional[TimedMetadataInsertionOutputTypeDef] = None


class JobTemplateSettingsOutputTypeDef(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    AvailBlanking: Optional[AvailBlankingTypeDef] = None
    ColorConversion3DLUTSettings: Optional[List[ColorConversion3DLUTSettingTypeDef]] = None
    Esam: Optional[EsamSettingsTypeDef] = None
    ExtendedDataServices: Optional[ExtendedDataServicesTypeDef] = None
    FollowSource: Optional[int] = None
    Inputs: Optional[List[InputTemplateOutputTypeDef]] = None
    KantarWatermark: Optional[KantarWatermarkSettingsTypeDef] = None
    MotionImageInserter: Optional[MotionImageInserterTypeDef] = None
    NielsenConfiguration: Optional[NielsenConfigurationTypeDef] = None
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettingsTypeDef] = None
    OutputGroups: Optional[List[OutputGroupOutputTypeDef]] = None
    TimecodeConfig: Optional[TimecodeConfigTypeDef] = None
    TimedMetadataInsertion: Optional[TimedMetadataInsertionOutputTypeDef] = None


class PresetTypeDef(BaseValidatorModel):
    pass


class CreatePresetResponseTypeDef(BaseValidatorModel):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPresetResponseTypeDef(BaseValidatorModel):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListPresetsResponseTypeDef(BaseValidatorModel):
    Presets: List[PresetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdatePresetResponseTypeDef(BaseValidatorModel):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JobSettingsTypeDef(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    AvailBlanking: Optional[AvailBlankingTypeDef] = None
    ColorConversion3DLUTSettings: Optional[Sequence[ColorConversion3DLUTSettingTypeDef]] = None
    Esam: Optional[EsamSettingsTypeDef] = None
    ExtendedDataServices: Optional[ExtendedDataServicesTypeDef] = None
    FollowSource: Optional[int] = None
    Inputs: Optional[Sequence[InputTypeDef]] = None
    KantarWatermark: Optional[KantarWatermarkSettingsTypeDef] = None
    MotionImageInserter: Optional[MotionImageInserterTypeDef] = None
    NielsenConfiguration: Optional[NielsenConfigurationTypeDef] = None
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettingsTypeDef] = None
    OutputGroups: Optional[Sequence[OutputGroupTypeDef]] = None
    TimecodeConfig: Optional[TimecodeConfigTypeDef] = None
    TimedMetadataInsertion: Optional[TimedMetadataInsertionTypeDef] = None


class JobTemplateSettingsTypeDef(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    AvailBlanking: Optional[AvailBlankingTypeDef] = None
    ColorConversion3DLUTSettings: Optional[Sequence[ColorConversion3DLUTSettingTypeDef]] = None
    Esam: Optional[EsamSettingsTypeDef] = None
    ExtendedDataServices: Optional[ExtendedDataServicesTypeDef] = None
    FollowSource: Optional[int] = None
    Inputs: Optional[Sequence[InputTemplateTypeDef]] = None
    KantarWatermark: Optional[KantarWatermarkSettingsTypeDef] = None
    MotionImageInserter: Optional[MotionImageInserterTypeDef] = None
    NielsenConfiguration: Optional[NielsenConfigurationTypeDef] = None
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettingsTypeDef] = None
    OutputGroups: Optional[Sequence[OutputGroupTypeDef]] = None
    TimecodeConfig: Optional[TimecodeConfigTypeDef] = None
    TimedMetadataInsertion: Optional[TimedMetadataInsertionTypeDef] = None


class PresetSettingsUnionTypeDef(BaseValidatorModel):
    pass


class CreatePresetRequestTypeDef(BaseValidatorModel):
    Name: str
    Settings: PresetSettingsUnionTypeDef
    Category: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdatePresetRequestTypeDef(BaseValidatorModel):
    Name: str
    Category: Optional[str] = None
    Description: Optional[str] = None
    Settings: Optional[PresetSettingsUnionTypeDef] = None


class JobMessagesTypeDef(BaseValidatorModel):
    pass


class JobTypeDef(BaseValidatorModel):
    Role: str
    Settings: JobSettingsOutputTypeDef
    AccelerationSettings: Optional[AccelerationSettingsTypeDef] = None
    AccelerationStatus: Optional[AccelerationStatusType] = None
    Arn: Optional[str] = None
    BillingTagsSource: Optional[BillingTagsSourceType] = None
    ClientRequestToken: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    CurrentPhase: Optional[JobPhaseType] = None
    ErrorCode: Optional[int] = None
    ErrorMessage: Optional[str] = None
    HopDestinations: Optional[List[HopDestinationTypeDef]] = None
    Id: Optional[str] = None
    JobEngineVersionRequested: Optional[str] = None
    JobEngineVersionUsed: Optional[str] = None
    JobPercentComplete: Optional[int] = None
    JobTemplate: Optional[str] = None
    Messages: Optional[JobMessagesTypeDef] = None
    OutputGroupDetails: Optional[List[OutputGroupDetailTypeDef]] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    QueueTransitions: Optional[List[QueueTransitionTypeDef]] = None
    RetryCount: Optional[int] = None
    SimulateReservedQueue: Optional[SimulateReservedQueueType] = None
    Status: Optional[JobStatusType] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None
    Timing: Optional[TimingTypeDef] = None
    UserMetadata: Optional[Dict[str, str]] = None
    Warnings: Optional[List[WarningGroupTypeDef]] = None


class CreateJobResponseTypeDef(BaseValidatorModel):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobResponseTypeDef(BaseValidatorModel):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class JobTemplateTypeDef(BaseValidatorModel):
    pass


class CreateJobTemplateResponseTypeDef(BaseValidatorModel):
    JobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobTemplateResponseTypeDef(BaseValidatorModel):
    JobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobTemplatesResponseTypeDef(BaseValidatorModel):
    JobTemplates: List[JobTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateJobTemplateResponseTypeDef(BaseValidatorModel):
    JobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JobSettingsUnionTypeDef(BaseValidatorModel):
    pass


class CreateJobRequestTypeDef(BaseValidatorModel):
    Role: str
    Settings: JobSettingsUnionTypeDef
    AccelerationSettings: Optional[AccelerationSettingsTypeDef] = None
    BillingTagsSource: Optional[BillingTagsSourceType] = None
    ClientRequestToken: Optional[str] = None
    HopDestinations: Optional[Sequence[HopDestinationTypeDef]] = None
    JobEngineVersion: Optional[str] = None
    JobTemplate: Optional[str] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    SimulateReservedQueue: Optional[SimulateReservedQueueType] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None
    Tags: Optional[Mapping[str, str]] = None
    UserMetadata: Optional[Mapping[str, str]] = None


class JobTemplateSettingsUnionTypeDef(BaseValidatorModel):
    pass


class CreateJobTemplateRequestTypeDef(BaseValidatorModel):
    Name: str
    Settings: JobTemplateSettingsUnionTypeDef
    AccelerationSettings: Optional[AccelerationSettingsTypeDef] = None
    Category: Optional[str] = None
    Description: Optional[str] = None
    HopDestinations: Optional[Sequence[HopDestinationTypeDef]] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateJobTemplateRequestTypeDef(BaseValidatorModel):
    Name: str
    AccelerationSettings: Optional[AccelerationSettingsTypeDef] = None
    Category: Optional[str] = None
    Description: Optional[str] = None
    HopDestinations: Optional[Sequence[HopDestinationTypeDef]] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    Settings: Optional[JobTemplateSettingsUnionTypeDef] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None


