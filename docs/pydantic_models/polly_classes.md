# polly_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteLexiconInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVoicesInputDescribeVoicesPaginateTypeDef

### Engine
- **Type**: typing.Optional[typing.Literal['generative', 'long-form', 'neural', 'standard']]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'arb', 'ca-ES', 'cmn-CN', 'cy-GB', 'da-DK', 'de-AT', 'de-DE', 'en-AU', 'en-GB', 'en-GB-WLS', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'es-ES', 'es-MX', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-FR', 'hi-IN', 'is-IS', 'it-IT', 'ja-JP', 'ko-KR', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'sv-SE', 'tr-TR', 'yue-CN']]

### IncludeAdditionalLanguageCodes
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.polly_classes.PaginatorConfigTypeDef]


# DescribeVoicesInputRequestTypeDef

### Engine
- **Type**: typing.Optional[typing.Literal['generative', 'long-form', 'neural', 'standard']]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'arb', 'ca-ES', 'cmn-CN', 'cy-GB', 'da-DK', 'de-AT', 'de-DE', 'en-AU', 'en-GB', 'en-GB-WLS', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'es-ES', 'es-MX', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-FR', 'hi-IN', 'is-IS', 'it-IT', 'ja-JP', 'ko-KR', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'sv-SE', 'tr-TR', 'yue-CN']]

### IncludeAdditionalLanguageCodes
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]


# DescribeVoicesOutputTypeDef

### Voices
- **Type**: typing.List[aws_resource_validator.pydantic_models.polly_classes.VoiceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLexiconInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetLexiconOutputTypeDef

### Lexicon
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.LexiconTypeDef'>
- **Required**: Yes

### LexiconAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.LexiconAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSpeechSynthesisTaskInputRequestTypeDef

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSpeechSynthesisTaskOutputTypeDef

### SynthesisTask
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.SynthesisTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LexiconAttributesTypeDef

### Alphabet
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'arb', 'ca-ES', 'cmn-CN', 'cy-GB', 'da-DK', 'de-AT', 'de-DE', 'en-AU', 'en-GB', 'en-GB-WLS', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'es-ES', 'es-MX', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-FR', 'hi-IN', 'is-IS', 'it-IT', 'ja-JP', 'ko-KR', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'sv-SE', 'tr-TR', 'yue-CN']]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### LexiconArn
- **Type**: typing.Optional[str]

### LexemesCount
- **Type**: typing.Optional[int]

### Size
- **Type**: typing.Optional[int]


# LexiconDescriptionTypeDef

### Name
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.polly_classes.LexiconAttributesTypeDef]


# LexiconTypeDef

### Content
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ListLexiconsInputListLexiconsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.polly_classes.PaginatorConfigTypeDef]


# ListLexiconsInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListLexiconsOutputTypeDef

### Lexicons
- **Type**: typing.List[aws_resource_validator.pydantic_models.polly_classes.LexiconDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSpeechSynthesisTasksInputListSpeechSynthesisTasksPaginateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['completed', 'failed', 'inProgress', 'scheduled']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.polly_classes.PaginatorConfigTypeDef]


# ListSpeechSynthesisTasksInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['completed', 'failed', 'inProgress', 'scheduled']]


# ListSpeechSynthesisTasksOutputTypeDef

### SynthesisTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.polly_classes.SynthesisTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutLexiconInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


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


# StartSpeechSynthesisTaskInputRequestTypeDef

### OutputFormat
- **Type**: typing.Literal['json', 'mp3', 'ogg_vorbis', 'pcm']
- **Required**: Yes

### OutputS3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceId
- **Type**: typing.Literal['Aditi', 'Adriano', 'Amy', 'Andres', 'Aria', 'Arlet', 'Arthur', 'Astrid', 'Ayanda', 'Bianca', 'Brian', 'Burcu', 'Camila', 'Carla', 'Carmen', 'Celine', 'Chantal', 'Conchita', 'Cristiano', 'Daniel', 'Danielle', 'Dora', 'Elin', 'Emma', 'Enrique', 'Ewa', 'Filiz', 'Gabrielle', 'Geraint', 'Giorgio', 'Gregory', 'Gwyneth', 'Hala', 'Hannah', 'Hans', 'Hiujin', 'Ida', 'Ines', 'Isabelle', 'Ivy', 'Jacek', 'Jan', 'Joanna', 'Joey', 'Justin', 'Kajal', 'Karl', 'Kazuha', 'Kendra', 'Kevin', 'Kimberly', 'Laura', 'Lea', 'Liam', 'Lisa', 'Liv', 'Lotte', 'Lucia', 'Lupe', 'Mads', 'Maja', 'Marlene', 'Mathieu', 'Matthew', 'Maxim', 'Mia', 'Miguel', 'Mizuki', 'Naja', 'Niamh', 'Nicole', 'Ola', 'Olivia', 'Pedro', 'Penelope', 'Raveena', 'Remi', 'Ricardo', 'Ruben', 'Russell', 'Ruth', 'Salli', 'Seoyeon', 'Sergio', 'Sofie', 'Stephen', 'Suvi', 'Takumi', 'Tatyana', 'Thiago', 'Tomoko', 'Vicki', 'Vitoria', 'Zayd', 'Zeina', 'Zhiyu']
- **Required**: Yes

### Engine
- **Type**: typing.Optional[typing.Literal['generative', 'long-form', 'neural', 'standard']]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'arb', 'ca-ES', 'cmn-CN', 'cy-GB', 'da-DK', 'de-AT', 'de-DE', 'en-AU', 'en-GB', 'en-GB-WLS', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'es-ES', 'es-MX', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-FR', 'hi-IN', 'is-IS', 'it-IT', 'ja-JP', 'ko-KR', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'sv-SE', 'tr-TR', 'yue-CN']]

### LexiconNames
- **Type**: typing.Optional[typing.Sequence[str]]

### OutputS3KeyPrefix
- **Type**: typing.Optional[str]

### SampleRate
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SpeechMarkTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['sentence', 'ssml', 'viseme', 'word']]]

### TextType
- **Type**: typing.Optional[typing.Literal['ssml', 'text']]


# StartSpeechSynthesisTaskOutputTypeDef

### SynthesisTask
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.SynthesisTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SynthesisTaskTypeDef

### Engine
- **Type**: typing.Optional[typing.Literal['generative', 'long-form', 'neural', 'standard']]

### TaskId
- **Type**: typing.Optional[str]

### TaskStatus
- **Type**: typing.Optional[typing.Literal['completed', 'failed', 'inProgress', 'scheduled']]

### TaskStatusReason
- **Type**: typing.Optional[str]

### OutputUri
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### RequestCharacters
- **Type**: typing.Optional[int]

### SnsTopicArn
- **Type**: typing.Optional[str]

### LexiconNames
- **Type**: typing.Optional[typing.List[str]]

### OutputFormat
- **Type**: typing.Optional[typing.Literal['json', 'mp3', 'ogg_vorbis', 'pcm']]

### SampleRate
- **Type**: typing.Optional[str]

### SpeechMarkTypes
- **Type**: typing.Optional[typing.List[typing.Literal['sentence', 'ssml', 'viseme', 'word']]]

### TextType
- **Type**: typing.Optional[typing.Literal['ssml', 'text']]

### VoiceId
- **Type**: typing.Optional[typing.Literal['Aditi', 'Adriano', 'Amy', 'Andres', 'Aria', 'Arlet', 'Arthur', 'Astrid', 'Ayanda', 'Bianca', 'Brian', 'Burcu', 'Camila', 'Carla', 'Carmen', 'Celine', 'Chantal', 'Conchita', 'Cristiano', 'Daniel', 'Danielle', 'Dora', 'Elin', 'Emma', 'Enrique', 'Ewa', 'Filiz', 'Gabrielle', 'Geraint', 'Giorgio', 'Gregory', 'Gwyneth', 'Hala', 'Hannah', 'Hans', 'Hiujin', 'Ida', 'Ines', 'Isabelle', 'Ivy', 'Jacek', 'Jan', 'Joanna', 'Joey', 'Justin', 'Kajal', 'Karl', 'Kazuha', 'Kendra', 'Kevin', 'Kimberly', 'Laura', 'Lea', 'Liam', 'Lisa', 'Liv', 'Lotte', 'Lucia', 'Lupe', 'Mads', 'Maja', 'Marlene', 'Mathieu', 'Matthew', 'Maxim', 'Mia', 'Miguel', 'Mizuki', 'Naja', 'Niamh', 'Nicole', 'Ola', 'Olivia', 'Pedro', 'Penelope', 'Raveena', 'Remi', 'Ricardo', 'Ruben', 'Russell', 'Ruth', 'Salli', 'Seoyeon', 'Sergio', 'Sofie', 'Stephen', 'Suvi', 'Takumi', 'Tatyana', 'Thiago', 'Tomoko', 'Vicki', 'Vitoria', 'Zayd', 'Zeina', 'Zhiyu']]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'arb', 'ca-ES', 'cmn-CN', 'cy-GB', 'da-DK', 'de-AT', 'de-DE', 'en-AU', 'en-GB', 'en-GB-WLS', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'es-ES', 'es-MX', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-FR', 'hi-IN', 'is-IS', 'it-IT', 'ja-JP', 'ko-KR', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'sv-SE', 'tr-TR', 'yue-CN']]


# SynthesizeSpeechInputRequestTypeDef

### OutputFormat
- **Type**: typing.Literal['json', 'mp3', 'ogg_vorbis', 'pcm']
- **Required**: Yes

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceId
- **Type**: typing.Literal['Aditi', 'Adriano', 'Amy', 'Andres', 'Aria', 'Arlet', 'Arthur', 'Astrid', 'Ayanda', 'Bianca', 'Brian', 'Burcu', 'Camila', 'Carla', 'Carmen', 'Celine', 'Chantal', 'Conchita', 'Cristiano', 'Daniel', 'Danielle', 'Dora', 'Elin', 'Emma', 'Enrique', 'Ewa', 'Filiz', 'Gabrielle', 'Geraint', 'Giorgio', 'Gregory', 'Gwyneth', 'Hala', 'Hannah', 'Hans', 'Hiujin', 'Ida', 'Ines', 'Isabelle', 'Ivy', 'Jacek', 'Jan', 'Joanna', 'Joey', 'Justin', 'Kajal', 'Karl', 'Kazuha', 'Kendra', 'Kevin', 'Kimberly', 'Laura', 'Lea', 'Liam', 'Lisa', 'Liv', 'Lotte', 'Lucia', 'Lupe', 'Mads', 'Maja', 'Marlene', 'Mathieu', 'Matthew', 'Maxim', 'Mia', 'Miguel', 'Mizuki', 'Naja', 'Niamh', 'Nicole', 'Ola', 'Olivia', 'Pedro', 'Penelope', 'Raveena', 'Remi', 'Ricardo', 'Ruben', 'Russell', 'Ruth', 'Salli', 'Seoyeon', 'Sergio', 'Sofie', 'Stephen', 'Suvi', 'Takumi', 'Tatyana', 'Thiago', 'Tomoko', 'Vicki', 'Vitoria', 'Zayd', 'Zeina', 'Zhiyu']
- **Required**: Yes

### Engine
- **Type**: typing.Optional[typing.Literal['generative', 'long-form', 'neural', 'standard']]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'arb', 'ca-ES', 'cmn-CN', 'cy-GB', 'da-DK', 'de-AT', 'de-DE', 'en-AU', 'en-GB', 'en-GB-WLS', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'es-ES', 'es-MX', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-FR', 'hi-IN', 'is-IS', 'it-IT', 'ja-JP', 'ko-KR', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'sv-SE', 'tr-TR', 'yue-CN']]

### LexiconNames
- **Type**: typing.Optional[typing.Sequence[str]]

### SampleRate
- **Type**: typing.Optional[str]

### SpeechMarkTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['sentence', 'ssml', 'viseme', 'word']]]

### TextType
- **Type**: typing.Optional[typing.Literal['ssml', 'text']]


# SynthesizeSpeechOutputTypeDef

### AudioStream
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### RequestCharacters
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.polly_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VoiceTypeDef

### Gender
- **Type**: typing.Optional[typing.Literal['Female', 'Male']]

### Id
- **Type**: typing.Optional[typing.Literal['Aditi', 'Adriano', 'Amy', 'Andres', 'Aria', 'Arlet', 'Arthur', 'Astrid', 'Ayanda', 'Bianca', 'Brian', 'Burcu', 'Camila', 'Carla', 'Carmen', 'Celine', 'Chantal', 'Conchita', 'Cristiano', 'Daniel', 'Danielle', 'Dora', 'Elin', 'Emma', 'Enrique', 'Ewa', 'Filiz', 'Gabrielle', 'Geraint', 'Giorgio', 'Gregory', 'Gwyneth', 'Hala', 'Hannah', 'Hans', 'Hiujin', 'Ida', 'Ines', 'Isabelle', 'Ivy', 'Jacek', 'Jan', 'Joanna', 'Joey', 'Justin', 'Kajal', 'Karl', 'Kazuha', 'Kendra', 'Kevin', 'Kimberly', 'Laura', 'Lea', 'Liam', 'Lisa', 'Liv', 'Lotte', 'Lucia', 'Lupe', 'Mads', 'Maja', 'Marlene', 'Mathieu', 'Matthew', 'Maxim', 'Mia', 'Miguel', 'Mizuki', 'Naja', 'Niamh', 'Nicole', 'Ola', 'Olivia', 'Pedro', 'Penelope', 'Raveena', 'Remi', 'Ricardo', 'Ruben', 'Russell', 'Ruth', 'Salli', 'Seoyeon', 'Sergio', 'Sofie', 'Stephen', 'Suvi', 'Takumi', 'Tatyana', 'Thiago', 'Tomoko', 'Vicki', 'Vitoria', 'Zayd', 'Zeina', 'Zhiyu']]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'arb', 'ca-ES', 'cmn-CN', 'cy-GB', 'da-DK', 'de-AT', 'de-DE', 'en-AU', 'en-GB', 'en-GB-WLS', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'es-ES', 'es-MX', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-FR', 'hi-IN', 'is-IS', 'it-IT', 'ja-JP', 'ko-KR', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'sv-SE', 'tr-TR', 'yue-CN']]

### LanguageName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### AdditionalLanguageCodes
- **Type**: typing.Optional[typing.List[typing.Literal['ar-AE', 'arb', 'ca-ES', 'cmn-CN', 'cy-GB', 'da-DK', 'de-AT', 'de-DE', 'en-AU', 'en-GB', 'en-GB-WLS', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'es-ES', 'es-MX', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-FR', 'hi-IN', 'is-IS', 'it-IT', 'ja-JP', 'ko-KR', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'sv-SE', 'tr-TR', 'yue-CN']]]

### SupportedEngines
- **Type**: typing.Optional[typing.List[typing.Literal['generative', 'long-form', 'neural', 'standard']]]


