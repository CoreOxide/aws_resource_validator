# Mediaconvert Classes

# AacSettings

### AudioDescriptionBroadcasterMix
- **Type**: typing.Optional[typing.Literal['BROADCASTER_MIXED_AD', 'NORMAL']]

### Bitrate
- **Type**: typing.Optional[int]

### CodecProfile
- **Type**: typing.Optional[typing.Literal['HEV1', 'HEV2', 'LC']]

### CodingMode
- **Type**: typing.Optional[typing.Literal['AD_RECEIVER_MIX', 'CODING_MODE_1_0', 'CODING_MODE_1_1', 'CODING_MODE_2_0', 'CODING_MODE_5_1']]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'VBR']]

### RawFormat
- **Type**: typing.Optional[typing.Literal['LATM_LOAS', 'NONE']]

### SampleRate
- **Type**: typing.Optional[int]

### Specification
- **Type**: typing.Optional[typing.Literal['MPEG2', 'MPEG4']]

### VbrQuality
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM_HIGH', 'MEDIUM_LOW']]


# Ac3Settings

### Bitrate
- **Type**: typing.Optional[int]

### BitstreamMode
- **Type**: typing.Optional[typing.Literal['COMMENTARY', 'COMPLETE_MAIN', 'DIALOGUE', 'EMERGENCY', 'HEARING_IMPAIRED', 'MUSIC_AND_EFFECTS', 'VISUALLY_IMPAIRED', 'VOICE_OVER']]

### CodingMode
- **Type**: typing.Optional[typing.Literal['CODING_MODE_1_0', 'CODING_MODE_1_1', 'CODING_MODE_2_0', 'CODING_MODE_3_2_LFE']]

### Dialnorm
- **Type**: typing.Optional[int]

### DynamicRangeCompressionLine
- **Type**: typing.Optional[typing.Literal['FILM_LIGHT', 'FILM_STANDARD', 'MUSIC_LIGHT', 'MUSIC_STANDARD', 'NONE', 'SPEECH']]

### DynamicRangeCompressionProfile
- **Type**: typing.Optional[typing.Literal['FILM_STANDARD', 'NONE']]

### DynamicRangeCompressionRf
- **Type**: typing.Optional[typing.Literal['FILM_LIGHT', 'FILM_STANDARD', 'MUSIC_LIGHT', 'MUSIC_STANDARD', 'NONE', 'SPEECH']]

### LfeFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### MetadataControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### SampleRate
- **Type**: typing.Optional[int]


# AccelerationSettings

### Mode
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'PREFERRED']
- **Required**: Yes


# AdvancedInputFilterSettings

### AddTexture
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Sharpening
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'OFF']]


# AiffSettings

### BitDepth
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]


# AncillarySourceSettings

### Convert608To708
- **Type**: typing.Optional[typing.Literal['DISABLED', 'UPCONVERT']]

### SourceAncillaryChannelNumber
- **Type**: typing.Optional[int]

### TerminateCaptions
- **Type**: typing.Optional[typing.Literal['DISABLED', 'END_OF_INPUT']]


# AssociateCertificateRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# AudioChannelTaggingSettings

### ChannelTag
- **Type**: typing.Optional[typing.Literal['C', 'CS', 'HI', 'L', 'LC', 'LFE', 'LFE2', 'LS', 'LSD', 'LT', 'LW', 'M', 'NAR', 'R', 'RC', 'RS', 'RSD', 'RSL', 'RSR', 'RT', 'RW', 'TBC', 'TBL', 'TBR', 'TCS', 'VHC', 'VHL', 'VHR']]

### ChannelTags
- **Type**: typing.Optional[typing.Sequence[typing.Literal['C', 'CS', 'HI', 'L', 'LC', 'LFE', 'LFE2', 'LS', 'LSD', 'LT', 'LW', 'M', 'NAR', 'R', 'RC', 'RS', 'RSD', 'RSL', 'RSR', 'RT', 'RW', 'TBC', 'TBL', 'TBR', 'TCS', 'VHC', 'VHL', 'VHR']]]


# AudioChannelTaggingSettingsOutput

### ChannelTag
- **Type**: typing.Optional[typing.Literal['C', 'CS', 'HI', 'L', 'LC', 'LFE', 'LFE2', 'LS', 'LSD', 'LT', 'LW', 'M', 'NAR', 'R', 'RC', 'RS', 'RSD', 'RSL', 'RSR', 'RT', 'RW', 'TBC', 'TBL', 'TBR', 'TCS', 'VHC', 'VHL', 'VHR']]

### ChannelTags
- **Type**: typing.Optional[typing.List[typing.Literal['C', 'CS', 'HI', 'L', 'LC', 'LFE', 'LFE2', 'LS', 'LSD', 'LT', 'LW', 'M', 'NAR', 'R', 'RC', 'RS', 'RSD', 'RSL', 'RSR', 'RT', 'RW', 'TBC', 'TBL', 'TBR', 'TCS', 'VHC', 'VHL', 'VHR']]]


# AudioCodecSettings

### AacSettings
- **Type**: <class 'NoneType'>

### Ac3Settings
- **Type**: <class 'NoneType'>

### AiffSettings
- **Type**: <class 'NoneType'>

### Codec
- **Type**: typing.Optional[typing.Literal['AAC', 'AC3', 'AIFF', 'EAC3', 'EAC3_ATMOS', 'FLAC', 'MP2', 'MP3', 'OPUS', 'PASSTHROUGH', 'VORBIS', 'WAV']]

### Eac3AtmosSettings
- **Type**: <class 'NoneType'>

### Eac3Settings
- **Type**: <class 'NoneType'>

### FlacSettings
- **Type**: <class 'NoneType'>

### Mp2Settings
- **Type**: <class 'NoneType'>

### Mp3Settings
- **Type**: <class 'NoneType'>

### OpusSettings
- **Type**: <class 'NoneType'>

### VorbisSettings
- **Type**: <class 'NoneType'>

### WavSettings
- **Type**: <class 'NoneType'>


# AudioDescription

### AudioChannelTaggingSettings
- **Type**: <class 'NoneType'>

### AudioNormalizationSettings
- **Type**: <class 'NoneType'>

### AudioSourceName
- **Type**: typing.Optional[str]

### AudioType
- **Type**: typing.Optional[int]

### AudioTypeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioCodecSettings]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageCodeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### RemixSettings
- **Type**: <class 'NoneType'>

### StreamName
- **Type**: typing.Optional[str]


# AudioDescriptionOutput

### AudioChannelTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioChannelTaggingSettingsOutput]

### AudioNormalizationSettings
- **Type**: <class 'NoneType'>

### AudioSourceName
- **Type**: typing.Optional[str]

### AudioType
- **Type**: typing.Optional[int]

### AudioTypeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioCodecSettings]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageCodeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RemixSettingsOutput]

### StreamName
- **Type**: typing.Optional[str]


# AudioNormalizationSettings

### Algorithm
- **Type**: typing.Optional[typing.Literal['ITU_BS_1770_1', 'ITU_BS_1770_2', 'ITU_BS_1770_3', 'ITU_BS_1770_4']]

### AlgorithmControl
- **Type**: typing.Optional[typing.Literal['CORRECT_AUDIO', 'MEASURE_ONLY']]

### CorrectionGateLevel
- **Type**: typing.Optional[int]

### LoudnessLogging
- **Type**: typing.Optional[typing.Literal['DONT_LOG', 'LOG']]

### PeakCalculation
- **Type**: typing.Optional[typing.Literal['NONE', 'TRUE_PEAK']]

### TargetLkfs
- **Type**: typing.Optional[float]

### TruePeakLimiterThreshold
- **Type**: typing.Optional[float]


# AudioProperties

### BitDepth
- **Type**: typing.Optional[int]

### BitRate
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### FrameRate
- **Type**: <class 'NoneType'>

### LanguageCode
- **Type**: typing.Optional[str]

### SampleRate
- **Type**: typing.Optional[int]


# AudioSelector

### AudioDurationCorrection
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'FORCE', 'FRAME', 'TRACK']]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DefaultSelection
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NOT_DEFAULT']]

### ExternalAudioFileInput
- **Type**: typing.Optional[str]

### HlsRenditionGroupSettings
- **Type**: <class 'NoneType'>

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### Offset
- **Type**: typing.Optional[int]

### Pids
- **Type**: typing.Optional[typing.Sequence[int]]

### ProgramSelection
- **Type**: typing.Optional[int]

### RemixSettings
- **Type**: <class 'NoneType'>

### SelectorType
- **Type**: typing.Optional[typing.Literal['HLS_RENDITION_GROUP', 'LANGUAGE_CODE', 'PID', 'TRACK']]

### Tracks
- **Type**: typing.Optional[typing.Sequence[int]]


# AudioSelectorGroup

### AudioSelectorNames
- **Type**: typing.Optional[typing.Sequence[str]]


# AudioSelectorGroupOutput

### AudioSelectorNames
- **Type**: typing.Optional[typing.List[str]]


# AudioSelectorOutput

### AudioDurationCorrection
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'FORCE', 'FRAME', 'TRACK']]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DefaultSelection
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NOT_DEFAULT']]

### ExternalAudioFileInput
- **Type**: typing.Optional[str]

### HlsRenditionGroupSettings
- **Type**: <class 'NoneType'>

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### Offset
- **Type**: typing.Optional[int]

### Pids
- **Type**: typing.Optional[typing.List[int]]

### ProgramSelection
- **Type**: typing.Optional[int]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RemixSettingsOutput]

### SelectorType
- **Type**: typing.Optional[typing.Literal['HLS_RENDITION_GROUP', 'LANGUAGE_CODE', 'PID', 'TRACK']]

### Tracks
- **Type**: typing.Optional[typing.List[int]]


# AutomatedAbrRule

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutomatedAbrRuleOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutomatedAbrSettings

### MaxAbrBitrate
- **Type**: typing.Optional[int]

### MaxRenditions
- **Type**: typing.Optional[int]

### MinAbrBitrate
- **Type**: typing.Optional[int]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedAbrRule]]


# AutomatedAbrSettingsOutput

### MaxAbrBitrate
- **Type**: typing.Optional[int]

### MaxRenditions
- **Type**: typing.Optional[int]

### MinAbrBitrate
- **Type**: typing.Optional[int]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedAbrRuleOutput]]


# AutomatedEncodingSettings

### AbrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedAbrSettings]


# AutomatedEncodingSettingsOutput

### AbrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedAbrSettingsOutput]


# Av1QvbrSettings

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### QvbrQualityLevelFineTune
- **Type**: typing.Optional[float]


# Av1Settings

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### BitDepth
- **Type**: typing.Optional[typing.Literal['BIT_10', 'BIT_8']]

### FilmGrainSynthesis
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### MaxBitrate
- **Type**: typing.Optional[int]

### NumberBFramesBetweenReferenceFrames
- **Type**: typing.Optional[int]

### QvbrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Av1QvbrSettings]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['QVBR']]

### Slices
- **Type**: typing.Optional[int]

### SpatialAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AvailBlanking

### AvailBlankingImage
- **Type**: typing.Optional[str]


# AvcIntraSettings

### AvcIntraClass
- **Type**: typing.Optional[typing.Literal['CLASS_100', 'CLASS_200', 'CLASS_4K_2K', 'CLASS_50']]

### AvcIntraUhdSettings
- **Type**: <class 'NoneType'>

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### InterlaceMode
- **Type**: typing.Optional[typing.Literal['BOTTOM_FIELD', 'FOLLOW_BOTTOM_FIELD', 'FOLLOW_TOP_FIELD', 'PROGRESSIVE', 'TOP_FIELD']]

### ScanTypeConversionMode
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'INTERLACED_OPTIMIZE']]

### SlowPal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Telecine
- **Type**: typing.Optional[typing.Literal['HARD', 'NONE']]


# AvcIntraUhdSettings

### QualityTuningLevel
- **Type**: typing.Optional[typing.Literal['MULTI_PASS', 'SINGLE_PASS']]


# BandwidthReductionFilter

### Sharpening
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'OFF']]

### Strength
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'OFF']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BurninDestinationSettings

### Alignment
- **Type**: typing.Optional[typing.Literal['AUTO', 'CENTERED', 'LEFT']]

### ApplyFontColor
- **Type**: typing.Optional[typing.Literal['ALL_TEXT', 'WHITE_TEXT_ONLY']]

### BackgroundColor
- **Type**: typing.Optional[typing.Literal['AUTO', 'BLACK', 'NONE', 'WHITE']]

### BackgroundOpacity
- **Type**: typing.Optional[int]

### FallbackFont
- **Type**: typing.Optional[typing.Literal['BEST_MATCH', 'MONOSPACED_SANSSERIF', 'MONOSPACED_SERIF', 'PROPORTIONAL_SANSSERIF', 'PROPORTIONAL_SERIF']]

### FontColor
- **Type**: typing.Optional[typing.Literal['AUTO', 'BLACK', 'BLUE', 'GREEN', 'HEX', 'RED', 'WHITE', 'YELLOW']]

### FontFileBold
- **Type**: typing.Optional[str]

### FontFileBoldItalic
- **Type**: typing.Optional[str]

### FontFileItalic
- **Type**: typing.Optional[str]

### FontFileRegular
- **Type**: typing.Optional[str]

### FontOpacity
- **Type**: typing.Optional[int]

### FontResolution
- **Type**: typing.Optional[int]

### FontScript
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'HANS', 'HANT']]

### FontSize
- **Type**: typing.Optional[int]

### HexFontColor
- **Type**: typing.Optional[str]

### OutlineColor
- **Type**: typing.Optional[typing.Literal['AUTO', 'BLACK', 'BLUE', 'GREEN', 'RED', 'WHITE', 'YELLOW']]

### OutlineSize
- **Type**: typing.Optional[int]

### RemoveRubyReserveAttributes
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ShadowColor
- **Type**: typing.Optional[typing.Literal['AUTO', 'BLACK', 'NONE', 'WHITE']]

### ShadowOpacity
- **Type**: typing.Optional[int]

### ShadowXOffset
- **Type**: typing.Optional[int]

### ShadowYOffset
- **Type**: typing.Optional[int]

### StylePassthrough
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TeletextSpacing
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED_GRID', 'PROPORTIONAL']]

### XPosition
- **Type**: typing.Optional[int]

### YPosition
- **Type**: typing.Optional[int]


# CancelJobRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# CaptionDescription

### CaptionSelectorName
- **Type**: typing.Optional[str]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDestinationSettings]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageDescription
- **Type**: typing.Optional[str]


# CaptionDescriptionOutput

### CaptionSelectorName
- **Type**: typing.Optional[str]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDestinationSettingsOutput]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageDescription
- **Type**: typing.Optional[str]


# CaptionDescriptionPreset

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDestinationSettings]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageDescription
- **Type**: typing.Optional[str]


# CaptionDescriptionPresetOutput

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDestinationSettingsOutput]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageDescription
- **Type**: typing.Optional[str]


# CaptionDestinationSettings

### BurninDestinationSettings
- **Type**: <class 'NoneType'>

### DestinationType
- **Type**: typing.Optional[typing.Literal['BURN_IN', 'DVB_SUB', 'EMBEDDED', 'EMBEDDED_PLUS_SCTE20', 'IMSC', 'SCC', 'SCTE20_PLUS_EMBEDDED', 'SMI', 'SRT', 'TELETEXT', 'TTML', 'WEBVTT']]

### DvbSubDestinationSettings
- **Type**: <class 'NoneType'>

### EmbeddedDestinationSettings
- **Type**: <class 'NoneType'>

### ImscDestinationSettings
- **Type**: <class 'NoneType'>

### SccDestinationSettings
- **Type**: <class 'NoneType'>

### SrtDestinationSettings
- **Type**: <class 'NoneType'>

### TeletextDestinationSettings
- **Type**: <class 'NoneType'>

### TtmlDestinationSettings
- **Type**: <class 'NoneType'>

### WebvttDestinationSettings
- **Type**: <class 'NoneType'>


# CaptionDestinationSettingsOutput

### BurninDestinationSettings
- **Type**: <class 'NoneType'>

### DestinationType
- **Type**: typing.Optional[typing.Literal['BURN_IN', 'DVB_SUB', 'EMBEDDED', 'EMBEDDED_PLUS_SCTE20', 'IMSC', 'SCC', 'SCTE20_PLUS_EMBEDDED', 'SMI', 'SRT', 'TELETEXT', 'TTML', 'WEBVTT']]

### DvbSubDestinationSettings
- **Type**: <class 'NoneType'>

### EmbeddedDestinationSettings
- **Type**: <class 'NoneType'>

### ImscDestinationSettings
- **Type**: <class 'NoneType'>

### SccDestinationSettings
- **Type**: <class 'NoneType'>

### SrtDestinationSettings
- **Type**: <class 'NoneType'>

### TeletextDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TeletextDestinationSettingsOutput]

### TtmlDestinationSettings
- **Type**: <class 'NoneType'>

### WebvttDestinationSettings
- **Type**: <class 'NoneType'>


# CaptionSelector

### CustomLanguageCode
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### SourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSourceSettings]


# CaptionSourceFramerate

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]


# CaptionSourceSettings

### AncillarySourceSettings
- **Type**: <class 'NoneType'>

### DvbSubSourceSettings
- **Type**: <class 'NoneType'>

### EmbeddedSourceSettings
- **Type**: <class 'NoneType'>

### FileSourceSettings
- **Type**: <class 'NoneType'>

### SourceType
- **Type**: typing.Optional[typing.Literal['ANCILLARY', 'DVB_SUB', 'EMBEDDED', 'IMSC', 'NULL_SOURCE', 'SCC', 'SCTE20', 'SMI', 'SMPTE_TT', 'SRT', 'STL', 'TELETEXT', 'TTML', 'WEBVTT']]

### TeletextSourceSettings
- **Type**: <class 'NoneType'>

### TrackSourceSettings
- **Type**: <class 'NoneType'>

### WebvttHlsSourceSettings
- **Type**: <class 'NoneType'>


# ChannelMapping

### OutputChannels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputChannelMapping]]


# ChannelMappingOutput

### OutputChannels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputChannelMappingOutput]]


# ClipLimits

### MaximumRGBTolerance
- **Type**: typing.Optional[int]

### MaximumYUV
- **Type**: typing.Optional[int]

### MinimumRGBTolerance
- **Type**: typing.Optional[int]

### MinimumYUV
- **Type**: typing.Optional[int]


# CmafAdditionalManifest

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.Sequence[str]]


# CmafAdditionalManifestOutput

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# CmafEncryptionSettings

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CmafEncryptionSettingsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CmafGroupSettings

### AdditionalManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafAdditionalManifest]]

### BaseUrl
- **Type**: typing.Optional[str]

### ClientCache
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CodecSpecification
- **Type**: typing.Optional[typing.Literal['RFC_4281', 'RFC_6381']]

### DashIFrameTrickPlayNameModifier
- **Type**: typing.Optional[str]

### DashManifestStyle
- **Type**: typing.Optional[typing.Literal['BASIC', 'COMPACT', 'DISTINCT']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: <class 'NoneType'>

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafEncryptionSettings]

### FragmentLength
- **Type**: typing.Optional[int]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafImageBasedTrickPlaySettings]

### ManifestCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### ManifestDurationFormat
- **Type**: typing.Optional[typing.Literal['FLOATING_POINT', 'INTEGER']]

### MinBufferTime
- **Type**: typing.Optional[int]

### MinFinalSegmentLength
- **Type**: typing.Optional[float]

### MpdManifestBandwidthType
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'MAX']]

### MpdProfile
- **Type**: typing.Optional[typing.Literal['MAIN_PROFILE', 'ON_DEMAND_PROFILE']]

### PtsOffsetHandlingForBFrames
- **Type**: typing.Optional[typing.Literal['MATCH_INITIAL_PTS', 'ZERO_BASED']]

### SegmentControl
- **Type**: typing.Optional[typing.Literal['SEGMENTED_FILES', 'SINGLE_FILE']]

### SegmentLength
- **Type**: typing.Optional[int]

### SegmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### StreamInfResolution
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### TargetDurationCompatibilityMode
- **Type**: typing.Optional[typing.Literal['LEGACY', 'SPEC_COMPLIANT']]

### VideoCompositionOffsets
- **Type**: typing.Optional[typing.Literal['SIGNED', 'UNSIGNED']]

### WriteDashManifest
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### WriteHlsManifest
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### WriteSegmentTimelineInRepresentation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CmafGroupSettingsOutput

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafAdditionalManifestOutput]]

### BaseUrl
- **Type**: typing.Optional[str]

### ClientCache
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CodecSpecification
- **Type**: typing.Optional[typing.Literal['RFC_4281', 'RFC_6381']]

### DashIFrameTrickPlayNameModifier
- **Type**: typing.Optional[str]

### DashManifestStyle
- **Type**: typing.Optional[typing.Literal['BASIC', 'COMPACT', 'DISTINCT']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: <class 'NoneType'>

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafEncryptionSettingsOutput]

### FragmentLength
- **Type**: typing.Optional[int]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafImageBasedTrickPlaySettings]

### ManifestCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### ManifestDurationFormat
- **Type**: typing.Optional[typing.Literal['FLOATING_POINT', 'INTEGER']]

### MinBufferTime
- **Type**: typing.Optional[int]

### MinFinalSegmentLength
- **Type**: typing.Optional[float]

### MpdManifestBandwidthType
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'MAX']]

### MpdProfile
- **Type**: typing.Optional[typing.Literal['MAIN_PROFILE', 'ON_DEMAND_PROFILE']]

### PtsOffsetHandlingForBFrames
- **Type**: typing.Optional[typing.Literal['MATCH_INITIAL_PTS', 'ZERO_BASED']]

### SegmentControl
- **Type**: typing.Optional[typing.Literal['SEGMENTED_FILES', 'SINGLE_FILE']]

### SegmentLength
- **Type**: typing.Optional[int]

### SegmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### StreamInfResolution
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### TargetDurationCompatibilityMode
- **Type**: typing.Optional[typing.Literal['LEGACY', 'SPEC_COMPLIANT']]

### VideoCompositionOffsets
- **Type**: typing.Optional[typing.Literal['SIGNED', 'UNSIGNED']]

### WriteDashManifest
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### WriteHlsManifest
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### WriteSegmentTimelineInRepresentation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CmafImageBasedTrickPlaySettings

### IntervalCadence
- **Type**: typing.Optional[typing.Literal['FOLLOW_CUSTOM', 'FOLLOW_IFRAME']]

### ThumbnailHeight
- **Type**: typing.Optional[int]

### ThumbnailInterval
- **Type**: typing.Optional[float]

### ThumbnailWidth
- **Type**: typing.Optional[int]

### TileHeight
- **Type**: typing.Optional[int]

### TileWidth
- **Type**: typing.Optional[int]


# CmfcSettings

### AudioDuration
- **Type**: typing.Optional[typing.Literal['DEFAULT_CODEC_DURATION', 'MATCH_VIDEO_DURATION']]

### AudioGroupId
- **Type**: typing.Optional[str]

### AudioRenditionSets
- **Type**: typing.Optional[str]

### AudioTrackType
- **Type**: typing.Optional[typing.Literal['ALTERNATE_AUDIO_AUTO_SELECT', 'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT', 'ALTERNATE_AUDIO_NOT_AUTO_SELECT', 'AUDIO_ONLY_VARIANT_STREAM']]

### DescriptiveVideoServiceFlag
- **Type**: typing.Optional[typing.Literal['DONT_FLAG', 'FLAG']]

### IFrameOnlyManifest
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### KlvMetadata
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### ManifestMetadataSignaling
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Scte35Esam
- **Type**: typing.Optional[typing.Literal['INSERT', 'NONE']]

### Scte35Source
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### TimedMetadata
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### TimedMetadataBoxVersion
- **Type**: typing.Optional[typing.Literal['VERSION_0', 'VERSION_1']]

### TimedMetadataSchemeIdUri
- **Type**: typing.Optional[str]

### TimedMetadataValue
- **Type**: typing.Optional[str]


# ColorConversion3DLUTSetting

### FileInput
- **Type**: typing.Optional[str]

### InputColorSpace
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'HDR10', 'HLG_2020', 'P3D65_HDR', 'P3D65_SDR', 'P3DCI', 'REC_601', 'REC_709']]

### InputMasteringLuminance
- **Type**: typing.Optional[int]

### OutputColorSpace
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'HDR10', 'HLG_2020', 'P3D65_HDR', 'P3D65_SDR', 'P3DCI', 'REC_601', 'REC_709']]

### OutputMasteringLuminance
- **Type**: typing.Optional[int]


# ColorCorrector

### Brightness
- **Type**: typing.Optional[int]

### ClipLimits
- **Type**: <class 'NoneType'>

### ColorSpaceConversion
- **Type**: typing.Optional[typing.Literal['FORCE_601', 'FORCE_709', 'FORCE_HDR10', 'FORCE_HLG_2020', 'FORCE_P3D65_HDR', 'FORCE_P3D65_SDR', 'FORCE_P3DCI', 'NONE']]

### Contrast
- **Type**: typing.Optional[int]

### Hdr10Metadata
- **Type**: <class 'NoneType'>

### HdrToSdrToneMapper
- **Type**: typing.Optional[typing.Literal['PRESERVE_DETAILS', 'VIBRANT']]

### Hue
- **Type**: typing.Optional[int]

### MaxLuminance
- **Type**: typing.Optional[int]

### SampleRangeConversion
- **Type**: typing.Optional[typing.Literal['LIMITED_RANGE_CLIP', 'LIMITED_RANGE_SQUEEZE', 'NONE']]

### Saturation
- **Type**: typing.Optional[int]

### SdrReferenceWhiteLevel
- **Type**: typing.Optional[int]


# Container

### Duration
- **Type**: typing.Optional[float]

### Format
- **Type**: typing.Optional[typing.Literal['matroska', 'mp4', 'quicktime', 'webm']]

### Tracks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.Track]]


# ContainerSettings

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerSettingsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateJobRequest

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobSettingsUnion'>
- **Required**: Yes

### AccelerationSettings
- **Type**: <class 'NoneType'>

### BillingTagsSource
- **Type**: typing.Optional[typing.Literal['JOB', 'JOB_TEMPLATE', 'PRESET', 'QUEUE']]

### ClientRequestToken
- **Type**: typing.Optional[str]

### HopDestinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.HopDestination]]

### JobEngineVersion
- **Type**: typing.Optional[str]

### JobTemplate
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Queue
- **Type**: typing.Optional[str]

### SimulateReservedQueue
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### StatusUpdateInterval
- **Type**: typing.Optional[typing.Literal['SECONDS_10', 'SECONDS_12', 'SECONDS_120', 'SECONDS_15', 'SECONDS_180', 'SECONDS_20', 'SECONDS_240', 'SECONDS_30', 'SECONDS_300', 'SECONDS_360', 'SECONDS_420', 'SECONDS_480', 'SECONDS_540', 'SECONDS_60', 'SECONDS_600']]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### UserMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateJobResponse

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJobTemplateRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplateSettingsUnion'>
- **Required**: Yes

### AccelerationSettings
- **Type**: <class 'NoneType'>

### Category
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### HopDestinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.HopDestination]]

### Priority
- **Type**: typing.Optional[int]

### Queue
- **Type**: typing.Optional[str]

### StatusUpdateInterval
- **Type**: typing.Optional[typing.Literal['SECONDS_10', 'SECONDS_12', 'SECONDS_120', 'SECONDS_15', 'SECONDS_180', 'SECONDS_20', 'SECONDS_240', 'SECONDS_30', 'SECONDS_300', 'SECONDS_360', 'SECONDS_420', 'SECONDS_480', 'SECONDS_540', 'SECONDS_60', 'SECONDS_600']]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateJobTemplateResponse

### JobTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePresetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.PresetSettingsUnion'>
- **Required**: Yes

### Category
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePresetResponse

### Preset
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Preset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQueueRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConcurrentJobs
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### PricingPlan
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'RESERVED']]

### ReservationPlanSettings
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PAUSED']]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQueueResponse

### Queue
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Queue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# DashAdditionalManifest

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.Sequence[str]]


# DashAdditionalManifestOutput

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# DashIsoEncryptionSettings

### PlaybackDeviceCompatibility
- **Type**: typing.Optional[typing.Literal['CENC_V1', 'UNENCRYPTED_SEI']]

### SpekeKeyProvider
- **Type**: <class 'NoneType'>


# DashIsoEncryptionSettingsOutput

### PlaybackDeviceCompatibility
- **Type**: typing.Optional[typing.Literal['CENC_V1', 'UNENCRYPTED_SEI']]

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderOutput]


# DashIsoGroupSettings

### AdditionalManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.DashAdditionalManifest]]

### AudioChannelConfigSchemeIdUri
- **Type**: typing.Optional[typing.Literal['DOLBY_CHANNEL_CONFIGURATION', 'MPEG_CHANNEL_CONFIGURATION']]

### BaseUrl
- **Type**: typing.Optional[str]

### DashIFrameTrickPlayNameModifier
- **Type**: typing.Optional[str]

### DashManifestStyle
- **Type**: typing.Optional[typing.Literal['BASIC', 'COMPACT', 'DISTINCT']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: <class 'NoneType'>

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoEncryptionSettings]

### FragmentLength
- **Type**: typing.Optional[int]

### HbbtvCompliance
- **Type**: typing.Optional[typing.Literal['HBBTV_1_5', 'NONE']]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoImageBasedTrickPlaySettings]

### MinBufferTime
- **Type**: typing.Optional[int]

### MinFinalSegmentLength
- **Type**: typing.Optional[float]

### MpdManifestBandwidthType
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'MAX']]

### MpdProfile
- **Type**: typing.Optional[typing.Literal['MAIN_PROFILE', 'ON_DEMAND_PROFILE']]

### PtsOffsetHandlingForBFrames
- **Type**: typing.Optional[typing.Literal['MATCH_INITIAL_PTS', 'ZERO_BASED']]

### SegmentControl
- **Type**: typing.Optional[typing.Literal['SEGMENTED_FILES', 'SINGLE_FILE']]

### SegmentLength
- **Type**: typing.Optional[int]

### SegmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### VideoCompositionOffsets
- **Type**: typing.Optional[typing.Literal['SIGNED', 'UNSIGNED']]

### WriteSegmentTimelineInRepresentation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DashIsoGroupSettingsOutput

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.DashAdditionalManifestOutput]]

### AudioChannelConfigSchemeIdUri
- **Type**: typing.Optional[typing.Literal['DOLBY_CHANNEL_CONFIGURATION', 'MPEG_CHANNEL_CONFIGURATION']]

### BaseUrl
- **Type**: typing.Optional[str]

### DashIFrameTrickPlayNameModifier
- **Type**: typing.Optional[str]

### DashManifestStyle
- **Type**: typing.Optional[typing.Literal['BASIC', 'COMPACT', 'DISTINCT']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: <class 'NoneType'>

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoEncryptionSettingsOutput]

### FragmentLength
- **Type**: typing.Optional[int]

### HbbtvCompliance
- **Type**: typing.Optional[typing.Literal['HBBTV_1_5', 'NONE']]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoImageBasedTrickPlaySettings]

### MinBufferTime
- **Type**: typing.Optional[int]

### MinFinalSegmentLength
- **Type**: typing.Optional[float]

### MpdManifestBandwidthType
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'MAX']]

### MpdProfile
- **Type**: typing.Optional[typing.Literal['MAIN_PROFILE', 'ON_DEMAND_PROFILE']]

### PtsOffsetHandlingForBFrames
- **Type**: typing.Optional[typing.Literal['MATCH_INITIAL_PTS', 'ZERO_BASED']]

### SegmentControl
- **Type**: typing.Optional[typing.Literal['SEGMENTED_FILES', 'SINGLE_FILE']]

### SegmentLength
- **Type**: typing.Optional[int]

### SegmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### VideoCompositionOffsets
- **Type**: typing.Optional[typing.Literal['SIGNED', 'UNSIGNED']]

### WriteSegmentTimelineInRepresentation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DashIsoImageBasedTrickPlaySettings

### IntervalCadence
- **Type**: typing.Optional[typing.Literal['FOLLOW_CUSTOM', 'FOLLOW_IFRAME']]

### ThumbnailHeight
- **Type**: typing.Optional[int]

### ThumbnailInterval
- **Type**: typing.Optional[float]

### ThumbnailWidth
- **Type**: typing.Optional[int]

### TileHeight
- **Type**: typing.Optional[int]

### TileWidth
- **Type**: typing.Optional[int]


# DataProperties

### LanguageCode
- **Type**: typing.Optional[str]


# Deinterlacer

### Algorithm
- **Type**: typing.Optional[typing.Literal['BLEND', 'BLEND_TICKER', 'INTERPOLATE', 'INTERPOLATE_TICKER', 'LINEAR_INTERPOLATION']]

### Control
- **Type**: typing.Optional[typing.Literal['FORCE_ALL_FRAMES', 'NORMAL']]

### Mode
- **Type**: typing.Optional[typing.Literal['ADAPTIVE', 'DEINTERLACE', 'INVERSE_TELECINE']]


# DeleteJobTemplateRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePresetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEndpointsRequest

### MaxResults
- **Type**: typing.Optional[int]

### Mode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'GET_ONLY']]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEndpointsRequestPaginate

### Mode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'GET_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfig]


# DescribeEndpointsResponse

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DestinationSettings

### S3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.S3DestinationSettings]


# DisassociateCertificateRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DolbyVision

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DolbyVisionLevel6Metadata

### MaxCll
- **Type**: typing.Optional[int]

### MaxFall
- **Type**: typing.Optional[int]


# DvbNitSettings

### NetworkId
- **Type**: typing.Optional[int]

### NetworkName
- **Type**: typing.Optional[str]

### NitInterval
- **Type**: typing.Optional[int]


# DvbSdtSettings

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DvbSubDestinationSettings

### Alignment
- **Type**: typing.Optional[typing.Literal['AUTO', 'CENTERED', 'LEFT']]

### ApplyFontColor
- **Type**: typing.Optional[typing.Literal['ALL_TEXT', 'WHITE_TEXT_ONLY']]

### BackgroundColor
- **Type**: typing.Optional[typing.Literal['AUTO', 'BLACK', 'NONE', 'WHITE']]

### BackgroundOpacity
- **Type**: typing.Optional[int]

### DdsHandling
- **Type**: typing.Optional[typing.Literal['NONE', 'NO_DISPLAY_WINDOW', 'SPECIFIED']]

### DdsXCoordinate
- **Type**: typing.Optional[int]

### DdsYCoordinate
- **Type**: typing.Optional[int]

### FallbackFont
- **Type**: typing.Optional[typing.Literal['BEST_MATCH', 'MONOSPACED_SANSSERIF', 'MONOSPACED_SERIF', 'PROPORTIONAL_SANSSERIF', 'PROPORTIONAL_SERIF']]

### FontColor
- **Type**: typing.Optional[typing.Literal['AUTO', 'BLACK', 'BLUE', 'GREEN', 'HEX', 'RED', 'WHITE', 'YELLOW']]

### FontFileBold
- **Type**: typing.Optional[str]

### FontFileBoldItalic
- **Type**: typing.Optional[str]

### FontFileItalic
- **Type**: typing.Optional[str]

### FontFileRegular
- **Type**: typing.Optional[str]

### FontOpacity
- **Type**: typing.Optional[int]

### FontResolution
- **Type**: typing.Optional[int]

### FontScript
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'HANS', 'HANT']]

### FontSize
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### HexFontColor
- **Type**: typing.Optional[str]

### OutlineColor
- **Type**: typing.Optional[typing.Literal['AUTO', 'BLACK', 'BLUE', 'GREEN', 'RED', 'WHITE', 'YELLOW']]

### OutlineSize
- **Type**: typing.Optional[int]

### ShadowColor
- **Type**: typing.Optional[typing.Literal['AUTO', 'BLACK', 'NONE', 'WHITE']]

### ShadowOpacity
- **Type**: typing.Optional[int]

### ShadowXOffset
- **Type**: typing.Optional[int]

### ShadowYOffset
- **Type**: typing.Optional[int]

### StylePassthrough
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SubtitlingType
- **Type**: typing.Optional[typing.Literal['HEARING_IMPAIRED', 'STANDARD']]

### TeletextSpacing
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED_GRID', 'PROPORTIONAL']]

### Width
- **Type**: typing.Optional[int]

### XPosition
- **Type**: typing.Optional[int]

### YPosition
- **Type**: typing.Optional[int]


# DvbSubSourceSettings

### Pid
- **Type**: typing.Optional[int]


# DvbTdtSettings

### TdtInterval
- **Type**: typing.Optional[int]


# DynamicAudioSelector

### AudioDurationCorrection
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'FORCE', 'FRAME', 'TRACK']]

### ExternalAudioFileInput
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### Offset
- **Type**: typing.Optional[int]

### SelectorType
- **Type**: typing.Optional[typing.Literal['ALL_TRACKS', 'LANGUAGE_CODE']]


# Eac3AtmosSettings

### Bitrate
- **Type**: typing.Optional[int]

### BitstreamMode
- **Type**: typing.Optional[typing.Literal['COMPLETE_MAIN']]

### CodingMode
- **Type**: typing.Optional[typing.Literal['CODING_MODE_5_1_4', 'CODING_MODE_7_1_4', 'CODING_MODE_9_1_6', 'CODING_MODE_AUTO']]

### DialogueIntelligence
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DownmixControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### DynamicRangeCompressionLine
- **Type**: typing.Optional[typing.Literal['FILM_LIGHT', 'FILM_STANDARD', 'MUSIC_LIGHT', 'MUSIC_STANDARD', 'NONE', 'SPEECH']]

### DynamicRangeCompressionRf
- **Type**: typing.Optional[typing.Literal['FILM_LIGHT', 'FILM_STANDARD', 'MUSIC_LIGHT', 'MUSIC_STANDARD', 'NONE', 'SPEECH']]

### DynamicRangeControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### LoRoCenterMixLevel
- **Type**: typing.Optional[float]

### LoRoSurroundMixLevel
- **Type**: typing.Optional[float]

### LtRtCenterMixLevel
- **Type**: typing.Optional[float]

### LtRtSurroundMixLevel
- **Type**: typing.Optional[float]

### MeteringMode
- **Type**: typing.Optional[typing.Literal['ITU_BS_1770_1', 'ITU_BS_1770_2', 'ITU_BS_1770_3', 'ITU_BS_1770_4', 'LEQ_A']]

### SampleRate
- **Type**: typing.Optional[int]

### SpeechThreshold
- **Type**: typing.Optional[int]

### StereoDownmix
- **Type**: typing.Optional[typing.Literal['DPL2', 'NOT_INDICATED', 'STEREO', 'SURROUND']]

### SurroundExMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'NOT_INDICATED']]


# Eac3Settings

### AttenuationControl
- **Type**: typing.Optional[typing.Literal['ATTENUATE_3_DB', 'NONE']]

### Bitrate
- **Type**: typing.Optional[int]

### BitstreamMode
- **Type**: typing.Optional[typing.Literal['COMMENTARY', 'COMPLETE_MAIN', 'EMERGENCY', 'HEARING_IMPAIRED', 'VISUALLY_IMPAIRED']]

### CodingMode
- **Type**: typing.Optional[typing.Literal['CODING_MODE_1_0', 'CODING_MODE_2_0', 'CODING_MODE_3_2']]

### DcFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Dialnorm
- **Type**: typing.Optional[int]

### DynamicRangeCompressionLine
- **Type**: typing.Optional[typing.Literal['FILM_LIGHT', 'FILM_STANDARD', 'MUSIC_LIGHT', 'MUSIC_STANDARD', 'NONE', 'SPEECH']]

### DynamicRangeCompressionRf
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

### SampleRate
- **Type**: typing.Optional[int]

### StereoDownmix
- **Type**: typing.Optional[typing.Literal['DPL2', 'LO_RO', 'LT_RT', 'NOT_INDICATED']]

### SurroundExMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'NOT_INDICATED']]

### SurroundMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'NOT_INDICATED']]


# EmbeddedDestinationSettings

### Destination608ChannelNumber
- **Type**: typing.Optional[int]

### Destination708ServiceNumber
- **Type**: typing.Optional[int]


# EmbeddedSourceSettings

### Convert608To708
- **Type**: typing.Optional[typing.Literal['DISABLED', 'UPCONVERT']]

### Source608ChannelNumber
- **Type**: typing.Optional[int]

### Source608TrackNumber
- **Type**: typing.Optional[int]

### TerminateCaptions
- **Type**: typing.Optional[typing.Literal['DISABLED', 'END_OF_INPUT']]


# EncryptionContractConfiguration

### SpekeAudioPreset
- **Type**: typing.Optional[typing.Literal['PRESET_AUDIO_1', 'PRESET_AUDIO_2', 'PRESET_AUDIO_3', 'SHARED', 'UNENCRYPTED']]

### SpekeVideoPreset
- **Type**: typing.Optional[typing.Literal['PRESET_VIDEO_1', 'PRESET_VIDEO_2', 'PRESET_VIDEO_3', 'PRESET_VIDEO_4', 'PRESET_VIDEO_5', 'PRESET_VIDEO_6', 'PRESET_VIDEO_7', 'PRESET_VIDEO_8', 'SHARED', 'UNENCRYPTED']]


# Endpoint

### Url
- **Type**: typing.Optional[str]


# EsamManifestConfirmConditionNotification

### MccXml
- **Type**: typing.Optional[str]


# EsamSettings

### ManifestConfirmConditionNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamManifestConfirmConditionNotification]

### ResponseSignalPreroll
- **Type**: typing.Optional[int]

### SignalProcessingNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSignalProcessingNotification]


# EsamSignalProcessingNotification

### SccXml
- **Type**: typing.Optional[str]


# ExtendedDataServices

### CopyProtectionAction
- **Type**: typing.Optional[typing.Literal['PASSTHROUGH', 'STRIP']]

### VchipAction
- **Type**: typing.Optional[typing.Literal['PASSTHROUGH', 'STRIP']]


# Extra

### AudioDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioDescriptionOutput]]

### CaptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDescriptionOutput]]

### ContainerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ContainerSettingsOutput]

### Extension
- **Type**: typing.Optional[str]

### NameModifier
- **Type**: typing.Optional[str]

### OutputSettings
- **Type**: <class 'NoneType'>

### Preset
- **Type**: typing.Optional[str]

### VideoDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoDescriptionOutput]


# F4vSettings

### MoovPlacement
- **Type**: typing.Optional[typing.Literal['NORMAL', 'PROGRESSIVE_DOWNLOAD']]


# FileGroupSettings

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: <class 'NoneType'>


# FileSourceSettings

### ByteRateLimit
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Convert608To708
- **Type**: typing.Optional[typing.Literal['DISABLED', 'UPCONVERT']]

### ConvertPaintToPop
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Framerate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSourceFramerate]

### SourceFile
- **Type**: typing.Optional[str]

### TimeDelta
- **Type**: typing.Optional[int]

### TimeDeltaUnits
- **Type**: typing.Optional[typing.Literal['MILLISECONDS', 'SECONDS']]


# FlacSettings

### BitDepth
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]


# ForceIncludeRenditionSize

### Height
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# FrameCaptureSettings

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### MaxCaptures
- **Type**: typing.Optional[int]

### Quality
- **Type**: typing.Optional[int]


# FrameRate

### Denominator
- **Type**: typing.Optional[int]

### Numerator
- **Type**: typing.Optional[int]


# GetJobRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResponse

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobTemplateRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobTemplateResponse

### JobTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyResponse

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Policy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# GetPresetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetPresetResponse

### Preset
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Preset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueueRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueResponse

### Queue
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Queue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# GifSettings

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'INTERPOLATE']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]


# H264QvbrSettings

### MaxAverageBitrate
- **Type**: typing.Optional[int]

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### QvbrQualityLevelFineTune
- **Type**: typing.Optional[float]


# H264Settings

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### BandwidthReductionFilter
- **Type**: <class 'NoneType'>

### Bitrate
- **Type**: typing.Optional[int]

### CodecLevel
- **Type**: typing.Optional[typing.Literal['AUTO', 'LEVEL_1', 'LEVEL_1_1', 'LEVEL_1_2', 'LEVEL_1_3', 'LEVEL_2', 'LEVEL_2_1', 'LEVEL_2_2', 'LEVEL_3', 'LEVEL_3_1', 'LEVEL_3_2', 'LEVEL_4', 'LEVEL_4_1', 'LEVEL_4_2', 'LEVEL_5', 'LEVEL_5_1', 'LEVEL_5_2']]

### CodecProfile
- **Type**: typing.Optional[typing.Literal['BASELINE', 'HIGH', 'HIGH_10BIT', 'HIGH_422', 'HIGH_422_10BIT', 'MAIN']]

### DynamicSubGop
- **Type**: typing.Optional[typing.Literal['ADAPTIVE', 'STATIC']]

### EndOfStreamMarkers
- **Type**: typing.Optional[typing.Literal['INCLUDE', 'SUPPRESS']]

### EntropyEncoding
- **Type**: typing.Optional[typing.Literal['CABAC', 'CAVLC']]

### FieldEncoding
- **Type**: typing.Optional[typing.Literal['FORCE_FIELD', 'MBAFF', 'PAFF']]

### FlickerAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### GopBReference
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### GopClosedCadence
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### GopSizeUnits
- **Type**: typing.Optional[typing.Literal['AUTO', 'FRAMES', 'SECONDS']]

### HrdBufferFinalFillPercentage
- **Type**: typing.Optional[int]

### HrdBufferInitialFillPercentage
- **Type**: typing.Optional[int]

### HrdBufferSize
- **Type**: typing.Optional[int]

### InterlaceMode
- **Type**: typing.Optional[typing.Literal['BOTTOM_FIELD', 'FOLLOW_BOTTOM_FIELD', 'FOLLOW_TOP_FIELD', 'PROGRESSIVE', 'TOP_FIELD']]

### MaxBitrate
- **Type**: typing.Optional[int]

### MinIInterval
- **Type**: typing.Optional[int]

### NumberBFramesBetweenReferenceFrames
- **Type**: typing.Optional[int]

### NumberReferenceFrames
- **Type**: typing.Optional[int]

### ParControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### QualityTuningLevel
- **Type**: typing.Optional[typing.Literal['MULTI_PASS_HQ', 'SINGLE_PASS', 'SINGLE_PASS_HQ']]

### QvbrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.H264QvbrSettings]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'QVBR', 'VBR']]

### RepeatPps
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SaliencyAwareEncoding
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PREFERRED']]

### ScanTypeConversionMode
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'INTERLACED_OPTIMIZE']]

### SceneChangeDetect
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'TRANSITION_DETECTION']]

### Slices
- **Type**: typing.Optional[int]

### SlowPal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Softness
- **Type**: typing.Optional[int]

### SpatialAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Syntax
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'RP2027']]

### Telecine
- **Type**: typing.Optional[typing.Literal['HARD', 'NONE', 'SOFT']]

### TemporalAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UnregisteredSeiTimecode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### WriteMp4PackagingType
- **Type**: typing.Optional[typing.Literal['AVC1', 'AVC3']]


# H265QvbrSettings

### MaxAverageBitrate
- **Type**: typing.Optional[int]

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### QvbrQualityLevelFineTune
- **Type**: typing.Optional[float]


# H265Settings

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### AlternateTransferFunctionSei
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### BandwidthReductionFilter
- **Type**: <class 'NoneType'>

### Bitrate
- **Type**: typing.Optional[int]

### CodecLevel
- **Type**: typing.Optional[typing.Literal['AUTO', 'LEVEL_1', 'LEVEL_2', 'LEVEL_2_1', 'LEVEL_3', 'LEVEL_3_1', 'LEVEL_4', 'LEVEL_4_1', 'LEVEL_5', 'LEVEL_5_1', 'LEVEL_5_2', 'LEVEL_6', 'LEVEL_6_1', 'LEVEL_6_2']]

### CodecProfile
- **Type**: typing.Optional[typing.Literal['MAIN10_HIGH', 'MAIN10_MAIN', 'MAIN_422_10BIT_HIGH', 'MAIN_422_10BIT_MAIN', 'MAIN_422_8BIT_HIGH', 'MAIN_422_8BIT_MAIN', 'MAIN_HIGH', 'MAIN_MAIN']]

### Deblocking
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DynamicSubGop
- **Type**: typing.Optional[typing.Literal['ADAPTIVE', 'STATIC']]

### EndOfStreamMarkers
- **Type**: typing.Optional[typing.Literal['INCLUDE', 'SUPPRESS']]

### FlickerAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### GopBReference
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### GopClosedCadence
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### GopSizeUnits
- **Type**: typing.Optional[typing.Literal['AUTO', 'FRAMES', 'SECONDS']]

### HrdBufferFinalFillPercentage
- **Type**: typing.Optional[int]

### HrdBufferInitialFillPercentage
- **Type**: typing.Optional[int]

### HrdBufferSize
- **Type**: typing.Optional[int]

### InterlaceMode
- **Type**: typing.Optional[typing.Literal['BOTTOM_FIELD', 'FOLLOW_BOTTOM_FIELD', 'FOLLOW_TOP_FIELD', 'PROGRESSIVE', 'TOP_FIELD']]

### MaxBitrate
- **Type**: typing.Optional[int]

### MinIInterval
- **Type**: typing.Optional[int]

### NumberBFramesBetweenReferenceFrames
- **Type**: typing.Optional[int]

### NumberReferenceFrames
- **Type**: typing.Optional[int]

### ParControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### QualityTuningLevel
- **Type**: typing.Optional[typing.Literal['MULTI_PASS_HQ', 'SINGLE_PASS', 'SINGLE_PASS_HQ']]

### QvbrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.H265QvbrSettings]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'QVBR', 'VBR']]

### SampleAdaptiveOffsetFilterMode
- **Type**: typing.Optional[typing.Literal['ADAPTIVE', 'DEFAULT', 'OFF']]

### ScanTypeConversionMode
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'INTERLACED_OPTIMIZE']]

### SceneChangeDetect
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'TRANSITION_DETECTION']]

### Slices
- **Type**: typing.Optional[int]

### SlowPal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SpatialAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Telecine
- **Type**: typing.Optional[typing.Literal['HARD', 'NONE', 'SOFT']]

### TemporalAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TemporalIds
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Tiles
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UnregisteredSeiTimecode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### WriteMp4PackagingType
- **Type**: typing.Optional[typing.Literal['HEV1', 'HVC1']]


# Hdr10Metadata

### BluePrimaryX
- **Type**: typing.Optional[int]

### BluePrimaryY
- **Type**: typing.Optional[int]

### GreenPrimaryX
- **Type**: typing.Optional[int]

### GreenPrimaryY
- **Type**: typing.Optional[int]

### MaxContentLightLevel
- **Type**: typing.Optional[int]

### MaxFrameAverageLightLevel
- **Type**: typing.Optional[int]

### MaxLuminance
- **Type**: typing.Optional[int]

### MinLuminance
- **Type**: typing.Optional[int]

### RedPrimaryX
- **Type**: typing.Optional[int]

### RedPrimaryY
- **Type**: typing.Optional[int]

### WhitePointX
- **Type**: typing.Optional[int]

### WhitePointY
- **Type**: typing.Optional[int]


# Hdr10Plus

### MasteringMonitorNits
- **Type**: typing.Optional[int]

### TargetMonitorNits
- **Type**: typing.Optional[int]


# HlsAdditionalManifest

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.Sequence[str]]


# HlsAdditionalManifestOutput

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# HlsCaptionLanguageMapping

### CaptionChannel
- **Type**: typing.Optional[int]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageDescription
- **Type**: typing.Optional[str]


# HlsEncryptionSettings

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HlsEncryptionSettingsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HlsGroupSettings

### AdMarkers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ELEMENTAL', 'ELEMENTAL_SCTE35']]]

### AdditionalManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsAdditionalManifest]]

### AudioOnlyHeader
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### BaseUrl
- **Type**: typing.Optional[str]

### CaptionLanguageMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsCaptionLanguageMapping]]

### CaptionLanguageSetting
- **Type**: typing.Optional[typing.Literal['INSERT', 'NONE', 'OMIT']]

### CaptionSegmentLengthControl
- **Type**: typing.Optional[typing.Literal['LARGE_SEGMENTS', 'MATCH_VIDEO']]

### ClientCache
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CodecSpecification
- **Type**: typing.Optional[typing.Literal['RFC_4281', 'RFC_6381']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: <class 'NoneType'>

### DirectoryStructure
- **Type**: typing.Optional[typing.Literal['SINGLE_DIRECTORY', 'SUBDIRECTORY_PER_STREAM']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsEncryptionSettings]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsImageBasedTrickPlaySettings]

### ManifestCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### ManifestDurationFormat
- **Type**: typing.Optional[typing.Literal['FLOATING_POINT', 'INTEGER']]

### MinFinalSegmentLength
- **Type**: typing.Optional[float]

### MinSegmentLength
- **Type**: typing.Optional[int]

### OutputSelection
- **Type**: typing.Optional[typing.Literal['MANIFESTS_AND_SEGMENTS', 'SEGMENTS_ONLY']]

### ProgramDateTime
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### ProgramDateTimePeriod
- **Type**: typing.Optional[int]

### ProgressiveWriteHlsManifest
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SegmentControl
- **Type**: typing.Optional[typing.Literal['SEGMENTED_FILES', 'SINGLE_FILE']]

### SegmentLength
- **Type**: typing.Optional[int]

### SegmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### SegmentsPerSubdirectory
- **Type**: typing.Optional[int]

### StreamInfResolution
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### TargetDurationCompatibilityMode
- **Type**: typing.Optional[typing.Literal['LEGACY', 'SPEC_COMPLIANT']]

### TimedMetadataId3Frame
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIV', 'TDRL']]

### TimedMetadataId3Period
- **Type**: typing.Optional[int]

### TimestampDeltaMilliseconds
- **Type**: typing.Optional[int]


# HlsGroupSettingsOutput

### AdMarkers
- **Type**: typing.Optional[typing.List[typing.Literal['ELEMENTAL', 'ELEMENTAL_SCTE35']]]

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsAdditionalManifestOutput]]

### AudioOnlyHeader
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### BaseUrl
- **Type**: typing.Optional[str]

### CaptionLanguageMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsCaptionLanguageMapping]]

### CaptionLanguageSetting
- **Type**: typing.Optional[typing.Literal['INSERT', 'NONE', 'OMIT']]

### CaptionSegmentLengthControl
- **Type**: typing.Optional[typing.Literal['LARGE_SEGMENTS', 'MATCH_VIDEO']]

### ClientCache
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CodecSpecification
- **Type**: typing.Optional[typing.Literal['RFC_4281', 'RFC_6381']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: <class 'NoneType'>

### DirectoryStructure
- **Type**: typing.Optional[typing.Literal['SINGLE_DIRECTORY', 'SUBDIRECTORY_PER_STREAM']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsEncryptionSettingsOutput]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsImageBasedTrickPlaySettings]

### ManifestCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### ManifestDurationFormat
- **Type**: typing.Optional[typing.Literal['FLOATING_POINT', 'INTEGER']]

### MinFinalSegmentLength
- **Type**: typing.Optional[float]

### MinSegmentLength
- **Type**: typing.Optional[int]

### OutputSelection
- **Type**: typing.Optional[typing.Literal['MANIFESTS_AND_SEGMENTS', 'SEGMENTS_ONLY']]

### ProgramDateTime
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### ProgramDateTimePeriod
- **Type**: typing.Optional[int]

### ProgressiveWriteHlsManifest
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SegmentControl
- **Type**: typing.Optional[typing.Literal['SEGMENTED_FILES', 'SINGLE_FILE']]

### SegmentLength
- **Type**: typing.Optional[int]

### SegmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### SegmentsPerSubdirectory
- **Type**: typing.Optional[int]

### StreamInfResolution
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### TargetDurationCompatibilityMode
- **Type**: typing.Optional[typing.Literal['LEGACY', 'SPEC_COMPLIANT']]

### TimedMetadataId3Frame
- **Type**: typing.Optional[typing.Literal['NONE', 'PRIV', 'TDRL']]

### TimedMetadataId3Period
- **Type**: typing.Optional[int]

### TimestampDeltaMilliseconds
- **Type**: typing.Optional[int]


# HlsImageBasedTrickPlaySettings

### IntervalCadence
- **Type**: typing.Optional[typing.Literal['FOLLOW_CUSTOM', 'FOLLOW_IFRAME']]

### ThumbnailHeight
- **Type**: typing.Optional[int]

### ThumbnailInterval
- **Type**: typing.Optional[float]

### ThumbnailWidth
- **Type**: typing.Optional[int]

### TileHeight
- **Type**: typing.Optional[int]

### TileWidth
- **Type**: typing.Optional[int]


# HlsRenditionGroupSettings

### RenditionGroupId
- **Type**: typing.Optional[str]

### RenditionLanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### RenditionName
- **Type**: typing.Optional[str]


# HlsSettings

### AudioGroupId
- **Type**: typing.Optional[str]

### AudioOnlyContainer
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'M2TS']]

### AudioRenditionSets
- **Type**: typing.Optional[str]

### AudioTrackType
- **Type**: typing.Optional[typing.Literal['ALTERNATE_AUDIO_AUTO_SELECT', 'ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT', 'ALTERNATE_AUDIO_NOT_AUTO_SELECT', 'AUDIO_ONLY_VARIANT_STREAM']]

### DescriptiveVideoServiceFlag
- **Type**: typing.Optional[typing.Literal['DONT_FLAG', 'FLAG']]

### IFrameOnlyManifest
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### SegmentModifier
- **Type**: typing.Optional[str]


# HopDestination

### Priority
- **Type**: typing.Optional[int]

### Queue
- **Type**: typing.Optional[str]

### WaitMinutes
- **Type**: typing.Optional[int]


# Id3Insertion

### Id3
- **Type**: typing.Optional[str]

### Timecode
- **Type**: typing.Optional[str]


# ImageInserter

### InsertableImages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.InsertableImage]]

### SdrReferenceWhiteLevel
- **Type**: typing.Optional[int]


# ImageInserterOutput

### InsertableImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InsertableImage]]

### SdrReferenceWhiteLevel
- **Type**: typing.Optional[int]


# ImscDestinationSettings

### Accessibility
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### StylePassthrough
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# Input

### AdvancedInputFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdvancedInputFilterSettings
- **Type**: <class 'NoneType'>

### AudioSelectorGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorGroup]]

### AudioSelectors
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelector]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSelector]]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DecryptionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.InputDecryptionSettings]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DolbyVisionMetadataXml
- **Type**: typing.Optional[str]

### DynamicAudioSelectors
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.DynamicAudioSelector]]

### FileInput
- **Type**: typing.Optional[str]

### FilterEnable
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLE', 'FORCE']]

### FilterStrength
- **Type**: typing.Optional[int]

### ImageInserter
- **Type**: <class 'NoneType'>

### InputClippings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.InputClipping]]

### InputScanType
- **Type**: typing.Optional[typing.Literal['AUTO', 'PSF']]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### ProgramNumber
- **Type**: typing.Optional[int]

### PsiControl
- **Type**: typing.Optional[typing.Literal['IGNORE_PSI', 'USE_PSI']]

### SupplementalImps
- **Type**: typing.Optional[typing.Sequence[str]]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]

### VideoGenerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.InputVideoGenerator]

### VideoOverlays
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlay]]

### VideoSelector
- **Type**: <class 'NoneType'>


# InputClipping

### EndTimecode
- **Type**: typing.Optional[str]

### StartTimecode
- **Type**: typing.Optional[str]


# InputDecryptionSettings

### DecryptionMode
- **Type**: typing.Optional[typing.Literal['AES_CBC', 'AES_CTR', 'AES_GCM']]

### EncryptedDecryptionKey
- **Type**: typing.Optional[str]

### InitializationVector
- **Type**: typing.Optional[str]

### KmsKeyRegion
- **Type**: typing.Optional[str]


# InputOutput

### AdvancedInputFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdvancedInputFilterSettings
- **Type**: <class 'NoneType'>

### AudioSelectorGroups
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorGroupOutput]]

### AudioSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorOutput]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSelector]]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DecryptionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.InputDecryptionSettings]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DolbyVisionMetadataXml
- **Type**: typing.Optional[str]

### DynamicAudioSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.DynamicAudioSelector]]

### FileInput
- **Type**: typing.Optional[str]

### FilterEnable
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLE', 'FORCE']]

### FilterStrength
- **Type**: typing.Optional[int]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterOutput]

### InputClippings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputClipping]]

### InputScanType
- **Type**: typing.Optional[typing.Literal['AUTO', 'PSF']]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### ProgramNumber
- **Type**: typing.Optional[int]

### PsiControl
- **Type**: typing.Optional[typing.Literal['IGNORE_PSI', 'USE_PSI']]

### SupplementalImps
- **Type**: typing.Optional[typing.List[str]]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]

### VideoGenerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.InputVideoGenerator]

### VideoOverlays
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayOutput]]

### VideoSelector
- **Type**: <class 'NoneType'>


# InputTemplate

### AdvancedInputFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdvancedInputFilterSettings
- **Type**: <class 'NoneType'>

### AudioSelectorGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorGroup]]

### AudioSelectors
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelector]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSelector]]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DolbyVisionMetadataXml
- **Type**: typing.Optional[str]

### DynamicAudioSelectors
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.DynamicAudioSelector]]

### FilterEnable
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLE', 'FORCE']]

### FilterStrength
- **Type**: typing.Optional[int]

### ImageInserter
- **Type**: <class 'NoneType'>

### InputClippings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.InputClipping]]

### InputScanType
- **Type**: typing.Optional[typing.Literal['AUTO', 'PSF']]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### ProgramNumber
- **Type**: typing.Optional[int]

### PsiControl
- **Type**: typing.Optional[typing.Literal['IGNORE_PSI', 'USE_PSI']]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]

### VideoOverlays
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlay]]

### VideoSelector
- **Type**: <class 'NoneType'>


# InputTemplateOutput

### AdvancedInputFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdvancedInputFilterSettings
- **Type**: <class 'NoneType'>

### AudioSelectorGroups
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorGroupOutput]]

### AudioSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorOutput]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSelector]]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DolbyVisionMetadataXml
- **Type**: typing.Optional[str]

### DynamicAudioSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.DynamicAudioSelector]]

### FilterEnable
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLE', 'FORCE']]

### FilterStrength
- **Type**: typing.Optional[int]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterOutput]

### InputClippings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputClipping]]

### InputScanType
- **Type**: typing.Optional[typing.Literal['AUTO', 'PSF']]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### ProgramNumber
- **Type**: typing.Optional[int]

### PsiControl
- **Type**: typing.Optional[typing.Literal['IGNORE_PSI', 'USE_PSI']]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]

### VideoOverlays
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayOutput]]

### VideoSelector
- **Type**: <class 'NoneType'>


# InputVideoGenerator

### Channels
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]


# InsertableImage

### Duration
- **Type**: typing.Optional[int]

### FadeIn
- **Type**: typing.Optional[int]

### FadeOut
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### ImageInserterInput
- **Type**: typing.Optional[str]

### ImageX
- **Type**: typing.Optional[int]

### ImageY
- **Type**: typing.Optional[int]

### Layer
- **Type**: typing.Optional[int]

### Opacity
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[str]

### Width
- **Type**: typing.Optional[int]


# Job

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobSettingsOutput'>
- **Required**: Yes

### AccelerationSettings
- **Type**: <class 'NoneType'>

### AccelerationStatus
- **Type**: typing.Optional[typing.Literal['ACCELERATED', 'IN_PROGRESS', 'NOT_ACCELERATED', 'NOT_APPLICABLE']]

### Arn
- **Type**: typing.Optional[str]

### BillingTagsSource
- **Type**: typing.Optional[typing.Literal['JOB', 'JOB_TEMPLATE', 'PRESET', 'QUEUE']]

### ClientRequestToken
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### CurrentPhase
- **Type**: typing.Optional[typing.Literal['PROBING', 'TRANSCODING', 'UPLOADING']]

### ErrorCode
- **Type**: typing.Optional[int]

### ErrorMessage
- **Type**: typing.Optional[str]

### HopDestinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.HopDestination]]

### Id
- **Type**: typing.Optional[str]

### JobEngineVersionRequested
- **Type**: typing.Optional[str]

### JobEngineVersionUsed
- **Type**: typing.Optional[str]

### JobPercentComplete
- **Type**: typing.Optional[int]

### JobTemplate
- **Type**: typing.Optional[str]

### Messages
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.JobMessages]

### OutputGroupDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupDetail]]

### Priority
- **Type**: typing.Optional[int]

### Queue
- **Type**: typing.Optional[str]

### QueueTransitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.QueueTransition]]

### RetryCount
- **Type**: typing.Optional[int]

### SimulateReservedQueue
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETE', 'ERROR', 'PROGRESSING', 'SUBMITTED']]

### StatusUpdateInterval
- **Type**: typing.Optional[typing.Literal['SECONDS_10', 'SECONDS_12', 'SECONDS_120', 'SECONDS_15', 'SECONDS_180', 'SECONDS_20', 'SECONDS_240', 'SECONDS_30', 'SECONDS_300', 'SECONDS_360', 'SECONDS_420', 'SECONDS_480', 'SECONDS_540', 'SECONDS_60', 'SECONDS_600']]

### Timing
- **Type**: <class 'NoneType'>

### UserMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### Warnings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.WarningGroup]]


# JobEngineVersion

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]

### Version
- **Type**: typing.Optional[str]


# JobMessages

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobSettings

### AdAvailOffset
- **Type**: typing.Optional[int]

### AvailBlanking
- **Type**: <class 'NoneType'>

### ColorConversion3DLUTSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorConversion3DLUTSetting]]

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSettings]

### ExtendedDataServices
- **Type**: <class 'NoneType'>

### FollowSource
- **Type**: typing.Optional[int]

### Inputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.Input]]

### KantarWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.KantarWatermarkSettings]

### MotionImageInserter
- **Type**: <class 'NoneType'>

### NielsenConfiguration
- **Type**: <class 'NoneType'>

### NielsenNonLinearWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenNonLinearWatermarkSettings]

### OutputGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroup]]

### TimecodeConfig
- **Type**: <class 'NoneType'>

### TimedMetadataInsertion
- **Type**: <class 'NoneType'>


# JobSettingsOutput

### AdAvailOffset
- **Type**: typing.Optional[int]

### AvailBlanking
- **Type**: <class 'NoneType'>

### ColorConversion3DLUTSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorConversion3DLUTSetting]]

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSettings]

### ExtendedDataServices
- **Type**: <class 'NoneType'>

### FollowSource
- **Type**: typing.Optional[int]

### Inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputOutput]]

### KantarWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.KantarWatermarkSettings]

### MotionImageInserter
- **Type**: <class 'NoneType'>

### NielsenConfiguration
- **Type**: <class 'NoneType'>

### NielsenNonLinearWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenNonLinearWatermarkSettings]

### OutputGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupOutput]]

### TimecodeConfig
- **Type**: <class 'NoneType'>

### TimedMetadataInsertion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimedMetadataInsertionOutput]


# JobSettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobTemplate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobTemplateSettings

### AdAvailOffset
- **Type**: typing.Optional[int]

### AvailBlanking
- **Type**: <class 'NoneType'>

### ColorConversion3DLUTSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorConversion3DLUTSetting]]

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSettings]

### ExtendedDataServices
- **Type**: <class 'NoneType'>

### FollowSource
- **Type**: typing.Optional[int]

### Inputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.InputTemplate]]

### KantarWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.KantarWatermarkSettings]

### MotionImageInserter
- **Type**: <class 'NoneType'>

### NielsenConfiguration
- **Type**: <class 'NoneType'>

### NielsenNonLinearWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenNonLinearWatermarkSettings]

### OutputGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroup]]

### TimecodeConfig
- **Type**: <class 'NoneType'>

### TimedMetadataInsertion
- **Type**: <class 'NoneType'>


# JobTemplateSettingsOutput

### AdAvailOffset
- **Type**: typing.Optional[int]

### AvailBlanking
- **Type**: <class 'NoneType'>

### ColorConversion3DLUTSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorConversion3DLUTSetting]]

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSettings]

### ExtendedDataServices
- **Type**: <class 'NoneType'>

### FollowSource
- **Type**: typing.Optional[int]

### Inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputTemplateOutput]]

### KantarWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.KantarWatermarkSettings]

### MotionImageInserter
- **Type**: <class 'NoneType'>

### NielsenConfiguration
- **Type**: <class 'NoneType'>

### NielsenNonLinearWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenNonLinearWatermarkSettings]

### OutputGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupOutput]]

### TimecodeConfig
- **Type**: <class 'NoneType'>

### TimedMetadataInsertion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimedMetadataInsertionOutput]


# JobTemplateSettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KantarWatermarkSettings

### ChannelName
- **Type**: typing.Optional[str]

### ContentReference
- **Type**: typing.Optional[str]

### CredentialsSecretName
- **Type**: typing.Optional[str]

### FileOffset
- **Type**: typing.Optional[float]

### KantarLicenseId
- **Type**: typing.Optional[int]

### KantarServerUrl
- **Type**: typing.Optional[str]

### LogDestination
- **Type**: typing.Optional[str]

### Metadata3
- **Type**: typing.Optional[str]

### Metadata4
- **Type**: typing.Optional[str]

### Metadata5
- **Type**: typing.Optional[str]

### Metadata6
- **Type**: typing.Optional[str]

### Metadata7
- **Type**: typing.Optional[str]

### Metadata8
- **Type**: typing.Optional[str]


# ListJobTemplatesRequest

### Category
- **Type**: typing.Optional[str]

### ListBy
- **Type**: typing.Optional[typing.Literal['CREATION_DATE', 'NAME', 'SYSTEM']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListJobTemplatesRequestPaginate

### Category
- **Type**: typing.Optional[str]

### ListBy
- **Type**: typing.Optional[typing.Literal['CREATION_DATE', 'NAME', 'SYSTEM']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfig]


# ListJobTemplatesResponse

### JobTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Queue
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETE', 'ERROR', 'PROGRESSING', 'SUBMITTED']]


# ListJobsRequestPaginate

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Queue
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETE', 'ERROR', 'PROGRESSING', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfig]


# ListJobsResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPresetsRequest

### Category
- **Type**: typing.Optional[str]

### ListBy
- **Type**: typing.Optional[typing.Literal['CREATION_DATE', 'NAME', 'SYSTEM']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListPresetsRequestPaginate

### Category
- **Type**: typing.Optional[str]

### ListBy
- **Type**: typing.Optional[typing.Literal['CREATION_DATE', 'NAME', 'SYSTEM']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfig]


# ListPresetsResponse

### Presets
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.Preset]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueuesRequest

### ListBy
- **Type**: typing.Optional[typing.Literal['CREATION_DATE', 'NAME']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListQueuesRequestPaginate

### ListBy
- **Type**: typing.Optional[typing.Literal['CREATION_DATE', 'NAME']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfig]


# ListQueuesResponse

### Queues
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.Queue]
- **Required**: Yes

### TotalConcurrentJobs
- **Type**: <class 'int'>
- **Required**: Yes

### UnallocatedConcurrentJobs
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### ResourceTags
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResourceTags'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# ListVersionsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVersionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfig]


# ListVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.JobEngineVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# M2tsScte35Esam

### Scte35EsamPid
- **Type**: typing.Optional[int]


# M2tsSettings

### AudioBufferModel
- **Type**: typing.Optional[typing.Literal['ATSC', 'DVB']]

### AudioDuration
- **Type**: typing.Optional[typing.Literal['DEFAULT_CODEC_DURATION', 'MATCH_VIDEO_DURATION']]

### AudioFramesPerPes
- **Type**: typing.Optional[int]

### AudioPids
- **Type**: typing.Optional[typing.Sequence[int]]

### Bitrate
- **Type**: typing.Optional[int]

### BufferModel
- **Type**: typing.Optional[typing.Literal['MULTIPLEX', 'NONE']]

### DataPTSControl
- **Type**: typing.Optional[typing.Literal['ALIGN_TO_VIDEO', 'AUTO']]

### DvbNitSettings
- **Type**: <class 'NoneType'>

### DvbSdtSettings
- **Type**: <class 'NoneType'>

### DvbSubPids
- **Type**: typing.Optional[typing.Sequence[int]]

### DvbTdtSettings
- **Type**: <class 'NoneType'>

### DvbTeletextPid
- **Type**: typing.Optional[int]

### EbpAudioInterval
- **Type**: typing.Optional[typing.Literal['VIDEO_AND_FIXED_INTERVALS', 'VIDEO_INTERVAL']]

### EbpPlacement
- **Type**: typing.Optional[typing.Literal['VIDEO_AND_AUDIO_PIDS', 'VIDEO_PID']]

### EsRateInPes
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### ForceTsVideoEbpOrder
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'FORCE']]

### FragmentTime
- **Type**: typing.Optional[float]

### KlvMetadata
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### MaxPcrInterval
- **Type**: typing.Optional[int]

### MinEbpInterval
- **Type**: typing.Optional[int]

### NielsenId3
- **Type**: typing.Optional[typing.Literal['INSERT', 'NONE']]

### NullPacketBitrate
- **Type**: typing.Optional[float]

### PatInterval
- **Type**: typing.Optional[int]

### PcrControl
- **Type**: typing.Optional[typing.Literal['CONFIGURED_PCR_PERIOD', 'PCR_EVERY_PES_PACKET']]

### PcrPid
- **Type**: typing.Optional[int]

### PmtInterval
- **Type**: typing.Optional[int]

### PmtPid
- **Type**: typing.Optional[int]

### PreventBufferUnderflow
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### PrivateMetadataPid
- **Type**: typing.Optional[int]

### ProgramNumber
- **Type**: typing.Optional[int]

### PtsOffset
- **Type**: typing.Optional[int]

### PtsOffsetMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'SECONDS']]

### RateMode
- **Type**: typing.Optional[typing.Literal['CBR', 'VBR']]

### Scte35Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M2tsScte35Esam]

### Scte35Pid
- **Type**: typing.Optional[int]

### Scte35Source
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### SegmentationMarkers
- **Type**: typing.Optional[typing.Literal['EBP', 'EBP_LEGACY', 'NONE', 'PSI_SEGSTART', 'RAI_ADAPT', 'RAI_SEGSTART']]

### SegmentationStyle
- **Type**: typing.Optional[typing.Literal['MAINTAIN_CADENCE', 'RESET_CADENCE']]

### SegmentationTime
- **Type**: typing.Optional[float]

### TimedMetadataPid
- **Type**: typing.Optional[int]

### TransportStreamId
- **Type**: typing.Optional[int]

### VideoPid
- **Type**: typing.Optional[int]


# M2tsSettingsOutput

### AudioBufferModel
- **Type**: typing.Optional[typing.Literal['ATSC', 'DVB']]

### AudioDuration
- **Type**: typing.Optional[typing.Literal['DEFAULT_CODEC_DURATION', 'MATCH_VIDEO_DURATION']]

### AudioFramesPerPes
- **Type**: typing.Optional[int]

### AudioPids
- **Type**: typing.Optional[typing.List[int]]

### Bitrate
- **Type**: typing.Optional[int]

### BufferModel
- **Type**: typing.Optional[typing.Literal['MULTIPLEX', 'NONE']]

### DataPTSControl
- **Type**: typing.Optional[typing.Literal['ALIGN_TO_VIDEO', 'AUTO']]

### DvbNitSettings
- **Type**: <class 'NoneType'>

### DvbSdtSettings
- **Type**: <class 'NoneType'>

### DvbSubPids
- **Type**: typing.Optional[typing.List[int]]

### DvbTdtSettings
- **Type**: <class 'NoneType'>

### DvbTeletextPid
- **Type**: typing.Optional[int]

### EbpAudioInterval
- **Type**: typing.Optional[typing.Literal['VIDEO_AND_FIXED_INTERVALS', 'VIDEO_INTERVAL']]

### EbpPlacement
- **Type**: typing.Optional[typing.Literal['VIDEO_AND_AUDIO_PIDS', 'VIDEO_PID']]

### EsRateInPes
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### ForceTsVideoEbpOrder
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'FORCE']]

### FragmentTime
- **Type**: typing.Optional[float]

### KlvMetadata
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### MaxPcrInterval
- **Type**: typing.Optional[int]

### MinEbpInterval
- **Type**: typing.Optional[int]

### NielsenId3
- **Type**: typing.Optional[typing.Literal['INSERT', 'NONE']]

### NullPacketBitrate
- **Type**: typing.Optional[float]

### PatInterval
- **Type**: typing.Optional[int]

### PcrControl
- **Type**: typing.Optional[typing.Literal['CONFIGURED_PCR_PERIOD', 'PCR_EVERY_PES_PACKET']]

### PcrPid
- **Type**: typing.Optional[int]

### PmtInterval
- **Type**: typing.Optional[int]

### PmtPid
- **Type**: typing.Optional[int]

### PreventBufferUnderflow
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### PrivateMetadataPid
- **Type**: typing.Optional[int]

### ProgramNumber
- **Type**: typing.Optional[int]

### PtsOffset
- **Type**: typing.Optional[int]

### PtsOffsetMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'SECONDS']]

### RateMode
- **Type**: typing.Optional[typing.Literal['CBR', 'VBR']]

### Scte35Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M2tsScte35Esam]

### Scte35Pid
- **Type**: typing.Optional[int]

### Scte35Source
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### SegmentationMarkers
- **Type**: typing.Optional[typing.Literal['EBP', 'EBP_LEGACY', 'NONE', 'PSI_SEGSTART', 'RAI_ADAPT', 'RAI_SEGSTART']]

### SegmentationStyle
- **Type**: typing.Optional[typing.Literal['MAINTAIN_CADENCE', 'RESET_CADENCE']]

### SegmentationTime
- **Type**: typing.Optional[float]

### TimedMetadataPid
- **Type**: typing.Optional[int]

### TransportStreamId
- **Type**: typing.Optional[int]

### VideoPid
- **Type**: typing.Optional[int]


# M3u8Settings

### AudioDuration
- **Type**: typing.Optional[typing.Literal['DEFAULT_CODEC_DURATION', 'MATCH_VIDEO_DURATION']]

### AudioFramesPerPes
- **Type**: typing.Optional[int]

### AudioPids
- **Type**: typing.Optional[typing.Sequence[int]]

### DataPTSControl
- **Type**: typing.Optional[typing.Literal['ALIGN_TO_VIDEO', 'AUTO']]

### MaxPcrInterval
- **Type**: typing.Optional[int]

### NielsenId3
- **Type**: typing.Optional[typing.Literal['INSERT', 'NONE']]

### PatInterval
- **Type**: typing.Optional[int]

### PcrControl
- **Type**: typing.Optional[typing.Literal['CONFIGURED_PCR_PERIOD', 'PCR_EVERY_PES_PACKET']]

### PcrPid
- **Type**: typing.Optional[int]

### PmtInterval
- **Type**: typing.Optional[int]

### PmtPid
- **Type**: typing.Optional[int]

### PrivateMetadataPid
- **Type**: typing.Optional[int]

### ProgramNumber
- **Type**: typing.Optional[int]

### PtsOffset
- **Type**: typing.Optional[int]

### PtsOffsetMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'SECONDS']]

### Scte35Pid
- **Type**: typing.Optional[int]

### Scte35Source
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### TimedMetadata
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### TimedMetadataPid
- **Type**: typing.Optional[int]

### TransportStreamId
- **Type**: typing.Optional[int]

### VideoPid
- **Type**: typing.Optional[int]


# M3u8SettingsOutput

### AudioDuration
- **Type**: typing.Optional[typing.Literal['DEFAULT_CODEC_DURATION', 'MATCH_VIDEO_DURATION']]

### AudioFramesPerPes
- **Type**: typing.Optional[int]

### AudioPids
- **Type**: typing.Optional[typing.List[int]]

### DataPTSControl
- **Type**: typing.Optional[typing.Literal['ALIGN_TO_VIDEO', 'AUTO']]

### MaxPcrInterval
- **Type**: typing.Optional[int]

### NielsenId3
- **Type**: typing.Optional[typing.Literal['INSERT', 'NONE']]

### PatInterval
- **Type**: typing.Optional[int]

### PcrControl
- **Type**: typing.Optional[typing.Literal['CONFIGURED_PCR_PERIOD', 'PCR_EVERY_PES_PACKET']]

### PcrPid
- **Type**: typing.Optional[int]

### PmtInterval
- **Type**: typing.Optional[int]

### PmtPid
- **Type**: typing.Optional[int]

### PrivateMetadataPid
- **Type**: typing.Optional[int]

### ProgramNumber
- **Type**: typing.Optional[int]

### PtsOffset
- **Type**: typing.Optional[int]

### PtsOffsetMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'SECONDS']]

### Scte35Pid
- **Type**: typing.Optional[int]

### Scte35Source
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### TimedMetadata
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### TimedMetadataPid
- **Type**: typing.Optional[int]

### TransportStreamId
- **Type**: typing.Optional[int]

### VideoPid
- **Type**: typing.Optional[int]


# Metadata

### ETag
- **Type**: typing.Optional[str]

### FileSize
- **Type**: typing.Optional[int]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### MimeType
- **Type**: typing.Optional[str]


# MinBottomRenditionSize

### Height
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# MinTopRenditionSize

### Height
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# MotionImageInserter

### Framerate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MotionImageInsertionFramerate]

### Input
- **Type**: typing.Optional[str]

### InsertionMode
- **Type**: typing.Optional[typing.Literal['MOV', 'PNG']]

### Offset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MotionImageInsertionOffset]

### Playback
- **Type**: typing.Optional[typing.Literal['ONCE', 'REPEAT']]

### StartTime
- **Type**: typing.Optional[str]


# MotionImageInsertionFramerate

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]


# MotionImageInsertionOffset

### ImageX
- **Type**: typing.Optional[int]

### ImageY
- **Type**: typing.Optional[int]


# MovSettings

### ClapAtom
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### CslgAtom
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### Mpeg2FourCCControl
- **Type**: typing.Optional[typing.Literal['MPEG', 'XDCAM']]

### PaddingControl
- **Type**: typing.Optional[typing.Literal['NONE', 'OMNEON']]

### Reference
- **Type**: typing.Optional[typing.Literal['EXTERNAL', 'SELF_CONTAINED']]


# Mp2Settings

### Bitrate
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]


# Mp3Settings

### Bitrate
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'VBR']]

### SampleRate
- **Type**: typing.Optional[int]

### VbrQuality
- **Type**: typing.Optional[int]


# Mp4Settings

### AudioDuration
- **Type**: typing.Optional[typing.Literal['DEFAULT_CODEC_DURATION', 'MATCH_VIDEO_DURATION']]

### CslgAtom
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### CttsVersion
- **Type**: typing.Optional[int]

### FreeSpaceBox
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### MoovPlacement
- **Type**: typing.Optional[typing.Literal['NORMAL', 'PROGRESSIVE_DOWNLOAD']]

### Mp4MajorBrand
- **Type**: typing.Optional[str]


# MpdSettings

### AccessibilityCaptionHints
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### AudioDuration
- **Type**: typing.Optional[typing.Literal['DEFAULT_CODEC_DURATION', 'MATCH_VIDEO_DURATION']]

### CaptionContainerType
- **Type**: typing.Optional[typing.Literal['FRAGMENTED_MP4', 'RAW']]

### KlvMetadata
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### ManifestMetadataSignaling
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Scte35Esam
- **Type**: typing.Optional[typing.Literal['INSERT', 'NONE']]

### Scte35Source
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### TimedMetadata
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH']]

### TimedMetadataBoxVersion
- **Type**: typing.Optional[typing.Literal['VERSION_0', 'VERSION_1']]

### TimedMetadataSchemeIdUri
- **Type**: typing.Optional[str]

### TimedMetadataValue
- **Type**: typing.Optional[str]


# Mpeg2Settings

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'OFF']]

### Bitrate
- **Type**: typing.Optional[int]

### CodecLevel
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGH1440', 'LOW', 'MAIN']]

### CodecProfile
- **Type**: typing.Optional[typing.Literal['MAIN', 'PROFILE_422']]

### DynamicSubGop
- **Type**: typing.Optional[typing.Literal['ADAPTIVE', 'STATIC']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### GopClosedCadence
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### GopSizeUnits
- **Type**: typing.Optional[typing.Literal['FRAMES', 'SECONDS']]

### HrdBufferFinalFillPercentage
- **Type**: typing.Optional[int]

### HrdBufferInitialFillPercentage
- **Type**: typing.Optional[int]

### HrdBufferSize
- **Type**: typing.Optional[int]

### InterlaceMode
- **Type**: typing.Optional[typing.Literal['BOTTOM_FIELD', 'FOLLOW_BOTTOM_FIELD', 'FOLLOW_TOP_FIELD', 'PROGRESSIVE', 'TOP_FIELD']]

### IntraDcPrecision
- **Type**: typing.Optional[typing.Literal['AUTO', 'INTRA_DC_PRECISION_10', 'INTRA_DC_PRECISION_11', 'INTRA_DC_PRECISION_8', 'INTRA_DC_PRECISION_9']]

### MaxBitrate
- **Type**: typing.Optional[int]

### MinIInterval
- **Type**: typing.Optional[int]

### NumberBFramesBetweenReferenceFrames
- **Type**: typing.Optional[int]

### ParControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### QualityTuningLevel
- **Type**: typing.Optional[typing.Literal['MULTI_PASS', 'SINGLE_PASS']]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'VBR']]

### ScanTypeConversionMode
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'INTERLACED_OPTIMIZE']]

### SceneChangeDetect
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SlowPal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Softness
- **Type**: typing.Optional[int]

### SpatialAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Syntax
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'D_10']]

### Telecine
- **Type**: typing.Optional[typing.Literal['HARD', 'NONE', 'SOFT']]

### TemporalAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MsSmoothAdditionalManifest

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.Sequence[str]]


# MsSmoothAdditionalManifestOutput

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# MsSmoothEncryptionSettings

### SpekeKeyProvider
- **Type**: <class 'NoneType'>


# MsSmoothEncryptionSettingsOutput

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderOutput]


# MsSmoothGroupSettings

### AdditionalManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothAdditionalManifest]]

### AudioDeduplication
- **Type**: typing.Optional[typing.Literal['COMBINE_DUPLICATE_STREAMS', 'NONE']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: <class 'NoneType'>

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothEncryptionSettings]

### FragmentLength
- **Type**: typing.Optional[int]

### FragmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### ManifestEncoding
- **Type**: typing.Optional[typing.Literal['UTF16', 'UTF8']]


# MsSmoothGroupSettingsOutput

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothAdditionalManifestOutput]]

### AudioDeduplication
- **Type**: typing.Optional[typing.Literal['COMBINE_DUPLICATE_STREAMS', 'NONE']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: <class 'NoneType'>

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothEncryptionSettingsOutput]

### FragmentLength
- **Type**: typing.Optional[int]

### FragmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### ManifestEncoding
- **Type**: typing.Optional[typing.Literal['UTF16', 'UTF8']]


# MxfSettings

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['COPY_FROM_VIDEO', 'NO_COPY']]

### Profile
- **Type**: typing.Optional[typing.Literal['D_10', 'OP1A', 'XAVC', 'XDCAM', 'XDCAM_RDD9']]

### XavcProfileSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MxfXavcProfileSettings]


# MxfXavcProfileSettings

### DurationMode
- **Type**: typing.Optional[typing.Literal['ALLOW_ANY_DURATION', 'DROP_FRAMES_FOR_COMPLIANCE']]

### MaxAncDataSize
- **Type**: typing.Optional[int]


# NexGuardFileMarkerSettings

### License
- **Type**: typing.Optional[str]

### Payload
- **Type**: typing.Optional[int]

### Preset
- **Type**: typing.Optional[str]

### Strength
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'LIGHTER', 'LIGHTEST', 'STRONGER', 'STRONGEST']]


# NielsenConfiguration

### BreakoutCode
- **Type**: typing.Optional[int]

### DistributorId
- **Type**: typing.Optional[str]


# NielsenNonLinearWatermarkSettings

### ActiveWatermarkProcess
- **Type**: typing.Optional[typing.Literal['CBET', 'NAES2_AND_NW', 'NAES2_AND_NW_AND_CBET']]

### AdiFilename
- **Type**: typing.Optional[str]

### AssetId
- **Type**: typing.Optional[str]

### AssetName
- **Type**: typing.Optional[str]

### CbetSourceId
- **Type**: typing.Optional[str]

### EpisodeId
- **Type**: typing.Optional[str]

### MetadataDestination
- **Type**: typing.Optional[str]

### SourceId
- **Type**: typing.Optional[int]

### SourceWatermarkStatus
- **Type**: typing.Optional[typing.Literal['CLEAN', 'WATERMARKED']]

### TicServerUrl
- **Type**: typing.Optional[str]

### UniqueTicPerAudioTrack
- **Type**: typing.Optional[typing.Literal['RESERVE_UNIQUE_TICS_PER_TRACK', 'SAME_TICS_PER_TRACK']]


# NoiseReducer

### Filter
- **Type**: typing.Optional[typing.Literal['BILATERAL', 'CONSERVE', 'GAUSSIAN', 'LANCZOS', 'MEAN', 'SHARPEN', 'SPATIAL', 'TEMPORAL']]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NoiseReducerFilterSettings]

### SpatialFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NoiseReducerSpatialFilterSettings]

### TemporalFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NoiseReducerTemporalFilterSettings]


# NoiseReducerFilterSettings

### Strength
- **Type**: typing.Optional[int]


# NoiseReducerSpatialFilterSettings

### PostFilterSharpenStrength
- **Type**: typing.Optional[int]

### Speed
- **Type**: typing.Optional[int]

### Strength
- **Type**: typing.Optional[int]


# NoiseReducerTemporalFilterSettings

### AggressiveMode
- **Type**: typing.Optional[int]

### PostTemporalSharpening
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'ENABLED']]

### PostTemporalSharpeningStrength
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Speed
- **Type**: typing.Optional[int]

### Strength
- **Type**: typing.Optional[int]


# OpusSettings

### Bitrate
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]


# Output

### AudioDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioDescription]]

### CaptionDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDescription]]

### ContainerSettings
- **Type**: <class 'NoneType'>

### Extension
- **Type**: typing.Optional[str]

### NameModifier
- **Type**: typing.Optional[str]

### OutputSettings
- **Type**: <class 'NoneType'>

### Preset
- **Type**: typing.Optional[str]

### VideoDescription
- **Type**: <class 'NoneType'>


# OutputChannelMapping

### InputChannels
- **Type**: typing.Optional[typing.Sequence[int]]

### InputChannelsFineTune
- **Type**: typing.Optional[typing.Sequence[float]]


# OutputChannelMappingOutput

### InputChannels
- **Type**: typing.Optional[typing.List[int]]

### InputChannelsFineTune
- **Type**: typing.Optional[typing.List[float]]


# OutputDetail

### DurationInMs
- **Type**: typing.Optional[int]

### VideoDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoDetail]


# OutputGroup

### AutomatedEncodingSettings
- **Type**: <class 'NoneType'>

### CustomName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### OutputGroupSettings
- **Type**: <class 'NoneType'>

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.Output]]


# OutputGroupDetail

### OutputDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputDetail]]


# OutputGroupOutput

### AutomatedEncodingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedEncodingSettingsOutput]

### CustomName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### OutputGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupSettingsOutput]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.Extra]]


# OutputGroupSettings

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OutputGroupSettingsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OutputSettings

### HlsSettings
- **Type**: <class 'NoneType'>


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartnerWatermarking

### NexguardFileMarkerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NexGuardFileMarkerSettings]


# Policy

### HttpInputs
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'DISALLOWED']]

### HttpsInputs
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'DISALLOWED']]

### S3Inputs
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'DISALLOWED']]


# Preset

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PresetSettings

### AudioDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioDescription]]

### CaptionDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDescriptionPreset]]

### ContainerSettings
- **Type**: <class 'NoneType'>

### VideoDescription
- **Type**: <class 'NoneType'>


# PresetSettingsOutput

### AudioDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioDescriptionOutput]]

### CaptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDescriptionPresetOutput]]

### ContainerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ContainerSettingsOutput]

### VideoDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoDescriptionOutput]


# PresetSettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProbeInputFile

### FileUrl
- **Type**: typing.Optional[str]


# ProbeRequest

### InputFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.ProbeInputFile]]


# ProbeResponse

### ProbeResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.ProbeResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# ProbeResult

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProresSettings

### ChromaSampling
- **Type**: typing.Optional[typing.Literal['PRESERVE_444_SAMPLING', 'SUBSAMPLE_TO_422']]

### CodecProfile
- **Type**: typing.Optional[typing.Literal['APPLE_PRORES_422', 'APPLE_PRORES_422_HQ', 'APPLE_PRORES_422_LT', 'APPLE_PRORES_422_PROXY', 'APPLE_PRORES_4444', 'APPLE_PRORES_4444_XQ']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### InterlaceMode
- **Type**: typing.Optional[typing.Literal['BOTTOM_FIELD', 'FOLLOW_BOTTOM_FIELD', 'FOLLOW_TOP_FIELD', 'PROGRESSIVE', 'TOP_FIELD']]

### ParControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### ScanTypeConversionMode
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'INTERLACED_OPTIMIZE']]

### SlowPal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Telecine
- **Type**: typing.Optional[typing.Literal['HARD', 'NONE']]


# PutPolicyRequest

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Policy'>
- **Required**: Yes


# PutPolicyResponse

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Policy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# Queue

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueueTransition

### DestinationQueue
- **Type**: typing.Optional[str]

### SourceQueue
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# Rectangle

### Height
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]

### X
- **Type**: typing.Optional[int]

### Y
- **Type**: typing.Optional[int]


# RemixSettings

### AudioDescriptionAudioChannel
- **Type**: typing.Optional[int]

### AudioDescriptionDataChannel
- **Type**: typing.Optional[int]

### ChannelMapping
- **Type**: <class 'NoneType'>

### ChannelsIn
- **Type**: typing.Optional[int]

### ChannelsOut
- **Type**: typing.Optional[int]


# RemixSettingsOutput

### AudioDescriptionAudioChannel
- **Type**: typing.Optional[int]

### AudioDescriptionDataChannel
- **Type**: typing.Optional[int]

### ChannelMapping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ChannelMappingOutput]

### ChannelsIn
- **Type**: typing.Optional[int]

### ChannelsOut
- **Type**: typing.Optional[int]


# ReservationPlan

### Commitment
- **Type**: typing.Optional[typing.Literal['ONE_YEAR']]

### ExpiresAt
- **Type**: typing.Optional[datetime.datetime]

### PurchasedAt
- **Type**: typing.Optional[datetime.datetime]

### RenewalType
- **Type**: typing.Optional[typing.Literal['AUTO_RENEW', 'EXPIRE']]

### ReservedSlots
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'EXPIRED']]


# ReservationPlanSettings

### Commitment
- **Type**: typing.Literal['ONE_YEAR']
- **Required**: Yes

### RenewalType
- **Type**: typing.Literal['AUTO_RENEW', 'EXPIRE']
- **Required**: Yes

### ReservedSlots
- **Type**: <class 'int'>
- **Required**: Yes


# ResourceTags

### Arn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# S3DestinationAccessControl

### CannedAcl
- **Type**: typing.Optional[typing.Literal['AUTHENTICATED_READ', 'BUCKET_OWNER_FULL_CONTROL', 'BUCKET_OWNER_READ', 'PUBLIC_READ']]


# S3DestinationSettings

### AccessControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.S3DestinationAccessControl]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.S3EncryptionSettings]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'REDUCED_REDUNDANCY', 'STANDARD', 'STANDARD_IA']]


# S3EncryptionSettings

### EncryptionType
- **Type**: typing.Optional[typing.Literal['SERVER_SIDE_ENCRYPTION_KMS', 'SERVER_SIDE_ENCRYPTION_S3']]

### KmsEncryptionContext
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]


# SccDestinationSettings

### Framerate
- **Type**: typing.Optional[typing.Literal['FRAMERATE_23_97', 'FRAMERATE_24', 'FRAMERATE_25', 'FRAMERATE_29_97_DROPFRAME', 'FRAMERATE_29_97_NON_DROPFRAME']]


# SearchJobsRequest

### InputFile
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Queue
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETE', 'ERROR', 'PROGRESSING', 'SUBMITTED']]


# SearchJobsRequestPaginate

### InputFile
- **Type**: typing.Optional[str]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Queue
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETE', 'ERROR', 'PROGRESSING', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfig]


# SearchJobsResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ServiceOverride

### Message
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### OverrideValue
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# SpekeKeyProvider

### CertificateArn
- **Type**: typing.Optional[str]

### EncryptionContractConfiguration
- **Type**: <class 'NoneType'>

### ResourceId
- **Type**: typing.Optional[str]

### SystemIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Url
- **Type**: typing.Optional[str]


# SpekeKeyProviderCmaf

### CertificateArn
- **Type**: typing.Optional[str]

### DashSignaledSystemIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EncryptionContractConfiguration
- **Type**: <class 'NoneType'>

### HlsSignaledSystemIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# SpekeKeyProviderCmafOutput

### CertificateArn
- **Type**: typing.Optional[str]

### DashSignaledSystemIds
- **Type**: typing.Optional[typing.List[str]]

### EncryptionContractConfiguration
- **Type**: <class 'NoneType'>

### HlsSignaledSystemIds
- **Type**: typing.Optional[typing.List[str]]

### ResourceId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# SpekeKeyProviderOutput

### CertificateArn
- **Type**: typing.Optional[str]

### EncryptionContractConfiguration
- **Type**: <class 'NoneType'>

### ResourceId
- **Type**: typing.Optional[str]

### SystemIds
- **Type**: typing.Optional[typing.List[str]]

### Url
- **Type**: typing.Optional[str]


# SrtDestinationSettings

### StylePassthrough
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# StaticKeyProvider

### KeyFormat
- **Type**: typing.Optional[str]

### KeyFormatVersions
- **Type**: typing.Optional[str]

### StaticKeyValue
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# TagResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TeletextDestinationSettings

### PageNumber
- **Type**: typing.Optional[str]

### PageTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PAGE_TYPE_ADDL_INFO', 'PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE', 'PAGE_TYPE_INITIAL', 'PAGE_TYPE_PROGRAM_SCHEDULE', 'PAGE_TYPE_SUBTITLE']]]


# TeletextDestinationSettingsOutput

### PageNumber
- **Type**: typing.Optional[str]

### PageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['PAGE_TYPE_ADDL_INFO', 'PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE', 'PAGE_TYPE_INITIAL', 'PAGE_TYPE_PROGRAM_SCHEDULE', 'PAGE_TYPE_SUBTITLE']]]


# TeletextSourceSettings

### PageNumber
- **Type**: typing.Optional[str]


# TimecodeBurnin

### FontSize
- **Type**: typing.Optional[int]

### Position
- **Type**: typing.Optional[typing.Literal['BOTTOM_CENTER', 'BOTTOM_LEFT', 'BOTTOM_RIGHT', 'MIDDLE_CENTER', 'MIDDLE_LEFT', 'MIDDLE_RIGHT', 'TOP_CENTER', 'TOP_LEFT', 'TOP_RIGHT']]

### Prefix
- **Type**: typing.Optional[str]


# TimecodeConfig

### Anchor
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### Start
- **Type**: typing.Optional[str]

### TimestampOffset
- **Type**: typing.Optional[str]


# TimedMetadataInsertion

### Id3Insertions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.Id3Insertion]]


# TimedMetadataInsertionOutput

### Id3Insertions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.Id3Insertion]]


# Timing

### FinishTime
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]


# Track

### AudioProperties
- **Type**: <class 'NoneType'>

### Codec
- **Type**: typing.Optional[typing.Literal['AAC', 'AC3', 'AV1', 'AVC', 'C608', 'C708', 'EAC3', 'FLAC', 'HEVC', 'MJPEG', 'MP3', 'MP4V', 'MPEG2', 'OPUS', 'PCM', 'PRORES', 'THEORA', 'UNKNOWN', 'VORBIS', 'VP8', 'VP9', 'WEBVTT']]

### DataProperties
- **Type**: <class 'NoneType'>

### Duration
- **Type**: typing.Optional[float]

### Index
- **Type**: typing.Optional[int]

### TrackType
- **Type**: typing.Optional[typing.Literal['audio', 'data', 'video']]

### VideoProperties
- **Type**: <class 'NoneType'>


# TrackMapping

### AudioTrackIndexes
- **Type**: typing.Optional[typing.List[int]]

### DataTrackIndexes
- **Type**: typing.Optional[typing.List[int]]

### VideoTrackIndexes
- **Type**: typing.Optional[typing.List[int]]


# TrackSourceSettings

### TrackNumber
- **Type**: typing.Optional[int]


# TtmlDestinationSettings

### StylePassthrough
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UncompressedSettings

### Fourcc
- **Type**: typing.Optional[typing.Literal['I420', 'I422', 'I444']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### InterlaceMode
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'PROGRESSIVE']]

### ScanTypeConversionMode
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'INTERLACED_OPTIMIZE']]

### SlowPal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Telecine
- **Type**: typing.Optional[typing.Literal['HARD', 'NONE']]


# UntagResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateJobTemplateRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccelerationSettings
- **Type**: <class 'NoneType'>

### Category
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### HopDestinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.HopDestination]]

### Priority
- **Type**: typing.Optional[int]

### Queue
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplateSettingsUnion]

### StatusUpdateInterval
- **Type**: typing.Optional[typing.Literal['SECONDS_10', 'SECONDS_12', 'SECONDS_120', 'SECONDS_15', 'SECONDS_180', 'SECONDS_20', 'SECONDS_240', 'SECONDS_30', 'SECONDS_300', 'SECONDS_360', 'SECONDS_420', 'SECONDS_480', 'SECONDS_540', 'SECONDS_60', 'SECONDS_600']]


# UpdateJobTemplateResponse

### JobTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePresetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Category
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PresetSettingsUnion]


# UpdatePresetResponse

### Preset
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Preset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateQueueRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConcurrentJobs
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### ReservationPlanSettings
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PAUSED']]


# UpdateQueueResponse

### Queue
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.Queue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadata'>
- **Required**: Yes


# Vc3Settings

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### InterlaceMode
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'PROGRESSIVE']]

### ScanTypeConversionMode
- **Type**: typing.Optional[typing.Literal['INTERLACED', 'INTERLACED_OPTIMIZE']]

### SlowPal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Telecine
- **Type**: typing.Optional[typing.Literal['HARD', 'NONE']]

### Vc3Class
- **Type**: typing.Optional[typing.Literal['CLASS_145_8BIT', 'CLASS_220_10BIT', 'CLASS_220_8BIT']]


# VideoCodecSettings

### Av1Settings
- **Type**: <class 'NoneType'>

### AvcIntraSettings
- **Type**: <class 'NoneType'>

### Codec
- **Type**: typing.Optional[typing.Literal['AV1', 'AVC_INTRA', 'FRAME_CAPTURE', 'GIF', 'H_264', 'H_265', 'MPEG2', 'PASSTHROUGH', 'PRORES', 'UNCOMPRESSED', 'VC3', 'VP8', 'VP9', 'XAVC']]

### FrameCaptureSettings
- **Type**: <class 'NoneType'>

### GifSettings
- **Type**: <class 'NoneType'>

### H264Settings
- **Type**: <class 'NoneType'>

### H265Settings
- **Type**: <class 'NoneType'>

### Mpeg2Settings
- **Type**: <class 'NoneType'>

### ProresSettings
- **Type**: <class 'NoneType'>

### UncompressedSettings
- **Type**: <class 'NoneType'>

### Vc3Settings
- **Type**: <class 'NoneType'>

### Vp8Settings
- **Type**: <class 'NoneType'>

### Vp9Settings
- **Type**: <class 'NoneType'>

### XavcSettings
- **Type**: <class 'NoneType'>


# VideoDescription

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### AntiAlias
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ChromaPositionMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'FORCE_CENTER', 'FORCE_TOP_LEFT']]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoCodecSettings]

### ColorMetadata
- **Type**: typing.Optional[typing.Literal['IGNORE', 'INSERT']]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### DropFrameTimecode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FixedAfd
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### RespondToAfd
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH', 'RESPOND']]

### ScalingBehavior
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'FILL', 'FIT', 'FIT_NO_UPSCALE', 'STRETCH_TO_OUTPUT']]

### Sharpness
- **Type**: typing.Optional[int]

### TimecodeInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PIC_TIMING_SEI']]

### TimecodeTrack
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### VideoPreprocessors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoPreprocessor]

### Width
- **Type**: typing.Optional[int]


# VideoDescriptionOutput

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### AntiAlias
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ChromaPositionMode
- **Type**: typing.Optional[typing.Literal['AUTO', 'FORCE_CENTER', 'FORCE_TOP_LEFT']]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoCodecSettings]

### ColorMetadata
- **Type**: typing.Optional[typing.Literal['IGNORE', 'INSERT']]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### DropFrameTimecode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FixedAfd
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Rectangle]

### RespondToAfd
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH', 'RESPOND']]

### ScalingBehavior
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'FILL', 'FIT', 'FIT_NO_UPSCALE', 'STRETCH_TO_OUTPUT']]

### Sharpness
- **Type**: typing.Optional[int]

### TimecodeInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PIC_TIMING_SEI']]

### TimecodeTrack
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### VideoPreprocessors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoPreprocessorOutput]

### Width
- **Type**: typing.Optional[int]


# VideoDetail

### HeightInPx
- **Type**: typing.Optional[int]

### WidthInPx
- **Type**: typing.Optional[int]


# VideoOverlay

### EndTimecode
- **Type**: typing.Optional[str]

### InitialPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayPosition]

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayInput]

### Playback
- **Type**: typing.Optional[typing.Literal['ONCE', 'REPEAT']]

### StartTimecode
- **Type**: typing.Optional[str]

### Transitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayTransition]]


# VideoOverlayInput

### FileInput
- **Type**: typing.Optional[str]

### InputClippings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayInputClipping]]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]


# VideoOverlayInputClipping

### EndTimecode
- **Type**: typing.Optional[str]

### StartTimecode
- **Type**: typing.Optional[str]


# VideoOverlayInputOutput

### FileInput
- **Type**: typing.Optional[str]

### InputClippings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayInputClipping]]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]


# VideoOverlayOutput

### EndTimecode
- **Type**: typing.Optional[str]

### InitialPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayPosition]

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayInputOutput]

### Playback
- **Type**: typing.Optional[typing.Literal['ONCE', 'REPEAT']]

### StartTimecode
- **Type**: typing.Optional[str]

### Transitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayTransition]]


# VideoOverlayPosition

### Height
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['PERCENTAGE', 'PIXELS']]

### Width
- **Type**: typing.Optional[int]

### XPosition
- **Type**: typing.Optional[int]

### YPosition
- **Type**: typing.Optional[int]


# VideoOverlayTransition

### EndPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayPosition]

### EndTimecode
- **Type**: typing.Optional[str]

### StartTimecode
- **Type**: typing.Optional[str]


# VideoPreprocessor

### ColorCorrector
- **Type**: <class 'NoneType'>

### Deinterlacer
- **Type**: <class 'NoneType'>

### DolbyVision
- **Type**: <class 'NoneType'>

### Hdr10Plus
- **Type**: <class 'NoneType'>

### ImageInserter
- **Type**: <class 'NoneType'>

### NoiseReducer
- **Type**: <class 'NoneType'>

### PartnerWatermarking
- **Type**: <class 'NoneType'>

### TimecodeBurnin
- **Type**: <class 'NoneType'>


# VideoPreprocessorOutput

### ColorCorrector
- **Type**: <class 'NoneType'>

### Deinterlacer
- **Type**: <class 'NoneType'>

### DolbyVision
- **Type**: <class 'NoneType'>

### Hdr10Plus
- **Type**: <class 'NoneType'>

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterOutput]

### NoiseReducer
- **Type**: <class 'NoneType'>

### PartnerWatermarking
- **Type**: <class 'NoneType'>

### TimecodeBurnin
- **Type**: <class 'NoneType'>


# VideoProperties

### BitDepth
- **Type**: typing.Optional[int]

### BitRate
- **Type**: typing.Optional[int]

### ColorPrimaries
- **Type**: typing.Optional[typing.Literal['EBU_3213_E', 'GENERIC_FILM', 'IPT', 'ITU_2020', 'ITU_470BG', 'ITU_470M', 'ITU_709', 'LAST', 'RESERVED', 'SMPTE_170M', 'SMPTE_2067XYZ', 'SMPTE_240M', 'SMPTE_428_1', 'SMPTE_431_2', 'SMPTE_EG_432_1', 'UNSPECIFIED']]

### FrameRate
- **Type**: <class 'NoneType'>

### Height
- **Type**: typing.Optional[int]

### MatrixCoefficients
- **Type**: typing.Optional[typing.Literal['CD_CL', 'CD_NCL', 'EBU3213', 'FCC', 'IPT', 'ITU_2020_CL', 'ITU_2020_NCL', 'ITU_2100ICtCp', 'ITU_470BG', 'ITU_709', 'LAST', 'RESERVED', 'RGB', 'SMPTE_170M', 'SMPTE_2085', 'SMPTE_240M', 'UNSPECIFIED', 'YCgCo']]

### TransferCharacteristics
- **Type**: typing.Optional[typing.Literal['ARIB_B67', 'IEC_61966_2_1', 'IEC_61966_2_4', 'ITU_1361', 'ITU_2020_10bit', 'ITU_2020_12bit', 'ITU_470BG', 'ITU_470M', 'ITU_709', 'LAST', 'LINEAR', 'LOC10_2_5', 'LOG10_2', 'RESERVED', 'SMPTE_170M', 'SMPTE_2084', 'SMPTE_240M', 'SMPTE_428_1', 'UNSPECIFIED']]

### Width
- **Type**: typing.Optional[int]


# VideoSelector

### AlphaBehavior
- **Type**: typing.Optional[typing.Literal['DISCARD', 'REMAP_TO_LUMA']]

### ColorSpace
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'HDR10', 'HLG_2020', 'P3D65_HDR', 'P3D65_SDR', 'P3DCI', 'REC_601', 'REC_709']]

### ColorSpaceUsage
- **Type**: typing.Optional[typing.Literal['FALLBACK', 'FORCE']]

### EmbeddedTimecodeOverride
- **Type**: typing.Optional[typing.Literal['NONE', 'USE_MDPM']]

### Hdr10Metadata
- **Type**: <class 'NoneType'>

### MaxLuminance
- **Type**: typing.Optional[int]

### PadVideo
- **Type**: typing.Optional[typing.Literal['BLACK', 'DISABLED']]

### Pid
- **Type**: typing.Optional[int]

### ProgramNumber
- **Type**: typing.Optional[int]

### Rotate
- **Type**: typing.Optional[typing.Literal['AUTO', 'DEGREES_180', 'DEGREES_270', 'DEGREES_90', 'DEGREE_0']]

### SampleRange
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'FULL_RANGE', 'LIMITED_RANGE']]


# VorbisSettings

### Channels
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]

### VbrQuality
- **Type**: typing.Optional[int]


# Vp8Settings

### Bitrate
- **Type**: typing.Optional[int]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### HrdBufferSize
- **Type**: typing.Optional[int]

### MaxBitrate
- **Type**: typing.Optional[int]

### ParControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### QualityTuningLevel
- **Type**: typing.Optional[typing.Literal['MULTI_PASS', 'MULTI_PASS_HQ']]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['VBR']]


# Vp9Settings

### Bitrate
- **Type**: typing.Optional[int]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### GopSize
- **Type**: typing.Optional[float]

### HrdBufferSize
- **Type**: typing.Optional[int]

### MaxBitrate
- **Type**: typing.Optional[int]

### ParControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### ParDenominator
- **Type**: typing.Optional[int]

### ParNumerator
- **Type**: typing.Optional[int]

### QualityTuningLevel
- **Type**: typing.Optional[typing.Literal['MULTI_PASS', 'MULTI_PASS_HQ']]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['VBR']]


# WarningGroup

### Code
- **Type**: <class 'int'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes


# WavSettings

### BitDepth
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### Format
- **Type**: typing.Optional[typing.Literal['EXTENSIBLE', 'RF64', 'RIFF']]

### SampleRate
- **Type**: typing.Optional[int]


# WebvttDestinationSettings

### Accessibility
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### StylePassthrough
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'MERGE', 'STRICT']]


# WebvttHlsSourceSettings

### RenditionGroupId
- **Type**: typing.Optional[str]

### RenditionLanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### RenditionName
- **Type**: typing.Optional[str]


# Xavc4kIntraCbgProfileSettings

### XavcClass
- **Type**: typing.Optional[typing.Literal['CLASS_100', 'CLASS_300', 'CLASS_480']]


# Xavc4kIntraVbrProfileSettings

### XavcClass
- **Type**: typing.Optional[typing.Literal['CLASS_100', 'CLASS_300', 'CLASS_480']]


# Xavc4kProfileSettings

### BitrateClass
- **Type**: typing.Optional[typing.Literal['BITRATE_CLASS_100', 'BITRATE_CLASS_140', 'BITRATE_CLASS_200']]

### CodecProfile
- **Type**: typing.Optional[typing.Literal['HIGH', 'HIGH_422']]

### FlickerAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### GopBReference
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### GopClosedCadence
- **Type**: typing.Optional[int]

### HrdBufferSize
- **Type**: typing.Optional[int]

### QualityTuningLevel
- **Type**: typing.Optional[typing.Literal['MULTI_PASS_HQ', 'SINGLE_PASS', 'SINGLE_PASS_HQ']]

### Slices
- **Type**: typing.Optional[int]


# XavcHdIntraCbgProfileSettings

### XavcClass
- **Type**: typing.Optional[typing.Literal['CLASS_100', 'CLASS_200', 'CLASS_50']]


# XavcHdProfileSettings

### BitrateClass
- **Type**: typing.Optional[typing.Literal['BITRATE_CLASS_25', 'BITRATE_CLASS_35', 'BITRATE_CLASS_50']]

### FlickerAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### GopBReference
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### GopClosedCadence
- **Type**: typing.Optional[int]

### HrdBufferSize
- **Type**: typing.Optional[int]

### InterlaceMode
- **Type**: typing.Optional[typing.Literal['BOTTOM_FIELD', 'FOLLOW_BOTTOM_FIELD', 'FOLLOW_TOP_FIELD', 'PROGRESSIVE', 'TOP_FIELD']]

### QualityTuningLevel
- **Type**: typing.Optional[typing.Literal['MULTI_PASS_HQ', 'SINGLE_PASS', 'SINGLE_PASS_HQ']]

### Slices
- **Type**: typing.Optional[int]

### Telecine
- **Type**: typing.Optional[typing.Literal['HARD', 'NONE']]


# XavcSettings

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### EntropyEncoding
- **Type**: typing.Optional[typing.Literal['AUTO', 'CABAC', 'CAVLC']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE', 'MAINTAIN_FRAME_COUNT']]

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### Profile
- **Type**: typing.Optional[typing.Literal['XAVC_4K', 'XAVC_4K_INTRA_CBG', 'XAVC_4K_INTRA_VBR', 'XAVC_HD', 'XAVC_HD_INTRA_CBG']]

### SlowPal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Softness
- **Type**: typing.Optional[int]

### SpatialAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TemporalAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Xavc4kIntraCbgProfileSettings
- **Type**: <class 'NoneType'>

### Xavc4kIntraVbrProfileSettings
- **Type**: <class 'NoneType'>

### Xavc4kProfileSettings
- **Type**: <class 'NoneType'>

### XavcHdIntraCbgProfileSettings
- **Type**: <class 'NoneType'>

### XavcHdProfileSettings
- **Type**: <class 'NoneType'>


