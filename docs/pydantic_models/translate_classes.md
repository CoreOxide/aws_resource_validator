# translate_classes

# AppliedTerminologyTypeDef

### Name
- **Type**: typing.Optional[str]

### Terms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.translate_classes.TermTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateParallelDataRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ParallelDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataConfigTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EncryptionKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.EncryptionKeyTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.translate_classes.TagTypeDef]]


# CreateParallelDataResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteParallelDataRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteParallelDataResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTerminologyRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTextTranslationJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTextTranslationJobResponseTypeDef

### TextTranslationJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TextTranslationJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentTypeDef

### Content
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionKeyTypeDef

### Type
- **Type**: typing.Literal['KMS']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetParallelDataRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetParallelDataResponseTypeDef

### ParallelDataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataPropertiesTypeDef'>
- **Required**: Yes

### DataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataDataLocationTypeDef'>
- **Required**: Yes

### AuxiliaryDataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataDataLocationTypeDef'>
- **Required**: Yes

### LatestUpdateAttemptAuxiliaryDataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataDataLocationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTerminologyRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TerminologyDataFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'TMX', 'TSV']]


# GetTerminologyResponseTypeDef

### TerminologyProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyPropertiesTypeDef'>
- **Required**: Yes

### TerminologyDataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyDataLocationTypeDef'>
- **Required**: Yes

### AuxiliaryDataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyDataLocationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportTerminologyRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MergeStrategy
- **Type**: typing.Literal['OVERWRITE']
- **Required**: Yes

### TerminologyData
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyDataTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EncryptionKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.EncryptionKeyTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.translate_classes.TagTypeDef]]


# ImportTerminologyResponseTypeDef

### TerminologyProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyPropertiesTypeDef'>
- **Required**: Yes

### AuxiliaryDataLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TerminologyDataLocationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputDataConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes


# JobDetailsTypeDef

### TranslatedDocumentsCount
- **Type**: typing.Optional[int]

### DocumentsWithErrorsCount
- **Type**: typing.Optional[int]

### InputDocumentsCount
- **Type**: typing.Optional[int]


# LanguageTypeDef

### LanguageName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: <class 'str'>
- **Required**: Yes


# ListLanguagesRequestRequestTypeDef

### DisplayLanguageCode
- **Type**: typing.Optional[typing.Literal['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLanguagesResponseTypeDef

### Languages
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.LanguageTypeDef]
- **Required**: Yes

### DisplayLanguageCode
- **Type**: typing.Literal['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListParallelDataRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListParallelDataResponseTypeDef

### ParallelDataPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.ParallelDataPropertiesTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTerminologiesRequestListTerminologiesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.PaginatorConfigTypeDef]


# ListTerminologiesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTerminologiesResponseTypeDef

### TerminologyPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.TerminologyPropertiesTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTextTranslationJobsRequestRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.TextTranslationJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTextTranslationJobsResponseTypeDef

### TextTranslationJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.TextTranslationJobPropertiesTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OutputDataConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.EncryptionKeyTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParallelDataConfigTypeDef

### S3Uri
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[typing.Literal['CSV', 'TMX', 'TSV']]


# ParallelDataDataLocationTypeDef

### RepositoryType
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes


# ParallelDataPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.ParallelDataConfigTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.EncryptionKeyTypeDef]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### LatestUpdateAttemptStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### LatestUpdateAttemptAt
- **Type**: typing.Optional[datetime.datetime]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# StartTextTranslationJobRequestRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.OutputDataConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.TranslationSettingsTypeDef]


# StartTextTranslationJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'COMPLETED_WITH_ERROR', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopTextTranslationJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopTextTranslationJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'COMPLETED_WITH_ERROR', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.translate_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TermTypeDef

### SourceText
- **Type**: typing.Optional[str]

### TargetText
- **Type**: typing.Optional[str]


# TerminologyDataLocationTypeDef

### RepositoryType
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes


# TerminologyDataTypeDef

### File
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### Format
- **Type**: typing.Literal['CSV', 'TMX', 'TSV']
- **Required**: Yes

### Directionality
- **Type**: typing.Optional[typing.Literal['MULTI', 'UNI']]


# TerminologyPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.EncryptionKeyTypeDef]

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


# TextTranslationJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERROR', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmittedBeforeTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmittedAfterTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TextTranslationJobPropertiesTypeDef

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERROR', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### JobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.JobDetailsTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.InputDataConfigTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.OutputDataConfigTypeDef]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.TranslationSettingsTypeDef]


# TranslateDocumentRequestRequestTypeDef

### Document
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.DocumentTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.TranslationSettingsTypeDef]


# TranslateDocumentResponseTypeDef

### TranslatedDocument
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TranslatedDocumentTypeDef'>
- **Required**: Yes

### SourceLanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### TargetLanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### AppliedTerminologies
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.AppliedTerminologyTypeDef]
- **Required**: Yes

### AppliedSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TranslationSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TranslateTextRequestRequestTypeDef

### Text
- **Type**: <class 'str'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.translate_classes.TranslationSettingsTypeDef]


# TranslateTextResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.translate_classes.AppliedTerminologyTypeDef]
- **Required**: Yes

### AppliedSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.TranslationSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TranslatedDocumentTypeDef

### Content
- **Type**: <class 'bytes'>
- **Required**: Yes


# TranslationSettingsTypeDef

### Formality
- **Type**: typing.Optional[typing.Literal['FORMAL', 'INFORMAL']]

### Profanity
- **Type**: typing.Optional[typing.Literal['MASK']]

### Brevity
- **Type**: typing.Optional[typing.Literal['ON']]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateParallelDataRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ParallelDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ParallelDataConfigTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateParallelDataResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.translate_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


