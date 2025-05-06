# Transcribe Classes

# AbsoluteTimeRange

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

# CallAnalyticsJob

### CallAnalyticsJobName
- **Type**: typing.Optional[str]

### CallAnalyticsJobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### CallAnalyticsJobDetails
- **Type**: <class 'NoneType'>

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### MediaSampleRateHertz
- **Type**: typing.Optional[int]

### MediaFormat
- **Type**: typing.Optional[typing.Literal['amr', 'flac', 'm4a', 'mp3', 'mp4', 'ogg', 'wav', 'webm']]

### Media
- **Type**: <class 'NoneType'>

### Transcript
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CallAnalyticsJobSettingsOutput]

### ChannelDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ChannelDefinition]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]


# CallAnalyticsJobDetails

### Skipped
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CallAnalyticsSkippedFeature]]


# CallAnalyticsJobSettings

### VocabularyName
- **Type**: typing.Optional[str]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]

### LanguageModelName
- **Type**: typing.Optional[str]

### ContentRedaction
- **Type**: <class 'NoneType'>

### LanguageOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]]

### LanguageIdSettings
- **Type**: typing.Optional[typing.Dict[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA'], NoneType]]

### Summarization
- **Type**: <class 'NoneType'>


# CallAnalyticsJobSettingsOutput

### VocabularyName
- **Type**: typing.Optional[str]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]

### LanguageModelName
- **Type**: typing.Optional[str]

### ContentRedaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ContentRedactionOutput]

### LanguageOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]]

### LanguageIdSettings
- **Type**: typing.Optional[typing.Dict[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA'], NoneType]]

### Summarization
- **Type**: <class 'NoneType'>


# CallAnalyticsJobSummary

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
- **Type**: <class 'NoneType'>

### FailureReason
- **Type**: typing.Optional[str]


# CallAnalyticsSkippedFeature

### Feature
- **Type**: typing.Optional[typing.Literal['GENERATIVE_SUMMARIZATION']]

### ReasonCode
- **Type**: typing.Optional[typing.Literal['FAILED_SAFETY_GUIDELINES', 'INSUFFICIENT_CONVERSATION_CONTENT']]

### Message
- **Type**: typing.Optional[str]


# CategoryProperties

### CategoryName
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.RuleOutput]]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]

### InputType
- **Type**: typing.Optional[typing.Literal['POST_CALL', 'REAL_TIME']]


# ChannelDefinition

### ChannelId
- **Type**: typing.Optional[int]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]


# ClinicalNoteGenerationSettings

### NoteTemplate
- **Type**: typing.Optional[typing.Literal['GIRPP', 'HISTORY_AND_PHYSICAL']]


# ContentRedaction

### RedactionType
- **Type**: typing.Literal['PII']
- **Required**: Yes

### RedactionOutput
- **Type**: typing.Literal['redacted', 'redacted_and_unredacted']
- **Required**: Yes

### PiiEntityTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADDRESS', 'ALL', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'EMAIL', 'NAME', 'PHONE', 'PIN', 'SSN']]]


# ContentRedactionOutput

### RedactionType
- **Type**: typing.Literal['PII']
- **Required**: Yes

### RedactionOutput
- **Type**: typing.Literal['redacted', 'redacted_and_unredacted']
- **Required**: Yes

### PiiEntityTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADDRESS', 'ALL', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'EMAIL', 'NAME', 'PHONE', 'PIN', 'SSN']]]


# CreateCallAnalyticsCategoryRequest

### CategoryName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Rule, aws_resource_validator.pydantic_models.transcribe.transcribe_classes.RuleOutput]]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]

### InputType
- **Type**: typing.Optional[typing.Literal['POST_CALL', 'REAL_TIME']]


# CreateCallAnalyticsCategoryResponse

### CategoryProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CategoryProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLanguageModelRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.InputDataConfig'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]


# CreateLanguageModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.InputDataConfig'>
- **Required**: Yes

### ModelStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMedicalVocabularyRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]


# CreateMedicalVocabularyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVocabularyFilterRequest

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### Words
- **Type**: typing.Optional[typing.List[str]]

### VocabularyFilterFileUri
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]

### DataAccessRoleArn
- **Type**: typing.Optional[str]


# CreateVocabularyFilterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVocabularyRequest

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### Phrases
- **Type**: typing.Optional[typing.List[str]]

### VocabularyFileUri
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]

### DataAccessRoleArn
- **Type**: typing.Optional[str]


# CreateVocabularyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCallAnalyticsCategoryRequest

### CategoryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCallAnalyticsJobRequest

### CallAnalyticsJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLanguageModelRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMedicalScribeJobRequest

### MedicalScribeJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMedicalTranscriptionJobRequest

### MedicalTranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMedicalVocabularyRequest

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTranscriptionJobRequest

### TranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVocabularyFilterRequest

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVocabularyRequest

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLanguageModelRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLanguageModelResponse

### LanguageModel
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.LanguageModel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# GetCallAnalyticsCategoryRequest

### CategoryName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCallAnalyticsCategoryResponse

### CategoryProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CategoryProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# GetCallAnalyticsJobRequest

### CallAnalyticsJobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCallAnalyticsJobResponse

### CallAnalyticsJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CallAnalyticsJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# GetMedicalScribeJobRequest

### MedicalScribeJobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMedicalScribeJobResponse

### MedicalScribeJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalScribeJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# GetMedicalTranscriptionJobRequest

### MedicalTranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMedicalTranscriptionJobResponse

### MedicalTranscriptionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalTranscriptionJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# GetMedicalVocabularyRequest

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMedicalVocabularyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# GetTranscriptionJobRequest

### TranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTranscriptionJobResponse

### TranscriptionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.TranscriptionJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# GetVocabularyFilterRequest

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes


# GetVocabularyFilterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# GetVocabularyRequest

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetVocabularyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# InputDataConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### TuningDataS3Uri
- **Type**: typing.Optional[str]


# InterruptionFilter

### Threshold
- **Type**: typing.Optional[int]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]

### AbsoluteTimeRange
- **Type**: <class 'NoneType'>

### RelativeTimeRange
- **Type**: <class 'NoneType'>

### Negate
- **Type**: typing.Optional[bool]


# JobExecutionSettings

### AllowDeferredExecution
- **Type**: typing.Optional[bool]

### DataAccessRoleArn
- **Type**: typing.Optional[str]


# LanguageCodeItem

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### DurationInSeconds
- **Type**: typing.Optional[float]


# LanguageIdSettings

### VocabularyName
- **Type**: typing.Optional[str]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### LanguageModelName
- **Type**: typing.Optional[str]


# LanguageModel

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
- **Type**: <class 'NoneType'>


# ListCallAnalyticsCategoriesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCallAnalyticsCategoriesResponse

### Categories
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CategoryProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCallAnalyticsJobsRequest

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### JobNameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCallAnalyticsJobsResponse

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### CallAnalyticsJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CallAnalyticsJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLanguageModelsRequest

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLanguageModelsResponse

### Models
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.LanguageModel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMedicalScribeJobsRequest

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### JobNameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMedicalScribeJobsResponse

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### MedicalScribeJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalScribeJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMedicalTranscriptionJobsRequest

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### JobNameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMedicalTranscriptionJobsResponse

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### MedicalTranscriptionJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalTranscriptionJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMedicalVocabulariesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StateEquals
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'READY']]

### NameContains
- **Type**: typing.Optional[str]


# ListMedicalVocabulariesResponse

### Status
- **Type**: typing.Literal['FAILED', 'PENDING', 'READY']
- **Required**: Yes

### Vocabularies
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.VocabularyInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# ListTranscriptionJobsRequest

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### JobNameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTranscriptionJobsResponse

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### TranscriptionJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.TranscriptionJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVocabulariesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StateEquals
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'READY']]

### NameContains
- **Type**: typing.Optional[str]


# ListVocabulariesResponse

### Status
- **Type**: typing.Literal['FAILED', 'PENDING', 'READY']
- **Required**: Yes

### Vocabularies
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.VocabularyInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVocabularyFiltersRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]


# ListVocabularyFiltersResponse

### VocabularyFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.VocabularyFilterInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Media

### MediaFileUri
- **Type**: typing.Optional[str]

### RedactedMediaFileUri
- **Type**: typing.Optional[str]


# MedicalScribeChannelDefinition

### ChannelId
- **Type**: <class 'int'>
- **Required**: Yes

### ParticipantRole
- **Type**: typing.Literal['CLINICIAN', 'PATIENT']
- **Required**: Yes


# MedicalScribeJob

### MedicalScribeJobName
- **Type**: typing.Optional[str]

### MedicalScribeJobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['en-US']]

### Media
- **Type**: <class 'NoneType'>

### MedicalScribeOutput
- **Type**: <class 'NoneType'>

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalScribeSettings]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### ChannelDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalScribeChannelDefinition]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]


# MedicalScribeJobSummary

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


# MedicalScribeOutput

### TranscriptFileUri
- **Type**: <class 'str'>
- **Required**: Yes

### ClinicalDocumentUri
- **Type**: <class 'str'>
- **Required**: Yes


# MedicalScribeSettings

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
- **Type**: <class 'NoneType'>


# MedicalTranscript

### TranscriptFileUri
- **Type**: typing.Optional[str]


# MedicalTranscriptionJob

### MedicalTranscriptionJobName
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
- **Type**: <class 'NoneType'>

### Transcript
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalTranscript]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalTranscriptionSetting]

### ContentIdentificationType
- **Type**: typing.Optional[typing.Literal['PHI']]

### Specialty
- **Type**: typing.Optional[typing.Literal['PRIMARYCARE']]

### Type
- **Type**: typing.Optional[typing.Literal['CONVERSATION', 'DICTATION']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]


# MedicalTranscriptionJobSummary

### MedicalTranscriptionJobName
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

### Specialty
- **Type**: typing.Optional[typing.Literal['PRIMARYCARE']]

### ContentIdentificationType
- **Type**: typing.Optional[typing.Literal['PHI']]

### Type
- **Type**: typing.Optional[typing.Literal['CONVERSATION', 'DICTATION']]


# MedicalTranscriptionSetting

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


# ModelSettings

### LanguageModelName
- **Type**: typing.Optional[str]


# NonTalkTimeFilter

### Threshold
- **Type**: typing.Optional[int]

### AbsoluteTimeRange
- **Type**: <class 'NoneType'>

### RelativeTimeRange
- **Type**: <class 'NoneType'>

### Negate
- **Type**: typing.Optional[bool]


# RelativeTimeRange

### StartPercentage
- **Type**: typing.Optional[int]

### EndPercentage
- **Type**: typing.Optional[int]

### First
- **Type**: typing.Optional[int]

### Last
- **Type**: typing.Optional[int]


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


# Rule

### NonTalkTimeFilter
- **Type**: <class 'NoneType'>

### InterruptionFilter
- **Type**: <class 'NoneType'>

### TranscriptFilter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.TranscriptFilter, aws_resource_validator.pydantic_models.transcribe.transcribe_classes.TranscriptFilterOutput, NoneType]

### SentimentFilter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.SentimentFilter, aws_resource_validator.pydantic_models.transcribe.transcribe_classes.SentimentFilterOutput, NoneType]


# RuleOutput

### NonTalkTimeFilter
- **Type**: <class 'NoneType'>

### InterruptionFilter
- **Type**: <class 'NoneType'>

### TranscriptFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.TranscriptFilterOutput]

### SentimentFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.SentimentFilterOutput]


# SentimentFilter

### Sentiments
- **Type**: typing.List[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]
- **Required**: Yes

### AbsoluteTimeRange
- **Type**: <class 'NoneType'>

### RelativeTimeRange
- **Type**: <class 'NoneType'>

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]

### Negate
- **Type**: typing.Optional[bool]


# SentimentFilterOutput

### Sentiments
- **Type**: typing.List[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]
- **Required**: Yes

### AbsoluteTimeRange
- **Type**: <class 'NoneType'>

### RelativeTimeRange
- **Type**: <class 'NoneType'>

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]

### Negate
- **Type**: typing.Optional[bool]


# Settings

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


# StartCallAnalyticsJobRequest

### CallAnalyticsJobName
- **Type**: <class 'str'>
- **Required**: Yes

### Media
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Media'>
- **Required**: Yes

### OutputLocation
- **Type**: typing.Optional[str]

### OutputEncryptionKMSKeyId
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CallAnalyticsJobSettings, aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CallAnalyticsJobSettingsOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]

### ChannelDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ChannelDefinition]]


# StartCallAnalyticsJobResponse

### CallAnalyticsJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CallAnalyticsJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# StartMedicalScribeJobRequest

### MedicalScribeJobName
- **Type**: <class 'str'>
- **Required**: Yes

### Media
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Media'>
- **Required**: Yes

### OutputBucketName
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalScribeSettings'>
- **Required**: Yes

### OutputEncryptionKMSKeyId
- **Type**: typing.Optional[str]

### KMSEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### ChannelDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalScribeChannelDefinition]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]


# StartMedicalScribeJobResponse

### MedicalScribeJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalScribeJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# StartMedicalTranscriptionJobRequest

### MedicalTranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### Media
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Media'>
- **Required**: Yes

### OutputBucketName
- **Type**: <class 'str'>
- **Required**: Yes

### Specialty
- **Type**: typing.Literal['PRIMARYCARE']
- **Required**: Yes

### Type
- **Type**: typing.Literal['CONVERSATION', 'DICTATION']
- **Required**: Yes

### MediaSampleRateHertz
- **Type**: typing.Optional[int]

### MediaFormat
- **Type**: typing.Optional[typing.Literal['amr', 'flac', 'm4a', 'mp3', 'mp4', 'ogg', 'wav', 'webm']]

### OutputKey
- **Type**: typing.Optional[str]

### OutputEncryptionKMSKeyId
- **Type**: typing.Optional[str]

### KMSEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalTranscriptionSetting]

### ContentIdentificationType
- **Type**: typing.Optional[typing.Literal['PHI']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]


# StartMedicalTranscriptionJobResponse

### MedicalTranscriptionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.MedicalTranscriptionJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# StartTranscriptionJobRequest

### TranscriptionJobName
- **Type**: <class 'str'>
- **Required**: Yes

### Media
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Media'>
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
- **Type**: typing.Optional[typing.Dict[str, str]]

### Settings
- **Type**: <class 'NoneType'>

### ModelSettings
- **Type**: <class 'NoneType'>

### JobExecutionSettings
- **Type**: <class 'NoneType'>

### ContentRedaction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ContentRedaction, aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ContentRedactionOutput, NoneType]

### IdentifyLanguage
- **Type**: typing.Optional[bool]

### IdentifyMultipleLanguages
- **Type**: typing.Optional[bool]

### LanguageOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]]

### Subtitles
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]

### LanguageIdSettings
- **Type**: typing.Optional[typing.Dict[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA'], NoneType]]

### ToxicityDetection
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ToxicityDetectionSettings, aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ToxicityDetectionSettingsOutput]]]


# StartTranscriptionJobResponse

### TranscriptionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.TranscriptionJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# Subtitles

### Formats
- **Type**: typing.Optional[typing.List[typing.Literal['srt', 'vtt']]]

### OutputStartIndex
- **Type**: typing.Optional[int]


# SubtitlesOutput

### Formats
- **Type**: typing.Optional[typing.List[typing.Literal['srt', 'vtt']]]

### SubtitleFileUris
- **Type**: typing.Optional[typing.List[str]]

### OutputStartIndex
- **Type**: typing.Optional[int]


# Summarization

### GenerateAbstractiveSummary
- **Type**: <class 'bool'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]
- **Required**: Yes


# ToxicityDetectionSettings

### ToxicityCategories
- **Type**: typing.List[typing.Literal['ALL']]
- **Required**: Yes


# ToxicityDetectionSettingsOutput

### ToxicityCategories
- **Type**: typing.List[typing.Literal['ALL']]
- **Required**: Yes


# Transcript

### TranscriptFileUri
- **Type**: typing.Optional[str]

### RedactedTranscriptFileUri
- **Type**: typing.Optional[str]


# TranscriptFilter

### TranscriptFilterType
- **Type**: typing.Literal['EXACT']
- **Required**: Yes

### Targets
- **Type**: typing.List[str]
- **Required**: Yes

### AbsoluteTimeRange
- **Type**: <class 'NoneType'>

### RelativeTimeRange
- **Type**: <class 'NoneType'>

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]

### Negate
- **Type**: typing.Optional[bool]


# TranscriptFilterOutput

### TranscriptFilterType
- **Type**: typing.Literal['EXACT']
- **Required**: Yes

### Targets
- **Type**: typing.List[str]
- **Required**: Yes

### AbsoluteTimeRange
- **Type**: <class 'NoneType'>

### RelativeTimeRange
- **Type**: <class 'NoneType'>

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]

### Negate
- **Type**: typing.Optional[bool]


# TranscriptionJob

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
- **Type**: <class 'NoneType'>

### Transcript
- **Type**: <class 'NoneType'>

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### Settings
- **Type**: <class 'NoneType'>

### ModelSettings
- **Type**: <class 'NoneType'>

### JobExecutionSettings
- **Type**: <class 'NoneType'>

### ContentRedaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ContentRedactionOutput]

### IdentifyLanguage
- **Type**: typing.Optional[bool]

### IdentifyMultipleLanguages
- **Type**: typing.Optional[bool]

### LanguageOptions
- **Type**: typing.Optional[typing.List[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]]

### IdentifiedLanguageScore
- **Type**: typing.Optional[float]

### LanguageCodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.LanguageCodeItem]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Tag]]

### Subtitles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.SubtitlesOutput]

### LanguageIdSettings
- **Type**: typing.Optional[typing.Dict[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA'], NoneType]]

### ToxicityDetection
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ToxicityDetectionSettingsOutput]]


# TranscriptionJobSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ContentRedactionOutput]

### ModelSettings
- **Type**: <class 'NoneType'>

### IdentifyLanguage
- **Type**: typing.Optional[bool]

### IdentifyMultipleLanguages
- **Type**: typing.Optional[bool]

### IdentifiedLanguageScore
- **Type**: typing.Optional[float]

### LanguageCodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.LanguageCodeItem]]

### ToxicityDetection
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ToxicityDetectionSettingsOutput]]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCallAnalyticsCategoryRequest

### CategoryName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.transcribe.transcribe_classes.Rule, aws_resource_validator.pydantic_models.transcribe.transcribe_classes.RuleOutput]]
- **Required**: Yes

### InputType
- **Type**: typing.Optional[typing.Literal['POST_CALL', 'REAL_TIME']]


# UpdateCallAnalyticsCategoryResponse

### CategoryProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.CategoryProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMedicalVocabularyRequest

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### VocabularyFileUri
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateMedicalVocabularyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVocabularyFilterRequest

### VocabularyFilterName
- **Type**: <class 'str'>
- **Required**: Yes

### Words
- **Type**: typing.Optional[typing.List[str]]

### VocabularyFilterFileUri
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]


# UpdateVocabularyFilterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVocabularyRequest

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']
- **Required**: Yes

### Phrases
- **Type**: typing.Optional[typing.List[str]]

### VocabularyFileUri
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]


# UpdateVocabularyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.transcribe.transcribe_classes.ResponseMetadata'>
- **Required**: Yes


# VocabularyFilterInfo

### VocabularyFilterName
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# VocabularyInfo

### VocabularyName
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ab-GE', 'af-ZA', 'ar-AE', 'ar-SA', 'ast-ES', 'az-AZ', 'ba-RU', 'be-BY', 'bg-BG', 'bn-IN', 'bs-BA', 'ca-ES', 'ckb-IQ', 'ckb-IR', 'cs-CZ', 'cy-WL', 'da-DK', 'de-CH', 'de-DE', 'el-GR', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'et-ET', 'eu-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gl-ES', 'gu-IN', 'ha-NG', 'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'ka-GE', 'kab-DZ', 'kk-KZ', 'kn-IN', 'ko-KR', 'ky-KG', 'lg-IN', 'lt-LT', 'lv-LV', 'mhr-RU', 'mi-NZ', 'mk-MK', 'ml-IN', 'mn-MN', 'mr-IN', 'ms-MY', 'mt-MT', 'nl-NL', 'no-NO', 'or-IN', 'pa-IN', 'pl-PL', 'ps-AF', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'rw-RW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'sr-RS', 'su-ID', 'sv-SE', 'sw-BI', 'sw-KE', 'sw-RW', 'sw-TZ', 'sw-UG', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR', 'tt-RU', 'ug-CN', 'uk-UA', 'uz-UZ', 'vi-VN', 'wo-SN', 'zh-CN', 'zh-TW', 'zu-ZA']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### VocabularyState
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'READY']]


