# Medialive Classes

# AacSettingsTypeDef

### Bitrate
- **Type**: typing.Optional[float]

### CodingMode
- **Type**: typing.Optional[typing.Literal['AD_RECEIVER_MIX', 'CODING_MODE_1_0', 'CODING_MODE_1_1', 'CODING_MODE_2_0', 'CODING_MODE_5_1']]

### InputType
- **Type**: typing.Optional[typing.Literal['BROADCASTER_MIXED_AD', 'NORMAL']]

### Profile
- **Type**: typing.Optional[typing.Literal['HEV1', 'HEV2', 'LC']]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'VBR']]

### RawFormat
- **Type**: typing.Optional[typing.Literal['LATM_LOAS', 'NONE']]

### SampleRate
- **Type**: typing.Optional[float]

### Spec
- **Type**: typing.Optional[typing.Literal['MPEG2', 'MPEG4']]

### VbrQuality
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM_HIGH', 'MEDIUM_LOW']]


# Ac3SettingsTypeDef

### Bitrate
- **Type**: typing.Optional[float]

### BitstreamMode
- **Type**: typing.Optional[typing.Literal['COMMENTARY', 'COMPLETE_MAIN', 'DIALOGUE', 'EMERGENCY', 'HEARING_IMPAIRED', 'MUSIC_AND_EFFECTS', 'VISUALLY_IMPAIRED', 'VOICE_OVER']]

### CodingMode
- **Type**: typing.Optional[typing.Literal['CODING_MODE_1_0', 'CODING_MODE_1_1', 'CODING_MODE_2_0', 'CODING_MODE_3_2_LFE']]

### Dialnorm
- **Type**: typing.Optional[int]

### DrcProfile
- **Type**: typing.Optional[typing.Literal['FILM_STANDARD', 'NONE']]

### LfeFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### MetadataControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### AttenuationControl
- **Type**: typing.Optional[typing.Literal['ATTENUATE_3_DB', 'NONE']]


# AcceptInputDeviceTransferRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# AccountConfigurationTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]


# AncillarySourceSettingsTypeDef

### SourceAncillaryChannelNumber
- **Type**: typing.Optional[int]


# AnywhereSettingsTypeDef

### ChannelPlacementGroupId
- **Type**: typing.Optional[str]

### ClusterId
- **Type**: typing.Optional[str]


# ArchiveCdnSettingsTypeDef

### ArchiveS3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ArchiveS3SettingsTypeDef]


# ArchiveContainerSettingsOutputTypeDef

### M2tsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.M2tsSettingsTypeDef]

### RawSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ArchiveContainerSettingsTypeDef

### M2tsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.M2tsSettingsTypeDef]

### RawSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ArchiveGroupSettingsTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes

### ArchiveCdnSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ArchiveCdnSettingsTypeDef]

### RolloverInterval
- **Type**: typing.Optional[int]


# ArchiveOutputSettingsOutputTypeDef

### ContainerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ArchiveContainerSettingsOutputTypeDef'>
- **Required**: Yes

### Extension
- **Type**: typing.Optional[str]

### NameModifier
- **Type**: typing.Optional[str]


# ArchiveOutputSettingsTypeDef

### ContainerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ArchiveContainerSettingsTypeDef'>
- **Required**: Yes

### Extension
- **Type**: typing.Optional[str]

### NameModifier
- **Type**: typing.Optional[str]


# ArchiveS3SettingsTypeDef

### CannedAcl
- **Type**: typing.Optional[typing.Literal['AUTHENTICATED_READ', 'BUCKET_OWNER_FULL_CONTROL', 'BUCKET_OWNER_READ', 'PUBLIC_READ']]


# AudioChannelMappingOutputTypeDef

### InputChannelLevels
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputChannelLevelTypeDef]
- **Required**: Yes

### OutputChannel
- **Type**: <class 'int'>
- **Required**: Yes


# AudioChannelMappingTypeDef

### InputChannelLevels
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputChannelLevelTypeDef]
- **Required**: Yes

### OutputChannel
- **Type**: <class 'int'>
- **Required**: Yes


# AudioCodecSettingsOutputTypeDef

### AacSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AacSettingsTypeDef]

### Ac3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Ac3SettingsTypeDef]

### Eac3AtmosSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Eac3AtmosSettingsTypeDef]

### Eac3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Eac3SettingsTypeDef]

### Mp2Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Mp2SettingsTypeDef]

### PassThroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### WavSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WavSettingsTypeDef]


# AudioCodecSettingsTypeDef

### AacSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AacSettingsTypeDef]

### Ac3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Ac3SettingsTypeDef]

### Eac3AtmosSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Eac3AtmosSettingsTypeDef]

### Eac3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Eac3SettingsTypeDef]

### Mp2Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Mp2SettingsTypeDef]

### PassThroughSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### WavSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WavSettingsTypeDef]


# AudioDescriptionOutputTypeDef

### AudioSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AudioNormalizationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioNormalizationSettingsTypeDef]

### AudioType
- **Type**: typing.Optional[typing.Literal['CLEAN_EFFECTS', 'HEARING_IMPAIRED', 'UNDEFINED', 'VISUAL_IMPAIRED_COMMENTARY']]

### AudioTypeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### AudioWatermarkingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioWatermarkSettingsTypeDef]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioCodecSettingsOutputTypeDef]

### LanguageCode
- **Type**: typing.Optional[str]

### LanguageCodeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.RemixSettingsOutputTypeDef]

### StreamName
- **Type**: typing.Optional[str]

### AudioDashRoles
- **Type**: typing.Optional[typing.List[typing.Literal['ALTERNATE', 'COMMENTARY', 'DESCRIPTION', 'DUB', 'EMERGENCY', 'ENHANCED-AUDIO-INTELLIGIBILITY', 'KARAOKE', 'MAIN', 'SUPPLEMENTARY']]]

### DvbDashAccessibility
- **Type**: typing.Optional[typing.Literal['DVBDASH_1_VISUALLY_IMPAIRED', 'DVBDASH_2_HARD_OF_HEARING', 'DVBDASH_3_SUPPLEMENTAL_COMMENTARY', 'DVBDASH_4_DIRECTORS_COMMENTARY', 'DVBDASH_5_EDUCATIONAL_NOTES', 'DVBDASH_6_MAIN_PROGRAM', 'DVBDASH_7_CLEAN_FEED']]


# AudioDescriptionTypeDef

### AudioSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AudioNormalizationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioNormalizationSettingsTypeDef]

### AudioType
- **Type**: typing.Optional[typing.Literal['CLEAN_EFFECTS', 'HEARING_IMPAIRED', 'UNDEFINED', 'VISUAL_IMPAIRED_COMMENTARY']]

### AudioTypeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### AudioWatermarkingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioWatermarkSettingsTypeDef]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioCodecSettingsTypeDef]

### LanguageCode
- **Type**: typing.Optional[str]

### LanguageCodeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.RemixSettingsTypeDef]

### StreamName
- **Type**: typing.Optional[str]

### AudioDashRoles
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALTERNATE', 'COMMENTARY', 'DESCRIPTION', 'DUB', 'EMERGENCY', 'ENHANCED-AUDIO-INTELLIGIBILITY', 'KARAOKE', 'MAIN', 'SUPPLEMENTARY']]]

### DvbDashAccessibility
- **Type**: typing.Optional[typing.Literal['DVBDASH_1_VISUALLY_IMPAIRED', 'DVBDASH_2_HARD_OF_HEARING', 'DVBDASH_3_SUPPLEMENTAL_COMMENTARY', 'DVBDASH_4_DIRECTORS_COMMENTARY', 'DVBDASH_5_EDUCATIONAL_NOTES', 'DVBDASH_6_MAIN_PROGRAM', 'DVBDASH_7_CLEAN_FEED']]


# AudioDolbyEDecodeTypeDef

### ProgramSelection
- **Type**: typing.Literal['ALL_CHANNELS', 'PROGRAM_1', 'PROGRAM_2', 'PROGRAM_3', 'PROGRAM_4', 'PROGRAM_5', 'PROGRAM_6', 'PROGRAM_7', 'PROGRAM_8']
- **Required**: Yes


# AudioHlsRenditionSelectionTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# AudioLanguageSelectionTypeDef

### LanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageSelectionPolicy
- **Type**: typing.Optional[typing.Literal['LOOSE', 'STRICT']]


# AudioNormalizationSettingsTypeDef

### Algorithm
- **Type**: typing.Optional[typing.Literal['ITU_1770_1', 'ITU_1770_2']]

### AlgorithmControl
- **Type**: typing.Optional[typing.Literal['CORRECT_AUDIO']]

### TargetLkfs
- **Type**: typing.Optional[float]


# AudioOnlyHlsSettingsTypeDef

### AudioGroupId
- **Type**: typing.Optional[str]

### AudioOnlyImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef]

### AudioTrackType
- **Type**: typing.Optional[typing.Literal['ALTERNATE_AUDIO_AUTO_SELECT', 'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT', 'ALTERNATE_AUDIO_NOT_AUTO_SELECT', 'AUDIO_ONLY_VARIANT_STREAM']]

### SegmentType
- **Type**: typing.Optional[typing.Literal['AAC', 'FMP4']]


# AudioPidSelectionTypeDef

### Pid
- **Type**: <class 'int'>
- **Required**: Yes


# AudioSelectorOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioSelectorSettingsOutputTypeDef]


# AudioSelectorSettingsOutputTypeDef

### AudioHlsRenditionSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioHlsRenditionSelectionTypeDef]

### AudioLanguageSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioLanguageSelectionTypeDef]

### AudioPidSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioPidSelectionTypeDef]

### AudioTrackSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioTrackSelectionOutputTypeDef]


# AudioSelectorSettingsTypeDef

### AudioHlsRenditionSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioHlsRenditionSelectionTypeDef]

### AudioLanguageSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioLanguageSelectionTypeDef]

### AudioPidSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioPidSelectionTypeDef]

### AudioTrackSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioTrackSelectionUnionTypeDef]


# AudioSelectorSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudioSelectorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioSelectorSettingsUnionTypeDef]


# AudioSelectorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudioSilenceFailoverSettingsTypeDef

### AudioSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### AudioSilenceThresholdMsec
- **Type**: typing.Optional[int]


# AudioTrackSelectionOutputTypeDef

### Tracks
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.AudioTrackTypeDef]
- **Required**: Yes

### DolbyEDecode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioDolbyEDecodeTypeDef]


# AudioTrackSelectionTypeDef

### Tracks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.AudioTrackTypeDef]
- **Required**: Yes

### DolbyEDecode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioDolbyEDecodeTypeDef]


# AudioTrackSelectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudioTrackTypeDef

### Track
- **Type**: <class 'int'>
- **Required**: Yes


# AudioWatermarkSettingsTypeDef

### NielsenWatermarksSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.NielsenWatermarksSettingsTypeDef]


# AutomaticInputFailoverSettingsOutputTypeDef

### SecondaryInputId
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorClearTimeMsec
- **Type**: typing.Optional[int]

### FailoverConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.FailoverConditionTypeDef]]

### InputPreference
- **Type**: typing.Optional[typing.Literal['EQUAL_INPUT_PREFERENCE', 'PRIMARY_INPUT_PREFERRED']]


# AutomaticInputFailoverSettingsTypeDef

### SecondaryInputId
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorClearTimeMsec
- **Type**: typing.Optional[int]

### FailoverConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.FailoverConditionTypeDef]]

### InputPreference
- **Type**: typing.Optional[typing.Literal['EQUAL_INPUT_PREFERENCE', 'PRIMARY_INPUT_PREFERRED']]


# AutomaticInputFailoverSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Av1ColorSpaceSettingsOutputTypeDef

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Hdr10Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Hdr10SettingsTypeDef]

### Rec601Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# Av1ColorSpaceSettingsTypeDef

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Hdr10Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Hdr10SettingsTypeDef]

### Rec601Settings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# Av1SettingsOutputTypeDef

### FramerateDenominator
- **Type**: <class 'int'>
- **Required**: Yes

### FramerateNumerator
- **Type**: <class 'int'>
- **Required**: Yes

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### BufSize
- **Type**: typing.Optional[int]

### ColorSpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Av1ColorSpaceSettingsOutputTypeDef]

### FixedAfd
- **Type**: typing.Optional[typing.Literal['AFD_0000', 'AFD_0010', 'AFD_0011', 'AFD_0100', 'AFD_1000', 'AFD_1001', 'AFD_1010', 'AFD_1011', 'AFD_1101', 'AFD_1110', 'AFD_1111']]

### GopSize
- **Type**: typing.Optional[float]

### GopSizeUnits
- **Type**: typing.Optional[typing.Literal['FRAMES', 'SECONDS']]

### Level
- **Type**: typing.Optional[typing.Literal['AV1_LEVEL_2', 'AV1_LEVEL_2_1', 'AV1_LEVEL_3', 'AV1_LEVEL_3_1', 'AV1_LEVEL_4', 'AV1_LEVEL_4_1', 'AV1_LEVEL_5', 'AV1_LEVEL_5_1', 'AV1_LEVEL_5_2', 'AV1_LEVEL_5_3', 'AV1_LEVEL_6', 'AV1_LEVEL_6_1', 'AV1_LEVEL_6_2', 'AV1_LEVEL_6_3', 'AV1_LEVEL_AUTO']]

### LookAheadRateControl
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### MaxBitrate
- **Type**: typing.Optional[int]

### MinIInterval
- **Type**: typing.Optional[int]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### SceneChangeDetect
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TimecodeBurninSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TimecodeBurninSettingsTypeDef]


# Av1SettingsTypeDef

### FramerateDenominator
- **Type**: <class 'int'>
- **Required**: Yes

### FramerateNumerator
- **Type**: <class 'int'>
- **Required**: Yes

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### BufSize
- **Type**: typing.Optional[int]

### ColorSpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Av1ColorSpaceSettingsTypeDef]

### FixedAfd
- **Type**: typing.Optional[typing.Literal['AFD_0000', 'AFD_0010', 'AFD_0011', 'AFD_0100', 'AFD_1000', 'AFD_1001', 'AFD_1010', 'AFD_1011', 'AFD_1101', 'AFD_1110', 'AFD_1111']]

### GopSize
- **Type**: typing.Optional[float]

### GopSizeUnits
- **Type**: typing.Optional[typing.Literal['FRAMES', 'SECONDS']]

### Level
- **Type**: typing.Optional[typing.Literal['AV1_LEVEL_2', 'AV1_LEVEL_2_1', 'AV1_LEVEL_3', 'AV1_LEVEL_3_1', 'AV1_LEVEL_4', 'AV1_LEVEL_4_1', 'AV1_LEVEL_5', 'AV1_LEVEL_5_1', 'AV1_LEVEL_5_2', 'AV1_LEVEL_5_3', 'AV1_LEVEL_6', 'AV1_LEVEL_6_1', 'AV1_LEVEL_6_2', 'AV1_LEVEL_6_3', 'AV1_LEVEL_AUTO']]

### LookAheadRateControl
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### MaxBitrate
- **Type**: typing.Optional[int]

### MinIInterval
- **Type**: typing.Optional[int]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### SceneChangeDetect
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TimecodeBurninSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TimecodeBurninSettingsTypeDef]


# AvailBlankingTypeDef

### AvailBlankingImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AvailConfigurationTypeDef

### AvailSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AvailSettingsTypeDef]

### Scte35SegmentationScope
- **Type**: typing.Optional[typing.Literal['ALL_OUTPUT_GROUPS', 'SCTE35_ENABLED_OUTPUT_GROUPS']]


# AvailSettingsTypeDef

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EsamTypeDef]

### Scte35SpliceInsert
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35SpliceInsertTypeDef]

### Scte35TimeSignalApos
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35TimeSignalAposTypeDef]


# BandwidthReductionFilterSettingsTypeDef

### PostFilterSharpening
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SHARPENING_1', 'SHARPENING_2', 'SHARPENING_3']]

### Strength
- **Type**: typing.Optional[typing.Literal['AUTO', 'STRENGTH_1', 'STRENGTH_2', 'STRENGTH_3', 'STRENGTH_4']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteRequestTypeDef

### ChannelIds
- **Type**: typing.Optional[typing.Sequence[str]]

### InputIds
- **Type**: typing.Optional[typing.Sequence[str]]

### InputSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MultiplexIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchDeleteResponseTypeDef

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.BatchFailedResultModelTypeDef]
- **Required**: Yes

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.BatchSuccessfulResultModelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchFailedResultModelTypeDef

### Arn
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# BatchScheduleActionCreateRequestTypeDef

### ScheduleActions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionUnionTypeDef]
- **Required**: Yes


# BatchScheduleActionCreateResultTypeDef

### ScheduleActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionOutputTypeDef]
- **Required**: Yes


# BatchScheduleActionDeleteRequestTypeDef

### ActionNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchScheduleActionDeleteResultTypeDef

### ScheduleActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionOutputTypeDef]
- **Required**: Yes


# BatchStartRequestTypeDef

### ChannelIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MultiplexIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchStartResponseTypeDef

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.BatchFailedResultModelTypeDef]
- **Required**: Yes

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.BatchSuccessfulResultModelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchStopRequestTypeDef

### ChannelIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MultiplexIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchStopResponseTypeDef

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.BatchFailedResultModelTypeDef]
- **Required**: Yes

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.BatchSuccessfulResultModelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchSuccessfulResultModelTypeDef

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# BatchUpdateScheduleRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### Creates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.BatchScheduleActionCreateRequestTypeDef]

### Deletes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.BatchScheduleActionDeleteRequestTypeDef]


# BatchUpdateScheduleResponseTypeDef

### Creates
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.BatchScheduleActionCreateResultTypeDef'>
- **Required**: Yes

### Deletes
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.BatchScheduleActionDeleteResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlackoutSlateTypeDef

### BlackoutSlateImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef]

### NetworkEndBlackout
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### NetworkEndBlackoutImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef]

### NetworkId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# BurnInDestinationSettingsTypeDef

### Alignment
- **Type**: typing.Optional[typing.Literal['CENTERED', 'LEFT', 'SMART']]

### BackgroundColor
- **Type**: typing.Optional[typing.Literal['BLACK', 'NONE', 'WHITE']]

### BackgroundOpacity
- **Type**: typing.Optional[int]

### Font
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef]

### FontColor
- **Type**: typing.Optional[typing.Literal['BLACK', 'BLUE', 'GREEN', 'RED', 'WHITE', 'YELLOW']]

### FontOpacity
- **Type**: typing.Optional[int]

### FontResolution
- **Type**: typing.Optional[int]

### FontSize
- **Type**: typing.Optional[str]

### OutlineColor
- **Type**: typing.Optional[typing.Literal['BLACK', 'BLUE', 'GREEN', 'RED', 'WHITE', 'YELLOW']]

### OutlineSize
- **Type**: typing.Optional[int]

### ShadowColor
- **Type**: typing.Optional[typing.Literal['BLACK', 'NONE', 'WHITE']]

### ShadowOpacity
- **Type**: typing.Optional[int]

### ShadowXOffset
- **Type**: typing.Optional[int]

### ShadowYOffset
- **Type**: typing.Optional[int]

### TeletextGridControl
- **Type**: typing.Optional[typing.Literal['FIXED', 'SCALED']]

### XPosition
- **Type**: typing.Optional[int]

### YPosition
- **Type**: typing.Optional[int]


# CancelInputDeviceTransferRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# CaptionDescriptionOutputTypeDef

### CaptionSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Accessibility
- **Type**: typing.Optional[typing.Literal['DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES', 'IMPLEMENTS_ACCESSIBILITY_FEATURES']]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CaptionDestinationSettingsOutputTypeDef]

### LanguageCode
- **Type**: typing.Optional[str]

### LanguageDescription
- **Type**: typing.Optional[str]

### CaptionDashRoles
- **Type**: typing.Optional[typing.List[typing.Literal['ALTERNATE', 'CAPTION', 'COMMENTARY', 'DESCRIPTION', 'DUB', 'EASYREADER', 'EMERGENCY', 'FORCED-SUBTITLE', 'KARAOKE', 'MAIN', 'METADATA', 'SUBTITLE', 'SUPPLEMENTARY']]]

### DvbDashAccessibility
- **Type**: typing.Optional[typing.Literal['DVBDASH_1_VISUALLY_IMPAIRED', 'DVBDASH_2_HARD_OF_HEARING', 'DVBDASH_3_SUPPLEMENTAL_COMMENTARY', 'DVBDASH_4_DIRECTORS_COMMENTARY', 'DVBDASH_5_EDUCATIONAL_NOTES', 'DVBDASH_6_MAIN_PROGRAM', 'DVBDASH_7_CLEAN_FEED']]


# CaptionDescriptionTypeDef

### CaptionSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Accessibility
- **Type**: typing.Optional[typing.Literal['DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES', 'IMPLEMENTS_ACCESSIBILITY_FEATURES']]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CaptionDestinationSettingsTypeDef]

### LanguageCode
- **Type**: typing.Optional[str]

### LanguageDescription
- **Type**: typing.Optional[str]

### CaptionDashRoles
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALTERNATE', 'CAPTION', 'COMMENTARY', 'DESCRIPTION', 'DUB', 'EASYREADER', 'EMERGENCY', 'FORCED-SUBTITLE', 'KARAOKE', 'MAIN', 'METADATA', 'SUBTITLE', 'SUPPLEMENTARY']]]

### DvbDashAccessibility
- **Type**: typing.Optional[typing.Literal['DVBDASH_1_VISUALLY_IMPAIRED', 'DVBDASH_2_HARD_OF_HEARING', 'DVBDASH_3_SUPPLEMENTAL_COMMENTARY', 'DVBDASH_4_DIRECTORS_COMMENTARY', 'DVBDASH_5_EDUCATIONAL_NOTES', 'DVBDASH_6_MAIN_PROGRAM', 'DVBDASH_7_CLEAN_FEED']]


# CaptionDestinationSettingsOutputTypeDef

### AribDestinationSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### BurnInDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.BurnInDestinationSettingsTypeDef]

### DvbSubDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.DvbSubDestinationSettingsTypeDef]

### EbuTtDDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EbuTtDDestinationSettingsTypeDef]

### EmbeddedDestinationSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### EmbeddedPlusScte20DestinationSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### RtmpCaptionInfoDestinationSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Scte20PlusEmbeddedDestinationSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Scte27DestinationSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SmpteTtDestinationSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TeletextDestinationSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TtmlDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TtmlDestinationSettingsTypeDef]

### WebvttDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WebvttDestinationSettingsTypeDef]


# CaptionDestinationSettingsTypeDef

### AribDestinationSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### BurnInDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.BurnInDestinationSettingsTypeDef]

### DvbSubDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.DvbSubDestinationSettingsTypeDef]

### EbuTtDDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EbuTtDDestinationSettingsTypeDef]

### EmbeddedDestinationSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### EmbeddedPlusScte20DestinationSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### RtmpCaptionInfoDestinationSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Scte20PlusEmbeddedDestinationSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Scte27DestinationSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### SmpteTtDestinationSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### TeletextDestinationSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### TtmlDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TtmlDestinationSettingsTypeDef]

### WebvttDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WebvttDestinationSettingsTypeDef]


# CaptionLanguageMappingTypeDef

### CaptionChannel
- **Type**: <class 'int'>
- **Required**: Yes

### LanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageDescription
- **Type**: <class 'str'>
- **Required**: Yes


# CaptionRectangleTypeDef

### Height
- **Type**: <class 'float'>
- **Required**: Yes

### LeftOffset
- **Type**: <class 'float'>
- **Required**: Yes

### TopOffset
- **Type**: <class 'float'>
- **Required**: Yes

### Width
- **Type**: <class 'float'>
- **Required**: Yes


# CaptionSelectorOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[str]

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CaptionSelectorSettingsOutputTypeDef]


# CaptionSelectorSettingsOutputTypeDef

### AncillarySourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AncillarySourceSettingsTypeDef]

### AribSourceSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### DvbSubSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.DvbSubSourceSettingsTypeDef]

### EmbeddedSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EmbeddedSourceSettingsTypeDef]

### Scte20SourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte20SourceSettingsTypeDef]

### Scte27SourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte27SourceSettingsTypeDef]

### TeletextSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TeletextSourceSettingsTypeDef]


# CaptionSelectorSettingsTypeDef

### AncillarySourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AncillarySourceSettingsTypeDef]

### AribSourceSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### DvbSubSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.DvbSubSourceSettingsTypeDef]

### EmbeddedSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EmbeddedSourceSettingsTypeDef]

### Scte20SourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte20SourceSettingsTypeDef]

### Scte27SourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte27SourceSettingsTypeDef]

### TeletextSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TeletextSourceSettingsTypeDef]


# CaptionSelectorSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaptionSelectorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[str]

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CaptionSelectorSettingsUnionTypeDef]


# CaptionSelectorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CdiInputSpecificationTypeDef

### Resolution
- **Type**: typing.Optional[typing.Literal['FHD', 'HD', 'SD', 'UHD']]


# ChannelEgressEndpointTypeDef

### SourceIp
- **Type**: typing.Optional[str]


# ChannelEngineVersionRequestTypeDef

### Version
- **Type**: typing.Optional[str]


# ChannelEngineVersionResponseTypeDef

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]

### Version
- **Type**: typing.Optional[str]


# ChannelSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### CdiInputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef]

### ChannelClass
- **Type**: typing.Optional[typing.Literal['SINGLE_PIPELINE', 'STANDARD']]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationOutputTypeDef]]

### EgressEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.ChannelEgressEndpointTypeDef]]

### Id
- **Type**: typing.Optional[str]

### InputAttachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentOutputTypeDef]]

### InputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSpecificationTypeDef]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MaintenanceStatusTypeDef]

### Name
- **Type**: typing.Optional[str]

### PipelinesRunningCount
- **Type**: typing.Optional[int]

### RoleArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VpcOutputSettingsDescriptionTypeDef]

### AnywhereSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.DescribeAnywhereSettingsTypeDef]

### ChannelEngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionResponseTypeDef]

### UsedChannelEngineVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionResponseTypeDef]]


# ChannelTypeDef

### Arn
- **Type**: typing.Optional[str]

### CdiInputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef]

### ChannelClass
- **Type**: typing.Optional[typing.Literal['SINGLE_PIPELINE', 'STANDARD']]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationOutputTypeDef]]

### EgressEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.ChannelEgressEndpointTypeDef]]

### EncoderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EncoderSettingsOutputTypeDef]

### Id
- **Type**: typing.Optional[str]

### InputAttachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentOutputTypeDef]]

### InputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSpecificationTypeDef]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MaintenanceStatusTypeDef]

### Name
- **Type**: typing.Optional[str]

### PipelineDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.PipelineDetailTypeDef]]

### PipelinesRunningCount
- **Type**: typing.Optional[int]

### RoleArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VpcOutputSettingsDescriptionTypeDef]

### AnywhereSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.DescribeAnywhereSettingsTypeDef]

### ChannelEngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionResponseTypeDef]


# ClaimDeviceRequestTypeDef

### Id
- **Type**: typing.Optional[str]


# CloudWatchAlarmTemplateGroupSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateCount
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CloudWatchAlarmTemplateSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EvaluationPeriods
- **Type**: <class 'int'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']
- **Required**: Yes

### TargetResourceType
- **Type**: typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'MEDIATAILOR_PLAYBACK_CONFIGURATION', 'S3_BUCKET']
- **Required**: Yes

### Threshold
- **Type**: <class 'float'>
- **Required**: Yes

### TreatMissingData
- **Type**: typing.Literal['breaching', 'ignore', 'missing', 'notBreaching']
- **Required**: Yes

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ClusterNetworkSettingsCreateRequestTypeDef

### DefaultRoute
- **Type**: typing.Optional[str]

### InterfaceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InterfaceMappingCreateRequestTypeDef]]


# ClusterNetworkSettingsTypeDef

### DefaultRoute
- **Type**: typing.Optional[str]

### InterfaceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.InterfaceMappingTypeDef]]


# ClusterNetworkSettingsUpdateRequestTypeDef

### DefaultRoute
- **Type**: typing.Optional[str]

### InterfaceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InterfaceMappingUpdateRequestTypeDef]]


# CmafIngestGroupSettingsTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes

### NielsenId3Behavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### Scte35Type
- **Type**: typing.Optional[typing.Literal['NONE', 'SCTE_35_WITHOUT_SEGMENTATION']]

### SegmentLength
- **Type**: typing.Optional[int]

### SegmentLengthUnits
- **Type**: typing.Optional[typing.Literal['MILLISECONDS', 'SECONDS']]

### SendDelayMs
- **Type**: typing.Optional[int]

### KlvBehavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### KlvNameModifier
- **Type**: typing.Optional[str]

### NielsenId3NameModifier
- **Type**: typing.Optional[str]

### Scte35NameModifier
- **Type**: typing.Optional[str]

### Id3Behavior
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Id3NameModifier
- **Type**: typing.Optional[str]


# CmafIngestOutputSettingsTypeDef

### NameModifier
- **Type**: typing.Optional[str]


# ColorCorrectionSettingsOutputTypeDef

### GlobalColorCorrections
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ColorCorrectionTypeDef]
- **Required**: Yes


# ColorCorrectionSettingsTypeDef

### GlobalColorCorrections
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.ColorCorrectionTypeDef]
- **Required**: Yes


# ColorCorrectionTypeDef

### InputColorSpace
- **Type**: typing.Literal['HDR10', 'HLG_2020', 'REC_601', 'REC_709']
- **Required**: Yes

### OutputColorSpace
- **Type**: typing.Literal['HDR10', 'HLG_2020', 'REC_601', 'REC_709']
- **Required**: Yes

### Uri
- **Type**: <class 'str'>
- **Required**: Yes


# CreateChannelPlacementGroupRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Nodes
- **Type**: typing.Optional[typing.Sequence[str]]

### RequestId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateChannelPlacementGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Channels
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Nodes
- **Type**: typing.List[str]
- **Required**: Yes

### State
- **Type**: typing.Literal['ASSIGNED', 'ASSIGNING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UNASSIGNED', 'UNASSIGNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelRequestTypeDef

### CdiInputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef]

### ChannelClass
- **Type**: typing.Optional[typing.Literal['SINGLE_PIPELINE', 'STANDARD']]

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationUnionTypeDef]]

### EncoderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EncoderSettingsUnionTypeDef]

### InputAttachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentUnionTypeDef]]

### InputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSpecificationTypeDef]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MaintenanceCreateSettingsTypeDef]

### Name
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### Reserved
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VpcOutputSettingsTypeDef]

### AnywhereSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AnywhereSettingsTypeDef]

### ChannelEngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionRequestTypeDef]

### DryRun
- **Type**: typing.Optional[bool]


# CreateChannelResponseTypeDef

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCloudWatchAlarmTemplateGroupRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestId
- **Type**: typing.Optional[str]


# CreateCloudWatchAlarmTemplateGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCloudWatchAlarmTemplateRequestTypeDef

### ComparisonOperator
- **Type**: typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']
- **Required**: Yes

### EvaluationPeriods
- **Type**: <class 'int'>
- **Required**: Yes

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']
- **Required**: Yes

### TargetResourceType
- **Type**: typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'MEDIATAILOR_PLAYBACK_CONFIGURATION', 'S3_BUCKET']
- **Required**: Yes

### Threshold
- **Type**: <class 'float'>
- **Required**: Yes

### TreatMissingData
- **Type**: typing.Literal['breaching', 'ignore', 'missing', 'notBreaching']
- **Required**: Yes

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestId
- **Type**: typing.Optional[str]


# CreateCloudWatchAlarmTemplateResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DatapointsToAlarm
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationPeriods
- **Type**: <class 'int'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TargetResourceType
- **Type**: typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'MEDIATAILOR_PLAYBACK_CONFIGURATION', 'S3_BUCKET']
- **Required**: Yes

### Threshold
- **Type**: <class 'float'>
- **Required**: Yes

### TreatMissingData
- **Type**: typing.Literal['breaching', 'ignore', 'missing', 'notBreaching']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterRequestTypeDef

### ClusterType
- **Type**: typing.Optional[typing.Literal['ON_PREMISES']]

### InstanceRoleArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ClusterNetworkSettingsCreateRequestTypeDef]

### RequestId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateClusterResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelIds
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterType
- **Type**: typing.Literal['ON_PREMISES']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ClusterNetworkSettingsTypeDef'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventBridgeRuleTemplateGroupRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestId
- **Type**: typing.Optional[str]


# CreateEventBridgeRuleTemplateGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventBridgeRuleTemplateRequestTypeDef

### EventType
- **Type**: typing.Literal['MEDIACONNECT_ALERT', 'MEDIACONNECT_FLOW_STATUS_CHANGE', 'MEDIACONNECT_OUTPUT_HEALTH', 'MEDIACONNECT_SOURCE_HEALTH', 'MEDIALIVE_CHANNEL_ALERT', 'MEDIALIVE_CHANNEL_INPUT_CHANGE', 'MEDIALIVE_CHANNEL_STATE_CHANGE', 'MEDIALIVE_MULTIPLEX_ALERT', 'MEDIALIVE_MULTIPLEX_STATE_CHANGE', 'MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION', 'MEDIAPACKAGE_INPUT_NOTIFICATION', 'MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION', 'SIGNAL_MAP_ACTIVE_ALARM']
- **Required**: Yes

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EventTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.EventBridgeRuleTemplateTargetTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestId
- **Type**: typing.Optional[str]


# CreateEventBridgeRuleTemplateResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EventTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.EventBridgeRuleTemplateTargetTypeDef]
- **Required**: Yes

### EventType
- **Type**: typing.Literal['MEDIACONNECT_ALERT', 'MEDIACONNECT_FLOW_STATUS_CHANGE', 'MEDIACONNECT_OUTPUT_HEALTH', 'MEDIACONNECT_SOURCE_HEALTH', 'MEDIALIVE_CHANNEL_ALERT', 'MEDIALIVE_CHANNEL_INPUT_CHANGE', 'MEDIALIVE_CHANNEL_STATE_CHANGE', 'MEDIALIVE_MULTIPLEX_ALERT', 'MEDIALIVE_MULTIPLEX_STATE_CHANGE', 'MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION', 'MEDIAPACKAGE_INPUT_NOTIFICATION', 'MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION', 'SIGNAL_MAP_ACTIVE_ALARM']
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInputResponseTypeDef

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInputSecurityGroupRequestTypeDef

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### WhitelistRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputWhitelistRuleCidrTypeDef]]


# CreateInputSecurityGroupResponseTypeDef

### SecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMultiplexProgramRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexProgramSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramSettingsTypeDef'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateMultiplexProgramResponseTypeDef

### MultiplexProgram
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMultiplexRequestTypeDef

### AvailabilityZones
- **Type**: typing.Sequence[str]
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexSettingsTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMultiplexResponseTypeDef

### Multiplex
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNetworkRequestTypeDef

### IpPools
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.IpPoolCreateRequestTypeDef]]

### Name
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### Routes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.RouteCreateRequestTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateNetworkResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedClusterIds
- **Type**: typing.List[str]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IpPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.IpPoolTypeDef]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.RouteTypeDef]
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'IDLE', 'IN_USE', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNodeRegistrationScriptRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NodeInterfaceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.NodeInterfaceMappingTypeDef]]

### RequestId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'BACKUP']]


# CreateNodeRegistrationScriptResponseTypeDef

### NodeRegistrationScript
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNodeRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### NodeInterfaceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.NodeInterfaceMappingCreateRequestTypeDef]]

### RequestId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'BACKUP']]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateNodeResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelPlacementGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['CONNECTED', 'DISCONNECTED']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NodeInterfaceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.NodeInterfaceMappingTypeDef]
- **Required**: Yes

### Role
- **Type**: typing.Literal['ACTIVE', 'BACKUP']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePartnerInputRequestTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePartnerInputResponseTypeDef

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSignalMapRequestTypeDef

### DiscoveryEntryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchAlarmTemplateGroupIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### Description
- **Type**: typing.Optional[str]

### EventBridgeRuleTemplateGroupIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestId
- **Type**: typing.Optional[str]


# CreateSignalMapResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchAlarmTemplateGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DiscoveryEntryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### EventBridgeRuleTemplateGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### FailedMediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive_classes.MediaResourceTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastDiscoveredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSuccessfulMonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.SuccessfulMonitorDeploymentTypeDef'>
- **Required**: Yes

### MediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive_classes.MediaResourceTypeDef]
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitorChangesPendingDeployment
- **Type**: <class 'bool'>
- **Required**: Yes

### MonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MonitorDeploymentTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'NOT_READY', 'READY', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_REVERTED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTagsRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DeleteChannelPlacementGroupRequestTypeDef

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelPlacementGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Channels
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Nodes
- **Type**: typing.List[str]
- **Required**: Yes

### State
- **Type**: typing.Literal['ASSIGNED', 'ASSIGNING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UNASSIGNED', 'UNASSIGNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteChannelRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef'>
- **Required**: Yes

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationOutputTypeDef]
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ChannelEgressEndpointTypeDef]
- **Required**: Yes

### EncoderSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.EncoderSettingsOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentOutputTypeDef]
- **Required**: Yes

### InputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputSpecificationTypeDef'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes

### Maintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MaintenanceStatusTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.PipelineDetailTypeDef]
- **Required**: Yes

### PipelinesRunningCount
- **Type**: <class 'int'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Vpc
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.VpcOutputSettingsDescriptionTypeDef'>
- **Required**: Yes

### AnywhereSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.DescribeAnywhereSettingsTypeDef'>
- **Required**: Yes

### ChannelEngineVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCloudWatchAlarmTemplateGroupRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCloudWatchAlarmTemplateRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelIds
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterType
- **Type**: typing.Literal['ON_PREMISES']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ClusterNetworkSettingsTypeDef'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEventBridgeRuleTemplateGroupRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventBridgeRuleTemplateRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInputRequestTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInputSecurityGroupRequestTypeDef

### InputSecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiplexProgramRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiplexProgramResponseTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexProgramSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramSettingsTypeDef'>
- **Required**: Yes

### PacketIdentifiersMap
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramPacketIdentifiersMapOutputTypeDef'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramPipelineDetailTypeDef]
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMultiplexRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiplexResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.MultiplexOutputDestinationTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexSettingsTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelinesRunningCount
- **Type**: <class 'int'>
- **Required**: Yes

### ProgramCount
- **Type**: <class 'int'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNetworkRequestTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedClusterIds
- **Type**: typing.List[str]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IpPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.IpPoolTypeDef]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.RouteTypeDef]
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'IDLE', 'IN_USE', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNodeRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNodeResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelPlacementGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['CONNECTED', 'DISCONNECTED']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NodeInterfaceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.NodeInterfaceMappingTypeDef]
- **Required**: Yes

### Role
- **Type**: typing.Literal['ACTIVE', 'BACKUP']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteReservationRequestTypeDef

### ReservationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReservationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### CurrencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### DurationUnits
- **Type**: typing.Literal['MONTHS']
- **Required**: Yes

### End
- **Type**: <class 'str'>
- **Required**: Yes

### FixedPrice
- **Type**: <class 'float'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingDescription
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingType
- **Type**: typing.Literal['NO_UPFRONT']
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### RenewalSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.RenewalSettingsTypeDef'>
- **Required**: Yes

### ReservationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ReservationResourceSpecificationTypeDef'>
- **Required**: Yes

### Start
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CANCELED', 'DELETED', 'EXPIRED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### UsagePrice
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteScheduleRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSignalMapRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeAccountConfigurationResponseTypeDef

### AccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.AccountConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAnywhereSettingsTypeDef

### ChannelPlacementGroupId
- **Type**: typing.Optional[str]

### ClusterId
- **Type**: typing.Optional[str]


# DescribeChannelPlacementGroupRequestTypeDef

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelPlacementGroupRequestWaitExtraExtraTypeDef

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelPlacementGroupRequestWaitExtraTypeDef

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelPlacementGroupRequestWaitTypeDef

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelPlacementGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Channels
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Nodes
- **Type**: typing.List[str]
- **Required**: Yes

### State
- **Type**: typing.Literal['ASSIGNED', 'ASSIGNING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UNASSIGNED', 'UNASSIGNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelPlacementGroupSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### Channels
- **Type**: typing.Optional[typing.List[str]]

### ClusterId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Nodes
- **Type**: typing.Optional[typing.List[str]]

### State
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'ASSIGNING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UNASSIGNED', 'UNASSIGNING']]


# DescribeChannelRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelRequestWaitExtraExtraExtraTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelRequestWaitExtraExtraTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelRequestWaitExtraTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelRequestWaitTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef'>
- **Required**: Yes

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationOutputTypeDef]
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ChannelEgressEndpointTypeDef]
- **Required**: Yes

### EncoderSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.EncoderSettingsOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentOutputTypeDef]
- **Required**: Yes

### InputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputSpecificationTypeDef'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes

### Maintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MaintenanceStatusTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.PipelineDetailTypeDef]
- **Required**: Yes

### PipelinesRunningCount
- **Type**: <class 'int'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Vpc
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.VpcOutputSettingsDescriptionTypeDef'>
- **Required**: Yes

### AnywhereSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.DescribeAnywhereSettingsTypeDef'>
- **Required**: Yes

### ChannelEngineVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterRequestWaitExtraTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeClusterRequestWaitTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeClusterResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelIds
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterType
- **Type**: typing.Literal['ON_PREMISES']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ClusterNetworkSettingsTypeDef'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### ChannelIds
- **Type**: typing.Optional[typing.List[str]]

### ClusterType
- **Type**: typing.Optional[typing.Literal['ON_PREMISES']]

### Id
- **Type**: typing.Optional[str]

### InstanceRoleArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ClusterNetworkSettingsTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']]


# DescribeInputDeviceRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInputDeviceThumbnailRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Accept
- **Type**: typing.Literal['image/jpeg']
- **Required**: Yes


# DescribeInputDeviceThumbnailResponseTypeDef

### Body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: typing.Literal['image/jpeg']
- **Required**: Yes

### ContentLength
- **Type**: <class 'int'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInputRequestTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInputRequestWaitExtraExtraTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeInputRequestWaitExtraTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeInputRequestWaitTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeInputSecurityGroupRequestTypeDef

### InputSecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInputSecurityGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Inputs
- **Type**: typing.List[str]
- **Required**: Yes

### State
- **Type**: typing.Literal['DELETED', 'IDLE', 'IN_USE', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### WhitelistRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputWhitelistRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMultiplexProgramRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMultiplexProgramResponseTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexProgramSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramSettingsTypeDef'>
- **Required**: Yes

### PacketIdentifiersMap
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramPacketIdentifiersMapOutputTypeDef'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramPipelineDetailTypeDef]
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMultiplexRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMultiplexRequestWaitExtraExtraExtraTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeMultiplexRequestWaitExtraExtraTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeMultiplexRequestWaitExtraTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeMultiplexRequestWaitTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeMultiplexResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.MultiplexOutputDestinationTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexSettingsTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelinesRunningCount
- **Type**: <class 'int'>
- **Required**: Yes

### ProgramCount
- **Type**: <class 'int'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNetworkRequestTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNetworkResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedClusterIds
- **Type**: typing.List[str]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IpPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.IpPoolTypeDef]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.RouteTypeDef]
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'IDLE', 'IN_USE', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNetworkSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### AssociatedClusterIds
- **Type**: typing.Optional[typing.List[str]]

### Id
- **Type**: typing.Optional[str]

### IpPools
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.IpPoolTypeDef]]

### Name
- **Type**: typing.Optional[str]

### Routes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.RouteTypeDef]]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'IDLE', 'IN_USE', 'UPDATING']]


# DescribeNodeRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodeRequestWaitExtraTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeNodeRequestWaitTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeNodeResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelPlacementGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['CONNECTED', 'DISCONNECTED']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NodeInterfaceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.NodeInterfaceMappingTypeDef]
- **Required**: Yes

### Role
- **Type**: typing.Literal['ACTIVE', 'BACKUP']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNodeSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### ChannelPlacementGroups
- **Type**: typing.Optional[typing.List[str]]

### ClusterId
- **Type**: typing.Optional[str]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED']]

### Id
- **Type**: typing.Optional[str]

### InstanceArn
- **Type**: typing.Optional[str]

### ManagedInstanceId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NodeInterfaceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.NodeInterfaceMappingTypeDef]]

### Role
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'BACKUP']]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']]


# DescribeOfferingRequestTypeDef

### OfferingId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOfferingResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### DurationUnits
- **Type**: typing.Literal['MONTHS']
- **Required**: Yes

### FixedPrice
- **Type**: <class 'float'>
- **Required**: Yes

### OfferingDescription
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingType
- **Type**: typing.Literal['NO_UPFRONT']
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ReservationResourceSpecificationTypeDef'>
- **Required**: Yes

### UsagePrice
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReservationRequestTypeDef

### ReservationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReservationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### CurrencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### DurationUnits
- **Type**: typing.Literal['MONTHS']
- **Required**: Yes

### End
- **Type**: <class 'str'>
- **Required**: Yes

### FixedPrice
- **Type**: <class 'float'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingDescription
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### OfferingType
- **Type**: typing.Literal['NO_UPFRONT']
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### RenewalSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.RenewalSettingsTypeDef'>
- **Required**: Yes

### ReservationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ReservationResourceSpecificationTypeDef'>
- **Required**: Yes

### Start
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CANCELED', 'DELETED', 'EXPIRED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### UsagePrice
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeScheduleRequestPaginateTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# DescribeScheduleRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScheduleResponseTypeDef

### ScheduleActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeThumbnailsRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### ThumbnailType
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThumbnailsResponseTypeDef

### ThumbnailDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ThumbnailDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DvbNitSettingsTypeDef

### NetworkId
- **Type**: <class 'int'>
- **Required**: Yes

### NetworkName
- **Type**: <class 'str'>
- **Required**: Yes

### RepInterval
- **Type**: typing.Optional[int]


# DvbSdtSettingsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DvbSubDestinationSettingsTypeDef

### Alignment
- **Type**: typing.Optional[typing.Literal['CENTERED', 'LEFT', 'SMART']]

### BackgroundColor
- **Type**: typing.Optional[typing.Literal['BLACK', 'NONE', 'WHITE']]

### BackgroundOpacity
- **Type**: typing.Optional[int]

### Font
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef]

### FontColor
- **Type**: typing.Optional[typing.Literal['BLACK', 'BLUE', 'GREEN', 'RED', 'WHITE', 'YELLOW']]

### FontOpacity
- **Type**: typing.Optional[int]

### FontResolution
- **Type**: typing.Optional[int]

### FontSize
- **Type**: typing.Optional[str]

### OutlineColor
- **Type**: typing.Optional[typing.Literal['BLACK', 'BLUE', 'GREEN', 'RED', 'WHITE', 'YELLOW']]

### OutlineSize
- **Type**: typing.Optional[int]

### ShadowColor
- **Type**: typing.Optional[typing.Literal['BLACK', 'NONE', 'WHITE']]

### ShadowOpacity
- **Type**: typing.Optional[int]

### ShadowXOffset
- **Type**: typing.Optional[int]

### ShadowYOffset
- **Type**: typing.Optional[int]

### TeletextGridControl
- **Type**: typing.Optional[typing.Literal['FIXED', 'SCALED']]

### XPosition
- **Type**: typing.Optional[int]

### YPosition
- **Type**: typing.Optional[int]


# DvbSubSourceSettingsTypeDef

### OcrLanguage
- **Type**: typing.Optional[typing.Literal['DEU', 'ENG', 'FRA', 'NLD', 'POR', 'SPA']]

### Pid
- **Type**: typing.Optional[int]


# DvbTdtSettingsTypeDef

### RepInterval
- **Type**: typing.Optional[int]


# Eac3AtmosSettingsTypeDef

### Bitrate
- **Type**: typing.Optional[float]

### CodingMode
- **Type**: typing.Optional[typing.Literal['CODING_MODE_5_1_4', 'CODING_MODE_7_1_4', 'CODING_MODE_9_1_6']]

### Dialnorm
- **Type**: typing.Optional[int]

### DrcLine
- **Type**: typing.Optional[typing.Literal['FILM_LIGHT', 'FILM_STANDARD', 'MUSIC_LIGHT', 'MUSIC_STANDARD', 'NONE', 'SPEECH']]

### DrcRf
- **Type**: typing.Optional[typing.Literal['FILM_LIGHT', 'FILM_STANDARD', 'MUSIC_LIGHT', 'MUSIC_STANDARD', 'NONE', 'SPEECH']]

### HeightTrim
- **Type**: typing.Optional[float]

### SurroundTrim
- **Type**: typing.Optional[float]


# Eac3SettingsTypeDef

### AttenuationControl
- **Type**: typing.Optional[typing.Literal['ATTENUATE_3_DB', 'NONE']]

### Bitrate
- **Type**: typing.Optional[float]

### BitstreamMode
- **Type**: typing.Optional[typing.Literal['COMMENTARY', 'COMPLETE_MAIN', 'EMERGENCY', 'HEARING_IMPAIRED', 'VISUALLY_IMPAIRED']]

### CodingMode
- **Type**: typing.Optional[typing.Literal['CODING_MODE_1_0', 'CODING_MODE_2_0', 'CODING_MODE_3_2']]

### DcFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Dialnorm
- **Type**: typing.Optional[int]

### DrcLine
- **Type**: typing.Optional[typing.Literal['FILM_LIGHT', 'FILM_STANDARD', 'MUSIC_LIGHT', 'MUSIC_STANDARD', 'NONE', 'SPEECH']]

### DrcRf
- **Type**: typing.Optional[typing.Literal['FILM_LIGHT', 'FILM_STANDARD', 'MUSIC_LIGHT', 'MUSIC_STANDARD', 'NONE', 'SPEECH']]

### LfeControl
- **Type**: typing.Optional[typing.Literal['LFE', 'NO_LFE']]

### LfeFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### LoRoCenterMixLevel
- **Type**: typing.Optional[float]

### LoRoSurroundMixLevel
- **Type**: typing.Optional[float]

### LtRtCenterMixLevel
- **Type**: typing.Optional[float]

### LtRtSurroundMixLevel
- **Type**: typing.Optional[float]

### MetadataControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### PassthroughControl
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'WHEN_POSSIBLE']]

### PhaseControl
- **Type**: typing.Optional[typing.Literal['NO_SHIFT', 'SHIFT_90_DEGREES']]

### StereoDownmix
- **Type**: typing.Optional[typing.Literal['DPL2', 'LO_RO', 'LT_RT', 'NOT_INDICATED']]

### SurroundExMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'NOT_INDICATED']]

### SurroundMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'NOT_INDICATED']]


# EbuTtDDestinationSettingsTypeDef

### CopyrightHolder
- **Type**: typing.Optional[str]

### FillLineGap
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FontFamily
- **Type**: typing.Optional[str]

### StyleControl
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### DefaultFontSize
- **Type**: typing.Optional[int]

### DefaultLineHeight
- **Type**: typing.Optional[int]


# EmbeddedSourceSettingsTypeDef

### Convert608To708
- **Type**: typing.Optional[typing.Literal['DISABLED', 'UPCONVERT']]

### Scte20Detection
- **Type**: typing.Optional[typing.Literal['AUTO', 'OFF']]

### Source608ChannelNumber
- **Type**: typing.Optional[int]

### Source608TrackNumber
- **Type**: typing.Optional[int]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncoderSettingsOutputTypeDef

### AudioDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.AudioDescriptionOutputTypeDef]
- **Required**: Yes

### OutputGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputGroupOutputTypeDef]
- **Required**: Yes

### TimecodeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.TimecodeConfigTypeDef'>
- **Required**: Yes

### VideoDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.VideoDescriptionOutputTypeDef]
- **Required**: Yes

### AvailBlanking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AvailBlankingTypeDef]

### AvailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AvailConfigurationTypeDef]

### BlackoutSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.BlackoutSlateTypeDef]

### CaptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.CaptionDescriptionOutputTypeDef]]

### FeatureActivations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FeatureActivationsTypeDef]

### GlobalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.GlobalConfigurationOutputTypeDef]

### MotionGraphicsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MotionGraphicsConfigurationOutputTypeDef]

### NielsenConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.NielsenConfigurationTypeDef]

### ThumbnailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ThumbnailConfigurationTypeDef]

### ColorCorrectionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ColorCorrectionSettingsOutputTypeDef]


# EncoderSettingsTypeDef

### AudioDescriptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.AudioDescriptionTypeDef]
- **Required**: Yes

### OutputGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.OutputGroupTypeDef]
- **Required**: Yes

### TimecodeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.TimecodeConfigTypeDef'>
- **Required**: Yes

### VideoDescriptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.VideoDescriptionTypeDef]
- **Required**: Yes

### AvailBlanking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AvailBlankingTypeDef]

### AvailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AvailConfigurationTypeDef]

### BlackoutSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.BlackoutSlateTypeDef]

### CaptionDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.CaptionDescriptionTypeDef]]

### FeatureActivations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FeatureActivationsTypeDef]

### GlobalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.GlobalConfigurationTypeDef]

### MotionGraphicsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MotionGraphicsConfigurationTypeDef]

### NielsenConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.NielsenConfigurationTypeDef]

### ThumbnailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ThumbnailConfigurationTypeDef]

### ColorCorrectionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ColorCorrectionSettingsTypeDef]


# EncoderSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EpochLockingSettingsTypeDef

### CustomEpoch
- **Type**: typing.Optional[str]

### JamSyncTime
- **Type**: typing.Optional[str]


# EsamTypeDef

### AcquisitionPointId
- **Type**: <class 'str'>
- **Required**: Yes

### PoisEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### AdAvailOffset
- **Type**: typing.Optional[int]

### PasswordParam
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### ZoneIdentity
- **Type**: typing.Optional[str]


# EventBridgeRuleTemplateGroupSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateCount
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EventBridgeRuleTemplateSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EventTargetCount
- **Type**: <class 'int'>
- **Required**: Yes

### EventType
- **Type**: typing.Literal['MEDIACONNECT_ALERT', 'MEDIACONNECT_FLOW_STATUS_CHANGE', 'MEDIACONNECT_OUTPUT_HEALTH', 'MEDIACONNECT_SOURCE_HEALTH', 'MEDIALIVE_CHANNEL_ALERT', 'MEDIALIVE_CHANNEL_INPUT_CHANGE', 'MEDIALIVE_CHANNEL_STATE_CHANGE', 'MEDIALIVE_MULTIPLEX_ALERT', 'MEDIALIVE_MULTIPLEX_STATE_CHANGE', 'MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION', 'MEDIAPACKAGE_INPUT_NOTIFICATION', 'MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION', 'SIGNAL_MAP_ACTIVE_ALARM']
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EventBridgeRuleTemplateTargetTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# ExtraTypeDef

### OutputSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputSettingsOutputTypeDef'>
- **Required**: Yes

### AudioDescriptionNames
- **Type**: typing.Optional[typing.List[str]]

### CaptionDescriptionNames
- **Type**: typing.Optional[typing.List[str]]

### OutputName
- **Type**: typing.Optional[str]

### VideoDescriptionName
- **Type**: typing.Optional[str]


# FailoverConditionSettingsTypeDef

### AudioSilenceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioSilenceFailoverSettingsTypeDef]

### InputLossSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLossFailoverSettingsTypeDef]

### VideoBlackSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VideoBlackFailoverSettingsTypeDef]


# FailoverConditionTypeDef

### FailoverConditionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FailoverConditionSettingsTypeDef]


# FeatureActivationsTypeDef

### InputPrepareScheduleActions
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### OutputStaticImageOverlayScheduleActions
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FecOutputSettingsTypeDef

### ColumnDepth
- **Type**: typing.Optional[int]

### IncludeFec
- **Type**: typing.Optional[typing.Literal['COLUMN', 'COLUMN_AND_ROW']]

### RowLength
- **Type**: typing.Optional[int]


# FixedModeScheduleActionStartSettingsTypeDef

### Time
- **Type**: <class 'str'>
- **Required**: Yes


# Fmp4HlsSettingsTypeDef

### AudioRenditionSets
- **Type**: typing.Optional[str]

### NielsenId3Behavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### TimedMetadataBehavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]


# FollowModeScheduleActionStartSettingsTypeDef

### FollowPoint
- **Type**: typing.Literal['END', 'START']
- **Required**: Yes

### ReferenceActionName
- **Type**: <class 'str'>
- **Required**: Yes


# FrameCaptureCdnSettingsTypeDef

### FrameCaptureS3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FrameCaptureS3SettingsTypeDef]


# FrameCaptureGroupSettingsTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes

### FrameCaptureCdnSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FrameCaptureCdnSettingsTypeDef]


# FrameCaptureOutputSettingsTypeDef

### NameModifier
- **Type**: typing.Optional[str]


# FrameCaptureS3SettingsTypeDef

### CannedAcl
- **Type**: typing.Optional[typing.Literal['AUTHENTICATED_READ', 'BUCKET_OWNER_FULL_CONTROL', 'BUCKET_OWNER_READ', 'PUBLIC_READ']]


# FrameCaptureSettingsTypeDef

### CaptureInterval
- **Type**: typing.Optional[int]

### CaptureIntervalUnits
- **Type**: typing.Optional[typing.Literal['MILLISECONDS', 'SECONDS']]

### TimecodeBurninSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TimecodeBurninSettingsTypeDef]


# GetCloudWatchAlarmTemplateGroupRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCloudWatchAlarmTemplateGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCloudWatchAlarmTemplateRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCloudWatchAlarmTemplateResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DatapointsToAlarm
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationPeriods
- **Type**: <class 'int'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TargetResourceType
- **Type**: typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'MEDIATAILOR_PLAYBACK_CONFIGURATION', 'S3_BUCKET']
- **Required**: Yes

### Threshold
- **Type**: <class 'float'>
- **Required**: Yes

### TreatMissingData
- **Type**: typing.Literal['breaching', 'ignore', 'missing', 'notBreaching']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventBridgeRuleTemplateGroupRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventBridgeRuleTemplateGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventBridgeRuleTemplateRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventBridgeRuleTemplateResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EventTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.EventBridgeRuleTemplateTargetTypeDef]
- **Required**: Yes

### EventType
- **Type**: typing.Literal['MEDIACONNECT_ALERT', 'MEDIACONNECT_FLOW_STATUS_CHANGE', 'MEDIACONNECT_OUTPUT_HEALTH', 'MEDIACONNECT_SOURCE_HEALTH', 'MEDIALIVE_CHANNEL_ALERT', 'MEDIALIVE_CHANNEL_INPUT_CHANGE', 'MEDIALIVE_CHANNEL_STATE_CHANGE', 'MEDIALIVE_MULTIPLEX_ALERT', 'MEDIALIVE_MULTIPLEX_STATE_CHANGE', 'MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION', 'MEDIAPACKAGE_INPUT_NOTIFICATION', 'MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION', 'SIGNAL_MAP_ACTIVE_ALARM']
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSignalMapRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSignalMapRequestWaitExtraExtraExtraTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# GetSignalMapRequestWaitExtraExtraTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# GetSignalMapRequestWaitExtraTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# GetSignalMapRequestWaitTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# GetSignalMapResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchAlarmTemplateGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DiscoveryEntryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### EventBridgeRuleTemplateGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### FailedMediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive_classes.MediaResourceTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastDiscoveredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSuccessfulMonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.SuccessfulMonitorDeploymentTypeDef'>
- **Required**: Yes

### MediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive_classes.MediaResourceTypeDef]
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitorChangesPendingDeployment
- **Type**: <class 'bool'>
- **Required**: Yes

### MonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MonitorDeploymentTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'NOT_READY', 'READY', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_REVERTED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlobalConfigurationOutputTypeDef

### InitialAudioGain
- **Type**: typing.Optional[int]

### InputEndAction
- **Type**: typing.Optional[typing.Literal['NONE', 'SWITCH_AND_LOOP_INPUTS']]

### InputLossBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLossBehaviorTypeDef]

### OutputLockingMode
- **Type**: typing.Optional[typing.Literal['EPOCH_LOCKING', 'PIPELINE_LOCKING']]

### OutputTimingSource
- **Type**: typing.Optional[typing.Literal['INPUT_CLOCK', 'SYSTEM_CLOCK']]

### SupportLowFramerateInputs
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### OutputLockingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.OutputLockingSettingsOutputTypeDef]


# GlobalConfigurationTypeDef

### InitialAudioGain
- **Type**: typing.Optional[int]

### InputEndAction
- **Type**: typing.Optional[typing.Literal['NONE', 'SWITCH_AND_LOOP_INPUTS']]

### InputLossBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLossBehaviorTypeDef]

### OutputLockingMode
- **Type**: typing.Optional[typing.Literal['EPOCH_LOCKING', 'PIPELINE_LOCKING']]

### OutputTimingSource
- **Type**: typing.Optional[typing.Literal['INPUT_CLOCK', 'SYSTEM_CLOCK']]

### SupportLowFramerateInputs
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### OutputLockingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.OutputLockingSettingsTypeDef]


# H264ColorSpaceSettingsOutputTypeDef

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec601Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# H264ColorSpaceSettingsTypeDef

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Rec601Settings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# H264FilterSettingsTypeDef

### TemporalFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TemporalFilterSettingsTypeDef]

### BandwidthReductionFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.BandwidthReductionFilterSettingsTypeDef]


# H264SettingsOutputTypeDef

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### Bitrate
- **Type**: typing.Optional[int]

### BufFillPct
- **Type**: typing.Optional[int]

### BufSize
- **Type**: typing.Optional[int]

### ColorMetadata
- **Type**: typing.Optional[typing.Literal['IGNORE', 'INSERT']]

### ColorSpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H264ColorSpaceSettingsOutputTypeDef]

### EntropyEncoding
- **Type**: typing.Optional[typing.Literal['CABAC', 'CAVLC']]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H264FilterSettingsTypeDef]

### FixedAfd
- **Type**: typing.Optional[typing.Literal['AFD_0000', 'AFD_0010', 'AFD_0011', 'AFD_0100', 'AFD_1000', 'AFD_1001', 'AFD_1010', 'AFD_1011', 'AFD_1101', 'AFD_1110', 'AFD_1111']]

### FlickerAq
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ForceFieldPictures
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### GopBReference
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### GopClosedCadence
- **Type**: typing.Optional[int]

### GopNumBFrames
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### GopSizeUnits
- **Type**: typing.Optional[typing.Literal['FRAMES', 'SECONDS']]

### Level
- **Type**: typing.Optional[typing.Literal['H264_LEVEL_1', 'H264_LEVEL_1_1', 'H264_LEVEL_1_2', 'H264_LEVEL_1_3', 'H264_LEVEL_2', 'H264_LEVEL_2_1', 'H264_LEVEL_2_2', 'H264_LEVEL_3', 'H264_LEVEL_3_1', 'H264_LEVEL_3_2', 'H264_LEVEL_4', 'H264_LEVEL_4_1', 'H264_LEVEL_4_2', 'H264_LEVEL_5', 'H264_LEVEL_5_1', 'H264_LEVEL_5_2', 'H264_LEVEL_AUTO']]

### LookAheadRateControl
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### MaxBitrate
- **Type**: typing.Optional[int]

### MinIInterval
- **Type**: typing.Optional[int]

### NumRefFrames
- **Type**: typing.Optional[int]

### ParControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### Profile
- **Type**: typing.Optional[typing.Literal['BASELINE', 'HIGH', 'HIGH_10BIT', 'HIGH_422', 'HIGH_422_10BIT', 'MAIN']]

### QualityLevel
- **Type**: typing.Optional[typing.Literal['ENHANCED_QUALITY', 'STANDARD_QUALITY']]

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'MULTIPLEX', 'QVBR', 'VBR']]

### ScanType
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'PROGRESSIVE']]

### SceneChangeDetect
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Slices
- **Type**: typing.Optional[int]

### Softness
- **Type**: typing.Optional[int]

### SpatialAq
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SubgopLength
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'FIXED']]

### Syntax
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'RP2027']]

### TemporalAq
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TimecodeInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PIC_TIMING_SEI']]

### TimecodeBurninSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TimecodeBurninSettingsTypeDef]

### MinQp
- **Type**: typing.Optional[int]


# H264SettingsTypeDef

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### Bitrate
- **Type**: typing.Optional[int]

### BufFillPct
- **Type**: typing.Optional[int]

### BufSize
- **Type**: typing.Optional[int]

### ColorMetadata
- **Type**: typing.Optional[typing.Literal['IGNORE', 'INSERT']]

### ColorSpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H264ColorSpaceSettingsTypeDef]

### EntropyEncoding
- **Type**: typing.Optional[typing.Literal['CABAC', 'CAVLC']]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H264FilterSettingsTypeDef]

### FixedAfd
- **Type**: typing.Optional[typing.Literal['AFD_0000', 'AFD_0010', 'AFD_0011', 'AFD_0100', 'AFD_1000', 'AFD_1001', 'AFD_1010', 'AFD_1011', 'AFD_1101', 'AFD_1110', 'AFD_1111']]

### FlickerAq
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ForceFieldPictures
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### GopBReference
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### GopClosedCadence
- **Type**: typing.Optional[int]

### GopNumBFrames
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### GopSizeUnits
- **Type**: typing.Optional[typing.Literal['FRAMES', 'SECONDS']]

### Level
- **Type**: typing.Optional[typing.Literal['H264_LEVEL_1', 'H264_LEVEL_1_1', 'H264_LEVEL_1_2', 'H264_LEVEL_1_3', 'H264_LEVEL_2', 'H264_LEVEL_2_1', 'H264_LEVEL_2_2', 'H264_LEVEL_3', 'H264_LEVEL_3_1', 'H264_LEVEL_3_2', 'H264_LEVEL_4', 'H264_LEVEL_4_1', 'H264_LEVEL_4_2', 'H264_LEVEL_5', 'H264_LEVEL_5_1', 'H264_LEVEL_5_2', 'H264_LEVEL_AUTO']]

### LookAheadRateControl
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### MaxBitrate
- **Type**: typing.Optional[int]

### MinIInterval
- **Type**: typing.Optional[int]

### NumRefFrames
- **Type**: typing.Optional[int]

### ParControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### Profile
- **Type**: typing.Optional[typing.Literal['BASELINE', 'HIGH', 'HIGH_10BIT', 'HIGH_422', 'HIGH_422_10BIT', 'MAIN']]

### QualityLevel
- **Type**: typing.Optional[typing.Literal['ENHANCED_QUALITY', 'STANDARD_QUALITY']]

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'MULTIPLEX', 'QVBR', 'VBR']]

### ScanType
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'PROGRESSIVE']]

### SceneChangeDetect
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Slices
- **Type**: typing.Optional[int]

### Softness
- **Type**: typing.Optional[int]

### SpatialAq
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SubgopLength
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'FIXED']]

### Syntax
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'RP2027']]

### TemporalAq
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TimecodeInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PIC_TIMING_SEI']]

### TimecodeBurninSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TimecodeBurninSettingsTypeDef]

### MinQp
- **Type**: typing.Optional[int]


# H265ColorSpaceSettingsOutputTypeDef

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### DolbyVision81Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Hdr10Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Hdr10SettingsTypeDef]

### Rec601Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# H265ColorSpaceSettingsTypeDef

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### DolbyVision81Settings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Hdr10Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Hdr10SettingsTypeDef]

### Rec601Settings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# H265FilterSettingsTypeDef

### TemporalFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TemporalFilterSettingsTypeDef]

### BandwidthReductionFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.BandwidthReductionFilterSettingsTypeDef]


# H265SettingsOutputTypeDef

### FramerateDenominator
- **Type**: <class 'int'>
- **Required**: Yes

### FramerateNumerator
- **Type**: <class 'int'>
- **Required**: Yes

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### AlternativeTransferFunction
- **Type**: typing.Optional[typing.Literal['INSERT', 'OMIT']]

### Bitrate
- **Type**: typing.Optional[int]

### BufSize
- **Type**: typing.Optional[int]

### ColorMetadata
- **Type**: typing.Optional[typing.Literal['IGNORE', 'INSERT']]

### ColorSpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H265ColorSpaceSettingsOutputTypeDef]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H265FilterSettingsTypeDef]

### FixedAfd
- **Type**: typing.Optional[typing.Literal['AFD_0000', 'AFD_0010', 'AFD_0011', 'AFD_0100', 'AFD_1000', 'AFD_1001', 'AFD_1010', 'AFD_1011', 'AFD_1101', 'AFD_1110', 'AFD_1111']]

### FlickerAq
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### GopClosedCadence
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### GopSizeUnits
- **Type**: typing.Optional[typing.Literal['FRAMES', 'SECONDS']]

### Level
- **Type**: typing.Optional[typing.Literal['H265_LEVEL_1', 'H265_LEVEL_2', 'H265_LEVEL_2_1', 'H265_LEVEL_3', 'H265_LEVEL_3_1', 'H265_LEVEL_4', 'H265_LEVEL_4_1', 'H265_LEVEL_5', 'H265_LEVEL_5_1', 'H265_LEVEL_5_2', 'H265_LEVEL_6', 'H265_LEVEL_6_1', 'H265_LEVEL_6_2', 'H265_LEVEL_AUTO']]

### LookAheadRateControl
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### MaxBitrate
- **Type**: typing.Optional[int]

### MinIInterval
- **Type**: typing.Optional[int]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### Profile
- **Type**: typing.Optional[typing.Literal['MAIN', 'MAIN_10BIT']]

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'MULTIPLEX', 'QVBR']]

### ScanType
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'PROGRESSIVE']]

### SceneChangeDetect
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Slices
- **Type**: typing.Optional[int]

### Tier
- **Type**: typing.Optional[typing.Literal['HIGH', 'MAIN']]

### TimecodeInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PIC_TIMING_SEI']]

### TimecodeBurninSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TimecodeBurninSettingsTypeDef]

### MvOverPictureBoundaries
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### MvTemporalPredictor
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TileHeight
- **Type**: typing.Optional[int]

### TilePadding
- **Type**: typing.Optional[typing.Literal['NONE', 'PADDED']]

### TileWidth
- **Type**: typing.Optional[int]

### TreeblockSize
- **Type**: typing.Optional[typing.Literal['AUTO', 'TREE_SIZE_32X32']]

### MinQp
- **Type**: typing.Optional[int]

### Deblocking
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# H265SettingsTypeDef

### FramerateDenominator
- **Type**: <class 'int'>
- **Required**: Yes

### FramerateNumerator
- **Type**: <class 'int'>
- **Required**: Yes

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### AlternativeTransferFunction
- **Type**: typing.Optional[typing.Literal['INSERT', 'OMIT']]

### Bitrate
- **Type**: typing.Optional[int]

### BufSize
- **Type**: typing.Optional[int]

### ColorMetadata
- **Type**: typing.Optional[typing.Literal['IGNORE', 'INSERT']]

### ColorSpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H265ColorSpaceSettingsTypeDef]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H265FilterSettingsTypeDef]

### FixedAfd
- **Type**: typing.Optional[typing.Literal['AFD_0000', 'AFD_0010', 'AFD_0011', 'AFD_0100', 'AFD_1000', 'AFD_1001', 'AFD_1010', 'AFD_1011', 'AFD_1101', 'AFD_1110', 'AFD_1111']]

### FlickerAq
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### GopClosedCadence
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### GopSizeUnits
- **Type**: typing.Optional[typing.Literal['FRAMES', 'SECONDS']]

### Level
- **Type**: typing.Optional[typing.Literal['H265_LEVEL_1', 'H265_LEVEL_2', 'H265_LEVEL_2_1', 'H265_LEVEL_3', 'H265_LEVEL_3_1', 'H265_LEVEL_4', 'H265_LEVEL_4_1', 'H265_LEVEL_5', 'H265_LEVEL_5_1', 'H265_LEVEL_5_2', 'H265_LEVEL_6', 'H265_LEVEL_6_1', 'H265_LEVEL_6_2', 'H265_LEVEL_AUTO']]

### LookAheadRateControl
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### MaxBitrate
- **Type**: typing.Optional[int]

### MinIInterval
- **Type**: typing.Optional[int]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### Profile
- **Type**: typing.Optional[typing.Literal['MAIN', 'MAIN_10BIT']]

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'MULTIPLEX', 'QVBR']]

### ScanType
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'PROGRESSIVE']]

### SceneChangeDetect
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Slices
- **Type**: typing.Optional[int]

### Tier
- **Type**: typing.Optional[typing.Literal['HIGH', 'MAIN']]

### TimecodeInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PIC_TIMING_SEI']]

### TimecodeBurninSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TimecodeBurninSettingsTypeDef]

### MvOverPictureBoundaries
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### MvTemporalPredictor
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TileHeight
- **Type**: typing.Optional[int]

### TilePadding
- **Type**: typing.Optional[typing.Literal['NONE', 'PADDED']]

### TileWidth
- **Type**: typing.Optional[int]

### TreeblockSize
- **Type**: typing.Optional[typing.Literal['AUTO', 'TREE_SIZE_32X32']]

### MinQp
- **Type**: typing.Optional[int]

### Deblocking
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# Hdr10SettingsTypeDef

### MaxCll
- **Type**: typing.Optional[int]

### MaxFall
- **Type**: typing.Optional[int]


# HlsAkamaiSettingsTypeDef

### ConnectionRetryInterval
- **Type**: typing.Optional[int]

### FilecacheDuration
- **Type**: typing.Optional[int]

### HttpTransferMode
- **Type**: typing.Optional[typing.Literal['CHUNKED', 'NON_CHUNKED']]

### NumRetries
- **Type**: typing.Optional[int]

### RestartDelay
- **Type**: typing.Optional[int]

### Salt
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# HlsBasicPutSettingsTypeDef

### ConnectionRetryInterval
- **Type**: typing.Optional[int]

### FilecacheDuration
- **Type**: typing.Optional[int]

### NumRetries
- **Type**: typing.Optional[int]

### RestartDelay
- **Type**: typing.Optional[int]


# HlsCdnSettingsTypeDef

### HlsAkamaiSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsAkamaiSettingsTypeDef]

### HlsBasicPutSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsBasicPutSettingsTypeDef]

### HlsMediaStoreSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsMediaStoreSettingsTypeDef]

### HlsS3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsS3SettingsTypeDef]

### HlsWebdavSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsWebdavSettingsTypeDef]


# HlsGroupSettingsOutputTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes

### AdMarkers
- **Type**: typing.Optional[typing.List[typing.Literal['ADOBE', 'ELEMENTAL', 'ELEMENTAL_SCTE35']]]

### BaseUrlContent
- **Type**: typing.Optional[str]

### BaseUrlContent1
- **Type**: typing.Optional[str]

### BaseUrlManifest
- **Type**: typing.Optional[str]

### BaseUrlManifest1
- **Type**: typing.Optional[str]

### CaptionLanguageMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.CaptionLanguageMappingTypeDef]]

### CaptionLanguageSetting
- **Type**: typing.Optional[typing.Literal['INSERT', 'NONE', 'OMIT']]

### ClientCache
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CodecSpecification
- **Type**: typing.Optional[typing.Literal['RFC_4281', 'RFC_6381']]

### ConstantIv
- **Type**: typing.Optional[str]

### DirectoryStructure
- **Type**: typing.Optional[typing.Literal['SINGLE_DIRECTORY', 'SUBDIRECTORY_PER_STREAM']]

### DiscontinuityTags
- **Type**: typing.Optional[typing.Literal['INSERT', 'NEVER_INSERT']]

### EncryptionType
- **Type**: typing.Optional[typing.Literal['AES128', 'SAMPLE_AES']]

### HlsCdnSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsCdnSettingsTypeDef]

### HlsId3SegmentTagging
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### IFrameOnlyPlaylists
- **Type**: typing.Optional[typing.Literal['DISABLED', 'STANDARD']]

### IncompleteSegmentBehavior
- **Type**: typing.Optional[typing.Literal['AUTO', 'SUPPRESS']]

### IndexNSegments
- **Type**: typing.Optional[int]

### InputLossAction
- **Type**: typing.Optional[typing.Literal['EMIT_OUTPUT', 'PAUSE_OUTPUT']]

### IvInManifest
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### IvSource
- **Type**: typing.Optional[typing.Literal['EXPLICIT', 'FOLLOWS_SEGMENT_NUMBER']]

### KeepSegments
- **Type**: typing.Optional[int]

### KeyFormat
- **Type**: typing.Optional[str]

### KeyFormatVersions
- **Type**: typing.Optional[str]

### KeyProviderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.KeyProviderSettingsTypeDef]

### ManifestCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### ManifestDurationFormat
- **Type**: typing.Optional[typing.Literal['FLOATING_POINT', 'INTEGER']]

### MinSegmentLength
- **Type**: typing.Optional[int]

### Mode
- **Type**: typing.Optional[typing.Literal['LIVE', 'VOD']]

### OutputSelection
- **Type**: typing.Optional[typing.Literal['MANIFESTS_AND_SEGMENTS', 'SEGMENTS_ONLY', 'VARIANT_MANIFESTS_AND_SEGMENTS']]

### ProgramDateTime
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### ProgramDateTimeClock
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_OUTPUT_TIMECODE', 'SYSTEM_CLOCK']]

### ProgramDateTimePeriod
- **Type**: typing.Optional[int]

### RedundantManifest
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SegmentLength
- **Type**: typing.Optional[int]

### SegmentationMode
- **Type**: typing.Optional[typing.Literal['USE_INPUT_SEGMENTATION', 'USE_SEGMENT_DURATION']]

### SegmentsPerSubdirectory
- **Type**: typing.Optional[int]

### StreamInfResolution
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### TimedMetadataId3Frame
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIV', 'TDRL']]

### TimedMetadataId3Period
- **Type**: typing.Optional[int]

### TimestampDeltaMilliseconds
- **Type**: typing.Optional[int]

### TsFileMode
- **Type**: typing.Optional[typing.Literal['SEGMENTED_FILES', 'SINGLE_FILE']]


# HlsGroupSettingsTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes

### AdMarkers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADOBE', 'ELEMENTAL', 'ELEMENTAL_SCTE35']]]

### BaseUrlContent
- **Type**: typing.Optional[str]

### BaseUrlContent1
- **Type**: typing.Optional[str]

### BaseUrlManifest
- **Type**: typing.Optional[str]

### BaseUrlManifest1
- **Type**: typing.Optional[str]

### CaptionLanguageMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.CaptionLanguageMappingTypeDef]]

### CaptionLanguageSetting
- **Type**: typing.Optional[typing.Literal['INSERT', 'NONE', 'OMIT']]

### ClientCache
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CodecSpecification
- **Type**: typing.Optional[typing.Literal['RFC_4281', 'RFC_6381']]

### ConstantIv
- **Type**: typing.Optional[str]

### DirectoryStructure
- **Type**: typing.Optional[typing.Literal['SINGLE_DIRECTORY', 'SUBDIRECTORY_PER_STREAM']]

### DiscontinuityTags
- **Type**: typing.Optional[typing.Literal['INSERT', 'NEVER_INSERT']]

### EncryptionType
- **Type**: typing.Optional[typing.Literal['AES128', 'SAMPLE_AES']]

### HlsCdnSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsCdnSettingsTypeDef]

### HlsId3SegmentTagging
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### IFrameOnlyPlaylists
- **Type**: typing.Optional[typing.Literal['DISABLED', 'STANDARD']]

### IncompleteSegmentBehavior
- **Type**: typing.Optional[typing.Literal['AUTO', 'SUPPRESS']]

### IndexNSegments
- **Type**: typing.Optional[int]

### InputLossAction
- **Type**: typing.Optional[typing.Literal['EMIT_OUTPUT', 'PAUSE_OUTPUT']]

### IvInManifest
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### IvSource
- **Type**: typing.Optional[typing.Literal['EXPLICIT', 'FOLLOWS_SEGMENT_NUMBER']]

### KeepSegments
- **Type**: typing.Optional[int]

### KeyFormat
- **Type**: typing.Optional[str]

### KeyFormatVersions
- **Type**: typing.Optional[str]

### KeyProviderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.KeyProviderSettingsTypeDef]

### ManifestCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### ManifestDurationFormat
- **Type**: typing.Optional[typing.Literal['FLOATING_POINT', 'INTEGER']]

### MinSegmentLength
- **Type**: typing.Optional[int]

### Mode
- **Type**: typing.Optional[typing.Literal['LIVE', 'VOD']]

### OutputSelection
- **Type**: typing.Optional[typing.Literal['MANIFESTS_AND_SEGMENTS', 'SEGMENTS_ONLY', 'VARIANT_MANIFESTS_AND_SEGMENTS']]

### ProgramDateTime
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### ProgramDateTimeClock
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_OUTPUT_TIMECODE', 'SYSTEM_CLOCK']]

### ProgramDateTimePeriod
- **Type**: typing.Optional[int]

### RedundantManifest
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SegmentLength
- **Type**: typing.Optional[int]

### SegmentationMode
- **Type**: typing.Optional[typing.Literal['USE_INPUT_SEGMENTATION', 'USE_SEGMENT_DURATION']]

### SegmentsPerSubdirectory
- **Type**: typing.Optional[int]

### StreamInfResolution
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### TimedMetadataId3Frame
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIV', 'TDRL']]

### TimedMetadataId3Period
- **Type**: typing.Optional[int]

### TimestampDeltaMilliseconds
- **Type**: typing.Optional[int]

### TsFileMode
- **Type**: typing.Optional[typing.Literal['SEGMENTED_FILES', 'SINGLE_FILE']]


# HlsId3SegmentTaggingScheduleActionSettingsTypeDef

### Tag
- **Type**: typing.Optional[str]

### Id3
- **Type**: typing.Optional[str]


# HlsInputSettingsTypeDef

### Bandwidth
- **Type**: typing.Optional[int]

### BufferSegments
- **Type**: typing.Optional[int]

### Retries
- **Type**: typing.Optional[int]

### RetryInterval
- **Type**: typing.Optional[int]

### Scte35Source
- **Type**: typing.Optional[typing.Literal['MANIFEST', 'SEGMENTS']]


# HlsMediaStoreSettingsTypeDef

### ConnectionRetryInterval
- **Type**: typing.Optional[int]

### FilecacheDuration
- **Type**: typing.Optional[int]

### MediaStoreStorageClass
- **Type**: typing.Optional[typing.Literal['TEMPORAL']]

### NumRetries
- **Type**: typing.Optional[int]

### RestartDelay
- **Type**: typing.Optional[int]


# HlsOutputSettingsOutputTypeDef

### HlsSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.HlsSettingsOutputTypeDef'>
- **Required**: Yes

### H265PackagingType
- **Type**: typing.Optional[typing.Literal['HEV1', 'HVC1']]

### NameModifier
- **Type**: typing.Optional[str]

### SegmentModifier
- **Type**: typing.Optional[str]


# HlsOutputSettingsTypeDef

### HlsSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.HlsSettingsTypeDef'>
- **Required**: Yes

### H265PackagingType
- **Type**: typing.Optional[typing.Literal['HEV1', 'HVC1']]

### NameModifier
- **Type**: typing.Optional[str]

### SegmentModifier
- **Type**: typing.Optional[str]


# HlsS3SettingsTypeDef

### CannedAcl
- **Type**: typing.Optional[typing.Literal['AUTHENTICATED_READ', 'BUCKET_OWNER_FULL_CONTROL', 'BUCKET_OWNER_READ', 'PUBLIC_READ']]


# HlsSettingsOutputTypeDef

### AudioOnlyHlsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioOnlyHlsSettingsTypeDef]

### Fmp4HlsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Fmp4HlsSettingsTypeDef]

### FrameCaptureHlsSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### StandardHlsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StandardHlsSettingsTypeDef]


# HlsSettingsTypeDef

### AudioOnlyHlsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioOnlyHlsSettingsTypeDef]

### Fmp4HlsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Fmp4HlsSettingsTypeDef]

### FrameCaptureHlsSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### StandardHlsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StandardHlsSettingsTypeDef]


# HlsTimedMetadataScheduleActionSettingsTypeDef

### Id3
- **Type**: <class 'str'>
- **Required**: Yes


# HlsWebdavSettingsTypeDef

### ConnectionRetryInterval
- **Type**: typing.Optional[int]

### FilecacheDuration
- **Type**: typing.Optional[int]

### HttpTransferMode
- **Type**: typing.Optional[typing.Literal['CHUNKED', 'NON_CHUNKED']]

### NumRetries
- **Type**: typing.Optional[int]

### RestartDelay
- **Type**: typing.Optional[int]


# Id3SegmentTaggingScheduleActionSettingsTypeDef

### Id3
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[str]


# InputAttachmentOutputTypeDef

### AutomaticInputFailoverSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AutomaticInputFailoverSettingsOutputTypeDef]

### InputAttachmentName
- **Type**: typing.Optional[str]

### InputId
- **Type**: typing.Optional[str]

### InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSettingsOutputTypeDef]

### LogicalInterfaceNames
- **Type**: typing.Optional[typing.List[str]]


# InputAttachmentTypeDef

### AutomaticInputFailoverSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AutomaticInputFailoverSettingsUnionTypeDef]

### InputAttachmentName
- **Type**: typing.Optional[str]

### InputId
- **Type**: typing.Optional[str]

### InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSettingsUnionTypeDef]

### LogicalInterfaceNames
- **Type**: typing.Optional[typing.Sequence[str]]


# InputAttachmentUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputChannelLevelTypeDef

### Gain
- **Type**: <class 'int'>
- **Required**: Yes

### InputChannel
- **Type**: <class 'int'>
- **Required**: Yes


# InputClippingSettingsTypeDef

### InputTimecodeSource
- **Type**: typing.Literal['EMBEDDED', 'ZEROBASED']
- **Required**: Yes

### StartTimecode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StartTimecodeTypeDef]

### StopTimecode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StopTimecodeTypeDef]


# InputDestinationRequestTypeDef

### StreamName
- **Type**: typing.Optional[str]

### Network
- **Type**: typing.Optional[str]

### NetworkRoutes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputRequestDestinationRouteTypeDef]]

### StaticIpAddress
- **Type**: typing.Optional[str]


# InputDestinationRouteTypeDef

### Cidr
- **Type**: typing.Optional[str]

### Gateway
- **Type**: typing.Optional[str]


# InputDestinationTypeDef

### Ip
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputDestinationVpcTypeDef]

### Network
- **Type**: typing.Optional[str]

### NetworkRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputDestinationRouteTypeDef]]


# InputDestinationVpcTypeDef

### AvailabilityZone
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]


# InputDeviceConfigurableAudioChannelPairConfigTypeDef

### Id
- **Type**: typing.Optional[int]

### Profile
- **Type**: typing.Optional[typing.Literal['CBR-AAC_HQ-192000', 'CBR-AAC_HQ-256000', 'CBR-AAC_HQ-384000', 'CBR-AAC_HQ-512000', 'DISABLED', 'VBR-AAC_HE-64000', 'VBR-AAC_HHE-16000', 'VBR-AAC_LC-128000']]


# InputDeviceConfigurableSettingsTypeDef

### ConfiguredInput
- **Type**: typing.Optional[typing.Literal['AUTO', 'HDMI', 'SDI']]

### MaxBitrate
- **Type**: typing.Optional[int]

### LatencyMs
- **Type**: typing.Optional[int]

### Codec
- **Type**: typing.Optional[typing.Literal['AVC', 'HEVC']]

### MediaconnectSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceMediaConnectConfigurableSettingsTypeDef]

### AudioChannelPairs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceConfigurableAudioChannelPairConfigTypeDef]]


# InputDeviceHdSettingsTypeDef

### ActiveInput
- **Type**: typing.Optional[typing.Literal['HDMI', 'SDI']]

### ConfiguredInput
- **Type**: typing.Optional[typing.Literal['AUTO', 'HDMI', 'SDI']]

### DeviceState
- **Type**: typing.Optional[typing.Literal['IDLE', 'STREAMING']]

### Framerate
- **Type**: typing.Optional[float]

### Height
- **Type**: typing.Optional[int]

### MaxBitrate
- **Type**: typing.Optional[int]

### ScanType
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'PROGRESSIVE']]

### Width
- **Type**: typing.Optional[int]

### LatencyMs
- **Type**: typing.Optional[int]


# InputDeviceMediaConnectConfigurableSettingsTypeDef

### FlowArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### SourceName
- **Type**: typing.Optional[str]


# InputDeviceMediaConnectSettingsTypeDef

### FlowArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### SourceName
- **Type**: typing.Optional[str]


# InputDeviceNetworkSettingsTypeDef

### DnsAddresses
- **Type**: typing.Optional[typing.List[str]]

### Gateway
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### IpScheme
- **Type**: typing.Optional[typing.Literal['DHCP', 'STATIC']]

### SubnetMask
- **Type**: typing.Optional[str]


# InputDeviceRequestTypeDef

### Id
- **Type**: typing.Optional[str]


# InputDeviceSettingsTypeDef

### Id
- **Type**: typing.Optional[str]


# InputDeviceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputDeviceUhdAudioChannelPairConfigTypeDef

### Id
- **Type**: typing.Optional[int]

### Profile
- **Type**: typing.Optional[typing.Literal['CBR-AAC_HQ-192000', 'CBR-AAC_HQ-256000', 'CBR-AAC_HQ-384000', 'CBR-AAC_HQ-512000', 'DISABLED', 'VBR-AAC_HE-64000', 'VBR-AAC_HHE-16000', 'VBR-AAC_LC-128000']]


# InputDeviceUhdSettingsTypeDef

### ActiveInput
- **Type**: typing.Optional[typing.Literal['HDMI', 'SDI']]

### ConfiguredInput
- **Type**: typing.Optional[typing.Literal['AUTO', 'HDMI', 'SDI']]

### DeviceState
- **Type**: typing.Optional[typing.Literal['IDLE', 'STREAMING']]

### Framerate
- **Type**: typing.Optional[float]

### Height
- **Type**: typing.Optional[int]

### MaxBitrate
- **Type**: typing.Optional[int]

### ScanType
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'PROGRESSIVE']]

### Width
- **Type**: typing.Optional[int]

### LatencyMs
- **Type**: typing.Optional[int]

### Codec
- **Type**: typing.Optional[typing.Literal['AVC', 'HEVC']]

### MediaconnectSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceMediaConnectSettingsTypeDef]

### AudioChannelPairs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceUhdAudioChannelPairConfigTypeDef]]


# InputLocationTypeDef

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### PasswordParam
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# InputLossBehaviorTypeDef

### BlackFrameMsec
- **Type**: typing.Optional[int]

### InputLossImageColor
- **Type**: typing.Optional[str]

### InputLossImageSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef]

### InputLossImageType
- **Type**: typing.Optional[typing.Literal['COLOR', 'SLATE']]

### RepeatFrameMsec
- **Type**: typing.Optional[int]


# InputLossFailoverSettingsTypeDef

### InputLossThresholdMsec
- **Type**: typing.Optional[int]


# InputPrepareScheduleActionSettingsOutputTypeDef

### InputAttachmentNameReference
- **Type**: typing.Optional[str]

### InputClippingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputClippingSettingsTypeDef]

### UrlPath
- **Type**: typing.Optional[typing.List[str]]


# InputPrepareScheduleActionSettingsTypeDef

### InputAttachmentNameReference
- **Type**: typing.Optional[str]

### InputClippingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputClippingSettingsTypeDef]

### UrlPath
- **Type**: typing.Optional[typing.Sequence[str]]


# InputPrepareScheduleActionSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputRequestDestinationRouteTypeDef

### Cidr
- **Type**: typing.Optional[str]

### Gateway
- **Type**: typing.Optional[str]


# InputSecurityGroupTypeDef

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Inputs
- **Type**: typing.Optional[typing.List[str]]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'IDLE', 'IN_USE', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### WhitelistRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputWhitelistRuleTypeDef]]


# InputSettingsOutputTypeDef

### AudioSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.AudioSelectorOutputTypeDef]]

### CaptionSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.CaptionSelectorOutputTypeDef]]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FilterStrength
- **Type**: typing.Optional[int]

### InputFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'FORCED']]

### NetworkInputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.NetworkInputSettingsTypeDef]

### Scte35Pid
- **Type**: typing.Optional[int]

### Smpte2038DataPreference
- **Type**: typing.Optional[typing.Literal['IGNORE', 'PREFER']]

### SourceEndBehavior
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'LOOP']]

### VideoSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VideoSelectorTypeDef]


# InputSettingsTypeDef

### AudioSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.AudioSelectorUnionTypeDef]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.CaptionSelectorUnionTypeDef]]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FilterStrength
- **Type**: typing.Optional[int]

### InputFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'FORCED']]

### NetworkInputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.NetworkInputSettingsTypeDef]

### Scte35Pid
- **Type**: typing.Optional[int]

### Smpte2038DataPreference
- **Type**: typing.Optional[typing.Literal['IGNORE', 'PREFER']]

### SourceEndBehavior
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'LOOP']]

### VideoSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VideoSelectorTypeDef]


# InputSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputSourceRequestTypeDef

### PasswordParam
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# InputSourceTypeDef

### PasswordParam
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# InputSpecificationTypeDef

### Codec
- **Type**: typing.Optional[typing.Literal['AVC', 'HEVC', 'MPEG2']]

### MaximumBitrate
- **Type**: typing.Optional[typing.Literal['MAX_10_MBPS', 'MAX_20_MBPS', 'MAX_50_MBPS']]

### Resolution
- **Type**: typing.Optional[typing.Literal['HD', 'SD', 'UHD']]


# InputSwitchScheduleActionSettingsOutputTypeDef

### InputAttachmentNameReference
- **Type**: <class 'str'>
- **Required**: Yes

### InputClippingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputClippingSettingsTypeDef]

### UrlPath
- **Type**: typing.Optional[typing.List[str]]


# InputSwitchScheduleActionSettingsTypeDef

### InputAttachmentNameReference
- **Type**: <class 'str'>
- **Required**: Yes

### InputClippingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputClippingSettingsTypeDef]

### UrlPath
- **Type**: typing.Optional[typing.Sequence[str]]


# InputSwitchScheduleActionSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputVpcRequestTypeDef

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# InputWhitelistRuleCidrTypeDef

### Cidr
- **Type**: typing.Optional[str]


# InputWhitelistRuleTypeDef

### Cidr
- **Type**: typing.Optional[str]


# InterfaceMappingCreateRequestTypeDef

### LogicalInterfaceName
- **Type**: typing.Optional[str]

### NetworkId
- **Type**: typing.Optional[str]


# InterfaceMappingTypeDef

### LogicalInterfaceName
- **Type**: typing.Optional[str]

### NetworkId
- **Type**: typing.Optional[str]


# InterfaceMappingUpdateRequestTypeDef

### LogicalInterfaceName
- **Type**: typing.Optional[str]

### NetworkId
- **Type**: typing.Optional[str]


# IpPoolCreateRequestTypeDef

### Cidr
- **Type**: typing.Optional[str]


# IpPoolTypeDef

### Cidr
- **Type**: typing.Optional[str]


# IpPoolUpdateRequestTypeDef

### Cidr
- **Type**: typing.Optional[str]


# KeyProviderSettingsTypeDef

### StaticKeySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticKeySettingsTypeDef]


# ListChannelPlacementGroupsRequestPaginateTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListChannelPlacementGroupsRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelPlacementGroupsResponseTypeDef

### ChannelPlacementGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.DescribeChannelPlacementGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListChannelsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ChannelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCloudWatchAlarmTemplateGroupsRequestPaginateTypeDef

### Scope
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListCloudWatchAlarmTemplateGroupsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]


# ListCloudWatchAlarmTemplateGroupsResponseTypeDef

### CloudWatchAlarmTemplateGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.CloudWatchAlarmTemplateGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCloudWatchAlarmTemplatesRequestPaginateTypeDef

### GroupIdentifier
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListCloudWatchAlarmTemplatesRequestTypeDef

### GroupIdentifier
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]


# ListCloudWatchAlarmTemplatesResponseTypeDef

### CloudWatchAlarmTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.CloudWatchAlarmTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListClustersRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersResponseTypeDef

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.DescribeClusterSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventBridgeRuleTemplateGroupsRequestPaginateTypeDef

### SignalMapIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListEventBridgeRuleTemplateGroupsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]


# ListEventBridgeRuleTemplateGroupsResponseTypeDef

### EventBridgeRuleTemplateGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.EventBridgeRuleTemplateGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventBridgeRuleTemplatesRequestPaginateTypeDef

### GroupIdentifier
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListEventBridgeRuleTemplatesRequestTypeDef

### GroupIdentifier
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]


# ListEventBridgeRuleTemplatesResponseTypeDef

### EventBridgeRuleTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.EventBridgeRuleTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInputDeviceTransfersRequestPaginateTypeDef

### TransferType
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListInputDeviceTransfersRequestTypeDef

### TransferType
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInputDeviceTransfersResponseTypeDef

### InputDeviceTransfers
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.TransferringInputDeviceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInputDevicesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListInputDevicesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInputDevicesResponseTypeDef

### InputDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInputSecurityGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListInputSecurityGroupsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInputSecurityGroupsResponseTypeDef

### InputSecurityGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputSecurityGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInputsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListInputsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInputsResponseTypeDef

### Inputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMultiplexProgramsRequestPaginateTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListMultiplexProgramsRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMultiplexProgramsResponseTypeDef

### MultiplexPrograms
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMultiplexesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListMultiplexesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMultiplexesResponseTypeDef

### Multiplexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.MultiplexSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNetworksRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListNetworksRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNetworksResponseTypeDef

### Networks
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.DescribeNetworkSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesRequestPaginateTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListNodesRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNodesResponseTypeDef

### Nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.DescribeNodeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOfferingsRequestPaginateTypeDef

### ChannelClass
- **Type**: typing.Optional[str]

### ChannelConfiguration
- **Type**: typing.Optional[str]

### Codec
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### MaximumBitrate
- **Type**: typing.Optional[str]

### MaximumFramerate
- **Type**: typing.Optional[str]

### Resolution
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### SpecialFeature
- **Type**: typing.Optional[str]

### VideoQuality
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListOfferingsRequestTypeDef

### ChannelClass
- **Type**: typing.Optional[str]

### ChannelConfiguration
- **Type**: typing.Optional[str]

### Codec
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### MaximumBitrate
- **Type**: typing.Optional[str]

### MaximumFramerate
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Resolution
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### SpecialFeature
- **Type**: typing.Optional[str]

### VideoQuality
- **Type**: typing.Optional[str]


# ListOfferingsResponseTypeDef

### Offerings
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.OfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReservationsRequestPaginateTypeDef

### ChannelClass
- **Type**: typing.Optional[str]

### Codec
- **Type**: typing.Optional[str]

### MaximumBitrate
- **Type**: typing.Optional[str]

### MaximumFramerate
- **Type**: typing.Optional[str]

### Resolution
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### SpecialFeature
- **Type**: typing.Optional[str]

### VideoQuality
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListReservationsRequestTypeDef

### ChannelClass
- **Type**: typing.Optional[str]

### Codec
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### MaximumBitrate
- **Type**: typing.Optional[str]

### MaximumFramerate
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Resolution
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### SpecialFeature
- **Type**: typing.Optional[str]

### VideoQuality
- **Type**: typing.Optional[str]


# ListReservationsResponseTypeDef

### Reservations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ReservationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSignalMapsRequestPaginateTypeDef

### CloudWatchAlarmTemplateGroupIdentifier
- **Type**: typing.Optional[str]

### EventBridgeRuleTemplateGroupIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListSignalMapsRequestTypeDef

### CloudWatchAlarmTemplateGroupIdentifier
- **Type**: typing.Optional[str]

### EventBridgeRuleTemplateGroupIdentifier
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSignalMapsResponseTypeDef

### SignalMaps
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.SignalMapSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# M2tsSettingsTypeDef

### AbsentInputAudioBehavior
- **Type**: typing.Optional[typing.Literal['DROP', 'ENCODE_SILENCE']]

### Arib
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AribCaptionsPid
- **Type**: typing.Optional[str]

### AribCaptionsPidControl
- **Type**: typing.Optional[typing.Literal['AUTO', 'USE_CONFIGURED']]

### AudioBufferModel
- **Type**: typing.Optional[typing.Literal['ATSC', 'DVB']]

### AudioFramesPerPes
- **Type**: typing.Optional[int]

### AudioPids
- **Type**: typing.Optional[str]

### AudioStreamType
- **Type**: typing.Optional[typing.Literal['ATSC', 'DVB']]

### Bitrate
- **Type**: typing.Optional[int]

### BufferModel
- **Type**: typing.Optional[typing.Literal['MULTIPLEX', 'NONE']]

### CcDescriptor
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DvbNitSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.DvbNitSettingsTypeDef]

### DvbSdtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.DvbSdtSettingsTypeDef]

### DvbSubPids
- **Type**: typing.Optional[str]

### DvbTdtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.DvbTdtSettingsTypeDef]

### DvbTeletextPid
- **Type**: typing.Optional[str]

### Ebif
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### EbpAudioInterval
- **Type**: typing.Optional[typing.Literal['VIDEO_AND_FIXED_INTERVALS', 'VIDEO_INTERVAL']]

### EbpLookaheadMs
- **Type**: typing.Optional[int]

### EbpPlacement
- **Type**: typing.Optional[typing.Literal['VIDEO_AND_AUDIO_PIDS', 'VIDEO_PID']]

### EcmPid
- **Type**: typing.Optional[str]

### EsRateInPes
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### EtvPlatformPid
- **Type**: typing.Optional[str]

### EtvSignalPid
- **Type**: typing.Optional[str]

### FragmentTime
- **Type**: typing.Optional[float]

### Klv
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### KlvDataPids
- **Type**: typing.Optional[str]

### NielsenId3Behavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### NullPacketBitrate
- **Type**: typing.Optional[float]

### PatInterval
- **Type**: typing.Optional[int]

### PcrControl
- **Type**: typing.Optional[typing.Literal['CONFIGURED_PCR_PERIOD', 'PCR_EVERY_PES_PACKET']]

### PcrPeriod
- **Type**: typing.Optional[int]

### PcrPid
- **Type**: typing.Optional[str]

### PmtInterval
- **Type**: typing.Optional[int]

### PmtPid
- **Type**: typing.Optional[str]

### ProgramNum
- **Type**: typing.Optional[int]

### RateMode
- **Type**: typing.Optional[typing.Literal['CBR', 'VBR']]

### Scte27Pids
- **Type**: typing.Optional[str]

### Scte35Control
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### Scte35Pid
- **Type**: typing.Optional[str]

### SegmentationMarkers
- **Type**: typing.Optional[typing.Literal['EBP', 'EBP_LEGACY', 'NONE', 'PSI_SEGSTART', 'RAI_ADAPT', 'RAI_SEGSTART']]

### SegmentationStyle
- **Type**: typing.Optional[typing.Literal['MAINTAIN_CADENCE', 'RESET_CADENCE']]

### SegmentationTime
- **Type**: typing.Optional[float]

### TimedMetadataBehavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### TimedMetadataPid
- **Type**: typing.Optional[str]

### TransportStreamId
- **Type**: typing.Optional[int]

### VideoPid
- **Type**: typing.Optional[str]

### Scte35PrerollPullupMilliseconds
- **Type**: typing.Optional[float]


# M3u8SettingsTypeDef

### AudioFramesPerPes
- **Type**: typing.Optional[int]

### AudioPids
- **Type**: typing.Optional[str]

### EcmPid
- **Type**: typing.Optional[str]

### NielsenId3Behavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### PatInterval
- **Type**: typing.Optional[int]

### PcrControl
- **Type**: typing.Optional[typing.Literal['CONFIGURED_PCR_PERIOD', 'PCR_EVERY_PES_PACKET']]

### PcrPeriod
- **Type**: typing.Optional[int]

### PcrPid
- **Type**: typing.Optional[str]

### PmtInterval
- **Type**: typing.Optional[int]

### PmtPid
- **Type**: typing.Optional[str]

### ProgramNum
- **Type**: typing.Optional[int]

### Scte35Behavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### Scte35Pid
- **Type**: typing.Optional[str]

### TimedMetadataBehavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### TimedMetadataPid
- **Type**: typing.Optional[str]

### TransportStreamId
- **Type**: typing.Optional[int]

### VideoPid
- **Type**: typing.Optional[str]

### KlvBehavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### KlvDataPids
- **Type**: typing.Optional[str]


# MaintenanceCreateSettingsTypeDef

### MaintenanceDay
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### MaintenanceStartTime
- **Type**: typing.Optional[str]


# MaintenanceStatusTypeDef

### MaintenanceDay
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### MaintenanceDeadline
- **Type**: typing.Optional[str]

### MaintenanceScheduledDate
- **Type**: typing.Optional[str]

### MaintenanceStartTime
- **Type**: typing.Optional[str]


# MaintenanceUpdateSettingsTypeDef

### MaintenanceDay
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### MaintenanceScheduledDate
- **Type**: typing.Optional[str]

### MaintenanceStartTime
- **Type**: typing.Optional[str]


# MediaConnectFlowRequestTypeDef

### FlowArn
- **Type**: typing.Optional[str]


# MediaConnectFlowTypeDef

### FlowArn
- **Type**: typing.Optional[str]


# MediaPackageGroupSettingsTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes


# MediaPackageOutputDestinationSettingsTypeDef

### ChannelId
- **Type**: typing.Optional[str]

### ChannelGroup
- **Type**: typing.Optional[str]

### ChannelName
- **Type**: typing.Optional[str]


# MediaResourceNeighborTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# MediaResourceTypeDef

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.MediaResourceNeighborTypeDef]]

### Name
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.MediaResourceNeighborTypeDef]]


# MonitorDeploymentTypeDef

### Status
- **Type**: typing.Literal['DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DEPLOYMENT_COMPLETE', 'DEPLOYMENT_FAILED', 'DEPLOYMENT_IN_PROGRESS', 'DRY_RUN_DEPLOYMENT_COMPLETE', 'DRY_RUN_DEPLOYMENT_FAILED', 'DRY_RUN_DEPLOYMENT_IN_PROGRESS', 'NOT_DEPLOYED']
- **Required**: Yes

### DetailsUri
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# MotionGraphicsActivateScheduleActionSettingsTypeDef

### Duration
- **Type**: typing.Optional[int]

### PasswordParam
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# MotionGraphicsConfigurationOutputTypeDef

### MotionGraphicsSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MotionGraphicsSettingsOutputTypeDef'>
- **Required**: Yes

### MotionGraphicsInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MotionGraphicsConfigurationTypeDef

### MotionGraphicsSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MotionGraphicsSettingsTypeDef'>
- **Required**: Yes

### MotionGraphicsInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MotionGraphicsSettingsOutputTypeDef

### HtmlMotionGraphicsSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# MotionGraphicsSettingsTypeDef

### HtmlMotionGraphicsSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# Mp2SettingsTypeDef

### Bitrate
- **Type**: typing.Optional[float]

### CodingMode
- **Type**: typing.Optional[typing.Literal['CODING_MODE_1_0', 'CODING_MODE_2_0']]

### SampleRate
- **Type**: typing.Optional[float]


# Mpeg2FilterSettingsTypeDef

### TemporalFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TemporalFilterSettingsTypeDef]


# Mpeg2SettingsTypeDef

### FramerateDenominator
- **Type**: <class 'int'>
- **Required**: Yes

### FramerateNumerator
- **Type**: <class 'int'>
- **Required**: Yes

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'OFF']]

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### ColorMetadata
- **Type**: typing.Optional[typing.Literal['IGNORE', 'INSERT']]

### ColorSpace
- **Type**: typing.Optional[typing.Literal['AUTO', 'PASSTHROUGH']]

### DisplayAspectRatio
- **Type**: typing.Optional[typing.Literal['DISPLAYRATIO16X9', 'DISPLAYRATIO4X3']]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Mpeg2FilterSettingsTypeDef]

### FixedAfd
- **Type**: typing.Optional[typing.Literal['AFD_0000', 'AFD_0010', 'AFD_0011', 'AFD_0100', 'AFD_1000', 'AFD_1001', 'AFD_1010', 'AFD_1011', 'AFD_1101', 'AFD_1110', 'AFD_1111']]

### GopClosedCadence
- **Type**: typing.Optional[int]

### GopNumBFrames
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### GopSizeUnits
- **Type**: typing.Optional[typing.Literal['FRAMES', 'SECONDS']]

### ScanType
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'PROGRESSIVE']]

### SubgopLength
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'FIXED']]

### TimecodeInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'GOP_TIMECODE']]

### TimecodeBurninSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TimecodeBurninSettingsTypeDef]


# MsSmoothGroupSettingsTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes

### AcquisitionPointId
- **Type**: typing.Optional[str]

### AudioOnlyTimecodeControl
- **Type**: typing.Optional[typing.Literal['PASSTHROUGH', 'USE_CONFIGURED_CLOCK']]

### CertificateMode
- **Type**: typing.Optional[typing.Literal['SELF_SIGNED', 'VERIFY_AUTHENTICITY']]

### ConnectionRetryInterval
- **Type**: typing.Optional[int]

### EventId
- **Type**: typing.Optional[str]

### EventIdMode
- **Type**: typing.Optional[typing.Literal['NO_EVENT_ID', 'USE_CONFIGURED', 'USE_TIMESTAMP']]

### EventStopBehavior
- **Type**: typing.Optional[typing.Literal['NONE', 'SEND_EOS']]

### FilecacheDuration
- **Type**: typing.Optional[int]

### FragmentLength
- **Type**: typing.Optional[int]

### InputLossAction
- **Type**: typing.Optional[typing.Literal['EMIT_OUTPUT', 'PAUSE_OUTPUT']]

### NumRetries
- **Type**: typing.Optional[int]

### RestartDelay
- **Type**: typing.Optional[int]

### SegmentationMode
- **Type**: typing.Optional[typing.Literal['USE_INPUT_SEGMENTATION', 'USE_SEGMENT_DURATION']]

### SendDelayMs
- **Type**: typing.Optional[int]

### SparseTrackType
- **Type**: typing.Optional[typing.Literal['NONE', 'SCTE_35', 'SCTE_35_WITHOUT_SEGMENTATION']]

### StreamManifestBehavior
- **Type**: typing.Optional[typing.Literal['DO_NOT_SEND', 'SEND']]

### TimestampOffset
- **Type**: typing.Optional[str]

### TimestampOffsetMode
- **Type**: typing.Optional[typing.Literal['USE_CONFIGURED_OFFSET', 'USE_EVENT_START_DATE']]


# MsSmoothOutputSettingsTypeDef

### H265PackagingType
- **Type**: typing.Optional[typing.Literal['HEV1', 'HVC1']]

### NameModifier
- **Type**: typing.Optional[str]


# MulticastInputSettingsTypeDef

### SourceIpAddress
- **Type**: typing.Optional[str]


# MulticastSettingsCreateRequestTypeDef

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.MulticastSourceCreateRequestTypeDef]]


# MulticastSettingsTypeDef

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.MulticastSourceTypeDef]]


# MulticastSettingsUpdateRequestTypeDef

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.MulticastSourceUpdateRequestTypeDef]]


# MulticastSourceCreateRequestTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIp
- **Type**: typing.Optional[str]


# MulticastSourceTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIp
- **Type**: typing.Optional[str]


# MulticastSourceUpdateRequestTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIp
- **Type**: typing.Optional[str]


# MultiplexContainerSettingsTypeDef

### MultiplexM2tsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexM2tsSettingsTypeDef]


# MultiplexM2tsSettingsTypeDef

### AbsentInputAudioBehavior
- **Type**: typing.Optional[typing.Literal['DROP', 'ENCODE_SILENCE']]

### Arib
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AudioBufferModel
- **Type**: typing.Optional[typing.Literal['ATSC', 'DVB']]

### AudioFramesPerPes
- **Type**: typing.Optional[int]

### AudioStreamType
- **Type**: typing.Optional[typing.Literal['ATSC', 'DVB']]

### CcDescriptor
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Ebif
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### EsRateInPes
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### Klv
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### NielsenId3Behavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### PcrControl
- **Type**: typing.Optional[typing.Literal['CONFIGURED_PCR_PERIOD', 'PCR_EVERY_PES_PACKET']]

### PcrPeriod
- **Type**: typing.Optional[int]

### Scte35Control
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### Scte35PrerollPullupMilliseconds
- **Type**: typing.Optional[float]


# MultiplexMediaConnectOutputDestinationSettingsTypeDef

### EntitlementArn
- **Type**: typing.Optional[str]


# MultiplexOutputDestinationTypeDef

### MediaConnectSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexMediaConnectOutputDestinationSettingsTypeDef]


# MultiplexOutputSettingsTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes

### ContainerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexContainerSettingsTypeDef]


# MultiplexProgramChannelDestinationSettingsTypeDef

### MultiplexId
- **Type**: typing.Optional[str]

### ProgramName
- **Type**: typing.Optional[str]


# MultiplexProgramPacketIdentifiersMapOutputTypeDef

### AudioPids
- **Type**: typing.Optional[typing.List[int]]

### DvbSubPids
- **Type**: typing.Optional[typing.List[int]]

### DvbTeletextPid
- **Type**: typing.Optional[int]

### EtvPlatformPid
- **Type**: typing.Optional[int]

### EtvSignalPid
- **Type**: typing.Optional[int]

### KlvDataPids
- **Type**: typing.Optional[typing.List[int]]

### PcrPid
- **Type**: typing.Optional[int]

### PmtPid
- **Type**: typing.Optional[int]

### PrivateMetadataPid
- **Type**: typing.Optional[int]

### Scte27Pids
- **Type**: typing.Optional[typing.List[int]]

### Scte35Pid
- **Type**: typing.Optional[int]

### TimedMetadataPid
- **Type**: typing.Optional[int]

### VideoPid
- **Type**: typing.Optional[int]

### AribCaptionsPid
- **Type**: typing.Optional[int]

### DvbTeletextPids
- **Type**: typing.Optional[typing.List[int]]

### EcmPid
- **Type**: typing.Optional[int]

### Smpte2038Pid
- **Type**: typing.Optional[int]


# MultiplexProgramPacketIdentifiersMapTypeDef

### AudioPids
- **Type**: typing.Optional[typing.Sequence[int]]

### DvbSubPids
- **Type**: typing.Optional[typing.Sequence[int]]

### DvbTeletextPid
- **Type**: typing.Optional[int]

### EtvPlatformPid
- **Type**: typing.Optional[int]

### EtvSignalPid
- **Type**: typing.Optional[int]

### KlvDataPids
- **Type**: typing.Optional[typing.Sequence[int]]

### PcrPid
- **Type**: typing.Optional[int]

### PmtPid
- **Type**: typing.Optional[int]

### PrivateMetadataPid
- **Type**: typing.Optional[int]

### Scte27Pids
- **Type**: typing.Optional[typing.Sequence[int]]

### Scte35Pid
- **Type**: typing.Optional[int]

### TimedMetadataPid
- **Type**: typing.Optional[int]

### VideoPid
- **Type**: typing.Optional[int]

### AribCaptionsPid
- **Type**: typing.Optional[int]

### DvbTeletextPids
- **Type**: typing.Optional[typing.Sequence[int]]

### EcmPid
- **Type**: typing.Optional[int]

### Smpte2038Pid
- **Type**: typing.Optional[int]


# MultiplexProgramPacketIdentifiersMapUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MultiplexProgramPipelineDetailTypeDef

### ActiveChannelPipeline
- **Type**: typing.Optional[str]

### PipelineId
- **Type**: typing.Optional[str]


# MultiplexProgramServiceDescriptorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MultiplexProgramSettingsTypeDef

### ProgramNumber
- **Type**: <class 'int'>
- **Required**: Yes

### PreferredChannelPipeline
- **Type**: typing.Optional[typing.Literal['CURRENTLY_ACTIVE', 'PIPELINE_0', 'PIPELINE_1']]

### ServiceDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramServiceDescriptorTypeDef]

### VideoSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexVideoSettingsTypeDef]


# MultiplexProgramSummaryTypeDef

### ChannelId
- **Type**: typing.Optional[str]

### ProgramName
- **Type**: typing.Optional[str]


# MultiplexProgramTypeDef

### ChannelId
- **Type**: typing.Optional[str]

### MultiplexProgramSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramSettingsTypeDef]

### PacketIdentifiersMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramPacketIdentifiersMapOutputTypeDef]

### PipelineDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramPipelineDetailTypeDef]]

### ProgramName
- **Type**: typing.Optional[str]


# MultiplexSettingsSummaryTypeDef

### TransportStreamBitrate
- **Type**: typing.Optional[int]


# MultiplexSettingsTypeDef

### TransportStreamBitrate
- **Type**: <class 'int'>
- **Required**: Yes

### TransportStreamId
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumVideoBufferDelayMilliseconds
- **Type**: typing.Optional[int]

### TransportStreamReservedBitrate
- **Type**: typing.Optional[int]


# MultiplexStatmuxVideoSettingsTypeDef

### MaximumBitrate
- **Type**: typing.Optional[int]

### MinimumBitrate
- **Type**: typing.Optional[int]

### Priority
- **Type**: typing.Optional[int]


# MultiplexSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### Id
- **Type**: typing.Optional[str]

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexSettingsSummaryTypeDef]

### Name
- **Type**: typing.Optional[str]

### PipelinesRunningCount
- **Type**: typing.Optional[int]

### ProgramCount
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# MultiplexTypeDef

### Arn
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.MultiplexOutputDestinationTypeDef]]

### Id
- **Type**: typing.Optional[str]

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexSettingsTypeDef]

### Name
- **Type**: typing.Optional[str]

### PipelinesRunningCount
- **Type**: typing.Optional[int]

### ProgramCount
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# MultiplexVideoSettingsTypeDef

### ConstantBitrate
- **Type**: typing.Optional[int]

### StatmuxSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexStatmuxVideoSettingsTypeDef]


# NetworkInputSettingsTypeDef

### HlsInputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsInputSettingsTypeDef]

### ServerValidation
- **Type**: typing.Optional[typing.Literal['CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME', 'CHECK_CRYPTOGRAPHY_ONLY']]

### MulticastInputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MulticastInputSettingsTypeDef]


# NielsenCBETTypeDef

### CbetCheckDigitString
- **Type**: <class 'str'>
- **Required**: Yes

### CbetStepaside
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### Csid
- **Type**: <class 'str'>
- **Required**: Yes


# NielsenConfigurationTypeDef

### DistributorId
- **Type**: typing.Optional[str]

### NielsenPcmToId3Tagging
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# NielsenNaesIiNwTypeDef

### CheckDigitString
- **Type**: <class 'str'>
- **Required**: Yes

### Sid
- **Type**: <class 'float'>
- **Required**: Yes

### Timezone
- **Type**: typing.Optional[typing.Literal['AMERICA_PUERTO_RICO', 'US_ALASKA', 'US_ARIZONA', 'US_CENTRAL', 'US_EASTERN', 'US_HAWAII', 'US_MOUNTAIN', 'US_PACIFIC', 'US_SAMOA', 'UTC']]


# NielsenWatermarksSettingsTypeDef

### NielsenCbetSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.NielsenCBETTypeDef]

### NielsenDistributionType
- **Type**: typing.Optional[typing.Literal['FINAL_DISTRIBUTOR', 'PROGRAM_CONTENT']]

### NielsenNaesIiNwSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.NielsenNaesIiNwTypeDef]


# NodeInterfaceMappingCreateRequestTypeDef

### LogicalInterfaceName
- **Type**: typing.Optional[str]

### NetworkInterfaceMode
- **Type**: typing.Optional[typing.Literal['BRIDGE', 'NAT']]

### PhysicalInterfaceName
- **Type**: typing.Optional[str]


# NodeInterfaceMappingTypeDef

### LogicalInterfaceName
- **Type**: typing.Optional[str]

### NetworkInterfaceMode
- **Type**: typing.Optional[typing.Literal['BRIDGE', 'NAT']]

### PhysicalInterfaceName
- **Type**: typing.Optional[str]


# OfferingTypeDef

### Arn
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[int]

### DurationUnits
- **Type**: typing.Optional[typing.Literal['MONTHS']]

### FixedPrice
- **Type**: typing.Optional[float]

### OfferingDescription
- **Type**: typing.Optional[str]

### OfferingId
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[typing.Literal['NO_UPFRONT']]

### Region
- **Type**: typing.Optional[str]

### ResourceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ReservationResourceSpecificationTypeDef]

### UsagePrice
- **Type**: typing.Optional[float]


# OutputDestinationOutputTypeDef

### Id
- **Type**: typing.Optional[str]

### MediaPackageSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.MediaPackageOutputDestinationSettingsTypeDef]]

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramChannelDestinationSettingsTypeDef]

### Settings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationSettingsTypeDef]]

### SrtSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.SrtOutputDestinationSettingsTypeDef]]


# OutputDestinationSettingsTypeDef

### PasswordParam
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# OutputDestinationTypeDef

### Id
- **Type**: typing.Optional[str]

### MediaPackageSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.MediaPackageOutputDestinationSettingsTypeDef]]

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramChannelDestinationSettingsTypeDef]

### Settings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationSettingsTypeDef]]

### SrtSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.SrtOutputDestinationSettingsTypeDef]]


# OutputDestinationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OutputGroupOutputTypeDef

### OutputGroupSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputGroupSettingsOutputTypeDef'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ExtraTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# OutputGroupSettingsOutputTypeDef

### ArchiveGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ArchiveGroupSettingsTypeDef]

### FrameCaptureGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FrameCaptureGroupSettingsTypeDef]

### HlsGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsGroupSettingsOutputTypeDef]

### MediaPackageGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MediaPackageGroupSettingsTypeDef]

### MsSmoothGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MsSmoothGroupSettingsTypeDef]

### MultiplexGroupSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### RtmpGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.RtmpGroupSettingsOutputTypeDef]

### UdpGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.UdpGroupSettingsTypeDef]

### CmafIngestGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CmafIngestGroupSettingsTypeDef]

### SrtGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.SrtGroupSettingsTypeDef]


# OutputGroupSettingsTypeDef

### ArchiveGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ArchiveGroupSettingsTypeDef]

### FrameCaptureGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FrameCaptureGroupSettingsTypeDef]

### HlsGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsGroupSettingsTypeDef]

### MediaPackageGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MediaPackageGroupSettingsTypeDef]

### MsSmoothGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MsSmoothGroupSettingsTypeDef]

### MultiplexGroupSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### RtmpGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.RtmpGroupSettingsTypeDef]

### UdpGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.UdpGroupSettingsTypeDef]

### CmafIngestGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CmafIngestGroupSettingsTypeDef]

### SrtGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.SrtGroupSettingsTypeDef]


# OutputGroupTypeDef

### OutputGroupSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputGroupSettingsTypeDef'>
- **Required**: Yes

### Outputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.OutputTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# OutputLocationRefTypeDef

### DestinationRefId
- **Type**: typing.Optional[str]


# OutputLockingSettingsOutputTypeDef

### EpochLockingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EpochLockingSettingsTypeDef]

### PipelineLockingSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# OutputLockingSettingsTypeDef

### EpochLockingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EpochLockingSettingsTypeDef]

### PipelineLockingSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# OutputSettingsOutputTypeDef

### ArchiveOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ArchiveOutputSettingsOutputTypeDef]

### FrameCaptureOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FrameCaptureOutputSettingsTypeDef]

### HlsOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsOutputSettingsOutputTypeDef]

### MediaPackageOutputSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### MsSmoothOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MsSmoothOutputSettingsTypeDef]

### MultiplexOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexOutputSettingsTypeDef]

### RtmpOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.RtmpOutputSettingsTypeDef]

### UdpOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.UdpOutputSettingsTypeDef]

### CmafIngestOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CmafIngestOutputSettingsTypeDef]

### SrtOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.SrtOutputSettingsTypeDef]


# OutputSettingsTypeDef

### ArchiveOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ArchiveOutputSettingsTypeDef]

### FrameCaptureOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FrameCaptureOutputSettingsTypeDef]

### HlsOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsOutputSettingsTypeDef]

### MediaPackageOutputSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### MsSmoothOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MsSmoothOutputSettingsTypeDef]

### MultiplexOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexOutputSettingsTypeDef]

### RtmpOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.RtmpOutputSettingsTypeDef]

### UdpOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.UdpOutputSettingsTypeDef]

### CmafIngestOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CmafIngestOutputSettingsTypeDef]

### SrtOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.SrtOutputSettingsTypeDef]


# OutputTypeDef

### OutputSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputSettingsTypeDef'>
- **Required**: Yes

### AudioDescriptionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### CaptionDescriptionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### OutputName
- **Type**: typing.Optional[str]

### VideoDescriptionName
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PauseStateScheduleActionSettingsOutputTypeDef

### Pipelines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.PipelinePauseStateSettingsTypeDef]]


# PauseStateScheduleActionSettingsTypeDef

### Pipelines
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.PipelinePauseStateSettingsTypeDef]]


# PauseStateScheduleActionSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineDetailTypeDef

### ActiveInputAttachmentName
- **Type**: typing.Optional[str]

### ActiveInputSwitchActionName
- **Type**: typing.Optional[str]

### ActiveMotionGraphicsActionName
- **Type**: typing.Optional[str]

### ActiveMotionGraphicsUri
- **Type**: typing.Optional[str]

### PipelineId
- **Type**: typing.Optional[str]

### ChannelEngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionResponseTypeDef]


# PipelinePauseStateSettingsTypeDef

### PipelineId
- **Type**: typing.Literal['PIPELINE_0', 'PIPELINE_1']
- **Required**: Yes


# PurchaseOfferingRequestTypeDef

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### OfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### RenewalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.RenewalSettingsTypeDef]

### RequestId
- **Type**: typing.Optional[str]

### Start
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PurchaseOfferingResponseTypeDef

### Reservation
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ReservationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RebootInputDeviceRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]


# RejectInputDeviceTransferRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# RemixSettingsOutputTypeDef

### ChannelMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.AudioChannelMappingOutputTypeDef]
- **Required**: Yes

### ChannelsIn
- **Type**: typing.Optional[int]

### ChannelsOut
- **Type**: typing.Optional[int]


# RemixSettingsTypeDef

### ChannelMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.AudioChannelMappingTypeDef]
- **Required**: Yes

### ChannelsIn
- **Type**: typing.Optional[int]

### ChannelsOut
- **Type**: typing.Optional[int]


# RenewalSettingsTypeDef

### AutomaticRenewal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'UNAVAILABLE']]

### RenewalCount
- **Type**: typing.Optional[int]


# ReservationResourceSpecificationTypeDef

### ChannelClass
- **Type**: typing.Optional[typing.Literal['SINGLE_PIPELINE', 'STANDARD']]

### Codec
- **Type**: typing.Optional[typing.Literal['AUDIO', 'AV1', 'AVC', 'HEVC', 'LINK', 'MPEG2']]

### MaximumBitrate
- **Type**: typing.Optional[typing.Literal['MAX_10_MBPS', 'MAX_20_MBPS', 'MAX_50_MBPS']]

### MaximumFramerate
- **Type**: typing.Optional[typing.Literal['MAX_30_FPS', 'MAX_60_FPS']]

### Resolution
- **Type**: typing.Optional[typing.Literal['FHD', 'HD', 'SD', 'UHD']]

### ResourceType
- **Type**: typing.Optional[typing.Literal['CHANNEL', 'INPUT', 'MULTIPLEX', 'OUTPUT']]

### SpecialFeature
- **Type**: typing.Optional[typing.Literal['ADVANCED_AUDIO', 'AUDIO_NORMALIZATION', 'MGHD', 'MGUHD']]

### VideoQuality
- **Type**: typing.Optional[typing.Literal['ENHANCED', 'PREMIUM', 'STANDARD']]


# ReservationTypeDef

### Arn
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]

### CurrencyCode
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[int]

### DurationUnits
- **Type**: typing.Optional[typing.Literal['MONTHS']]

### End
- **Type**: typing.Optional[str]

### FixedPrice
- **Type**: typing.Optional[float]

### Name
- **Type**: typing.Optional[str]

### OfferingDescription
- **Type**: typing.Optional[str]

### OfferingId
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[typing.Literal['NO_UPFRONT']]

### Region
- **Type**: typing.Optional[str]

### RenewalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.RenewalSettingsTypeDef]

### ReservationId
- **Type**: typing.Optional[str]

### ResourceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ReservationResourceSpecificationTypeDef]

### Start
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELED', 'DELETED', 'EXPIRED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### UsagePrice
- **Type**: typing.Optional[float]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# RestartChannelPipelinesRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineIds
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PIPELINE_0', 'PIPELINE_1']]]


# RestartChannelPipelinesResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef'>
- **Required**: Yes

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationOutputTypeDef]
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ChannelEgressEndpointTypeDef]
- **Required**: Yes

### EncoderSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.EncoderSettingsOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentOutputTypeDef]
- **Required**: Yes

### InputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputSpecificationTypeDef'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes

### Maintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MaintenanceStatusTypeDef'>
- **Required**: Yes

### MaintenanceStatus
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.PipelineDetailTypeDef]
- **Required**: Yes

### PipelinesRunningCount
- **Type**: <class 'int'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Vpc
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.VpcOutputSettingsDescriptionTypeDef'>
- **Required**: Yes

### AnywhereSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.DescribeAnywhereSettingsTypeDef'>
- **Required**: Yes

### ChannelEngineVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RouteCreateRequestTypeDef

### Cidr
- **Type**: typing.Optional[str]

### Gateway
- **Type**: typing.Optional[str]


# RouteTypeDef

### Cidr
- **Type**: typing.Optional[str]

### Gateway
- **Type**: typing.Optional[str]


# RouteUpdateRequestTypeDef

### Cidr
- **Type**: typing.Optional[str]

### Gateway
- **Type**: typing.Optional[str]


# RtmpGroupSettingsOutputTypeDef

### AdMarkers
- **Type**: typing.Optional[typing.List[typing.Literal['ON_CUE_POINT_SCTE35']]]

### AuthenticationScheme
- **Type**: typing.Optional[typing.Literal['AKAMAI', 'COMMON']]

### CacheFullBehavior
- **Type**: typing.Optional[typing.Literal['DISCONNECT_IMMEDIATELY', 'WAIT_FOR_SERVER']]

### CacheLength
- **Type**: typing.Optional[int]

### CaptionData
- **Type**: typing.Optional[typing.Literal['ALL', 'FIELD1_608', 'FIELD1_AND_FIELD2_608']]

### InputLossAction
- **Type**: typing.Optional[typing.Literal['EMIT_OUTPUT', 'PAUSE_OUTPUT']]

### RestartDelay
- **Type**: typing.Optional[int]

### IncludeFillerNalUnits
- **Type**: typing.Optional[typing.Literal['AUTO', 'DROP', 'INCLUDE']]


# RtmpGroupSettingsTypeDef

### AdMarkers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ON_CUE_POINT_SCTE35']]]

### AuthenticationScheme
- **Type**: typing.Optional[typing.Literal['AKAMAI', 'COMMON']]

### CacheFullBehavior
- **Type**: typing.Optional[typing.Literal['DISCONNECT_IMMEDIATELY', 'WAIT_FOR_SERVER']]

### CacheLength
- **Type**: typing.Optional[int]

### CaptionData
- **Type**: typing.Optional[typing.Literal['ALL', 'FIELD1_608', 'FIELD1_AND_FIELD2_608']]

### InputLossAction
- **Type**: typing.Optional[typing.Literal['EMIT_OUTPUT', 'PAUSE_OUTPUT']]

### RestartDelay
- **Type**: typing.Optional[int]

### IncludeFillerNalUnits
- **Type**: typing.Optional[typing.Literal['AUTO', 'DROP', 'INCLUDE']]


# RtmpOutputSettingsTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes

### CertificateMode
- **Type**: typing.Optional[typing.Literal['SELF_SIGNED', 'VERIFY_AUTHENTICITY']]

### ConnectionRetryInterval
- **Type**: typing.Optional[int]

### NumRetries
- **Type**: typing.Optional[int]


# ScheduleActionOutputTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleActionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionSettingsOutputTypeDef'>
- **Required**: Yes

### ScheduleActionStartSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionStartSettingsOutputTypeDef'>
- **Required**: Yes


# ScheduleActionSettingsOutputTypeDef

### HlsId3SegmentTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsId3SegmentTaggingScheduleActionSettingsTypeDef]

### HlsTimedMetadataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsTimedMetadataScheduleActionSettingsTypeDef]

### InputPrepareSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputPrepareScheduleActionSettingsOutputTypeDef]

### InputSwitchSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSwitchScheduleActionSettingsOutputTypeDef]

### MotionGraphicsImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MotionGraphicsActivateScheduleActionSettingsTypeDef]

### MotionGraphicsImageDeactivateSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### PauseStateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PauseStateScheduleActionSettingsOutputTypeDef]

### Scte35InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35InputScheduleActionSettingsTypeDef]

### Scte35ReturnToNetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35ReturnToNetworkScheduleActionSettingsTypeDef]

### Scte35SpliceInsertSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35SpliceInsertScheduleActionSettingsTypeDef]

### Scte35TimeSignalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35TimeSignalScheduleActionSettingsOutputTypeDef]

### StaticImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageActivateScheduleActionSettingsTypeDef]

### StaticImageDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageDeactivateScheduleActionSettingsTypeDef]

### StaticImageOutputActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageOutputActivateScheduleActionSettingsOutputTypeDef]

### StaticImageOutputDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageOutputDeactivateScheduleActionSettingsOutputTypeDef]

### Id3SegmentTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Id3SegmentTaggingScheduleActionSettingsTypeDef]

### TimedMetadataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TimedMetadataScheduleActionSettingsTypeDef]


# ScheduleActionSettingsTypeDef

### HlsId3SegmentTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsId3SegmentTaggingScheduleActionSettingsTypeDef]

### HlsTimedMetadataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsTimedMetadataScheduleActionSettingsTypeDef]

### InputPrepareSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputPrepareScheduleActionSettingsUnionTypeDef]

### InputSwitchSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSwitchScheduleActionSettingsUnionTypeDef]

### MotionGraphicsImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MotionGraphicsActivateScheduleActionSettingsTypeDef]

### MotionGraphicsImageDeactivateSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### PauseStateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PauseStateScheduleActionSettingsUnionTypeDef]

### Scte35InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35InputScheduleActionSettingsTypeDef]

### Scte35ReturnToNetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35ReturnToNetworkScheduleActionSettingsTypeDef]

### Scte35SpliceInsertSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35SpliceInsertScheduleActionSettingsTypeDef]

### Scte35TimeSignalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35TimeSignalScheduleActionSettingsUnionTypeDef]

### StaticImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageActivateScheduleActionSettingsTypeDef]

### StaticImageDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageDeactivateScheduleActionSettingsTypeDef]

### StaticImageOutputActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageOutputActivateScheduleActionSettingsUnionTypeDef]

### StaticImageOutputDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageOutputDeactivateScheduleActionSettingsUnionTypeDef]

### Id3SegmentTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Id3SegmentTaggingScheduleActionSettingsTypeDef]

### TimedMetadataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.TimedMetadataScheduleActionSettingsTypeDef]


# ScheduleActionSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScheduleActionStartSettingsOutputTypeDef

### FixedModeScheduleActionStartSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FixedModeScheduleActionStartSettingsTypeDef]

### FollowModeScheduleActionStartSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FollowModeScheduleActionStartSettingsTypeDef]

### ImmediateModeScheduleActionStartSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ScheduleActionStartSettingsTypeDef

### FixedModeScheduleActionStartSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FixedModeScheduleActionStartSettingsTypeDef]

### FollowModeScheduleActionStartSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FollowModeScheduleActionStartSettingsTypeDef]

### ImmediateModeScheduleActionStartSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ScheduleActionStartSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScheduleActionTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleActionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionSettingsUnionTypeDef'>
- **Required**: Yes

### ScheduleActionStartSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionStartSettingsUnionTypeDef'>
- **Required**: Yes


# ScheduleActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Scte20SourceSettingsTypeDef

### Convert608To708
- **Type**: typing.Optional[typing.Literal['DISABLED', 'UPCONVERT']]

### Source608ChannelNumber
- **Type**: typing.Optional[int]


# Scte27SourceSettingsTypeDef

### OcrLanguage
- **Type**: typing.Optional[typing.Literal['DEU', 'ENG', 'FRA', 'NLD', 'POR', 'SPA']]

### Pid
- **Type**: typing.Optional[int]


# Scte35DeliveryRestrictionsTypeDef

### ArchiveAllowedFlag
- **Type**: typing.Literal['ARCHIVE_ALLOWED', 'ARCHIVE_NOT_ALLOWED']
- **Required**: Yes

### DeviceRestrictions
- **Type**: typing.Literal['NONE', 'RESTRICT_GROUP0', 'RESTRICT_GROUP1', 'RESTRICT_GROUP2']
- **Required**: Yes

### NoRegionalBlackoutFlag
- **Type**: typing.Literal['NO_REGIONAL_BLACKOUT', 'REGIONAL_BLACKOUT']
- **Required**: Yes

### WebDeliveryAllowedFlag
- **Type**: typing.Literal['WEB_DELIVERY_ALLOWED', 'WEB_DELIVERY_NOT_ALLOWED']
- **Required**: Yes


# Scte35DescriptorSettingsTypeDef

### SegmentationDescriptorScte35DescriptorSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.Scte35SegmentationDescriptorTypeDef'>
- **Required**: Yes


# Scte35DescriptorTypeDef

### Scte35DescriptorSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.Scte35DescriptorSettingsTypeDef'>
- **Required**: Yes


# Scte35InputScheduleActionSettingsTypeDef

### Mode
- **Type**: typing.Literal['FIXED', 'FOLLOW_ACTIVE']
- **Required**: Yes

### InputAttachmentNameReference
- **Type**: typing.Optional[str]


# Scte35ReturnToNetworkScheduleActionSettingsTypeDef

### SpliceEventId
- **Type**: <class 'int'>
- **Required**: Yes


# Scte35SegmentationDescriptorTypeDef

### SegmentationCancelIndicator
- **Type**: typing.Literal['SEGMENTATION_EVENT_CANCELED', 'SEGMENTATION_EVENT_NOT_CANCELED']
- **Required**: Yes

### SegmentationEventId
- **Type**: <class 'int'>
- **Required**: Yes

### DeliveryRestrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35DeliveryRestrictionsTypeDef]

### SegmentNum
- **Type**: typing.Optional[int]

### SegmentationDuration
- **Type**: typing.Optional[int]

### SegmentationTypeId
- **Type**: typing.Optional[int]

### SegmentationUpid
- **Type**: typing.Optional[str]

### SegmentationUpidType
- **Type**: typing.Optional[int]

### SegmentsExpected
- **Type**: typing.Optional[int]

### SubSegmentNum
- **Type**: typing.Optional[int]

### SubSegmentsExpected
- **Type**: typing.Optional[int]


# Scte35SpliceInsertScheduleActionSettingsTypeDef

### SpliceEventId
- **Type**: <class 'int'>
- **Required**: Yes

### Duration
- **Type**: typing.Optional[int]


# Scte35SpliceInsertTypeDef

### AdAvailOffset
- **Type**: typing.Optional[int]

### NoRegionalBlackoutFlag
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'IGNORE']]

### WebDeliveryAllowedFlag
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'IGNORE']]


# Scte35TimeSignalAposTypeDef

### AdAvailOffset
- **Type**: typing.Optional[int]

### NoRegionalBlackoutFlag
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'IGNORE']]

### WebDeliveryAllowedFlag
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'IGNORE']]


# Scte35TimeSignalScheduleActionSettingsOutputTypeDef

### Scte35Descriptors
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.Scte35DescriptorTypeDef]
- **Required**: Yes


# Scte35TimeSignalScheduleActionSettingsTypeDef

### Scte35Descriptors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.Scte35DescriptorTypeDef]
- **Required**: Yes


# Scte35TimeSignalScheduleActionSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignalMapSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MonitorDeploymentStatus
- **Type**: typing.Literal['DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DEPLOYMENT_COMPLETE', 'DEPLOYMENT_FAILED', 'DEPLOYMENT_IN_PROGRESS', 'DRY_RUN_DEPLOYMENT_COMPLETE', 'DRY_RUN_DEPLOYMENT_FAILED', 'DRY_RUN_DEPLOYMENT_IN_PROGRESS', 'NOT_DEPLOYED']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'NOT_READY', 'READY', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_REVERTED']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SrtCallerDecryptionRequestTypeDef

### Algorithm
- **Type**: typing.Optional[typing.Literal['AES128', 'AES192', 'AES256']]

### PassphraseSecretArn
- **Type**: typing.Optional[str]


# SrtCallerDecryptionTypeDef

### Algorithm
- **Type**: typing.Optional[typing.Literal['AES128', 'AES192', 'AES256']]

### PassphraseSecretArn
- **Type**: typing.Optional[str]


# SrtCallerSourceRequestTypeDef

### Decryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.SrtCallerDecryptionRequestTypeDef]

### MinimumLatency
- **Type**: typing.Optional[int]

### SrtListenerAddress
- **Type**: typing.Optional[str]

### SrtListenerPort
- **Type**: typing.Optional[str]

### StreamId
- **Type**: typing.Optional[str]


# SrtCallerSourceTypeDef

### Decryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.SrtCallerDecryptionTypeDef]

### MinimumLatency
- **Type**: typing.Optional[int]

### SrtListenerAddress
- **Type**: typing.Optional[str]

### SrtListenerPort
- **Type**: typing.Optional[str]

### StreamId
- **Type**: typing.Optional[str]


# SrtGroupSettingsTypeDef

### InputLossAction
- **Type**: typing.Optional[typing.Literal['DROP_PROGRAM', 'DROP_TS', 'EMIT_PROGRAM']]


# SrtOutputDestinationSettingsTypeDef

### EncryptionPassphraseSecretArn
- **Type**: typing.Optional[str]

### StreamId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# SrtOutputSettingsTypeDef

### ContainerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.UdpContainerSettingsTypeDef'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes

### BufferMsec
- **Type**: typing.Optional[int]

### EncryptionType
- **Type**: typing.Optional[typing.Literal['AES128', 'AES192', 'AES256']]

### Latency
- **Type**: typing.Optional[int]


# SrtSettingsRequestTypeDef

### SrtCallerSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.SrtCallerSourceRequestTypeDef]]


# SrtSettingsTypeDef

### SrtCallerSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.SrtCallerSourceTypeDef]]


# StandardHlsSettingsTypeDef

### M3u8Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.M3u8SettingsTypeDef'>
- **Required**: Yes

### AudioRenditionSets
- **Type**: typing.Optional[str]


# StartChannelRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# StartChannelResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef'>
- **Required**: Yes

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationOutputTypeDef]
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ChannelEgressEndpointTypeDef]
- **Required**: Yes

### EncoderSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.EncoderSettingsOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentOutputTypeDef]
- **Required**: Yes

### InputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputSpecificationTypeDef'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes

### Maintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MaintenanceStatusTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.PipelineDetailTypeDef]
- **Required**: Yes

### PipelinesRunningCount
- **Type**: <class 'int'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Vpc
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.VpcOutputSettingsDescriptionTypeDef'>
- **Required**: Yes

### AnywhereSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.DescribeAnywhereSettingsTypeDef'>
- **Required**: Yes

### ChannelEngineVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDeleteMonitorDeploymentRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartDeleteMonitorDeploymentResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchAlarmTemplateGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DiscoveryEntryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### EventBridgeRuleTemplateGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### FailedMediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive_classes.MediaResourceTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastDiscoveredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSuccessfulMonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.SuccessfulMonitorDeploymentTypeDef'>
- **Required**: Yes

### MediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive_classes.MediaResourceTypeDef]
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitorChangesPendingDeployment
- **Type**: <class 'bool'>
- **Required**: Yes

### MonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MonitorDeploymentTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'NOT_READY', 'READY', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_REVERTED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartInputDeviceMaintenanceWindowRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# StartInputDeviceRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# StartMonitorDeploymentRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# StartMonitorDeploymentResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchAlarmTemplateGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DiscoveryEntryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### EventBridgeRuleTemplateGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### FailedMediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive_classes.MediaResourceTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastDiscoveredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSuccessfulMonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.SuccessfulMonitorDeploymentTypeDef'>
- **Required**: Yes

### MediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive_classes.MediaResourceTypeDef]
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitorChangesPendingDeployment
- **Type**: <class 'bool'>
- **Required**: Yes

### MonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MonitorDeploymentTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'NOT_READY', 'READY', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_REVERTED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMultiplexRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes


# StartMultiplexResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.MultiplexOutputDestinationTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexSettingsTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelinesRunningCount
- **Type**: <class 'int'>
- **Required**: Yes

### ProgramCount
- **Type**: <class 'int'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTimecodeTypeDef

### Timecode
- **Type**: typing.Optional[str]


# StartUpdateSignalMapRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchAlarmTemplateGroupIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### Description
- **Type**: typing.Optional[str]

### DiscoveryEntryPointArn
- **Type**: typing.Optional[str]

### EventBridgeRuleTemplateGroupIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### ForceRediscovery
- **Type**: typing.Optional[bool]

### Name
- **Type**: typing.Optional[str]


# StartUpdateSignalMapResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchAlarmTemplateGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DiscoveryEntryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### EventBridgeRuleTemplateGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### FailedMediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive_classes.MediaResourceTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastDiscoveredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSuccessfulMonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.SuccessfulMonitorDeploymentTypeDef'>
- **Required**: Yes

### MediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive_classes.MediaResourceTypeDef]
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitorChangesPendingDeployment
- **Type**: <class 'bool'>
- **Required**: Yes

### MonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MonitorDeploymentTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'NOT_READY', 'READY', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_REVERTED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StaticImageActivateScheduleActionSettingsTypeDef

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef'>
- **Required**: Yes

### Duration
- **Type**: typing.Optional[int]

### FadeIn
- **Type**: typing.Optional[int]

### FadeOut
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### ImageX
- **Type**: typing.Optional[int]

### ImageY
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]

### Opacity
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# StaticImageDeactivateScheduleActionSettingsTypeDef

### FadeOut
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]


# StaticImageOutputActivateScheduleActionSettingsOutputTypeDef

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef'>
- **Required**: Yes

### OutputNames
- **Type**: typing.List[str]
- **Required**: Yes

### Duration
- **Type**: typing.Optional[int]

### FadeIn
- **Type**: typing.Optional[int]

### FadeOut
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### ImageX
- **Type**: typing.Optional[int]

### ImageY
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]

### Opacity
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# StaticImageOutputActivateScheduleActionSettingsTypeDef

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef'>
- **Required**: Yes

### OutputNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Duration
- **Type**: typing.Optional[int]

### FadeIn
- **Type**: typing.Optional[int]

### FadeOut
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### ImageX
- **Type**: typing.Optional[int]

### ImageY
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]

### Opacity
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# StaticImageOutputActivateScheduleActionSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StaticImageOutputDeactivateScheduleActionSettingsOutputTypeDef

### OutputNames
- **Type**: typing.List[str]
- **Required**: Yes

### FadeOut
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]


# StaticImageOutputDeactivateScheduleActionSettingsTypeDef

### OutputNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FadeOut
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]


# StaticImageOutputDeactivateScheduleActionSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StaticKeySettingsTypeDef

### StaticKeyValue
- **Type**: <class 'str'>
- **Required**: Yes

### KeyProviderServer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef]


# StopChannelRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# StopChannelResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef'>
- **Required**: Yes

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationOutputTypeDef]
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ChannelEgressEndpointTypeDef]
- **Required**: Yes

### EncoderSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.EncoderSettingsOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentOutputTypeDef]
- **Required**: Yes

### InputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputSpecificationTypeDef'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes

### Maintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MaintenanceStatusTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.PipelineDetailTypeDef]
- **Required**: Yes

### PipelinesRunningCount
- **Type**: <class 'int'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Vpc
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.VpcOutputSettingsDescriptionTypeDef'>
- **Required**: Yes

### AnywhereSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.DescribeAnywhereSettingsTypeDef'>
- **Required**: Yes

### ChannelEngineVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopInputDeviceRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# StopMultiplexRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes


# StopMultiplexResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.MultiplexOutputDestinationTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexSettingsTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelinesRunningCount
- **Type**: <class 'int'>
- **Required**: Yes

### ProgramCount
- **Type**: <class 'int'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopTimecodeTypeDef

### LastFrameClippingBehavior
- **Type**: typing.Optional[typing.Literal['EXCLUDE_LAST_FRAME', 'INCLUDE_LAST_FRAME']]

### Timecode
- **Type**: typing.Optional[str]


# SuccessfulMonitorDeploymentTypeDef

### DetailsUri
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DEPLOYMENT_COMPLETE', 'DEPLOYMENT_FAILED', 'DEPLOYMENT_IN_PROGRESS', 'DRY_RUN_DEPLOYMENT_COMPLETE', 'DRY_RUN_DEPLOYMENT_FAILED', 'DRY_RUN_DEPLOYMENT_IN_PROGRESS', 'NOT_DEPLOYED']
- **Required**: Yes


# TeletextSourceSettingsTypeDef

### OutputRectangle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CaptionRectangleTypeDef]

### PageNumber
- **Type**: typing.Optional[str]


# TemporalFilterSettingsTypeDef

### PostFilterSharpening
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'ENABLED']]

### Strength
- **Type**: typing.Optional[typing.Literal['AUTO', 'STRENGTH_1', 'STRENGTH_10', 'STRENGTH_11', 'STRENGTH_12', 'STRENGTH_13', 'STRENGTH_14', 'STRENGTH_15', 'STRENGTH_16', 'STRENGTH_2', 'STRENGTH_3', 'STRENGTH_4', 'STRENGTH_5', 'STRENGTH_6', 'STRENGTH_7', 'STRENGTH_8', 'STRENGTH_9']]


# ThumbnailConfigurationTypeDef

### State
- **Type**: typing.Literal['AUTO', 'DISABLED']
- **Required**: Yes


# ThumbnailDetailTypeDef

### PipelineId
- **Type**: typing.Optional[str]

### Thumbnails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.ThumbnailTypeDef]]


# ThumbnailTypeDef

### Body
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### ThumbnailType
- **Type**: typing.Optional[typing.Literal['CURRENT_ACTIVE', 'UNSPECIFIED']]

### TimeStamp
- **Type**: typing.Optional[datetime.datetime]


# TimecodeBurninSettingsTypeDef

### FontSize
- **Type**: typing.Literal['EXTRA_SMALL_10', 'LARGE_48', 'MEDIUM_32', 'SMALL_16']
- **Required**: Yes

### Position
- **Type**: typing.Literal['BOTTOM_CENTER', 'BOTTOM_LEFT', 'BOTTOM_RIGHT', 'MIDDLE_CENTER', 'MIDDLE_LEFT', 'MIDDLE_RIGHT', 'TOP_CENTER', 'TOP_LEFT', 'TOP_RIGHT']
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# TimecodeConfigTypeDef

### Source
- **Type**: typing.Literal['EMBEDDED', 'SYSTEMCLOCK', 'ZEROBASED']
- **Required**: Yes

### SyncThreshold
- **Type**: typing.Optional[int]


# TimedMetadataScheduleActionSettingsTypeDef

### Id3
- **Type**: <class 'str'>
- **Required**: Yes


# TransferInputDeviceRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetCustomerId
- **Type**: typing.Optional[str]

### TargetRegion
- **Type**: typing.Optional[str]

### TransferMessage
- **Type**: typing.Optional[str]


# TransferringInputDeviceSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### TargetCustomerId
- **Type**: typing.Optional[str]

### TransferType
- **Type**: typing.Optional[typing.Literal['INCOMING', 'OUTGOING']]


# TtmlDestinationSettingsTypeDef

### StyleControl
- **Type**: typing.Optional[typing.Literal['PASSTHROUGH', 'USE_CONFIGURED']]


# UdpContainerSettingsTypeDef

### M2tsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.M2tsSettingsTypeDef]


# UdpGroupSettingsTypeDef

### InputLossAction
- **Type**: typing.Optional[typing.Literal['DROP_PROGRAM', 'DROP_TS', 'EMIT_PROGRAM']]

### TimedMetadataId3Frame
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIV', 'TDRL']]

### TimedMetadataId3Period
- **Type**: typing.Optional[int]


# UdpOutputSettingsTypeDef

### ContainerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.UdpContainerSettingsTypeDef'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputLocationRefTypeDef'>
- **Required**: Yes

### BufferMsec
- **Type**: typing.Optional[int]

### FecOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FecOutputSettingsTypeDef]


# UpdateAccountConfigurationRequestTypeDef

### AccountConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AccountConfigurationTypeDef]


# UpdateAccountConfigurationResponseTypeDef

### AccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.AccountConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelClassRequestTypeDef

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationUnionTypeDef]]


# UpdateChannelClassResponseTypeDef

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelPlacementGroupRequestTypeDef

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Nodes
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateChannelPlacementGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Channels
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Nodes
- **Type**: typing.List[str]
- **Required**: Yes

### State
- **Type**: typing.Literal['ASSIGNED', 'ASSIGNING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UNASSIGNED', 'UNASSIGNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef]

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationUnionTypeDef]]

### EncoderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EncoderSettingsUnionTypeDef]

### InputAttachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentUnionTypeDef]]

### InputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSpecificationTypeDef]

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MaintenanceUpdateSettingsTypeDef]

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ChannelEngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ChannelEngineVersionRequestTypeDef]

### DryRun
- **Type**: typing.Optional[bool]


# UpdateChannelResponseTypeDef

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCloudWatchAlarmTemplateGroupRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateCloudWatchAlarmTemplateGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCloudWatchAlarmTemplateRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']]

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### EvaluationPeriods
- **Type**: typing.Optional[int]

### GroupIdentifier
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### TargetResourceType
- **Type**: typing.Optional[typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'MEDIATAILOR_PLAYBACK_CONFIGURATION', 'S3_BUCKET']]

### Threshold
- **Type**: typing.Optional[float]

### TreatMissingData
- **Type**: typing.Optional[typing.Literal['breaching', 'ignore', 'missing', 'notBreaching']]


# UpdateCloudWatchAlarmTemplateResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DatapointsToAlarm
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationPeriods
- **Type**: <class 'int'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TargetResourceType
- **Type**: typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'MEDIATAILOR_PLAYBACK_CONFIGURATION', 'S3_BUCKET']
- **Required**: Yes

### Threshold
- **Type**: <class 'float'>
- **Required**: Yes

### TreatMissingData
- **Type**: typing.Literal['breaching', 'ignore', 'missing', 'notBreaching']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### NetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ClusterNetworkSettingsUpdateRequestTypeDef]


# UpdateClusterResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelIds
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterType
- **Type**: typing.Literal['ON_PREMISES']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ClusterNetworkSettingsTypeDef'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEventBridgeRuleTemplateGroupRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateEventBridgeRuleTemplateGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEventBridgeRuleTemplateRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EventTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.EventBridgeRuleTemplateTargetTypeDef]]

### EventType
- **Type**: typing.Optional[typing.Literal['MEDIACONNECT_ALERT', 'MEDIACONNECT_FLOW_STATUS_CHANGE', 'MEDIACONNECT_OUTPUT_HEALTH', 'MEDIACONNECT_SOURCE_HEALTH', 'MEDIALIVE_CHANNEL_ALERT', 'MEDIALIVE_CHANNEL_INPUT_CHANGE', 'MEDIALIVE_CHANNEL_STATE_CHANGE', 'MEDIALIVE_MULTIPLEX_ALERT', 'MEDIALIVE_MULTIPLEX_STATE_CHANGE', 'MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION', 'MEDIAPACKAGE_INPUT_NOTIFICATION', 'MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION', 'SIGNAL_MAP_ACTIVE_ALARM']]

### GroupIdentifier
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# UpdateEventBridgeRuleTemplateResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EventTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.EventBridgeRuleTemplateTargetTypeDef]
- **Required**: Yes

### EventType
- **Type**: typing.Literal['MEDIACONNECT_ALERT', 'MEDIACONNECT_FLOW_STATUS_CHANGE', 'MEDIACONNECT_OUTPUT_HEALTH', 'MEDIACONNECT_SOURCE_HEALTH', 'MEDIALIVE_CHANNEL_ALERT', 'MEDIALIVE_CHANNEL_INPUT_CHANGE', 'MEDIALIVE_CHANNEL_STATE_CHANGE', 'MEDIALIVE_MULTIPLEX_ALERT', 'MEDIALIVE_MULTIPLEX_STATE_CHANGE', 'MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION', 'MEDIAPACKAGE_INPUT_NOTIFICATION', 'MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION', 'SIGNAL_MAP_ACTIVE_ALARM']
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInputDeviceRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### HdDeviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceConfigurableSettingsTypeDef]

### Name
- **Type**: typing.Optional[str]

### UhdDeviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceConfigurableSettingsTypeDef]

### AvailabilityZone
- **Type**: typing.Optional[str]


# UpdateInputRequestTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputDestinationRequestTypeDef]]

### InputDevices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceRequestTypeDef]]

### InputSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### MediaConnectFlows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.MediaConnectFlowRequestTypeDef]]

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputSourceRequestTypeDef]]

### SrtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.SrtSettingsRequestTypeDef]

### MulticastSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MulticastSettingsUpdateRequestTypeDef]


# UpdateInputResponseTypeDef

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInputSecurityGroupRequestTypeDef

### InputSecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### WhitelistRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputWhitelistRuleCidrTypeDef]]


# UpdateInputSecurityGroupResponseTypeDef

### SecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMultiplexProgramRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexProgramSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramSettingsTypeDef]


# UpdateMultiplexProgramResponseTypeDef

### MultiplexProgram
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMultiplexRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexSettingsTypeDef]

### Name
- **Type**: typing.Optional[str]

### PacketIdentifiersMapping
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramPacketIdentifiersMapUnionTypeDef]]


# UpdateMultiplexResponseTypeDef

### Multiplex
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNetworkRequestTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### IpPools
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.IpPoolUpdateRequestTypeDef]]

### Name
- **Type**: typing.Optional[str]

### Routes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.RouteUpdateRequestTypeDef]]


# UpdateNetworkResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedClusterIds
- **Type**: typing.List[str]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IpPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.IpPoolTypeDef]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.RouteTypeDef]
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'IDLE', 'IN_USE', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNodeRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'BACKUP']]


# UpdateNodeResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelPlacementGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['CONNECTED', 'DISCONNECTED']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NodeInterfaceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.NodeInterfaceMappingTypeDef]
- **Required**: Yes

### Role
- **Type**: typing.Literal['ACTIVE', 'BACKUP']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNodeStateRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAINING']]


# UpdateNodeStateResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelPlacementGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['CONNECTED', 'DISCONNECTED']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NodeInterfaceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.NodeInterfaceMappingTypeDef]
- **Required**: Yes

### Role
- **Type**: typing.Literal['ACTIVE', 'BACKUP']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReservationRequestTypeDef

### ReservationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### RenewalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.RenewalSettingsTypeDef]


# UpdateReservationResponseTypeDef

### Reservation
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ReservationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VideoBlackFailoverSettingsTypeDef

### BlackDetectThreshold
- **Type**: typing.Optional[float]

### VideoBlackThresholdMsec
- **Type**: typing.Optional[int]


# VideoCodecSettingsOutputTypeDef

### FrameCaptureSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FrameCaptureSettingsTypeDef]

### H264Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H264SettingsOutputTypeDef]

### H265Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H265SettingsOutputTypeDef]

### Mpeg2Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Mpeg2SettingsTypeDef]

### Av1Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Av1SettingsOutputTypeDef]


# VideoCodecSettingsTypeDef

### FrameCaptureSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FrameCaptureSettingsTypeDef]

### H264Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H264SettingsTypeDef]

### H265Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H265SettingsTypeDef]

### Mpeg2Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Mpeg2SettingsTypeDef]

### Av1Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Av1SettingsTypeDef]


# VideoDescriptionOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VideoCodecSettingsOutputTypeDef]

### Height
- **Type**: typing.Optional[int]

### RespondToAfd
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH', 'RESPOND']]

### ScalingBehavior
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'STRETCH_TO_OUTPUT']]

### Sharpness
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# VideoDescriptionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VideoCodecSettingsTypeDef]

### Height
- **Type**: typing.Optional[int]

### RespondToAfd
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH', 'RESPOND']]

### ScalingBehavior
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'STRETCH_TO_OUTPUT']]

### Sharpness
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# VideoSelectorColorSpaceSettingsTypeDef

### Hdr10Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Hdr10SettingsTypeDef]


# VideoSelectorPidTypeDef

### Pid
- **Type**: typing.Optional[int]


# VideoSelectorProgramIdTypeDef

### ProgramId
- **Type**: typing.Optional[int]


# VideoSelectorSettingsTypeDef

### VideoSelectorPid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VideoSelectorPidTypeDef]

### VideoSelectorProgramId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VideoSelectorProgramIdTypeDef]


# VideoSelectorTypeDef

### ColorSpace
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'HDR10', 'HLG_2020', 'REC_601', 'REC_709']]

### ColorSpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VideoSelectorColorSpaceSettingsTypeDef]

### ColorSpaceUsage
- **Type**: typing.Optional[typing.Literal['FALLBACK', 'FORCE']]

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.VideoSelectorSettingsTypeDef]


# VpcOutputSettingsDescriptionTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### NetworkInterfaceIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]


# VpcOutputSettingsTypeDef

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PublicAddressAllocationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WavSettingsTypeDef

### BitDepth
- **Type**: typing.Optional[float]

### CodingMode
- **Type**: typing.Optional[typing.Literal['CODING_MODE_1_0', 'CODING_MODE_2_0', 'CODING_MODE_4_0', 'CODING_MODE_8_0']]

### SampleRate
- **Type**: typing.Optional[float]


# WebvttDestinationSettingsTypeDef

### StyleControl
- **Type**: typing.Optional[typing.Literal['NO_STYLE_DATA', 'PASSTHROUGH']]


