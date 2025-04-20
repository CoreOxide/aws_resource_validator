# Comprehendmedical Comprehendmedical Classes

# Attribute

### Type
- **Type**: typing.Optional[typing.Literal['ACUITY', 'ADDRESS', 'AGE', 'ALCOHOL_CONSUMPTION', 'ALLERGIES', 'AMOUNT', 'BRAND_NAME', 'CONTACT_POINT', 'DATE', 'DIRECTION', 'DOSAGE', 'DURATION', 'DX_NAME', 'EMAIL', 'FORM', 'FREQUENCY', 'GENDER', 'GENERIC_NAME', 'ID', 'IDENTIFIER', 'NAME', 'PHONE_OR_FAX', 'PROCEDURE_NAME', 'PROFESSION', 'QUALITY', 'QUANTITY', 'RACE_ETHNICITY', 'RATE', 'REC_DRUG_USE', 'ROUTE_OR_MODE', 'STRENGTH', 'SYSTEM_ORGAN_SITE', 'TEST_NAME', 'TEST_UNIT', 'TEST_UNITS', 'TEST_VALUE', 'TIME_EXPRESSION', 'TIME_TO_DX_NAME', 'TIME_TO_MEDICATION_NAME', 'TIME_TO_PROCEDURE_NAME', 'TIME_TO_TEST_NAME', 'TIME_TO_TREATMENT_NAME', 'TOBACCO_USE', 'TREATMENT_NAME', 'URL']]

### Score
- **Type**: typing.Optional[float]

### RelationshipScore
- **Type**: typing.Optional[float]

### RelationshipType
- **Type**: typing.Optional[typing.Literal['ACUITY', 'ADMINISTERED_VIA', 'AMOUNT', 'DIRECTION', 'DOSAGE', 'DURATION', 'EVERY', 'FOR', 'FORM', 'FREQUENCY', 'NEGATIVE', 'OVERLAP', 'QUALITY', 'RATE', 'ROUTE_OR_MODE', 'STRENGTH', 'SYSTEM_ORGAN_SITE', 'TEST_UNIT', 'TEST_UNITS', 'TEST_VALUE', 'USAGE', 'WITH_DOSAGE']]

### Id
- **Type**: typing.Optional[int]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### Text
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[typing.Literal['ANATOMY', 'BEHAVIORAL_ENVIRONMENTAL_SOCIAL', 'MEDICAL_CONDITION', 'MEDICATION', 'PROTECTED_HEALTH_INFORMATION', 'TEST_TREATMENT_PROCEDURE', 'TIME_EXPRESSION']]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.Trait]]


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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeICD10CMInferenceJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeICD10CMInferenceJobResponse

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePHIDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePHIDetectionJobResponse

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRxNormInferenceJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRxNormInferenceJobResponse

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSNOMEDCTInferenceJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSNOMEDCTInferenceJobResponse

### ComprehendMedicalAsyncJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DetectEntitiesRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes


# DetectEntitiesResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.Entity]
- **Required**: Yes

### UnmappedAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.UnmappedAttribute]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DetectEntitiesV2Request

### Text
- **Type**: <class 'str'>
- **Required**: Yes


# DetectEntitiesV2Response

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.Entity]
- **Required**: Yes

### UnmappedAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.UnmappedAttribute]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# DetectPHIRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes


# DetectPHIResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.Entity]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# Entity

### Id
- **Type**: typing.Optional[int]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### Score
- **Type**: typing.Optional[float]

### Text
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[typing.Literal['ANATOMY', 'BEHAVIORAL_ENVIRONMENTAL_SOCIAL', 'MEDICAL_CONDITION', 'MEDICATION', 'PROTECTED_HEALTH_INFORMATION', 'TEST_TREATMENT_PROCEDURE', 'TIME_EXPRESSION']]

### Type
- **Type**: typing.Optional[typing.Literal['ACUITY', 'ADDRESS', 'AGE', 'ALCOHOL_CONSUMPTION', 'ALLERGIES', 'AMOUNT', 'BRAND_NAME', 'CONTACT_POINT', 'DATE', 'DIRECTION', 'DOSAGE', 'DURATION', 'DX_NAME', 'EMAIL', 'FORM', 'FREQUENCY', 'GENDER', 'GENERIC_NAME', 'ID', 'IDENTIFIER', 'NAME', 'PHONE_OR_FAX', 'PROCEDURE_NAME', 'PROFESSION', 'QUALITY', 'QUANTITY', 'RACE_ETHNICITY', 'RATE', 'REC_DRUG_USE', 'ROUTE_OR_MODE', 'STRENGTH', 'SYSTEM_ORGAN_SITE', 'TEST_NAME', 'TEST_UNIT', 'TEST_UNITS', 'TEST_VALUE', 'TIME_EXPRESSION', 'TIME_TO_DX_NAME', 'TIME_TO_MEDICATION_NAME', 'TIME_TO_PROCEDURE_NAME', 'TIME_TO_TEST_NAME', 'TIME_TO_TREATMENT_NAME', 'TOBACCO_USE', 'TREATMENT_NAME', 'URL']]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.Trait]]

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.Attribute]]


# ICD10CMAttribute

### Type
- **Type**: typing.Optional[typing.Literal['ACUITY', 'DIRECTION', 'QUALITY', 'QUANTITY', 'SYSTEM_ORGAN_SITE', 'TIME_EXPRESSION', 'TIME_TO_DX_NAME']]

### Score
- **Type**: typing.Optional[float]

### RelationshipScore
- **Type**: typing.Optional[float]

### Id
- **Type**: typing.Optional[int]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### Text
- **Type**: typing.Optional[str]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ICD10CMTrait]]

### Category
- **Type**: typing.Optional[typing.Literal['DX_NAME', 'TIME_EXPRESSION']]

### RelationshipType
- **Type**: typing.Optional[typing.Literal['OVERLAP', 'QUALITY', 'SYSTEM_ORGAN_SITE']]


# ICD10CMConcept

### Description
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# ICD10CMEntity

### Id
- **Type**: typing.Optional[int]

### Text
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[typing.Literal['MEDICAL_CONDITION']]

### Type
- **Type**: typing.Optional[typing.Literal['DX_NAME', 'TIME_EXPRESSION']]

### Score
- **Type**: typing.Optional[float]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ICD10CMAttribute]]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ICD10CMTrait]]

### ICD10CMConcepts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ICD10CMConcept]]


# ICD10CMTrait

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# InferICD10CMRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes


# InferICD10CMResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ICD10CMEntity]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# InferRxNormRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes


# InferRxNormResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.RxNormEntity]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# InferSNOMEDCTRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes


# InferSNOMEDCTResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.SNOMEDCTEntity]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SNOMEDCTDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.SNOMEDCTDetails'>
- **Required**: Yes

### Characters
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.Characters'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# InputDataConfig

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Key
- **Type**: typing.Optional[str]


# ListEntitiesDetectionV2JobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntitiesDetectionV2JobsResponse

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListICD10CMInferenceJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListICD10CMInferenceJobsResponse

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPHIDetectionJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPHIDetectionJobsResponse

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRxNormInferenceJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRxNormInferenceJobsResponse

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSNOMEDCTInferenceJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSNOMEDCTInferenceJobsResponse

### ComprehendMedicalAsyncJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ComprehendMedicalAsyncJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
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


# RxNormAttribute

### Type
- **Type**: typing.Optional[typing.Literal['DOSAGE', 'DURATION', 'FORM', 'FREQUENCY', 'RATE', 'ROUTE_OR_MODE', 'STRENGTH']]

### Score
- **Type**: typing.Optional[float]

### RelationshipScore
- **Type**: typing.Optional[float]

### Id
- **Type**: typing.Optional[int]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### Text
- **Type**: typing.Optional[str]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.RxNormTrait]]


# RxNormConcept

### Description
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# RxNormEntity

### Id
- **Type**: typing.Optional[int]

### Text
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[typing.Literal['MEDICATION']]

### Type
- **Type**: typing.Optional[typing.Literal['BRAND_NAME', 'GENERIC_NAME']]

### Score
- **Type**: typing.Optional[float]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.RxNormAttribute]]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.RxNormTrait]]

### RxNormConcepts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.RxNormConcept]]


# RxNormTrait

### Name
- **Type**: typing.Optional[typing.Literal['NEGATION', 'PAST_HISTORY']]

### Score
- **Type**: typing.Optional[float]


# SNOMEDCTAttribute

### Category
- **Type**: typing.Optional[typing.Literal['ANATOMY', 'MEDICAL_CONDITION', 'TEST_TREATMENT_PROCEDURE']]

### Type
- **Type**: typing.Optional[typing.Literal['ACUITY', 'DIRECTION', 'QUALITY', 'SYSTEM_ORGAN_SITE', 'TEST_UNIT', 'TEST_VALUE']]

### Score
- **Type**: typing.Optional[float]

### RelationshipScore
- **Type**: typing.Optional[float]

### RelationshipType
- **Type**: typing.Optional[typing.Literal['ACUITY', 'DIRECTION', 'QUALITY', 'SYSTEM_ORGAN_SITE', 'TEST_UNIT', 'TEST_UNITS', 'TEST_VALUE']]

### Id
- **Type**: typing.Optional[int]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### Text
- **Type**: typing.Optional[str]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.SNOMEDCTTrait]]

### SNOMEDCTConcepts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.SNOMEDCTConcept]]


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

### Id
- **Type**: typing.Optional[int]

### Text
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[typing.Literal['ANATOMY', 'MEDICAL_CONDITION', 'TEST_TREATMENT_PROCEDURE']]

### Type
- **Type**: typing.Optional[typing.Literal['DX_NAME', 'PROCEDURE_NAME', 'TEST_NAME', 'TREATMENT_NAME']]

### Score
- **Type**: typing.Optional[float]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.SNOMEDCTAttribute]]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.SNOMEDCTTrait]]

### SNOMEDCTConcepts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.SNOMEDCTConcept]]


# SNOMEDCTTrait

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'FUTURE', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PAST_HISTORY', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# StartEntitiesDetectionV2JobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.OutputDataConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StartICD10CMInferenceJobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.OutputDataConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StartPHIDetectionJobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.OutputDataConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StartRxNormInferenceJobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.OutputDataConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# StartSNOMEDCTInferenceJobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.OutputDataConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical.comprehendmedical_classes.ResponseMetadata'>
- **Required**: Yes


# Trait

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'FUTURE', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PAST_HISTORY', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# UnmappedAttribute

### Type
- **Type**: typing.Optional[typing.Literal['ANATOMY', 'BEHAVIORAL_ENVIRONMENTAL_SOCIAL', 'MEDICAL_CONDITION', 'MEDICATION', 'PROTECTED_HEALTH_INFORMATION', 'TEST_TREATMENT_PROCEDURE', 'TIME_EXPRESSION']]

### Attribute
- **Type**: <class 'NoneType'>


