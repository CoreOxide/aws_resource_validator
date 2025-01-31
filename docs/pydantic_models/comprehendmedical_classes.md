# Comprehendmedical Classes

# AttributeTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.TraitTypeDef]]


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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# DescribeEntitiesDetectionV2JobRequestRequestTypeDef

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


# DescribeICD10CMInferenceJobRequestRequestTypeDef

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


# DescribePHIDetectionJobRequestRequestTypeDef

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


# DescribeRxNormInferenceJobRequestRequestTypeDef

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


# DescribeSNOMEDCTInferenceJobRequestRequestTypeDef

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


# DetectEntitiesRequestRequestTypeDef

### Text
- **Type**: <class 'str'>
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


# DetectEntitiesV2RequestRequestTypeDef

### Text
- **Type**: <class 'str'>
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


# DetectPHIRequestRequestTypeDef

### Text
- **Type**: <class 'str'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.TraitTypeDef]]

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.AttributeTypeDef]]


# ICD10CMAttributeTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ICD10CMTraitTypeDef]]

### Category
- **Type**: typing.Optional[typing.Literal['DX_NAME', 'TIME_EXPRESSION']]

### RelationshipType
- **Type**: typing.Optional[typing.Literal['OVERLAP', 'QUALITY', 'SYSTEM_ORGAN_SITE']]


# ICD10CMConceptTypeDef

### Description
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# ICD10CMEntityTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ICD10CMAttributeTypeDef]]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ICD10CMTraitTypeDef]]

### ICD10CMConcepts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.ICD10CMConceptTypeDef]]


# ICD10CMTraitTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# InferICD10CMRequestRequestTypeDef

### Text
- **Type**: <class 'str'>
- **Required**: Yes


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


# InferRxNormRequestRequestTypeDef

### Text
- **Type**: <class 'str'>
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


# InferSNOMEDCTRequestRequestTypeDef

### Text
- **Type**: <class 'str'>
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


# ListEntitiesDetectionV2JobsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListICD10CMInferenceJobsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPHIDetectionJobsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRxNormInferenceJobsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSNOMEDCTInferenceJobsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehendmedical_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# RxNormAttributeTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.RxNormTraitTypeDef]]


# RxNormConceptTypeDef

### Description
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# RxNormEntityTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.RxNormAttributeTypeDef]]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.RxNormTraitTypeDef]]

### RxNormConcepts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.RxNormConceptTypeDef]]


# RxNormTraitTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['NEGATION', 'PAST_HISTORY']]

### Score
- **Type**: typing.Optional[float]


# SNOMEDCTAttributeTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.SNOMEDCTTraitTypeDef]]

### SNOMEDCTConcepts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.SNOMEDCTConceptTypeDef]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.SNOMEDCTAttributeTypeDef]]

### Traits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.SNOMEDCTTraitTypeDef]]

### SNOMEDCTConcepts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehendmedical_classes.SNOMEDCTConceptTypeDef]]


# SNOMEDCTTraitTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'FUTURE', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PAST_HISTORY', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# StartEntitiesDetectionV2JobRequestRequestTypeDef

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


# StartICD10CMInferenceJobRequestRequestTypeDef

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


# StartPHIDetectionJobRequestRequestTypeDef

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


# StartRxNormInferenceJobRequestRequestTypeDef

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


# StartSNOMEDCTInferenceJobRequestRequestTypeDef

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


# StopEntitiesDetectionV2JobRequestRequestTypeDef

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


# StopICD10CMInferenceJobRequestRequestTypeDef

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


# StopPHIDetectionJobRequestRequestTypeDef

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


# StopRxNormInferenceJobRequestRequestTypeDef

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


# StopSNOMEDCTInferenceJobRequestRequestTypeDef

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


# TraitTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['DIAGNOSIS', 'FUTURE', 'HYPOTHETICAL', 'LOW_CONFIDENCE', 'NEGATION', 'PAST_HISTORY', 'PERTAINS_TO_FAMILY', 'SIGN', 'SYMPTOM']]

### Score
- **Type**: typing.Optional[float]


# UnmappedAttributeTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['ANATOMY', 'BEHAVIORAL_ENVIRONMENTAL_SOCIAL', 'MEDICAL_CONDITION', 'MEDICATION', 'PROTECTED_HEALTH_INFORMATION', 'TEST_TREATMENT_PROCEDURE', 'TIME_EXPRESSION']]

### Attribute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehendmedical_classes.AttributeTypeDef]


