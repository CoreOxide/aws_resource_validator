# Transcribe Classes

# AbsoluteTimeRangeTypeDef

### StartTime
- **Type**: typing.Optional[int]

### EndTime
- **Type**: typing.Optional[int]

### First
- **Type**: typing.Optional[int]

### Last
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CallAnalyticsJobDetailsTypeDef

### Skipped
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.CallAnalyticsSkippedFeatureTypeDef]]


# CallAnalyticsJobSettingsOutputTypeDef

### VocabularyName
- **Type**: typing.Optional[str]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]

### LanguageModelName
- **Type**: typing.Optional[str]

### ContentRedaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.ContentRedactionOutputTypeDef]

### LanguageOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]]

### LanguageIdSettings
- **Type**: typing.Optional[typing.Dict[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA'], aws_resource_validator.pydantic_models.transcribe_classes.LanguageIdSettingsTypeDef]]

### Summarization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.SummarizationTypeDef]


# CallAnalyticsJobSettingsTypeDef

### VocabularyName
- **Type**: typing.Optional[str]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]

### LanguageModelName
- **Type**: typing.Optional[str]

### ContentRedaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.ContentRedactionTypeDef]

### LanguageOptions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]]

### LanguageIdSettings
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA'], aws_resource_validator.pydantic_models.transcribe_classes.LanguageIdSettingsTypeDef]]

### Summarization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.SummarizationTypeDef]


# CallAnalyticsJobSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CallAnalyticsJobSummaryTypeDef

### CallAnalyticsJobName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### CallAnalyticsJobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### CallAnalyticsJobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.CallAnalyticsJobDetailsTypeDef]

### FailureReason
- **Type**: typing.Optional[str]


# CallAnalyticsJobTypeDef

### CallAnalyticsJobName
- **Type**: typing.Optional[str]

### CallAnalyticsJobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### CallAnalyticsJobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.CallAnalyticsJobDetailsTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### MediaSampleRateHertz
- **Type**: typing.Optional[int]

### MediaFormat
- **Type**: typing.Optional[typing.Literal['amr', 'flac', 'm4a', 'mp3', 'mp4', 'ogg', 'wav', 'webm']]

### Media
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.MediaTypeDef]

### Transcript
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.TranscriptTypeDef]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### IdentifiedLanguageScore
- **Type**: typing.Optional[float]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.CallAnalyticsJobSettingsOutputTypeDef]

### ChannelDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.ChannelDefinitionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]


# CallAnalyticsSkippedFeatureTypeDef

### Feature
- **Type**: typing.Optional[typing.Literal['GENERATIVE_SUMMARIZATION']]

### ReasonCode
- **Type**: typing.Optional[typing.Literal['FAILED_SAFETY_GUIDELINES', 'INSUFFICIENT_CONVERSATION_CONTENT']]

### Message
- **Type**: typing.Optional[str]


# CategoryPropertiesTypeDef

### CategoryName
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.RuleOutputTypeDef]]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]

### InputType
- **Type**: typing.Optional[typing.Literal['POST_CALL', 'REAL_TIME']]


# ChannelDefinitionTypeDef

### ChannelId
- **Type**: typing.Optional[int]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]


# ClinicalNoteGenerationSettingsTypeDef

### NoteTemplate
- **Type**: typing.Optional[typing.Literal['GIRPP', 'HISTORY_AND_PHYSICAL']]


# ContentRedactionOutputTypeDef

### RedactionType
- **Type**: typing.Literal['PII']
- **Required**: Yes

### RedactionOutput
- **Type**: typing.Literal['redacted', 'redacted_and_unredacted']
- **Required**: Yes

### PiiEntityTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADDRESS', 'ALL', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'EMAIL', 'NAME', 'PHONE', 'PIN', 'SSN']]]


# ContentRedactionTypeDef

### RedactionType
- **Type**: typing.Literal['PII']
- **Required**: Yes

### RedactionOutput
- **Type**: typing.Literal['redacted', 'redacted_and_unredacted']
- **Required**: Yes

### PiiEntityTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADDRESS', 'ALL', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'EMAIL', 'NAME', 'PHONE', 'PIN', 'SSN']]]


# ContentRedactionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCallAnalyticsCategoryRequestTypeDef

### CategoryName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.RuleUnionTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]

### InputType
- **Type**: typing.Optional[typing.Literal['POST_CALL', 'REAL_TIME']]


# CreateCallAnalyticsCategoryResponseTypeDef

### CategoryProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.CategoryPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLanguageModelRequestTypeDef

### LanguageCode
- **Type**: typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'hi-IN', 'ja-JP']
- **Required**: Yes

### BaseModelName
- **Type**: typing.Literal['NarrowBand', 'WideBand']
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]


# CreateLanguageModelResponseTypeDef

### LanguageCode
- **Type**: typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'hi-IN', 'ja-JP']
- **Required**: Yes

### BaseModelName
- **Type**: typing.Literal['NarrowBand', 'WideBand']
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### ModelStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMedicalVocabularyRequestTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### VocabularyFileUri
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]


# CreateMedicalVocabularyResponseTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### VocabularyState
- **Type**: typing.Literal['FAILED', 'PENDING', 'READY']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVocabularyFilterRequestTypeDef

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### Words
- **Type**: typing.Optional[typing.Sequence[str]]

### VocabularyFilterFileUri
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]

### DataAccessRoleArn
- **Type**: typing.Optional[str]


# CreateVocabularyFilterResponseTypeDef

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVocabularyRequestTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### Phrases
- **Type**: typing.Optional[typing.Sequence[str]]

### VocabularyFileUri
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]

### DataAccessRoleArn
- **Type**: typing.Optional[str]


# CreateVocabularyResponseTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### VocabularyState
- **Type**: typing.Literal['FAILED', 'PENDING', 'READY']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCallAnalyticsCategoryRequestTypeDef

### CategoryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCallAnalyticsJobRequestTypeDef

### CallAnalyticsJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLanguageModelRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMedicalScribeJobRequestTypeDef

### MedicalScribeJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMedicalTranscriptionJobRequestTypeDef

### MedicalTranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMedicalVocabularyRequestTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTranscriptionJobRequestTypeDef

### TranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVocabularyFilterRequestTypeDef

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVocabularyRequestTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLanguageModelRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLanguageModelResponseTypeDef

### LanguageModel
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.LanguageModelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCallAnalyticsCategoryRequestTypeDef

### CategoryName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCallAnalyticsCategoryResponseTypeDef

### CategoryProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.CategoryPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCallAnalyticsJobRequestTypeDef

### CallAnalyticsJobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCallAnalyticsJobResponseTypeDef

### CallAnalyticsJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.CallAnalyticsJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMedicalScribeJobRequestTypeDef

### MedicalScribeJobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMedicalScribeJobResponseTypeDef

### MedicalScribeJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.MedicalScribeJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMedicalTranscriptionJobRequestTypeDef

### MedicalTranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMedicalTranscriptionJobResponseTypeDef

### MedicalTranscriptionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.MedicalTranscriptionJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMedicalVocabularyRequestTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMedicalVocabularyResponseTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### VocabularyState
- **Type**: typing.Literal['FAILED', 'PENDING', 'READY']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### DownloadUri
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTranscriptionJobRequestTypeDef

### TranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTranscriptionJobResponseTypeDef

### TranscriptionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.TranscriptionJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVocabularyFilterRequestTypeDef

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes


# GetVocabularyFilterResponseTypeDef

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DownloadUri
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVocabularyRequestTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetVocabularyResponseTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### VocabularyState
- **Type**: typing.Literal['FAILED', 'PENDING', 'READY']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### DownloadUri
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputDataConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### TuningDataS3Uri
- **Type**: typing.Optional[str]


# InterruptionFilterTypeDef

### Threshold
- **Type**: typing.Optional[int]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]

### AbsoluteTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.AbsoluteTimeRangeTypeDef]

### RelativeTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.RelativeTimeRangeTypeDef]

### Negate
- **Type**: typing.Optional[bool]


# JobExecutionSettingsTypeDef

### AllowDeferredExecution
- **Type**: typing.Optional[bool]

### DataAccessRoleArn
- **Type**: typing.Optional[str]


# LanguageCodeItemTypeDef

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### DurationInSeconds
- **Type**: typing.Optional[float]


# LanguageIdSettingsTypeDef

### VocabularyName
- **Type**: typing.Optional[str]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### LanguageModelName
- **Type**: typing.Optional[str]


# LanguageModelTypeDef

### ModelName
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'hi-IN', 'ja-JP']]

### BaseModelName
- **Type**: typing.Optional[typing.Literal['NarrowBand', 'WideBand']]

### ModelStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### UpgradeAvailability
- **Type**: typing.Optional[bool]

### FailureReason
- **Type**: typing.Optional[str]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.InputDataConfigTypeDef]


# ListCallAnalyticsCategoriesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCallAnalyticsCategoriesResponseTypeDef

### Categories
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe_classes.CategoryPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCallAnalyticsJobsRequestTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### JobNameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCallAnalyticsJobsResponseTypeDef

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### CallAnalyticsJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe_classes.CallAnalyticsJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLanguageModelsRequestTypeDef

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLanguageModelsResponseTypeDef

### Models
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe_classes.LanguageModelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMedicalScribeJobsRequestTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### JobNameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMedicalScribeJobsResponseTypeDef

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### MedicalScribeJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe_classes.MedicalScribeJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMedicalTranscriptionJobsRequestTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### JobNameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMedicalTranscriptionJobsResponseTypeDef

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### MedicalTranscriptionJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe_classes.MedicalTranscriptionJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMedicalVocabulariesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StateEquals
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'READY']]

### NameContains
- **Type**: typing.Optional[str]


# ListMedicalVocabulariesResponseTypeDef

### Status
- **Type**: typing.Literal['FAILED', 'PENDING', 'READY']
- **Required**: Yes

### Vocabularies
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe_classes.VocabularyInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTranscriptionJobsRequestTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### JobNameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTranscriptionJobsResponseTypeDef

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### TranscriptionJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe_classes.TranscriptionJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVocabulariesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StateEquals
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'READY']]

### NameContains
- **Type**: typing.Optional[str]


# ListVocabulariesResponseTypeDef

### Status
- **Type**: typing.Literal['FAILED', 'PENDING', 'READY']
- **Required**: Yes

### Vocabularies
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe_classes.VocabularyInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVocabularyFiltersRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]


# ListVocabularyFiltersResponseTypeDef

### VocabularyFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe_classes.VocabularyFilterInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MediaTypeDef

### MediaFileUri
- **Type**: typing.Optional[str]

### RedactedMediaFileUri
- **Type**: typing.Optional[str]


# MedicalScribeChannelDefinitionTypeDef

### ChannelId
- **Type**: <class 'int'>
- **Required**: Yes

### ParticipantRole
- **Type**: typing.Literal['CLINICIAN', 'PATIENT']
- **Required**: Yes


# MedicalScribeJobSummaryTypeDef

### MedicalScribeJobName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['en-US']]

### MedicalScribeJobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### FailureReason
- **Type**: typing.Optional[str]


# MedicalScribeJobTypeDef

### MedicalScribeJobName
- **Type**: typing.Optional[str]

### MedicalScribeJobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['en-US']]

### Media
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.MediaTypeDef]

### MedicalScribeOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.MedicalScribeOutputTypeDef]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.MedicalScribeSettingsTypeDef]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### ChannelDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.MedicalScribeChannelDefinitionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]


# MedicalScribeOutputTypeDef

### TranscriptFileUri
- **Type**: <class 'str'>
- **Required**: Yes

### ClinicalDocumentUri
- **Type**: <class 'str'>
- **Required**: Yes


# MedicalScribeSettingsTypeDef

### ShowSpeakerLabels
- **Type**: typing.Optional[bool]

### MaxSpeakerLabels
- **Type**: typing.Optional[int]

### ChannelIdentification
- **Type**: typing.Optional[bool]

### VocabularyName
- **Type**: typing.Optional[str]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]

### ClinicalNoteGenerationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.ClinicalNoteGenerationSettingsTypeDef]


# MedicalTranscriptTypeDef

### TranscriptFileUri
- **Type**: typing.Optional[str]


# MedicalTranscriptionJobSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MedicalTranscriptionJobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MedicalTranscriptionSettingTypeDef

### ShowSpeakerLabels
- **Type**: typing.Optional[bool]

### MaxSpeakerLabels
- **Type**: typing.Optional[int]

### ChannelIdentification
- **Type**: typing.Optional[bool]

### ShowAlternatives
- **Type**: typing.Optional[bool]

### MaxAlternatives
- **Type**: typing.Optional[int]

### VocabularyName
- **Type**: typing.Optional[str]


# ModelSettingsTypeDef

### LanguageModelName
- **Type**: typing.Optional[str]


# NonTalkTimeFilterTypeDef

### Threshold
- **Type**: typing.Optional[int]

### AbsoluteTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.AbsoluteTimeRangeTypeDef]

### RelativeTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.RelativeTimeRangeTypeDef]

### Negate
- **Type**: typing.Optional[bool]


# RelativeTimeRangeTypeDef

### StartPercentage
- **Type**: typing.Optional[int]

### EndPercentage
- **Type**: typing.Optional[int]

### First
- **Type**: typing.Optional[int]

### Last
- **Type**: typing.Optional[int]


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


# RuleOutputTypeDef

### NonTalkTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.NonTalkTimeFilterTypeDef]

### InterruptionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.InterruptionFilterTypeDef]

### TranscriptFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.TranscriptFilterOutputTypeDef]

### SentimentFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.SentimentFilterOutputTypeDef]


# RuleTypeDef

### NonTalkTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.NonTalkTimeFilterTypeDef]

### InterruptionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.InterruptionFilterTypeDef]

### TranscriptFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.TranscriptFilterUnionTypeDef]

### SentimentFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.SentimentFilterUnionTypeDef]


# RuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SentimentFilterOutputTypeDef

### Sentiments
- **Type**: typing.List[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]
- **Required**: Yes

### AbsoluteTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.AbsoluteTimeRangeTypeDef]

### RelativeTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.RelativeTimeRangeTypeDef]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]

### Negate
- **Type**: typing.Optional[bool]


# SentimentFilterTypeDef

### Sentiments
- **Type**: typing.Sequence[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]
- **Required**: Yes

### AbsoluteTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.AbsoluteTimeRangeTypeDef]

### RelativeTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.RelativeTimeRangeTypeDef]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]

### Negate
- **Type**: typing.Optional[bool]


# SentimentFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SettingsTypeDef

### VocabularyName
- **Type**: typing.Optional[str]

### ShowSpeakerLabels
- **Type**: typing.Optional[bool]

### MaxSpeakerLabels
- **Type**: typing.Optional[int]

### ChannelIdentification
- **Type**: typing.Optional[bool]

### ShowAlternatives
- **Type**: typing.Optional[bool]

### MaxAlternatives
- **Type**: typing.Optional[int]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]


# StartCallAnalyticsJobRequestTypeDef

### CallAnalyticsJobName
- **Type**: <class 'str'>
- **Required**: Yes

### Media
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.MediaTypeDef'>
- **Required**: Yes

### OutputLocation
- **Type**: typing.Optional[str]

### OutputEncryptionKMSKeyId
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.CallAnalyticsJobSettingsUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]

### ChannelDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.ChannelDefinitionTypeDef]]


# StartCallAnalyticsJobResponseTypeDef

### CallAnalyticsJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.CallAnalyticsJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMedicalScribeJobRequestTypeDef

### MedicalScribeJobName
- **Type**: <class 'str'>
- **Required**: Yes

### Media
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.MediaTypeDef'>
- **Required**: Yes

### OutputBucketName
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.MedicalScribeSettingsTypeDef'>
- **Required**: Yes

### OutputEncryptionKMSKeyId
- **Type**: typing.Optional[str]

### KMSEncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ChannelDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.MedicalScribeChannelDefinitionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]


# StartMedicalScribeJobResponseTypeDef

### MedicalScribeJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.MedicalScribeJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMedicalTranscriptionJobResponseTypeDef

### MedicalTranscriptionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.MedicalTranscriptionJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTranscriptionJobRequestTypeDef

### TranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes

### Media
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.MediaTypeDef'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### MediaSampleRateHertz
- **Type**: typing.Optional[int]

### MediaFormat
- **Type**: typing.Optional[typing.Literal['amr', 'flac', 'm4a', 'mp3', 'mp4', 'ogg', 'wav', 'webm']]

### OutputBucketName
- **Type**: typing.Optional[str]

### OutputKey
- **Type**: typing.Optional[str]

### OutputEncryptionKMSKeyId
- **Type**: typing.Optional[str]

### KMSEncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.SettingsTypeDef]

### ModelSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.ModelSettingsTypeDef]

### JobExecutionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.JobExecutionSettingsTypeDef]

### ContentRedaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.ContentRedactionUnionTypeDef]

### IdentifyLanguage
- **Type**: typing.Optional[bool]

### IdentifyMultipleLanguages
- **Type**: typing.Optional[bool]

### LanguageOptions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]]

### Subtitles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.SubtitlesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]

### LanguageIdSettings
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA'], aws_resource_validator.pydantic_models.transcribe_classes.LanguageIdSettingsTypeDef]]

### ToxicityDetection
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.ToxicityDetectionSettingsUnionTypeDef]]


# StartTranscriptionJobResponseTypeDef

### TranscriptionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.TranscriptionJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubtitlesOutputTypeDef

### Formats
- **Type**: typing.Optional[typing.List[typing.Literal['srt', 'vtt']]]

### SubtitleFileUris
- **Type**: typing.Optional[typing.List[str]]

### OutputStartIndex
- **Type**: typing.Optional[int]


# SubtitlesTypeDef

### Formats
- **Type**: typing.Optional[typing.Sequence[typing.Literal['srt', 'vtt']]]

### OutputStartIndex
- **Type**: typing.Optional[int]


# SummarizationTypeDef

### GenerateAbstractiveSummary
- **Type**: <class 'bool'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ToxicityDetectionSettingsOutputTypeDef

### ToxicityCategories
- **Type**: typing.List[typing.Literal['ALL']]
- **Required**: Yes


# ToxicityDetectionSettingsTypeDef

### ToxicityCategories
- **Type**: typing.Sequence[typing.Literal['ALL']]
- **Required**: Yes


# ToxicityDetectionSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TranscriptFilterOutputTypeDef

### TranscriptFilterType
- **Type**: typing.Literal['EXACT']
- **Required**: Yes

### Targets
- **Type**: typing.List[str]
- **Required**: Yes

### AbsoluteTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.AbsoluteTimeRangeTypeDef]

### RelativeTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.RelativeTimeRangeTypeDef]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]

### Negate
- **Type**: typing.Optional[bool]


# TranscriptFilterTypeDef

### TranscriptFilterType
- **Type**: typing.Literal['EXACT']
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AbsoluteTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.AbsoluteTimeRangeTypeDef]

### RelativeTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.RelativeTimeRangeTypeDef]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]

### Negate
- **Type**: typing.Optional[bool]


# TranscriptFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TranscriptTypeDef

### TranscriptFileUri
- **Type**: typing.Optional[str]

### RedactedTranscriptFileUri
- **Type**: typing.Optional[str]


# TranscriptionJobSummaryTypeDef

### TranscriptionJobName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### TranscriptionJobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### FailureReason
- **Type**: typing.Optional[str]

### OutputLocationType
- **Type**: typing.Optional[typing.Literal['CUSTOMER_BUCKET', 'SERVICE_BUCKET']]

### ContentRedaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.ContentRedactionOutputTypeDef]

### ModelSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.ModelSettingsTypeDef]

### IdentifyLanguage
- **Type**: typing.Optional[bool]

### IdentifyMultipleLanguages
- **Type**: typing.Optional[bool]

### IdentifiedLanguageScore
- **Type**: typing.Optional[float]

### LanguageCodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.LanguageCodeItemTypeDef]]

### ToxicityDetection
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.ToxicityDetectionSettingsOutputTypeDef]]


# TranscriptionJobTypeDef

### TranscriptionJobName
- **Type**: typing.Optional[str]

### TranscriptionJobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### MediaSampleRateHertz
- **Type**: typing.Optional[int]

### MediaFormat
- **Type**: typing.Optional[typing.Literal['amr', 'flac', 'm4a', 'mp3', 'mp4', 'ogg', 'wav', 'webm']]

### Media
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.MediaTypeDef]

### Transcript
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.TranscriptTypeDef]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.SettingsTypeDef]

### ModelSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.ModelSettingsTypeDef]

### JobExecutionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.JobExecutionSettingsTypeDef]

### ContentRedaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.ContentRedactionOutputTypeDef]

### IdentifyLanguage
- **Type**: typing.Optional[bool]

### IdentifyMultipleLanguages
- **Type**: typing.Optional[bool]

### LanguageOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]]

### IdentifiedLanguageScore
- **Type**: typing.Optional[float]

### LanguageCodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.LanguageCodeItemTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.TagTypeDef]]

### Subtitles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe_classes.SubtitlesOutputTypeDef]

### LanguageIdSettings
- **Type**: typing.Optional[typing.Dict[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA'], aws_resource_validator.pydantic_models.transcribe_classes.LanguageIdSettingsTypeDef]]

### ToxicityDetection
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe_classes.ToxicityDetectionSettingsOutputTypeDef]]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCallAnalyticsCategoryRequestTypeDef

### CategoryName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.transcribe_classes.RuleUnionTypeDef]
- **Required**: Yes

### InputType
- **Type**: typing.Optional[typing.Literal['POST_CALL', 'REAL_TIME']]


# UpdateCallAnalyticsCategoryResponseTypeDef

### CategoryProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.CategoryPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMedicalVocabularyRequestTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### VocabularyFileUri
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateMedicalVocabularyResponseTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VocabularyState
- **Type**: typing.Literal['FAILED', 'PENDING', 'READY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVocabularyFilterRequestTypeDef

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### Words
- **Type**: typing.Optional[typing.Sequence[str]]

### VocabularyFilterFileUri
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]


# UpdateVocabularyFilterResponseTypeDef

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVocabularyRequestTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### Phrases
- **Type**: typing.Optional[typing.Sequence[str]]

### VocabularyFileUri
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]


# UpdateVocabularyResponseTypeDef

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VocabularyState
- **Type**: typing.Literal['FAILED', 'PENDING', 'READY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VocabularyFilterInfoTypeDef

### VocabularyFilterName
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# VocabularyInfoTypeDef

### VocabularyName
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### VocabularyState
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'READY']]


