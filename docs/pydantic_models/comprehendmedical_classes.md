# Comprehendmedical Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Characters

### OriginalTextCharacters
- **Type**: typing.Optional[int]


# ComprehendMedicalAsyncJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.Timestamp]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.Timestamp]


# ComprehendMedicalAsyncJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### ExpirationTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: <class 'NoneType'>

### OutputDataConfig
- **Type**: <class 'NoneType'>

### LanguageCode
- **Type**: typing.Optional[typing.Literal['en']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### ManifestFilePath
- **Type**: typing.Optional[str]

### KMSKey
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]


# DescribeEntitiesDetectionV2JobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEntitiesDetectionV2JobResponse

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeICD10CMInferenceJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeICD10CMInferenceJobResponse

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePHIDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePHIDetectionJobResponse

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRxNormInferenceJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRxNormInferenceJobResponse

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSNOMEDCTInferenceJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSNOMEDCTInferenceJobResponse

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DetectEntitiesResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.Entity]
- **Required**: Yes

### UnmappedAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.UnmappedAttribute]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DetectEntitiesV2Response

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.Entity]
- **Required**: Yes

### UnmappedAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.UnmappedAttribute]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DetectPHIResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.Entity]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# Entity

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ICD10CMConcept

### Description
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# ICD10CMEntity

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ICD10CMTrait

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# InferICD10CMResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ICD10CMEntity]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# InferRxNormResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.RxNormEntity]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# InferSNOMEDCTResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.SNOMEDCTEntity]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SNOMEDCTDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.SNOMEDCTDetails'>
- **Required**: Yes

### Characters
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.Characters'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# InputDataConfig

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Key
- **Type**: typing.Optional[str]


# ListEntitiesDetectionV2JobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntitiesDetectionV2JobsResponse

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListICD10CMInferenceJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListICD10CMInferenceJobsResponse

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPHIDetectionJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPHIDetectionJobsResponse

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRxNormInferenceJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRxNormInferenceJobsResponse

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSNOMEDCTInferenceJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSNOMEDCTInferenceJobsResponse

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OutputDataConfig

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Key
- **Type**: typing.Optional[str]


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


# RxNormConcept

### Description
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# RxNormEntity

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RxNormTrait

### Name
- **Type**: typing.Optional[typing.Literal['NEGATION', 'PAST_HISTORY']]

### Score
- **Type**: typing.Optional[float]


# SNOMEDCTConcept

### Description
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# SNOMEDCTDetails

### Edition
- **Type**: typing.Optional[str]

### Language
- **Type**: typing.Optional[str]

### VersionDate
- **Type**: typing.Optional[str]


# SNOMEDCTEntity

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SNOMEDCTTrait

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'FUTURE', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PAST_HISTORY', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# StartEntitiesDetectionV2JobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['en']
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### KMSKey
- **Type**: typing.Optional[str]


# StartEntitiesDetectionV2JobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StartICD10CMInferenceJobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['en']
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### KMSKey
- **Type**: typing.Optional[str]


# StartICD10CMInferenceJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StartPHIDetectionJobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['en']
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### KMSKey
- **Type**: typing.Optional[str]


# StartPHIDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StartRxNormInferenceJobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['en']
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### KMSKey
- **Type**: typing.Optional[str]


# StartRxNormInferenceJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StartSNOMEDCTInferenceJobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['en']
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### KMSKey
- **Type**: typing.Optional[str]


# StartSNOMEDCTInferenceJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StopEntitiesDetectionV2JobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopEntitiesDetectionV2JobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StopICD10CMInferenceJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopICD10CMInferenceJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StopPHIDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopPHIDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StopRxNormInferenceJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopRxNormInferenceJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StopSNOMEDCTInferenceJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopSNOMEDCTInferenceJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Trait

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'FUTURE', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PAST_HISTORY', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# UnmappedAttribute

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

