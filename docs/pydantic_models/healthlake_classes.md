# Pydantic Models in healthlake_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateFHIRDatastoreRequestRequestTypeDef

### DatastoreTypeVersion
- **Type**: typing.Literal['R4']
- **Required**: Yes

### DatastoreName
- **Type**: typing.Optional[str]

### SseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.SseConfigurationTypeDef]

### PreloadDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.PreloadDataConfigTypeDef]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.healthlake_classes.TagTypeDef]]

### IdentityProviderConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.IdentityProviderConfigurationTypeDef]


# CreateFHIRDatastoreResponseTypeDef

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DatastoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatastoreStatus
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### DatastoreEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DatastoreFilterTypeDef

### DatastoreName
- **Type**: typing.Optional[str]

### DatastoreStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DatastorePropertiesTypeDef

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DatastoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatastoreStatus
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### DatastoreTypeVersion
- **Type**: typing.Literal['R4']
- **Required**: Yes

### DatastoreEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### DatastoreName
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### SseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.SseConfigurationTypeDef]

### PreloadDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.PreloadDataConfigTypeDef]

### IdentityProviderConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.IdentityProviderConfigurationTypeDef]

### ErrorCause
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.ErrorCauseTypeDef]


# DeleteFHIRDatastoreRequestRequestTypeDef

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFHIRDatastoreResponseTypeDef

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DatastoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatastoreStatus
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### DatastoreEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFHIRDatastoreRequestRequestTypeDef

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFHIRDatastoreResponseTypeDef

### DatastoreProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.DatastorePropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFHIRExportJobRequestRequestTypeDef

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFHIRExportJobResponseTypeDef

### ExportJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ExportJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFHIRImportJobRequestRequestTypeDef

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFHIRImportJobResponseTypeDef

### ImportJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ImportJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ErrorCauseTypeDef

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorCategory
- **Type**: typing.Optional[typing.Literal['NON_RETRYABLE_ERROR', 'RETRYABLE_ERROR']]


# ExportJobPropertiesTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### SubmitTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# IdentityProviderConfigurationTypeDef

### AuthorizationStrategy
- **Type**: typing.Literal['AWS_AUTH', 'SMART_ON_FHIR_V1']
- **Required**: Yes

### FineGrainedAuthorizationEnabled
- **Type**: typing.Optional[bool]

### Metadata
- **Type**: typing.Optional[str]

### IdpLambdaArn
- **Type**: typing.Optional[str]


# ImportJobPropertiesTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### SubmitTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### JobOutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.OutputDataConfigTypeDef]

### JobProgressReport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.JobProgressReportTypeDef]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# InputDataConfigTypeDef

### S3Uri
- **Type**: typing.Optional[str]


# JobProgressReportTypeDef

### TotalNumberOfScannedFiles
- **Type**: typing.Optional[int]

### TotalSizeOfScannedFilesInMB
- **Type**: typing.Optional[float]

### TotalNumberOfImportedFiles
- **Type**: typing.Optional[int]

### TotalNumberOfResourcesScanned
- **Type**: typing.Optional[int]

### TotalNumberOfResourcesImported
- **Type**: typing.Optional[int]

### TotalNumberOfResourcesWithCustomerError
- **Type**: typing.Optional[int]

### TotalNumberOfFilesReadWithCustomerError
- **Type**: typing.Optional[int]

### Throughput
- **Type**: typing.Optional[float]


# KmsEncryptionConfigTypeDef

### CmkType
- **Type**: typing.Literal['AWS_OWNED_KMS_KEY', 'CUSTOMER_MANAGED_KMS_KEY']
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ListFHIRDatastoresRequestRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.DatastoreFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFHIRDatastoresResponseTypeDef

### DatastorePropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.healthlake_classes.DatastorePropertiesTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFHIRExportJobsRequestRequestTypeDef

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### SubmittedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmittedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListFHIRExportJobsResponseTypeDef

### ExportJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.healthlake_classes.ExportJobPropertiesTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFHIRImportJobsRequestRequestTypeDef

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### SubmittedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmittedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListFHIRImportJobsResponseTypeDef

### ImportJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.healthlake_classes.ImportJobPropertiesTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.healthlake_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OutputDataConfigTypeDef

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake_classes.S3ConfigurationTypeDef]


# PreloadDataConfigTypeDef

### PreloadDataType
- **Type**: typing.Literal['SYNTHEA']
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


# S3ConfigurationTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# SseConfigurationTypeDef

### KmsEncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.KmsEncryptionConfigTypeDef'>
- **Required**: Yes


# StartFHIRExportJobRequestRequestTypeDef

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]


# StartFHIRExportJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartFHIRImportJobRequestRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### JobOutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]


# StartFHIRImportJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.healthlake_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


