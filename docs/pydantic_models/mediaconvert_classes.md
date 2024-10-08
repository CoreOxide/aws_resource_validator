# Pydantic Models in mediaconvert_classes

# AacSettingsTypeDef

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


# Ac3SettingsTypeDef

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


# AccelerationSettingsTypeDef

### Mode
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'PREFERRED']
- **Required**: Yes


# AdvancedInputFilterSettingsTypeDef

### AddTexture
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Sharpening
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'OFF']]


# AiffSettingsTypeDef

### BitDepth
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]


# AllowedRenditionSizeTypeDef

### Height
- **Type**: typing.Optional[int]

### Required
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Width
- **Type**: typing.Optional[int]


# AncillarySourceSettingsTypeDef

### Convert608To708
- **Type**: typing.Optional[typing.Literal['DISABLED', 'UPCONVERT']]

### SourceAncillaryChannelNumber
- **Type**: typing.Optional[int]

### TerminateCaptions
- **Type**: typing.Optional[typing.Literal['DISABLED', 'END_OF_INPUT']]


# AssociateCertificateRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# AudioChannelTaggingSettingsExtraOutputTypeDef

### ChannelTag
- **Type**: typing.Optional[typing.Literal['C', 'CS', 'HI', 'L', 'LC', 'LFE', 'LFE2', 'LS', 'LSD', 'LT', 'LW', 'M', 'NAR', 'R', 'RC', 'RS', 'RSD', 'RSL', 'RSR', 'RT', 'RW', 'TBC', 'TBL', 'TBR', 'TCS', 'VHC', 'VHL', 'VHR']]

### ChannelTags
- **Type**: typing.Optional[typing.List[typing.Literal['C', 'CS', 'HI', 'L', 'LC', 'LFE', 'LFE2', 'LS', 'LSD', 'LT', 'LW', 'M', 'NAR', 'R', 'RC', 'RS', 'RSD', 'RSL', 'RSR', 'RT', 'RW', 'TBC', 'TBL', 'TBR', 'TCS', 'VHC', 'VHL', 'VHR']]]


# AudioChannelTaggingSettingsOutputTypeDef

### ChannelTag
- **Type**: typing.Optional[typing.Literal['C', 'CS', 'HI', 'L', 'LC', 'LFE', 'LFE2', 'LS', 'LSD', 'LT', 'LW', 'M', 'NAR', 'R', 'RC', 'RS', 'RSD', 'RSL', 'RSR', 'RT', 'RW', 'TBC', 'TBL', 'TBR', 'TCS', 'VHC', 'VHL', 'VHR']]

### ChannelTags
- **Type**: typing.Optional[typing.List[typing.Literal['C', 'CS', 'HI', 'L', 'LC', 'LFE', 'LFE2', 'LS', 'LSD', 'LT', 'LW', 'M', 'NAR', 'R', 'RC', 'RS', 'RSD', 'RSL', 'RSR', 'RT', 'RW', 'TBC', 'TBL', 'TBR', 'TCS', 'VHC', 'VHL', 'VHR']]]


# AudioChannelTaggingSettingsTypeDef

### ChannelTag
- **Type**: typing.Optional[typing.Literal['C', 'CS', 'HI', 'L', 'LC', 'LFE', 'LFE2', 'LS', 'LSD', 'LT', 'LW', 'M', 'NAR', 'R', 'RC', 'RS', 'RSD', 'RSL', 'RSR', 'RT', 'RW', 'TBC', 'TBL', 'TBR', 'TCS', 'VHC', 'VHL', 'VHR']]

### ChannelTags
- **Type**: typing.Optional[typing.Sequence[typing.Literal['C', 'CS', 'HI', 'L', 'LC', 'LFE', 'LFE2', 'LS', 'LSD', 'LT', 'LW', 'M', 'NAR', 'R', 'RC', 'RS', 'RSD', 'RSL', 'RSR', 'RT', 'RW', 'TBC', 'TBL', 'TBR', 'TCS', 'VHC', 'VHL', 'VHR']]]


# AudioCodecSettingsTypeDef

### AacSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AacSettingsTypeDef]

### Ac3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Ac3SettingsTypeDef]

### AiffSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AiffSettingsTypeDef]

### Codec
- **Type**: typing.Optional[typing.Literal['AAC', 'AC3', 'AIFF', 'EAC3', 'EAC3_ATMOS', 'FLAC', 'MP2', 'MP3', 'OPUS', 'PASSTHROUGH', 'VORBIS', 'WAV']]

### Eac3AtmosSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Eac3AtmosSettingsTypeDef]

### Eac3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Eac3SettingsTypeDef]

### FlacSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.FlacSettingsTypeDef]

### Mp2Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Mp2SettingsTypeDef]

### Mp3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Mp3SettingsTypeDef]

### OpusSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.OpusSettingsTypeDef]

### VorbisSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VorbisSettingsTypeDef]

### WavSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.WavSettingsTypeDef]


# AudioDescriptionExtraOutputTypeDef

### AudioChannelTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioChannelTaggingSettingsExtraOutputTypeDef]

### AudioNormalizationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioNormalizationSettingsTypeDef]

### AudioSourceName
- **Type**: typing.Optional[str]

### AudioType
- **Type**: typing.Optional[int]

### AudioTypeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioCodecSettingsTypeDef]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageCodeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RemixSettingsExtraOutputTypeDef]

### StreamName
- **Type**: typing.Optional[str]


# AudioDescriptionOutputTypeDef

### AudioChannelTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioChannelTaggingSettingsOutputTypeDef]

### AudioNormalizationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioNormalizationSettingsTypeDef]

### AudioSourceName
- **Type**: typing.Optional[str]

### AudioType
- **Type**: typing.Optional[int]

### AudioTypeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioCodecSettingsTypeDef]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageCodeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RemixSettingsOutputTypeDef]

### StreamName
- **Type**: typing.Optional[str]


# AudioDescriptionTypeDef

### AudioChannelTaggingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioChannelTaggingSettingsTypeDef]

### AudioNormalizationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioNormalizationSettingsTypeDef]

### AudioSourceName
- **Type**: typing.Optional[str]

### AudioType
- **Type**: typing.Optional[int]

### AudioTypeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioCodecSettingsTypeDef]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageCodeControl
- **Type**: typing.Optional[typing.Literal['FOLLOW_INPUT', 'USE_CONFIGURED']]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RemixSettingsTypeDef]

### StreamName
- **Type**: typing.Optional[str]


# AudioNormalizationSettingsTypeDef

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


# AudioSelectorExtraOutputTypeDef

### AudioDurationCorrection
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'FRAME', 'TRACK']]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DefaultSelection
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NOT_DEFAULT']]

### ExternalAudioFileInput
- **Type**: typing.Optional[str]

### HlsRenditionGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsRenditionGroupSettingsTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### Offset
- **Type**: typing.Optional[int]

### Pids
- **Type**: typing.Optional[typing.List[int]]

### ProgramSelection
- **Type**: typing.Optional[int]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RemixSettingsExtraOutputTypeDef]

### SelectorType
- **Type**: typing.Optional[typing.Literal['HLS_RENDITION_GROUP', 'LANGUAGE_CODE', 'PID', 'TRACK']]

### Tracks
- **Type**: typing.Optional[typing.List[int]]


# AudioSelectorGroupExtraOutputTypeDef

### AudioSelectorNames
- **Type**: typing.Optional[typing.List[str]]


# AudioSelectorGroupOutputTypeDef

### AudioSelectorNames
- **Type**: typing.Optional[typing.List[str]]


# AudioSelectorGroupTypeDef

### AudioSelectorNames
- **Type**: typing.Optional[typing.Sequence[str]]


# AudioSelectorOutputTypeDef

### AudioDurationCorrection
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'FRAME', 'TRACK']]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DefaultSelection
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NOT_DEFAULT']]

### ExternalAudioFileInput
- **Type**: typing.Optional[str]

### HlsRenditionGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsRenditionGroupSettingsTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### Offset
- **Type**: typing.Optional[int]

### Pids
- **Type**: typing.Optional[typing.List[int]]

### ProgramSelection
- **Type**: typing.Optional[int]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RemixSettingsOutputTypeDef]

### SelectorType
- **Type**: typing.Optional[typing.Literal['HLS_RENDITION_GROUP', 'LANGUAGE_CODE', 'PID', 'TRACK']]

### Tracks
- **Type**: typing.Optional[typing.List[int]]


# AudioSelectorTypeDef

### AudioDurationCorrection
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'FRAME', 'TRACK']]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DefaultSelection
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NOT_DEFAULT']]

### ExternalAudioFileInput
- **Type**: typing.Optional[str]

### HlsRenditionGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsRenditionGroupSettingsTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### Offset
- **Type**: typing.Optional[int]

### Pids
- **Type**: typing.Optional[typing.Sequence[int]]

### ProgramSelection
- **Type**: typing.Optional[int]

### RemixSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RemixSettingsTypeDef]

### SelectorType
- **Type**: typing.Optional[typing.Literal['HLS_RENDITION_GROUP', 'LANGUAGE_CODE', 'PID', 'TRACK']]

### Tracks
- **Type**: typing.Optional[typing.Sequence[int]]


# AutomatedAbrRuleExtraOutputTypeDef

### AllowedRenditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.AllowedRenditionSizeTypeDef]]

### ForceIncludeRenditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.ForceIncludeRenditionSizeTypeDef]]

### MinBottomRenditionSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MinBottomRenditionSizeTypeDef]

### MinTopRenditionSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MinTopRenditionSizeTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['ALLOWED_RENDITIONS', 'FORCE_INCLUDE_RENDITIONS', 'MIN_BOTTOM_RENDITION_SIZE', 'MIN_TOP_RENDITION_SIZE']]


# AutomatedAbrRuleOutputTypeDef

### AllowedRenditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.AllowedRenditionSizeTypeDef]]

### ForceIncludeRenditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.ForceIncludeRenditionSizeTypeDef]]

### MinBottomRenditionSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MinBottomRenditionSizeTypeDef]

### MinTopRenditionSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MinTopRenditionSizeTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['ALLOWED_RENDITIONS', 'FORCE_INCLUDE_RENDITIONS', 'MIN_BOTTOM_RENDITION_SIZE', 'MIN_TOP_RENDITION_SIZE']]


# AutomatedAbrRuleTypeDef

### AllowedRenditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.AllowedRenditionSizeTypeDef]]

### ForceIncludeRenditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.ForceIncludeRenditionSizeTypeDef]]

### MinBottomRenditionSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MinBottomRenditionSizeTypeDef]

### MinTopRenditionSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MinTopRenditionSizeTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['ALLOWED_RENDITIONS', 'FORCE_INCLUDE_RENDITIONS', 'MIN_BOTTOM_RENDITION_SIZE', 'MIN_TOP_RENDITION_SIZE']]


# AutomatedAbrSettingsExtraOutputTypeDef

### MaxAbrBitrate
- **Type**: typing.Optional[int]

### MaxRenditions
- **Type**: typing.Optional[int]

### MinAbrBitrate
- **Type**: typing.Optional[int]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedAbrRuleExtraOutputTypeDef]]


# AutomatedAbrSettingsOutputTypeDef

### MaxAbrBitrate
- **Type**: typing.Optional[int]

### MaxRenditions
- **Type**: typing.Optional[int]

### MinAbrBitrate
- **Type**: typing.Optional[int]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedAbrRuleOutputTypeDef]]


# AutomatedAbrSettingsTypeDef

### MaxAbrBitrate
- **Type**: typing.Optional[int]

### MaxRenditions
- **Type**: typing.Optional[int]

### MinAbrBitrate
- **Type**: typing.Optional[int]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedAbrRuleTypeDef]]


# AutomatedEncodingSettingsExtraOutputTypeDef

### AbrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedAbrSettingsExtraOutputTypeDef]


# AutomatedEncodingSettingsOutputTypeDef

### AbrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedAbrSettingsOutputTypeDef]


# AutomatedEncodingSettingsTypeDef

### AbrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedAbrSettingsTypeDef]


# Av1QvbrSettingsTypeDef

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### QvbrQualityLevelFineTune
- **Type**: typing.Optional[float]


# Av1SettingsTypeDef

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### BitDepth
- **Type**: typing.Optional[typing.Literal['BIT_10', 'BIT_8']]

### FilmGrainSynthesis
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Av1QvbrSettingsTypeDef]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['QVBR']]

### Slices
- **Type**: typing.Optional[int]

### SpatialAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AvailBlankingTypeDef

### AvailBlankingImage
- **Type**: typing.Optional[str]


# AvcIntraSettingsTypeDef

### AvcIntraClass
- **Type**: typing.Optional[typing.Literal['CLASS_100', 'CLASS_200', 'CLASS_4K_2K', 'CLASS_50']]

### AvcIntraUhdSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AvcIntraUhdSettingsTypeDef]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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


# AvcIntraUhdSettingsTypeDef

### QualityTuningLevel
- **Type**: typing.Optional[typing.Literal['MULTI_PASS', 'SINGLE_PASS']]


# BandwidthReductionFilterTypeDef

### Sharpening
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'OFF']]

### Strength
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'OFF']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BurninDestinationSettingsTypeDef

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


# CancelJobRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# CaptionDescriptionPresetExtraOutputTypeDef

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDestinationSettingsExtraOutputTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageDescription
- **Type**: typing.Optional[str]


# CaptionDescriptionPresetOutputTypeDef

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDestinationSettingsOutputTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageDescription
- **Type**: typing.Optional[str]


# CaptionDescriptionPresetTypeDef

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDestinationSettingsTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageDescription
- **Type**: typing.Optional[str]


# CaptionDescriptionTypeDef

### CaptionSelectorName
- **Type**: typing.Optional[str]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDestinationSettingsTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageDescription
- **Type**: typing.Optional[str]


# CaptionDestinationSettingsExtraOutputTypeDef

### BurninDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.BurninDestinationSettingsTypeDef]

### DestinationType
- **Type**: typing.Optional[typing.Literal['BURN_IN', 'DVB_SUB', 'EMBEDDED', 'EMBEDDED_PLUS_SCTE20', 'IMSC', 'SCC', 'SCTE20_PLUS_EMBEDDED', 'SMI', 'SRT', 'TELETEXT', 'TTML', 'WEBVTT']]

### DvbSubDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbSubDestinationSettingsTypeDef]

### EmbeddedDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EmbeddedDestinationSettingsTypeDef]

### ImscDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImscDestinationSettingsTypeDef]

### SccDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SccDestinationSettingsTypeDef]

### SrtDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SrtDestinationSettingsTypeDef]

### TeletextDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TeletextDestinationSettingsExtraOutputTypeDef]

### TtmlDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TtmlDestinationSettingsTypeDef]

### WebvttDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.WebvttDestinationSettingsTypeDef]


# CaptionDestinationSettingsOutputTypeDef

### BurninDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.BurninDestinationSettingsTypeDef]

### DestinationType
- **Type**: typing.Optional[typing.Literal['BURN_IN', 'DVB_SUB', 'EMBEDDED', 'EMBEDDED_PLUS_SCTE20', 'IMSC', 'SCC', 'SCTE20_PLUS_EMBEDDED', 'SMI', 'SRT', 'TELETEXT', 'TTML', 'WEBVTT']]

### DvbSubDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbSubDestinationSettingsTypeDef]

### EmbeddedDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EmbeddedDestinationSettingsTypeDef]

### ImscDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImscDestinationSettingsTypeDef]

### SccDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SccDestinationSettingsTypeDef]

### SrtDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SrtDestinationSettingsTypeDef]

### TeletextDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TeletextDestinationSettingsOutputTypeDef]

### TtmlDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TtmlDestinationSettingsTypeDef]

### WebvttDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.WebvttDestinationSettingsTypeDef]


# CaptionDestinationSettingsTypeDef

### BurninDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.BurninDestinationSettingsTypeDef]

### DestinationType
- **Type**: typing.Optional[typing.Literal['BURN_IN', 'DVB_SUB', 'EMBEDDED', 'EMBEDDED_PLUS_SCTE20', 'IMSC', 'SCC', 'SCTE20_PLUS_EMBEDDED', 'SMI', 'SRT', 'TELETEXT', 'TTML', 'WEBVTT']]

### DvbSubDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbSubDestinationSettingsTypeDef]

### EmbeddedDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EmbeddedDestinationSettingsTypeDef]

### ImscDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImscDestinationSettingsTypeDef]

### SccDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SccDestinationSettingsTypeDef]

### SrtDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SrtDestinationSettingsTypeDef]

### TeletextDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TeletextDestinationSettingsTypeDef]

### TtmlDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TtmlDestinationSettingsTypeDef]

### WebvttDestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.WebvttDestinationSettingsTypeDef]


# CaptionSelectorTypeDef

### CustomLanguageCode
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### SourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSourceSettingsTypeDef]


# CaptionSourceFramerateTypeDef

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]


# CaptionSourceSettingsTypeDef

### AncillarySourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AncillarySourceSettingsTypeDef]

### DvbSubSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbSubSourceSettingsTypeDef]

### EmbeddedSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EmbeddedSourceSettingsTypeDef]

### FileSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.FileSourceSettingsTypeDef]

### SourceType
- **Type**: typing.Optional[typing.Literal['ANCILLARY', 'DVB_SUB', 'EMBEDDED', 'IMSC', 'NULL_SOURCE', 'SCC', 'SCTE20', 'SMI', 'SMPTE_TT', 'SRT', 'STL', 'TELETEXT', 'TTML', 'WEBVTT']]

### TeletextSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TeletextSourceSettingsTypeDef]

### TrackSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TrackSourceSettingsTypeDef]

### WebvttHlsSourceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.WebvttHlsSourceSettingsTypeDef]


# ChannelMappingExtraOutputTypeDef

### OutputChannels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputChannelMappingExtraOutputTypeDef]]


# ChannelMappingOutputTypeDef

### OutputChannels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputChannelMappingOutputTypeDef]]


# ChannelMappingTypeDef

### OutputChannels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputChannelMappingTypeDef]]


# ClipLimitsTypeDef

### MaximumRGBTolerance
- **Type**: typing.Optional[int]

### MaximumYUV
- **Type**: typing.Optional[int]

### MinimumRGBTolerance
- **Type**: typing.Optional[int]

### MinimumYUV
- **Type**: typing.Optional[int]


# CmafAdditionalManifestExtraOutputTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# CmafAdditionalManifestOutputTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# CmafAdditionalManifestTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.Sequence[str]]


# CmafEncryptionSettingsExtraOutputTypeDef

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_CTR', 'SAMPLE_AES']]

### InitializationVectorInManifest
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderCmafExtraOutputTypeDef]

### StaticKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.StaticKeyProviderTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['SPEKE', 'STATIC_KEY']]


# CmafEncryptionSettingsOutputTypeDef

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_CTR', 'SAMPLE_AES']]

### InitializationVectorInManifest
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderCmafOutputTypeDef]

### StaticKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.StaticKeyProviderTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['SPEKE', 'STATIC_KEY']]


# CmafEncryptionSettingsTypeDef

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_CTR', 'SAMPLE_AES']]

### InitializationVectorInManifest
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderCmafTypeDef]

### StaticKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.StaticKeyProviderTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['SPEKE', 'STATIC_KEY']]


# CmafGroupSettingsExtraOutputTypeDef

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafAdditionalManifestExtraOutputTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafEncryptionSettingsExtraOutputTypeDef]

### FragmentLength
- **Type**: typing.Optional[int]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafImageBasedTrickPlaySettingsTypeDef]

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


# CmafGroupSettingsOutputTypeDef

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafAdditionalManifestOutputTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafEncryptionSettingsOutputTypeDef]

### FragmentLength
- **Type**: typing.Optional[int]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafImageBasedTrickPlaySettingsTypeDef]

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


# CmafGroupSettingsTypeDef

### AdditionalManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafAdditionalManifestTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafEncryptionSettingsTypeDef]

### FragmentLength
- **Type**: typing.Optional[int]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafImageBasedTrickPlaySettingsTypeDef]

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


# CmafImageBasedTrickPlaySettingsTypeDef

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


# CmfcSettingsTypeDef

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


# ColorConversion3DLUTSettingTypeDef

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


# ColorCorrectorTypeDef

### Brightness
- **Type**: typing.Optional[int]

### ClipLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ClipLimitsTypeDef]

### ColorSpaceConversion
- **Type**: typing.Optional[typing.Literal['FORCE_601', 'FORCE_709', 'FORCE_HDR10', 'FORCE_HLG_2020', 'FORCE_P3D65_HDR', 'FORCE_P3D65_SDR', 'FORCE_P3DCI', 'NONE']]

### Contrast
- **Type**: typing.Optional[int]

### Hdr10Metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Hdr10MetadataTypeDef]

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


# ContainerSettingsExtraOutputTypeDef

### CmfcSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmfcSettingsTypeDef]

### Container
- **Type**: typing.Optional[typing.Literal['CMFC', 'F4V', 'ISMV', 'M2TS', 'M3U8', 'MOV', 'MP4', 'MPD', 'MXF', 'RAW', 'WEBM', 'Y4M']]

### F4vSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.F4vSettingsTypeDef]

### M2tsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M2tsSettingsExtraOutputTypeDef]

### M3u8Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M3u8SettingsExtraOutputTypeDef]

### MovSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MovSettingsTypeDef]

### Mp4Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Mp4SettingsTypeDef]

### MpdSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MpdSettingsTypeDef]

### MxfSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MxfSettingsTypeDef]


# ContainerSettingsOutputTypeDef

### CmfcSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmfcSettingsTypeDef]

### Container
- **Type**: typing.Optional[typing.Literal['CMFC', 'F4V', 'ISMV', 'M2TS', 'M3U8', 'MOV', 'MP4', 'MPD', 'MXF', 'RAW', 'WEBM', 'Y4M']]

### F4vSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.F4vSettingsTypeDef]

### M2tsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M2tsSettingsOutputTypeDef]

### M3u8Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M3u8SettingsOutputTypeDef]

### MovSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MovSettingsTypeDef]

### Mp4Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Mp4SettingsTypeDef]

### MpdSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MpdSettingsTypeDef]

### MxfSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MxfSettingsTypeDef]


# ContainerSettingsTypeDef

### CmfcSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmfcSettingsTypeDef]

### Container
- **Type**: typing.Optional[typing.Literal['CMFC', 'F4V', 'ISMV', 'M2TS', 'M3U8', 'MOV', 'MP4', 'MPD', 'MXF', 'RAW', 'WEBM', 'Y4M']]

### F4vSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.F4vSettingsTypeDef]

### M2tsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M2tsSettingsTypeDef]

### M3u8Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M3u8SettingsTypeDef]

### MovSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MovSettingsTypeDef]

### Mp4Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Mp4SettingsTypeDef]

### MpdSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MpdSettingsTypeDef]

### MxfSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MxfSettingsTypeDef]


# CreateJobRequestRequestTypeDef

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobSettingsTypeDef'>
- **Required**: Yes

### AccelerationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AccelerationSettingsTypeDef]

### BillingTagsSource
- **Type**: typing.Optional[typing.Literal['JOB', 'JOB_TEMPLATE', 'PRESET', 'QUEUE']]

### ClientRequestToken
- **Type**: typing.Optional[str]

### HopDestinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.HopDestinationTypeDef]]

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


# CreateJobResponseTypeDef

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJobTemplateRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplateSettingsTypeDef'>
- **Required**: Yes

### AccelerationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AccelerationSettingsTypeDef]

### Category
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### HopDestinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.HopDestinationTypeDef]]

### Priority
- **Type**: typing.Optional[int]

### Queue
- **Type**: typing.Optional[str]

### StatusUpdateInterval
- **Type**: typing.Optional[typing.Literal['SECONDS_10', 'SECONDS_12', 'SECONDS_120', 'SECONDS_15', 'SECONDS_180', 'SECONDS_20', 'SECONDS_240', 'SECONDS_30', 'SECONDS_300', 'SECONDS_360', 'SECONDS_420', 'SECONDS_480', 'SECONDS_540', 'SECONDS_60', 'SECONDS_600']]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateJobTemplateResponseTypeDef

### JobTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePresetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.PresetSettingsTypeDef'>
- **Required**: Yes

### Category
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePresetResponseTypeDef

### Preset
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.PresetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQueueRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### PricingPlan
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'RESERVED']]

### ReservationPlanSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ReservationPlanSettingsTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PAUSED']]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQueueResponseTypeDef

### Queue
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.QueueTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DashAdditionalManifestExtraOutputTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# DashAdditionalManifestOutputTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# DashAdditionalManifestTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.Sequence[str]]


# DashIsoEncryptionSettingsExtraOutputTypeDef

### PlaybackDeviceCompatibility
- **Type**: typing.Optional[typing.Literal['CENC_V1', 'UNENCRYPTED_SEI']]

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderExtraOutputTypeDef]


# DashIsoEncryptionSettingsOutputTypeDef

### PlaybackDeviceCompatibility
- **Type**: typing.Optional[typing.Literal['CENC_V1', 'UNENCRYPTED_SEI']]

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderOutputTypeDef]


# DashIsoEncryptionSettingsTypeDef

### PlaybackDeviceCompatibility
- **Type**: typing.Optional[typing.Literal['CENC_V1', 'UNENCRYPTED_SEI']]

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderTypeDef]


# DashIsoGroupSettingsExtraOutputTypeDef

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.DashAdditionalManifestExtraOutputTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoEncryptionSettingsExtraOutputTypeDef]

### FragmentLength
- **Type**: typing.Optional[int]

### HbbtvCompliance
- **Type**: typing.Optional[typing.Literal['HBBTV_1_5', 'NONE']]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoImageBasedTrickPlaySettingsTypeDef]

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


# DashIsoGroupSettingsOutputTypeDef

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.DashAdditionalManifestOutputTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoEncryptionSettingsOutputTypeDef]

### FragmentLength
- **Type**: typing.Optional[int]

### HbbtvCompliance
- **Type**: typing.Optional[typing.Literal['HBBTV_1_5', 'NONE']]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoImageBasedTrickPlaySettingsTypeDef]

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


# DashIsoGroupSettingsTypeDef

### AdditionalManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.DashAdditionalManifestTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoEncryptionSettingsTypeDef]

### FragmentLength
- **Type**: typing.Optional[int]

### HbbtvCompliance
- **Type**: typing.Optional[typing.Literal['HBBTV_1_5', 'NONE']]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoImageBasedTrickPlaySettingsTypeDef]

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


# DashIsoImageBasedTrickPlaySettingsTypeDef

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


# DeinterlacerTypeDef

### Algorithm
- **Type**: typing.Optional[typing.Literal['BLEND', 'BLEND_TICKER', 'INTERPOLATE', 'INTERPOLATE_TICKER', 'LINEAR_INTERPOLATION']]

### Control
- **Type**: typing.Optional[typing.Literal['FORCE_ALL_FRAMES', 'NORMAL']]

### Mode
- **Type**: typing.Optional[typing.Literal['ADAPTIVE', 'DEINTERLACE', 'INVERSE_TELECINE']]


# DeleteJobTemplateRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePresetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEndpointsRequestDescribeEndpointsPaginateTypeDef

### Mode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'GET_ONLY']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfigTypeDef]


# DescribeEndpointsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### Mode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'GET_ONLY']]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEndpointsResponseTypeDef

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.EndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DestinationSettingsTypeDef

### S3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.S3DestinationSettingsTypeDef]


# DisassociateCertificateRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DolbyVisionLevel6MetadataTypeDef

### MaxCll
- **Type**: typing.Optional[int]

### MaxFall
- **Type**: typing.Optional[int]


# DolbyVisionTypeDef

### L6Metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DolbyVisionLevel6MetadataTypeDef]

### L6Mode
- **Type**: typing.Optional[typing.Literal['PASSTHROUGH', 'RECALCULATE', 'SPECIFY']]

### Mapping
- **Type**: typing.Optional[typing.Literal['HDR10_1000', 'HDR10_NOMAP']]

### Profile
- **Type**: typing.Optional[typing.Literal['PROFILE_5', 'PROFILE_8_1']]


# DvbNitSettingsTypeDef

### NetworkId
- **Type**: typing.Optional[int]

### NetworkName
- **Type**: typing.Optional[str]

### NitInterval
- **Type**: typing.Optional[int]


# DvbSdtSettingsTypeDef

### OutputSdt
- **Type**: typing.Optional[typing.Literal['SDT_FOLLOW', 'SDT_FOLLOW_IF_PRESENT', 'SDT_MANUAL', 'SDT_NONE']]

### SdtInterval
- **Type**: typing.Optional[int]

### ServiceName
- **Type**: typing.Optional[str]

### ServiceProviderName
- **Type**: typing.Optional[str]


# DvbSubDestinationSettingsTypeDef

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


# DvbSubSourceSettingsTypeDef

### Pid
- **Type**: typing.Optional[int]


# DvbTdtSettingsTypeDef

### TdtInterval
- **Type**: typing.Optional[int]


# Eac3AtmosSettingsTypeDef

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


# Eac3SettingsTypeDef

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


# EmbeddedDestinationSettingsTypeDef

### Destination608ChannelNumber
- **Type**: typing.Optional[int]

### Destination708ServiceNumber
- **Type**: typing.Optional[int]


# EmbeddedSourceSettingsTypeDef

### Convert608To708
- **Type**: typing.Optional[typing.Literal['DISABLED', 'UPCONVERT']]

### Source608ChannelNumber
- **Type**: typing.Optional[int]

### Source608TrackNumber
- **Type**: typing.Optional[int]

### TerminateCaptions
- **Type**: typing.Optional[typing.Literal['DISABLED', 'END_OF_INPUT']]


# EndpointTypeDef

### Url
- **Type**: typing.Optional[str]


# EsamManifestConfirmConditionNotificationTypeDef

### MccXml
- **Type**: typing.Optional[str]


# EsamSettingsTypeDef

### ManifestConfirmConditionNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamManifestConfirmConditionNotificationTypeDef]

### ResponseSignalPreroll
- **Type**: typing.Optional[int]

### SignalProcessingNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSignalProcessingNotificationTypeDef]


# EsamSignalProcessingNotificationTypeDef

### SccXml
- **Type**: typing.Optional[str]


# ExtendedDataServicesTypeDef

### CopyProtectionAction
- **Type**: typing.Optional[typing.Literal['PASSTHROUGH', 'STRIP']]

### VchipAction
- **Type**: typing.Optional[typing.Literal['PASSTHROUGH', 'STRIP']]


# F4vSettingsTypeDef

### MoovPlacement
- **Type**: typing.Optional[typing.Literal['NORMAL', 'PROGRESSIVE_DOWNLOAD']]


# FileGroupSettingsTypeDef

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]


# FileSourceSettingsTypeDef

### Convert608To708
- **Type**: typing.Optional[typing.Literal['DISABLED', 'UPCONVERT']]

### ConvertPaintToPop
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Framerate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSourceFramerateTypeDef]

### SourceFile
- **Type**: typing.Optional[str]

### TimeDelta
- **Type**: typing.Optional[int]

### TimeDeltaUnits
- **Type**: typing.Optional[typing.Literal['MILLISECONDS', 'SECONDS']]


# FlacSettingsTypeDef

### BitDepth
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]


# ForceIncludeRenditionSizeTypeDef

### Height
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# FrameCaptureSettingsTypeDef

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]

### MaxCaptures
- **Type**: typing.Optional[int]

### Quality
- **Type**: typing.Optional[int]


# GetJobRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResponseTypeDef

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobTemplateRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobTemplateResponseTypeDef

### JobTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPresetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetPresetResponseTypeDef

### Preset
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.PresetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueueRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueResponseTypeDef

### Queue
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.QueueTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# H264QvbrSettingsTypeDef

### MaxAverageBitrate
- **Type**: typing.Optional[int]

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### QvbrQualityLevelFineTune
- **Type**: typing.Optional[float]


# H264SettingsTypeDef

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### BandwidthReductionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.BandwidthReductionFilterTypeDef]

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
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.H264QvbrSettingsTypeDef]

### RateControlMode
- **Type**: typing.Optional[typing.Literal['CBR', 'QVBR', 'VBR']]

### RepeatPps
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

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


# H265QvbrSettingsTypeDef

### MaxAverageBitrate
- **Type**: typing.Optional[int]

### QvbrQualityLevel
- **Type**: typing.Optional[int]

### QvbrQualityLevelFineTune
- **Type**: typing.Optional[float]


# H265SettingsTypeDef

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### AlternateTransferFunctionSei
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### BandwidthReductionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.BandwidthReductionFilterTypeDef]

### Bitrate
- **Type**: typing.Optional[int]

### CodecLevel
- **Type**: typing.Optional[typing.Literal['AUTO', 'LEVEL_1', 'LEVEL_2', 'LEVEL_2_1', 'LEVEL_3', 'LEVEL_3_1', 'LEVEL_4', 'LEVEL_4_1', 'LEVEL_5', 'LEVEL_5_1', 'LEVEL_5_2', 'LEVEL_6', 'LEVEL_6_1', 'LEVEL_6_2']]

### CodecProfile
- **Type**: typing.Optional[typing.Literal['MAIN10_HIGH', 'MAIN10_MAIN', 'MAIN_422_10BIT_HIGH', 'MAIN_422_10BIT_MAIN', 'MAIN_422_8BIT_HIGH', 'MAIN_422_8BIT_MAIN', 'MAIN_HIGH', 'MAIN_MAIN']]

### DynamicSubGop
- **Type**: typing.Optional[typing.Literal['ADAPTIVE', 'STATIC']]

### EndOfStreamMarkers
- **Type**: typing.Optional[typing.Literal['INCLUDE', 'SUPPRESS']]

### FlickerAdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.H265QvbrSettingsTypeDef]

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


# Hdr10MetadataTypeDef

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


# Hdr10PlusTypeDef

### MasteringMonitorNits
- **Type**: typing.Optional[int]

### TargetMonitorNits
- **Type**: typing.Optional[int]


# HlsAdditionalManifestExtraOutputTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# HlsAdditionalManifestOutputTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# HlsAdditionalManifestTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.Sequence[str]]


# HlsCaptionLanguageMappingTypeDef

### CaptionChannel
- **Type**: typing.Optional[int]

### CustomLanguageCode
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### LanguageDescription
- **Type**: typing.Optional[str]


# HlsEncryptionSettingsExtraOutputTypeDef

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES128', 'SAMPLE_AES']]

### InitializationVectorInManifest
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### OfflineEncrypted
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderExtraOutputTypeDef]

### StaticKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.StaticKeyProviderTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['SPEKE', 'STATIC_KEY']]


# HlsEncryptionSettingsOutputTypeDef

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES128', 'SAMPLE_AES']]

### InitializationVectorInManifest
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### OfflineEncrypted
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderOutputTypeDef]

### StaticKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.StaticKeyProviderTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['SPEKE', 'STATIC_KEY']]


# HlsEncryptionSettingsTypeDef

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES128', 'SAMPLE_AES']]

### InitializationVectorInManifest
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### OfflineEncrypted
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderTypeDef]

### StaticKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.StaticKeyProviderTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['SPEKE', 'STATIC_KEY']]


# HlsGroupSettingsExtraOutputTypeDef

### AdMarkers
- **Type**: typing.Optional[typing.List[typing.Literal['ELEMENTAL', 'ELEMENTAL_SCTE35']]]

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsAdditionalManifestExtraOutputTypeDef]]

### AudioOnlyHeader
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### BaseUrl
- **Type**: typing.Optional[str]

### CaptionLanguageMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsCaptionLanguageMappingTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### DirectoryStructure
- **Type**: typing.Optional[typing.Literal['SINGLE_DIRECTORY', 'SUBDIRECTORY_PER_STREAM']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsEncryptionSettingsExtraOutputTypeDef]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsImageBasedTrickPlaySettingsTypeDef]

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


# HlsGroupSettingsOutputTypeDef

### AdMarkers
- **Type**: typing.Optional[typing.List[typing.Literal['ELEMENTAL', 'ELEMENTAL_SCTE35']]]

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsAdditionalManifestOutputTypeDef]]

### AudioOnlyHeader
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### BaseUrl
- **Type**: typing.Optional[str]

### CaptionLanguageMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsCaptionLanguageMappingTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### DirectoryStructure
- **Type**: typing.Optional[typing.Literal['SINGLE_DIRECTORY', 'SUBDIRECTORY_PER_STREAM']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsEncryptionSettingsOutputTypeDef]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsImageBasedTrickPlaySettingsTypeDef]

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


# HlsGroupSettingsTypeDef

### AdMarkers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ELEMENTAL', 'ELEMENTAL_SCTE35']]]

### AdditionalManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsAdditionalManifestTypeDef]]

### AudioOnlyHeader
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### BaseUrl
- **Type**: typing.Optional[str]

### CaptionLanguageMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsCaptionLanguageMappingTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### DirectoryStructure
- **Type**: typing.Optional[typing.Literal['SINGLE_DIRECTORY', 'SUBDIRECTORY_PER_STREAM']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsEncryptionSettingsTypeDef]

### ImageBasedTrickPlay
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'NONE', 'THUMBNAIL', 'THUMBNAIL_AND_FULLFRAME']]

### ImageBasedTrickPlaySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsImageBasedTrickPlaySettingsTypeDef]

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


# HlsImageBasedTrickPlaySettingsTypeDef

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


# HlsRenditionGroupSettingsTypeDef

### RenditionGroupId
- **Type**: typing.Optional[str]

### RenditionLanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### RenditionName
- **Type**: typing.Optional[str]


# HlsSettingsTypeDef

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


# HopDestinationTypeDef

### Priority
- **Type**: typing.Optional[int]

### Queue
- **Type**: typing.Optional[str]

### WaitMinutes
- **Type**: typing.Optional[int]


# Id3InsertionTypeDef

### Id3
- **Type**: typing.Optional[str]

### Timecode
- **Type**: typing.Optional[str]


# ImageInserterExtraOutputTypeDef

### InsertableImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InsertableImageTypeDef]]

### SdrReferenceWhiteLevel
- **Type**: typing.Optional[int]


# ImageInserterOutputTypeDef

### InsertableImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InsertableImageTypeDef]]

### SdrReferenceWhiteLevel
- **Type**: typing.Optional[int]


# ImageInserterTypeDef

### InsertableImages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.InsertableImageTypeDef]]

### SdrReferenceWhiteLevel
- **Type**: typing.Optional[int]


# ImscDestinationSettingsTypeDef

### Accessibility
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### StylePassthrough
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# InputClippingTypeDef

### EndTimecode
- **Type**: typing.Optional[str]

### StartTimecode
- **Type**: typing.Optional[str]


# InputDecryptionSettingsTypeDef

### DecryptionMode
- **Type**: typing.Optional[typing.Literal['AES_CBC', 'AES_CTR', 'AES_GCM']]

### EncryptedDecryptionKey
- **Type**: typing.Optional[str]

### InitializationVector
- **Type**: typing.Optional[str]

### KmsKeyRegion
- **Type**: typing.Optional[str]


# InputExtraOutputTypeDef

### AdvancedInputFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdvancedInputFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AdvancedInputFilterSettingsTypeDef]

### AudioSelectorGroups
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorGroupExtraOutputTypeDef]]

### AudioSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorExtraOutputTypeDef]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSelectorTypeDef]]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DecryptionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.InputDecryptionSettingsTypeDef]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DolbyVisionMetadataXml
- **Type**: typing.Optional[str]

### FileInput
- **Type**: typing.Optional[str]

### FilterEnable
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLE', 'FORCE']]

### FilterStrength
- **Type**: typing.Optional[int]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterExtraOutputTypeDef]

### InputClippings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputClippingTypeDef]]

### InputScanType
- **Type**: typing.Optional[typing.Literal['AUTO', 'PSF']]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.InputVideoGeneratorTypeDef]

### VideoOverlays
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayExtraOutputTypeDef]]

### VideoSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoSelectorTypeDef]


# InputOutputTypeDef

### AdvancedInputFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdvancedInputFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AdvancedInputFilterSettingsTypeDef]

### AudioSelectorGroups
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorGroupOutputTypeDef]]

### AudioSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorOutputTypeDef]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSelectorTypeDef]]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DecryptionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.InputDecryptionSettingsTypeDef]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DolbyVisionMetadataXml
- **Type**: typing.Optional[str]

### FileInput
- **Type**: typing.Optional[str]

### FilterEnable
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLE', 'FORCE']]

### FilterStrength
- **Type**: typing.Optional[int]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterOutputTypeDef]

### InputClippings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputClippingTypeDef]]

### InputScanType
- **Type**: typing.Optional[typing.Literal['AUTO', 'PSF']]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.InputVideoGeneratorTypeDef]

### VideoOverlays
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayOutputTypeDef]]

### VideoSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoSelectorTypeDef]


# InputTemplateExtraOutputTypeDef

### AdvancedInputFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdvancedInputFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AdvancedInputFilterSettingsTypeDef]

### AudioSelectorGroups
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorGroupExtraOutputTypeDef]]

### AudioSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorExtraOutputTypeDef]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSelectorTypeDef]]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DolbyVisionMetadataXml
- **Type**: typing.Optional[str]

### FilterEnable
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLE', 'FORCE']]

### FilterStrength
- **Type**: typing.Optional[int]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterExtraOutputTypeDef]

### InputClippings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputClippingTypeDef]]

### InputScanType
- **Type**: typing.Optional[typing.Literal['AUTO', 'PSF']]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### ProgramNumber
- **Type**: typing.Optional[int]

### PsiControl
- **Type**: typing.Optional[typing.Literal['IGNORE_PSI', 'USE_PSI']]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]

### VideoOverlays
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayExtraOutputTypeDef]]

### VideoSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoSelectorTypeDef]


# InputTemplateOutputTypeDef

### AdvancedInputFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdvancedInputFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AdvancedInputFilterSettingsTypeDef]

### AudioSelectorGroups
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorGroupOutputTypeDef]]

### AudioSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorOutputTypeDef]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSelectorTypeDef]]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DolbyVisionMetadataXml
- **Type**: typing.Optional[str]

### FilterEnable
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLE', 'FORCE']]

### FilterStrength
- **Type**: typing.Optional[int]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterOutputTypeDef]

### InputClippings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputClippingTypeDef]]

### InputScanType
- **Type**: typing.Optional[typing.Literal['AUTO', 'PSF']]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### ProgramNumber
- **Type**: typing.Optional[int]

### PsiControl
- **Type**: typing.Optional[typing.Literal['IGNORE_PSI', 'USE_PSI']]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]

### VideoOverlays
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayOutputTypeDef]]

### VideoSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoSelectorTypeDef]


# InputTemplateTypeDef

### AdvancedInputFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdvancedInputFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AdvancedInputFilterSettingsTypeDef]

### AudioSelectorGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorGroupTypeDef]]

### AudioSelectors
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorTypeDef]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSelectorTypeDef]]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DolbyVisionMetadataXml
- **Type**: typing.Optional[str]

### FilterEnable
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLE', 'FORCE']]

### FilterStrength
- **Type**: typing.Optional[int]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterTypeDef]

### InputClippings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.InputClippingTypeDef]]

### InputScanType
- **Type**: typing.Optional[typing.Literal['AUTO', 'PSF']]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### ProgramNumber
- **Type**: typing.Optional[int]

### PsiControl
- **Type**: typing.Optional[typing.Literal['IGNORE_PSI', 'USE_PSI']]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]

### VideoOverlays
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayTypeDef]]

### VideoSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoSelectorTypeDef]


# InputTypeDef

### AdvancedInputFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdvancedInputFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AdvancedInputFilterSettingsTypeDef]

### AudioSelectorGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorGroupTypeDef]]

### AudioSelectors
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.AudioSelectorTypeDef]]

### CaptionSelectors
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionSelectorTypeDef]]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### DeblockFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DecryptionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.InputDecryptionSettingsTypeDef]

### DenoiseFilter
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DolbyVisionMetadataXml
- **Type**: typing.Optional[str]

### FileInput
- **Type**: typing.Optional[str]

### FilterEnable
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLE', 'FORCE']]

### FilterStrength
- **Type**: typing.Optional[int]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterTypeDef]

### InputClippings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.InputClippingTypeDef]]

### InputScanType
- **Type**: typing.Optional[typing.Literal['AUTO', 'PSF']]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.InputVideoGeneratorTypeDef]

### VideoOverlays
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayTypeDef]]

### VideoSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoSelectorTypeDef]


# InputVideoGeneratorTypeDef

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


# InsertableImageTypeDef

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


# JobMessagesTypeDef

### Info
- **Type**: typing.Optional[typing.List[str]]

### Warning
- **Type**: typing.Optional[typing.List[str]]


# JobSettingsExtraOutputTypeDef

### AdAvailOffset
- **Type**: typing.Optional[int]

### AvailBlanking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AvailBlankingTypeDef]

### ColorConversion3DLUTSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorConversion3DLUTSettingTypeDef]]

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSettingsTypeDef]

### ExtendedDataServices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ExtendedDataServicesTypeDef]

### FollowSource
- **Type**: typing.Optional[int]

### Inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputExtraOutputTypeDef]]

### KantarWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.KantarWatermarkSettingsTypeDef]

### MotionImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MotionImageInserterTypeDef]

### NielsenConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenConfigurationTypeDef]

### NielsenNonLinearWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenNonLinearWatermarkSettingsTypeDef]

### OutputGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupExtraOutputTypeDef]]

### TimecodeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimecodeConfigTypeDef]

### TimedMetadataInsertion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimedMetadataInsertionExtraOutputTypeDef]


# JobSettingsOutputTypeDef

### AdAvailOffset
- **Type**: typing.Optional[int]

### AvailBlanking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AvailBlankingTypeDef]

### ColorConversion3DLUTSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorConversion3DLUTSettingTypeDef]]

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSettingsTypeDef]

### ExtendedDataServices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ExtendedDataServicesTypeDef]

### FollowSource
- **Type**: typing.Optional[int]

### Inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputOutputTypeDef]]

### KantarWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.KantarWatermarkSettingsTypeDef]

### MotionImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MotionImageInserterTypeDef]

### NielsenConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenConfigurationTypeDef]

### NielsenNonLinearWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenNonLinearWatermarkSettingsTypeDef]

### OutputGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupOutputTypeDef]]

### TimecodeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimecodeConfigTypeDef]

### TimedMetadataInsertion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimedMetadataInsertionOutputTypeDef]


# JobSettingsTypeDef

### AdAvailOffset
- **Type**: typing.Optional[int]

### AvailBlanking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AvailBlankingTypeDef]

### ColorConversion3DLUTSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorConversion3DLUTSettingTypeDef]]

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSettingsTypeDef]

### ExtendedDataServices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ExtendedDataServicesTypeDef]

### FollowSource
- **Type**: typing.Optional[int]

### Inputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.InputTypeDef]]

### KantarWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.KantarWatermarkSettingsTypeDef]

### MotionImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MotionImageInserterTypeDef]

### NielsenConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenConfigurationTypeDef]

### NielsenNonLinearWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenNonLinearWatermarkSettingsTypeDef]

### OutputGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupTypeDef]]

### TimecodeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimecodeConfigTypeDef]

### TimedMetadataInsertion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimedMetadataInsertionTypeDef]


# JobTemplateSettingsExtraOutputTypeDef

### AdAvailOffset
- **Type**: typing.Optional[int]

### AvailBlanking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AvailBlankingTypeDef]

### ColorConversion3DLUTSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorConversion3DLUTSettingTypeDef]]

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSettingsTypeDef]

### ExtendedDataServices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ExtendedDataServicesTypeDef]

### FollowSource
- **Type**: typing.Optional[int]

### Inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputTemplateExtraOutputTypeDef]]

### KantarWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.KantarWatermarkSettingsTypeDef]

### MotionImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MotionImageInserterTypeDef]

### NielsenConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenConfigurationTypeDef]

### NielsenNonLinearWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenNonLinearWatermarkSettingsTypeDef]

### OutputGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupExtraOutputTypeDef]]

### TimecodeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimecodeConfigTypeDef]

### TimedMetadataInsertion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimedMetadataInsertionExtraOutputTypeDef]


# JobTemplateSettingsOutputTypeDef

### AdAvailOffset
- **Type**: typing.Optional[int]

### AvailBlanking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AvailBlankingTypeDef]

### ColorConversion3DLUTSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorConversion3DLUTSettingTypeDef]]

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSettingsTypeDef]

### ExtendedDataServices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ExtendedDataServicesTypeDef]

### FollowSource
- **Type**: typing.Optional[int]

### Inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.InputTemplateOutputTypeDef]]

### KantarWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.KantarWatermarkSettingsTypeDef]

### MotionImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MotionImageInserterTypeDef]

### NielsenConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenConfigurationTypeDef]

### NielsenNonLinearWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenNonLinearWatermarkSettingsTypeDef]

### OutputGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupOutputTypeDef]]

### TimecodeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimecodeConfigTypeDef]

### TimedMetadataInsertion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimedMetadataInsertionOutputTypeDef]


# JobTemplateSettingsTypeDef

### AdAvailOffset
- **Type**: typing.Optional[int]

### AvailBlanking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AvailBlankingTypeDef]

### ColorConversion3DLUTSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorConversion3DLUTSettingTypeDef]]

### Esam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.EsamSettingsTypeDef]

### ExtendedDataServices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ExtendedDataServicesTypeDef]

### FollowSource
- **Type**: typing.Optional[int]

### Inputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.InputTemplateTypeDef]]

### KantarWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.KantarWatermarkSettingsTypeDef]

### MotionImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MotionImageInserterTypeDef]

### NielsenConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenConfigurationTypeDef]

### NielsenNonLinearWatermark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NielsenNonLinearWatermarkSettingsTypeDef]

### OutputGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupTypeDef]]

### TimecodeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimecodeConfigTypeDef]

### TimedMetadataInsertion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimedMetadataInsertionTypeDef]


# JobTemplateTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplateSettingsOutputTypeDef'>
- **Required**: Yes

### AccelerationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AccelerationSettingsTypeDef]

### Arn
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### HopDestinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.HopDestinationTypeDef]]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### Priority
- **Type**: typing.Optional[int]

### Queue
- **Type**: typing.Optional[str]

### StatusUpdateInterval
- **Type**: typing.Optional[typing.Literal['SECONDS_10', 'SECONDS_12', 'SECONDS_120', 'SECONDS_15', 'SECONDS_180', 'SECONDS_20', 'SECONDS_240', 'SECONDS_30', 'SECONDS_300', 'SECONDS_360', 'SECONDS_420', 'SECONDS_480', 'SECONDS_540', 'SECONDS_60', 'SECONDS_600']]

### Type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'SYSTEM']]


# JobTypeDef

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobSettingsOutputTypeDef'>
- **Required**: Yes

### AccelerationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AccelerationSettingsTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.HopDestinationTypeDef]]

### Id
- **Type**: typing.Optional[str]

### JobPercentComplete
- **Type**: typing.Optional[int]

### JobTemplate
- **Type**: typing.Optional[str]

### Messages
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.JobMessagesTypeDef]

### OutputGroupDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupDetailTypeDef]]

### Priority
- **Type**: typing.Optional[int]

### Queue
- **Type**: typing.Optional[str]

### QueueTransitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.QueueTransitionTypeDef]]

### RetryCount
- **Type**: typing.Optional[int]

### SimulateReservedQueue
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETE', 'ERROR', 'PROGRESSING', 'SUBMITTED']]

### StatusUpdateInterval
- **Type**: typing.Optional[typing.Literal['SECONDS_10', 'SECONDS_12', 'SECONDS_120', 'SECONDS_15', 'SECONDS_180', 'SECONDS_20', 'SECONDS_240', 'SECONDS_30', 'SECONDS_300', 'SECONDS_360', 'SECONDS_420', 'SECONDS_480', 'SECONDS_540', 'SECONDS_60', 'SECONDS_600']]

### Timing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimingTypeDef]

### UserMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### Warnings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.WarningGroupTypeDef]]


# KantarWatermarkSettingsTypeDef

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


# ListJobTemplatesRequestListJobTemplatesPaginateTypeDef

### Category
- **Type**: typing.Optional[str]

### ListBy
- **Type**: typing.Optional[typing.Literal['CREATION_DATE', 'NAME', 'SYSTEM']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfigTypeDef]


# ListJobTemplatesRequestRequestTypeDef

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


# ListJobTemplatesResponseTypeDef

### JobTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequestListJobsPaginateTypeDef

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Queue
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETE', 'ERROR', 'PROGRESSING', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfigTypeDef]


# ListJobsRequestRequestTypeDef

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


# ListJobsResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.JobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPresetsRequestListPresetsPaginateTypeDef

### Category
- **Type**: typing.Optional[str]

### ListBy
- **Type**: typing.Optional[typing.Literal['CREATION_DATE', 'NAME', 'SYSTEM']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfigTypeDef]


# ListPresetsRequestRequestTypeDef

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


# ListPresetsResponseTypeDef

### Presets
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.PresetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueuesRequestListQueuesPaginateTypeDef

### ListBy
- **Type**: typing.Optional[typing.Literal['CREATION_DATE', 'NAME']]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfigTypeDef]


# ListQueuesRequestRequestTypeDef

### ListBy
- **Type**: typing.Optional[typing.Literal['CREATION_DATE', 'NAME']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListQueuesResponseTypeDef

### Queues
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.QueueTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### ResourceTags
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResourceTagsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# M2tsScte35EsamTypeDef

### Scte35EsamPid
- **Type**: typing.Optional[int]


# M2tsSettingsExtraOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbNitSettingsTypeDef]

### DvbSdtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbSdtSettingsTypeDef]

### DvbSubPids
- **Type**: typing.Optional[typing.List[int]]

### DvbTdtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbTdtSettingsTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M2tsScte35EsamTypeDef]

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


# M2tsSettingsOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbNitSettingsTypeDef]

### DvbSdtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbSdtSettingsTypeDef]

### DvbSubPids
- **Type**: typing.Optional[typing.List[int]]

### DvbTdtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbTdtSettingsTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M2tsScte35EsamTypeDef]

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


# M2tsSettingsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbNitSettingsTypeDef]

### DvbSdtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbSdtSettingsTypeDef]

### DvbSubPids
- **Type**: typing.Optional[typing.Sequence[int]]

### DvbTdtSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DvbTdtSettingsTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.M2tsScte35EsamTypeDef]

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


# M3u8SettingsExtraOutputTypeDef

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


# M3u8SettingsOutputTypeDef

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


# M3u8SettingsTypeDef

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


# MinBottomRenditionSizeTypeDef

### Height
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# MinTopRenditionSizeTypeDef

### Height
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# MotionImageInserterTypeDef

### Framerate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MotionImageInsertionFramerateTypeDef]

### Input
- **Type**: typing.Optional[str]

### InsertionMode
- **Type**: typing.Optional[typing.Literal['MOV', 'PNG']]

### Offset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MotionImageInsertionOffsetTypeDef]

### Playback
- **Type**: typing.Optional[typing.Literal['ONCE', 'REPEAT']]

### StartTime
- **Type**: typing.Optional[str]


# MotionImageInsertionFramerateTypeDef

### FramerateDenominator
- **Type**: typing.Optional[int]

### FramerateNumerator
- **Type**: typing.Optional[int]


# MotionImageInsertionOffsetTypeDef

### ImageX
- **Type**: typing.Optional[int]

### ImageY
- **Type**: typing.Optional[int]


# MovSettingsTypeDef

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


# Mp2SettingsTypeDef

### Bitrate
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]


# Mp3SettingsTypeDef

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


# Mp4SettingsTypeDef

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


# MpdSettingsTypeDef

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


# Mpeg2SettingsTypeDef

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
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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


# MsSmoothAdditionalManifestExtraOutputTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# MsSmoothAdditionalManifestOutputTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.List[str]]


# MsSmoothAdditionalManifestTypeDef

### ManifestNameModifier
- **Type**: typing.Optional[str]

### SelectedOutputs
- **Type**: typing.Optional[typing.Sequence[str]]


# MsSmoothEncryptionSettingsExtraOutputTypeDef

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderExtraOutputTypeDef]


# MsSmoothEncryptionSettingsOutputTypeDef

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderOutputTypeDef]


# MsSmoothEncryptionSettingsTypeDef

### SpekeKeyProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.SpekeKeyProviderTypeDef]


# MsSmoothGroupSettingsExtraOutputTypeDef

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothAdditionalManifestExtraOutputTypeDef]]

### AudioDeduplication
- **Type**: typing.Optional[typing.Literal['COMBINE_DUPLICATE_STREAMS', 'NONE']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothEncryptionSettingsExtraOutputTypeDef]

### FragmentLength
- **Type**: typing.Optional[int]

### FragmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### ManifestEncoding
- **Type**: typing.Optional[typing.Literal['UTF16', 'UTF8']]


# MsSmoothGroupSettingsOutputTypeDef

### AdditionalManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothAdditionalManifestOutputTypeDef]]

### AudioDeduplication
- **Type**: typing.Optional[typing.Literal['COMBINE_DUPLICATE_STREAMS', 'NONE']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothEncryptionSettingsOutputTypeDef]

### FragmentLength
- **Type**: typing.Optional[int]

### FragmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### ManifestEncoding
- **Type**: typing.Optional[typing.Literal['UTF16', 'UTF8']]


# MsSmoothGroupSettingsTypeDef

### AdditionalManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothAdditionalManifestTypeDef]]

### AudioDeduplication
- **Type**: typing.Optional[typing.Literal['COMBINE_DUPLICATE_STREAMS', 'NONE']]

### Destination
- **Type**: typing.Optional[str]

### DestinationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DestinationSettingsTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothEncryptionSettingsTypeDef]

### FragmentLength
- **Type**: typing.Optional[int]

### FragmentLengthControl
- **Type**: typing.Optional[typing.Literal['EXACT', 'GOP_MULTIPLE']]

### ManifestEncoding
- **Type**: typing.Optional[typing.Literal['UTF16', 'UTF8']]


# MxfSettingsTypeDef

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['COPY_FROM_VIDEO', 'NO_COPY']]

### Profile
- **Type**: typing.Optional[typing.Literal['D_10', 'OP1A', 'XAVC', 'XDCAM', 'XDCAM_RDD9']]

### XavcProfileSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MxfXavcProfileSettingsTypeDef]


# MxfXavcProfileSettingsTypeDef

### DurationMode
- **Type**: typing.Optional[typing.Literal['ALLOW_ANY_DURATION', 'DROP_FRAMES_FOR_COMPLIANCE']]

### MaxAncDataSize
- **Type**: typing.Optional[int]


# NexGuardFileMarkerSettingsTypeDef

### License
- **Type**: typing.Optional[str]

### Payload
- **Type**: typing.Optional[int]

### Preset
- **Type**: typing.Optional[str]

### Strength
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'LIGHTER', 'LIGHTEST', 'STRONGER', 'STRONGEST']]


# NielsenConfigurationTypeDef

### BreakoutCode
- **Type**: typing.Optional[int]

### DistributorId
- **Type**: typing.Optional[str]


# NielsenNonLinearWatermarkSettingsTypeDef

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


# NoiseReducerFilterSettingsTypeDef

### Strength
- **Type**: typing.Optional[int]


# NoiseReducerSpatialFilterSettingsTypeDef

### PostFilterSharpenStrength
- **Type**: typing.Optional[int]

### Speed
- **Type**: typing.Optional[int]

### Strength
- **Type**: typing.Optional[int]


# NoiseReducerTemporalFilterSettingsTypeDef

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


# NoiseReducerTypeDef

### Filter
- **Type**: typing.Optional[typing.Literal['BILATERAL', 'CONSERVE', 'GAUSSIAN', 'LANCZOS', 'MEAN', 'SHARPEN', 'SPATIAL', 'TEMPORAL']]

### FilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NoiseReducerFilterSettingsTypeDef]

### SpatialFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NoiseReducerSpatialFilterSettingsTypeDef]

### TemporalFilterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NoiseReducerTemporalFilterSettingsTypeDef]


# OpusSettingsTypeDef

### Bitrate
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]


# OutputChannelMappingExtraOutputTypeDef

### InputChannels
- **Type**: typing.Optional[typing.List[int]]

### InputChannelsFineTune
- **Type**: typing.Optional[typing.List[float]]


# OutputChannelMappingOutputTypeDef

### InputChannels
- **Type**: typing.Optional[typing.List[int]]

### InputChannelsFineTune
- **Type**: typing.Optional[typing.List[float]]


# OutputChannelMappingTypeDef

### InputChannels
- **Type**: typing.Optional[typing.Sequence[int]]

### InputChannelsFineTune
- **Type**: typing.Optional[typing.Sequence[float]]


# OutputDetailTypeDef

### DurationInMs
- **Type**: typing.Optional[int]

### VideoDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoDetailTypeDef]


# OutputGroupDetailTypeDef

### OutputDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputDetailTypeDef]]


# OutputGroupExtraOutputTypeDef

### AutomatedEncodingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedEncodingSettingsExtraOutputTypeDef]

### CustomName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### OutputGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupSettingsExtraOutputTypeDef]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputTypeDef]]


# OutputGroupOutputTypeDef

### AutomatedEncodingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedEncodingSettingsOutputTypeDef]

### CustomName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### OutputGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupSettingsOutputTypeDef]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputTypeDef]]


# OutputGroupSettingsExtraOutputTypeDef

### CmafGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafGroupSettingsExtraOutputTypeDef]

### DashIsoGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoGroupSettingsExtraOutputTypeDef]

### FileGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.FileGroupSettingsTypeDef]

### HlsGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsGroupSettingsExtraOutputTypeDef]

### MsSmoothGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothGroupSettingsExtraOutputTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['CMAF_GROUP_SETTINGS', 'DASH_ISO_GROUP_SETTINGS', 'FILE_GROUP_SETTINGS', 'HLS_GROUP_SETTINGS', 'MS_SMOOTH_GROUP_SETTINGS']]


# OutputGroupSettingsOutputTypeDef

### CmafGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafGroupSettingsOutputTypeDef]

### DashIsoGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoGroupSettingsOutputTypeDef]

### FileGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.FileGroupSettingsTypeDef]

### HlsGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsGroupSettingsOutputTypeDef]

### MsSmoothGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothGroupSettingsOutputTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['CMAF_GROUP_SETTINGS', 'DASH_ISO_GROUP_SETTINGS', 'FILE_GROUP_SETTINGS', 'HLS_GROUP_SETTINGS', 'MS_SMOOTH_GROUP_SETTINGS']]


# OutputGroupSettingsTypeDef

### CmafGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.CmafGroupSettingsTypeDef]

### DashIsoGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DashIsoGroupSettingsTypeDef]

### FileGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.FileGroupSettingsTypeDef]

### HlsGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsGroupSettingsTypeDef]

### MsSmoothGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.MsSmoothGroupSettingsTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['CMAF_GROUP_SETTINGS', 'DASH_ISO_GROUP_SETTINGS', 'FILE_GROUP_SETTINGS', 'HLS_GROUP_SETTINGS', 'MS_SMOOTH_GROUP_SETTINGS']]


# OutputGroupTypeDef

### AutomatedEncodingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AutomatedEncodingSettingsTypeDef]

### CustomName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### OutputGroupSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputGroupSettingsTypeDef]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputTypeDef]]


# OutputSettingsTypeDef

### HlsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.HlsSettingsTypeDef]


# OutputTypeDef

### AudioDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioDescriptionTypeDef]]

### CaptionDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDescriptionTypeDef]]

### ContainerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ContainerSettingsTypeDef]

### Extension
- **Type**: typing.Optional[str]

### NameModifier
- **Type**: typing.Optional[str]

### OutputSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.OutputSettingsTypeDef]

### Preset
- **Type**: typing.Optional[str]

### VideoDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoDescriptionTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartnerWatermarkingTypeDef

### NexguardFileMarkerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NexGuardFileMarkerSettingsTypeDef]


# PolicyTypeDef

### HttpInputs
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'DISALLOWED']]

### HttpsInputs
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'DISALLOWED']]

### S3Inputs
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'DISALLOWED']]


# PresetSettingsExtraOutputTypeDef

### AudioDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioDescriptionExtraOutputTypeDef]]

### CaptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDescriptionPresetExtraOutputTypeDef]]

### ContainerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ContainerSettingsExtraOutputTypeDef]

### VideoDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoDescriptionExtraOutputTypeDef]


# PresetSettingsOutputTypeDef

### AudioDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioDescriptionOutputTypeDef]]

### CaptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDescriptionPresetOutputTypeDef]]

### ContainerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ContainerSettingsOutputTypeDef]

### VideoDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoDescriptionOutputTypeDef]


# PresetSettingsTypeDef

### AudioDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.AudioDescriptionTypeDef]]

### CaptionDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.CaptionDescriptionPresetTypeDef]]

### ContainerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ContainerSettingsTypeDef]

### VideoDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoDescriptionTypeDef]


# PresetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.PresetSettingsOutputTypeDef'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'SYSTEM']]


# ProresSettingsTypeDef

### ChromaSampling
- **Type**: typing.Optional[typing.Literal['PRESERVE_444_SAMPLING', 'SUBSAMPLE_TO_422']]

### CodecProfile
- **Type**: typing.Optional[typing.Literal['APPLE_PRORES_422', 'APPLE_PRORES_422_HQ', 'APPLE_PRORES_422_LT', 'APPLE_PRORES_422_PROXY', 'APPLE_PRORES_4444', 'APPLE_PRORES_4444_XQ']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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


# PutPolicyRequestRequestTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.PolicyTypeDef'>
- **Required**: Yes


# PutPolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueueTransitionTypeDef

### DestinationQueue
- **Type**: typing.Optional[str]

### SourceQueue
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# QueueTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### PricingPlan
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'RESERVED']]

### ProgressingJobsCount
- **Type**: typing.Optional[int]

### ReservationPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ReservationPlanTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PAUSED']]

### SubmittedJobsCount
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'SYSTEM']]


# RectangleTypeDef

### Height
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]

### X
- **Type**: typing.Optional[int]

### Y
- **Type**: typing.Optional[int]


# RemixSettingsExtraOutputTypeDef

### AudioDescriptionAudioChannel
- **Type**: typing.Optional[int]

### AudioDescriptionDataChannel
- **Type**: typing.Optional[int]

### ChannelMapping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ChannelMappingExtraOutputTypeDef]

### ChannelsIn
- **Type**: typing.Optional[int]

### ChannelsOut
- **Type**: typing.Optional[int]


# RemixSettingsOutputTypeDef

### AudioDescriptionAudioChannel
- **Type**: typing.Optional[int]

### AudioDescriptionDataChannel
- **Type**: typing.Optional[int]

### ChannelMapping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ChannelMappingOutputTypeDef]

### ChannelsIn
- **Type**: typing.Optional[int]

### ChannelsOut
- **Type**: typing.Optional[int]


# RemixSettingsTypeDef

### AudioDescriptionAudioChannel
- **Type**: typing.Optional[int]

### AudioDescriptionDataChannel
- **Type**: typing.Optional[int]

### ChannelMapping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ChannelMappingTypeDef]

### ChannelsIn
- **Type**: typing.Optional[int]

### ChannelsOut
- **Type**: typing.Optional[int]


# ReservationPlanSettingsTypeDef

### Commitment
- **Type**: typing.Literal['ONE_YEAR']
- **Required**: Yes

### RenewalType
- **Type**: typing.Literal['AUTO_RENEW', 'EXPIRE']
- **Required**: Yes

### ReservedSlots
- **Type**: <class 'int'>
- **Required**: Yes


# ReservationPlanTypeDef

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


# ResourceTagsTypeDef

### Arn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# S3DestinationAccessControlTypeDef

### CannedAcl
- **Type**: typing.Optional[typing.Literal['AUTHENTICATED_READ', 'BUCKET_OWNER_FULL_CONTROL', 'BUCKET_OWNER_READ', 'PUBLIC_READ']]


# S3DestinationSettingsTypeDef

### AccessControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.S3DestinationAccessControlTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.S3EncryptionSettingsTypeDef]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'REDUCED_REDUNDANCY', 'STANDARD', 'STANDARD_IA']]


# S3EncryptionSettingsTypeDef

### EncryptionType
- **Type**: typing.Optional[typing.Literal['SERVER_SIDE_ENCRYPTION_KMS', 'SERVER_SIDE_ENCRYPTION_S3']]

### KmsEncryptionContext
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]


# SccDestinationSettingsTypeDef

### Framerate
- **Type**: typing.Optional[typing.Literal['FRAMERATE_23_97', 'FRAMERATE_24', 'FRAMERATE_25', 'FRAMERATE_29_97_DROPFRAME', 'FRAMERATE_29_97_NON_DROPFRAME']]


# SearchJobsRequestRequestTypeDef

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


# SearchJobsRequestSearchJobsPaginateTypeDef

### InputFile
- **Type**: typing.Optional[str]

### Order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### Queue
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETE', 'ERROR', 'PROGRESSING', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PaginatorConfigTypeDef]


# SearchJobsResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.JobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SpekeKeyProviderCmafExtraOutputTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### DashSignaledSystemIds
- **Type**: typing.Optional[typing.List[str]]

### HlsSignaledSystemIds
- **Type**: typing.Optional[typing.List[str]]

### ResourceId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# SpekeKeyProviderCmafOutputTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### DashSignaledSystemIds
- **Type**: typing.Optional[typing.List[str]]

### HlsSignaledSystemIds
- **Type**: typing.Optional[typing.List[str]]

### ResourceId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# SpekeKeyProviderCmafTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### DashSignaledSystemIds
- **Type**: typing.Optional[typing.Sequence[str]]

### HlsSignaledSystemIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# SpekeKeyProviderExtraOutputTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### SystemIds
- **Type**: typing.Optional[typing.List[str]]

### Url
- **Type**: typing.Optional[str]


# SpekeKeyProviderOutputTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### SystemIds
- **Type**: typing.Optional[typing.List[str]]

### Url
- **Type**: typing.Optional[str]


# SpekeKeyProviderTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### SystemIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Url
- **Type**: typing.Optional[str]


# SrtDestinationSettingsTypeDef

### StylePassthrough
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# StaticKeyProviderTypeDef

### KeyFormat
- **Type**: typing.Optional[str]

### KeyFormatVersions
- **Type**: typing.Optional[str]

### StaticKeyValue
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TeletextDestinationSettingsExtraOutputTypeDef

### PageNumber
- **Type**: typing.Optional[str]

### PageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['PAGE_TYPE_ADDL_INFO', 'PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE', 'PAGE_TYPE_INITIAL', 'PAGE_TYPE_PROGRAM_SCHEDULE', 'PAGE_TYPE_SUBTITLE']]]


# TeletextDestinationSettingsOutputTypeDef

### PageNumber
- **Type**: typing.Optional[str]

### PageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['PAGE_TYPE_ADDL_INFO', 'PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE', 'PAGE_TYPE_INITIAL', 'PAGE_TYPE_PROGRAM_SCHEDULE', 'PAGE_TYPE_SUBTITLE']]]


# TeletextDestinationSettingsTypeDef

### PageNumber
- **Type**: typing.Optional[str]

### PageTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PAGE_TYPE_ADDL_INFO', 'PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE', 'PAGE_TYPE_INITIAL', 'PAGE_TYPE_PROGRAM_SCHEDULE', 'PAGE_TYPE_SUBTITLE']]]


# TeletextSourceSettingsTypeDef

### PageNumber
- **Type**: typing.Optional[str]


# TimecodeBurninTypeDef

### FontSize
- **Type**: typing.Optional[int]

### Position
- **Type**: typing.Optional[typing.Literal['BOTTOM_CENTER', 'BOTTOM_LEFT', 'BOTTOM_RIGHT', 'MIDDLE_CENTER', 'MIDDLE_LEFT', 'MIDDLE_RIGHT', 'TOP_CENTER', 'TOP_LEFT', 'TOP_RIGHT']]

### Prefix
- **Type**: typing.Optional[str]


# TimecodeConfigTypeDef

### Anchor
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### Start
- **Type**: typing.Optional[str]

### TimestampOffset
- **Type**: typing.Optional[str]


# TimedMetadataInsertionExtraOutputTypeDef

### Id3Insertions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.Id3InsertionTypeDef]]


# TimedMetadataInsertionOutputTypeDef

### Id3Insertions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.Id3InsertionTypeDef]]


# TimedMetadataInsertionTypeDef

### Id3Insertions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.Id3InsertionTypeDef]]


# TimingTypeDef

### FinishTime
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]


# TrackSourceSettingsTypeDef

### TrackNumber
- **Type**: typing.Optional[int]


# TtmlDestinationSettingsTypeDef

### StylePassthrough
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UncompressedSettingsTypeDef

### Fourcc
- **Type**: typing.Optional[typing.Literal['I420', 'I422', 'I444']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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


# UntagResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateJobTemplateRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccelerationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AccelerationSettingsTypeDef]

### Category
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### HopDestinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.HopDestinationTypeDef]]

### Priority
- **Type**: typing.Optional[int]

### Queue
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplateSettingsTypeDef]

### StatusUpdateInterval
- **Type**: typing.Optional[typing.Literal['SECONDS_10', 'SECONDS_12', 'SECONDS_120', 'SECONDS_15', 'SECONDS_180', 'SECONDS_20', 'SECONDS_240', 'SECONDS_30', 'SECONDS_300', 'SECONDS_360', 'SECONDS_420', 'SECONDS_480', 'SECONDS_540', 'SECONDS_60', 'SECONDS_600']]


# UpdateJobTemplateResponseTypeDef

### JobTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.JobTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePresetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Category
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PresetSettingsTypeDef]


# UpdatePresetResponseTypeDef

### Preset
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.PresetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateQueueRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ReservationPlanSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ReservationPlanSettingsTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PAUSED']]


# UpdateQueueResponseTypeDef

### Queue
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.QueueTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediaconvert_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# Vc3SettingsTypeDef

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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


# VideoCodecSettingsTypeDef

### Av1Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Av1SettingsTypeDef]

### AvcIntraSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.AvcIntraSettingsTypeDef]

### Codec
- **Type**: typing.Optional[typing.Literal['AV1', 'AVC_INTRA', 'FRAME_CAPTURE', 'H_264', 'H_265', 'MPEG2', 'PASSTHROUGH', 'PRORES', 'UNCOMPRESSED', 'VC3', 'VP8', 'VP9', 'XAVC']]

### FrameCaptureSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.FrameCaptureSettingsTypeDef]

### H264Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.H264SettingsTypeDef]

### H265Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.H265SettingsTypeDef]

### Mpeg2Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Mpeg2SettingsTypeDef]

### ProresSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ProresSettingsTypeDef]

### UncompressedSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.UncompressedSettingsTypeDef]

### Vc3Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Vc3SettingsTypeDef]

### Vp8Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Vp8SettingsTypeDef]

### Vp9Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Vp9SettingsTypeDef]

### XavcSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.XavcSettingsTypeDef]


# VideoDescriptionExtraOutputTypeDef

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### AntiAlias
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoCodecSettingsTypeDef]

### ColorMetadata
- **Type**: typing.Optional[typing.Literal['IGNORE', 'INSERT']]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### DropFrameTimecode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FixedAfd
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### RespondToAfd
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH', 'RESPOND']]

### ScalingBehavior
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'FILL', 'FIT', 'FIT_NO_UPSCALE', 'STRETCH_TO_OUTPUT']]

### Sharpness
- **Type**: typing.Optional[int]

### TimecodeInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PIC_TIMING_SEI']]

### VideoPreprocessors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoPreprocessorExtraOutputTypeDef]

### Width
- **Type**: typing.Optional[int]


# VideoDescriptionOutputTypeDef

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### AntiAlias
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoCodecSettingsTypeDef]

### ColorMetadata
- **Type**: typing.Optional[typing.Literal['IGNORE', 'INSERT']]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### DropFrameTimecode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FixedAfd
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### RespondToAfd
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH', 'RESPOND']]

### ScalingBehavior
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'FILL', 'FIT', 'FIT_NO_UPSCALE', 'STRETCH_TO_OUTPUT']]

### Sharpness
- **Type**: typing.Optional[int]

### TimecodeInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PIC_TIMING_SEI']]

### VideoPreprocessors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoPreprocessorOutputTypeDef]

### Width
- **Type**: typing.Optional[int]


# VideoDescriptionTypeDef

### AfdSignaling
- **Type**: typing.Optional[typing.Literal['AUTO', 'FIXED', 'NONE']]

### AntiAlias
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CodecSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoCodecSettingsTypeDef]

### ColorMetadata
- **Type**: typing.Optional[typing.Literal['IGNORE', 'INSERT']]

### Crop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### DropFrameTimecode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### FixedAfd
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### Position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.RectangleTypeDef]

### RespondToAfd
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH', 'RESPOND']]

### ScalingBehavior
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'FILL', 'FIT', 'FIT_NO_UPSCALE', 'STRETCH_TO_OUTPUT']]

### Sharpness
- **Type**: typing.Optional[int]

### TimecodeInsertion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PIC_TIMING_SEI']]

### VideoPreprocessors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoPreprocessorTypeDef]

### Width
- **Type**: typing.Optional[int]


# VideoDetailTypeDef

### HeightInPx
- **Type**: typing.Optional[int]

### WidthInPx
- **Type**: typing.Optional[int]


# VideoOverlayExtraOutputTypeDef

### EndTimecode
- **Type**: typing.Optional[str]

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayInputExtraOutputTypeDef]

### StartTimecode
- **Type**: typing.Optional[str]


# VideoOverlayInputClippingTypeDef

### EndTimecode
- **Type**: typing.Optional[str]

### StartTimecode
- **Type**: typing.Optional[str]


# VideoOverlayInputExtraOutputTypeDef

### FileInput
- **Type**: typing.Optional[str]

### InputClippings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayInputClippingTypeDef]]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]


# VideoOverlayInputOutputTypeDef

### FileInput
- **Type**: typing.Optional[str]

### InputClippings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayInputClippingTypeDef]]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]


# VideoOverlayInputTypeDef

### FileInput
- **Type**: typing.Optional[str]

### InputClippings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayInputClippingTypeDef]]

### TimecodeSource
- **Type**: typing.Optional[typing.Literal['EMBEDDED', 'SPECIFIEDSTART', 'ZEROBASED']]

### TimecodeStart
- **Type**: typing.Optional[str]


# VideoOverlayOutputTypeDef

### EndTimecode
- **Type**: typing.Optional[str]

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayInputOutputTypeDef]

### StartTimecode
- **Type**: typing.Optional[str]


# VideoOverlayTypeDef

### EndTimecode
- **Type**: typing.Optional[str]

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.VideoOverlayInputTypeDef]

### StartTimecode
- **Type**: typing.Optional[str]


# VideoPreprocessorExtraOutputTypeDef

### ColorCorrector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorCorrectorTypeDef]

### Deinterlacer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DeinterlacerTypeDef]

### DolbyVision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DolbyVisionTypeDef]

### Hdr10Plus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Hdr10PlusTypeDef]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterExtraOutputTypeDef]

### NoiseReducer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NoiseReducerTypeDef]

### PartnerWatermarking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PartnerWatermarkingTypeDef]

### TimecodeBurnin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimecodeBurninTypeDef]


# VideoPreprocessorOutputTypeDef

### ColorCorrector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorCorrectorTypeDef]

### Deinterlacer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DeinterlacerTypeDef]

### DolbyVision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DolbyVisionTypeDef]

### Hdr10Plus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Hdr10PlusTypeDef]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterOutputTypeDef]

### NoiseReducer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NoiseReducerTypeDef]

### PartnerWatermarking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PartnerWatermarkingTypeDef]

### TimecodeBurnin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimecodeBurninTypeDef]


# VideoPreprocessorTypeDef

### ColorCorrector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ColorCorrectorTypeDef]

### Deinterlacer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DeinterlacerTypeDef]

### DolbyVision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.DolbyVisionTypeDef]

### Hdr10Plus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Hdr10PlusTypeDef]

### ImageInserter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.ImageInserterTypeDef]

### NoiseReducer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.NoiseReducerTypeDef]

### PartnerWatermarking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.PartnerWatermarkingTypeDef]

### TimecodeBurnin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.TimecodeBurninTypeDef]


# VideoSelectorTypeDef

### AlphaBehavior
- **Type**: typing.Optional[typing.Literal['DISCARD', 'REMAP_TO_LUMA']]

### ColorSpace
- **Type**: typing.Optional[typing.Literal['FOLLOW', 'HDR10', 'HLG_2020', 'P3D65_HDR', 'P3D65_SDR', 'P3DCI', 'REC_601', 'REC_709']]

### ColorSpaceUsage
- **Type**: typing.Optional[typing.Literal['FALLBACK', 'FORCE']]

### EmbeddedTimecodeOverride
- **Type**: typing.Optional[typing.Literal['NONE', 'USE_MDPM']]

### Hdr10Metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Hdr10MetadataTypeDef]

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


# VorbisSettingsTypeDef

### Channels
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]

### VbrQuality
- **Type**: typing.Optional[int]


# Vp8SettingsTypeDef

### Bitrate
- **Type**: typing.Optional[int]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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


# Vp9SettingsTypeDef

### Bitrate
- **Type**: typing.Optional[int]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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


# WarningGroupTypeDef

### Code
- **Type**: <class 'int'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes


# WavSettingsTypeDef

### BitDepth
- **Type**: typing.Optional[int]

### Channels
- **Type**: typing.Optional[int]

### Format
- **Type**: typing.Optional[typing.Literal['RF64', 'RIFF']]

### SampleRate
- **Type**: typing.Optional[int]


# WebvttDestinationSettingsTypeDef

### Accessibility
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### StylePassthrough
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'STRICT']]


# WebvttHlsSourceSettingsTypeDef

### RenditionGroupId
- **Type**: typing.Optional[str]

### RenditionLanguageCode
- **Type**: typing.Optional[typing.Literal['AAR', 'ABK', 'AFR', 'AKA', 'AMH', 'ARA', 'ARG', 'ASM', 'AVA', 'AVE', 'AYM', 'AZE', 'BAK', 'BAM', 'BEL', 'BEN', 'BIH', 'BIS', 'BOD', 'BOS', 'BRE', 'BUL', 'CAT', 'CES', 'CHA', 'CHE', 'CHU', 'CHV', 'COR', 'COS', 'CRE', 'CYM', 'DAN', 'DEU', 'DIV', 'DZO', 'ELL', 'ENG', 'ENM', 'EPO', 'EST', 'EUS', 'EWE', 'FAO', 'FAS', 'FIJ', 'FIN', 'FRA', 'FRM', 'FRY', 'FUL', 'GER', 'GLA', 'GLE', 'GLG', 'GLV', 'GRN', 'GUJ', 'HAT', 'HAU', 'HEB', 'HER', 'HIN', 'HMO', 'HRV', 'HUN', 'HYE', 'IBO', 'IDO', 'III', 'IKU', 'ILE', 'INA', 'IND', 'IPK', 'ISL', 'ITA', 'JAV', 'JPN', 'KAL', 'KAN', 'KAS', 'KAT', 'KAU', 'KAZ', 'KHM', 'KIK', 'KIN', 'KIR', 'KOM', 'KON', 'KOR', 'KUA', 'KUR', 'LAO', 'LAT', 'LAV', 'LIM', 'LIN', 'LIT', 'LTZ', 'LUB', 'LUG', 'MAH', 'MAL', 'MAR', 'MKD', 'MLG', 'MLT', 'MON', 'MRI', 'MSA', 'MYA', 'NAU', 'NAV', 'NBL', 'NDE', 'NDO', 'NEP', 'NLD', 'NNO', 'NOB', 'NOR', 'NYA', 'OCI', 'OJI', 'ORI', 'ORJ', 'ORM', 'OSS', 'PAN', 'PLI', 'POL', 'POR', 'PUS', 'QAA', 'QPC', 'QUE', 'ROH', 'RON', 'RUN', 'RUS', 'SAG', 'SAN', 'SIN', 'SLK', 'SLV', 'SME', 'SMO', 'SNA', 'SND', 'SOM', 'SOT', 'SPA', 'SQI', 'SRB', 'SRD', 'SRP', 'SSW', 'SUN', 'SWA', 'SWE', 'TAH', 'TAM', 'TAT', 'TEL', 'TGK', 'TGL', 'THA', 'TIR', 'TNG', 'TON', 'TSN', 'TSO', 'TUK', 'TUR', 'TWI', 'UIG', 'UKR', 'URD', 'UZB', 'VEN', 'VIE', 'VOL', 'WLN', 'WOL', 'XHO', 'YID', 'YOR', 'ZHA', 'ZHO', 'ZUL']]

### RenditionName
- **Type**: typing.Optional[str]


# Xavc4kIntraCbgProfileSettingsTypeDef

### XavcClass
- **Type**: typing.Optional[typing.Literal['CLASS_100', 'CLASS_300', 'CLASS_480']]


# Xavc4kIntraVbrProfileSettingsTypeDef

### XavcClass
- **Type**: typing.Optional[typing.Literal['CLASS_100', 'CLASS_300', 'CLASS_480']]


# Xavc4kProfileSettingsTypeDef

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


# XavcHdIntraCbgProfileSettingsTypeDef

### XavcClass
- **Type**: typing.Optional[typing.Literal['CLASS_100', 'CLASS_200', 'CLASS_50']]


# XavcHdProfileSettingsTypeDef

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


# XavcSettingsTypeDef

### AdaptiveQuantization
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'HIGHER', 'LOW', 'MAX', 'MEDIUM', 'OFF']]

### EntropyEncoding
- **Type**: typing.Optional[typing.Literal['AUTO', 'CABAC', 'CAVLC']]

### FramerateControl
- **Type**: typing.Optional[typing.Literal['INITIALIZE_FROM_SOURCE', 'SPECIFIED']]

### FramerateConversionAlgorithm
- **Type**: typing.Optional[typing.Literal['DUPLICATE_DROP', 'FRAMEFORMER', 'INTERPOLATE']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Xavc4kIntraCbgProfileSettingsTypeDef]

### Xavc4kIntraVbrProfileSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Xavc4kIntraVbrProfileSettingsTypeDef]

### Xavc4kProfileSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.Xavc4kProfileSettingsTypeDef]

### XavcHdIntraCbgProfileSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.XavcHdIntraCbgProfileSettingsTypeDef]

### XavcHdProfileSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediaconvert_classes.XavcHdProfileSettingsTypeDef]


