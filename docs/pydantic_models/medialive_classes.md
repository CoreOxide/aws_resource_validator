# Medialive Classes

# AacSettings

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


# Ac3Settings

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


# AcceptInputDeviceTransferRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# AccountConfiguration

### KmsKeyId
- **Type**: typing.Optional[str]


# AncillarySourceSettings

### SourceAncillaryChannelNumber
- **Type**: typing.Optional[int]


# AnywhereSettings

### ChannelPlacementGroupId
- **Type**: typing.Optional[str]

### ClusterId
- **Type**: typing.Optional[str]


# ArchiveCdnSettings

### ArchiveS3Settings
- **Type**: <class 'NoneType'>


# ArchiveContainerSettings

### M2tsSettings
- **Type**: <class 'NoneType'>

### RawSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ArchiveContainerSettingsOutput

### M2tsSettings
- **Type**: <class 'NoneType'>

### RawSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ArchiveGroupSettings

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
- **Required**: Yes

### ArchiveCdnSettings
- **Type**: <class 'NoneType'>

### RolloverInterval
- **Type**: typing.Optional[int]


# ArchiveOutputSettings

### ContainerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ArchiveContainerSettings'>
- **Required**: Yes

### Extension
- **Type**: typing.Optional[str]

### NameModifier
- **Type**: typing.Optional[str]


# ArchiveOutputSettingsOutput

### ContainerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ArchiveContainerSettingsOutput'>
- **Required**: Yes

### Extension
- **Type**: typing.Optional[str]

### NameModifier
- **Type**: typing.Optional[str]


# ArchiveS3Settings

### CannedAcl
- **Type**: typing.Optional[typing.Literal['AUTHENTICATED_READ', 'BUCKET_OWNER_FULL_CONTROL', 'BUCKET_OWNER_READ', 'PUBLIC_READ']]


# AudioChannelMapping

### InputChannelLevels
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputChannelLevel]
- **Required**: Yes

### OutputChannel
- **Type**: <class 'int'>
- **Required**: Yes


# AudioChannelMappingOutput

### InputChannelLevels
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputChannelLevel]
- **Required**: Yes

### OutputChannel
- **Type**: <class 'int'>
- **Required**: Yes


# AudioCodecSettings

### AacSettings
- **Type**: <class 'NoneType'>

### Ac3Settings
- **Type**: <class 'NoneType'>

### Eac3AtmosSettings
- **Type**: <class 'NoneType'>

### Eac3Settings
- **Type**: <class 'NoneType'>

### Mp2Settings
- **Type**: <class 'NoneType'>

### PassThroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### WavSettings
- **Type**: <class 'NoneType'>


# AudioCodecSettingsOutput

### AacSettings
- **Type**: <class 'NoneType'>

### Ac3Settings
- **Type**: <class 'NoneType'>

### Eac3AtmosSettings
- **Type**: <class 'NoneType'>

### Eac3Settings
- **Type**: <class 'NoneType'>

### Mp2Settings
- **Type**: <class 'NoneType'>

### PassThroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### WavSettings
- **Type**: <class 'NoneType'>


# AudioDescription

### AudioSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AudioNormalizationSettings
- **Type**: <class 'NoneType'>

### AudioType
- **Type**: typing.Optional[typing.Literal['CLEAN_EFFECTS', 'HEARING_IMPAIRED', 'UNDEFINED', 'VISUAL_IMPAIRED_COMMENTARY']]

### AudioTypeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### AudioWatermarkingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioWatermarkSettings]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioCodecSettings]

### LanguageCode
- **Type**: typing.Optional[str]

### LanguageCodeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### RemixSettings
- **Type**: <class 'NoneType'>

### StreamName
- **Type**: typing.Optional[str]

### AudioDashRoles
- **Type**: typing.Optional[typing.List[typing.Literal['ALTERNATE', 'COMMENTARY', 'DESCRIPTION', 'DUB', 'EMERGENCY', 'ENHANCED-AUDIO-INTELLIGIBILITY', 'KARAOKE', 'MAIN', 'SUPPLEMENTARY']]]

### DvbDashAccessibility
- **Type**: typing.Optional[typing.Literal['DVBDASH_1_VISUALLY_IMPAIRED', 'DVBDASH_2_HARD_OF_HEARING', 'DVBDASH_3_SUPPLEMENTAL_COMMENTARY', 'DVBDASH_4_DIRECTORS_COMMENTARY', 'DVBDASH_5_EDUCATIONAL_NOTES', 'DVBDASH_6_MAIN_PROGRAM', 'DVBDASH_7_CLEAN_FEED']]


# AudioDescriptionOutput

### AudioSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AudioNormalizationSettings
- **Type**: <class 'NoneType'>

### AudioType
- **Type**: typing.Optional[typing.Literal['CLEAN_EFFECTS', 'HEARING_IMPAIRED', 'UNDEFINED', 'VISUAL_IMPAIRED_COMMENTARY']]

### AudioTypeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### AudioWatermarkingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioWatermarkSettings]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioCodecSettingsOutput]

### LanguageCode
- **Type**: typing.Optional[str]

### LanguageCodeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.RemixSettingsOutput]

### StreamName
- **Type**: typing.Optional[str]

### AudioDashRoles
- **Type**: typing.Optional[typing.List[typing.Literal['ALTERNATE', 'COMMENTARY', 'DESCRIPTION', 'DUB', 'EMERGENCY', 'ENHANCED-AUDIO-INTELLIGIBILITY', 'KARAOKE', 'MAIN', 'SUPPLEMENTARY']]]

### DvbDashAccessibility
- **Type**: typing.Optional[typing.Literal['DVBDASH_1_VISUALLY_IMPAIRED', 'DVBDASH_2_HARD_OF_HEARING', 'DVBDASH_3_SUPPLEMENTAL_COMMENTARY', 'DVBDASH_4_DIRECTORS_COMMENTARY', 'DVBDASH_5_EDUCATIONAL_NOTES', 'DVBDASH_6_MAIN_PROGRAM', 'DVBDASH_7_CLEAN_FEED']]


# AudioDolbyEDecode

### ProgramSelection
- **Type**: typing.Literal['ALL_CHANNELS', 'PROGRAM_1', 'PROGRAM_2', 'PROGRAM_3', 'PROGRAM_4', 'PROGRAM_5', 'PROGRAM_6', 'PROGRAM_7', 'PROGRAM_8']
- **Required**: Yes


# AudioHlsRenditionSelection

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# AudioLanguageSelection

### LanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageSelectionPolicy
- **Type**: typing.Optional[typing.Literal['LOOSE', 'STRICT']]


# AudioNormalizationSettings

### Algorithm
- **Type**: typing.Optional[typing.Literal['ITU_1770_1', 'ITU_1770_2']]

### AlgorithmControl
- **Type**: typing.Optional[typing.Literal['CORRECT_AUDIO']]

### TargetLkfs
- **Type**: typing.Optional[float]


# AudioOnlyHlsSettings

### AudioGroupId
- **Type**: typing.Optional[str]

### AudioOnlyImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation]

### AudioTrackType
- **Type**: typing.Optional[typing.Literal['ALTERNATE_AUDIO_AUTO_SELECT', 'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT', 'ALTERNATE_AUDIO_NOT_AUTO_SELECT', 'AUDIO_ONLY_VARIANT_STREAM']]

### SegmentType
- **Type**: typing.Optional[typing.Literal['AAC', 'FMP4']]


# AudioPidSelection

### Pid
- **Type**: <class 'int'>
- **Required**: Yes


# AudioSelector

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SelectorSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioSelectorSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioSelectorSettingsOutput, NoneType]


# AudioSelectorOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioSelectorSettingsOutput]


# AudioSelectorSettings

### AudioHlsRenditionSelection
- **Type**: <class 'NoneType'>

### AudioLanguageSelection
- **Type**: <class 'NoneType'>

### AudioPidSelection
- **Type**: <class 'NoneType'>

### AudioTrackSelection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioTrackSelection, aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioTrackSelectionOutput, NoneType]


# AudioSelectorSettingsOutput

### AudioHlsRenditionSelection
- **Type**: <class 'NoneType'>

### AudioLanguageSelection
- **Type**: <class 'NoneType'>

### AudioPidSelection
- **Type**: <class 'NoneType'>

### AudioTrackSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioTrackSelectionOutput]


# AudioSilenceFailoverSettings

### AudioSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### AudioSilenceThresholdMsec
- **Type**: typing.Optional[int]


# AudioTrack

### Track
- **Type**: <class 'int'>
- **Required**: Yes


# AudioTrackSelection

### Tracks
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioTrack]
- **Required**: Yes

### DolbyEDecode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioDolbyEDecode]


# AudioTrackSelectionOutput

### Tracks
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioTrack]
- **Required**: Yes

### DolbyEDecode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioDolbyEDecode]


# AudioWatermarkSettings

### NielsenWatermarksSettings
- **Type**: <class 'NoneType'>


# AutomaticInputFailoverSettings

### SecondaryInputId
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorClearTimeMsec
- **Type**: typing.Optional[int]

### FailoverConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.FailoverCondition]]

### InputPreference
- **Type**: typing.Optional[typing.Literal['EQUAL_INPUT_PREFERENCE', 'PRIMARY_INPUT_PREFERRED']]


# AutomaticInputFailoverSettingsOutput

### SecondaryInputId
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorClearTimeMsec
- **Type**: typing.Optional[int]

### FailoverConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.FailoverCondition]]

### InputPreference
- **Type**: typing.Optional[typing.Literal['EQUAL_INPUT_PREFERENCE', 'PRIMARY_INPUT_PREFERRED']]


# Av1ColorSpaceSettings

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Hdr10Settings
- **Type**: <class 'NoneType'>

### Rec601Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# Av1ColorSpaceSettingsOutput

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Hdr10Settings
- **Type**: <class 'NoneType'>

### Rec601Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# Av1Settings

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Av1ColorSpaceSettings]

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
- **Type**: <class 'NoneType'>


# Av1SettingsOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Av1ColorSpaceSettingsOutput]

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
- **Type**: <class 'NoneType'>


# AvailBlanking

### AvailBlankingImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AvailConfiguration

### AvailSettings
- **Type**: <class 'NoneType'>

### Scte35SegmentationScope
- **Type**: typing.Optional[typing.Literal['ALL_OUTPUT_GROUPS', 'SCTE35_ENABLED_OUTPUT_GROUPS']]


# AvailSettings

### Esam
- **Type**: <class 'NoneType'>

### Scte35SpliceInsert
- **Type**: <class 'NoneType'>

### Scte35TimeSignalApos
- **Type**: <class 'NoneType'>


# BandwidthReductionFilterSettings

### PostFilterSharpening
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SHARPENING_1', 'SHARPENING_2', 'SHARPENING_3']]

### Strength
- **Type**: typing.Optional[typing.Literal['AUTO', 'STRENGTH_1', 'STRENGTH_2', 'STRENGTH_3', 'STRENGTH_4']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteRequest

### ChannelIds
- **Type**: typing.Optional[typing.List[str]]

### InputIds
- **Type**: typing.Optional[typing.List[str]]

### InputSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### MultiplexIds
- **Type**: typing.Optional[typing.List[str]]


# BatchDeleteResponse

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.BatchFailedResultModel]
- **Required**: Yes

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.BatchSuccessfulResultModel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# BatchFailedResultModel

### Arn
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# BatchScheduleActionCreateRequest

### ScheduleActions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleAction, aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleActionOutput]]
- **Required**: Yes


# BatchScheduleActionCreateResult

### ScheduleActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleActionOutput]
- **Required**: Yes


# BatchScheduleActionDeleteRequest

### ActionNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchScheduleActionDeleteResult

### ScheduleActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleActionOutput]
- **Required**: Yes


# BatchStartRequest

### ChannelIds
- **Type**: typing.Optional[typing.List[str]]

### MultiplexIds
- **Type**: typing.Optional[typing.List[str]]


# BatchStartResponse

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.BatchFailedResultModel]
- **Required**: Yes

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.BatchSuccessfulResultModel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# BatchStopRequest

### ChannelIds
- **Type**: typing.Optional[typing.List[str]]

### MultiplexIds
- **Type**: typing.Optional[typing.List[str]]


# BatchStopResponse

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.BatchFailedResultModel]
- **Required**: Yes

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.BatchSuccessfulResultModel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# BatchSuccessfulResultModel

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# BatchUpdateScheduleRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### Creates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.BatchScheduleActionCreateRequest]

### Deletes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.BatchScheduleActionDeleteRequest]


# BatchUpdateScheduleResponse

### Creates
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.BatchScheduleActionCreateResult'>
- **Required**: Yes

### Deletes
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.BatchScheduleActionDeleteResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# BlackoutSlate

### BlackoutSlateImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation]

### NetworkEndBlackout
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### NetworkEndBlackoutImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation]

### NetworkId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# BurnInDestinationSettings

### Alignment
- **Type**: typing.Optional[typing.Literal['CENTERED', 'LEFT', 'SMART']]

### BackgroundColor
- **Type**: typing.Optional[typing.Literal['BLACK', 'NONE', 'WHITE']]

### BackgroundOpacity
- **Type**: typing.Optional[int]

### Font
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation]

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


# CancelInputDeviceTransferRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# CaptionDescription

### CaptionSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Accessibility
- **Type**: typing.Optional[typing.Literal['DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES', 'IMPLEMENTS_ACCESSIBILITY_FEATURES']]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionDestinationSettings]

### LanguageCode
- **Type**: typing.Optional[str]

### LanguageDescription
- **Type**: typing.Optional[str]

### CaptionDashRoles
- **Type**: typing.Optional[typing.List[typing.Literal['ALTERNATE', 'CAPTION', 'COMMENTARY', 'DESCRIPTION', 'DUB', 'EASYREADER', 'EMERGENCY', 'FORCED-SUBTITLE', 'KARAOKE', 'MAIN', 'METADATA', 'SUBTITLE', 'SUPPLEMENTARY']]]

### DvbDashAccessibility
- **Type**: typing.Optional[typing.Literal['DVBDASH_1_VISUALLY_IMPAIRED', 'DVBDASH_2_HARD_OF_HEARING', 'DVBDASH_3_SUPPLEMENTAL_COMMENTARY', 'DVBDASH_4_DIRECTORS_COMMENTARY', 'DVBDASH_5_EDUCATIONAL_NOTES', 'DVBDASH_6_MAIN_PROGRAM', 'DVBDASH_7_CLEAN_FEED']]


# CaptionDescriptionOutput

### CaptionSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Accessibility
- **Type**: typing.Optional[typing.Literal['DOES_NOT_IMPLEMENT_ACCESSIBILITY_FEATURES', 'IMPLEMENTS_ACCESSIBILITY_FEATURES']]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionDestinationSettingsOutput]

### LanguageCode
- **Type**: typing.Optional[str]

### LanguageDescription
- **Type**: typing.Optional[str]

### CaptionDashRoles
- **Type**: typing.Optional[typing.List[typing.Literal['ALTERNATE', 'CAPTION', 'COMMENTARY', 'DESCRIPTION', 'DUB', 'EASYREADER', 'EMERGENCY', 'FORCED-SUBTITLE', 'KARAOKE', 'MAIN', 'METADATA', 'SUBTITLE', 'SUPPLEMENTARY']]]

### DvbDashAccessibility
- **Type**: typing.Optional[typing.Literal['DVBDASH_1_VISUALLY_IMPAIRED', 'DVBDASH_2_HARD_OF_HEARING', 'DVBDASH_3_SUPPLEMENTAL_COMMENTARY', 'DVBDASH_4_DIRECTORS_COMMENTARY', 'DVBDASH_5_EDUCATIONAL_NOTES', 'DVBDASH_6_MAIN_PROGRAM', 'DVBDASH_7_CLEAN_FEED']]


# CaptionDestinationSettings

### AribDestinationSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### BurnInDestinationSettings
- **Type**: <class 'NoneType'>

### DvbSubDestinationSettings
- **Type**: <class 'NoneType'>

### EbuTtDDestinationSettings
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

### WebvttDestinationSettings
- **Type**: <class 'NoneType'>


# CaptionDestinationSettingsOutput

### AribDestinationSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### BurnInDestinationSettings
- **Type**: <class 'NoneType'>

### DvbSubDestinationSettings
- **Type**: <class 'NoneType'>

### EbuTtDDestinationSettings
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

### WebvttDestinationSettings
- **Type**: <class 'NoneType'>


# CaptionLanguageMapping

### CaptionChannel
- **Type**: <class 'int'>
- **Required**: Yes

### LanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageDescription
- **Type**: <class 'str'>
- **Required**: Yes


# CaptionRectangle

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


# CaptionSelector

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[str]

### SelectorSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionSelectorSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionSelectorSettingsOutput, NoneType]


# CaptionSelectorOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[str]

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionSelectorSettingsOutput]


# CaptionSelectorSettings

### AncillarySourceSettings
- **Type**: <class 'NoneType'>

### AribSourceSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### DvbSubSourceSettings
- **Type**: <class 'NoneType'>

### EmbeddedSourceSettings
- **Type**: <class 'NoneType'>

### Scte20SourceSettings
- **Type**: <class 'NoneType'>

### Scte27SourceSettings
- **Type**: <class 'NoneType'>

### TeletextSourceSettings
- **Type**: <class 'NoneType'>


# CaptionSelectorSettingsOutput

### AncillarySourceSettings
- **Type**: <class 'NoneType'>

### AribSourceSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### DvbSubSourceSettings
- **Type**: <class 'NoneType'>

### EmbeddedSourceSettings
- **Type**: <class 'NoneType'>

### Scte20SourceSettings
- **Type**: <class 'NoneType'>

### Scte27SourceSettings
- **Type**: <class 'NoneType'>

### TeletextSourceSettings
- **Type**: <class 'NoneType'>


# CdiInputSpecification

### Resolution
- **Type**: typing.Optional[typing.Literal['FHD', 'HD', 'SD', 'UHD']]


# Channel

### Arn
- **Type**: typing.Optional[str]

### CdiInputSpecification
- **Type**: <class 'NoneType'>

### ChannelClass
- **Type**: typing.Optional[typing.Literal['SINGLE_PIPELINE', 'STANDARD']]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationOutput]]

### EgressEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEgressEndpoint]]

### EncoderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.EncoderSettingsOutput]

### Id
- **Type**: typing.Optional[str]

### InputAttachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachmentOutput]]

### InputSpecification
- **Type**: <class 'NoneType'>

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MaintenanceStatus]

### Name
- **Type**: typing.Optional[str]

### PipelineDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.PipelineDetail]]

### PipelinesRunningCount
- **Type**: typing.Optional[int]

### RoleArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'IDLE', 'RECOVERING', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATE_FAILED', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.VpcOutputSettingsDescription]

### AnywhereSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeAnywhereSettings]

### ChannelEngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionResponse]


# ChannelEgressEndpoint

### SourceIp
- **Type**: typing.Optional[str]


# ChannelEngineVersionRequest

### Version
- **Type**: typing.Optional[str]


# ChannelEngineVersionResponse

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]

### Version
- **Type**: typing.Optional[str]


# ChannelSummary

### Arn
- **Type**: typing.Optional[str]

### CdiInputSpecification
- **Type**: <class 'NoneType'>

### ChannelClass
- **Type**: typing.Optional[typing.Literal['SINGLE_PIPELINE', 'STANDARD']]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationOutput]]

### EgressEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEgressEndpoint]]

### Id
- **Type**: typing.Optional[str]

### InputAttachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachmentOutput]]

### InputSpecification
- **Type**: <class 'NoneType'>

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MaintenanceStatus]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.VpcOutputSettingsDescription]

### AnywhereSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeAnywhereSettings]

### ChannelEngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionResponse]

### UsedChannelEngineVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionResponse]]


# ClaimDeviceRequest

### Id
- **Type**: typing.Optional[str]


# CloudWatchAlarmTemplateGroupSummary

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


# CloudWatchAlarmTemplateSummary

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


# ClusterNetworkSettings

### DefaultRoute
- **Type**: typing.Optional[str]

### InterfaceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InterfaceMapping]]


# ClusterNetworkSettingsCreateRequest

### DefaultRoute
- **Type**: typing.Optional[str]

### InterfaceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InterfaceMappingCreateRequest]]


# ClusterNetworkSettingsUpdateRequest

### DefaultRoute
- **Type**: typing.Optional[str]

### InterfaceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InterfaceMappingUpdateRequest]]


# CmafIngestGroupSettings

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
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


# CmafIngestOutputSettings

### NameModifier
- **Type**: typing.Optional[str]


# ColorCorrection

### InputColorSpace
- **Type**: typing.Literal['HDR10', 'HLG_2020', 'REC_601', 'REC_709']
- **Required**: Yes

### OutputColorSpace
- **Type**: typing.Literal['HDR10', 'HLG_2020', 'REC_601', 'REC_709']
- **Required**: Yes

### Uri
- **Type**: <class 'str'>
- **Required**: Yes


# ColorCorrectionSettings

### GlobalColorCorrections
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ColorCorrection]
- **Required**: Yes


# ColorCorrectionSettingsOutput

### GlobalColorCorrections
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ColorCorrection]
- **Required**: Yes


# CreateChannelPlacementGroupRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Nodes
- **Type**: typing.Optional[typing.List[str]]

### RequestId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateChannelPlacementGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateChannelRequest

### CdiInputSpecification
- **Type**: <class 'NoneType'>

### ChannelClass
- **Type**: typing.Optional[typing.Literal['SINGLE_PIPELINE', 'STANDARD']]

### Destinations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestination, aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationOutput]]]

### EncoderSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.EncoderSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.EncoderSettingsOutput, NoneType]

### InputAttachments
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachment, aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachmentOutput]]]

### InputSpecification
- **Type**: <class 'NoneType'>

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MaintenanceCreateSettings]

### Name
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### Reserved
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.VpcOutputSettings]

### AnywhereSettings
- **Type**: <class 'NoneType'>

### ChannelEngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionRequest]

### DryRun
- **Type**: typing.Optional[bool]


# CreateChannelResponse

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Channel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCloudWatchAlarmTemplateGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RequestId
- **Type**: typing.Optional[str]


# CreateCloudWatchAlarmTemplateGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCloudWatchAlarmTemplateRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### RequestId
- **Type**: typing.Optional[str]


# CreateCloudWatchAlarmTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterRequest

### ClusterType
- **Type**: typing.Optional[typing.Literal['ON_PREMISES']]

### InstanceRoleArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ClusterNetworkSettingsCreateRequest]

### RequestId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateClusterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ClusterNetworkSettings'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventBridgeRuleTemplateGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RequestId
- **Type**: typing.Optional[str]


# CreateEventBridgeRuleTemplateGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventBridgeRuleTemplateRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.EventBridgeRuleTemplateTarget]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RequestId
- **Type**: typing.Optional[str]


# CreateEventBridgeRuleTemplateResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.EventBridgeRuleTemplateTarget]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInputRequest

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDestinationRequest]]

### InputDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceSettings]]

### InputSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### MediaConnectFlows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaConnectFlowRequest]]

### Name
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSourceRequest]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_CDI', 'INPUT_DEVICE', 'MEDIACONNECT', 'MP4_FILE', 'MULTICAST', 'RTMP_PULL', 'RTMP_PUSH', 'RTP_PUSH', 'SRT_CALLER', 'TS_FILE', 'UDP_PUSH', 'URL_PULL']]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputVpcRequest]

### SrtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.SrtSettingsRequest]

### InputNetworkLocation
- **Type**: typing.Optional[typing.Literal['AWS', 'ON_PREMISES']]

### MulticastSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MulticastSettingsCreateRequest]


# CreateInputResponse

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Input'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInputSecurityGroupRequest

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### WhitelistRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputWhitelistRuleCidr]]


# CreateInputSecurityGroupResponse

### SecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMultiplexProgramRequest

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexProgramSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramSettings'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateMultiplexProgramResponse

### MultiplexProgram
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgram'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMultiplexRequest

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexSettings'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMultiplexResponse

### Multiplex
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Multiplex'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNetworkRequest

### IpPools
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.IpPoolCreateRequest]]

### Name
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### Routes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.RouteCreateRequest]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateNetworkResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.IpPool]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Route]
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'IDLE', 'IN_USE', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNodeRegistrationScriptRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NodeInterfaceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.NodeInterfaceMapping]]

### RequestId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'BACKUP']]


# CreateNodeRegistrationScriptResponse

### NodeRegistrationScript
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNodeRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### NodeInterfaceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.NodeInterfaceMappingCreateRequest]]

### RequestId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'BACKUP']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateNodeResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.NodeInterfaceMapping]
- **Required**: Yes

### Role
- **Type**: typing.Literal['ACTIVE', 'BACKUP']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePartnerInputRequest

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreatePartnerInputResponse

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Input'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSignalMapRequest

### DiscoveryEntryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchAlarmTemplateGroupIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### Description
- **Type**: typing.Optional[str]

### EventBridgeRuleTemplateGroupIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RequestId
- **Type**: typing.Optional[str]


# CreateSignalMapResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResource]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastDiscoveredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSuccessfulMonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.SuccessfulMonitorDeployment'>
- **Required**: Yes

### MediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResource]
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitorChangesPendingDeployment
- **Type**: <class 'bool'>
- **Required**: Yes

### MonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MonitorDeployment'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTagsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DeleteChannelPlacementGroupRequest

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelPlacementGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteChannelRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.CdiInputSpecification'>
- **Required**: Yes

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationOutput]
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEgressEndpoint]
- **Required**: Yes

### EncoderSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.EncoderSettingsOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachmentOutput]
- **Required**: Yes

### InputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSpecification'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes

### Maintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MaintenanceStatus'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.PipelineDetail]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.VpcOutputSettingsDescription'>
- **Required**: Yes

### AnywhereSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeAnywhereSettings'>
- **Required**: Yes

### ChannelEngineVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCloudWatchAlarmTemplateGroupRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCloudWatchAlarmTemplateRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ClusterNetworkSettings'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEventBridgeRuleTemplateGroupRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventBridgeRuleTemplateRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInputRequest

### InputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInputSecurityGroupRequest

### InputSecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiplexProgramRequest

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiplexProgramResponse

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexProgramSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramSettings'>
- **Required**: Yes

### PacketIdentifiersMap
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramPacketIdentifiersMapOutput'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramPipelineDetail]
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMultiplexRequest

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiplexResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexOutputDestination]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNetworkRequest

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.IpPool]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Route]
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'IDLE', 'IN_USE', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNodeRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNodeResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.NodeInterfaceMapping]
- **Required**: Yes

### Role
- **Type**: typing.Literal['ACTIVE', 'BACKUP']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteReservationRequest

### ReservationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReservationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.RenewalSettings'>
- **Required**: Yes

### ReservationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ReservationResourceSpecification'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteScheduleRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSignalMapRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeAccountConfigurationResponse

### AccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.AccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAnywhereSettings

### ChannelPlacementGroupId
- **Type**: typing.Optional[str]

### ClusterId
- **Type**: typing.Optional[str]


# DescribeChannelPlacementGroupRequest

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelPlacementGroupRequestWait

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeChannelPlacementGroupRequestWaitExtra

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeChannelPlacementGroupRequestWaitExtraExtra

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeChannelPlacementGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeChannelPlacementGroupSummary

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


# DescribeChannelRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelRequestWait

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeChannelRequestWaitExtra

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeChannelRequestWaitExtraExtra

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeChannelRequestWaitExtraExtraExtra

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeChannelResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.CdiInputSpecification'>
- **Required**: Yes

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationOutput]
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEgressEndpoint]
- **Required**: Yes

### EncoderSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.EncoderSettingsOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachmentOutput]
- **Required**: Yes

### InputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSpecification'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes

### Maintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MaintenanceStatus'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.PipelineDetail]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.VpcOutputSettingsDescription'>
- **Required**: Yes

### AnywhereSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeAnywhereSettings'>
- **Required**: Yes

### ChannelEngineVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterRequestWait

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClusterRequestWaitExtra

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClusterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ClusterNetworkSettings'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ClusterNetworkSettings]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']]


# DescribeInputDeviceRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInputDeviceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['CONNECTED', 'DISCONNECTED']
- **Required**: Yes

### DeviceSettingsSyncState
- **Type**: typing.Literal['SYNCED', 'SYNCING']
- **Required**: Yes

### DeviceUpdateStatus
- **Type**: typing.Literal['NOT_UP_TO_DATE', 'UPDATING', 'UP_TO_DATE']
- **Required**: Yes

### HdDeviceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceHdSettings'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MacAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceNetworkSettings'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['HD', 'UHD']
- **Required**: Yes

### UhdDeviceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceUhdSettings'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### MedialiveInputArns
- **Type**: typing.List[str]
- **Required**: Yes

### OutputType
- **Type**: typing.Literal['MEDIACONNECT_FLOW', 'MEDIALIVE_INPUT', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInputDeviceThumbnailRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Accept
- **Type**: typing.Literal['image/jpeg']
- **Required**: Yes


# DescribeInputDeviceThumbnailResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInputRequest

### InputId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInputRequestWait

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeInputRequestWaitExtra

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeInputRequestWaitExtraExtra

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeInputResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AttachedChannels
- **Type**: typing.List[str]
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDestination]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### InputDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceSettings]
- **Required**: Yes

### InputPartnerIds
- **Type**: typing.List[str]
- **Required**: Yes

### InputSourceType
- **Type**: typing.Literal['DYNAMIC', 'STATIC']
- **Required**: Yes

### MediaConnectFlows
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaConnectFlow]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### Sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSource]
- **Required**: Yes

### State
- **Type**: typing.Literal['ATTACHED', 'CREATING', 'DELETED', 'DELETING', 'DETACHED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Type
- **Type**: typing.Literal['AWS_CDI', 'INPUT_DEVICE', 'MEDIACONNECT', 'MP4_FILE', 'MULTICAST', 'RTMP_PULL', 'RTMP_PUSH', 'RTP_PUSH', 'SRT_CALLER', 'TS_FILE', 'UDP_PUSH', 'URL_PULL']
- **Required**: Yes

### SrtSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.SrtSettings'>
- **Required**: Yes

### InputNetworkLocation
- **Type**: typing.Literal['AWS', 'ON_PREMISES']
- **Required**: Yes

### MulticastSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MulticastSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInputSecurityGroupRequest

### InputSecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInputSecurityGroupResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputWhitelistRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMultiplexProgramRequest

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMultiplexProgramResponse

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexProgramSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramSettings'>
- **Required**: Yes

### PacketIdentifiersMap
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramPacketIdentifiersMapOutput'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramPipelineDetail]
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMultiplexRequest

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMultiplexRequestWait

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeMultiplexRequestWaitExtra

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeMultiplexRequestWaitExtraExtra

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeMultiplexRequestWaitExtraExtraExtra

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeMultiplexResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexOutputDestination]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNetworkRequest

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNetworkResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.IpPool]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Route]
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'IDLE', 'IN_USE', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNetworkSummary

### Arn
- **Type**: typing.Optional[str]

### AssociatedClusterIds
- **Type**: typing.Optional[typing.List[str]]

### Id
- **Type**: typing.Optional[str]

### IpPools
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.IpPool]]

### Name
- **Type**: typing.Optional[str]

### Routes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Route]]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'IDLE', 'IN_USE', 'UPDATING']]


# DescribeNodeRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodeRequestWait

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeNodeRequestWaitExtra

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeNodeResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.NodeInterfaceMapping]
- **Required**: Yes

### Role
- **Type**: typing.Literal['ACTIVE', 'BACKUP']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNodeSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.NodeInterfaceMapping]]

### Role
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'BACKUP']]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']]


# DescribeOfferingRequest

### OfferingId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOfferingResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ReservationResourceSpecification'>
- **Required**: Yes

### UsagePrice
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReservationRequest

### ReservationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReservationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.RenewalSettings'>
- **Required**: Yes

### ReservationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ReservationResourceSpecification'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeScheduleRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScheduleRequestPaginate

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# DescribeScheduleResponse

### ScheduleActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleActionOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeThumbnailsRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### ThumbnailType
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThumbnailsResponse

### ThumbnailDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ThumbnailDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# DvbNitSettings

### NetworkId
- **Type**: <class 'int'>
- **Required**: Yes

### NetworkName
- **Type**: <class 'str'>
- **Required**: Yes

### RepInterval
- **Type**: typing.Optional[int]


# DvbSdtSettings

### OutputSdt
- **Type**: typing.Optional[typing.Literal['SDT_FOLLOW', 'SDT_FOLLOW_IF_PRESENT', 'SDT_MANUAL', 'SDT_NONE']]

### RepInterval
- **Type**: typing.Optional[int]

### ServiceName
- **Type**: typing.Optional[str]

### ServiceProviderName
- **Type**: typing.Optional[str]


# DvbSubDestinationSettings

### Alignment
- **Type**: typing.Optional[typing.Literal['CENTERED', 'LEFT', 'SMART']]

### BackgroundColor
- **Type**: typing.Optional[typing.Literal['BLACK', 'NONE', 'WHITE']]

### BackgroundOpacity
- **Type**: typing.Optional[int]

### Font
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation]

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


# DvbSubSourceSettings

### OcrLanguage
- **Type**: typing.Optional[typing.Literal['DEU', 'ENG', 'FRA', 'NLD', 'POR', 'SPA']]

### Pid
- **Type**: typing.Optional[int]


# DvbTdtSettings

### RepInterval
- **Type**: typing.Optional[int]


# Eac3AtmosSettings

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


# Eac3Settings

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


# EbuTtDDestinationSettings

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


# EmbeddedSourceSettings

### Convert608To708
- **Type**: typing.Optional[typing.Literal['DISABLED', 'UPCONVERT']]

### Scte20Detection
- **Type**: typing.Optional[typing.Literal['AUTO', 'OFF']]

### Source608ChannelNumber
- **Type**: typing.Optional[int]

### Source608TrackNumber
- **Type**: typing.Optional[int]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# EncoderSettings

### AudioDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioDescription]
- **Required**: Yes

### OutputGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputGroup]
- **Required**: Yes

### TimecodeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.TimecodeConfig'>
- **Required**: Yes

### VideoDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.VideoDescription]
- **Required**: Yes

### AvailBlanking
- **Type**: <class 'NoneType'>

### AvailConfiguration
- **Type**: <class 'NoneType'>

### BlackoutSlate
- **Type**: <class 'NoneType'>

### CaptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionDescription]]

### FeatureActivations
- **Type**: <class 'NoneType'>

### GlobalConfiguration
- **Type**: <class 'NoneType'>

### MotionGraphicsConfiguration
- **Type**: <class 'NoneType'>

### NielsenConfiguration
- **Type**: <class 'NoneType'>

### ThumbnailConfiguration
- **Type**: <class 'NoneType'>

### ColorCorrectionSettings
- **Type**: <class 'NoneType'>


# EncoderSettingsOutput

### AudioDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioDescriptionOutput]
- **Required**: Yes

### OutputGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputGroupOutput]
- **Required**: Yes

### TimecodeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.TimecodeConfig'>
- **Required**: Yes

### VideoDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.VideoDescriptionOutput]
- **Required**: Yes

### AvailBlanking
- **Type**: <class 'NoneType'>

### AvailConfiguration
- **Type**: <class 'NoneType'>

### BlackoutSlate
- **Type**: <class 'NoneType'>

### CaptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionDescriptionOutput]]

### FeatureActivations
- **Type**: <class 'NoneType'>

### GlobalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.GlobalConfigurationOutput]

### MotionGraphicsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MotionGraphicsConfigurationOutput]

### NielsenConfiguration
- **Type**: <class 'NoneType'>

### ThumbnailConfiguration
- **Type**: <class 'NoneType'>

### ColorCorrectionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ColorCorrectionSettingsOutput]


# EpochLockingSettings

### CustomEpoch
- **Type**: typing.Optional[str]

### JamSyncTime
- **Type**: typing.Optional[str]


# Esam

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


# EventBridgeRuleTemplateGroupSummary

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


# EventBridgeRuleTemplateSummary

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


# EventBridgeRuleTemplateTarget

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# Extra

### OutputSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputSettingsOutput'>
- **Required**: Yes

### AudioDescriptionNames
- **Type**: typing.Optional[typing.List[str]]

### CaptionDescriptionNames
- **Type**: typing.Optional[typing.List[str]]

### OutputName
- **Type**: typing.Optional[str]

### VideoDescriptionName
- **Type**: typing.Optional[str]


# FailoverCondition

### FailoverConditionSettings
- **Type**: <class 'NoneType'>


# FailoverConditionSettings

### AudioSilenceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioSilenceFailoverSettings]

### InputLossSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLossFailoverSettings]

### VideoBlackSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.VideoBlackFailoverSettings]


# FeatureActivations

### InputPrepareScheduleActions
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### OutputStaticImageOverlayScheduleActions
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FecOutputSettings

### ColumnDepth
- **Type**: typing.Optional[int]

### IncludeFec
- **Type**: typing.Optional[typing.Literal['COLUMN', 'COLUMN_AND_ROW']]

### RowLength
- **Type**: typing.Optional[int]


# FixedModeScheduleActionStartSettings

### Time
- **Type**: <class 'str'>
- **Required**: Yes


# Fmp4HlsSettings

### AudioRenditionSets
- **Type**: typing.Optional[str]

### NielsenId3Behavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]

### TimedMetadataBehavior
- **Type**: typing.Optional[typing.Literal['NO_PASSTHROUGH', 'PASSTHROUGH']]


# FollowModeScheduleActionStartSettings

### FollowPoint
- **Type**: typing.Literal['END', 'START']
- **Required**: Yes

### ReferenceActionName
- **Type**: <class 'str'>
- **Required**: Yes


# FrameCaptureCdnSettings

### FrameCaptureS3Settings
- **Type**: <class 'NoneType'>


# FrameCaptureGroupSettings

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
- **Required**: Yes

### FrameCaptureCdnSettings
- **Type**: <class 'NoneType'>


# FrameCaptureOutputSettings

### NameModifier
- **Type**: typing.Optional[str]


# FrameCaptureS3Settings

### CannedAcl
- **Type**: typing.Optional[typing.Literal['AUTHENTICATED_READ', 'BUCKET_OWNER_FULL_CONTROL', 'BUCKET_OWNER_READ', 'PUBLIC_READ']]


# FrameCaptureSettings

### CaptureInterval
- **Type**: typing.Optional[int]

### CaptureIntervalUnits
- **Type**: typing.Optional[typing.Literal['MILLISECONDS', 'SECONDS']]

### TimecodeBurninSettings
- **Type**: <class 'NoneType'>


# GetCloudWatchAlarmTemplateGroupRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCloudWatchAlarmTemplateGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# GetCloudWatchAlarmTemplateRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCloudWatchAlarmTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventBridgeRuleTemplateGroupRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventBridgeRuleTemplateGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventBridgeRuleTemplateRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventBridgeRuleTemplateResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.EventBridgeRuleTemplateTarget]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# GetSignalMapRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSignalMapRequestWait

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetSignalMapRequestWaitExtra

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetSignalMapRequestWaitExtraExtra

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetSignalMapRequestWaitExtraExtraExtra

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetSignalMapResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResource]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastDiscoveredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSuccessfulMonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.SuccessfulMonitorDeployment'>
- **Required**: Yes

### MediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResource]
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitorChangesPendingDeployment
- **Type**: <class 'bool'>
- **Required**: Yes

### MonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MonitorDeployment'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# GlobalConfiguration

### InitialAudioGain
- **Type**: typing.Optional[int]

### InputEndAction
- **Type**: typing.Optional[typing.Literal['NONE', 'SWITCH_AND_LOOP_INPUTS']]

### InputLossBehavior
- **Type**: <class 'NoneType'>

### OutputLockingMode
- **Type**: typing.Optional[typing.Literal['EPOCH_LOCKING', 'PIPELINE_LOCKING']]

### OutputTimingSource
- **Type**: typing.Optional[typing.Literal['INPUT_CLOCK', 'SYSTEM_CLOCK']]

### SupportLowFramerateInputs
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### OutputLockingSettings
- **Type**: <class 'NoneType'>


# GlobalConfigurationOutput

### InitialAudioGain
- **Type**: typing.Optional[int]

### InputEndAction
- **Type**: typing.Optional[typing.Literal['NONE', 'SWITCH_AND_LOOP_INPUTS']]

### InputLossBehavior
- **Type**: <class 'NoneType'>

### OutputLockingMode
- **Type**: typing.Optional[typing.Literal['EPOCH_LOCKING', 'PIPELINE_LOCKING']]

### OutputTimingSource
- **Type**: typing.Optional[typing.Literal['INPUT_CLOCK', 'SYSTEM_CLOCK']]

### SupportLowFramerateInputs
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### OutputLockingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLockingSettingsOutput]


# H264ColorSpaceSettings

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec601Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# H264ColorSpaceSettingsOutput

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec601Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# H264FilterSettings

### TemporalFilterSettings
- **Type**: <class 'NoneType'>

### BandwidthReductionFilterSettings
- **Type**: <class 'NoneType'>


# H264Settings

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.H264ColorSpaceSettings]

### EntropyEncoding
- **Type**: typing.Optional[typing.Literal['CABAC', 'CAVLC']]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.H264FilterSettings]

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
- **Type**: <class 'NoneType'>

### MinQp
- **Type**: typing.Optional[int]


# H264SettingsOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.H264ColorSpaceSettingsOutput]

### EntropyEncoding
- **Type**: typing.Optional[typing.Literal['CABAC', 'CAVLC']]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.H264FilterSettings]

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
- **Type**: <class 'NoneType'>

### MinQp
- **Type**: typing.Optional[int]


# H265ColorSpaceSettings

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### DolbyVision81Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Hdr10Settings
- **Type**: <class 'NoneType'>

### Rec601Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# H265ColorSpaceSettingsOutput

### ColorSpacePassthroughSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### DolbyVision81Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Hdr10Settings
- **Type**: <class 'NoneType'>

### Rec601Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Rec709Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# H265FilterSettings

### TemporalFilterSettings
- **Type**: <class 'NoneType'>

### BandwidthReductionFilterSettings
- **Type**: <class 'NoneType'>


# H265Settings

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.H265ColorSpaceSettings]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.H265FilterSettings]

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
- **Type**: <class 'NoneType'>

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


# H265SettingsOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.H265ColorSpaceSettingsOutput]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.H265FilterSettings]

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
- **Type**: <class 'NoneType'>

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


# Hdr10Settings

### MaxCll
- **Type**: typing.Optional[int]

### MaxFall
- **Type**: typing.Optional[int]


# HlsAkamaiSettings

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


# HlsBasicPutSettings

### ConnectionRetryInterval
- **Type**: typing.Optional[int]

### FilecacheDuration
- **Type**: typing.Optional[int]

### NumRetries
- **Type**: typing.Optional[int]

### RestartDelay
- **Type**: typing.Optional[int]


# HlsCdnSettings

### HlsAkamaiSettings
- **Type**: <class 'NoneType'>

### HlsBasicPutSettings
- **Type**: <class 'NoneType'>

### HlsMediaStoreSettings
- **Type**: <class 'NoneType'>

### HlsS3Settings
- **Type**: <class 'NoneType'>

### HlsWebdavSettings
- **Type**: <class 'NoneType'>


# HlsGroupSettings

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionLanguageMapping]]

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
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

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


# HlsGroupSettingsOutput

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionLanguageMapping]]

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
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

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


# HlsId3SegmentTaggingScheduleActionSettings

### Tag
- **Type**: typing.Optional[str]

### Id3
- **Type**: typing.Optional[str]


# HlsInputSettings

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


# HlsMediaStoreSettings

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


# HlsOutputSettings

### HlsSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.HlsSettings'>
- **Required**: Yes

### H265PackagingType
- **Type**: typing.Optional[typing.Literal['HEV1', 'HVC1']]

### NameModifier
- **Type**: typing.Optional[str]

### SegmentModifier
- **Type**: typing.Optional[str]


# HlsOutputSettingsOutput

### HlsSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.HlsSettingsOutput'>
- **Required**: Yes

### H265PackagingType
- **Type**: typing.Optional[typing.Literal['HEV1', 'HVC1']]

### NameModifier
- **Type**: typing.Optional[str]

### SegmentModifier
- **Type**: typing.Optional[str]


# HlsS3Settings

### CannedAcl
- **Type**: typing.Optional[typing.Literal['AUTHENTICATED_READ', 'BUCKET_OWNER_FULL_CONTROL', 'BUCKET_OWNER_READ', 'PUBLIC_READ']]


# HlsSettings

### AudioOnlyHlsSettings
- **Type**: <class 'NoneType'>

### Fmp4HlsSettings
- **Type**: <class 'NoneType'>

### FrameCaptureHlsSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### StandardHlsSettings
- **Type**: <class 'NoneType'>


# HlsSettingsOutput

### AudioOnlyHlsSettings
- **Type**: <class 'NoneType'>

### Fmp4HlsSettings
- **Type**: <class 'NoneType'>

### FrameCaptureHlsSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### StandardHlsSettings
- **Type**: <class 'NoneType'>


# HlsTimedMetadataScheduleActionSettings

### Id3
- **Type**: <class 'str'>
- **Required**: Yes


# HlsWebdavSettings

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


# Id3SegmentTaggingScheduleActionSettings

### Id3
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[str]


# Input

### Arn
- **Type**: typing.Optional[str]

### AttachedChannels
- **Type**: typing.Optional[typing.List[str]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDestination]]

### Id
- **Type**: typing.Optional[str]

### InputClass
- **Type**: typing.Optional[typing.Literal['SINGLE_PIPELINE', 'STANDARD']]

### InputDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceSettings]]

### InputPartnerIds
- **Type**: typing.Optional[typing.List[str]]

### InputSourceType
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]

### MediaConnectFlows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaConnectFlow]]

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSource]]

### State
- **Type**: typing.Optional[typing.Literal['ATTACHED', 'CREATING', 'DELETED', 'DELETING', 'DETACHED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_CDI', 'INPUT_DEVICE', 'MEDIACONNECT', 'MP4_FILE', 'MULTICAST', 'RTMP_PULL', 'RTMP_PUSH', 'RTP_PUSH', 'SRT_CALLER', 'TS_FILE', 'UDP_PUSH', 'URL_PULL']]

### SrtSettings
- **Type**: <class 'NoneType'>

### InputNetworkLocation
- **Type**: typing.Optional[typing.Literal['AWS', 'ON_PREMISES']]

### MulticastSettings
- **Type**: <class 'NoneType'>


# InputAttachment

### AutomaticInputFailoverSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.AutomaticInputFailoverSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.AutomaticInputFailoverSettingsOutput, NoneType]

### InputAttachmentName
- **Type**: typing.Optional[str]

### InputId
- **Type**: typing.Optional[str]

### InputSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSettingsOutput, NoneType]

### LogicalInterfaceNames
- **Type**: typing.Optional[typing.List[str]]


# InputAttachmentOutput

### AutomaticInputFailoverSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.AutomaticInputFailoverSettingsOutput]

### InputAttachmentName
- **Type**: typing.Optional[str]

### InputId
- **Type**: typing.Optional[str]

### InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSettingsOutput]

### LogicalInterfaceNames
- **Type**: typing.Optional[typing.List[str]]


# InputChannelLevel

### Gain
- **Type**: <class 'int'>
- **Required**: Yes

### InputChannel
- **Type**: <class 'int'>
- **Required**: Yes


# InputClippingSettings

### InputTimecodeSource
- **Type**: typing.Literal['EMBEDDED', 'ZEROBASED']
- **Required**: Yes

### StartTimecode
- **Type**: <class 'NoneType'>

### StopTimecode
- **Type**: <class 'NoneType'>


# InputDestination

### Ip
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDestinationVpc]

### Network
- **Type**: typing.Optional[str]

### NetworkRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDestinationRoute]]


# InputDestinationRequest

### StreamName
- **Type**: typing.Optional[str]

### Network
- **Type**: typing.Optional[str]

### NetworkRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputRequestDestinationRoute]]

### StaticIpAddress
- **Type**: typing.Optional[str]


# InputDestinationRoute

### Cidr
- **Type**: typing.Optional[str]

### Gateway
- **Type**: typing.Optional[str]


# InputDestinationVpc

### AvailabilityZone
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]


# InputDeviceConfigurableAudioChannelPairConfig

### Id
- **Type**: typing.Optional[int]

### Profile
- **Type**: typing.Optional[typing.Literal['CBR-AAC_HQ-192000', 'CBR-AAC_HQ-256000', 'CBR-AAC_HQ-384000', 'CBR-AAC_HQ-512000', 'DISABLED', 'VBR-AAC_HE-64000', 'VBR-AAC_HHE-16000', 'VBR-AAC_LC-128000']]


# InputDeviceConfigurableSettings

### ConfiguredInput
- **Type**: typing.Optional[typing.Literal['AUTO', 'HDMI', 'SDI']]

### MaxBitrate
- **Type**: typing.Optional[int]

### LatencyMs
- **Type**: typing.Optional[int]

### Codec
- **Type**: typing.Optional[typing.Literal['AVC', 'HEVC']]

### MediaconnectSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceMediaConnectConfigurableSettings]

### AudioChannelPairs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceConfigurableAudioChannelPairConfig]]


# InputDeviceHdSettings

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


# InputDeviceMediaConnectConfigurableSettings

### FlowArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### SourceName
- **Type**: typing.Optional[str]


# InputDeviceMediaConnectSettings

### FlowArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### SourceName
- **Type**: typing.Optional[str]


# InputDeviceNetworkSettings

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


# InputDeviceRequest

### Id
- **Type**: typing.Optional[str]


# InputDeviceSettings

### Id
- **Type**: typing.Optional[str]


# InputDeviceSummary

### Arn
- **Type**: typing.Optional[str]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED']]

### DeviceSettingsSyncState
- **Type**: typing.Optional[typing.Literal['SYNCED', 'SYNCING']]

### DeviceUpdateStatus
- **Type**: typing.Optional[typing.Literal['NOT_UP_TO_DATE', 'UPDATING', 'UP_TO_DATE']]

### HdDeviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceHdSettings]

### Id
- **Type**: typing.Optional[str]

### MacAddress
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceNetworkSettings]

### SerialNumber
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['HD', 'UHD']]

### UhdDeviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceUhdSettings]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### MedialiveInputArns
- **Type**: typing.Optional[typing.List[str]]

### OutputType
- **Type**: typing.Optional[typing.Literal['MEDIACONNECT_FLOW', 'MEDIALIVE_INPUT', 'NONE']]


# InputDeviceUhdAudioChannelPairConfig

### Id
- **Type**: typing.Optional[int]

### Profile
- **Type**: typing.Optional[typing.Literal['CBR-AAC_HQ-192000', 'CBR-AAC_HQ-256000', 'CBR-AAC_HQ-384000', 'CBR-AAC_HQ-512000', 'DISABLED', 'VBR-AAC_HE-64000', 'VBR-AAC_HHE-16000', 'VBR-AAC_LC-128000']]


# InputDeviceUhdSettings

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceMediaConnectSettings]

### AudioChannelPairs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceUhdAudioChannelPairConfig]]


# InputLocation

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### PasswordParam
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# InputLossBehavior

### BlackFrameMsec
- **Type**: typing.Optional[int]

### InputLossImageColor
- **Type**: typing.Optional[str]

### InputLossImageSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation]

### InputLossImageType
- **Type**: typing.Optional[typing.Literal['COLOR', 'SLATE']]

### RepeatFrameMsec
- **Type**: typing.Optional[int]


# InputLossFailoverSettings

### InputLossThresholdMsec
- **Type**: typing.Optional[int]


# InputPrepareScheduleActionSettings

### InputAttachmentNameReference
- **Type**: typing.Optional[str]

### InputClippingSettings
- **Type**: <class 'NoneType'>

### UrlPath
- **Type**: typing.Optional[typing.List[str]]


# InputPrepareScheduleActionSettingsOutput

### InputAttachmentNameReference
- **Type**: typing.Optional[str]

### InputClippingSettings
- **Type**: <class 'NoneType'>

### UrlPath
- **Type**: typing.Optional[typing.List[str]]


# InputRequestDestinationRoute

### Cidr
- **Type**: typing.Optional[str]

### Gateway
- **Type**: typing.Optional[str]


# InputSecurityGroup

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputWhitelistRule]]


# InputSettings

### AudioSelectors
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioSelector, aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioSelectorOutput]]]

### CaptionSelectors
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionSelector, aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionSelectorOutput]]]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FilterStrength
- **Type**: typing.Optional[int]

### InputFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'FORCED']]

### NetworkInputSettings
- **Type**: <class 'NoneType'>

### Scte35Pid
- **Type**: typing.Optional[int]

### Smpte2038DataPreference
- **Type**: typing.Optional[typing.Literal['IGNORE', 'PREFER']]

### SourceEndBehavior
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'LOOP']]

### VideoSelector
- **Type**: <class 'NoneType'>


# InputSettingsOutput

### AudioSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioSelectorOutput]]

### CaptionSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionSelectorOutput]]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FilterStrength
- **Type**: typing.Optional[int]

### InputFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'FORCED']]

### NetworkInputSettings
- **Type**: <class 'NoneType'>

### Scte35Pid
- **Type**: typing.Optional[int]

### Smpte2038DataPreference
- **Type**: typing.Optional[typing.Literal['IGNORE', 'PREFER']]

### SourceEndBehavior
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'LOOP']]

### VideoSelector
- **Type**: <class 'NoneType'>


# InputSource

### PasswordParam
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# InputSourceRequest

### PasswordParam
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# InputSpecification

### Codec
- **Type**: typing.Optional[typing.Literal['AVC', 'HEVC', 'MPEG2']]

### MaximumBitrate
- **Type**: typing.Optional[typing.Literal['MAX_10_MBPS', 'MAX_20_MBPS', 'MAX_50_MBPS']]

### Resolution
- **Type**: typing.Optional[typing.Literal['HD', 'SD', 'UHD']]


# InputSwitchScheduleActionSettings

### InputAttachmentNameReference
- **Type**: <class 'str'>
- **Required**: Yes

### InputClippingSettings
- **Type**: <class 'NoneType'>

### UrlPath
- **Type**: typing.Optional[typing.List[str]]


# InputSwitchScheduleActionSettingsOutput

### InputAttachmentNameReference
- **Type**: <class 'str'>
- **Required**: Yes

### InputClippingSettings
- **Type**: <class 'NoneType'>

### UrlPath
- **Type**: typing.Optional[typing.List[str]]


# InputVpcRequest

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# InputWhitelistRule

### Cidr
- **Type**: typing.Optional[str]


# InputWhitelistRuleCidr

### Cidr
- **Type**: typing.Optional[str]


# InterfaceMapping

### LogicalInterfaceName
- **Type**: typing.Optional[str]

### NetworkId
- **Type**: typing.Optional[str]


# InterfaceMappingCreateRequest

### LogicalInterfaceName
- **Type**: typing.Optional[str]

### NetworkId
- **Type**: typing.Optional[str]


# InterfaceMappingUpdateRequest

### LogicalInterfaceName
- **Type**: typing.Optional[str]

### NetworkId
- **Type**: typing.Optional[str]


# IpPool

### Cidr
- **Type**: typing.Optional[str]


# IpPoolCreateRequest

### Cidr
- **Type**: typing.Optional[str]


# IpPoolUpdateRequest

### Cidr
- **Type**: typing.Optional[str]


# KeyProviderSettings

### StaticKeySettings
- **Type**: <class 'NoneType'>


# ListChannelPlacementGroupsRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelPlacementGroupsRequestPaginate

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListChannelPlacementGroupsResponse

### ChannelPlacementGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeChannelPlacementGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListChannelsResponse

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCloudWatchAlarmTemplateGroupsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]


# ListCloudWatchAlarmTemplateGroupsRequestPaginate

### Scope
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListCloudWatchAlarmTemplateGroupsResponse

### CloudWatchAlarmTemplateGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.CloudWatchAlarmTemplateGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCloudWatchAlarmTemplatesRequest

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


# ListCloudWatchAlarmTemplatesRequestPaginate

### GroupIdentifier
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListCloudWatchAlarmTemplatesResponse

### CloudWatchAlarmTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.CloudWatchAlarmTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListClustersResponse

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeClusterSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventBridgeRuleTemplateGroupsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]


# ListEventBridgeRuleTemplateGroupsRequestPaginate

### SignalMapIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListEventBridgeRuleTemplateGroupsResponse

### EventBridgeRuleTemplateGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.EventBridgeRuleTemplateGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventBridgeRuleTemplatesRequest

### GroupIdentifier
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]


# ListEventBridgeRuleTemplatesRequestPaginate

### GroupIdentifier
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListEventBridgeRuleTemplatesResponse

### EventBridgeRuleTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.EventBridgeRuleTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInputDeviceTransfersRequest

### TransferType
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInputDeviceTransfersRequestPaginate

### TransferType
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListInputDeviceTransfersResponse

### InputDeviceTransfers
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.TransferringInputDeviceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInputDevicesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInputDevicesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListInputDevicesResponse

### InputDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInputSecurityGroupsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInputSecurityGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListInputSecurityGroupsResponse

### InputSecurityGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSecurityGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInputsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInputsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListInputsResponse

### Inputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Input]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMultiplexProgramsRequest

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMultiplexProgramsRequestPaginate

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListMultiplexProgramsResponse

### MultiplexPrograms
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMultiplexesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMultiplexesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListMultiplexesResponse

### Multiplexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNetworksRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNetworksRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListNetworksResponse

### Networks
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeNetworkSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNodesRequestPaginate

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListNodesResponse

### Nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeNodeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOfferingsRequest

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


# ListOfferingsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListOfferingsResponse

### Offerings
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Offering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReservationsRequest

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


# ListReservationsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListReservationsResponse

### Reservations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Reservation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSignalMapsRequest

### CloudWatchAlarmTemplateGroupIdentifier
- **Type**: typing.Optional[str]

### EventBridgeRuleTemplateGroupIdentifier
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSignalMapsRequestPaginate

### CloudWatchAlarmTemplateGroupIdentifier
- **Type**: typing.Optional[str]

### EventBridgeRuleTemplateGroupIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PaginatorConfig]


# ListSignalMapsResponse

### SignalMaps
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.SignalMapSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# ListVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# M2tsSettings

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
- **Type**: <class 'NoneType'>

### DvbSdtSettings
- **Type**: <class 'NoneType'>

### DvbSubPids
- **Type**: typing.Optional[str]

### DvbTdtSettings
- **Type**: <class 'NoneType'>

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


# M3u8Settings

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


# MaintenanceCreateSettings

### MaintenanceDay
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### MaintenanceStartTime
- **Type**: typing.Optional[str]


# MaintenanceStatus

### MaintenanceDay
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### MaintenanceDeadline
- **Type**: typing.Optional[str]

### MaintenanceScheduledDate
- **Type**: typing.Optional[str]

### MaintenanceStartTime
- **Type**: typing.Optional[str]


# MaintenanceUpdateSettings

### MaintenanceDay
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### MaintenanceScheduledDate
- **Type**: typing.Optional[str]

### MaintenanceStartTime
- **Type**: typing.Optional[str]


# MediaConnectFlow

### FlowArn
- **Type**: typing.Optional[str]


# MediaConnectFlowRequest

### FlowArn
- **Type**: typing.Optional[str]


# MediaPackageGroupSettings

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
- **Required**: Yes


# MediaPackageOutputDestinationSettings

### ChannelId
- **Type**: typing.Optional[str]

### ChannelGroup
- **Type**: typing.Optional[str]

### ChannelName
- **Type**: typing.Optional[str]


# MediaResource

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResourceNeighbor]]

### Name
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResourceNeighbor]]


# MediaResourceNeighbor

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# MonitorDeployment

### Status
- **Type**: typing.Literal['DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DEPLOYMENT_COMPLETE', 'DEPLOYMENT_FAILED', 'DEPLOYMENT_IN_PROGRESS', 'DRY_RUN_DEPLOYMENT_COMPLETE', 'DRY_RUN_DEPLOYMENT_FAILED', 'DRY_RUN_DEPLOYMENT_IN_PROGRESS', 'NOT_DEPLOYED']
- **Required**: Yes

### DetailsUri
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# MotionGraphicsActivateScheduleActionSettings

### Duration
- **Type**: typing.Optional[int]

### PasswordParam
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# MotionGraphicsConfiguration

### MotionGraphicsSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MotionGraphicsSettings'>
- **Required**: Yes

### MotionGraphicsInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MotionGraphicsConfigurationOutput

### MotionGraphicsSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MotionGraphicsSettingsOutput'>
- **Required**: Yes

### MotionGraphicsInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MotionGraphicsSettings

### HtmlMotionGraphicsSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# MotionGraphicsSettingsOutput

### HtmlMotionGraphicsSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# Mp2Settings

### Bitrate
- **Type**: typing.Optional[float]

### CodingMode
- **Type**: typing.Optional[typing.Literal['CODING_MODE_1_0', 'CODING_MODE_2_0']]

### SampleRate
- **Type**: typing.Optional[float]


# Mpeg2FilterSettings

### TemporalFilterSettings
- **Type**: <class 'NoneType'>


# Mpeg2Settings

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Mpeg2FilterSettings]

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
- **Type**: <class 'NoneType'>


# MsSmoothGroupSettings

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
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


# MsSmoothOutputSettings

### H265PackagingType
- **Type**: typing.Optional[typing.Literal['HEV1', 'HVC1']]

### NameModifier
- **Type**: typing.Optional[str]


# MulticastInputSettings

### SourceIpAddress
- **Type**: typing.Optional[str]


# MulticastSettings

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MulticastSource]]


# MulticastSettingsCreateRequest

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MulticastSourceCreateRequest]]


# MulticastSettingsUpdateRequest

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MulticastSourceUpdateRequest]]


# MulticastSource

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIp
- **Type**: typing.Optional[str]


# MulticastSourceCreateRequest

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIp
- **Type**: typing.Optional[str]


# MulticastSourceUpdateRequest

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIp
- **Type**: typing.Optional[str]


# Multiplex

### Arn
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexOutputDestination]]

### Id
- **Type**: typing.Optional[str]

### MultiplexSettings
- **Type**: <class 'NoneType'>

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


# MultiplexContainerSettings

### MultiplexM2tsSettings
- **Type**: <class 'NoneType'>


# MultiplexM2tsSettings

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


# MultiplexMediaConnectOutputDestinationSettings

### EntitlementArn
- **Type**: typing.Optional[str]


# MultiplexOutputDestination

### MediaConnectSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexMediaConnectOutputDestinationSettings]


# MultiplexOutputSettings

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
- **Required**: Yes

### ContainerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexContainerSettings]


# MultiplexProgram

### ChannelId
- **Type**: typing.Optional[str]

### MultiplexProgramSettings
- **Type**: <class 'NoneType'>

### PacketIdentifiersMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramPacketIdentifiersMapOutput]

### PipelineDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramPipelineDetail]]

### ProgramName
- **Type**: typing.Optional[str]


# MultiplexProgramChannelDestinationSettings

### MultiplexId
- **Type**: typing.Optional[str]

### ProgramName
- **Type**: typing.Optional[str]


# MultiplexProgramPacketIdentifiersMap

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


# MultiplexProgramPacketIdentifiersMapOutput

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


# MultiplexProgramPipelineDetail

### ActiveChannelPipeline
- **Type**: typing.Optional[str]

### PipelineId
- **Type**: typing.Optional[str]


# MultiplexProgramServiceDescriptor

### ProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# MultiplexProgramSettings

### ProgramNumber
- **Type**: <class 'int'>
- **Required**: Yes

### PreferredChannelPipeline
- **Type**: typing.Optional[typing.Literal['CURRENTLY_ACTIVE', 'PIPELINE_0', 'PIPELINE_1']]

### ServiceDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramServiceDescriptor]

### VideoSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexVideoSettings]


# MultiplexProgramSummary

### ChannelId
- **Type**: typing.Optional[str]

### ProgramName
- **Type**: typing.Optional[str]


# MultiplexSettings

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


# MultiplexSettingsSummary

### TransportStreamBitrate
- **Type**: typing.Optional[int]


# MultiplexStatmuxVideoSettings

### MaximumBitrate
- **Type**: typing.Optional[int]

### MinimumBitrate
- **Type**: typing.Optional[int]

### Priority
- **Type**: typing.Optional[int]


# MultiplexSummary

### Arn
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### Id
- **Type**: typing.Optional[str]

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexSettingsSummary]

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


# MultiplexVideoSettings

### ConstantBitrate
- **Type**: typing.Optional[int]

### StatmuxSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexStatmuxVideoSettings]


# NetworkInputSettings

### HlsInputSettings
- **Type**: <class 'NoneType'>

### ServerValidation
- **Type**: typing.Optional[typing.Literal['CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME', 'CHECK_CRYPTOGRAPHY_ONLY']]

### MulticastInputSettings
- **Type**: <class 'NoneType'>


# NielsenCBET

### CbetCheckDigitString
- **Type**: <class 'str'>
- **Required**: Yes

### CbetStepaside
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### Csid
- **Type**: <class 'str'>
- **Required**: Yes


# NielsenConfiguration

### DistributorId
- **Type**: typing.Optional[str]

### NielsenPcmToId3Tagging
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# NielsenNaesIiNw

### CheckDigitString
- **Type**: <class 'str'>
- **Required**: Yes

### Sid
- **Type**: <class 'float'>
- **Required**: Yes

### Timezone
- **Type**: typing.Optional[typing.Literal['AMERICA_PUERTO_RICO', 'US_ALASKA', 'US_ARIZONA', 'US_CENTRAL', 'US_EASTERN', 'US_HAWAII', 'US_MOUNTAIN', 'US_PACIFIC', 'US_SAMOA', 'UTC']]


# NielsenWatermarksSettings

### NielsenCbetSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.NielsenCBET]

### NielsenDistributionType
- **Type**: typing.Optional[typing.Literal['FINAL_DISTRIBUTOR', 'PROGRAM_CONTENT']]

### NielsenNaesIiNwSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.NielsenNaesIiNw]


# NodeInterfaceMapping

### LogicalInterfaceName
- **Type**: typing.Optional[str]

### NetworkInterfaceMode
- **Type**: typing.Optional[typing.Literal['BRIDGE', 'NAT']]

### PhysicalInterfaceName
- **Type**: typing.Optional[str]


# NodeInterfaceMappingCreateRequest

### LogicalInterfaceName
- **Type**: typing.Optional[str]

### NetworkInterfaceMode
- **Type**: typing.Optional[typing.Literal['BRIDGE', 'NAT']]

### PhysicalInterfaceName
- **Type**: typing.Optional[str]


# Offering

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ReservationResourceSpecification]

### UsagePrice
- **Type**: typing.Optional[float]


# Output

### OutputSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputSettings'>
- **Required**: Yes

### AudioDescriptionNames
- **Type**: typing.Optional[typing.List[str]]

### CaptionDescriptionNames
- **Type**: typing.Optional[typing.List[str]]

### OutputName
- **Type**: typing.Optional[str]

### VideoDescriptionName
- **Type**: typing.Optional[str]


# OutputDestination

### Id
- **Type**: typing.Optional[str]

### MediaPackageSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaPackageOutputDestinationSettings]]

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramChannelDestinationSettings]

### Settings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationSettings]]

### SrtSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.SrtOutputDestinationSettings]]


# OutputDestinationOutput

### Id
- **Type**: typing.Optional[str]

### MediaPackageSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaPackageOutputDestinationSettings]]

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramChannelDestinationSettings]

### Settings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationSettings]]

### SrtSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.SrtOutputDestinationSettings]]


# OutputDestinationSettings

### PasswordParam
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# OutputGroup

### OutputGroupSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputGroupSettings'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Output]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# OutputGroupOutput

### OutputGroupSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputGroupSettingsOutput'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Extra]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# OutputGroupSettings

### ArchiveGroupSettings
- **Type**: <class 'NoneType'>

### FrameCaptureGroupSettings
- **Type**: <class 'NoneType'>

### HlsGroupSettings
- **Type**: <class 'NoneType'>

### MediaPackageGroupSettings
- **Type**: <class 'NoneType'>

### MsSmoothGroupSettings
- **Type**: <class 'NoneType'>

### MultiplexGroupSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### RtmpGroupSettings
- **Type**: <class 'NoneType'>

### UdpGroupSettings
- **Type**: <class 'NoneType'>

### CmafIngestGroupSettings
- **Type**: <class 'NoneType'>

### SrtGroupSettings
- **Type**: <class 'NoneType'>


# OutputGroupSettingsOutput

### ArchiveGroupSettings
- **Type**: <class 'NoneType'>

### FrameCaptureGroupSettings
- **Type**: <class 'NoneType'>

### HlsGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.HlsGroupSettingsOutput]

### MediaPackageGroupSettings
- **Type**: <class 'NoneType'>

### MsSmoothGroupSettings
- **Type**: <class 'NoneType'>

### MultiplexGroupSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### RtmpGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.RtmpGroupSettingsOutput]

### UdpGroupSettings
- **Type**: <class 'NoneType'>

### CmafIngestGroupSettings
- **Type**: <class 'NoneType'>

### SrtGroupSettings
- **Type**: <class 'NoneType'>


# OutputLocationRef

### DestinationRefId
- **Type**: typing.Optional[str]


# OutputLockingSettings

### EpochLockingSettings
- **Type**: <class 'NoneType'>

### PipelineLockingSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# OutputLockingSettingsOutput

### EpochLockingSettings
- **Type**: <class 'NoneType'>

### PipelineLockingSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# OutputSettings

### ArchiveOutputSettings
- **Type**: <class 'NoneType'>

### FrameCaptureOutputSettings
- **Type**: <class 'NoneType'>

### HlsOutputSettings
- **Type**: <class 'NoneType'>

### MediaPackageOutputSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### MsSmoothOutputSettings
- **Type**: <class 'NoneType'>

### MultiplexOutputSettings
- **Type**: <class 'NoneType'>

### RtmpOutputSettings
- **Type**: <class 'NoneType'>

### UdpOutputSettings
- **Type**: <class 'NoneType'>

### CmafIngestOutputSettings
- **Type**: <class 'NoneType'>

### SrtOutputSettings
- **Type**: <class 'NoneType'>


# OutputSettingsOutput

### ArchiveOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ArchiveOutputSettingsOutput]

### FrameCaptureOutputSettings
- **Type**: <class 'NoneType'>

### HlsOutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.HlsOutputSettingsOutput]

### MediaPackageOutputSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### MsSmoothOutputSettings
- **Type**: <class 'NoneType'>

### MultiplexOutputSettings
- **Type**: <class 'NoneType'>

### RtmpOutputSettings
- **Type**: <class 'NoneType'>

### UdpOutputSettings
- **Type**: <class 'NoneType'>

### CmafIngestOutputSettings
- **Type**: <class 'NoneType'>

### SrtOutputSettings
- **Type**: <class 'NoneType'>


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PauseStateScheduleActionSettings

### Pipelines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.PipelinePauseStateSettings]]


# PauseStateScheduleActionSettingsOutput

### Pipelines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.PipelinePauseStateSettings]]


# PipelineDetail

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionResponse]


# PipelinePauseStateSettings

### PipelineId
- **Type**: typing.Literal['PIPELINE_0', 'PIPELINE_1']
- **Required**: Yes


# PurchaseOfferingRequest

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### OfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### RenewalSettings
- **Type**: <class 'NoneType'>

### RequestId
- **Type**: typing.Optional[str]

### Start
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PurchaseOfferingResponse

### Reservation
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Reservation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# RebootInputDeviceRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]


# RejectInputDeviceTransferRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# RemixSettings

### ChannelMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioChannelMapping]
- **Required**: Yes

### ChannelsIn
- **Type**: typing.Optional[int]

### ChannelsOut
- **Type**: typing.Optional[int]


# RemixSettingsOutput

### ChannelMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.AudioChannelMappingOutput]
- **Required**: Yes

### ChannelsIn
- **Type**: typing.Optional[int]

### ChannelsOut
- **Type**: typing.Optional[int]


# RenewalSettings

### AutomaticRenewal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'UNAVAILABLE']]

### RenewalCount
- **Type**: typing.Optional[int]


# Reservation

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
- **Type**: <class 'NoneType'>

### ReservationId
- **Type**: typing.Optional[str]

### ResourceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ReservationResourceSpecification]

### Start
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELED', 'DELETED', 'EXPIRED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### UsagePrice
- **Type**: typing.Optional[float]


# ReservationResourceSpecification

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


# ResponseMetadata

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


# RestartChannelPipelinesRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineIds
- **Type**: typing.Optional[typing.List[typing.Literal['PIPELINE_0', 'PIPELINE_1']]]


# RestartChannelPipelinesResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.CdiInputSpecification'>
- **Required**: Yes

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationOutput]
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEgressEndpoint]
- **Required**: Yes

### EncoderSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.EncoderSettingsOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachmentOutput]
- **Required**: Yes

### InputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSpecification'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes

### Maintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MaintenanceStatus'>
- **Required**: Yes

### MaintenanceStatus
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.PipelineDetail]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.VpcOutputSettingsDescription'>
- **Required**: Yes

### AnywhereSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeAnywhereSettings'>
- **Required**: Yes

### ChannelEngineVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# Route

### Cidr
- **Type**: typing.Optional[str]

### Gateway
- **Type**: typing.Optional[str]


# RouteCreateRequest

### Cidr
- **Type**: typing.Optional[str]

### Gateway
- **Type**: typing.Optional[str]


# RouteUpdateRequest

### Cidr
- **Type**: typing.Optional[str]

### Gateway
- **Type**: typing.Optional[str]


# RtmpGroupSettings

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


# RtmpGroupSettingsOutput

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


# RtmpOutputSettings

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
- **Required**: Yes

### CertificateMode
- **Type**: typing.Optional[typing.Literal['SELF_SIGNED', 'VERIFY_AUTHENTICITY']]

### ConnectionRetryInterval
- **Type**: typing.Optional[int]

### NumRetries
- **Type**: typing.Optional[int]


# ScheduleAction

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleActionSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleActionSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleActionSettingsOutput]
- **Required**: Yes

### ScheduleActionStartSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleActionStartSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleActionStartSettingsOutput]
- **Required**: Yes


# ScheduleActionOutput

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleActionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleActionSettingsOutput'>
- **Required**: Yes

### ScheduleActionStartSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ScheduleActionStartSettingsOutput'>
- **Required**: Yes


# ScheduleActionSettings

### HlsId3SegmentTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.HlsId3SegmentTaggingScheduleActionSettings]

### HlsTimedMetadataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.HlsTimedMetadataScheduleActionSettings]

### InputPrepareSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputPrepareScheduleActionSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.InputPrepareScheduleActionSettingsOutput, NoneType]

### InputSwitchSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSwitchScheduleActionSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSwitchScheduleActionSettingsOutput, NoneType]

### MotionGraphicsImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MotionGraphicsActivateScheduleActionSettings]

### MotionGraphicsImageDeactivateSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### PauseStateSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.PauseStateScheduleActionSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.PauseStateScheduleActionSettingsOutput, NoneType]

### Scte35InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35InputScheduleActionSettings]

### Scte35ReturnToNetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35ReturnToNetworkScheduleActionSettings]

### Scte35SpliceInsertSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35SpliceInsertScheduleActionSettings]

### Scte35TimeSignalSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35TimeSignalScheduleActionSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35TimeSignalScheduleActionSettingsOutput, NoneType]

### StaticImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.StaticImageActivateScheduleActionSettings]

### StaticImageDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.StaticImageDeactivateScheduleActionSettings]

### StaticImageOutputActivateSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.StaticImageOutputActivateScheduleActionSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.StaticImageOutputActivateScheduleActionSettingsOutput, NoneType]

### StaticImageOutputDeactivateSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.StaticImageOutputDeactivateScheduleActionSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.StaticImageOutputDeactivateScheduleActionSettingsOutput, NoneType]

### Id3SegmentTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Id3SegmentTaggingScheduleActionSettings]

### TimedMetadataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.TimedMetadataScheduleActionSettings]


# ScheduleActionSettingsOutput

### HlsId3SegmentTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.HlsId3SegmentTaggingScheduleActionSettings]

### HlsTimedMetadataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.HlsTimedMetadataScheduleActionSettings]

### InputPrepareSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputPrepareScheduleActionSettingsOutput]

### InputSwitchSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSwitchScheduleActionSettingsOutput]

### MotionGraphicsImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MotionGraphicsActivateScheduleActionSettings]

### MotionGraphicsImageDeactivateSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### PauseStateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.PauseStateScheduleActionSettingsOutput]

### Scte35InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35InputScheduleActionSettings]

### Scte35ReturnToNetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35ReturnToNetworkScheduleActionSettings]

### Scte35SpliceInsertSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35SpliceInsertScheduleActionSettings]

### Scte35TimeSignalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35TimeSignalScheduleActionSettingsOutput]

### StaticImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.StaticImageActivateScheduleActionSettings]

### StaticImageDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.StaticImageDeactivateScheduleActionSettings]

### StaticImageOutputActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.StaticImageOutputActivateScheduleActionSettingsOutput]

### StaticImageOutputDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.StaticImageOutputDeactivateScheduleActionSettingsOutput]

### Id3SegmentTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Id3SegmentTaggingScheduleActionSettings]

### TimedMetadataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.TimedMetadataScheduleActionSettings]


# ScheduleActionStartSettings

### FixedModeScheduleActionStartSettings
- **Type**: <class 'NoneType'>

### FollowModeScheduleActionStartSettings
- **Type**: <class 'NoneType'>

### ImmediateModeScheduleActionStartSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ScheduleActionStartSettingsOutput

### FixedModeScheduleActionStartSettings
- **Type**: <class 'NoneType'>

### FollowModeScheduleActionStartSettings
- **Type**: <class 'NoneType'>

### ImmediateModeScheduleActionStartSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# Scte20SourceSettings

### Convert608To708
- **Type**: typing.Optional[typing.Literal['DISABLED', 'UPCONVERT']]

### Source608ChannelNumber
- **Type**: typing.Optional[int]


# Scte27SourceSettings

### OcrLanguage
- **Type**: typing.Optional[typing.Literal['DEU', 'ENG', 'FRA', 'NLD', 'POR', 'SPA']]

### Pid
- **Type**: typing.Optional[int]


# Scte35DeliveryRestrictions

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


# Scte35Descriptor

### Scte35DescriptorSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35DescriptorSettings'>
- **Required**: Yes


# Scte35DescriptorSettings

### SegmentationDescriptorScte35DescriptorSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35SegmentationDescriptor'>
- **Required**: Yes


# Scte35InputScheduleActionSettings

### Mode
- **Type**: typing.Literal['FIXED', 'FOLLOW_ACTIVE']
- **Required**: Yes

### InputAttachmentNameReference
- **Type**: typing.Optional[str]


# Scte35ReturnToNetworkScheduleActionSettings

### SpliceEventId
- **Type**: <class 'int'>
- **Required**: Yes


# Scte35SegmentationDescriptor

### SegmentationCancelIndicator
- **Type**: typing.Literal['SEGMENTATION_EVENT_CANCELED', 'SEGMENTATION_EVENT_NOT_CANCELED']
- **Required**: Yes

### SegmentationEventId
- **Type**: <class 'int'>
- **Required**: Yes

### DeliveryRestrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35DeliveryRestrictions]

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


# Scte35SpliceInsert

### AdAvailOffset
- **Type**: typing.Optional[int]

### NoRegionalBlackoutFlag
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'IGNORE']]

### WebDeliveryAllowedFlag
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'IGNORE']]


# Scte35SpliceInsertScheduleActionSettings

### SpliceEventId
- **Type**: <class 'int'>
- **Required**: Yes

### Duration
- **Type**: typing.Optional[int]


# Scte35TimeSignalApos

### AdAvailOffset
- **Type**: typing.Optional[int]

### NoRegionalBlackoutFlag
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'IGNORE']]

### WebDeliveryAllowedFlag
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'IGNORE']]


# Scte35TimeSignalScheduleActionSettings

### Scte35Descriptors
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35Descriptor]
- **Required**: Yes


# Scte35TimeSignalScheduleActionSettingsOutput

### Scte35Descriptors
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Scte35Descriptor]
- **Required**: Yes


# SignalMapSummary

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


# SrtCallerDecryption

### Algorithm
- **Type**: typing.Optional[typing.Literal['AES128', 'AES192', 'AES256']]

### PassphraseSecretArn
- **Type**: typing.Optional[str]


# SrtCallerDecryptionRequest

### Algorithm
- **Type**: typing.Optional[typing.Literal['AES128', 'AES192', 'AES256']]

### PassphraseSecretArn
- **Type**: typing.Optional[str]


# SrtCallerSource

### Decryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.SrtCallerDecryption]

### MinimumLatency
- **Type**: typing.Optional[int]

### SrtListenerAddress
- **Type**: typing.Optional[str]

### SrtListenerPort
- **Type**: typing.Optional[str]

### StreamId
- **Type**: typing.Optional[str]


# SrtCallerSourceRequest

### Decryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.SrtCallerDecryptionRequest]

### MinimumLatency
- **Type**: typing.Optional[int]

### SrtListenerAddress
- **Type**: typing.Optional[str]

### SrtListenerPort
- **Type**: typing.Optional[str]

### StreamId
- **Type**: typing.Optional[str]


# SrtGroupSettings

### InputLossAction
- **Type**: typing.Optional[typing.Literal['DROP_PROGRAM', 'DROP_TS', 'EMIT_PROGRAM']]


# SrtOutputDestinationSettings

### EncryptionPassphraseSecretArn
- **Type**: typing.Optional[str]

### StreamId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# SrtOutputSettings

### ContainerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.UdpContainerSettings'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
- **Required**: Yes

### BufferMsec
- **Type**: typing.Optional[int]

### EncryptionType
- **Type**: typing.Optional[typing.Literal['AES128', 'AES192', 'AES256']]

### Latency
- **Type**: typing.Optional[int]


# SrtSettings

### SrtCallerSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.SrtCallerSource]]


# SrtSettingsRequest

### SrtCallerSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.SrtCallerSourceRequest]]


# StandardHlsSettings

### M3u8Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.M3u8Settings'>
- **Required**: Yes

### AudioRenditionSets
- **Type**: typing.Optional[str]


# StartChannelRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# StartChannelResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.CdiInputSpecification'>
- **Required**: Yes

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationOutput]
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEgressEndpoint]
- **Required**: Yes

### EncoderSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.EncoderSettingsOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachmentOutput]
- **Required**: Yes

### InputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSpecification'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes

### Maintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MaintenanceStatus'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.PipelineDetail]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.VpcOutputSettingsDescription'>
- **Required**: Yes

### AnywhereSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeAnywhereSettings'>
- **Required**: Yes

### ChannelEngineVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# StartDeleteMonitorDeploymentRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartDeleteMonitorDeploymentResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResource]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastDiscoveredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSuccessfulMonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.SuccessfulMonitorDeployment'>
- **Required**: Yes

### MediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResource]
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitorChangesPendingDeployment
- **Type**: <class 'bool'>
- **Required**: Yes

### MonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MonitorDeployment'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# StartInputDeviceMaintenanceWindowRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# StartInputDeviceRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# StartMonitorDeploymentRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# StartMonitorDeploymentResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResource]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastDiscoveredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSuccessfulMonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.SuccessfulMonitorDeployment'>
- **Required**: Yes

### MediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResource]
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitorChangesPendingDeployment
- **Type**: <class 'bool'>
- **Required**: Yes

### MonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MonitorDeployment'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# StartMultiplexRequest

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes


# StartMultiplexResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexOutputDestination]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# StartTimecode

### Timecode
- **Type**: typing.Optional[str]


# StartUpdateSignalMapRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchAlarmTemplateGroupIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### Description
- **Type**: typing.Optional[str]

### DiscoveryEntryPointArn
- **Type**: typing.Optional[str]

### EventBridgeRuleTemplateGroupIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### ForceRediscovery
- **Type**: typing.Optional[bool]

### Name
- **Type**: typing.Optional[str]


# StartUpdateSignalMapResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResource]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastDiscoveredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSuccessfulMonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.SuccessfulMonitorDeployment'>
- **Required**: Yes

### MediaResourceMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaResource]
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitorChangesPendingDeployment
- **Type**: <class 'bool'>
- **Required**: Yes

### MonitorDeployment
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MonitorDeployment'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# StaticImageActivateScheduleActionSettings

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation'>
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


# StaticImageDeactivateScheduleActionSettings

### FadeOut
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]


# StaticImageOutputActivateScheduleActionSettings

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation'>
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


# StaticImageOutputActivateScheduleActionSettingsOutput

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation'>
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


# StaticImageOutputDeactivateScheduleActionSettings

### OutputNames
- **Type**: typing.List[str]
- **Required**: Yes

### FadeOut
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]


# StaticImageOutputDeactivateScheduleActionSettingsOutput

### OutputNames
- **Type**: typing.List[str]
- **Required**: Yes

### FadeOut
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]


# StaticKeySettings

### StaticKeyValue
- **Type**: <class 'str'>
- **Required**: Yes

### KeyProviderServer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputLocation]


# StopChannelRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# StopChannelResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.CdiInputSpecification'>
- **Required**: Yes

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationOutput]
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEgressEndpoint]
- **Required**: Yes

### EncoderSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.EncoderSettingsOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachmentOutput]
- **Required**: Yes

### InputSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSpecification'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes

### Maintenance
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MaintenanceStatus'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.PipelineDetail]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.VpcOutputSettingsDescription'>
- **Required**: Yes

### AnywhereSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.DescribeAnywhereSettings'>
- **Required**: Yes

### ChannelEngineVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# StopInputDeviceRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# StopMultiplexRequest

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes


# StopMultiplexResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexOutputDestination]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# StopTimecode

### LastFrameClippingBehavior
- **Type**: typing.Optional[typing.Literal['EXCLUDE_LAST_FRAME', 'INCLUDE_LAST_FRAME']]

### Timecode
- **Type**: typing.Optional[str]


# SuccessfulMonitorDeployment

### DetailsUri
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DEPLOYMENT_COMPLETE', 'DEPLOYMENT_FAILED', 'DEPLOYMENT_IN_PROGRESS', 'DRY_RUN_DEPLOYMENT_COMPLETE', 'DRY_RUN_DEPLOYMENT_FAILED', 'DRY_RUN_DEPLOYMENT_IN_PROGRESS', 'NOT_DEPLOYED']
- **Required**: Yes


# TeletextSourceSettings

### OutputRectangle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.CaptionRectangle]

### PageNumber
- **Type**: typing.Optional[str]


# TemporalFilterSettings

### PostFilterSharpening
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'ENABLED']]

### Strength
- **Type**: typing.Optional[typing.Literal['AUTO', 'STRENGTH_1', 'STRENGTH_10', 'STRENGTH_11', 'STRENGTH_12', 'STRENGTH_13', 'STRENGTH_14', 'STRENGTH_15', 'STRENGTH_16', 'STRENGTH_2', 'STRENGTH_3', 'STRENGTH_4', 'STRENGTH_5', 'STRENGTH_6', 'STRENGTH_7', 'STRENGTH_8', 'STRENGTH_9']]


# Thumbnail

### Body
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### ThumbnailType
- **Type**: typing.Optional[typing.Literal['CURRENT_ACTIVE', 'UNSPECIFIED']]

### TimeStamp
- **Type**: typing.Optional[datetime.datetime]


# ThumbnailConfiguration

### State
- **Type**: typing.Literal['AUTO', 'DISABLED']
- **Required**: Yes


# ThumbnailDetail

### PipelineId
- **Type**: typing.Optional[str]

### Thumbnails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Thumbnail]]


# TimecodeBurninSettings

### FontSize
- **Type**: typing.Literal['EXTRA_SMALL_10', 'LARGE_48', 'MEDIUM_32', 'SMALL_16']
- **Required**: Yes

### Position
- **Type**: typing.Literal['BOTTOM_CENTER', 'BOTTOM_LEFT', 'BOTTOM_RIGHT', 'MIDDLE_CENTER', 'MIDDLE_LEFT', 'MIDDLE_RIGHT', 'TOP_CENTER', 'TOP_LEFT', 'TOP_RIGHT']
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# TimecodeConfig

### Source
- **Type**: typing.Literal['EMBEDDED', 'SYSTEMCLOCK', 'ZEROBASED']
- **Required**: Yes

### SyncThreshold
- **Type**: typing.Optional[int]


# TimedMetadataScheduleActionSettings

### Id3
- **Type**: <class 'str'>
- **Required**: Yes


# TransferInputDeviceRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetCustomerId
- **Type**: typing.Optional[str]

### TargetRegion
- **Type**: typing.Optional[str]

### TransferMessage
- **Type**: typing.Optional[str]


# TransferringInputDeviceSummary

### Id
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### TargetCustomerId
- **Type**: typing.Optional[str]

### TransferType
- **Type**: typing.Optional[typing.Literal['INCOMING', 'OUTGOING']]


# TtmlDestinationSettings

### StyleControl
- **Type**: typing.Optional[typing.Literal['PASSTHROUGH', 'USE_CONFIGURED']]


# UdpContainerSettings

### M2tsSettings
- **Type**: <class 'NoneType'>


# UdpGroupSettings

### InputLossAction
- **Type**: typing.Optional[typing.Literal['DROP_PROGRAM', 'DROP_TS', 'EMIT_PROGRAM']]

### TimedMetadataId3Frame
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIV', 'TDRL']]

### TimedMetadataId3Period
- **Type**: typing.Optional[int]


# UdpOutputSettings

### ContainerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.UdpContainerSettings'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputLocationRef'>
- **Required**: Yes

### BufferMsec
- **Type**: typing.Optional[int]

### FecOutputSettings
- **Type**: <class 'NoneType'>


# UpdateAccountConfigurationRequest

### AccountConfiguration
- **Type**: <class 'NoneType'>


# UpdateAccountConfigurationResponse

### AccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.AccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateChannelClassRequest

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestination, aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationOutput]]]


# UpdateChannelClassResponse

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Channel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateChannelPlacementGroupRequest

### ChannelPlacementGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Nodes
- **Type**: typing.Optional[typing.List[str]]


# UpdateChannelPlacementGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateChannelRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: <class 'NoneType'>

### Destinations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestination, aws_resource_validator.pydantic_models.medialive.medialive_classes.OutputDestinationOutput]]]

### EncoderSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.EncoderSettings, aws_resource_validator.pydantic_models.medialive.medialive_classes.EncoderSettingsOutput, NoneType]

### InputAttachments
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachment, aws_resource_validator.pydantic_models.medialive.medialive_classes.InputAttachmentOutput]]]

### InputSpecification
- **Type**: <class 'NoneType'>

### LogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'DISABLED', 'ERROR', 'INFO', 'WARNING']]

### Maintenance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MaintenanceUpdateSettings]

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ChannelEngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ChannelEngineVersionRequest]

### DryRun
- **Type**: typing.Optional[bool]


# UpdateChannelResponse

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Channel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCloudWatchAlarmTemplateGroupRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateCloudWatchAlarmTemplateGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCloudWatchAlarmTemplateRequest

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


# UpdateCloudWatchAlarmTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### NetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.ClusterNetworkSettingsUpdateRequest]


# UpdateClusterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ClusterNetworkSettings'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEventBridgeRuleTemplateGroupRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateEventBridgeRuleTemplateGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEventBridgeRuleTemplateRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EventTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.EventBridgeRuleTemplateTarget]]

### EventType
- **Type**: typing.Optional[typing.Literal['MEDIACONNECT_ALERT', 'MEDIACONNECT_FLOW_STATUS_CHANGE', 'MEDIACONNECT_OUTPUT_HEALTH', 'MEDIACONNECT_SOURCE_HEALTH', 'MEDIALIVE_CHANNEL_ALERT', 'MEDIALIVE_CHANNEL_INPUT_CHANGE', 'MEDIALIVE_CHANNEL_STATE_CHANGE', 'MEDIALIVE_MULTIPLEX_ALERT', 'MEDIALIVE_MULTIPLEX_STATE_CHANGE', 'MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION', 'MEDIAPACKAGE_INPUT_NOTIFICATION', 'MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION', 'SIGNAL_MAP_ACTIVE_ALARM']]

### GroupIdentifier
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# UpdateEventBridgeRuleTemplateResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.EventBridgeRuleTemplateTarget]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInputDeviceRequest

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### HdDeviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceConfigurableSettings]

### Name
- **Type**: typing.Optional[str]

### UhdDeviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceConfigurableSettings]

### AvailabilityZone
- **Type**: typing.Optional[str]


# UpdateInputDeviceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['CONNECTED', 'DISCONNECTED']
- **Required**: Yes

### DeviceSettingsSyncState
- **Type**: typing.Literal['SYNCED', 'SYNCING']
- **Required**: Yes

### DeviceUpdateStatus
- **Type**: typing.Literal['NOT_UP_TO_DATE', 'UPDATING', 'UP_TO_DATE']
- **Required**: Yes

### HdDeviceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceHdSettings'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MacAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceNetworkSettings'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['HD', 'UHD']
- **Required**: Yes

### UhdDeviceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceUhdSettings'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### MedialiveInputArns
- **Type**: typing.List[str]
- **Required**: Yes

### OutputType
- **Type**: typing.Literal['MEDIACONNECT_FLOW', 'MEDIALIVE_INPUT', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInputRequest

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDestinationRequest]]

### InputDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputDeviceRequest]]

### InputSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### MediaConnectFlows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.MediaConnectFlowRequest]]

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSourceRequest]]

### SrtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.SrtSettingsRequest]

### MulticastSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.MulticastSettingsUpdateRequest]


# UpdateInputResponse

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Input'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInputSecurityGroupRequest

### InputSecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### WhitelistRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.InputWhitelistRuleCidr]]


# UpdateInputSecurityGroupResponse

### SecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.InputSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMultiplexProgramRequest

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexProgramSettings
- **Type**: <class 'NoneType'>


# UpdateMultiplexProgramResponse

### MultiplexProgram
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgram'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMultiplexRequest

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: <class 'NoneType'>

### Name
- **Type**: typing.Optional[str]

### PacketIdentifiersMapping
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramPacketIdentifiersMap, aws_resource_validator.pydantic_models.medialive.medialive_classes.MultiplexProgramPacketIdentifiersMapOutput]]]


# UpdateMultiplexResponse

### Multiplex
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Multiplex'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNetworkRequest

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### IpPools
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.IpPoolUpdateRequest]]

### Name
- **Type**: typing.Optional[str]

### Routes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.RouteUpdateRequest]]


# UpdateNetworkResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.IpPool]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.Route]
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'IDLE', 'IN_USE', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNodeRequest

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


# UpdateNodeResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.NodeInterfaceMapping]
- **Required**: Yes

### Role
- **Type**: typing.Literal['ACTIVE', 'BACKUP']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNodeStateRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAINING']]


# UpdateNodeStateResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive.medialive_classes.NodeInterfaceMapping]
- **Required**: Yes

### Role
- **Type**: typing.Literal['ACTIVE', 'BACKUP']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVATION_FAILED', 'ACTIVE', 'CREATED', 'DEREGISTERED', 'DEREGISTERING', 'DEREGISTRATION_FAILED', 'DRAINING', 'IN_USE', 'READY', 'READY_TO_ACTIVATE', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateReservationRequest

### ReservationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### RenewalSettings
- **Type**: <class 'NoneType'>


# UpdateReservationResponse

### Reservation
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.Reservation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive.medialive_classes.ResponseMetadata'>
- **Required**: Yes


# VideoBlackFailoverSettings

### BlackDetectThreshold
- **Type**: typing.Optional[float]

### VideoBlackThresholdMsec
- **Type**: typing.Optional[int]


# VideoCodecSettings

### FrameCaptureSettings
- **Type**: <class 'NoneType'>

### H264Settings
- **Type**: <class 'NoneType'>

### H265Settings
- **Type**: <class 'NoneType'>

### Mpeg2Settings
- **Type**: <class 'NoneType'>

### Av1Settings
- **Type**: <class 'NoneType'>


# VideoCodecSettingsOutput

### FrameCaptureSettings
- **Type**: <class 'NoneType'>

### H264Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.H264SettingsOutput]

### H265Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.H265SettingsOutput]

### Mpeg2Settings
- **Type**: <class 'NoneType'>

### Av1Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.Av1SettingsOutput]


# VideoDescription

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.VideoCodecSettings]

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


# VideoDescriptionOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.VideoCodecSettingsOutput]

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


# VideoSelector

### ColorSpace
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'HDR10', 'HLG_2020', 'REC_601', 'REC_709']]

### ColorSpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.VideoSelectorColorSpaceSettings]

### ColorSpaceUsage
- **Type**: typing.Optional[typing.Literal['FALLBACK', 'FORCE']]

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive.medialive_classes.VideoSelectorSettings]


# VideoSelectorColorSpaceSettings

### Hdr10Settings
- **Type**: <class 'NoneType'>


# VideoSelectorPid

### Pid
- **Type**: typing.Optional[int]


# VideoSelectorProgramId

### ProgramId
- **Type**: typing.Optional[int]


# VideoSelectorSettings

### VideoSelectorPid
- **Type**: <class 'NoneType'>

### VideoSelectorProgramId
- **Type**: <class 'NoneType'>


# VpcOutputSettings

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### PublicAddressAllocationIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# VpcOutputSettingsDescription

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### NetworkInterfaceIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WavSettings

### BitDepth
- **Type**: typing.Optional[float]

### CodingMode
- **Type**: typing.Optional[typing.Literal['CODING_MODE_1_0', 'CODING_MODE_2_0', 'CODING_MODE_4_0', 'CODING_MODE_8_0']]

### SampleRate
- **Type**: typing.Optional[float]


# WebvttDestinationSettings

### StyleControl
- **Type**: typing.Optional[typing.Literal['NO_STYLE_DATA', 'PASSTHROUGH']]


