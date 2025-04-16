# Translate Classes

# AppliedTerminology

### Name
- **Type**: typing.Optional[str]

### Terms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.translate_classes.Term]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateParallelDataRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ParallelDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataConfig'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EncryptionKey
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.translate_classes.Tag]]


# CreateParallelDataResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteParallelDataRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteParallelDataResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTerminologyRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTextTranslationJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTextTranslationJobResponse

### TextTranslationJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TextTranslationJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# Document

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.Blob'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionKey

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetParallelDataRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetParallelDataResponse

### ParallelDataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataProperties'>
- **Required**: Yes

### DataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataDataLocation'>
- **Required**: Yes

### AuxiliaryDataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataDataLocation'>
- **Required**: Yes

### LatestUpdateAttemptAuxiliaryDataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataDataLocation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# GetTerminologyRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TerminologyDataFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'TMX', 'TSV']]


# GetTerminologyResponse

### TerminologyProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyProperties'>
- **Required**: Yes

### TerminologyDataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyDataLocation'>
- **Required**: Yes

### AuxiliaryDataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyDataLocation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# ImportTerminologyRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MergeStrategy
- **Type**: typing.Literal['OVERWRITE']
- **Required**: Yes

### TerminologyData
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyData'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EncryptionKey
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.translate_classes.Tag]]


# ImportTerminologyResponse

### TerminologyProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyProperties'>
- **Required**: Yes

### AuxiliaryDataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyDataLocation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# InputDataConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes


# JobDetails

### TranslatedDocumentsCount
- **Type**: typing.Optional[int]

### DocumentsWithErrorsCount
- **Type**: typing.Optional[int]

### InputDocumentsCount
- **Type**: typing.Optional[int]


# Language

### LanguageName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: <class 'str'>
- **Required**: Yes


# ListLanguagesRequest

### DisplayLanguageCode
- **Type**: typing.Optional[typing.Literal['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLanguagesResponse

### Languages
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.Language]
- **Required**: Yes

### DisplayLanguageCode
- **Type**: typing.Literal['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListParallelDataRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListParallelDataResponse

### ParallelDataPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.ParallelDataProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# ListTerminologiesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTerminologiesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.PaginatorConfig]


# ListTerminologiesResponse

### TerminologyPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.TerminologyProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTextTranslationJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.TextTranslationJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTextTranslationJobsResponse

### TextTranslationJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.TextTranslationJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OutputDataConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKey
- **Type**: <class 'NoneType'>


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParallelDataConfig

### S3Uri
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[typing.Literal['CSV', 'TMX', 'TSV']]


# ParallelDataDataLocation

### RepositoryType
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes


# ParallelDataProperties

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### SourceLanguageCode
- **Type**: typing.Optional[str]

### TargetLanguageCodes
- **Type**: typing.Optional[typing.List[str]]

### ParallelDataConfig
- **Type**: <class 'NoneType'>

### Message
- **Type**: typing.Optional[str]

### ImportedDataSize
- **Type**: typing.Optional[int]

### ImportedRecordCount
- **Type**: typing.Optional[int]

### FailedRecordCount
- **Type**: typing.Optional[int]

### SkippedRecordCount
- **Type**: typing.Optional[int]

### EncryptionKey
- **Type**: <class 'NoneType'>

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### LatestUpdateAttemptStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### LatestUpdateAttemptAt
- **Type**: typing.Optional[datetime.datetime]


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


# StartTextTranslationJobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### TargetLanguageCodes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### TerminologyNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ParallelDataNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.TranslationSettings]


# StartTextTranslationJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'COMPLETED_WITH_ERROR', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# StopTextTranslationJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopTextTranslationJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'COMPLETED_WITH_ERROR', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.translate_classes.Tag]
- **Required**: Yes


# Term

### SourceText
- **Type**: typing.Optional[str]

### TargetText
- **Type**: typing.Optional[str]


# TerminologyData

### File
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.Blob'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['CSV', 'TMX', 'TSV']
- **Required**: Yes

### Directionality
- **Type**: typing.Optional[typing.Literal['MULTI', 'UNI']]


# TerminologyDataLocation

### RepositoryType
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes


# TerminologyProperties

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### SourceLanguageCode
- **Type**: typing.Optional[str]

### TargetLanguageCodes
- **Type**: typing.Optional[typing.List[str]]

### EncryptionKey
- **Type**: <class 'NoneType'>

### SizeBytes
- **Type**: typing.Optional[int]

### TermCount
- **Type**: typing.Optional[int]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Directionality
- **Type**: typing.Optional[typing.Literal['MULTI', 'UNI']]

### Message
- **Type**: typing.Optional[str]

### SkippedTermCount
- **Type**: typing.Optional[int]

### Format
- **Type**: typing.Optional[typing.Literal['CSV', 'TMX', 'TSV']]


# TextTranslationJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERROR', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmittedBeforeTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.Timestamp]

### SubmittedAfterTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.Timestamp]


# TextTranslationJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERROR', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### JobDetails
- **Type**: <class 'NoneType'>

### SourceLanguageCode
- **Type**: typing.Optional[str]

### TargetLanguageCodes
- **Type**: typing.Optional[typing.List[str]]

### TerminologyNames
- **Type**: typing.Optional[typing.List[str]]

### ParallelDataNames
- **Type**: typing.Optional[typing.List[str]]

### Message
- **Type**: typing.Optional[str]

### SubmittedTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: <class 'NoneType'>

### OutputDataConfig
- **Type**: <class 'NoneType'>

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.TranslationSettings]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TranslateDocumentRequest

### Document
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.Document'>
- **Required**: Yes

### SourceLanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### TargetLanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### TerminologyNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.TranslationSettings]


# TranslateDocumentResponse

### TranslatedDocument
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TranslatedDocument'>
- **Required**: Yes

### SourceLanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### TargetLanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### AppliedTerminologies
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.AppliedTerminology]
- **Required**: Yes

### AppliedSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TranslationSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# TranslateTextResponse

### TranslatedText
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### TargetLanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### AppliedTerminologies
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.AppliedTerminology]
- **Required**: Yes

### AppliedSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TranslationSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


# TranslatedDocument

### Content
- **Type**: <class 'bytes'>
- **Required**: Yes


# TranslationSettings

### Formality
- **Type**: typing.Optional[typing.Literal['FORMAL', 'INFORMAL']]

### Profanity
- **Type**: typing.Optional[typing.Literal['MASK']]

### Brevity
- **Type**: typing.Optional[typing.Literal['ON']]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateParallelDataRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ParallelDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataConfig'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateParallelDataResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### LatestUpdateAttemptStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### LatestUpdateAttemptAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadata'>
- **Required**: Yes


