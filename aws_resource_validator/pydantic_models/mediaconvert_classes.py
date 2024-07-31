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
from aws_resource_validator.pydantic_models.mediaconvert_constants import *

class AacSettingsTypeDef(BaseModel):
    AudioDescriptionBroadcasterMix: Optional[AacAudioDescriptionBroadcasterMixType] = None
    Bitrate: Optional[int] = None
    CodecProfile: Optional[AacCodecProfileType] = None
    CodingMode: Optional[AacCodingModeType] = None
    RateControlMode: Optional[AacRateControlModeType] = None
    RawFormat: Optional[AacRawFormatType] = None
    SampleRate: Optional[int] = None
    Specification: Optional[AacSpecificationType] = None
    VbrQuality: Optional[AacVbrQualityType] = None

class Ac3SettingsTypeDef(BaseModel):
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

class AccelerationSettingsTypeDef(BaseModel):
    Mode: AccelerationModeType

class AdvancedInputFilterSettingsTypeDef(BaseModel):
    AddTexture: Optional[AdvancedInputFilterAddTextureType] = None
    Sharpening: Optional[AdvancedInputFilterSharpenType] = None

class AiffSettingsTypeDef(BaseModel):
    BitDepth: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None

class AllowedRenditionSizeTypeDef(BaseModel):
    Height: Optional[int] = None
    Required: Optional[RequiredFlagType] = None
    Width: Optional[int] = None

class AncillarySourceSettingsTypeDef(BaseModel):
    Convert608To708: Optional[AncillaryConvert608To708Type] = None
    SourceAncillaryChannelNumber: Optional[int] = None
    TerminateCaptions: Optional[AncillaryTerminateCaptionsType] = None

class AssociateCertificateRequestRequestTypeDef(BaseModel):
    Arn: str

class AudioChannelTaggingSettingsExtraOutputTypeDef(BaseModel):
    ChannelTag: Optional[AudioChannelTagType] = None
    ChannelTags: Optional[List[AudioChannelTagType]] = None

class AudioChannelTaggingSettingsOutputTypeDef(BaseModel):
    ChannelTag: Optional[AudioChannelTagType] = None
    ChannelTags: Optional[List[AudioChannelTagType]] = None

class AudioChannelTaggingSettingsTypeDef(BaseModel):
    ChannelTag: Optional[AudioChannelTagType] = None
    ChannelTags: Optional[Sequence[AudioChannelTagType]] = None

class Eac3AtmosSettingsTypeDef(BaseModel):
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

class Eac3SettingsTypeDef(BaseModel):
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

class FlacSettingsTypeDef(BaseModel):
    BitDepth: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None

class Mp2SettingsTypeDef(BaseModel):
    Bitrate: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None

class Mp3SettingsTypeDef(BaseModel):
    Bitrate: Optional[int] = None
    Channels: Optional[int] = None
    RateControlMode: Optional[Mp3RateControlModeType] = None
    SampleRate: Optional[int] = None
    VbrQuality: Optional[int] = None

class OpusSettingsTypeDef(BaseModel):
    Bitrate: Optional[int] = None
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None

class VorbisSettingsTypeDef(BaseModel):
    Channels: Optional[int] = None
    SampleRate: Optional[int] = None
    VbrQuality: Optional[int] = None

class WavSettingsTypeDef(BaseModel):
    BitDepth: Optional[int] = None
    Channels: Optional[int] = None
    Format: Optional[WavFormatType] = None
    SampleRate: Optional[int] = None

class AudioNormalizationSettingsTypeDef(BaseModel):
    Algorithm: Optional[AudioNormalizationAlgorithmType] = None
    AlgorithmControl: Optional[AudioNormalizationAlgorithmControlType] = None
    CorrectionGateLevel: Optional[int] = None
    LoudnessLogging: Optional[AudioNormalizationLoudnessLoggingType] = None
    PeakCalculation: Optional[AudioNormalizationPeakCalculationType] = None
    TargetLkfs: Optional[float] = None
    TruePeakLimiterThreshold: Optional[float] = None

class HlsRenditionGroupSettingsTypeDef(BaseModel):
    RenditionGroupId: Optional[str] = None
    RenditionLanguageCode: Optional[LanguageCodeType] = None
    RenditionName: Optional[str] = None

class AudioSelectorGroupExtraOutputTypeDef(BaseModel):
    AudioSelectorNames: Optional[List[str]] = None

class AudioSelectorGroupOutputTypeDef(BaseModel):
    AudioSelectorNames: Optional[List[str]] = None

class AudioSelectorGroupTypeDef(BaseModel):
    AudioSelectorNames: Optional[Sequence[str]] = None

class ForceIncludeRenditionSizeTypeDef(BaseModel):
    Height: Optional[int] = None
    Width: Optional[int] = None

class MinBottomRenditionSizeTypeDef(BaseModel):
    Height: Optional[int] = None
    Width: Optional[int] = None

class MinTopRenditionSizeTypeDef(BaseModel):
    Height: Optional[int] = None
    Width: Optional[int] = None

class Av1QvbrSettingsTypeDef(BaseModel):
    QvbrQualityLevel: Optional[int] = None
    QvbrQualityLevelFineTune: Optional[float] = None

class AvailBlankingTypeDef(BaseModel):
    AvailBlankingImage: Optional[str] = None

class AvcIntraUhdSettingsTypeDef(BaseModel):
    QualityTuningLevel: Optional[AvcIntraUhdQualityTuningLevelType] = None

class BandwidthReductionFilterTypeDef(BaseModel):
    Sharpening: Optional[BandwidthReductionFilterSharpeningType] = None
    Strength: Optional[BandwidthReductionFilterStrengthType] = None

class BurninDestinationSettingsTypeDef(BaseModel):
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
    ShadowColor: Optional[BurninSubtitleShadowColorType] = None
    ShadowOpacity: Optional[int] = None
    ShadowXOffset: Optional[int] = None
    ShadowYOffset: Optional[int] = None
    StylePassthrough: Optional[BurnInSubtitleStylePassthroughType] = None
    TeletextSpacing: Optional[BurninSubtitleTeletextSpacingType] = None
    XPosition: Optional[int] = None
    YPosition: Optional[int] = None

class CancelJobRequestRequestTypeDef(BaseModel):
    Id: str

class DvbSubDestinationSettingsTypeDef(BaseModel):
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

class EmbeddedDestinationSettingsTypeDef(BaseModel):
    Destination608ChannelNumber: Optional[int] = None
    Destination708ServiceNumber: Optional[int] = None

class ImscDestinationSettingsTypeDef(BaseModel):
    Accessibility: Optional[ImscAccessibilitySubsType] = None
    StylePassthrough: Optional[ImscStylePassthroughType] = None

class SccDestinationSettingsTypeDef(BaseModel):
    Framerate: Optional[SccDestinationFramerateType] = None

class SrtDestinationSettingsTypeDef(BaseModel):
    StylePassthrough: Optional[SrtStylePassthroughType] = None

class TeletextDestinationSettingsExtraOutputTypeDef(BaseModel):
    PageNumber: Optional[str] = None
    PageTypes: Optional[List[TeletextPageTypeType]] = None

class TtmlDestinationSettingsTypeDef(BaseModel):
    StylePassthrough: Optional[TtmlStylePassthroughType] = None

class WebvttDestinationSettingsTypeDef(BaseModel):
    Accessibility: Optional[WebvttAccessibilitySubsType] = None
    StylePassthrough: Optional[WebvttStylePassthroughType] = None

class TeletextDestinationSettingsOutputTypeDef(BaseModel):
    PageNumber: Optional[str] = None
    PageTypes: Optional[List[TeletextPageTypeType]] = None

class TeletextDestinationSettingsTypeDef(BaseModel):
    PageNumber: Optional[str] = None
    PageTypes: Optional[Sequence[TeletextPageTypeType]] = None

class CaptionSourceFramerateTypeDef(BaseModel):
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None

class DvbSubSourceSettingsTypeDef(BaseModel):
    Pid: Optional[int] = None

class EmbeddedSourceSettingsTypeDef(BaseModel):
    Convert608To708: Optional[EmbeddedConvert608To708Type] = None
    Source608ChannelNumber: Optional[int] = None
    Source608TrackNumber: Optional[int] = None
    TerminateCaptions: Optional[EmbeddedTerminateCaptionsType] = None

class TeletextSourceSettingsTypeDef(BaseModel):
    PageNumber: Optional[str] = None

class TrackSourceSettingsTypeDef(BaseModel):
    TrackNumber: Optional[int] = None

class WebvttHlsSourceSettingsTypeDef(BaseModel):
    RenditionGroupId: Optional[str] = None
    RenditionLanguageCode: Optional[LanguageCodeType] = None
    RenditionName: Optional[str] = None

class OutputChannelMappingExtraOutputTypeDef(BaseModel):
    InputChannels: Optional[List[int]] = None
    InputChannelsFineTune: Optional[List[float]] = None

class OutputChannelMappingOutputTypeDef(BaseModel):
    InputChannels: Optional[List[int]] = None
    InputChannelsFineTune: Optional[List[float]] = None

class OutputChannelMappingTypeDef(BaseModel):
    InputChannels: Optional[Sequence[int]] = None
    InputChannelsFineTune: Optional[Sequence[float]] = None

class ClipLimitsTypeDef(BaseModel):
    MaximumRGBTolerance: Optional[int] = None
    MaximumYUV: Optional[int] = None
    MinimumRGBTolerance: Optional[int] = None
    MinimumYUV: Optional[int] = None

class CmafAdditionalManifestExtraOutputTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None

class CmafAdditionalManifestOutputTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None

class CmafAdditionalManifestTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[Sequence[str]] = None

class SpekeKeyProviderCmafExtraOutputTypeDef(BaseModel):
    CertificateArn: Optional[str] = None
    DashSignaledSystemIds: Optional[List[str]] = None
    HlsSignaledSystemIds: Optional[List[str]] = None
    ResourceId: Optional[str] = None
    Url: Optional[str] = None

class StaticKeyProviderTypeDef(BaseModel):
    KeyFormat: Optional[str] = None
    KeyFormatVersions: Optional[str] = None
    StaticKeyValue: Optional[str] = None
    Url: Optional[str] = None

class SpekeKeyProviderCmafOutputTypeDef(BaseModel):
    CertificateArn: Optional[str] = None
    DashSignaledSystemIds: Optional[List[str]] = None
    HlsSignaledSystemIds: Optional[List[str]] = None
    ResourceId: Optional[str] = None
    Url: Optional[str] = None

class SpekeKeyProviderCmafTypeDef(BaseModel):
    CertificateArn: Optional[str] = None
    DashSignaledSystemIds: Optional[Sequence[str]] = None
    HlsSignaledSystemIds: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    Url: Optional[str] = None

class CmafImageBasedTrickPlaySettingsTypeDef(BaseModel):
    IntervalCadence: Optional[CmafIntervalCadenceType] = None
    ThumbnailHeight: Optional[int] = None
    ThumbnailInterval: Optional[float] = None
    ThumbnailWidth: Optional[int] = None
    TileHeight: Optional[int] = None
    TileWidth: Optional[int] = None

class CmfcSettingsTypeDef(BaseModel):
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

class ColorConversion3DLUTSettingTypeDef(BaseModel):
    FileInput: Optional[str] = None
    InputColorSpace: Optional[ColorSpaceType] = None
    InputMasteringLuminance: Optional[int] = None
    OutputColorSpace: Optional[ColorSpaceType] = None
    OutputMasteringLuminance: Optional[int] = None

class Hdr10MetadataTypeDef(BaseModel):
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

class F4vSettingsTypeDef(BaseModel):
    MoovPlacement: Optional[F4vMoovPlacementType] = None

class M3u8SettingsExtraOutputTypeDef(BaseModel):
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

class MovSettingsTypeDef(BaseModel):
    ClapAtom: Optional[MovClapAtomType] = None
    CslgAtom: Optional[MovCslgAtomType] = None
    Mpeg2FourCCControl: Optional[MovMpeg2FourCCControlType] = None
    PaddingControl: Optional[MovPaddingControlType] = None
    Reference: Optional[MovReferenceType] = None

class Mp4SettingsTypeDef(BaseModel):
    AudioDuration: Optional[CmfcAudioDurationType] = None
    CslgAtom: Optional[Mp4CslgAtomType] = None
    CttsVersion: Optional[int] = None
    FreeSpaceBox: Optional[Mp4FreeSpaceBoxType] = None
    MoovPlacement: Optional[Mp4MoovPlacementType] = None
    Mp4MajorBrand: Optional[str] = None

class MpdSettingsTypeDef(BaseModel):
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

class M3u8SettingsOutputTypeDef(BaseModel):
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

class M3u8SettingsTypeDef(BaseModel):
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

class HopDestinationTypeDef(BaseModel):
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    WaitMinutes: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ReservationPlanSettingsTypeDef(BaseModel):
    Commitment: Literal["ONE_YEAR"]
    RenewalType: RenewalTypeType
    ReservedSlots: int

class DashAdditionalManifestExtraOutputTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None

class DashAdditionalManifestOutputTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None

class DashAdditionalManifestTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[Sequence[str]] = None

class SpekeKeyProviderExtraOutputTypeDef(BaseModel):
    CertificateArn: Optional[str] = None
    ResourceId: Optional[str] = None
    SystemIds: Optional[List[str]] = None
    Url: Optional[str] = None

class SpekeKeyProviderOutputTypeDef(BaseModel):
    CertificateArn: Optional[str] = None
    ResourceId: Optional[str] = None
    SystemIds: Optional[List[str]] = None
    Url: Optional[str] = None

class SpekeKeyProviderTypeDef(BaseModel):
    CertificateArn: Optional[str] = None
    ResourceId: Optional[str] = None
    SystemIds: Optional[Sequence[str]] = None
    Url: Optional[str] = None

class DashIsoImageBasedTrickPlaySettingsTypeDef(BaseModel):
    IntervalCadence: Optional[DashIsoIntervalCadenceType] = None
    ThumbnailHeight: Optional[int] = None
    ThumbnailInterval: Optional[float] = None
    ThumbnailWidth: Optional[int] = None
    TileHeight: Optional[int] = None
    TileWidth: Optional[int] = None

class DeinterlacerTypeDef(BaseModel):
    Algorithm: Optional[DeinterlaceAlgorithmType] = None
    Control: Optional[DeinterlacerControlType] = None
    Mode: Optional[DeinterlacerModeType] = None

class DeleteJobTemplateRequestRequestTypeDef(BaseModel):
    Name: str

class DeletePresetRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteQueueRequestRequestTypeDef(BaseModel):
    Name: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeEndpointsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    Mode: Optional[DescribeEndpointsModeType] = None
    NextToken: Optional[str] = None

class EndpointTypeDef(BaseModel):
    Url: Optional[str] = None

class DisassociateCertificateRequestRequestTypeDef(BaseModel):
    Arn: str

class DolbyVisionLevel6MetadataTypeDef(BaseModel):
    MaxCll: Optional[int] = None
    MaxFall: Optional[int] = None

class DvbNitSettingsTypeDef(BaseModel):
    NetworkId: Optional[int] = None
    NetworkName: Optional[str] = None
    NitInterval: Optional[int] = None

class DvbSdtSettingsTypeDef(BaseModel):
    OutputSdt: Optional[OutputSdtType] = None
    SdtInterval: Optional[int] = None
    ServiceName: Optional[str] = None
    ServiceProviderName: Optional[str] = None

class DvbTdtSettingsTypeDef(BaseModel):
    TdtInterval: Optional[int] = None

class EsamManifestConfirmConditionNotificationTypeDef(BaseModel):
    MccXml: Optional[str] = None

class EsamSignalProcessingNotificationTypeDef(BaseModel):
    SccXml: Optional[str] = None

class ExtendedDataServicesTypeDef(BaseModel):
    CopyProtectionAction: Optional[CopyProtectionActionType] = None
    VchipAction: Optional[VchipActionType] = None

class FrameCaptureSettingsTypeDef(BaseModel):
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    MaxCaptures: Optional[int] = None
    Quality: Optional[int] = None

class GetJobRequestRequestTypeDef(BaseModel):
    Id: str

class GetJobTemplateRequestRequestTypeDef(BaseModel):
    Name: str

class PolicyTypeDef(BaseModel):
    HttpInputs: Optional[InputPolicyType] = None
    HttpsInputs: Optional[InputPolicyType] = None
    S3Inputs: Optional[InputPolicyType] = None

class GetPresetRequestRequestTypeDef(BaseModel):
    Name: str

class GetQueueRequestRequestTypeDef(BaseModel):
    Name: str

class H264QvbrSettingsTypeDef(BaseModel):
    MaxAverageBitrate: Optional[int] = None
    QvbrQualityLevel: Optional[int] = None
    QvbrQualityLevelFineTune: Optional[float] = None

class H265QvbrSettingsTypeDef(BaseModel):
    MaxAverageBitrate: Optional[int] = None
    QvbrQualityLevel: Optional[int] = None
    QvbrQualityLevelFineTune: Optional[float] = None

class Hdr10PlusTypeDef(BaseModel):
    MasteringMonitorNits: Optional[int] = None
    TargetMonitorNits: Optional[int] = None

class HlsAdditionalManifestExtraOutputTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None

class HlsAdditionalManifestOutputTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None

class HlsAdditionalManifestTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[Sequence[str]] = None

class HlsCaptionLanguageMappingTypeDef(BaseModel):
    CaptionChannel: Optional[int] = None
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None

class HlsImageBasedTrickPlaySettingsTypeDef(BaseModel):
    IntervalCadence: Optional[HlsIntervalCadenceType] = None
    ThumbnailHeight: Optional[int] = None
    ThumbnailInterval: Optional[float] = None
    ThumbnailWidth: Optional[int] = None
    TileHeight: Optional[int] = None
    TileWidth: Optional[int] = None

class HlsSettingsTypeDef(BaseModel):
    AudioGroupId: Optional[str] = None
    AudioOnlyContainer: Optional[HlsAudioOnlyContainerType] = None
    AudioRenditionSets: Optional[str] = None
    AudioTrackType: Optional[HlsAudioTrackTypeType] = None
    DescriptiveVideoServiceFlag: Optional[HlsDescriptiveVideoServiceFlagType] = None
    IFrameOnlyManifest: Optional[HlsIFrameOnlyManifestType] = None
    SegmentModifier: Optional[str] = None

class Id3InsertionTypeDef(BaseModel):
    Id3: Optional[str] = None
    Timecode: Optional[str] = None

class InsertableImageTypeDef(BaseModel):
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

class InputClippingTypeDef(BaseModel):
    EndTimecode: Optional[str] = None
    StartTimecode: Optional[str] = None

class InputDecryptionSettingsTypeDef(BaseModel):
    DecryptionMode: Optional[DecryptionModeType] = None
    EncryptedDecryptionKey: Optional[str] = None
    InitializationVector: Optional[str] = None
    KmsKeyRegion: Optional[str] = None

class InputVideoGeneratorTypeDef(BaseModel):
    Channels: Optional[int] = None
    Duration: Optional[int] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    SampleRate: Optional[int] = None

class RectangleTypeDef(BaseModel):
    Height: Optional[int] = None
    Width: Optional[int] = None
    X: Optional[int] = None
    Y: Optional[int] = None

class JobMessagesTypeDef(BaseModel):
    Info: Optional[List[str]] = None
    Warning: Optional[List[str]] = None

class KantarWatermarkSettingsTypeDef(BaseModel):
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

class NielsenConfigurationTypeDef(BaseModel):
    BreakoutCode: Optional[int] = None
    DistributorId: Optional[str] = None

class NielsenNonLinearWatermarkSettingsTypeDef(BaseModel):
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

class TimecodeConfigTypeDef(BaseModel):
    Anchor: Optional[str] = None
    Source: Optional[TimecodeSourceType] = None
    Start: Optional[str] = None
    TimestampOffset: Optional[str] = None

class QueueTransitionTypeDef(BaseModel):
    DestinationQueue: Optional[str] = None
    SourceQueue: Optional[str] = None
    Timestamp: Optional[datetime] = None

class TimingTypeDef(BaseModel):
    FinishTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    SubmitTime: Optional[datetime] = None

class WarningGroupTypeDef(BaseModel):
    Code: int
    Count: int

class ListJobTemplatesRequestRequestTypeDef(BaseModel):
    Category: Optional[str] = None
    ListBy: Optional[JobTemplateListByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None

class ListPresetsRequestRequestTypeDef(BaseModel):
    Category: Optional[str] = None
    ListBy: Optional[PresetListByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None

class ListQueuesRequestRequestTypeDef(BaseModel):
    ListBy: Optional[QueueListByType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    Arn: str

class ResourceTagsTypeDef(BaseModel):
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class M2tsScte35EsamTypeDef(BaseModel):
    Scte35EsamPid: Optional[int] = None

class MotionImageInsertionFramerateTypeDef(BaseModel):
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None

class MotionImageInsertionOffsetTypeDef(BaseModel):
    ImageX: Optional[int] = None
    ImageY: Optional[int] = None

class Mpeg2SettingsTypeDef(BaseModel):
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

class MsSmoothAdditionalManifestExtraOutputTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None

class MsSmoothAdditionalManifestOutputTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[List[str]] = None

class MsSmoothAdditionalManifestTypeDef(BaseModel):
    ManifestNameModifier: Optional[str] = None
    SelectedOutputs: Optional[Sequence[str]] = None

class MxfXavcProfileSettingsTypeDef(BaseModel):
    DurationMode: Optional[MxfXavcDurationModeType] = None
    MaxAncDataSize: Optional[int] = None

class NexGuardFileMarkerSettingsTypeDef(BaseModel):
    License: Optional[str] = None
    Payload: Optional[int] = None
    Preset: Optional[str] = None
    Strength: Optional[WatermarkingStrengthType] = None

class NoiseReducerFilterSettingsTypeDef(BaseModel):
    Strength: Optional[int] = None

class NoiseReducerSpatialFilterSettingsTypeDef(BaseModel):
    PostFilterSharpenStrength: Optional[int] = None
    Speed: Optional[int] = None
    Strength: Optional[int] = None

class NoiseReducerTemporalFilterSettingsTypeDef(BaseModel):
    AggressiveMode: Optional[int] = None
    PostTemporalSharpening: Optional[NoiseFilterPostTemporalSharpeningType] = None
    PostTemporalSharpeningStrength: Optional[       NoiseFilterPostTemporalSharpeningStrengthType     ] = None
    Speed: Optional[int] = None
    Strength: Optional[int] = None

class VideoDetailTypeDef(BaseModel):
    HeightInPx: Optional[int] = None
    WidthInPx: Optional[int] = None

class ProresSettingsTypeDef(BaseModel):
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

class ReservationPlanTypeDef(BaseModel):
    Commitment: Optional[Literal["ONE_YEAR"]] = None
    ExpiresAt: Optional[datetime] = None
    PurchasedAt: Optional[datetime] = None
    RenewalType: Optional[RenewalTypeType] = None
    ReservedSlots: Optional[int] = None
    Status: Optional[ReservationPlanStatusType] = None

class S3DestinationAccessControlTypeDef(BaseModel):
    CannedAcl: Optional[S3ObjectCannedAclType] = None

class S3EncryptionSettingsTypeDef(BaseModel):
    EncryptionType: Optional[S3ServerSideEncryptionTypeType] = None
    KmsEncryptionContext: Optional[str] = None
    KmsKeyArn: Optional[str] = None

class SearchJobsRequestRequestTypeDef(BaseModel):
    InputFile: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    Arn: str
    Tags: Mapping[str, str]

class TimecodeBurninTypeDef(BaseModel):
    FontSize: Optional[int] = None
    Position: Optional[TimecodeBurninPositionType] = None
    Prefix: Optional[str] = None

class UncompressedSettingsTypeDef(BaseModel):
    Fourcc: Optional[UncompressedFourccType] = None
    FramerateControl: Optional[UncompressedFramerateControlType] = None
    FramerateConversionAlgorithm: Optional[UncompressedFramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    InterlaceMode: Optional[UncompressedInterlaceModeType] = None
    ScanTypeConversionMode: Optional[UncompressedScanTypeConversionModeType] = None
    SlowPal: Optional[UncompressedSlowPalType] = None
    Telecine: Optional[UncompressedTelecineType] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    Arn: str
    TagKeys: Optional[Sequence[str]] = None

class Vc3SettingsTypeDef(BaseModel):
    FramerateControl: Optional[Vc3FramerateControlType] = None
    FramerateConversionAlgorithm: Optional[Vc3FramerateConversionAlgorithmType] = None
    FramerateDenominator: Optional[int] = None
    FramerateNumerator: Optional[int] = None
    InterlaceMode: Optional[Vc3InterlaceModeType] = None
    ScanTypeConversionMode: Optional[Vc3ScanTypeConversionModeType] = None
    SlowPal: Optional[Vc3SlowPalType] = None
    Telecine: Optional[Vc3TelecineType] = None
    Vc3Class: Optional[Vc3ClassType] = None

class Vp8SettingsTypeDef(BaseModel):
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

class Vp9SettingsTypeDef(BaseModel):
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

class VideoOverlayInputClippingTypeDef(BaseModel):
    EndTimecode: Optional[str] = None
    StartTimecode: Optional[str] = None

class Xavc4kIntraCbgProfileSettingsTypeDef(BaseModel):
    XavcClass: Optional[Xavc4kIntraCbgProfileClassType] = None

class Xavc4kIntraVbrProfileSettingsTypeDef(BaseModel):
    XavcClass: Optional[Xavc4kIntraVbrProfileClassType] = None

class Xavc4kProfileSettingsTypeDef(BaseModel):
    BitrateClass: Optional[Xavc4kProfileBitrateClassType] = None
    CodecProfile: Optional[Xavc4kProfileCodecProfileType] = None
    FlickerAdaptiveQuantization: Optional[XavcFlickerAdaptiveQuantizationType] = None
    GopBReference: Optional[XavcGopBReferenceType] = None
    GopClosedCadence: Optional[int] = None
    HrdBufferSize: Optional[int] = None
    QualityTuningLevel: Optional[Xavc4kProfileQualityTuningLevelType] = None
    Slices: Optional[int] = None

class XavcHdIntraCbgProfileSettingsTypeDef(BaseModel):
    XavcClass: Optional[XavcHdIntraCbgProfileClassType] = None

class XavcHdProfileSettingsTypeDef(BaseModel):
    BitrateClass: Optional[XavcHdProfileBitrateClassType] = None
    FlickerAdaptiveQuantization: Optional[XavcFlickerAdaptiveQuantizationType] = None
    GopBReference: Optional[XavcGopBReferenceType] = None
    GopClosedCadence: Optional[int] = None
    HrdBufferSize: Optional[int] = None
    InterlaceMode: Optional[XavcInterlaceModeType] = None
    QualityTuningLevel: Optional[XavcHdProfileQualityTuningLevelType] = None
    Slices: Optional[int] = None
    Telecine: Optional[XavcHdProfileTelecineType] = None

class AudioCodecSettingsTypeDef(BaseModel):
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

class AutomatedAbrRuleExtraOutputTypeDef(BaseModel):
    AllowedRenditions: Optional[List[AllowedRenditionSizeTypeDef]] = None
    ForceIncludeRenditions: Optional[List[ForceIncludeRenditionSizeTypeDef]] = None
    MinBottomRenditionSize: Optional[MinBottomRenditionSizeTypeDef] = None
    MinTopRenditionSize: Optional[MinTopRenditionSizeTypeDef] = None
    Type: Optional[RuleTypeType] = None

class AutomatedAbrRuleOutputTypeDef(BaseModel):
    AllowedRenditions: Optional[List[AllowedRenditionSizeTypeDef]] = None
    ForceIncludeRenditions: Optional[List[ForceIncludeRenditionSizeTypeDef]] = None
    MinBottomRenditionSize: Optional[MinBottomRenditionSizeTypeDef] = None
    MinTopRenditionSize: Optional[MinTopRenditionSizeTypeDef] = None
    Type: Optional[RuleTypeType] = None

class AutomatedAbrRuleTypeDef(BaseModel):
    AllowedRenditions: Optional[Sequence[AllowedRenditionSizeTypeDef]] = None
    ForceIncludeRenditions: Optional[Sequence[ForceIncludeRenditionSizeTypeDef]] = None
    MinBottomRenditionSize: Optional[MinBottomRenditionSizeTypeDef] = None
    MinTopRenditionSize: Optional[MinTopRenditionSizeTypeDef] = None
    Type: Optional[RuleTypeType] = None

class Av1SettingsTypeDef(BaseModel):
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

class AvcIntraSettingsTypeDef(BaseModel):
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

class CaptionDestinationSettingsExtraOutputTypeDef(BaseModel):
    BurninDestinationSettings: Optional[BurninDestinationSettingsTypeDef] = None
    DestinationType: Optional[CaptionDestinationTypeType] = None
    DvbSubDestinationSettings: Optional[DvbSubDestinationSettingsTypeDef] = None
    EmbeddedDestinationSettings: Optional[EmbeddedDestinationSettingsTypeDef] = None
    ImscDestinationSettings: Optional[ImscDestinationSettingsTypeDef] = None
    SccDestinationSettings: Optional[SccDestinationSettingsTypeDef] = None
    SrtDestinationSettings: Optional[SrtDestinationSettingsTypeDef] = None
    TeletextDestinationSettings: Optional[TeletextDestinationSettingsExtraOutputTypeDef] = None
    TtmlDestinationSettings: Optional[TtmlDestinationSettingsTypeDef] = None
    WebvttDestinationSettings: Optional[WebvttDestinationSettingsTypeDef] = None

class CaptionDestinationSettingsOutputTypeDef(BaseModel):
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

class CaptionDestinationSettingsTypeDef(BaseModel):
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

class FileSourceSettingsTypeDef(BaseModel):
    Convert608To708: Optional[FileSourceConvert608To708Type] = None
    ConvertPaintToPop: Optional[CaptionSourceConvertPaintOnToPopOnType] = None
    Framerate: Optional[CaptionSourceFramerateTypeDef] = None
    SourceFile: Optional[str] = None
    TimeDelta: Optional[int] = None
    TimeDeltaUnits: Optional[FileSourceTimeDeltaUnitsType] = None

class ChannelMappingExtraOutputTypeDef(BaseModel):
    OutputChannels: Optional[List[OutputChannelMappingExtraOutputTypeDef]] = None

class ChannelMappingOutputTypeDef(BaseModel):
    OutputChannels: Optional[List[OutputChannelMappingOutputTypeDef]] = None

class ChannelMappingTypeDef(BaseModel):
    OutputChannels: Optional[Sequence[OutputChannelMappingTypeDef]] = None

class CmafEncryptionSettingsExtraOutputTypeDef(BaseModel):
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionTypeType] = None
    InitializationVectorInManifest: Optional[CmafInitializationVectorInManifestType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderCmafExtraOutputTypeDef] = None
    StaticKeyProvider: Optional[StaticKeyProviderTypeDef] = None
    Type: Optional[CmafKeyProviderTypeType] = None

class CmafEncryptionSettingsOutputTypeDef(BaseModel):
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionTypeType] = None
    InitializationVectorInManifest: Optional[CmafInitializationVectorInManifestType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderCmafOutputTypeDef] = None
    StaticKeyProvider: Optional[StaticKeyProviderTypeDef] = None
    Type: Optional[CmafKeyProviderTypeType] = None

class CmafEncryptionSettingsTypeDef(BaseModel):
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionTypeType] = None
    InitializationVectorInManifest: Optional[CmafInitializationVectorInManifestType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderCmafTypeDef] = None
    StaticKeyProvider: Optional[StaticKeyProviderTypeDef] = None
    Type: Optional[CmafKeyProviderTypeType] = None

class ColorCorrectorTypeDef(BaseModel):
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

class VideoSelectorTypeDef(BaseModel):
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

class CreateQueueRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    PricingPlan: Optional[PricingPlanType] = None
    ReservationPlanSettings: Optional[ReservationPlanSettingsTypeDef] = None
    Status: Optional[QueueStatusType] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateQueueRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    ReservationPlanSettings: Optional[ReservationPlanSettingsTypeDef] = None
    Status: Optional[QueueStatusType] = None

class DashIsoEncryptionSettingsExtraOutputTypeDef(BaseModel):
    PlaybackDeviceCompatibility: Optional[DashIsoPlaybackDeviceCompatibilityType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderExtraOutputTypeDef] = None

class HlsEncryptionSettingsExtraOutputTypeDef(BaseModel):
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[HlsEncryptionTypeType] = None
    InitializationVectorInManifest: Optional[HlsInitializationVectorInManifestType] = None
    OfflineEncrypted: Optional[HlsOfflineEncryptedType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderExtraOutputTypeDef] = None
    StaticKeyProvider: Optional[StaticKeyProviderTypeDef] = None
    Type: Optional[HlsKeyProviderTypeType] = None

class MsSmoothEncryptionSettingsExtraOutputTypeDef(BaseModel):
    SpekeKeyProvider: Optional[SpekeKeyProviderExtraOutputTypeDef] = None

class DashIsoEncryptionSettingsOutputTypeDef(BaseModel):
    PlaybackDeviceCompatibility: Optional[DashIsoPlaybackDeviceCompatibilityType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderOutputTypeDef] = None

class HlsEncryptionSettingsOutputTypeDef(BaseModel):
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[HlsEncryptionTypeType] = None
    InitializationVectorInManifest: Optional[HlsInitializationVectorInManifestType] = None
    OfflineEncrypted: Optional[HlsOfflineEncryptedType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderOutputTypeDef] = None
    StaticKeyProvider: Optional[StaticKeyProviderTypeDef] = None
    Type: Optional[HlsKeyProviderTypeType] = None

class MsSmoothEncryptionSettingsOutputTypeDef(BaseModel):
    SpekeKeyProvider: Optional[SpekeKeyProviderOutputTypeDef] = None

class DashIsoEncryptionSettingsTypeDef(BaseModel):
    PlaybackDeviceCompatibility: Optional[DashIsoPlaybackDeviceCompatibilityType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderTypeDef] = None

class HlsEncryptionSettingsTypeDef(BaseModel):
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[HlsEncryptionTypeType] = None
    InitializationVectorInManifest: Optional[HlsInitializationVectorInManifestType] = None
    OfflineEncrypted: Optional[HlsOfflineEncryptedType] = None
    SpekeKeyProvider: Optional[SpekeKeyProviderTypeDef] = None
    StaticKeyProvider: Optional[StaticKeyProviderTypeDef] = None
    Type: Optional[HlsKeyProviderTypeType] = None

class MsSmoothEncryptionSettingsTypeDef(BaseModel):
    SpekeKeyProvider: Optional[SpekeKeyProviderTypeDef] = None

class DescribeEndpointsRequestDescribeEndpointsPaginateTypeDef(BaseModel):
    Mode: Optional[DescribeEndpointsModeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobTemplatesRequestListJobTemplatesPaginateTypeDef(BaseModel):
    Category: Optional[str] = None
    ListBy: Optional[JobTemplateListByType] = None
    Order: Optional[OrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseModel):
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPresetsRequestListPresetsPaginateTypeDef(BaseModel):
    Category: Optional[str] = None
    ListBy: Optional[PresetListByType] = None
    Order: Optional[OrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueuesRequestListQueuesPaginateTypeDef(BaseModel):
    ListBy: Optional[QueueListByType] = None
    Order: Optional[OrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchJobsRequestSearchJobsPaginateTypeDef(BaseModel):
    InputFile: Optional[str] = None
    Order: Optional[OrderType] = None
    Queue: Optional[str] = None
    Status: Optional[JobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEndpointsResponseTypeDef(BaseModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DolbyVisionTypeDef(BaseModel):
    L6Metadata: Optional[DolbyVisionLevel6MetadataTypeDef] = None
    L6Mode: Optional[DolbyVisionLevel6ModeType] = None
    Mapping: Optional[DolbyVisionMappingType] = None
    Profile: Optional[DolbyVisionProfileType] = None

class EsamSettingsTypeDef(BaseModel):
    ManifestConfirmConditionNotification: Optional[       EsamManifestConfirmConditionNotificationTypeDef     ] = None
    ResponseSignalPreroll: Optional[int] = None
    SignalProcessingNotification: Optional[EsamSignalProcessingNotificationTypeDef] = None

class GetPolicyResponseTypeDef(BaseModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutPolicyRequestRequestTypeDef(BaseModel):
    Policy: PolicyTypeDef

class PutPolicyResponseTypeDef(BaseModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class H264SettingsTypeDef(BaseModel):
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

class H265SettingsTypeDef(BaseModel):
    AdaptiveQuantization: Optional[H265AdaptiveQuantizationType] = None
    AlternateTransferFunctionSei: Optional[H265AlternateTransferFunctionSeiType] = None
    BandwidthReductionFilter: Optional[BandwidthReductionFilterTypeDef] = None
    Bitrate: Optional[int] = None
    CodecLevel: Optional[H265CodecLevelType] = None
    CodecProfile: Optional[H265CodecProfileType] = None
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

class OutputSettingsTypeDef(BaseModel):
    HlsSettings: Optional[HlsSettingsTypeDef] = None

class TimedMetadataInsertionExtraOutputTypeDef(BaseModel):
    Id3Insertions: Optional[List[Id3InsertionTypeDef]] = None

class TimedMetadataInsertionOutputTypeDef(BaseModel):
    Id3Insertions: Optional[List[Id3InsertionTypeDef]] = None

class TimedMetadataInsertionTypeDef(BaseModel):
    Id3Insertions: Optional[Sequence[Id3InsertionTypeDef]] = None

class ImageInserterExtraOutputTypeDef(BaseModel):
    InsertableImages: Optional[List[InsertableImageTypeDef]] = None
    SdrReferenceWhiteLevel: Optional[int] = None

class ImageInserterOutputTypeDef(BaseModel):
    InsertableImages: Optional[List[InsertableImageTypeDef]] = None
    SdrReferenceWhiteLevel: Optional[int] = None

class ImageInserterTypeDef(BaseModel):
    InsertableImages: Optional[Sequence[InsertableImageTypeDef]] = None
    SdrReferenceWhiteLevel: Optional[int] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    ResourceTags: ResourceTagsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class M2tsSettingsExtraOutputTypeDef(BaseModel):
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

class M2tsSettingsOutputTypeDef(BaseModel):
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

class M2tsSettingsTypeDef(BaseModel):
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

class MotionImageInserterTypeDef(BaseModel):
    Framerate: Optional[MotionImageInsertionFramerateTypeDef] = None
    Input: Optional[str] = None
    InsertionMode: Optional[MotionImageInsertionModeType] = None
    Offset: Optional[MotionImageInsertionOffsetTypeDef] = None
    Playback: Optional[MotionImagePlaybackType] = None
    StartTime: Optional[str] = None

class MxfSettingsTypeDef(BaseModel):
    AfdSignaling: Optional[MxfAfdSignalingType] = None
    Profile: Optional[MxfProfileType] = None
    XavcProfileSettings: Optional[MxfXavcProfileSettingsTypeDef] = None

class PartnerWatermarkingTypeDef(BaseModel):
    NexguardFileMarkerSettings: Optional[NexGuardFileMarkerSettingsTypeDef] = None

class NoiseReducerTypeDef(BaseModel):
    Filter: Optional[NoiseReducerFilterType] = None
    FilterSettings: Optional[NoiseReducerFilterSettingsTypeDef] = None
    SpatialFilterSettings: Optional[NoiseReducerSpatialFilterSettingsTypeDef] = None
    TemporalFilterSettings: Optional[NoiseReducerTemporalFilterSettingsTypeDef] = None

class OutputDetailTypeDef(BaseModel):
    DurationInMs: Optional[int] = None
    VideoDetails: Optional[VideoDetailTypeDef] = None

class QueueTypeDef(BaseModel):
    Name: str
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None
    PricingPlan: Optional[PricingPlanType] = None
    ProgressingJobsCount: Optional[int] = None
    ReservationPlan: Optional[ReservationPlanTypeDef] = None
    Status: Optional[QueueStatusType] = None
    SubmittedJobsCount: Optional[int] = None
    Type: Optional[TypeType] = None

class S3DestinationSettingsTypeDef(BaseModel):
    AccessControl: Optional[S3DestinationAccessControlTypeDef] = None
    Encryption: Optional[S3EncryptionSettingsTypeDef] = None
    StorageClass: Optional[S3StorageClassType] = None

class VideoOverlayInputExtraOutputTypeDef(BaseModel):
    FileInput: Optional[str] = None
    InputClippings: Optional[List[VideoOverlayInputClippingTypeDef]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None

class VideoOverlayInputOutputTypeDef(BaseModel):
    FileInput: Optional[str] = None
    InputClippings: Optional[List[VideoOverlayInputClippingTypeDef]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None

class VideoOverlayInputTypeDef(BaseModel):
    FileInput: Optional[str] = None
    InputClippings: Optional[Sequence[VideoOverlayInputClippingTypeDef]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None

class XavcSettingsTypeDef(BaseModel):
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

class AutomatedAbrSettingsExtraOutputTypeDef(BaseModel):
    MaxAbrBitrate: Optional[int] = None
    MaxRenditions: Optional[int] = None
    MinAbrBitrate: Optional[int] = None
    Rules: Optional[List[AutomatedAbrRuleExtraOutputTypeDef]] = None

class AutomatedAbrSettingsOutputTypeDef(BaseModel):
    MaxAbrBitrate: Optional[int] = None
    MaxRenditions: Optional[int] = None
    MinAbrBitrate: Optional[int] = None
    Rules: Optional[List[AutomatedAbrRuleOutputTypeDef]] = None

class AutomatedAbrSettingsTypeDef(BaseModel):
    MaxAbrBitrate: Optional[int] = None
    MaxRenditions: Optional[int] = None
    MinAbrBitrate: Optional[int] = None
    Rules: Optional[Sequence[AutomatedAbrRuleTypeDef]] = None

class CaptionDescriptionPresetExtraOutputTypeDef(BaseModel):
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettingsExtraOutputTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None

class CaptionDescriptionPresetOutputTypeDef(BaseModel):
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettingsOutputTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None

class CaptionDescriptionPresetTypeDef(BaseModel):
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettingsTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None

class CaptionDescriptionTypeDef(BaseModel):
    CaptionSelectorName: Optional[str] = None
    CustomLanguageCode: Optional[str] = None
    DestinationSettings: Optional[CaptionDestinationSettingsTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageDescription: Optional[str] = None

class CaptionSourceSettingsTypeDef(BaseModel):
    AncillarySourceSettings: Optional[AncillarySourceSettingsTypeDef] = None
    DvbSubSourceSettings: Optional[DvbSubSourceSettingsTypeDef] = None
    EmbeddedSourceSettings: Optional[EmbeddedSourceSettingsTypeDef] = None
    FileSourceSettings: Optional[FileSourceSettingsTypeDef] = None
    SourceType: Optional[CaptionSourceTypeType] = None
    TeletextSourceSettings: Optional[TeletextSourceSettingsTypeDef] = None
    TrackSourceSettings: Optional[TrackSourceSettingsTypeDef] = None
    WebvttHlsSourceSettings: Optional[WebvttHlsSourceSettingsTypeDef] = None

class RemixSettingsExtraOutputTypeDef(BaseModel):
    AudioDescriptionAudioChannel: Optional[int] = None
    AudioDescriptionDataChannel: Optional[int] = None
    ChannelMapping: Optional[ChannelMappingExtraOutputTypeDef] = None
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None

class RemixSettingsOutputTypeDef(BaseModel):
    AudioDescriptionAudioChannel: Optional[int] = None
    AudioDescriptionDataChannel: Optional[int] = None
    ChannelMapping: Optional[ChannelMappingOutputTypeDef] = None
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None

class RemixSettingsTypeDef(BaseModel):
    AudioDescriptionAudioChannel: Optional[int] = None
    AudioDescriptionDataChannel: Optional[int] = None
    ChannelMapping: Optional[ChannelMappingTypeDef] = None
    ChannelsIn: Optional[int] = None
    ChannelsOut: Optional[int] = None

class ContainerSettingsExtraOutputTypeDef(BaseModel):
    CmfcSettings: Optional[CmfcSettingsTypeDef] = None
    Container: Optional[ContainerTypeType] = None
    F4vSettings: Optional[F4vSettingsTypeDef] = None
    M2tsSettings: Optional[M2tsSettingsExtraOutputTypeDef] = None
    M3u8Settings: Optional[M3u8SettingsExtraOutputTypeDef] = None
    MovSettings: Optional[MovSettingsTypeDef] = None
    Mp4Settings: Optional[Mp4SettingsTypeDef] = None
    MpdSettings: Optional[MpdSettingsTypeDef] = None
    MxfSettings: Optional[MxfSettingsTypeDef] = None

class ContainerSettingsOutputTypeDef(BaseModel):
    CmfcSettings: Optional[CmfcSettingsTypeDef] = None
    Container: Optional[ContainerTypeType] = None
    F4vSettings: Optional[F4vSettingsTypeDef] = None
    M2tsSettings: Optional[M2tsSettingsOutputTypeDef] = None
    M3u8Settings: Optional[M3u8SettingsOutputTypeDef] = None
    MovSettings: Optional[MovSettingsTypeDef] = None
    Mp4Settings: Optional[Mp4SettingsTypeDef] = None
    MpdSettings: Optional[MpdSettingsTypeDef] = None
    MxfSettings: Optional[MxfSettingsTypeDef] = None

class ContainerSettingsTypeDef(BaseModel):
    CmfcSettings: Optional[CmfcSettingsTypeDef] = None
    Container: Optional[ContainerTypeType] = None
    F4vSettings: Optional[F4vSettingsTypeDef] = None
    M2tsSettings: Optional[M2tsSettingsTypeDef] = None
    M3u8Settings: Optional[M3u8SettingsTypeDef] = None
    MovSettings: Optional[MovSettingsTypeDef] = None
    Mp4Settings: Optional[Mp4SettingsTypeDef] = None
    MpdSettings: Optional[MpdSettingsTypeDef] = None
    MxfSettings: Optional[MxfSettingsTypeDef] = None

class VideoPreprocessorExtraOutputTypeDef(BaseModel):
    ColorCorrector: Optional[ColorCorrectorTypeDef] = None
    Deinterlacer: Optional[DeinterlacerTypeDef] = None
    DolbyVision: Optional[DolbyVisionTypeDef] = None
    Hdr10Plus: Optional[Hdr10PlusTypeDef] = None
    ImageInserter: Optional[ImageInserterExtraOutputTypeDef] = None
    NoiseReducer: Optional[NoiseReducerTypeDef] = None
    PartnerWatermarking: Optional[PartnerWatermarkingTypeDef] = None
    TimecodeBurnin: Optional[TimecodeBurninTypeDef] = None

class VideoPreprocessorOutputTypeDef(BaseModel):
    ColorCorrector: Optional[ColorCorrectorTypeDef] = None
    Deinterlacer: Optional[DeinterlacerTypeDef] = None
    DolbyVision: Optional[DolbyVisionTypeDef] = None
    Hdr10Plus: Optional[Hdr10PlusTypeDef] = None
    ImageInserter: Optional[ImageInserterOutputTypeDef] = None
    NoiseReducer: Optional[NoiseReducerTypeDef] = None
    PartnerWatermarking: Optional[PartnerWatermarkingTypeDef] = None
    TimecodeBurnin: Optional[TimecodeBurninTypeDef] = None

class VideoPreprocessorTypeDef(BaseModel):
    ColorCorrector: Optional[ColorCorrectorTypeDef] = None
    Deinterlacer: Optional[DeinterlacerTypeDef] = None
    DolbyVision: Optional[DolbyVisionTypeDef] = None
    Hdr10Plus: Optional[Hdr10PlusTypeDef] = None
    ImageInserter: Optional[ImageInserterTypeDef] = None
    NoiseReducer: Optional[NoiseReducerTypeDef] = None
    PartnerWatermarking: Optional[PartnerWatermarkingTypeDef] = None
    TimecodeBurnin: Optional[TimecodeBurninTypeDef] = None

class OutputGroupDetailTypeDef(BaseModel):
    OutputDetails: Optional[List[OutputDetailTypeDef]] = None

class CreateQueueResponseTypeDef(BaseModel):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueResponseTypeDef(BaseModel):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueuesResponseTypeDef(BaseModel):
    Queues: List[QueueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateQueueResponseTypeDef(BaseModel):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationSettingsTypeDef(BaseModel):
    S3Settings: Optional[S3DestinationSettingsTypeDef] = None

class VideoOverlayExtraOutputTypeDef(BaseModel):
    EndTimecode: Optional[str] = None
    Input: Optional[VideoOverlayInputExtraOutputTypeDef] = None
    StartTimecode: Optional[str] = None

class VideoOverlayOutputTypeDef(BaseModel):
    EndTimecode: Optional[str] = None
    Input: Optional[VideoOverlayInputOutputTypeDef] = None
    StartTimecode: Optional[str] = None

class VideoOverlayTypeDef(BaseModel):
    EndTimecode: Optional[str] = None
    Input: Optional[VideoOverlayInputTypeDef] = None
    StartTimecode: Optional[str] = None

class VideoCodecSettingsTypeDef(BaseModel):
    Av1Settings: Optional[Av1SettingsTypeDef] = None
    AvcIntraSettings: Optional[AvcIntraSettingsTypeDef] = None
    Codec: Optional[VideoCodecType] = None
    FrameCaptureSettings: Optional[FrameCaptureSettingsTypeDef] = None
    H264Settings: Optional[H264SettingsTypeDef] = None
    H265Settings: Optional[H265SettingsTypeDef] = None
    Mpeg2Settings: Optional[Mpeg2SettingsTypeDef] = None
    ProresSettings: Optional[ProresSettingsTypeDef] = None
    UncompressedSettings: Optional[UncompressedSettingsTypeDef] = None
    Vc3Settings: Optional[Vc3SettingsTypeDef] = None
    Vp8Settings: Optional[Vp8SettingsTypeDef] = None
    Vp9Settings: Optional[Vp9SettingsTypeDef] = None
    XavcSettings: Optional[XavcSettingsTypeDef] = None

class AutomatedEncodingSettingsExtraOutputTypeDef(BaseModel):
    AbrSettings: Optional[AutomatedAbrSettingsExtraOutputTypeDef] = None

class AutomatedEncodingSettingsOutputTypeDef(BaseModel):
    AbrSettings: Optional[AutomatedAbrSettingsOutputTypeDef] = None

class AutomatedEncodingSettingsTypeDef(BaseModel):
    AbrSettings: Optional[AutomatedAbrSettingsTypeDef] = None

class CaptionSelectorTypeDef(BaseModel):
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    SourceSettings: Optional[CaptionSourceSettingsTypeDef] = None

class AudioDescriptionExtraOutputTypeDef(BaseModel):
    AudioChannelTaggingSettings: Optional[AudioChannelTaggingSettingsExtraOutputTypeDef] = None
    AudioNormalizationSettings: Optional[AudioNormalizationSettingsTypeDef] = None
    AudioSourceName: Optional[str] = None
    AudioType: Optional[int] = None
    AudioTypeControl: Optional[AudioTypeControlType] = None
    CodecSettings: Optional[AudioCodecSettingsTypeDef] = None
    CustomLanguageCode: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageCodeControl: Optional[AudioLanguageCodeControlType] = None
    RemixSettings: Optional[RemixSettingsExtraOutputTypeDef] = None
    StreamName: Optional[str] = None

class AudioSelectorExtraOutputTypeDef(BaseModel):
    AudioDurationCorrection: Optional[AudioDurationCorrectionType] = None
    CustomLanguageCode: Optional[str] = None
    DefaultSelection: Optional[AudioDefaultSelectionType] = None
    ExternalAudioFileInput: Optional[str] = None
    HlsRenditionGroupSettings: Optional[HlsRenditionGroupSettingsTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    Offset: Optional[int] = None
    Pids: Optional[List[int]] = None
    ProgramSelection: Optional[int] = None
    RemixSettings: Optional[RemixSettingsExtraOutputTypeDef] = None
    SelectorType: Optional[AudioSelectorTypeType] = None
    Tracks: Optional[List[int]] = None

class AudioDescriptionOutputTypeDef(BaseModel):
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

class AudioSelectorOutputTypeDef(BaseModel):
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

class AudioDescriptionTypeDef(BaseModel):
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

class AudioSelectorTypeDef(BaseModel):
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

class CmafGroupSettingsExtraOutputTypeDef(BaseModel):
    AdditionalManifests: Optional[List[CmafAdditionalManifestExtraOutputTypeDef]] = None
    BaseUrl: Optional[str] = None
    ClientCache: Optional[CmafClientCacheType] = None
    CodecSpecification: Optional[CmafCodecSpecificationType] = None
    DashIFrameTrickPlayNameModifier: Optional[str] = None
    DashManifestStyle: Optional[DashManifestStyleType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[CmafEncryptionSettingsExtraOutputTypeDef] = None
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
    WriteSegmentTimelineInRepresentation: Optional[       CmafWriteSegmentTimelineInRepresentationType     ] = None

class CmafGroupSettingsOutputTypeDef(BaseModel):
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
    WriteSegmentTimelineInRepresentation: Optional[       CmafWriteSegmentTimelineInRepresentationType     ] = None

class CmafGroupSettingsTypeDef(BaseModel):
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
    WriteSegmentTimelineInRepresentation: Optional[       CmafWriteSegmentTimelineInRepresentationType     ] = None

class DashIsoGroupSettingsExtraOutputTypeDef(BaseModel):
    AdditionalManifests: Optional[List[DashAdditionalManifestExtraOutputTypeDef]] = None
    AudioChannelConfigSchemeIdUri: Optional[DashIsoGroupAudioChannelConfigSchemeIdUriType] = None
    BaseUrl: Optional[str] = None
    DashIFrameTrickPlayNameModifier: Optional[str] = None
    DashManifestStyle: Optional[DashManifestStyleType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[DashIsoEncryptionSettingsExtraOutputTypeDef] = None
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
    WriteSegmentTimelineInRepresentation: Optional[       DashIsoWriteSegmentTimelineInRepresentationType     ] = None

class DashIsoGroupSettingsOutputTypeDef(BaseModel):
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
    WriteSegmentTimelineInRepresentation: Optional[       DashIsoWriteSegmentTimelineInRepresentationType     ] = None

class DashIsoGroupSettingsTypeDef(BaseModel):
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
    WriteSegmentTimelineInRepresentation: Optional[       DashIsoWriteSegmentTimelineInRepresentationType     ] = None

class FileGroupSettingsTypeDef(BaseModel):
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None

class HlsGroupSettingsExtraOutputTypeDef(BaseModel):
    AdMarkers: Optional[List[HlsAdMarkersType]] = None
    AdditionalManifests: Optional[List[HlsAdditionalManifestExtraOutputTypeDef]] = None
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
    Encryption: Optional[HlsEncryptionSettingsExtraOutputTypeDef] = None
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

class HlsGroupSettingsOutputTypeDef(BaseModel):
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

class HlsGroupSettingsTypeDef(BaseModel):
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

class MsSmoothGroupSettingsExtraOutputTypeDef(BaseModel):
    AdditionalManifests: Optional[List[MsSmoothAdditionalManifestExtraOutputTypeDef]] = None
    AudioDeduplication: Optional[MsSmoothAudioDeduplicationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[MsSmoothEncryptionSettingsExtraOutputTypeDef] = None
    FragmentLength: Optional[int] = None
    FragmentLengthControl: Optional[MsSmoothFragmentLengthControlType] = None
    ManifestEncoding: Optional[MsSmoothManifestEncodingType] = None

class MsSmoothGroupSettingsOutputTypeDef(BaseModel):
    AdditionalManifests: Optional[List[MsSmoothAdditionalManifestOutputTypeDef]] = None
    AudioDeduplication: Optional[MsSmoothAudioDeduplicationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[MsSmoothEncryptionSettingsOutputTypeDef] = None
    FragmentLength: Optional[int] = None
    FragmentLengthControl: Optional[MsSmoothFragmentLengthControlType] = None
    ManifestEncoding: Optional[MsSmoothManifestEncodingType] = None

class MsSmoothGroupSettingsTypeDef(BaseModel):
    AdditionalManifests: Optional[Sequence[MsSmoothAdditionalManifestTypeDef]] = None
    AudioDeduplication: Optional[MsSmoothAudioDeduplicationType] = None
    Destination: Optional[str] = None
    DestinationSettings: Optional[DestinationSettingsTypeDef] = None
    Encryption: Optional[MsSmoothEncryptionSettingsTypeDef] = None
    FragmentLength: Optional[int] = None
    FragmentLengthControl: Optional[MsSmoothFragmentLengthControlType] = None
    ManifestEncoding: Optional[MsSmoothManifestEncodingType] = None

class VideoDescriptionExtraOutputTypeDef(BaseModel):
    AfdSignaling: Optional[AfdSignalingType] = None
    AntiAlias: Optional[AntiAliasType] = None
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
    VideoPreprocessors: Optional[VideoPreprocessorExtraOutputTypeDef] = None
    Width: Optional[int] = None

class VideoDescriptionOutputTypeDef(BaseModel):
    AfdSignaling: Optional[AfdSignalingType] = None
    AntiAlias: Optional[AntiAliasType] = None
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
    VideoPreprocessors: Optional[VideoPreprocessorOutputTypeDef] = None
    Width: Optional[int] = None

class VideoDescriptionTypeDef(BaseModel):
    AfdSignaling: Optional[AfdSignalingType] = None
    AntiAlias: Optional[AntiAliasType] = None
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
    VideoPreprocessors: Optional[VideoPreprocessorTypeDef] = None
    Width: Optional[int] = None

class InputExtraOutputTypeDef(BaseModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettingsTypeDef] = None
    AudioSelectorGroups: Optional[Dict[str, AudioSelectorGroupExtraOutputTypeDef]] = None
    AudioSelectors: Optional[Dict[str, AudioSelectorExtraOutputTypeDef]] = None
    CaptionSelectors: Optional[Dict[str, CaptionSelectorTypeDef]] = None
    Crop: Optional[RectangleTypeDef] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DecryptionSettings: Optional[InputDecryptionSettingsTypeDef] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
    FileInput: Optional[str] = None
    FilterEnable: Optional[InputFilterEnableType] = None
    FilterStrength: Optional[int] = None
    ImageInserter: Optional[ImageInserterExtraOutputTypeDef] = None
    InputClippings: Optional[List[InputClippingTypeDef]] = None
    InputScanType: Optional[InputScanTypeType] = None
    Position: Optional[RectangleTypeDef] = None
    ProgramNumber: Optional[int] = None
    PsiControl: Optional[InputPsiControlType] = None
    SupplementalImps: Optional[List[str]] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None
    VideoGenerator: Optional[InputVideoGeneratorTypeDef] = None
    VideoOverlays: Optional[List[VideoOverlayExtraOutputTypeDef]] = None
    VideoSelector: Optional[VideoSelectorTypeDef] = None

class InputTemplateExtraOutputTypeDef(BaseModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettingsTypeDef] = None
    AudioSelectorGroups: Optional[Dict[str, AudioSelectorGroupExtraOutputTypeDef]] = None
    AudioSelectors: Optional[Dict[str, AudioSelectorExtraOutputTypeDef]] = None
    CaptionSelectors: Optional[Dict[str, CaptionSelectorTypeDef]] = None
    Crop: Optional[RectangleTypeDef] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
    FilterEnable: Optional[InputFilterEnableType] = None
    FilterStrength: Optional[int] = None
    ImageInserter: Optional[ImageInserterExtraOutputTypeDef] = None
    InputClippings: Optional[List[InputClippingTypeDef]] = None
    InputScanType: Optional[InputScanTypeType] = None
    Position: Optional[RectangleTypeDef] = None
    ProgramNumber: Optional[int] = None
    PsiControl: Optional[InputPsiControlType] = None
    TimecodeSource: Optional[InputTimecodeSourceType] = None
    TimecodeStart: Optional[str] = None
    VideoOverlays: Optional[List[VideoOverlayExtraOutputTypeDef]] = None
    VideoSelector: Optional[VideoSelectorTypeDef] = None

class InputOutputTypeDef(BaseModel):
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

class InputTemplateOutputTypeDef(BaseModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettingsTypeDef] = None
    AudioSelectorGroups: Optional[Dict[str, AudioSelectorGroupOutputTypeDef]] = None
    AudioSelectors: Optional[Dict[str, AudioSelectorOutputTypeDef]] = None
    CaptionSelectors: Optional[Dict[str, CaptionSelectorTypeDef]] = None
    Crop: Optional[RectangleTypeDef] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
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

class InputTemplateTypeDef(BaseModel):
    AdvancedInputFilter: Optional[AdvancedInputFilterType] = None
    AdvancedInputFilterSettings: Optional[AdvancedInputFilterSettingsTypeDef] = None
    AudioSelectorGroups: Optional[Mapping[str, AudioSelectorGroupTypeDef]] = None
    AudioSelectors: Optional[Mapping[str, AudioSelectorTypeDef]] = None
    CaptionSelectors: Optional[Mapping[str, CaptionSelectorTypeDef]] = None
    Crop: Optional[RectangleTypeDef] = None
    DeblockFilter: Optional[InputDeblockFilterType] = None
    DenoiseFilter: Optional[InputDenoiseFilterType] = None
    DolbyVisionMetadataXml: Optional[str] = None
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

class InputTypeDef(BaseModel):
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

class OutputGroupSettingsExtraOutputTypeDef(BaseModel):
    CmafGroupSettings: Optional[CmafGroupSettingsExtraOutputTypeDef] = None
    DashIsoGroupSettings: Optional[DashIsoGroupSettingsExtraOutputTypeDef] = None
    FileGroupSettings: Optional[FileGroupSettingsTypeDef] = None
    HlsGroupSettings: Optional[HlsGroupSettingsExtraOutputTypeDef] = None
    MsSmoothGroupSettings: Optional[MsSmoothGroupSettingsExtraOutputTypeDef] = None
    Type: Optional[OutputGroupTypeType] = None

class OutputGroupSettingsOutputTypeDef(BaseModel):
    CmafGroupSettings: Optional[CmafGroupSettingsOutputTypeDef] = None
    DashIsoGroupSettings: Optional[DashIsoGroupSettingsOutputTypeDef] = None
    FileGroupSettings: Optional[FileGroupSettingsTypeDef] = None
    HlsGroupSettings: Optional[HlsGroupSettingsOutputTypeDef] = None
    MsSmoothGroupSettings: Optional[MsSmoothGroupSettingsOutputTypeDef] = None
    Type: Optional[OutputGroupTypeType] = None

class OutputGroupSettingsTypeDef(BaseModel):
    CmafGroupSettings: Optional[CmafGroupSettingsTypeDef] = None
    DashIsoGroupSettings: Optional[DashIsoGroupSettingsTypeDef] = None
    FileGroupSettings: Optional[FileGroupSettingsTypeDef] = None
    HlsGroupSettings: Optional[HlsGroupSettingsTypeDef] = None
    MsSmoothGroupSettings: Optional[MsSmoothGroupSettingsTypeDef] = None
    Type: Optional[OutputGroupTypeType] = None

class PresetSettingsExtraOutputTypeDef(BaseModel):
    AudioDescriptions: Optional[List[AudioDescriptionExtraOutputTypeDef]] = None
    CaptionDescriptions: Optional[List[CaptionDescriptionPresetExtraOutputTypeDef]] = None
    ContainerSettings: Optional[ContainerSettingsExtraOutputTypeDef] = None
    VideoDescription: Optional[VideoDescriptionExtraOutputTypeDef] = None

class PresetSettingsOutputTypeDef(BaseModel):
    AudioDescriptions: Optional[List[AudioDescriptionOutputTypeDef]] = None
    CaptionDescriptions: Optional[List[CaptionDescriptionPresetOutputTypeDef]] = None
    ContainerSettings: Optional[ContainerSettingsOutputTypeDef] = None
    VideoDescription: Optional[VideoDescriptionOutputTypeDef] = None

class OutputTypeDef(BaseModel):
    AudioDescriptions: Optional[Sequence[AudioDescriptionTypeDef]] = None
    CaptionDescriptions: Optional[Sequence[CaptionDescriptionTypeDef]] = None
    ContainerSettings: Optional[ContainerSettingsTypeDef] = None
    Extension: Optional[str] = None
    NameModifier: Optional[str] = None
    OutputSettings: Optional[OutputSettingsTypeDef] = None
    Preset: Optional[str] = None
    VideoDescription: Optional[VideoDescriptionTypeDef] = None

class PresetSettingsTypeDef(BaseModel):
    AudioDescriptions: Optional[Sequence[AudioDescriptionTypeDef]] = None
    CaptionDescriptions: Optional[Sequence[CaptionDescriptionPresetTypeDef]] = None
    ContainerSettings: Optional[ContainerSettingsTypeDef] = None
    VideoDescription: Optional[VideoDescriptionTypeDef] = None

class PresetTypeDef(BaseModel):
    Name: str
    Settings: PresetSettingsOutputTypeDef
    Arn: Optional[str] = None
    Category: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None
    Type: Optional[TypeType] = None

class OutputGroupExtraOutputTypeDef(BaseModel):
    AutomatedEncodingSettings: Optional[AutomatedEncodingSettingsExtraOutputTypeDef] = None
    CustomName: Optional[str] = None
    Name: Optional[str] = None
    OutputGroupSettings: Optional[OutputGroupSettingsExtraOutputTypeDef] = None
    Outputs: Optional[List[OutputTypeDef]] = None

class OutputGroupOutputTypeDef(BaseModel):
    AutomatedEncodingSettings: Optional[AutomatedEncodingSettingsOutputTypeDef] = None
    CustomName: Optional[str] = None
    Name: Optional[str] = None
    OutputGroupSettings: Optional[OutputGroupSettingsOutputTypeDef] = None
    Outputs: Optional[List[OutputTypeDef]] = None

class OutputGroupTypeDef(BaseModel):
    AutomatedEncodingSettings: Optional[AutomatedEncodingSettingsTypeDef] = None
    CustomName: Optional[str] = None
    Name: Optional[str] = None
    OutputGroupSettings: Optional[OutputGroupSettingsTypeDef] = None
    Outputs: Optional[Sequence[OutputTypeDef]] = None

class CreatePresetRequestRequestTypeDef(BaseModel):
    Name: str
    Settings: PresetSettingsTypeDef
    Category: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdatePresetRequestRequestTypeDef(BaseModel):
    Name: str
    Category: Optional[str] = None
    Description: Optional[str] = None
    Settings: Optional[PresetSettingsTypeDef] = None

class CreatePresetResponseTypeDef(BaseModel):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPresetResponseTypeDef(BaseModel):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPresetsResponseTypeDef(BaseModel):
    Presets: List[PresetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdatePresetResponseTypeDef(BaseModel):
    Preset: PresetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobSettingsExtraOutputTypeDef(BaseModel):
    AdAvailOffset: Optional[int] = None
    AvailBlanking: Optional[AvailBlankingTypeDef] = None
    ColorConversion3DLUTSettings: Optional[List[ColorConversion3DLUTSettingTypeDef]] = None
    Esam: Optional[EsamSettingsTypeDef] = None
    ExtendedDataServices: Optional[ExtendedDataServicesTypeDef] = None
    FollowSource: Optional[int] = None
    Inputs: Optional[List[InputExtraOutputTypeDef]] = None
    KantarWatermark: Optional[KantarWatermarkSettingsTypeDef] = None
    MotionImageInserter: Optional[MotionImageInserterTypeDef] = None
    NielsenConfiguration: Optional[NielsenConfigurationTypeDef] = None
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettingsTypeDef] = None
    OutputGroups: Optional[List[OutputGroupExtraOutputTypeDef]] = None
    TimecodeConfig: Optional[TimecodeConfigTypeDef] = None
    TimedMetadataInsertion: Optional[TimedMetadataInsertionExtraOutputTypeDef] = None

class JobTemplateSettingsExtraOutputTypeDef(BaseModel):
    AdAvailOffset: Optional[int] = None
    AvailBlanking: Optional[AvailBlankingTypeDef] = None
    ColorConversion3DLUTSettings: Optional[List[ColorConversion3DLUTSettingTypeDef]] = None
    Esam: Optional[EsamSettingsTypeDef] = None
    ExtendedDataServices: Optional[ExtendedDataServicesTypeDef] = None
    FollowSource: Optional[int] = None
    Inputs: Optional[List[InputTemplateExtraOutputTypeDef]] = None
    KantarWatermark: Optional[KantarWatermarkSettingsTypeDef] = None
    MotionImageInserter: Optional[MotionImageInserterTypeDef] = None
    NielsenConfiguration: Optional[NielsenConfigurationTypeDef] = None
    NielsenNonLinearWatermark: Optional[NielsenNonLinearWatermarkSettingsTypeDef] = None
    OutputGroups: Optional[List[OutputGroupExtraOutputTypeDef]] = None
    TimecodeConfig: Optional[TimecodeConfigTypeDef] = None
    TimedMetadataInsertion: Optional[TimedMetadataInsertionExtraOutputTypeDef] = None

class JobSettingsOutputTypeDef(BaseModel):
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

class JobTemplateSettingsOutputTypeDef(BaseModel):
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

class JobSettingsTypeDef(BaseModel):
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

class JobTemplateSettingsTypeDef(BaseModel):
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

class JobTypeDef(BaseModel):
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

class JobTemplateTypeDef(BaseModel):
    Name: str
    Settings: JobTemplateSettingsOutputTypeDef
    AccelerationSettings: Optional[AccelerationSettingsTypeDef] = None
    Arn: Optional[str] = None
    Category: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    HopDestinations: Optional[List[HopDestinationTypeDef]] = None
    LastUpdated: Optional[datetime] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None
    Type: Optional[TypeType] = None

class CreateJobRequestRequestTypeDef(BaseModel):
    Role: str
    Settings: JobSettingsTypeDef
    AccelerationSettings: Optional[AccelerationSettingsTypeDef] = None
    BillingTagsSource: Optional[BillingTagsSourceType] = None
    ClientRequestToken: Optional[str] = None
    HopDestinations: Optional[Sequence[HopDestinationTypeDef]] = None
    JobTemplate: Optional[str] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    SimulateReservedQueue: Optional[SimulateReservedQueueType] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None
    Tags: Optional[Mapping[str, str]] = None
    UserMetadata: Optional[Mapping[str, str]] = None

class CreateJobTemplateRequestRequestTypeDef(BaseModel):
    Name: str
    Settings: JobTemplateSettingsTypeDef
    AccelerationSettings: Optional[AccelerationSettingsTypeDef] = None
    Category: Optional[str] = None
    Description: Optional[str] = None
    HopDestinations: Optional[Sequence[HopDestinationTypeDef]] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateJobTemplateRequestRequestTypeDef(BaseModel):
    Name: str
    AccelerationSettings: Optional[AccelerationSettingsTypeDef] = None
    Category: Optional[str] = None
    Description: Optional[str] = None
    HopDestinations: Optional[Sequence[HopDestinationTypeDef]] = None
    Priority: Optional[int] = None
    Queue: Optional[str] = None
    Settings: Optional[JobTemplateSettingsTypeDef] = None
    StatusUpdateInterval: Optional[StatusUpdateIntervalType] = None

class CreateJobResponseTypeDef(BaseModel):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobResponseTypeDef(BaseModel):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResponseTypeDef(BaseModel):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchJobsResponseTypeDef(BaseModel):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateJobTemplateResponseTypeDef(BaseModel):
    JobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobTemplateResponseTypeDef(BaseModel):
    JobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobTemplatesResponseTypeDef(BaseModel):
    JobTemplates: List[JobTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateJobTemplateResponseTypeDef(BaseModel):
    JobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

