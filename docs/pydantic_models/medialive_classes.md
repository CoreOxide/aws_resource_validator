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


# AcceptInputDeviceTransferRequestRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# AccountConfigurationTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]


# AncillarySourceSettingsTypeDef

### SourceAncillaryChannelNumber
- **Type**: typing.Optional[int]


# ArchiveCdnSettingsTypeDef

### ArchiveS3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.ArchiveS3SettingsTypeDef]


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


# AudioSelectorExtraOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioSelectorSettingsExtraOutputTypeDef]


# AudioSelectorOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioSelectorSettingsOutputTypeDef]


# AudioSelectorSettingsExtraOutputTypeDef

### AudioHlsRenditionSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioHlsRenditionSelectionTypeDef]

### AudioLanguageSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioLanguageSelectionTypeDef]

### AudioPidSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioPidSelectionTypeDef]

### AudioTrackSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioTrackSelectionExtraOutputTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioTrackSelectionTypeDef]


# AudioSelectorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioSelectorSettingsTypeDef]


# AudioSilenceFailoverSettingsTypeDef

### AudioSelectorName
- **Type**: <class 'str'>
- **Required**: Yes

### AudioSilenceThresholdMsec
- **Type**: typing.Optional[int]


# AudioTrackSelectionExtraOutputTypeDef

### Tracks
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.AudioTrackTypeDef]
- **Required**: Yes

### DolbyEDecode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AudioDolbyEDecodeTypeDef]


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


# AudioTrackTypeDef

### Track
- **Type**: <class 'int'>
- **Required**: Yes


# AudioWatermarkSettingsTypeDef

### NielsenWatermarksSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.NielsenWatermarksSettingsTypeDef]


# AutomaticInputFailoverSettingsExtraOutputTypeDef

### SecondaryInputId
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorClearTimeMsec
- **Type**: typing.Optional[int]

### FailoverConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.FailoverConditionTypeDef]]

### InputPreference
- **Type**: typing.Optional[typing.Literal['EQUAL_INPUT_PREFERENCE', 'PRIMARY_INPUT_PREFERRED']]


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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteRequestRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionTypeDef]
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


# BatchStartRequestRequestTypeDef

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


# BatchStopRequestRequestTypeDef

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


# BatchUpdateScheduleRequestRequestTypeDef

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


# CancelInputDeviceTransferRequestRequestTypeDef

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


# CaptionSelectorExtraOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[str]

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CaptionSelectorSettingsExtraOutputTypeDef]


# CaptionSelectorOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[str]

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CaptionSelectorSettingsOutputTypeDef]


# CaptionSelectorSettingsExtraOutputTypeDef

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


# CaptionSelectorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[str]

### SelectorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CaptionSelectorSettingsTypeDef]


# CdiInputSpecificationTypeDef

### Resolution
- **Type**: typing.Optional[typing.Literal['FHD', 'HD', 'SD', 'UHD']]


# ChannelEgressEndpointTypeDef

### SourceIp
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


# ClaimDeviceRequestRequestTypeDef

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
- **Type**: typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'S3_BUCKET']
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


# CreateChannelRequestRequestTypeDef

### CdiInputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef]

### ChannelClass
- **Type**: typing.Optional[typing.Literal['SINGLE_PIPELINE', 'STANDARD']]

### Destinations
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationTypeDef, aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationExtraOutputTypeDef]]]

### EncoderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EncoderSettingsTypeDef]

### InputAttachments
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentTypeDef, aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentExtraOutputTypeDef]]]

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


# CreateChannelResponseTypeDef

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCloudWatchAlarmTemplateGroupRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


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


# CreateCloudWatchAlarmTemplateRequestRequestTypeDef

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
- **Type**: typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'S3_BUCKET']
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
- **Type**: typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'S3_BUCKET']
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


# CreateEventBridgeRuleTemplateGroupRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


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


# CreateEventBridgeRuleTemplateRequestRequestTypeDef

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


# CreateInputRequestRequestTypeDef

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputDestinationRequestTypeDef]]

### InputDevices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceSettingsTypeDef]]

### InputSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### MediaConnectFlows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.MediaConnectFlowRequestTypeDef]]

### Name
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.InputSourceRequestTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_CDI', 'INPUT_DEVICE', 'MEDIACONNECT', 'MP4_FILE', 'RTMP_PULL', 'RTMP_PUSH', 'RTP_PUSH', 'TS_FILE', 'UDP_PUSH', 'URL_PULL']]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputVpcRequestTypeDef]


# CreateInputResponseTypeDef

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInputSecurityGroupRequestRequestTypeDef

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


# CreateMultiplexProgramRequestRequestTypeDef

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


# CreateMultiplexRequestRequestTypeDef

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


# CreatePartnerInputRequestRequestTypeDef

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


# CreateSignalMapRequestRequestTypeDef

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


# CreateTagsRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DeleteChannelRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCloudWatchAlarmTemplateGroupRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCloudWatchAlarmTemplateRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventBridgeRuleTemplateGroupRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventBridgeRuleTemplateRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInputRequestRequestTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInputSecurityGroupRequestRequestTypeDef

### InputSecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiplexProgramRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramPacketIdentifiersMapTypeDef'>
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


# DeleteMultiplexRequestRequestTypeDef

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


# DeleteReservationRequestRequestTypeDef

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


# DeleteScheduleRequestRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSignalMapRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsRequestRequestTypeDef

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


# DescribeChannelRequestChannelCreatedWaitTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelRequestChannelDeletedWaitTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelRequestChannelRunningWaitTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelRequestChannelStoppedWaitTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeChannelRequestRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes


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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInputDeviceRequestRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInputDeviceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputDeviceHdSettingsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputDeviceNetworkSettingsTypeDef'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['HD', 'UHD']
- **Required**: Yes

### UhdDeviceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputDeviceUhdSettingsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInputDeviceThumbnailRequestRequestTypeDef

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


# DescribeInputRequestInputAttachedWaitTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeInputRequestInputDeletedWaitTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeInputRequestInputDetachedWaitTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeInputRequestRequestTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInputResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AttachedChannels
- **Type**: typing.List[str]
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputDestinationTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### InputDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceSettingsTypeDef]
- **Required**: Yes

### InputPartnerIds
- **Type**: typing.List[str]
- **Required**: Yes

### InputSourceType
- **Type**: typing.Literal['DYNAMIC', 'STATIC']
- **Required**: Yes

### MediaConnectFlows
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.MediaConnectFlowTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputSourceTypeDef]
- **Required**: Yes

### State
- **Type**: typing.Literal['ATTACHED', 'CREATING', 'DELETED', 'DELETING', 'DETACHED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Type
- **Type**: typing.Literal['AWS_CDI', 'INPUT_DEVICE', 'MEDIACONNECT', 'MP4_FILE', 'RTMP_PULL', 'RTMP_PUSH', 'RTP_PUSH', 'TS_FILE', 'UDP_PUSH', 'URL_PULL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInputSecurityGroupRequestRequestTypeDef

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


# DescribeMultiplexProgramRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramPacketIdentifiersMapTypeDef'>
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


# DescribeMultiplexRequestMultiplexCreatedWaitTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeMultiplexRequestMultiplexDeletedWaitTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeMultiplexRequestMultiplexRunningWaitTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeMultiplexRequestMultiplexStoppedWaitTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# DescribeMultiplexRequestRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes


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


# DescribeOfferingRequestRequestTypeDef

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


# DescribeReservationRequestRequestTypeDef

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


# DescribeScheduleRequestDescribeSchedulePaginateTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# DescribeScheduleRequestRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeScheduleResponseTypeDef

### ScheduleActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionExtraOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeThumbnailsRequestRequestTypeDef

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

### OutputSdt
- **Type**: typing.Optional[typing.Literal['SDT_FOLLOW', 'SDT_FOLLOW_IF_PRESENT', 'SDT_MANUAL', 'SDT_NONE']]

### RepInterval
- **Type**: typing.Optional[int]

### ServiceName
- **Type**: typing.Optional[str]

### ServiceProviderName
- **Type**: typing.Optional[str]


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


# GetCloudWatchAlarmTemplateGroupRequestRequestTypeDef

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


# GetCloudWatchAlarmTemplateRequestRequestTypeDef

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
- **Type**: typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'S3_BUCKET']
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


# GetEventBridgeRuleTemplateGroupRequestRequestTypeDef

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


# GetEventBridgeRuleTemplateRequestRequestTypeDef

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


# GetSignalMapRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSignalMapRequestSignalMapCreatedWaitTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# GetSignalMapRequestSignalMapMonitorDeletedWaitTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# GetSignalMapRequestSignalMapMonitorDeployedWaitTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.WaiterConfigTypeDef]


# GetSignalMapRequestSignalMapUpdatedWaitTypeDef

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


# InputAttachmentExtraOutputTypeDef

### AutomaticInputFailoverSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AutomaticInputFailoverSettingsExtraOutputTypeDef]

### InputAttachmentName
- **Type**: typing.Optional[str]

### InputId
- **Type**: typing.Optional[str]

### InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSettingsExtraOutputTypeDef]


# InputAttachmentOutputTypeDef

### AutomaticInputFailoverSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AutomaticInputFailoverSettingsOutputTypeDef]

### InputAttachmentName
- **Type**: typing.Optional[str]

### InputId
- **Type**: typing.Optional[str]

### InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSettingsOutputTypeDef]


# InputAttachmentTypeDef

### AutomaticInputFailoverSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AutomaticInputFailoverSettingsTypeDef]

### InputAttachmentName
- **Type**: typing.Optional[str]

### InputId
- **Type**: typing.Optional[str]

### InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSettingsTypeDef]


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


# InputDestinationTypeDef

### Ip
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputDestinationVpcTypeDef]


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

### Arn
- **Type**: typing.Optional[str]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED']]

### DeviceSettingsSyncState
- **Type**: typing.Optional[typing.Literal['SYNCED', 'SYNCING']]

### DeviceUpdateStatus
- **Type**: typing.Optional[typing.Literal['NOT_UP_TO_DATE', 'UPDATING', 'UP_TO_DATE']]

### HdDeviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceHdSettingsTypeDef]

### Id
- **Type**: typing.Optional[str]

### MacAddress
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceNetworkSettingsTypeDef]

### SerialNumber
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['HD', 'UHD']]

### UhdDeviceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceUhdSettingsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### MedialiveInputArns
- **Type**: typing.Optional[typing.List[str]]

### OutputType
- **Type**: typing.Optional[typing.Literal['MEDIACONNECT_FLOW', 'MEDIALIVE_INPUT', 'NONE']]


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


# InputPrepareScheduleActionSettingsExtraOutputTypeDef

### InputAttachmentNameReference
- **Type**: typing.Optional[str]

### InputClippingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputClippingSettingsTypeDef]

### UrlPath
- **Type**: typing.Optional[typing.List[str]]


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


# InputSettingsExtraOutputTypeDef

### AudioSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.AudioSelectorExtraOutputTypeDef]]

### CaptionSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.CaptionSelectorExtraOutputTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.AudioSelectorTypeDef]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.CaptionSelectorTypeDef]]

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


# InputSwitchScheduleActionSettingsExtraOutputTypeDef

### InputAttachmentNameReference
- **Type**: <class 'str'>
- **Required**: Yes

### InputClippingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputClippingSettingsTypeDef]

### UrlPath
- **Type**: typing.Optional[typing.List[str]]


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


# InputTypeDef

### Arn
- **Type**: typing.Optional[str]

### AttachedChannels
- **Type**: typing.Optional[typing.List[str]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputDestinationTypeDef]]

### Id
- **Type**: typing.Optional[str]

### InputClass
- **Type**: typing.Optional[typing.Literal['SINGLE_PIPELINE', 'STANDARD']]

### InputDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputDeviceSettingsTypeDef]]

### InputPartnerIds
- **Type**: typing.Optional[typing.List[str]]

### InputSourceType
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]

### MediaConnectFlows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.MediaConnectFlowTypeDef]]

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.InputSourceTypeDef]]

### State
- **Type**: typing.Optional[typing.Literal['ATTACHED', 'CREATING', 'DELETED', 'DELETING', 'DETACHED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_CDI', 'INPUT_DEVICE', 'MEDIACONNECT', 'MP4_FILE', 'RTMP_PULL', 'RTMP_PUSH', 'RTP_PUSH', 'TS_FILE', 'UDP_PUSH', 'URL_PULL']]


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


# KeyProviderSettingsTypeDef

### StaticKeySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticKeySettingsTypeDef]


# ListChannelsRequestListChannelsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListChannelsRequestRequestTypeDef

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


# ListCloudWatchAlarmTemplateGroupsRequestRequestTypeDef

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


# ListCloudWatchAlarmTemplatesRequestListCloudWatchAlarmTemplatesPaginateTypeDef

### GroupIdentifier
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListCloudWatchAlarmTemplatesRequestRequestTypeDef

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


# ListEventBridgeRuleTemplateGroupsRequestRequestTypeDef

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


# ListEventBridgeRuleTemplatesRequestListEventBridgeRuleTemplatesPaginateTypeDef

### GroupIdentifier
- **Type**: typing.Optional[str]

### SignalMapIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListEventBridgeRuleTemplatesRequestRequestTypeDef

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


# ListInputDeviceTransfersRequestListInputDeviceTransfersPaginateTypeDef

### TransferType
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListInputDeviceTransfersRequestRequestTypeDef

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


# ListInputDevicesRequestListInputDevicesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListInputDevicesRequestRequestTypeDef

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


# ListInputSecurityGroupsRequestListInputSecurityGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListInputSecurityGroupsRequestRequestTypeDef

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


# ListInputsRequestListInputsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListInputsRequestRequestTypeDef

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


# ListMultiplexProgramsRequestListMultiplexProgramsPaginateTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListMultiplexProgramsRequestRequestTypeDef

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


# ListMultiplexesRequestListMultiplexesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListMultiplexesRequestRequestTypeDef

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


# ListOfferingsRequestListOfferingsPaginateTypeDef

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


# ListOfferingsRequestRequestTypeDef

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


# ListReservationsRequestListReservationsPaginateTypeDef

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


# ListReservationsRequestRequestTypeDef

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


# ListSignalMapsRequestListSignalMapsPaginateTypeDef

### CloudWatchAlarmTemplateGroupIdentifier
- **Type**: typing.Optional[str]

### EventBridgeRuleTemplateGroupIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PaginatorConfigTypeDef]


# ListSignalMapsRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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


# MultiplexProgramChannelDestinationSettingsTypeDef

### MultiplexId
- **Type**: typing.Optional[str]

### ProgramName
- **Type**: typing.Optional[str]


# MultiplexProgramPacketIdentifiersMapTypeDef

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


# MultiplexProgramPipelineDetailTypeDef

### ActiveChannelPipeline
- **Type**: typing.Optional[str]

### PipelineId
- **Type**: typing.Optional[str]


# MultiplexProgramServiceDescriptorTypeDef

### ProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramPacketIdentifiersMapTypeDef]

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


# OutputDestinationExtraOutputTypeDef

### Id
- **Type**: typing.Optional[str]

### MediaPackageSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.MediaPackageOutputDestinationSettingsTypeDef]]

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramChannelDestinationSettingsTypeDef]

### Settings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationSettingsTypeDef]]


# OutputDestinationOutputTypeDef

### Id
- **Type**: typing.Optional[str]

### MediaPackageSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.MediaPackageOutputDestinationSettingsTypeDef]]

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexProgramChannelDestinationSettingsTypeDef]

### Settings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationSettingsTypeDef]]


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


# OutputGroupOutputTypeDef

### OutputGroupSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.OutputGroupSettingsOutputTypeDef'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.OutputTypeDef]
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


# PauseStateScheduleActionSettingsExtraOutputTypeDef

### Pipelines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.PipelinePauseStateSettingsTypeDef]]


# PauseStateScheduleActionSettingsOutputTypeDef

### Pipelines
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.medialive_classes.PipelinePauseStateSettingsTypeDef]]


# PauseStateScheduleActionSettingsTypeDef

### Pipelines
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.PipelinePauseStateSettingsTypeDef]]


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


# PipelinePauseStateSettingsTypeDef

### PipelineId
- **Type**: typing.Literal['PIPELINE_0', 'PIPELINE_1']
- **Required**: Yes


# PurchaseOfferingRequestRequestTypeDef

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


# RebootInputDeviceRequestRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]


# RejectInputDeviceTransferRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['AUDIO', 'AVC', 'HEVC', 'LINK', 'MPEG2']]

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


# RestartChannelPipelinesRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ScheduleActionExtraOutputTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleActionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionSettingsExtraOutputTypeDef'>
- **Required**: Yes

### ScheduleActionStartSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionStartSettingsExtraOutputTypeDef'>
- **Required**: Yes


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


# ScheduleActionSettingsExtraOutputTypeDef

### HlsId3SegmentTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsId3SegmentTaggingScheduleActionSettingsTypeDef]

### HlsTimedMetadataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsTimedMetadataScheduleActionSettingsTypeDef]

### InputPrepareSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputPrepareScheduleActionSettingsExtraOutputTypeDef]

### InputSwitchSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSwitchScheduleActionSettingsExtraOutputTypeDef]

### MotionGraphicsImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MotionGraphicsActivateScheduleActionSettingsTypeDef]

### MotionGraphicsImageDeactivateSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### PauseStateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PauseStateScheduleActionSettingsExtraOutputTypeDef]

### Scte35InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35InputScheduleActionSettingsTypeDef]

### Scte35ReturnToNetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35ReturnToNetworkScheduleActionSettingsTypeDef]

### Scte35SpliceInsertSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35SpliceInsertScheduleActionSettingsTypeDef]

### Scte35TimeSignalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35TimeSignalScheduleActionSettingsExtraOutputTypeDef]

### StaticImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageActivateScheduleActionSettingsTypeDef]

### StaticImageDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageDeactivateScheduleActionSettingsTypeDef]

### StaticImageOutputActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageOutputActivateScheduleActionSettingsExtraOutputTypeDef]

### StaticImageOutputDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageOutputDeactivateScheduleActionSettingsExtraOutputTypeDef]


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


# ScheduleActionSettingsTypeDef

### HlsId3SegmentTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsId3SegmentTaggingScheduleActionSettingsTypeDef]

### HlsTimedMetadataSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.HlsTimedMetadataScheduleActionSettingsTypeDef]

### InputPrepareSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputPrepareScheduleActionSettingsTypeDef]

### InputSwitchSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputSwitchScheduleActionSettingsTypeDef]

### MotionGraphicsImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MotionGraphicsActivateScheduleActionSettingsTypeDef]

### MotionGraphicsImageDeactivateSettings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### PauseStateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.PauseStateScheduleActionSettingsTypeDef]

### Scte35InputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35InputScheduleActionSettingsTypeDef]

### Scte35ReturnToNetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35ReturnToNetworkScheduleActionSettingsTypeDef]

### Scte35SpliceInsertSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35SpliceInsertScheduleActionSettingsTypeDef]

### Scte35TimeSignalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Scte35TimeSignalScheduleActionSettingsTypeDef]

### StaticImageActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageActivateScheduleActionSettingsTypeDef]

### StaticImageDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageDeactivateScheduleActionSettingsTypeDef]

### StaticImageOutputActivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageOutputActivateScheduleActionSettingsTypeDef]

### StaticImageOutputDeactivateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.StaticImageOutputDeactivateScheduleActionSettingsTypeDef]


# ScheduleActionStartSettingsExtraOutputTypeDef

### FixedModeScheduleActionStartSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FixedModeScheduleActionStartSettingsTypeDef]

### FollowModeScheduleActionStartSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FollowModeScheduleActionStartSettingsTypeDef]

### ImmediateModeScheduleActionStartSettings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


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


# ScheduleActionTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleActionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionSettingsTypeDef'>
- **Required**: Yes

### ScheduleActionStartSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ScheduleActionStartSettingsTypeDef'>
- **Required**: Yes


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


# Scte35TimeSignalScheduleActionSettingsExtraOutputTypeDef

### Scte35Descriptors
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.Scte35DescriptorTypeDef]
- **Required**: Yes


# Scte35TimeSignalScheduleActionSettingsOutputTypeDef

### Scte35Descriptors
- **Type**: typing.List[aws_resource_validator.pydantic_models.medialive_classes.Scte35DescriptorTypeDef]
- **Required**: Yes


# Scte35TimeSignalScheduleActionSettingsTypeDef

### Scte35Descriptors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.medialive_classes.Scte35DescriptorTypeDef]
- **Required**: Yes


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


# StandardHlsSettingsTypeDef

### M3u8Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.M3u8SettingsTypeDef'>
- **Required**: Yes

### AudioRenditionSets
- **Type**: typing.Optional[str]


# StartChannelRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDeleteMonitorDeploymentRequestRequestTypeDef

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


# StartInputDeviceMaintenanceWindowRequestRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# StartInputDeviceRequestRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# StartMonitorDeploymentRequestRequestTypeDef

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


# StartMultiplexRequestRequestTypeDef

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


# StartUpdateSignalMapRequestRequestTypeDef

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


# StaticImageOutputActivateScheduleActionSettingsExtraOutputTypeDef

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


# StaticImageOutputDeactivateScheduleActionSettingsExtraOutputTypeDef

### OutputNames
- **Type**: typing.List[str]
- **Required**: Yes

### FadeOut
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]


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


# StaticKeySettingsTypeDef

### StaticKeyValue
- **Type**: <class 'str'>
- **Required**: Yes

### KeyProviderServer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.InputLocationTypeDef]


# StopChannelRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopInputDeviceRequestRequestTypeDef

### InputDeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# StopMultiplexRequestRequestTypeDef

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


# TransferInputDeviceRequestRequestTypeDef

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


# UpdateAccountConfigurationRequestRequestTypeDef

### AccountConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.AccountConfigurationTypeDef]


# UpdateAccountConfigurationResponseTypeDef

### AccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.AccountConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelClassRequestRequestTypeDef

### ChannelClass
- **Type**: typing.Literal['SINGLE_PIPELINE', 'STANDARD']
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationTypeDef, aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationExtraOutputTypeDef]]]


# UpdateChannelClassResponseTypeDef

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelRequestRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CdiInputSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.CdiInputSpecificationTypeDef]

### Destinations
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationTypeDef, aws_resource_validator.pydantic_models.medialive_classes.OutputDestinationExtraOutputTypeDef]]]

### EncoderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.EncoderSettingsTypeDef]

### InputAttachments
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentTypeDef, aws_resource_validator.pydantic_models.medialive_classes.InputAttachmentExtraOutputTypeDef]]]

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


# UpdateChannelResponseTypeDef

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ChannelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCloudWatchAlarmTemplateGroupRequestRequestTypeDef

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


# UpdateCloudWatchAlarmTemplateRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'S3_BUCKET']]

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
- **Type**: typing.Literal['CLOUDFRONT_DISTRIBUTION', 'MEDIACONNECT_FLOW', 'MEDIALIVE_CHANNEL', 'MEDIALIVE_INPUT_DEVICE', 'MEDIALIVE_MULTIPLEX', 'MEDIAPACKAGE_CHANNEL', 'MEDIAPACKAGE_ORIGIN_ENDPOINT', 'S3_BUCKET']
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


# UpdateEventBridgeRuleTemplateGroupRequestRequestTypeDef

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


# UpdateEventBridgeRuleTemplateRequestRequestTypeDef

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


# UpdateInputDeviceRequestRequestTypeDef

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


# UpdateInputDeviceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputDeviceHdSettingsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputDeviceNetworkSettingsTypeDef'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['HD', 'UHD']
- **Required**: Yes

### UhdDeviceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputDeviceUhdSettingsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInputRequestRequestTypeDef

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


# UpdateInputResponseTypeDef

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.InputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInputSecurityGroupRequestRequestTypeDef

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


# UpdateMultiplexProgramRequestRequestTypeDef

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


# UpdateMultiplexRequestRequestTypeDef

### MultiplexId
- **Type**: <class 'str'>
- **Required**: Yes

### MultiplexSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.MultiplexSettingsTypeDef]

### Name
- **Type**: typing.Optional[str]


# UpdateMultiplexResponseTypeDef

### Multiplex
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.MultiplexTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.medialive_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReservationRequestRequestTypeDef

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


# VideoCodecSettingsTypeDef

### FrameCaptureSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.FrameCaptureSettingsTypeDef]

### H264Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H264SettingsTypeDef]

### H265Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.H265SettingsTypeDef]

### Mpeg2Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.medialive_classes.Mpeg2SettingsTypeDef]


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


