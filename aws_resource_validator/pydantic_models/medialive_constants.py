from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AacCodingModeType = Literal["AD_RECEIVER_MIX", "CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_5_1"]
AacInputTypeType = Literal["BROADCASTER_MIXED_AD", "NORMAL"]
AacProfileType = Literal["HEV1", "HEV2", "LC"]
AacRateControlModeType = Literal["CBR", "VBR"]
AacRawFormatType = Literal["LATM_LOAS", "NONE"]
AacSpecType = Literal["MPEG2", "MPEG4"]
AacVbrQualityType = Literal["HIGH", "LOW", "MEDIUM_HIGH", "MEDIUM_LOW"]
Ac3AttenuationControlType = Literal["ATTENUATE_3_DB", "NONE"]
Ac3BitstreamModeType = Literal["COMMENTARY",
    "COMPLETE_MAIN",
    "DIALOGUE",
    "EMERGENCY",
    "HEARING_IMPAIRED",
    "MUSIC_AND_EFFECTS",
    "VISUALLY_IMPAIRED",
    "VOICE_OVER",]
Ac3CodingModeType = Literal["CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_3_2_LFE"]
Ac3DrcProfileType = Literal["FILM_STANDARD", "NONE"]
Ac3LfeFilterType = Literal["DISABLED", "ENABLED"]
Ac3MetadataControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AcceptHeaderType = Literal["image/jpeg"]
AccessibilityTypeType = Literal["DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES", "IMPLEMENTS_ACCESSIBILITY_FEATURES"]
AfdSignalingType = Literal["AUTO", "FIXED", "NONE"]
AudioDescriptionAudioTypeControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AudioDescriptionLanguageCodeControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AudioLanguageSelectionPolicyType = Literal["LOOSE", "STRICT"]
AudioNormalizationAlgorithmControlType = Literal["CORRECT_AUDIO"]
AudioNormalizationAlgorithmType = Literal["ITU_1770_1", "ITU_1770_2"]
AudioOnlyHlsSegmentTypeType = Literal["AAC", "FMP4"]
AudioOnlyHlsTrackTypeType = Literal["ALTERNATE_AUDIO_AUTO_SELECT",
    "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
    "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
    "AUDIO_ONLY_VARIANT_STREAM",]
AudioTypeType = Literal["CLEAN_EFFECTS", "HEARING_IMPAIRED", "UNDEFINED", "VISUAL_IMPAIRED_COMMENTARY"]
AuthenticationSchemeType = Literal["AKAMAI", "COMMON"]
AvailBlankingStateType = Literal["DISABLED", "ENABLED"]
BlackoutSlateNetworkEndBlackoutType = Literal["DISABLED", "ENABLED"]
BlackoutSlateStateType = Literal["DISABLED", "ENABLED"]
BurnInAlignmentType = Literal["CENTERED", "LEFT", "SMART"]
BurnInBackgroundColorType = Literal["BLACK", "NONE", "WHITE"]
BurnInFontColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurnInOutlineColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurnInShadowColorType = Literal["BLACK", "NONE", "WHITE"]
BurnInTeletextGridControlType = Literal["FIXED", "SCALED"]
CdiInputResolutionType = Literal["FHD", "HD", "SD", "UHD"]
ChannelClassType = Literal["SINGLE_PIPELINE", "STANDARD"]
ChannelCreatedWaiterName = Literal["channel_created"]
ChannelDeletedWaiterName = Literal["channel_deleted"]
ChannelPipelineIdToRestartType = Literal["PIPELINE_0", "PIPELINE_1"]
ChannelRunningWaiterName = Literal["channel_running"]
ChannelStateType = Literal["CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "IDLE",
    "RECOVERING",
    "RUNNING",
    "STARTING",
    "STOPPING",
    "UPDATE_FAILED",
    "UPDATING",]
ChannelStoppedWaiterName = Literal["channel_stopped"]
CloudWatchAlarmTemplateComparisonOperatorType = Literal["GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanOrEqualToThreshold",
    "LessThanThreshold",]
CloudWatchAlarmTemplateStatisticType = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
CloudWatchAlarmTemplateTargetResourceTypeType = Literal["CLOUDFRONT_DISTRIBUTION",
    "MEDIACONNECT_FLOW",
    "MEDIALIVE_CHANNEL",
    "MEDIALIVE_INPUT_DEVICE",
    "MEDIALIVE_MULTIPLEX",
    "MEDIAPACKAGE_CHANNEL",
    "MEDIAPACKAGE_ORIGIN_ENDPOINT",
    "S3_BUCKET",]
CloudWatchAlarmTemplateTreatMissingDataType = Literal["breaching", "ignore", "missing", "notBreaching"]
CmafIngestSegmentLengthUnitsType = Literal["MILLISECONDS", "SECONDS"]
CmafNielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
ColorSpaceType = Literal["HDR10", "HLG_2020", "REC_601", "REC_709"]
ContentTypeType = Literal["image/jpeg"]
DashRoleAudioType = Literal["ALTERNATE",
    "COMMENTARY",
    "DESCRIPTION",
    "DUB",
    "EMERGENCY",
    "ENHANCED-AUDIO-INTELLIGIBILITY",
    "KARAOKE",
    "MAIN",
    "SUPPLEMENTARY",]
DashRoleCaptionType = Literal["ALTERNATE",
    "CAPTION",
    "COMMENTARY",
    "DESCRIPTION",
    "DUB",
    "EASYREADER",
    "EMERGENCY",
    "FORCED-SUBTITLE",
    "KARAOKE",
    "MAIN",
    "METADATA",
    "SUBTITLE",
    "SUPPLEMENTARY",]
DescribeSchedulePaginatorName = Literal["describe_schedule"]
DeviceSettingsSyncStateType = Literal["SYNCED", "SYNCING"]
DeviceUpdateStatusType = Literal["NOT_UP_TO_DATE", "UPDATING", "UP_TO_DATE"]
DolbyEProgramSelectionType = Literal["ALL_CHANNELS",
    "PROGRAM_1",
    "PROGRAM_2",
    "PROGRAM_3",
    "PROGRAM_4",
    "PROGRAM_5",
    "PROGRAM_6",
    "PROGRAM_7",
    "PROGRAM_8",]
DvbDashAccessibilityType = Literal["DVBDASH_1_VISUALLY_IMPAIRED",
    "DVBDASH_2_HARD_OF_HEARING",
    "DVBDASH_3_SUPPLEMENTAL_COMMENTARY",
    "DVBDASH_4_DIRECTORS_COMMENTARY",
    "DVBDASH_5_EDUCATIONAL_NOTES",
    "DVBDASH_6_MAIN_PROGRAM",
    "DVBDASH_7_CLEAN_FEED",]
DvbSdtOutputSdtType = Literal["SDT_FOLLOW", "SDT_FOLLOW_IF_PRESENT", "SDT_MANUAL", "SDT_NONE"]
DvbSubDestinationAlignmentType = Literal["CENTERED", "LEFT", "SMART"]
DvbSubDestinationBackgroundColorType = Literal["BLACK", "NONE", "WHITE"]
DvbSubDestinationFontColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubDestinationOutlineColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubDestinationShadowColorType = Literal["BLACK", "NONE", "WHITE"]
DvbSubDestinationTeletextGridControlType = Literal["FIXED", "SCALED"]
DvbSubOcrLanguageType = Literal["DEU", "ENG", "FRA", "NLD", "POR", "SPA"]
Eac3AtmosCodingModeType = Literal["CODING_MODE_5_1_4", "CODING_MODE_7_1_4", "CODING_MODE_9_1_6"]
Eac3AtmosDrcLineType = Literal["FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"]
Eac3AtmosDrcRfType = Literal["FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"]
Eac3AttenuationControlType = Literal["ATTENUATE_3_DB", "NONE"]
Eac3BitstreamModeType = Literal["COMMENTARY", "COMPLETE_MAIN", "EMERGENCY", "HEARING_IMPAIRED", "VISUALLY_IMPAIRED"]
Eac3CodingModeType = Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_3_2"]
Eac3DcFilterType = Literal["DISABLED", "ENABLED"]
Eac3DrcLineType = Literal["FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"]
Eac3DrcRfType = Literal["FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"]
Eac3LfeControlType = Literal["LFE", "NO_LFE"]
Eac3LfeFilterType = Literal["DISABLED", "ENABLED"]
Eac3MetadataControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
Eac3PassthroughControlType = Literal["NO_PASSTHROUGH", "WHEN_POSSIBLE"]
Eac3PhaseControlType = Literal["NO_SHIFT", "SHIFT_90_DEGREES"]
Eac3StereoDownmixType = Literal["DPL2", "LO_RO", "LT_RT", "NOT_INDICATED"]
Eac3SurroundExModeType = Literal["DISABLED", "ENABLED", "NOT_INDICATED"]
Eac3SurroundModeType = Literal["DISABLED", "ENABLED", "NOT_INDICATED"]
EbuTtDDestinationStyleControlType = Literal["EXCLUDE", "INCLUDE"]
EbuTtDFillLineGapControlType = Literal["DISABLED", "ENABLED"]
EmbeddedConvert608To708Type = Literal["DISABLED", "UPCONVERT"]
EmbeddedScte20DetectionType = Literal["AUTO", "OFF"]
EventBridgeRuleTemplateEventTypeType = Literal["MEDIACONNECT_ALERT",
    "MEDIACONNECT_FLOW_STATUS_CHANGE",
    "MEDIACONNECT_OUTPUT_HEALTH",
    "MEDIACONNECT_SOURCE_HEALTH",
    "MEDIALIVE_CHANNEL_ALERT",
    "MEDIALIVE_CHANNEL_INPUT_CHANGE",
    "MEDIALIVE_CHANNEL_STATE_CHANGE",
    "MEDIALIVE_MULTIPLEX_ALERT",
    "MEDIALIVE_MULTIPLEX_STATE_CHANGE",
    "MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION",
    "MEDIAPACKAGE_INPUT_NOTIFICATION",
    "MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION",
    "SIGNAL_MAP_ACTIVE_ALARM",]
FeatureActivationsInputPrepareScheduleActionsType = Literal["DISABLED", "ENABLED"]
FeatureActivationsOutputStaticImageOverlayScheduleActionsType = Literal["DISABLED", "ENABLED"]
FecOutputIncludeFecType = Literal["COLUMN", "COLUMN_AND_ROW"]
FixedAfdType = Literal["AFD_0000",
    "AFD_0010",
    "AFD_0011",
    "AFD_0100",
    "AFD_1000",
    "AFD_1001",
    "AFD_1010",
    "AFD_1011",
    "AFD_1101",
    "AFD_1110",
    "AFD_1111",]
Fmp4NielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
Fmp4TimedMetadataBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
FollowPointType = Literal["END", "START"]
FrameCaptureIntervalUnitType = Literal["MILLISECONDS", "SECONDS"]
GlobalConfigurationInputEndActionType = Literal["NONE", "SWITCH_AND_LOOP_INPUTS"]
GlobalConfigurationLowFramerateInputsType = Literal["DISABLED", "ENABLED"]
GlobalConfigurationOutputLockingModeType = Literal["EPOCH_LOCKING", "PIPELINE_LOCKING"]
GlobalConfigurationOutputTimingSourceType = Literal["INPUT_CLOCK", "SYSTEM_CLOCK"]
H264AdaptiveQuantizationType = Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H264ColorMetadataType = Literal["IGNORE", "INSERT"]
H264EntropyEncodingType = Literal["CABAC", "CAVLC"]
H264FlickerAqType = Literal["DISABLED", "ENABLED"]
H264ForceFieldPicturesType = Literal["DISABLED", "ENABLED"]
H264FramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264GopBReferenceType = Literal["DISABLED", "ENABLED"]
H264GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
H264LevelType = Literal["H264_LEVEL_1",
    "H264_LEVEL_1_1",
    "H264_LEVEL_1_2",
    "H264_LEVEL_1_3",
    "H264_LEVEL_2",
    "H264_LEVEL_2_1",
    "H264_LEVEL_2_2",
    "H264_LEVEL_3",
    "H264_LEVEL_3_1",
    "H264_LEVEL_3_2",
    "H264_LEVEL_4",
    "H264_LEVEL_4_1",
    "H264_LEVEL_4_2",
    "H264_LEVEL_5",
    "H264_LEVEL_5_1",
    "H264_LEVEL_5_2",
    "H264_LEVEL_AUTO",]
H264LookAheadRateControlType = Literal["HIGH", "LOW", "MEDIUM"]
H264ParControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264ProfileType = Literal["BASELINE", "HIGH", "HIGH_10BIT", "HIGH_422", "HIGH_422_10BIT", "MAIN"]
H264QualityLevelType = Literal["ENHANCED_QUALITY", "STANDARD_QUALITY"]
H264RateControlModeType = Literal["CBR", "MULTIPLEX", "QVBR", "VBR"]
H264ScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
H264SceneChangeDetectType = Literal["DISABLED", "ENABLED"]
H264SpatialAqType = Literal["DISABLED", "ENABLED"]
H264SubGopLengthType = Literal["DYNAMIC", "FIXED"]
H264SyntaxType = Literal["DEFAULT", "RP2027"]
H264TemporalAqType = Literal["DISABLED", "ENABLED"]
H264TimecodeInsertionBehaviorType = Literal["DISABLED", "PIC_TIMING_SEI"]
H265AdaptiveQuantizationType = Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H265AlternativeTransferFunctionType = Literal["INSERT", "OMIT"]
H265ColorMetadataType = Literal["IGNORE", "INSERT"]
H265FlickerAqType = Literal["DISABLED", "ENABLED"]
H265GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
H265LevelType = Literal["H265_LEVEL_1",
    "H265_LEVEL_2",
    "H265_LEVEL_2_1",
    "H265_LEVEL_3",
    "H265_LEVEL_3_1",
    "H265_LEVEL_4",
    "H265_LEVEL_4_1",
    "H265_LEVEL_5",
    "H265_LEVEL_5_1",
    "H265_LEVEL_5_2",
    "H265_LEVEL_6",
    "H265_LEVEL_6_1",
    "H265_LEVEL_6_2",
    "H265_LEVEL_AUTO",]
H265LookAheadRateControlType = Literal["HIGH", "LOW", "MEDIUM"]
H265MvOverPictureBoundariesType = Literal["DISABLED", "ENABLED"]
H265MvTemporalPredictorType = Literal["DISABLED", "ENABLED"]
H265ProfileType = Literal["MAIN", "MAIN_10BIT"]
H265RateControlModeType = Literal["CBR", "MULTIPLEX", "QVBR"]
H265ScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
H265SceneChangeDetectType = Literal["DISABLED", "ENABLED"]
H265TierType = Literal["HIGH", "MAIN"]
H265TilePaddingType = Literal["NONE", "PADDED"]
H265TimecodeInsertionBehaviorType = Literal["DISABLED", "PIC_TIMING_SEI"]
H265TreeblockSizeType = Literal["AUTO", "TREE_SIZE_32X32"]
HlsAdMarkersType = Literal["ADOBE", "ELEMENTAL", "ELEMENTAL_SCTE35"]
HlsAkamaiHttpTransferModeType = Literal["CHUNKED", "NON_CHUNKED"]
HlsCaptionLanguageSettingType = Literal["INSERT", "NONE", "OMIT"]
HlsClientCacheType = Literal["DISABLED", "ENABLED"]
HlsCodecSpecificationType = Literal["RFC_4281", "RFC_6381"]
HlsDirectoryStructureType = Literal["SINGLE_DIRECTORY", "SUBDIRECTORY_PER_STREAM"]
HlsDiscontinuityTagsType = Literal["INSERT", "NEVER_INSERT"]
HlsEncryptionTypeType = Literal["AES128", "SAMPLE_AES"]
HlsH265PackagingTypeType = Literal["HEV1", "HVC1"]
HlsId3SegmentTaggingStateType = Literal["DISABLED", "ENABLED"]
HlsIncompleteSegmentBehaviorType = Literal["AUTO", "SUPPRESS"]
HlsIvInManifestType = Literal["EXCLUDE", "INCLUDE"]
HlsIvSourceType = Literal["EXPLICIT", "FOLLOWS_SEGMENT_NUMBER"]
HlsManifestCompressionType = Literal["GZIP", "NONE"]
HlsManifestDurationFormatType = Literal["FLOATING_POINT", "INTEGER"]
HlsMediaStoreStorageClassType = Literal["TEMPORAL"]
HlsModeType = Literal["LIVE", "VOD"]
HlsOutputSelectionType = Literal["MANIFESTS_AND_SEGMENTS", "SEGMENTS_ONLY", "VARIANT_MANIFESTS_AND_SEGMENTS"]
HlsProgramDateTimeClockType = Literal["INITIALIZE_FROM_OUTPUT_TIMECODE", "SYSTEM_CLOCK"]
HlsProgramDateTimeType = Literal["EXCLUDE", "INCLUDE"]
HlsRedundantManifestType = Literal["DISABLED", "ENABLED"]
HlsScte35SourceTypeType = Literal["MANIFEST", "SEGMENTS"]
HlsSegmentationModeType = Literal["USE_INPUT_SEGMENTATION", "USE_SEGMENT_DURATION"]
HlsStreamInfResolutionType = Literal["EXCLUDE", "INCLUDE"]
HlsTimedMetadataId3FrameType = Literal["NONE", "PRIV", "TDRL"]
HlsTsFileModeType = Literal["SEGMENTED_FILES", "SINGLE_FILE"]
HlsWebdavHttpTransferModeType = Literal["CHUNKED", "NON_CHUNKED"]
IFrameOnlyPlaylistTypeType = Literal["DISABLED", "STANDARD"]
IncludeFillerNalUnitsType = Literal["AUTO", "DROP", "INCLUDE"]
InputAttachedWaiterName = Literal["input_attached"]
InputClassType = Literal["SINGLE_PIPELINE", "STANDARD"]
InputCodecType = Literal["AVC", "HEVC", "MPEG2"]
InputDeblockFilterType = Literal["DISABLED", "ENABLED"]
InputDeletedWaiterName = Literal["input_deleted"]
InputDenoiseFilterType = Literal["DISABLED", "ENABLED"]
InputDetachedWaiterName = Literal["input_detached"]
InputDeviceActiveInputType = Literal["HDMI", "SDI"]
InputDeviceCodecType = Literal["AVC", "HEVC"]
InputDeviceConfigurableAudioChannelPairProfileType = Literal["CBR-AAC_HQ-192000",
    "CBR-AAC_HQ-256000",
    "CBR-AAC_HQ-384000",
    "CBR-AAC_HQ-512000",
    "DISABLED",
    "VBR-AAC_HE-64000",
    "VBR-AAC_HHE-16000",
    "VBR-AAC_LC-128000",]
InputDeviceConfiguredInputType = Literal["AUTO", "HDMI", "SDI"]
InputDeviceConnectionStateType = Literal["CONNECTED", "DISCONNECTED"]
InputDeviceIpSchemeType = Literal["DHCP", "STATIC"]
InputDeviceOutputTypeType = Literal["MEDIACONNECT_FLOW", "MEDIALIVE_INPUT", "NONE"]
InputDeviceScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
InputDeviceStateType = Literal["IDLE", "STREAMING"]
InputDeviceTransferTypeType = Literal["INCOMING", "OUTGOING"]
InputDeviceTypeType = Literal["HD", "UHD"]
InputDeviceUhdAudioChannelPairProfileType = Literal["CBR-AAC_HQ-192000",
    "CBR-AAC_HQ-256000",
    "CBR-AAC_HQ-384000",
    "CBR-AAC_HQ-512000",
    "DISABLED",
    "VBR-AAC_HE-64000",
    "VBR-AAC_HHE-16000",
    "VBR-AAC_LC-128000",]
InputFilterType = Literal["AUTO", "DISABLED", "FORCED"]
InputLossActionForHlsOutType = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForMsSmoothOutType = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForRtmpOutType = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForUdpOutType = Literal["DROP_PROGRAM", "DROP_TS", "EMIT_PROGRAM"]
InputLossImageTypeType = Literal["COLOR", "SLATE"]
InputMaximumBitrateType = Literal["MAX_10_MBPS", "MAX_20_MBPS", "MAX_50_MBPS"]
InputPreferenceType = Literal["EQUAL_INPUT_PREFERENCE", "PRIMARY_INPUT_PREFERRED"]
InputResolutionType = Literal["HD", "SD", "UHD"]
InputSecurityGroupStateType = Literal["DELETED", "IDLE", "IN_USE", "UPDATING"]
InputSourceEndBehaviorType = Literal["CONTINUE", "LOOP"]
InputSourceTypeType = Literal["DYNAMIC", "STATIC"]
InputStateType = Literal["ATTACHED", "CREATING", "DELETED", "DELETING", "DETACHED"]
InputTimecodeSourceType = Literal["EMBEDDED", "ZEROBASED"]
InputTypeType = Literal["AWS_CDI",
    "INPUT_DEVICE",
    "MEDIACONNECT",
    "MP4_FILE",
    "RTMP_PULL",
    "RTMP_PUSH",
    "RTP_PUSH",
    "TS_FILE",
    "UDP_PUSH",
    "URL_PULL",]
LastFrameClippingBehaviorType = Literal["EXCLUDE_LAST_FRAME", "INCLUDE_LAST_FRAME"]
ListChannelsPaginatorName = Literal["list_channels"]
ListCloudWatchAlarmTemplateGroupsPaginatorName = Literal["list_cloud_watch_alarm_template_groups"]
ListCloudWatchAlarmTemplatesPaginatorName = Literal["list_cloud_watch_alarm_templates"]
ListEventBridgeRuleTemplateGroupsPaginatorName = Literal["list_event_bridge_rule_template_groups"]
ListEventBridgeRuleTemplatesPaginatorName = Literal["list_event_bridge_rule_templates"]
ListInputDeviceTransfersPaginatorName = Literal["list_input_device_transfers"]
ListInputDevicesPaginatorName = Literal["list_input_devices"]
ListInputSecurityGroupsPaginatorName = Literal["list_input_security_groups"]
ListInputsPaginatorName = Literal["list_inputs"]
ListMultiplexProgramsPaginatorName = Literal["list_multiplex_programs"]
ListMultiplexesPaginatorName = Literal["list_multiplexes"]
ListOfferingsPaginatorName = Literal["list_offerings"]
ListReservationsPaginatorName = Literal["list_reservations"]
ListSignalMapsPaginatorName = Literal["list_signal_maps"]
LogLevelType = Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"]
M2tsAbsentInputAudioBehaviorType = Literal["DROP", "ENCODE_SILENCE"]
M2tsAribCaptionsPidControlType = Literal["AUTO", "USE_CONFIGURED"]
M2tsAribType = Literal["DISABLED", "ENABLED"]
M2tsAudioBufferModelType = Literal["ATSC", "DVB"]
M2tsAudioIntervalType = Literal["VIDEO_AND_FIXED_INTERVALS", "VIDEO_INTERVAL"]
M2tsAudioStreamTypeType = Literal["ATSC", "DVB"]
M2tsBufferModelType = Literal["MULTIPLEX", "NONE"]
M2tsCcDescriptorType = Literal["DISABLED", "ENABLED"]
M2tsEbifControlType = Literal["NONE", "PASSTHROUGH"]
M2tsEbpPlacementType = Literal["VIDEO_AND_AUDIO_PIDS", "VIDEO_PID"]
M2tsEsRateInPesType = Literal["EXCLUDE", "INCLUDE"]
M2tsKlvType = Literal["NONE", "PASSTHROUGH"]
M2tsNielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M2tsPcrControlType = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M2tsRateModeType = Literal["CBR", "VBR"]
M2tsScte35ControlType = Literal["NONE", "PASSTHROUGH"]
M2tsSegmentationMarkersType = Literal["EBP", "EBP_LEGACY", "NONE", "PSI_SEGSTART", "RAI_ADAPT", "RAI_SEGSTART"]
M2tsSegmentationStyleType = Literal["MAINTAIN_CADENCE", "RESET_CADENCE"]
M2tsTimedMetadataBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8KlvBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8NielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8PcrControlType = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M3u8Scte35BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8TimedMetadataBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
MaintenanceDayType = Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"]
MotionGraphicsInsertionType = Literal["DISABLED", "ENABLED"]
Mp2CodingModeType = Literal["CODING_MODE_1_0", "CODING_MODE_2_0"]
Mpeg2AdaptiveQuantizationType = Literal["AUTO", "HIGH", "LOW", "MEDIUM", "OFF"]
Mpeg2ColorMetadataType = Literal["IGNORE", "INSERT"]
Mpeg2ColorSpaceType = Literal["AUTO", "PASSTHROUGH"]
Mpeg2DisplayRatioType = Literal["DISPLAYRATIO16X9", "DISPLAYRATIO4X3"]
Mpeg2GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
Mpeg2ScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
Mpeg2SubGopLengthType = Literal["DYNAMIC", "FIXED"]
Mpeg2TimecodeInsertionBehaviorType = Literal["DISABLED", "GOP_TIMECODE"]
MsSmoothH265PackagingTypeType = Literal["HEV1", "HVC1"]
MultiplexCreatedWaiterName = Literal["multiplex_created"]
MultiplexDeletedWaiterName = Literal["multiplex_deleted"]
MultiplexRunningWaiterName = Literal["multiplex_running"]
MultiplexStateType = Literal["CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "IDLE",
    "RECOVERING",
    "RUNNING",
    "STARTING",
    "STOPPING",]
MultiplexStoppedWaiterName = Literal["multiplex_stopped"]
NetworkInputServerValidationType = Literal["CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME", "CHECK_CRYPTOGRAPHY_ONLY"]
NielsenPcmToId3TaggingStateType = Literal["DISABLED", "ENABLED"]
NielsenWatermarkTimezonesType = Literal["AMERICA_PUERTO_RICO",
    "US_ALASKA",
    "US_ARIZONA",
    "US_CENTRAL",
    "US_EASTERN",
    "US_HAWAII",
    "US_MOUNTAIN",
    "US_PACIFIC",
    "US_SAMOA",
    "UTC",]
NielsenWatermarksCbetStepasideType = Literal["DISABLED", "ENABLED"]
NielsenWatermarksDistributionTypesType = Literal["FINAL_DISTRIBUTOR", "PROGRAM_CONTENT"]
OfferingDurationUnitsType = Literal["MONTHS"]
OfferingTypeType = Literal["NO_UPFRONT"]
PipelineIdType = Literal["PIPELINE_0", "PIPELINE_1"]
PreferredChannelPipelineType = Literal["CURRENTLY_ACTIVE", "PIPELINE_0", "PIPELINE_1"]
RebootInputDeviceForceType = Literal["NO", "YES"]
ReservationAutomaticRenewalType = Literal["DISABLED", "ENABLED", "UNAVAILABLE"]
ReservationCodecType = Literal["AUDIO", "AVC", "HEVC", "LINK", "MPEG2"]
ReservationMaximumBitrateType = Literal["MAX_10_MBPS", "MAX_20_MBPS", "MAX_50_MBPS"]
ReservationMaximumFramerateType = Literal["MAX_30_FPS", "MAX_60_FPS"]
ReservationResolutionType = Literal["FHD", "HD", "SD", "UHD"]
ReservationResourceTypeType = Literal["CHANNEL", "INPUT", "MULTIPLEX", "OUTPUT"]
ReservationSpecialFeatureType = Literal["ADVANCED_AUDIO", "AUDIO_NORMALIZATION", "MGHD", "MGUHD"]
ReservationStateType = Literal["ACTIVE", "CANCELED", "DELETED", "EXPIRED"]
ReservationVideoQualityType = Literal["ENHANCED", "PREMIUM", "STANDARD"]
RtmpAdMarkersType = Literal["ON_CUE_POINT_SCTE35"]
RtmpCacheFullBehaviorType = Literal["DISCONNECT_IMMEDIATELY", "WAIT_FOR_SERVER"]
RtmpCaptionDataType = Literal["ALL", "FIELD1_608", "FIELD1_AND_FIELD2_608"]
RtmpOutputCertificateModeType = Literal["SELF_SIGNED", "VERIFY_AUTHENTICITY"]
S3CannedAclType = Literal["AUTHENTICATED_READ", "BUCKET_OWNER_FULL_CONTROL", "BUCKET_OWNER_READ", "PUBLIC_READ"]
Scte20Convert608To708Type = Literal["DISABLED", "UPCONVERT"]
Scte27OcrLanguageType = Literal["DEU", "ENG", "FRA", "NLD", "POR", "SPA"]
Scte35AposNoRegionalBlackoutBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35AposWebDeliveryAllowedBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35ArchiveAllowedFlagType = Literal["ARCHIVE_ALLOWED", "ARCHIVE_NOT_ALLOWED"]
Scte35DeviceRestrictionsType = Literal["NONE", "RESTRICT_GROUP0", "RESTRICT_GROUP1", "RESTRICT_GROUP2"]
Scte35InputModeType = Literal["FIXED", "FOLLOW_ACTIVE"]
Scte35NoRegionalBlackoutFlagType = Literal["NO_REGIONAL_BLACKOUT", "REGIONAL_BLACKOUT"]
Scte35SegmentationCancelIndicatorType = Literal["SEGMENTATION_EVENT_CANCELED", "SEGMENTATION_EVENT_NOT_CANCELED"]
Scte35SegmentationScopeType = Literal["ALL_OUTPUT_GROUPS", "SCTE35_ENABLED_OUTPUT_GROUPS"]
Scte35SpliceInsertNoRegionalBlackoutBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35SpliceInsertWebDeliveryAllowedBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35TypeType = Literal["NONE", "SCTE_35_WITHOUT_SEGMENTATION"]
Scte35WebDeliveryAllowedFlagType = Literal["WEB_DELIVERY_ALLOWED", "WEB_DELIVERY_NOT_ALLOWED"]
SignalMapCreatedWaiterName = Literal["signal_map_created"]
SignalMapMonitorDeletedWaiterName = Literal["signal_map_monitor_deleted"]
SignalMapMonitorDeployedWaiterName = Literal["signal_map_monitor_deployed"]
SignalMapMonitorDeploymentStatusType = Literal["DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DEPLOYMENT_COMPLETE",
    "DEPLOYMENT_FAILED",
    "DEPLOYMENT_IN_PROGRESS",
    "DRY_RUN_DEPLOYMENT_COMPLETE",
    "DRY_RUN_DEPLOYMENT_FAILED",
    "DRY_RUN_DEPLOYMENT_IN_PROGRESS",
    "NOT_DEPLOYED",]
SignalMapStatusType = Literal["CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "NOT_READY",
    "READY",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_REVERTED",]
SignalMapUpdatedWaiterName = Literal["signal_map_updated"]
SmoothGroupAudioOnlyTimecodeControlType = Literal["PASSTHROUGH", "USE_CONFIGURED_CLOCK"]
SmoothGroupCertificateModeType = Literal["SELF_SIGNED", "VERIFY_AUTHENTICITY"]
SmoothGroupEventIdModeType = Literal["NO_EVENT_ID", "USE_CONFIGURED", "USE_TIMESTAMP"]
SmoothGroupEventStopBehaviorType = Literal["NONE", "SEND_EOS"]
SmoothGroupSegmentationModeType = Literal["USE_INPUT_SEGMENTATION", "USE_SEGMENT_DURATION"]
SmoothGroupSparseTrackTypeType = Literal["NONE", "SCTE_35", "SCTE_35_WITHOUT_SEGMENTATION"]
SmoothGroupStreamManifestBehaviorType = Literal["DO_NOT_SEND", "SEND"]
SmoothGroupTimestampOffsetModeType = Literal["USE_CONFIGURED_OFFSET", "USE_EVENT_START_DATE"]
Smpte2038DataPreferenceType = Literal["IGNORE", "PREFER"]
TemporalFilterPostFilterSharpeningType = Literal["AUTO", "DISABLED", "ENABLED"]
TemporalFilterStrengthType = Literal["AUTO",
    "STRENGTH_1",
    "STRENGTH_10",
    "STRENGTH_11",
    "STRENGTH_12",
    "STRENGTH_13",
    "STRENGTH_14",
    "STRENGTH_15",
    "STRENGTH_16",
    "STRENGTH_2",
    "STRENGTH_3",
    "STRENGTH_4",
    "STRENGTH_5",
    "STRENGTH_6",
    "STRENGTH_7",
    "STRENGTH_8",
    "STRENGTH_9",]
ThumbnailStateType = Literal["AUTO", "DISABLED"]
ThumbnailTypeType = Literal["CURRENT_ACTIVE", "UNSPECIFIED"]
TimecodeBurninFontSizeType = Literal["EXTRA_SMALL_10", "LARGE_48", "MEDIUM_32", "SMALL_16"]
TimecodeBurninPositionType = Literal["BOTTOM_CENTER",
    "BOTTOM_LEFT",
    "BOTTOM_RIGHT",
    "MIDDLE_CENTER",
    "MIDDLE_LEFT",
    "MIDDLE_RIGHT",
    "TOP_CENTER",
    "TOP_LEFT",
    "TOP_RIGHT",]
TimecodeConfigSourceType = Literal["EMBEDDED", "SYSTEMCLOCK", "ZEROBASED"]
TtmlDestinationStyleControlType = Literal["PASSTHROUGH", "USE_CONFIGURED"]
UdpTimedMetadataId3FrameType = Literal["NONE", "PRIV", "TDRL"]
VideoDescriptionRespondToAfdType = Literal["NONE", "PASSTHROUGH", "RESPOND"]
VideoDescriptionScalingBehaviorType = Literal["DEFAULT", "STRETCH_TO_OUTPUT"]
VideoSelectorColorSpaceType = Literal["FOLLOW", "HDR10", "HLG_2020", "REC_601", "REC_709"]
VideoSelectorColorSpaceUsageType = Literal["FALLBACK", "FORCE"]
WavCodingModeType = Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_4_0", "CODING_MODE_8_0"]
WebvttDestinationStyleControlType = Literal["NO_STYLE_DATA", "PASSTHROUGH"]
MediaLiveServiceName = Literal["medialive"]
ServiceName = Literal["accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "alexaforbusiness",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appfabric",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "arc-zonal-shift",
    "artifact",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "b2bi",
    "backup",
    "backup-gateway",
    "backupstorage",
    "batch",
    "bcm-data-exports",
    "bedrock",
    "bedrock-agent",
    "bedrock-agent-runtime",
    "bedrock-runtime",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chatbot",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-media-pipelines",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "chime-sdk-voice",
    "cleanrooms",
    "cleanroomsml",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudfront-keyvaluestore",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudtrail-data",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codeconnections",
    "codedeploy",
    "codeguru-reviewer",
    "codeguru-security",
    "codeguruprofiler",
    "codepipeline",
    "codestar",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectcampaigns",
    "connectcases",
    "connectparticipant",
    "controlcatalog",
    "controltower",
    "cost-optimization-hub",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "datazone",
    "dax",
    "deadline",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "docdb-elastic",
    "drs",
    "ds",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "eks-auth",
    "elastic-inference",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "emr-serverless",
    "entityresolution",
    "es",
    "events",
    "evidently",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "freetier",
    "fsx",
    "gamelift",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "honeycode",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector-scan",
    "inspector2",
    "internetmonitor",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot1click-devices",
    "iot1click-projects",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotfleetwise",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "ivs-realtime",
    "ivschat",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kendra-ranking",
    "keyspaces",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesis-video-webrtc-storage",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "launch-wizard",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "license-manager-linux-subscriptions",
    "license-manager-user-subscriptions",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "m2",
    "machinelearning",
    "macie2",
    "managedblockchain",
    "managedblockchain-query",
    "marketplace-agreement",
    "marketplace-catalog",
    "marketplace-deployment",
    "marketplace-entitlement",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediapackagev2",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "medical-imaging",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhuborchestrator",
    "migrationhubstrategy",
    "mobile",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "neptune-graph",
    "neptunedata",
    "network-firewall",
    "networkmanager",
    "networkmonitor",
    "nimble",
    "oam",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "osis",
    "outposts",
    "panorama",
    "payment-cryptography",
    "payment-cryptography-data",
    "pca-connector-ad",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "pipes",
    "polly",
    "pricing",
    "privatenetworks",
    "proton",
    "qbusiness",
    "qconnect",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "redshift-serverless",
    "rekognition",
    "repostspace",
    "resiliencehub",
    "resource-explorer-2",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "rolesanywhere",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53profiles",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-geospatial",
    "sagemaker-metrics",
    "sagemaker-runtime",
    "savingsplans",
    "scheduler",
    "schemas",
    "sdb",
    "secretsmanager",
    "securityhub",
    "securitylake",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "simspaceweaver",
    "sms",
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "ssm-sap",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "supplychain",
    "support",
    "support-app",
    "swf",
    "synthetics",
    "textract",
    "timestream-influxdb",
    "timestream-query",
    "timestream-write",
    "tnb",
    "transcribe",
    "transfer",
    "translate",
    "trustedadvisor",
    "verifiedpermissions",
    "voice-id",
    "vpc-lattice",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "worklink",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-thin-client",
    "workspaces-web",
    "xray",]
ResourceServiceName = Literal["cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",]
PaginatorName = Literal["describe_schedule",
    "list_channels",
    "list_cloud_watch_alarm_template_groups",
    "list_cloud_watch_alarm_templates",
    "list_event_bridge_rule_template_groups",
    "list_event_bridge_rule_templates",
    "list_input_device_transfers",
    "list_input_devices",
    "list_input_security_groups",
    "list_inputs",
    "list_multiplex_programs",
    "list_multiplexes",
    "list_offerings",
    "list_reservations",
    "list_signal_maps",]
WaiterName = Literal["channel_created",
    "channel_deleted",
    "channel_running",
    "channel_stopped",
    "input_attached",
    "input_deleted",
    "input_detached",
    "multiplex_created",
    "multiplex_deleted",
    "multiplex_running",
    "multiplex_stopped",
    "signal_map_created",
    "signal_map_monitor_deleted",
    "signal_map_monitor_deployed",
    "signal_map_updated",]
RegionName = Literal["ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-4",
    "ca-central-1",
    "eu-central-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-central-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-2",]
OutputDestinationUnionTypeDef = Union['OutputDestinationTypeDef', 'OutputDestinationExtraOutputTypeDef']
InputAttachmentUnionTypeDef = Union['InputAttachmentTypeDef', 'InputAttachmentExtraOutputTypeDef']
EncoderSettingsUnionTypeDef = Union['EncoderSettingsTypeDef', 'EncoderSettingsOutputTypeDef']
