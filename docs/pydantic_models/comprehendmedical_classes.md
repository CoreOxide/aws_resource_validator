# Comprehendmedical Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CharactersTypeDef

### OriginalTextCharacters
- **Type**: typing.Optional[int]


# ComprehendMedicalAsyncJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.TimestampTypeDef]


# ComprehendMedicalAsyncJobPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfigTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfigTypeDef]

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


# DescribeEntitiesDetectionV2JobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEntitiesDetectionV2JobResponseTypeDef

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeICD10CMInferenceJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeICD10CMInferenceJobResponseTypeDef

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePHIDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePHIDetectionJobResponseTypeDef

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRxNormInferenceJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRxNormInferenceJobResponseTypeDef

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSNOMEDCTInferenceJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSNOMEDCTInferenceJobResponseTypeDef

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectEntitiesResponseTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.EntityTypeDef]
- **Required**: Yes

### UnmappedAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.UnmappedAttributeTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectEntitiesV2ResponseTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.EntityTypeDef]
- **Required**: Yes

### UnmappedAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.UnmappedAttributeTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectPHIResponseTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.EntityTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EntityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ICD10CMConceptTypeDef

### Description
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# ICD10CMEntityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ICD10CMTraitTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# InferICD10CMResponseTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ICD10CMEntityTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InferRxNormResponseTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.RxNormEntityTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InferSNOMEDCTResponseTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.SNOMEDCTEntityTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SNOMEDCTDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.SNOMEDCTDetailsTypeDef'>
- **Required**: Yes

### Characters
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.CharactersTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputDataConfigTypeDef

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Key
- **Type**: typing.Optional[str]


# ListEntitiesDetectionV2JobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntitiesDetectionV2JobsResponseTypeDef

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListICD10CMInferenceJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListICD10CMInferenceJobsResponseTypeDef

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPHIDetectionJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPHIDetectionJobsResponseTypeDef

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRxNormInferenceJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRxNormInferenceJobsResponseTypeDef

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSNOMEDCTInferenceJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSNOMEDCTInferenceJobsResponseTypeDef

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ComprehendMedicalAsyncJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OutputDataConfigTypeDef

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Key
- **Type**: typing.Optional[str]


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


# RxNormConceptTypeDef

### Description
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# RxNormEntityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RxNormTraitTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['NEGATION', 'PAST_HISTORY']]

### Score
- **Type**: typing.Optional[float]


# SNOMEDCTConceptTypeDef

### Description
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# SNOMEDCTDetailsTypeDef

### Edition
- **Type**: typing.Optional[str]

### Language
- **Type**: typing.Optional[str]

### VersionDate
- **Type**: typing.Optional[str]


# SNOMEDCTEntityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SNOMEDCTTraitTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'FUTURE', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PAST_HISTORY', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# StartEntitiesDetectionV2JobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfigTypeDef'>
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


# StartEntitiesDetectionV2JobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartICD10CMInferenceJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfigTypeDef'>
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


# StartICD10CMInferenceJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartPHIDetectionJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfigTypeDef'>
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


# StartPHIDetectionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartRxNormInferenceJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfigTypeDef'>
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


# StartRxNormInferenceJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSNOMEDCTInferenceJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.OutputDataConfigTypeDef'>
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


# StartSNOMEDCTInferenceJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopEntitiesDetectionV2JobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopEntitiesDetectionV2JobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopICD10CMInferenceJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopICD10CMInferenceJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopPHIDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopPHIDetectionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopRxNormInferenceJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopRxNormInferenceJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopSNOMEDCTInferenceJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopSNOMEDCTInferenceJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TraitTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'FUTURE', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PAST_HISTORY', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# UnmappedAttributeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

