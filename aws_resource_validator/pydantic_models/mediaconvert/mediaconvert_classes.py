from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mediaconvert.mediaconvert_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AacSettings(BaseValidatorModel):
    AudioDescriptionBroadcasterMix: Optional[AacAudioDescriptionBroadcasterMixType] = None
    Bitrate: Optional[int] = None
    CodecProfile: Optional[AacCodecProfileType] = None
    CodingMode: Optional[AacCodingModeType] = None
    RateControlMode: Optional[AacRateControlModeType] = None
    RawFormat: Optional[AacRawFormatType] = None
    SampleRate: Optional[int] = None
    Specification: Optional[AacSpecificationType] = None
    VbrQuality: Optional[AacVbrQualityType] = None


class Ac3Settings(BaseValidatorModel):
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


class AccelerationSettings(BaseValidatorModel):
    Mode: AccelerationModeType


class AdvancedInputFilterSettings(BaseValidatorModel):
    AddTexture: Optional[AdvancedInputFilterAddTextureType] = None
    Sharpening: Optional[AdvancedInputFilterSharpenType] = None


class AiffSettings(BaseValidatorModel):
    BitDepth: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None


class AllowedRenditionSize(BaseValidatorModel):
    Height: Optional[int] = None
    Required: Optional[RequiredFlagType] = None
    Width: Optional[int] = None


class AncillarySourceSettings(BaseValidatorModel):
    Convert608To708: Optional[AncillaryConvert608To708Type] = None
    SourceAncillaryChannelNumber: Optional[int] = None
    TerminateCaptions: Optional[AncillaryTerminateCaptionsType] = None


class AssociateCertificateRequest(BaseValidatorModel):
    Arn: str


class AudioChannelTaggingSettingsOutput(BaseValidatorModel):
    ChannelTag: Optional[AudioChannelTagType] = None
    ChannelTags: Optional[List[AudioChannelTagType]] = None


class AudioChannelTaggingSettings(BaseValidatorModel):
    ChannelTag: Optional[AudioChannelTagType] = None
    ChannelTags: Optional[List[AudioChannelTagType]] = None


class Eac3AtmosSettings(BaseValidatorModel):
    Bitrate: Optional[int] = None
    BitstreamMode: Optional[Literal['COMPLETE_MAIN']] = None
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


class Eac3Settings(BaseValidatorModel):
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


class FlacSettings(BaseValidatorModel):
    BitDepth: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None


class Mp2Settings(BaseValidatorModel):
    Bitrate: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None


class Mp3Settings(BaseValidatorModel):
    Bitrate: Optional[int] = None
    Channels: Optional[int] = None
    RateControlMode: Optional[Mp3RateControlModeType] = None
    SampleRate: Optional[int] = None
    VbrQuality: Optional[int] = None


class OpusSettings(BaseValidatorModel):
    Bitrate: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None


class VorbisSettings(BaseValidatorModel):
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None
    VbrQuality: Optional[int] = None


class WavSettings(BaseValidatorModel):
    BitDepth: Optional[int] = None
    Channels: Optional[int] = None
    Format: Optional[WavFormatType] = None
    SampleRate: Optional[int] = None


class AudioNormalizationSettings(BaseValidatorModel):
    Algorithm: Optional[AudioNormalizationAlgorithmType] = None
    AlgorithmControl: Optional[AudioNormalizationAlgorithmControlType] = None
    CorrectionGateLevel: Optional[int] = None
    LoudnessLogging: Optional[AudioNormalizationLoudnessLoggingType] = None
    PeakCalculation: Optional[AudioNormalizationPeakCalculationType] = None
    TargetLkfs: Optional[float] = None
    TruePeakLimiterThreshold: Optional[float] = None


class FrameRate(BaseValidatorModel):
    Denominator: Optional[int] = None
    Numerator: Optional[int] = None


class AudioSelectorGroupOutput(BaseValidatorModel):
    AudioSelectorNames: Optional[List[str]] = None


class AudioSelectorGroup(BaseValidatorModel):
    AudioSelectorNames: Optional[List[str]] = None


class HlsRenditionGroupSettings(BaseValidatorModel):
    RenditionGroupId: Optional[str] = None
    RenditionLanguageCode: Optional[LanguageCodeType] = None
    RenditionName: Optional[str] = None


class ForceIncludeRenditionSize(BaseValidatorModel):
    Height: Optional[int] = None
    Width: Optional[int] = None


class MinBottomRenditionSize(BaseValidatorModel):
    Height: Optional[int] = None
    Width: Optional[int] = None


class MinTopRenditionSize(BaseValidatorModel):
    Height: Optional[int] = None
    Width: Optional[int] = None


class Av1QvbrSettings(BaseValidatorModel):
    QvbrQualityLevel: Optional[int] = None
    QvbrQualityLevelFineTune: Optional[float] = None


class AvailBlanking(BaseValidatorModel):
    AvailBlankingImage: Optional[str] = None


class AvcIntraUhdSettings(BaseValidatorModel):
    QualityTuningLevel: Optional[AvcIntraUhdQualityTuningLevelType] = None


class BandwidthReductionFilter(BaseValidatorModel):
    Sharpening: Optional[BandwidthReductionFilterSharpeningType] = None
    Strength: Optional[BandwidthReductionFilterStrengthType] = None


class BurninDestinationSettings(BaseValidatorModel):
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


class CancelJobRequest(BaseValidatorModel):
    Id: str


class DvbSubDestinationSettings(BaseValidatorModel):
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


class EmbeddedDestinationSettings(BaseValidatorModel):
    Destination608ChannelNumber: Optional[int] = None
    Destination708ServiceNumber: Optional[int] = None


class ImscDestinationSettings(BaseValidatorModel):
    Accessibility: Optional[ImscAccessibilitySubsType] = None
    StylePassthrough: Optional[ImscStylePassthroughType] = None


class SccDestinationSettings(BaseValidatorModel):
    Framerate: Optional[SccDestinationFramerateType] = None


class SrtDestinationSettings(BaseValidatorModel):
    StylePassthrough: Optional[SrtStylePassthroughType] = None


class TeletextDestinationSettingsOutput(BaseValidatorModel):
    PageNumber: Optional[str] = None
    PageTypes: Optional[List[TeletextPageTypeType]] = None


class TtmlDestinationSettings(BaseValidatorModel):
    StylePassthrough: Optional[TtmlStylePassthroughType] = None


class WebvttDestinationSettings(BaseValidatorModel):
    Accessibility: Optional[WebvttAccessibilitySubsType] = None
    StylePassthrough: Optional[WebvttStylePassthroughType] = None


class TeletextDestinationSettings(BaseValidatorModel):
    PageNumber: Optional[str] = None
    PageTypes: Optional[List[TeletextPageTypeType]] = None


class CaptionSourceFramerate(BaseValidatorModel):
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None


class DvbSubSourceSettings(BaseValidatorModel):
    Pid: Optional[int] = None


class EmbeddedSourceSettings(BaseValidatorModel):
    Convert608To708: Optional[EmbeddedConvert608To708Type] = None
    Source608ChannelNumber: Optional[int] = None
    Source608TrackNumber: Optional[int] = None
    TerminateCaptions: Optional[EmbeddedTerminateCaptionsType] = None


class TeletextSourceSettings(BaseValidatorModel):
    PageNumber: Optional[str] = None


class TrackSourceSettings(BaseValidatorModel):
    TrackNumber: Optional[int] = None


class WebvttHlsSourceSettings(BaseValidatorModel):
    RenditionGroupId: Optional[str] = None
    RenditionLanguageCode: Optional[LanguageCodeType] = None
    RenditionName: Optional[str] = None


class OutputChannelMappingOutput(BaseValidatorModel):
    InputChannels: Optional[List[int]] = None
    InputChannelsFineTune: Optional[List[float]] = None


class OutputChannelMapping(BaseValidatorModel):
    InputChannels: Optional[List[int]] = None
    InputChannelsFineTune: Optional[List[float]] = None


class ClipLimits(BaseValidatorModel):
    MaximumRGBTolerance: Optional[int] = None
    MaximumYUV: Optional[int] = None
    MinimumRGBTolerance: Optional[int] = None
    MinimumYUV: Optional[int] = None


class CmafAdditionalManifestOutput(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class CmafAdditionalManifest(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class StaticKeyProvider(BaseValidatorModel):
    KeyFormat: Optional[str] = None
    KeyFormatVersions: Optional[str] = None
    StaticKeyValue: Optional[str] = None
    Url: Optional[str] = None


class CmafImageBasedTrickPlaySettings(BaseValidatorModel):
    IntervalCadence: Optional[CmafIntervalCadenceType] = None
    ThumbnailHeight: Optional[int] = None
    ThumbnailInterval: Optional[float] = None
    ThumbnailWidth: Optional[int] = None
    TileHeight: Optional[int] = None
    TileWidth: Optional[int] = None


class CmfcSettings(BaseValidatorModel):
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


class ColorConversion3DLUTSetting(BaseValidatorModel):
    FileInput: Optional[str] = None
    InputColorSpace: Optional[ColorSpaceType] = None
    InputMasteringLuminance: Optional[int] = None
    OutputColorSpace: Optional[ColorSpaceType] = None
    OutputMasteringLuminance: Optional[int] = None


class Hdr10Metadata(BaseValidatorModel):
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


class F4vSettings(BaseValidatorModel):
    MoovPlacement: Optional[F4vMoovPlacementType] = None


class M3u8SettingsOutput(BaseValidatorModel):
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


class MovSettings(BaseValidatorModel):
    ClapAtom: Optional[MovClapAtomType] = None
    CslgAtom: Optional[MovCslgAtomType] = None
    Mpeg2FourCCControl: Optional[MovMpeg2FourCCControlType] = None
    PaddingControl: Optional[MovPaddingControlType] = None
    Reference: Optional[MovReferenceType] = None


class Mp4Settings(BaseValidatorModel):
    AudioDuration: Optional[CmfcAudioDurationType] = None
    CslgAtom: Optional[Mp4CslgAtomType] = None
    CttsVersion: Optional[int] = None
    FreeSpaceBox: Optional[Mp4FreeSpaceBoxType] = None
    MoovPlacement: Optional[Mp4MoovPlacementType] = None
    Mp4MajorBrand: Optional[str] = None


class MpdSettings(BaseValidatorModel):
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


class M3u8Settings(BaseValidatorModel):
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


class HopDestination(BaseValidatorModel):
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    WaitMinutes: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ReservationPlanSettings(BaseValidatorModel):
    Commitment: Literal['ONE_YEAR']
    RenewalType: RenewalTypeType
    ReservedSlots: int


class DashAdditionalManifestOutput(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class DashAdditionalManifest(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class DashIsoImageBasedTrickPlaySettings(BaseValidatorModel):
    IntervalCadence: Optional[DashIsoIntervalCadenceType] = None
    ThumbnailHeight: Optional[int] = None
    ThumbnailInterval: Optional[float] = None
    ThumbnailWidth: Optional[int] = None
    TileHeight: Optional[int] = None
    TileWidth: Optional[int] = None


class DataProperties(BaseValidatorModel):
    LanguageCode: Optional[str] = None


class Deinterlacer(BaseValidatorModel):
    Algorithm: Optional[DeinterlaceAlgorithmType] = None
    Control: Optional[DeinterlacerControlType] = None
    Mode: Optional[DeinterlacerModeType] = None


class DeleteJobTemplateRequest(BaseValidatorModel):
    Name: str


class DeletePresetRequest(BaseValidatorModel):
    Name: str


class DeleteQueueRequest(BaseValidatorModel):
    Name: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeEndpointsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    Mode: Optional[DescribeEndpointsModeType] = None
    NextToken: Optional[str] = None


class Endpoint(BaseValidatorModel):
    Url: Optional[str] = None


class DisassociateCertificateRequest(BaseValidatorModel):
    Arn: str


class DolbyVisionLevel6Metadata(BaseValidatorModel):
    MaxCll: Optional[int] = None
    MaxFall: Optional[int] = None


class DvbNitSettings(BaseValidatorModel):
    NetworkId: Optional[int] = None
    NetworkName: Optional[str] = None
    NitInterval: Optional[int] = None


class DvbSdtSettings(BaseValidatorModel):
    OutputSdt: Optional[OutputSdtType] = None
    SdtInterval: Optional[int] = None
    ServiceName: Optional[str] = None
    ServiceProviderName: Optional[str] = None


class DvbTdtSettings(BaseValidatorModel):
    TdtInterval: Optional[int] = None


class DynamicAudioSelector(BaseValidatorModel):
    AudioDurationCorrection: Optional[AudioDurationCorrectionType] = None
    ExternalAudioFileInput: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Offset: Optional[int] = None
    SelectorType: Optional[DynamicAudioSelectorTypeType] = None


class EncryptionContractConfiguration(BaseValidatorModel):
    SpekeAudioPreset: Optional[PresetSpeke20AudioType] = None
    SpekeVideoPreset: Optional[PresetSpeke20VideoType] = None


class EsamManifestConfirmConditionNotification(BaseValidatorModel):
    MccXml: Optional[str] = None


class EsamSignalProcessingNotification(BaseValidatorModel):
    SccXml: Optional[str] = None


class ExtendedDataServices(BaseValidatorModel):
    CopyProtectionAction: Optional[CopyProtectionActionType] = None
    VchipAction: Optional[VchipActionType] = None


class FrameCaptureSettings(BaseValidatorModel):
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    MaxCaptures: Optional[int] = None
    Quality: Optional[int] = None


class GetJobRequest(BaseValidatorModel):
    Id: str


class GetJobTemplateRequest(BaseValidatorModel):
    Name: str


class Policy(BaseValidatorModel):
    HttpInputs: Optional[InputPolicyType] = None
    HttpsInputs: Optional[InputPolicyType] = None
    S3Inputs: Optional[InputPolicyType] = None


class GetPresetRequest(BaseValidatorModel):
    Name: str


class GetQueueRequest(BaseValidatorModel):
    Name: str


class GifSettings(BaseValidatorModel):
    FramerateControl: Optional[GifFramerateControlType] = None
    FramerateConversionAlgorithm: Optional[GifFramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None


class H264QvbrSettings(BaseValidatorModel):
    MaxAverageBitrate: Optional[int] = None
    QvbrQualityLevel: Optional[int] = None
    QvbrQualityLevelFineTune: Optional[float] = None


class H265QvbrSettings(BaseValidatorModel):
    MaxAverageBitrate: Optional[int] = None
    QvbrQualityLevel: Optional[int] = None
    QvbrQualityLevelFineTune: Optional[float] = None


class Hdr10Plus(BaseValidatorModel):
    MasteringMonitorNits: Optional[int] = None
    TargetMonitorNits: Optional[int] = None


class HlsAdditionalManifestOutput(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class HlsAdditionalManifest(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class HlsCaptionLanguageMapping(BaseValidatorModel):
    CaptionChannel: Optional[int] = None
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None


class HlsImageBasedTrickPlaySettings(BaseValidatorModel):
    IntervalCadence: Optional[HlsIntervalCadenceType] = None
    ThumbnailHeight: Optional[int] = None
    ThumbnailInterval: Optional[float] = None
    ThumbnailWidth: Optional[int] = None
    TileHeight: Optional[int] = None
    TileWidth: Optional[int] = None


class HlsSettings(BaseValidatorModel):
    AudioGroupId: Optional[str] = None
    AudioOnlyContainer: Optional[HlsAudioOnlyContainerType] = None
    AudioRenditionSets: Optional[str] = None
    AudioTrackType: Optional[HlsAudioTrackTypeType] = None
    DescriptiveVideoServiceFlag: Optional[HlsDescriptiveVideoServiceFlagType] = None
    IFrameOnlyManifest: Optional[HlsIFrameOnlyManifestType] = None
    SegmentModifier: Optional[str] = None


class Id3Insertion(BaseValidatorModel):
    Id3: Optional[str] = None
    Timecode: Optional[str] = None


class InsertableImage(BaseValidatorModel):
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


class InputClipping(BaseValidatorModel):
    EndTimecode: Optional[str] = None
    StartTimecode: Optional[str] = None


class InputDecryptionSettings(BaseValidatorModel):
    DecryptionMode: Optional[DecryptionModeType] = None
    EncryptedDecryptionKey: Optional[str] = None
    InitializationVector: Optional[str] = None
    KmsKeyRegion: Optional[str] = None


class InputVideoGenerator(BaseValidatorModel):
    Channels: Optional[int] = None
    Duration: Optional[int] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    SampleRate: Optional[int] = None


class Rectangle(BaseValidatorModel):
    Height: Optional[int] = None
    Width: Optional[int] = None
    X: Optional[int] = None
    Y: Optional[int] = None


class JobEngineVersion(BaseValidatorModel):
    ExpirationDate: Optional[datetime] = None
    Version: Optional[str] = None


class JobMessages(BaseValidatorModel):
    Info: Optional[List[str]] = None
    Warning: Optional[List[str]] = None


class KantarWatermarkSettings(BaseValidatorModel):
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


class NielsenConfiguration(BaseValidatorModel):
    BreakoutCode: Optional[int] = None
    DistributorId: Optional[str] = None


class NielsenNonLinearWatermarkSettings(BaseValidatorModel):
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


class TimecodeConfig(BaseValidatorModel):
    Anchor: Optional[str] = None
    Source: Optional[TimecodeSourceType] = None
    Start: Optional[str] = None
    TimestampOffset: Optional[str] = None


class QueueTransition(BaseValidatorModel):
    DestinationQueue: Optional[str] = None
    SourceQueue: Optional[str] = None
    Timestamp: Optional[datetime] = None


class Timing(BaseValidatorModel):
    FinishTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    SubmitTime: Optional[datetime] = None


class WarningGroup(BaseValidatorModel):
    Code: int
    Count: int


class ListJobTemplatesRequest(BaseValidatorModel):
    Category: Optional[str] = None
    ListBy: Optional[JobTemplateListByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None


class ListJobsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None


class ListPresetsRequest(BaseValidatorModel):
    Category: Optional[str] = None
    ListBy: Optional[PresetListByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None


class ListQueuesRequest(BaseValidatorModel):
    ListBy: Optional[QueueListByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    Arn: str


class ResourceTags(BaseValidatorModel):
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ListVersionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class M2tsScte35Esam(BaseValidatorModel):
    Scte35EsamPid: Optional[int] = None


class Metadata(BaseValidatorModel):
    ETag: Optional[str] = None
    FileSize: Optional[int] = None
    LastModified: Optional[datetime] = None
    MimeType: Optional[str] = None


class MotionImageInsertionFramerate(BaseValidatorModel):
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None


class MotionImageInsertionOffset(BaseValidatorModel):
    ImageX: Optional[int] = None
    ImageY: Optional[int] = None


class Mpeg2Settings(BaseValidatorModel):
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


class MsSmoothAdditionalManifestOutput(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class MsSmoothAdditionalManifest(BaseValidatorModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None


class MxfXavcProfileSettings(BaseValidatorModel):
    DurationMode: Optional[MxfXavcDurationModeType] = None
    MaxAncDataSize: Optional[int] = None


class NexGuardFileMarkerSettings(BaseValidatorModel):
    License: Optional[str] = None
    Payload: Optional[int] = None
    Preset: Optional[str] = None
    Strength: Optional[WatermarkingStrengthType] = None


class NoiseReducerFilterSettings(BaseValidatorModel):
    Strength: Optional[int] = None


class NoiseReducerSpatialFilterSettings(BaseValidatorModel):
    PostFilterSharpenStrength: Optional[int] = None
    Speed: Optional[int] = None
    Strength: Optional[int] = None


class NoiseReducerTemporalFilterSettings(BaseValidatorModel):
    AggressiveMode: Optional[int] = None
    PostTemporalSharpening: Optional[NoiseFilterPostTemporalSharpeningType] = None
    PostTemporalSharpeningStrength: Optional[NoiseFilterPostTemporalSharpeningStrengthType] = None
    Speed: Optional[int] = None
    Strength: Optional[int] = None


class VideoDetail(BaseValidatorModel):
    HeightInPx: Optional[int] = None
    WidthInPx: Optional[int] = None


class ProbeInputFile(BaseValidatorModel):
    FileUrl: Optional[str] = None


class TrackMapping(BaseValidatorModel):
    AudioTrackIndexes: Optional[List[int]] = None
    DataTrackIndexes: Optional[List[int]] = None
    VideoTrackIndexes: Optional[List[int]] = None


class ProresSettings(BaseValidatorModel):
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


class ReservationPlan(BaseValidatorModel):
    Commitment: Optional[Literal['ONE_YEAR']] = None
    ExpiresAt: Optional[datetime] = None
    PurchasedAt: Optional[datetime] = None
    RenewalType: Optional[RenewalTypeType] = None
    ReservedSlots: Optional[int] = None
    Status: Optional[ReservationPlanStatusType] = None


class ServiceOverride(BaseValidatorModel):
    Message: Optional[str] = None
    Name: Optional[str] = None
    OverrideValue: Optional[str] = None
    Value: Optional[str] = None


class S3DestinationAccessControl(BaseValidatorModel):
    CannedAcl: Optional[S3ObjectCannedAclType] = None


class S3EncryptionSettings(BaseValidatorModel):
    EncryptionType: Optional[S3ServerSideEncryptionTypeType] = None
    KmsEncryptionContext: Optional[str] = None
    KmsKeyArn: Optional[str] = None


class SearchJobsRequest(BaseValidatorModel):
    InputFile: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None


class TagResourceRequest(BaseValidatorModel):
    Arn: str
    Tags: Dict[str, str]


class TimecodeBurnin(BaseValidatorModel):
    FontSize: Optional[int] = None
    Position: Optional[TimecodeBurninPositionType] = None
    Prefix: Optional[str] = None


class UncompressedSettings(BaseValidatorModel):
    Fourcc: Optional[UncompressedFourccType] = None
    FramerateControl: Optional[UncompressedFramerateControlType] = None
    FramerateConversionAlgorithm: Optional[UncompressedFramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    InterlaceMode: Optional[UncompressedInterlaceModeType] = None
    ScanTypeConversionMode: Optional[UncompressedScanTypeConversionModeType] = None
    SlowPal: Optional[UncompressedSlowPalType] = None
    Telecine: Optional[UncompressedTelecineType] = None


class UntagResourceRequest(BaseValidatorModel):
    Arn: str
    TagKeys: Optional[List[str]] = None


class Vc3Settings(BaseValidatorModel):
    FramerateControl: Optional[Vc3FramerateControlType] = None
    FramerateConversionAlgorithm: Optional[Vc3FramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    InterlaceMode: Optional[Vc3InterlaceModeType] = None
    ScanTypeConversionMode: Optional[Vc3ScanTypeConversionModeType] = None
    SlowPal: Optional[Vc3SlowPalType] = None
    Telecine: Optional[Vc3TelecineType] = None
    Vc3Class: Optional[Vc3ClassType] = None


class Vp8Settings(BaseValidatorModel):
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
    RateControlMode: Optional[Literal['VBR']] = None


class Vp9Settings(BaseValidatorModel):
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
    RateControlMode: Optional[Literal['VBR']] = None


class VideoOverlayInputClipping(BaseValidatorModel):
    EndTimecode: Optional[str] = None
    StartTimecode: Optional[str] = None


class VideoOverlayPosition(BaseValidatorModel):
    Height: Optional[int] = None
    Unit: Optional[VideoOverlayUnitType] = None
    Width: Optional[int] = None
    XPosition: Optional[int] = None
    YPosition: Optional[int] = None


class Xavc4kIntraCbgProfileSettings(BaseValidatorModel):
    XavcClass: Optional[Xavc4kIntraCbgProfileClassType] = None


class Xavc4kIntraVbrProfileSettings(BaseValidatorModel):
    XavcClass: Optional[Xavc4kIntraVbrProfileClassType] = None


class Xavc4kProfileSettings(BaseValidatorModel):
    BitrateClass: Optional[Xavc4kProfileBitrateClassType] = None
    CodecProfile: Optional[Xavc4kProfileCodecProfileType] = None
    FlickerAdaptiveQuantization: Optional[XavcFlickerAdaptiveQuantizationType] = None
    GopBReference: Optional[XavcGopBReferenceType] = None
    GopClosedCadence: Optional[int] = None
    HrdBufferSize: Optional[int] = None
    QualityTuningLevel: Optional[Xavc4kProfileQualityTuningLevelType] = None
    Slices: Optional[int] = None


class XavcHdIntraCbgProfileSettings(BaseValidatorModel):
    XavcClass: Optional[XavcHdIntraCbgProfileClassType] = None


class XavcHdProfileSettings(BaseValidatorModel):
    BitrateClass: Optional[XavcHdProfileBitrateClassType] = None
    FlickerAdaptiveQuantization: Optional[XavcFlickerAdaptiveQuantizationType] = None
    GopBReference: Optional[XavcGopBReferenceType] = None
    GopClosedCadence: Optional[int] = None
    HrdBufferSize: Optional[int] = None
    InterlaceMode: Optional[XavcInterlaceModeType] = None
    QualityTuningLevel: Optional[XavcHdProfileQualityTuningLevelType] = None
    Slices: Optional[int] = None
    Telecine: Optional[XavcHdProfileTelecineType] = None


class AudioCodecSettings(BaseValidatorModel):
    AacSettings: Optional[AacSettings] = None
    Ac3Settings: Optional[Ac3Settings] = None
    AiffSettings: Optional[AiffSettings] = None
    Codec: Optional[AudioCodecType] = None
    Eac3AtmosSettings: Optional[Eac3AtmosSettings] = None
    Eac3Settings: Optional[Eac3Settings] = None
    FlacSettings: Optional[FlacSettings] = None
    Mp2Settings: Optional[Mp2Settings] = None
    Mp3Settings: Optional[Mp3Settings] = None
    OpusSettings: Optional[OpusSettings] = None
    VorbisSettings: Optional[VorbisSettings] = None
    WavSettings: Optional[WavSettings] = None


class AudioProperties(BaseValidatorModel):
    BitDepth: Optional[int] = None
    BitRate: Optional[int] = None
    Channels: Optional[int] = None
    FrameRate: Optional[FrameRate] = None
    LanguageCode: Optional[str] = None
    SampleRate: Optional[int] = None


class VideoProperties(BaseValidatorModel):
    BitDepth: Optional[int] = None
    BitRate: Optional[int] = None
    ColorPrimaries: Optional[ColorPrimariesType] = None
    FrameRate: Optional[FrameRate] = None
    Height: Optional[int] = None
    MatrixCoefficients: Optional[MatrixCoefficientsType] = None
    TransferCharacteristics: Optional[TransferCharacteristicsType] = None
    Width: Optional[int] = None


class AutomatedAbrRuleOutput(BaseValidatorModel):
    AllowedRenditions: Optional[List[AllowedRenditionSize]] = None
    ForceIncludeRenditions: Optional[List[ForceIncludeRenditionSize]] = None
    MinBottomRenditionSize: Optional[MinBottomRenditionSize] = None
    MinTopRenditionSize: Optional[MinTopRenditionSize] = None
    Type: Optional[RuleTypeType] = None


class AutomatedAbrRule(BaseValidatorModel):
    AllowedRenditions: Optional[List[AllowedRenditionSize]] = None
    ForceIncludeRenditions: Optional[List[ForceIncludeRenditionSize]] = None
    MinBottomRenditionSize: Optional[MinBottomRenditionSize] = None
    MinTopRenditionSize: Optional[MinTopRenditionSize] = None
    Type: Optional[RuleTypeType] = None


class Av1Settings(BaseValidatorModel):
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
    QvbrSettings: Optional[Av1QvbrSettings] = None
    RateControlMode: Optional[Literal['QVBR']] = None
    Slices: Optional[int] = None
    SpatialAdaptiveQuantization: Optional[Av1SpatialAdaptiveQuantizationType] = None


class AvcIntraSettings(BaseValidatorModel):
    AvcIntraClass: Optional[AvcIntraClassType] = None
    AvcIntraUhdSettings: Optional[AvcIntraUhdSettings] = None
    FramerateControl: Optional[AvcIntraFramerateControlType] = None
    FramerateConversionAlgorithm: Optional[AvcIntraFramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    InterlaceMode: Optional[AvcIntraInterlaceModeType] = None
    ScanTypeConversionMode: Optional[AvcIntraScanTypeConversionModeType] = None
    SlowPal: Optional[AvcIntraSlowPalType] = None
    Telecine: Optional[AvcIntraTelecineType] = None


class CaptionDestinationSettingsOutput(BaseValidatorModel):
    BurninDestinationSettings: Optional[BurninDestinationSettings] = None
    DestinationType: Optional[CaptionDestinationTypeType] = None
    DvbSubDestinationSettings: Optional[DvbSubDestinationSettings] = None
    EmbeddedDestinationSettings: Optional[EmbeddedDestinationSettings] = None
    ImscDestinationSettings: Optional[ImscDestinationSettings] = None
    SccDestinationSettings: Optional[SccDestinationSettings] = None
    SrtDestinationSettings: Optional[SrtDestinationSettings] = None
    TeletextDestinationSettings: Optional[TeletextDestinationSettingsOutput] = None
    TtmlDestinationSettings: Optional[TtmlDestinationSettings] = None
    WebvttDestinationSettings: Optional[WebvttDestinationSettings] = None


class CaptionDestinationSettings(BaseValidatorModel):
    BurninDestinationSettings: Optional[BurninDestinationSettings] = None
    DestinationType: Optional[CaptionDestinationTypeType] = None
    DvbSubDestinationSettings: Optional[DvbSubDestinationSettings] = None
    EmbeddedDestinationSettings: Optional[EmbeddedDestinationSettings] = None
    ImscDestinationSettings: Optional[ImscDestinationSettings] = None
    SccDestinationSettings: Optional[SccDestinationSettings] = None
    SrtDestinationSettings: Optional[SrtDestinationSettings] = None
    TeletextDestinationSettings: Optional[TeletextDestinationSettings] = None
    TtmlDestinationSettings: Optional[TtmlDestinationSettings] = None
    WebvttDestinationSettings: Optional[WebvttDestinationSettings] = None


class FileSourceSettings(BaseValidatorModel):
    ByteRateLimit: Optional[CaptionSourceByteRateLimitType] = None
    Convert608To708: Optional[FileSourceConvert608To708Type] = None
    ConvertPaintToPop: Optional[CaptionSourceConvertPaintOnToPopOnType] = None
    Framerate: Optional[CaptionSourceFramerate] = None
    SourceFile: Optional[str] = None
    TimeDelta: Optional[int] = None
    TimeDeltaUnits: Optional[FileSourceTimeDeltaUnitsType] = None


class ChannelMappingOutput(BaseValidatorModel):
    OutputChannels: Optional[List[OutputChannelMappingOutput]] = None


class ChannelMapping(BaseValidatorModel):
    OutputChannels: Optional[List[OutputChannelMapping]] = None


class ColorCorrector(BaseValidatorModel):
    Brightness: Optional[int] = None
    ClipLimits: Optional[ClipLimits] = None
    ColorSpaceConversion: Optional[ColorSpaceConversionType] = None
    Contrast: Optional[int] = None
    Hdr10Metadata: Optional[Hdr10Metadata] = None
    HdrToSdrToneMapper: Optional[HDRToSDRToneMapperType] = None
    Hue: Optional[int] = None
    MaxLuminance: Optional[int] = None
    SampleRangeConversion: Optional[SampleRangeConversionType] = None
    Saturation: Optional[int] = None
    SdrReferenceWhiteLevel: Optional[int] = None


class VideoSelector(BaseValidatorModel):
    AlphaBehavior: Optional[AlphaBehaviorType] = None
    ColorSpace: Optional[ColorSpaceType] = None
    ColorSpaceUsage: Optional[ColorSpaceUsageType] = None
    EmbeddedTimecodeOverride: Optional[EmbeddedTimecodeOverrideType] = None
    Hdr10Metadata: Optional[Hdr10Metadata] = None
    MaxLuminance: Optional[int] = None
    PadVideo: Optional[PadVideoType] = None
    Pid: Optional[int] = None
    ProgramNumber: Optional[int] = None
    Rotate: Optional[InputRotateType] = None
    SampleRange: Optional[InputSampleRangeType] = None


class CreateQueueRequest(BaseValidatorModel):
    Name: str
    ConcurrentJobs: Optional[int] = None
    Description: Optional[str] = None
    PricingPlan: Optional[PricingPlanType] = None
    ReservationPlanSettings: Optional[ReservationPlanSettings] = None
    Status: Optional[QueueStatusType] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateQueueRequest(BaseValidatorModel):
    Name: str
    ConcurrentJobs: Optional[int] = None
    Description: Optional[str] = None
    ReservationPlanSettings: Optional[ReservationPlanSettings] = None
    Status: Optional[QueueStatusType] = None


class DescribeEndpointsRequestPaginate(BaseValidatorModel):
    Mode: Optional[DescribeEndpointsModeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobTemplatesRequestPaginate(BaseValidatorModel):
    Category: Optional[str] = None
    ListBy: Optional[JobTemplateListByType] = None
    Order: Optional[OrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsRequestPaginate(BaseValidatorModel):
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPresetsRequestPaginate(BaseValidatorModel):
    Category: Optional[str] = None
    ListBy: Optional[PresetListByType] = None
    Order: Optional[OrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueuesRequestPaginate(BaseValidatorModel):
    ListBy: Optional[QueueListByType] = None
    Order: Optional[OrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVersionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchJobsRequestPaginate(BaseValidatorModel):
    InputFile: Optional[str] = None
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEndpointsResponse(BaseValidatorModel):
    Endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DolbyVision(BaseValidatorModel):
    L6Metadata: Optional[DolbyVisionLevel6Metadata] = None
    L6Mode: Optional[DolbyVisionLevel6ModeType] = None
    Mapping: Optional[DolbyVisionMappingType] = None
    Profile: Optional[DolbyVisionProfileType] = None


class SpekeKeyProviderCmafOutput(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    DashSignaledSystemIds: Optional[List[str]] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfiguration] = None
    HlsSignaledSystemIds: Optional[List[str]] = None
    ResourceId: Optional[str] = None
    Url: Optional[str] = None


class SpekeKeyProviderCmaf(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    DashSignaledSystemIds: Optional[List[str]] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfiguration] = None
    HlsSignaledSystemIds: Optional[List[str]] = None
    ResourceId: Optional[str] = None
    Url: Optional[str] = None


class SpekeKeyProviderOutput(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfiguration] = None
    ResourceId: Optional[str] = None
    SystemIds: Optional[List[str]] = None
    Url: Optional[str] = None


class SpekeKeyProvider(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfiguration] = None
    ResourceId: Optional[str] = None
    SystemIds: Optional[List[str]] = None
    Url: Optional[str] = None


class EsamSettings(BaseValidatorModel):
    ManifestConfirmConditionNotification: Optional[EsamManifestConfirmConditionNotification] = None
    ResponseSignalPreroll: Optional[int] = None
    SignalProcessingNotification: Optional[EsamSignalProcessingNotification] = None


class GetPolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


class PutPolicyRequest(BaseValidatorModel):
    Policy: Policy


class PutPolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


class H264Settings(BaseValidatorModel):
    AdaptiveQuantization: Optional[H264AdaptiveQuantizationType] = None
    BandwidthReductionFilter: Optional[BandwidthReductionFilter] = None
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
    QvbrSettings: Optional[H264QvbrSettings] = None
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


class H265Settings(BaseValidatorModel):
    AdaptiveQuantization: Optional[H265AdaptiveQuantizationType] = None
    AlternateTransferFunctionSei: Optional[H265AlternateTransferFunctionSeiType] = None
    BandwidthReductionFilter: Optional[BandwidthReductionFilter] = None
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
    QvbrSettings: Optional[H265QvbrSettings] = None
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


class OutputSettings(BaseValidatorModel):
    HlsSettings: Optional[HlsSettings] = None


class TimedMetadataInsertionOutput(BaseValidatorModel):
    Id3Insertions: Optional[List[Id3Insertion]] = None


class TimedMetadataInsertion(BaseValidatorModel):
    Id3Insertions: Optional[List[Id3Insertion]] = None


class ImageInserterOutput(BaseValidatorModel):
    InsertableImages: Optional[List[InsertableImage]] = None
    SdrReferenceWhiteLevel: Optional[int] = None


class ImageInserter(BaseValidatorModel):
    InsertableImages: Optional[List[InsertableImage]] = None
    SdrReferenceWhiteLevel: Optional[int] = None


class ListVersionsResponse(BaseValidatorModel):
    Versions: List[JobEngineVersion]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceTags: ResourceTags
    ResponseMetadata: ResponseMetadata


class M2tsSettingsOutput(BaseValidatorModel):
    AudioBufferModel: Optional[M2tsAudioBufferModelType] = None
    AudioDuration: Optional[M2tsAudioDurationType] = None
    AudioFramesPerPes: Optional[int] = None
    AudioPids: Optional[List[int]] = None
    Bitrate: Optional[int] = None
    BufferModel: Optional[M2tsBufferModelType] = None
    DataPTSControl: Optional[M2tsDataPtsControlType] = None
    DvbNitSettings: Optional[DvbNitSettings] = None
    DvbSdtSettings: Optional[DvbSdtSettings] = None
    DvbSubPids: Optional[List[int]] = None
    DvbTdtSettings: Optional[DvbTdtSettings] = None
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
    Scte35Esam: Optional[M2tsScte35Esam] = None
    Scte35Pid: Optional[int] = None
    Scte35Source: Optional[M2tsScte35SourceType] = None
    SegmentationMarkers: Optional[M2tsSegmentationMarkersType] = None
    SegmentationStyle: Optional[M2tsSegmentationStyleType] = None
    SegmentationTime: Optional[float] = None
    TimedMetadataPid: Optional[int] = None
    TransportStreamId: Optional[int] = None
    VideoPid: Optional[int] = None


class M2tsSettings(BaseValidatorModel):
    AudioBufferModel: Optional[M2tsAudioBufferModelType] = None
    AudioDuration: Optional[M2tsAudioDurationType] = None
    AudioFramesPerPes: Optional[int] = None
    AudioPids: Optional[List[int]] = None
    Bitrate: Optional[int] = None
    BufferModel: Optional[M2tsBufferModelType] = None
    DataPTSControl: Optional[M2tsDataPtsControlType] = None
    DvbNitSettings: Optional[DvbNitSettings] = None
    DvbSdtSettings: Optional[DvbSdtSettings] = None
    DvbSubPids: Optional[List[int]] = None
    DvbTdtSettings: Optional[DvbTdtSettings] = None
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
    Scte35Esam: Optional[M2tsScte35Esam] = None
    Scte35Pid: Optional[int] = None
    Scte35Source: Optional[M2tsScte35SourceType] = None
    SegmentationMarkers: Optional[M2tsSegmentationMarkersType] = None
    SegmentationStyle: Optional[M2tsSegmentationStyleType] = None
    SegmentationTime: Optional[float] = None
    TimedMetadataPid: Optional[int] = None
    TransportStreamId: Optional[int] = None
    VideoPid: Optional[int] = None


class MotionImageInserter(BaseValidatorModel):
    Framerate: Optional[MotionImageInsertionFramerate] = None
    Input: Optional[str] = None
    InsertionMode: Optional[MotionImageInsertionModeType] = None
    Offset: Optional[MotionImageInsertionOffset] = None
    Playback: Optional[MotionImagePlaybackType] = None
    StartTime: Optional[str] = None


class MxfSettings(BaseValidatorModel):
    AfdSignaling: Optional[MxfAfdSignalingType] = None
    Profile: Optional[MxfProfileType] = None
    XavcProfileSettings: Optional[MxfXavcProfileSettings] = None


class PartnerWatermarking(BaseValidatorModel):
    NexguardFileMarkerSettings: Optional[NexGuardFileMarkerSettings] = None


class NoiseReducer(BaseValidatorModel):
    Filter: Optional[NoiseReducerFilterType] = None
    FilterSettings: Optional[NoiseReducerFilterSettings] = None
    SpatialFilterSettings: Optional[NoiseReducerSpatialFilterSettings] = None
    TemporalFilterSettings: Optional[NoiseReducerTemporalFilterSettings] = None


class OutputDetail(BaseValidatorModel):
    DurationInMs: Optional[int] = None
    VideoDetails: Optional[VideoDetail] = None


class ProbeRequest(BaseValidatorModel):
    InputFiles: Optional[List[ProbeInputFile]] = None


class Queue(BaseValidatorModel):
    Name: str
    Arn: Optional[str] = None
    ConcurrentJobs: Optional[int] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None
    PricingPlan: Optional[PricingPlanType] = None
    ProgressingJobsCount: Optional[int] = None
    ReservationPlan: Optional[ReservationPlan] = None
    ServiceOverrides: Optional[List[ServiceOverride]] = None
    Status: Optional[QueueStatusType] = None
    SubmittedJobsCount: Optional[int] = None
    Type: Optional[TypeType] = None


class S3DestinationSettings(BaseValidatorModel):
    AccessControl: Optional[S3DestinationAccessControl] = None
    Encryption: Optional[S3EncryptionSettings] = None
    StorageClass: Optional[S3StorageClassType] = None


class VideoOverlayInputOutput(BaseValidatorModel):
    FileInput: Optional[str] = None
    InputClippings: Optional[List[VideoOverlayInputClipping]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None


class VideoOverlayInput(BaseValidatorModel):
    FileInput: Optional[str] = None
    InputClippings: Optional[List[VideoOverlayInputClipping]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None


class VideoOverlayTransition(BaseValidatorModel):
    EndPosition: Optional[VideoOverlayPosition] = None
    EndTimecode: Optional[str] = None
    StartTimecode: Optional[str] = None


class XavcSettings(BaseValidatorModel):
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
    Xavc4kIntraCbgProfileSettings: Optional[Xavc4kIntraCbgProfileSettings] = None
    Xavc4kIntraVbrProfileSettings: Optional[Xavc4kIntraVbrProfileSettings] = None
    Xavc4kProfileSettings: Optional[Xavc4kProfileSettings] = None
    XavcHdIntraCbgProfileSettings: Optional[XavcHdIntraCbgProfileSettings] = None
    XavcHdProfileSettings: Optional[XavcHdProfileSettings] = None


class Track(BaseValidatorModel):
    AudioProperties: Optional[AudioProperties] = None
    Codec: Optional[CodecType] = None
    DataProperties: Optional[DataProperties] = None
    Duration: Optional[float] = None
    Index: Optional[int] = None
    TrackType: Optional[TrackTypeType] = None
    VideoProperties: Optional[VideoProperties] = None


class AutomatedAbrSettingsOutput(BaseValidatorModel):
    MaxAbrBitrate: Optional[int] = None
    MaxRenditions: Optional[int] = None
    MinAbrBitrate: Optional[int] = None
    Rules: Optional[List[AutomatedAbrRuleOutput]] = None


class AutomatedAbrSettings(BaseValidatorModel):
    MaxAbrBitrate: Optional[int] = None
    MaxRenditions: Optional[int] = None
    MinAbrBitrate: Optional[int] = None
    Rules: Optional[List[AutomatedAbrRule]] = None


class CaptionDescriptionOutput(BaseValidatorModel):
    CaptionSelectorName: Optional[str] = None
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettingsOutput] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None


class CaptionDescriptionPresetOutput(BaseValidatorModel):
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettingsOutput] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None


class CaptionDescriptionPreset(BaseValidatorModel):
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettings] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None


class CaptionDescription(BaseValidatorModel):
    CaptionSelectorName: Optional[str] = None
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettings] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None


class CaptionSourceSettings(BaseValidatorModel):
    AncillarySourceSettings: Optional[AncillarySourceSettings] = None
    DvbSubSourceSettings: Optional[DvbSubSourceSettings] = None
    EmbeddedSourceSettings: Optional[EmbeddedSourceSettings] = None
    FileSourceSettings: Optional[FileSourceSettings] = None
    SourceType: Optional[CaptionSourceTypeType] = None
    TeletextSourceSettings: Optional[TeletextSourceSettings] = None
    TrackSourceSettings: Optional[TrackSourceSettings] = None
    WebvttHlsSourceSettings: Optional[WebvttHlsSourceSettings] = None


class RemixSettingsOutput(BaseValidatorModel):
    AudioDescriptionAudioChannel: Optional[int] = None
    AudioDescriptionDataChannel: Optional[int] = None
    ChannelMapping: Optional[ChannelMappingOutput] = None
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None


class RemixSettings(BaseValidatorModel):
    AudioDescriptionAudioChannel: Optional[int] = None
    AudioDescriptionDataChannel: Optional[int] = None
    ChannelMapping: Optional[ChannelMapping] = None
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None


class CmafEncryptionSettingsOutput(BaseValidatorModel):
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionTypeType] = None
    InitializationVectorInManifest: Optional[CmafInitializationVectorInManifestType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderCmafOutput] = None
    StaticKeyProvider: Optional[StaticKeyProvider] = None
    Type: Optional[CmafKeyProviderTypeType] = None


class CmafEncryptionSettings(BaseValidatorModel):
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionTypeType] = None
    InitializationVectorInManifest: Optional[CmafInitializationVectorInManifestType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderCmaf] = None
    StaticKeyProvider: Optional[StaticKeyProvider] = None
    Type: Optional[CmafKeyProviderTypeType] = None


class DashIsoEncryptionSettingsOutput(BaseValidatorModel):
    PlaybackDeviceCompatibility: Optional[DashIsoPlaybackDeviceCompatibilityType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderOutput] = None


class HlsEncryptionSettingsOutput(BaseValidatorModel):
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[HlsEncryptionTypeType] = None
    InitializationVectorInManifest: Optional[HlsInitializationVectorInManifestType] = None
    OfflineEncrypted: Optional[HlsOfflineEncryptedType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderOutput] = None
    StaticKeyProvider: Optional[StaticKeyProvider] = None
    Type: Optional[HlsKeyProviderTypeType] = None


class MsSmoothEncryptionSettingsOutput(BaseValidatorModel):
    SpekeKeyProvider: Optional[SpekeKeyProviderOutput] = None


class DashIsoEncryptionSettings(BaseValidatorModel):
    PlaybackDeviceCompatibility: Optional[DashIsoPlaybackDeviceCompatibilityType] = None
    SpekeKeyProvider: Optional[SpekeKeyProvider] = None


class HlsEncryptionSettings(BaseValidatorModel):
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[HlsEncryptionTypeType] = None
    InitializationVectorInManifest: Optional[HlsInitializationVectorInManifestType] = None
    OfflineEncrypted: Optional[HlsOfflineEncryptedType] = None
    SpekeKeyProvider: Optional[SpekeKeyProvider] = None
    StaticKeyProvider: Optional[StaticKeyProvider] = None
    Type: Optional[HlsKeyProviderTypeType] = None


class MsSmoothEncryptionSettings(BaseValidatorModel):
    SpekeKeyProvider: Optional[SpekeKeyProvider] = None


class ContainerSettingsOutput(BaseValidatorModel):
    CmfcSettings: Optional[CmfcSettings] = None
    Container: Optional[ContainerTypeType] = None
    F4vSettings: Optional[F4vSettings] = None
    M2tsSettings: Optional[M2tsSettingsOutput] = None
    M3u8Settings: Optional[M3u8SettingsOutput] = None
    MovSettings: Optional[MovSettings] = None
    Mp4Settings: Optional[Mp4Settings] = None
    MpdSettings: Optional[MpdSettings] = None
    MxfSettings: Optional[MxfSettings] = None


class ContainerSettings(BaseValidatorModel):
    CmfcSettings: Optional[CmfcSettings] = None
    Container: Optional[ContainerTypeType] = None
    F4vSettings: Optional[F4vSettings] = None
    M2tsSettings: Optional[M2tsSettings] = None
    M3u8Settings: Optional[M3u8Settings] = None
    MovSettings: Optional[MovSettings] = None
    Mp4Settings: Optional[Mp4Settings] = None
    MpdSettings: Optional[MpdSettings] = None
    MxfSettings: Optional[MxfSettings] = None


class VideoPreprocessorOutput(BaseValidatorModel):
    ColorCorrector: Optional[ColorCorrector] = None
    Deinterlacer: Optional[Deinterlacer] = None
    DolbyVision: Optional[DolbyVision] = None
    Hdr10Plus: Optional[Hdr10Plus] = None
    ImageInserter: Optional[ImageInserterOutput] = None
    NoiseReducer: Optional[NoiseReducer] = None
    PartnerWatermarking: Optional[PartnerWatermarking] = None
    TimecodeBurnin: Optional[TimecodeBurnin] = None


class VideoPreprocessor(BaseValidatorModel):
    ColorCorrector: Optional[ColorCorrector] = None
    Deinterlacer: Optional[Deinterlacer] = None
    DolbyVision: Optional[DolbyVision] = None
    Hdr10Plus: Optional[Hdr10Plus] = None
    ImageInserter: Optional[ImageInserter] = None
    NoiseReducer: Optional[NoiseReducer] = None
    PartnerWatermarking: Optional[PartnerWatermarking] = None
    TimecodeBurnin: Optional[TimecodeBurnin] = None


class OutputGroupDetail(BaseValidatorModel):
    OutputDetails: Optional[List[OutputDetail]] = None


class CreateQueueResponse(BaseValidatorModel):
    Queue: Queue
    ResponseMetadata: ResponseMetadata


class GetQueueResponse(BaseValidatorModel):
    Queue: Queue
    ResponseMetadata: ResponseMetadata


class ListQueuesResponse(BaseValidatorModel):
    Queues: List[Queue]
    TotalConcurrentJobs: int
    UnallocatedConcurrentJobs: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateQueueResponse(BaseValidatorModel):
    Queue: Queue
    ResponseMetadata: ResponseMetadata


class DestinationSettings(BaseValidatorModel):
    S3Settings: Optional[S3DestinationSettings] = None


class VideoOverlayOutput(BaseValidatorModel):
    EndTimecode: Optional[str] = None
    InitialPosition: Optional[VideoOverlayPosition] = None
    Input: Optional[VideoOverlayInputOutput] = None
    Playback: Optional[VideoOverlayPlayBackModeType] = None
    StartTimecode: Optional[str] = None
    Transitions: Optional[List[VideoOverlayTransition]] = None


class VideoOverlay(BaseValidatorModel):
    EndTimecode: Optional[str] = None
    InitialPosition: Optional[VideoOverlayPosition] = None
    Input: Optional[VideoOverlayInput] = None
    Playback: Optional[VideoOverlayPlayBackModeType] = None
    StartTimecode: Optional[str] = None
    Transitions: Optional[List[VideoOverlayTransition]] = None


class VideoCodecSettings(BaseValidatorModel):
    Av1Settings: Optional[Av1Settings] = None
    AvcIntraSettings: Optional[AvcIntraSettings] = None
    Codec: Optional[VideoCodecType] = None
    FrameCaptureSettings: Optional[FrameCaptureSettings] = None
    GifSettings: Optional[GifSettings] = None
    H264Settings: Optional[H264Settings] = None
    H265Settings: Optional[H265Settings] = None
    Mpeg2Settings: Optional[Mpeg2Settings] = None
    ProresSettings: Optional[ProresSettings] = None
    UncompressedSettings: Optional[UncompressedSettings] = None
    Vc3Settings: Optional[Vc3Settings] = None
    Vp8Settings: Optional[Vp8Settings] = None
    Vp9Settings: Optional[Vp9Settings] = None
    XavcSettings: Optional[XavcSettings] = None


class Container(BaseValidatorModel):
    Duration: Optional[float] = None
    Format: Optional[FormatType] = None
    Tracks: Optional[List[Track]] = None


class AutomatedEncodingSettingsOutput(BaseValidatorModel):
    AbrSettings: Optional[AutomatedAbrSettingsOutput] = None


class AutomatedEncodingSettings(BaseValidatorModel):
    AbrSettings: Optional[AutomatedAbrSettings] = None


class CaptionSelector(BaseValidatorModel):
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    SourceSettings: Optional[CaptionSourceSettings] = None


class AudioDescriptionOutput(BaseValidatorModel):
    AudioChannelTaggingSettings: Optional[AudioChannelTaggingSettingsOutput] = None
    AudioNormalizationSettings: Optional[AudioNormalizationSettings] = None
    AudioSourceName: Optional[str] = None
    AudioType: Optional[int] = None
    AudioTypeControl: Optional[AudioTypeControlType] = None
    CodecSettings: Optional[AudioCodecSettings] = None
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageCodeControl: Optional[AudioLanguageCodeControlType] = None
    RemixSettings: Optional[RemixSettingsOutput] = None
    StreamName: Optional[str] = None


class AudioSelectorOutput(BaseValidatorModel):
    AudioDurationCorrection: Optional[AudioDurationCorrectionType] = None
    CustomLanguageCode: Optional[str] = None
    DefaultSelection: Optional[AudioDefaultSelectionType] = None
    ExternalAudioFileInput: Optional[str] = None
    HlsRenditionGroupSettings: Optional[HlsRenditionGroupSettings] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Offset: Optional[int] = None
    Pids: Optional[List[int]] = None
    ProgramSelection: Optional[int] = None
    RemixSettings: Optional[RemixSettingsOutput] = None
    SelectorType: Optional[AudioSelectorTypeType] = None
    Tracks: Optional[List[int]] = None


class AudioDescription(BaseValidatorModel):
    AudioChannelTaggingSettings: Optional[AudioChannelTaggingSettings] = None
    AudioNormalizationSettings: Optional[AudioNormalizationSettings] = None
    AudioSourceName: Optional[str] = None
    AudioType: Optional[int] = None
    AudioTypeControl: Optional[AudioTypeControlType] = None
    CodecSettings: Optional[AudioCodecSettings] = None
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageCodeControl: Optional[AudioLanguageCodeControlType] = None
    RemixSettings: Optional[RemixSettings] = None
    StreamName: Optional[str] = None


class AudioSelector(BaseValidatorModel):
    AudioDurationCorrection: Optional[AudioDurationCorrectionType] = None
    CustomLanguageCode: Optional[str] = None
    DefaultSelection: Optional[AudioDefaultSelectionType] = None
    ExternalAudioFileInput: Optional[str] = None
    HlsRenditionGroupSettings: Optional[HlsRenditionGroupSettings] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Offset: Optional[int] = None
    Pids: Optional[List[int]] = None
    ProgramSelection: Optional[int] = None
    RemixSettings: Optional[RemixSettings] = None
    SelectorType: Optional[AudioSelectorTypeType] = None
    Tracks: Optional[List[int]] = None


class CmafGroupSettingsOutput(BaseValidatorModel):
    AdditionalManifests: Optional[List[CmafAdditionalManifestOutput]] = None
    BaseUrl: Optional[str] = None
    ClientCache: Optional[CmafClientCacheType] = None
    CodecSpecification: Optional[CmafCodecSpecificationType] = None
    DashIFrameTrickPlayNameModifier: Optional[str] = None
    DashManifestStyle: Optional[DashManifestStyleType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettings] = None
    Encryption: Optional[CmafEncryptionSettingsOutput] = None
    FragmentLength: Optional[int] = None
    ImageBasedTrickPlay: Optional[CmafImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[CmafImageBasedTrickPlaySettings] = None
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


class CmafGroupSettings(BaseValidatorModel):
    AdditionalManifests: Optional[List[CmafAdditionalManifest]] = None
    BaseUrl: Optional[str] = None
    ClientCache: Optional[CmafClientCacheType] = None
    CodecSpecification: Optional[CmafCodecSpecificationType] = None
    DashIFrameTrickPlayNameModifier: Optional[str] = None
    DashManifestStyle: Optional[DashManifestStyleType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettings] = None
    Encryption: Optional[CmafEncryptionSettings] = None
    FragmentLength: Optional[int] = None
    ImageBasedTrickPlay: Optional[CmafImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[CmafImageBasedTrickPlaySettings] = None
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


class DashIsoGroupSettingsOutput(BaseValidatorModel):
    AdditionalManifests: Optional[List[DashAdditionalManifestOutput]] = None
    AudioChannelConfigSchemeIdUri: Optional[DashIsoGroupAudioChannelConfigSchemeIdUriType] = None
    BaseUrl: Optional[str] = None
    DashIFrameTrickPlayNameModifier: Optional[str] = None
    DashManifestStyle: Optional[DashManifestStyleType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettings] = None
    Encryption: Optional[DashIsoEncryptionSettingsOutput] = None
    FragmentLength: Optional[int] = None
    HbbtvCompliance: Optional[DashIsoHbbtvComplianceType] = None
    ImageBasedTrickPlay: Optional[DashIsoImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[DashIsoImageBasedTrickPlaySettings] = None
    MinBufferTime: Optional[int] = None
    MinFinalSegmentLength: Optional[float] = None
    MpdManifestBandwidthType: Optional[DashIsoMpdManifestBandwidthTypeType] = None
    MpdProfile: Optional[DashIsoMpdProfileType] = None
    PtsOffsetHandlingForBFrames: Optional[DashIsoPtsOffsetHandlingForBFramesType] = None
    SegmentControl: Optional[DashIsoSegmentControlType] = None
    SegmentLength: Optional[int] = None
    SegmentLengthControl: Optional[DashIsoSegmentLengthControlType] = None
    VideoCompositionOffsets: Optional[DashIsoVideoCompositionOffsetsType] = None
    WriteSegmentTimelineInRepresentation: Optional[DashIsoWriteSegmentTimelineInRepresentationType] = None


class DashIsoGroupSettings(BaseValidatorModel):
    AdditionalManifests: Optional[List[DashAdditionalManifest]] = None
    AudioChannelConfigSchemeIdUri: Optional[DashIsoGroupAudioChannelConfigSchemeIdUriType] = None
    BaseUrl: Optional[str] = None
    DashIFrameTrickPlayNameModifier: Optional[str] = None
    DashManifestStyle: Optional[DashManifestStyleType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettings] = None
    Encryption: Optional[DashIsoEncryptionSettings] = None
    FragmentLength: Optional[int] = None
    HbbtvCompliance: Optional[DashIsoHbbtvComplianceType] = None
    ImageBasedTrickPlay: Optional[DashIsoImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[DashIsoImageBasedTrickPlaySettings] = None
    MinBufferTime: Optional[int] = None
    MinFinalSegmentLength: Optional[float] = None
    MpdManifestBandwidthType: Optional[DashIsoMpdManifestBandwidthTypeType] = None
    MpdProfile: Optional[DashIsoMpdProfileType] = None
    PtsOffsetHandlingForBFrames: Optional[DashIsoPtsOffsetHandlingForBFramesType] = None
    SegmentControl: Optional[DashIsoSegmentControlType] = None
    SegmentLength: Optional[int] = None
    SegmentLengthControl: Optional[DashIsoSegmentLengthControlType] = None
    VideoCompositionOffsets: Optional[DashIsoVideoCompositionOffsetsType] = None
    WriteSegmentTimelineInRepresentation: Optional[DashIsoWriteSegmentTimelineInRepresentationType] = None


class FileGroupSettings(BaseValidatorModel):
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettings] = None


class HlsGroupSettingsOutput(BaseValidatorModel):
    AdMarkers: Optional[List[HlsAdMarkersType]] = None
    AdditionalManifests: Optional[List[HlsAdditionalManifestOutput]] = None
    AudioOnlyHeader: Optional[HlsAudioOnlyHeaderType] = None
    BaseUrl: Optional[str] = None
    CaptionLanguageMappings: Optional[List[HlsCaptionLanguageMapping]] = None
    CaptionLanguageSetting: Optional[HlsCaptionLanguageSettingType] = None
    CaptionSegmentLengthControl: Optional[HlsCaptionSegmentLengthControlType] = None
    ClientCache: Optional[HlsClientCacheType] = None
    CodecSpecification: Optional[HlsCodecSpecificationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettings] = None
    DirectoryStructure: Optional[HlsDirectoryStructureType] = None
    Encryption: Optional[HlsEncryptionSettingsOutput] = None
    ImageBasedTrickPlay: Optional[HlsImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[HlsImageBasedTrickPlaySettings] = None
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


class HlsGroupSettings(BaseValidatorModel):
    AdMarkers: Optional[List[HlsAdMarkersType]] = None
    AdditionalManifests: Optional[List[HlsAdditionalManifest]] = None
    AudioOnlyHeader: Optional[HlsAudioOnlyHeaderType] = None
    BaseUrl: Optional[str] = None
    CaptionLanguageMappings: Optional[List[HlsCaptionLanguageMapping]] = None
    CaptionLanguageSetting: Optional[HlsCaptionLanguageSettingType] = None
    CaptionSegmentLengthControl: Optional[HlsCaptionSegmentLengthControlType] = None
    ClientCache: Optional[HlsClientCacheType] = None
    CodecSpecification: Optional[HlsCodecSpecificationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettings] = None
    DirectoryStructure: Optional[HlsDirectoryStructureType] = None
    Encryption: Optional[HlsEncryptionSettings] = None
    ImageBasedTrickPlay: Optional[HlsImageBasedTrickPlayType] = None
    ImageBasedTrickPlaySettings: Optional[HlsImageBasedTrickPlaySettings] = None
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


class MsSmoothGroupSettingsOutput(BaseValidatorModel):
    AdditionalManifests: Optional[List[MsSmoothAdditionalManifestOutput]] = None
    AudioDeduplication: Optional[MsSmoothAudioDeduplicationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettings] = None
    Encryption: Optional[MsSmoothEncryptionSettingsOutput] = None
    FragmentLength: Optional[int] = None
    FragmentLengthControl: Optional[MsSmoothFragmentLengthControlType] = None
    ManifestEncoding: Optional[MsSmoothManifestEncodingType] = None


class MsSmoothGroupSettings(BaseValidatorModel):
    AdditionalManifests: Optional[List[MsSmoothAdditionalManifest]] = None
    AudioDeduplication: Optional[MsSmoothAudioDeduplicationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettings] = None
    Encryption: Optional[MsSmoothEncryptionSettings] = None
    FragmentLength: Optional[int] = None
    FragmentLengthControl: Optional[MsSmoothFragmentLengthControlType] = None
    ManifestEncoding: Optional[MsSmoothManifestEncodingType] = None


class VideoDescriptionOutput(BaseValidatorModel):
    AfdSignaling: Optional[AfdSignalingType] = None
    AntiAlias: Optional[AntiAliasType] = None
    ChromaPositionMode: Optional[ChromaPositionModeType] = None
    CodecSettings: Optional[VideoCodecSettings] = None
    ColorMetadata: Optional[ColorMetadataType] = None
    Crop: Optional[Rectangle] = None
    DropFrameTimecode: Optional[DropFrameTimecodeType] = None
    FixedAfd: Optional[int] = None
    Height: Optional[int] = None
    Position: Optional[Rectangle] = None
    RespondToAfd: Optional[RespondToAfdType] = None
    ScalingBehavior: Optional[ScalingBehaviorType] = None
    Sharpness: Optional[int] = None
    TimecodeInsertion: Optional[VideoTimecodeInsertionType] = None
    TimecodeTrack: Optional[TimecodeTrackType] = None
    VideoPreprocessors: Optional[VideoPreprocessorOutput] = None
    Width: Optional[int] = None


class VideoDescription(BaseValidatorModel):
    AfdSignaling: Optional[AfdSignalingType] = None
    AntiAlias: Optional[AntiAliasType] = None
    ChromaPositionMode: Optional[ChromaPositionModeType] = None
    CodecSettings: Optional[VideoCodecSettings] = None
    ColorMetadata: Optional[ColorMetadataType] = None
    Crop: Optional[Rectangle] = None
    DropFrameTimecode: Optional[DropFrameTimecodeType] = None
    FixedAfd: Optional[int] = None
    Height: Optional[int] = None
    Position: Optional[Rectangle] = None
    RespondToAfd: Optional[RespondToAfdType] = None
    ScalingBehavior: Optional[ScalingBehaviorType] = None
    Sharpness: Optional[int] = None
    TimecodeInsertion: Optional[VideoTimecodeInsertionType] = None
    TimecodeTrack: Optional[TimecodeTrackType] = None
    VideoPreprocessors: Optional[VideoPreprocessor] = None
    Width: Optional[int] = None


class ProbeResult(BaseValidatorModel):
    Container: Optional[Container] = None
    Metadata: Optional[Metadata] = None
    TrackMappings: Optional[List[TrackMapping]] = None


class InputOutput(BaseValidatorModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettings] = None
    AudioSelectorGroups: Optional[Dict[str, AudioSelectorGroupOutput]] = None
    AudioSelectors: Optional[Dict[str, AudioSelectorOutput]] = None
    CaptionSelectors: Optional[Dict[str, CaptionSelector]] = None
    Crop: Optional[Rectangle] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DecryptionSettings: Optional[InputDecryptionSettings] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
    DynamicAudioSelectors: Optional[Dict[str, DynamicAudioSelector]] = None
    FileInput: Optional[str] = None
    FilterEnable: Optional[InputFilterEnableType] = None
    FilterStrength: Optional[int] = None
    ImageInserter: Optional[ImageInserterOutput] = None
    InputClippings: Optional[List[InputClipping]] = None
    InputScanType: Optional[InputScanTypeType] = None
    Position: Optional[Rectangle] = None
    ProgramNumber: Optional[int] = None
    PsiControl: Optional[InputPsiControlType] = None
    SupplementalImps: Optional[List[str]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None
    VideoGenerator: Optional[InputVideoGenerator] = None
    VideoOverlays: Optional[List[VideoOverlayOutput]] = None
    VideoSelector: Optional[VideoSelector] = None


class InputTemplateOutput(BaseValidatorModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettings] = None
    AudioSelectorGroups: Optional[Dict[str, AudioSelectorGroupOutput]] = None
    AudioSelectors: Optional[Dict[str, AudioSelectorOutput]] = None
    CaptionSelectors: Optional[Dict[str, CaptionSelector]] = None
    Crop: Optional[Rectangle] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
    DynamicAudioSelectors: Optional[Dict[str, DynamicAudioSelector]] = None
    FilterEnable: Optional[InputFilterEnableType] = None
    FilterStrength: Optional[int] = None
    ImageInserter: Optional[ImageInserterOutput] = None
    InputClippings: Optional[List[InputClipping]] = None
    InputScanType: Optional[InputScanTypeType] = None
    Position: Optional[Rectangle] = None
    ProgramNumber: Optional[int] = None
    PsiControl: Optional[InputPsiControlType] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None
    VideoOverlays: Optional[List[VideoOverlayOutput]] = None
    VideoSelector: Optional[VideoSelector] = None


class InputTemplate(BaseValidatorModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettings] = None
    AudioSelectorGroups: Optional[Dict[str, AudioSelectorGroup]] = None
    AudioSelectors: Optional[Dict[str, AudioSelector]] = None
    CaptionSelectors: Optional[Dict[str, CaptionSelector]] = None
    Crop: Optional[Rectangle] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
    DynamicAudioSelectors: Optional[Dict[str, DynamicAudioSelector]] = None
    FilterEnable: Optional[InputFilterEnableType] = None
    FilterStrength: Optional[int] = None
    ImageInserter: Optional[ImageInserter] = None
    InputClippings: Optional[List[InputClipping]] = None
    InputScanType: Optional[InputScanTypeType] = None
    Position: Optional[Rectangle] = None
    ProgramNumber: Optional[int] = None
    PsiControl: Optional[InputPsiControlType] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None
    VideoOverlays: Optional[List[VideoOverlay]] = None
    VideoSelector: Optional[VideoSelector] = None


class Input(BaseValidatorModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettings] = None
    AudioSelectorGroups: Optional[Dict[str, AudioSelectorGroup]] = None
    AudioSelectors: Optional[Dict[str, AudioSelector]] = None
    CaptionSelectors: Optional[Dict[str, CaptionSelector]] = None
    Crop: Optional[Rectangle] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DecryptionSettings: Optional[InputDecryptionSettings] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
    DynamicAudioSelectors: Optional[Dict[str, DynamicAudioSelector]] = None
    FileInput: Optional[str] = None
    FilterEnable: Optional[InputFilterEnableType] = None
    FilterStrength: Optional[int] = None
    ImageInserter: Optional[ImageInserter] = None
    InputClippings: Optional[List[InputClipping]] = None
    InputScanType: Optional[InputScanTypeType] = None
    Position: Optional[Rectangle] = None
    ProgramNumber: Optional[int] = None
    PsiControl: Optional[InputPsiControlType] = None
    SupplementalImps: Optional[List[str]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None
    VideoGenerator: Optional[InputVideoGenerator] = None
    VideoOverlays: Optional[List[VideoOverlay]] = None
    VideoSelector: Optional[VideoSelector] = None


class OutputGroupSettingsOutput(BaseValidatorModel):
    CmafGroupSettings: Optional[CmafGroupSettingsOutput] = None
    DashIsoGroupSettings: Optional[DashIsoGroupSettingsOutput] = None
    FileGroupSettings: Optional[FileGroupSettings] = None
    HlsGroupSettings: Optional[HlsGroupSettingsOutput] = None
    MsSmoothGroupSettings: Optional[MsSmoothGroupSettingsOutput] = None
    Type: Optional[OutputGroupTypeType] = None


class OutputGroupSettings(BaseValidatorModel):
    CmafGroupSettings: Optional[CmafGroupSettings] = None
    DashIsoGroupSettings: Optional[DashIsoGroupSettings] = None
    FileGroupSettings: Optional[FileGroupSettings] = None
    HlsGroupSettings: Optional[HlsGroupSettings] = None
    MsSmoothGroupSettings: Optional[MsSmoothGroupSettings] = None
    Type: Optional[OutputGroupTypeType] = None


class Extra(BaseValidatorModel):
    AudioDescriptions: Optional[List[AudioDescriptionOutput]] = None
    CaptionDescriptions: Optional[List[CaptionDescriptionOutput]] = None
    ContainerSettings: Optional[ContainerSettingsOutput] = None
    Extension: Optional[str] = None
    NameModifier: Optional[str] = None
    OutputSettings: Optional[OutputSettings] = None
    Preset: Optional[str] = None
    VideoDescription: Optional[VideoDescriptionOutput] = None


class PresetSettingsOutput(BaseValidatorModel):
    AudioDescriptions: Optional[List[AudioDescriptionOutput]] = None
    CaptionDescriptions: Optional[List[CaptionDescriptionPresetOutput]] = None
    ContainerSettings: Optional[ContainerSettingsOutput] = None
    VideoDescription: Optional[VideoDescriptionOutput] = None


class Output(BaseValidatorModel):
    AudioDescriptions: Optional[List[AudioDescription]] = None
    CaptionDescriptions: Optional[List[CaptionDescription]] = None
    ContainerSettings: Optional[ContainerSettings] = None
    Extension: Optional[str] = None
    NameModifier: Optional[str] = None
    OutputSettings: Optional[OutputSettings] = None
    Preset: Optional[str] = None
    VideoDescription: Optional[VideoDescription] = None


class PresetSettings(BaseValidatorModel):
    AudioDescriptions: Optional[List[AudioDescription]] = None
    CaptionDescriptions: Optional[List[CaptionDescriptionPreset]] = None
    ContainerSettings: Optional[ContainerSettings] = None
    VideoDescription: Optional[VideoDescription] = None


class ProbeResponse(BaseValidatorModel):
    ProbeResults: List[ProbeResult]
    ResponseMetadata: ResponseMetadata


class OutputGroupOutput(BaseValidatorModel):
    AutomatedEncodingSettings: Optional[AutomatedEncodingSettingsOutput] = None
    CustomName: Optional[str] = None
    Name: Optional[str] = None
    OutputGroupSettings: Optional[OutputGroupSettingsOutput] = None
    Outputs: Optional[List[Extra]] = None


class Preset(BaseValidatorModel):
    Name: str
    Settings: PresetSettingsOutput
    Arn: Optional[str] = None
    Category: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None
    Type: Optional[TypeType] = None


class OutputGroup(BaseValidatorModel):
    AutomatedEncodingSettings: Optional[AutomatedEncodingSettings] = None
    CustomName: Optional[str] = None
    Name: Optional[str] = None
    OutputGroupSettings: Optional[OutputGroupSettings] = None
    Outputs: Optional[List[Output]] = None

PresetSettingsUnion = Union[PresetSettings, PresetSettingsOutput]


class JobSettingsOutput(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    AvailBlanking: Optional[AvailBlanking] = None
    ColorConversion3DLUTSettings: Optional[List[ColorConversion3DLUTSetting]] = None
    Esam: Optional[EsamSettings] = None
    ExtendedDataServices: Optional[ExtendedDataServices] = None
    FollowSource: Optional[int] = None
    Inputs: Optional[List[InputOutput]] = None
    KantarWatermark: Optional[KantarWatermarkSettings] = None
    MotionImageInserter: Optional[MotionImageInserter] = None
    NielsenConfiguration: Optional[NielsenConfiguration] = None
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettings] = None
    OutputGroups: Optional[List[OutputGroupOutput]] = None
    TimecodeConfig: Optional[TimecodeConfig] = None
    TimedMetadataInsertion: Optional[TimedMetadataInsertionOutput] = None


class JobTemplateSettingsOutput(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    AvailBlanking: Optional[AvailBlanking] = None
    ColorConversion3DLUTSettings: Optional[List[ColorConversion3DLUTSetting]] = None
    Esam: Optional[EsamSettings] = None
    ExtendedDataServices: Optional[ExtendedDataServices] = None
    FollowSource: Optional[int] = None
    Inputs: Optional[List[InputTemplateOutput]] = None
    KantarWatermark: Optional[KantarWatermarkSettings] = None
    MotionImageInserter: Optional[MotionImageInserter] = None
    NielsenConfiguration: Optional[NielsenConfiguration] = None
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettings] = None
    OutputGroups: Optional[List[OutputGroupOutput]] = None
    TimecodeConfig: Optional[TimecodeConfig] = None
    TimedMetadataInsertion: Optional[TimedMetadataInsertionOutput] = None


class CreatePresetResponse(BaseValidatorModel):
    Preset: Preset
    ResponseMetadata: ResponseMetadata


class GetPresetResponse(BaseValidatorModel):
    Preset: Preset
    ResponseMetadata: ResponseMetadata


class ListPresetsResponse(BaseValidatorModel):
    Presets: List[Preset]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdatePresetResponse(BaseValidatorModel):
    Preset: Preset
    ResponseMetadata: ResponseMetadata


class JobSettings(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    AvailBlanking: Optional[AvailBlanking] = None
    ColorConversion3DLUTSettings: Optional[List[ColorConversion3DLUTSetting]] = None
    Esam: Optional[EsamSettings] = None
    ExtendedDataServices: Optional[ExtendedDataServices] = None
    FollowSource: Optional[int] = None
    Inputs: Optional[List[Input]] = None
    KantarWatermark: Optional[KantarWatermarkSettings] = None
    MotionImageInserter: Optional[MotionImageInserter] = None
    NielsenConfiguration: Optional[NielsenConfiguration] = None
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettings] = None
    OutputGroups: Optional[List[OutputGroup]] = None
    TimecodeConfig: Optional[TimecodeConfig] = None
    TimedMetadataInsertion: Optional[TimedMetadataInsertion] = None


class JobTemplateSettings(BaseValidatorModel):
    AdAvailOffset: Optional[int] = None
    AvailBlanking: Optional[AvailBlanking] = None
    ColorConversion3DLUTSettings: Optional[List[ColorConversion3DLUTSetting]] = None
    Esam: Optional[EsamSettings] = None
    ExtendedDataServices: Optional[ExtendedDataServices] = None
    FollowSource: Optional[int] = None
    Inputs: Optional[List[InputTemplate]] = None
    KantarWatermark: Optional[KantarWatermarkSettings] = None
    MotionImageInserter: Optional[MotionImageInserter] = None
    NielsenConfiguration: Optional[NielsenConfiguration] = None
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettings] = None
    OutputGroups: Optional[List[OutputGroup]] = None
    TimecodeConfig: Optional[TimecodeConfig] = None
    TimedMetadataInsertion: Optional[TimedMetadataInsertion] = None


class CreatePresetRequest(BaseValidatorModel):
    Name: str
    Settings: PresetSettingsUnion
    Category: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class UpdatePresetRequest(BaseValidatorModel):
    Name: str
    Category: Optional[str] = None
    Description: Optional[str] = None
    Settings: Optional[PresetSettingsUnion] = None


class Job(BaseValidatorModel):
    Role: str
    Settings: JobSettingsOutput
    AccelerationSettings: Optional[AccelerationSettings] = None
    AccelerationStatus: Optional[AccelerationStatusType] = None
    Arn: Optional[str] = None
    BillingTagsSource: Optional[BillingTagsSourceType] = None
    ClientRequestToken: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    CurrentPhase: Optional[JobPhaseType] = None
    ErrorCode: Optional[int] = None
    ErrorMessage: Optional[str] = None
    HopDestinations: Optional[List[HopDestination]] = None
    Id: Optional[str] = None
    JobEngineVersionRequested: Optional[str] = None
    JobEngineVersionUsed: Optional[str] = None
    JobPercentComplete: Optional[int] = None
    JobTemplate: Optional[str] = None
    Messages: Optional[JobMessages] = None
    OutputGroupDetails: Optional[List[OutputGroupDetail]] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    QueueTransitions: Optional[List[QueueTransition]] = None
    RetryCount: Optional[int] = None
    SimulateReservedQueue: Optional[SimulateReservedQueueType] = None
    Status: Optional[JobStatusType] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None
    Timing: Optional[Timing] = None
    UserMetadata: Optional[Dict[str, str]] = None
    Warnings: Optional[List[WarningGroup]] = None


class JobTemplate(BaseValidatorModel):
    Name: str
    Settings: JobTemplateSettingsOutput
    AccelerationSettings: Optional[AccelerationSettings] = None
    Arn: Optional[str] = None
    Category: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    HopDestinations: Optional[List[HopDestination]] = None
    LastUpdated: Optional[datetime] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None
    Type: Optional[TypeType] = None

JobSettingsUnion = Union[JobSettings, JobSettingsOutput]

JobTemplateSettingsUnion = Union[JobTemplateSettings, JobTemplateSettingsOutput]


class CreateJobResponse(BaseValidatorModel):
    Job: Job
    ResponseMetadata: ResponseMetadata


class GetJobResponse(BaseValidatorModel):
    Job: Job
    ResponseMetadata: ResponseMetadata


class ListJobsResponse(BaseValidatorModel):
    Jobs: List[Job]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchJobsResponse(BaseValidatorModel):
    Jobs: List[Job]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateJobTemplateResponse(BaseValidatorModel):
    JobTemplate: JobTemplate
    ResponseMetadata: ResponseMetadata


class GetJobTemplateResponse(BaseValidatorModel):
    JobTemplate: JobTemplate
    ResponseMetadata: ResponseMetadata


class ListJobTemplatesResponse(BaseValidatorModel):
    JobTemplates: List[JobTemplate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateJobTemplateResponse(BaseValidatorModel):
    JobTemplate: JobTemplate
    ResponseMetadata: ResponseMetadata


class CreateJobRequest(BaseValidatorModel):
    Role: str
    Settings: JobSettingsUnion
    AccelerationSettings: Optional[AccelerationSettings] = None
    BillingTagsSource: Optional[BillingTagsSourceType] = None
    ClientRequestToken: Optional[str] = None
    HopDestinations: Optional[List[HopDestination]] = None
    JobEngineVersion: Optional[str] = None
    JobTemplate: Optional[str] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    SimulateReservedQueue: Optional[SimulateReservedQueueType] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None
    Tags: Optional[Dict[str, str]] = None
    UserMetadata: Optional[Dict[str, str]] = None


class CreateJobTemplateRequest(BaseValidatorModel):
    Name: str
    Settings: JobTemplateSettingsUnion
    AccelerationSettings: Optional[AccelerationSettings] = None
    Category: Optional[str] = None
    Description: Optional[str] = None
    HopDestinations: Optional[List[HopDestination]] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateJobTemplateRequest(BaseValidatorModel):
    Name: str
    AccelerationSettings: Optional[AccelerationSettings] = None
    Category: Optional[str] = None
    Description: Optional[str] = None
    HopDestinations: Optional[List[HopDestination]] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    Settings: Optional[JobTemplateSettingsUnion] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None