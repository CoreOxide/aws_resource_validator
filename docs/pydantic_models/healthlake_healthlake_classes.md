# Healthlake Healthlake Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateFHIRDatastoreRequest

### DatastoreTypeVersion
- **Type**: typing.Literal['R4']
- **Required**: Yes

### DatastoreName
- **Type**: typing.Optional[str]

### SseConfiguration
- **Type**: <class 'NoneType'>

### PreloadDataConfig
- **Type**: <class 'NoneType'>

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.healthlake.healthlake_classes.Tag]]

### IdentityProviderConfiguration
- **Type**: <class 'NoneType'>


# CreateFHIRDatastoreResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes


# DatastoreFilter

### DatastoreName
- **Type**: typing.Optional[str]

### DatastoreStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DatastoreProperties

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
- **Type**: <class 'NoneType'>

### PreloadDataConfig
- **Type**: <class 'NoneType'>

### IdentityProviderConfiguration
- **Type**: <class 'NoneType'>

### ErrorCause
- **Type**: <class 'NoneType'>


# DeleteFHIRDatastoreRequest

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFHIRDatastoreResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFHIRDatastoreRequest

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFHIRDatastoreResponse

### DatastoreProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.DatastoreProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFHIRExportJobRequest

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFHIRExportJobResponse

### ExportJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ExportJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFHIRImportJobRequest

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFHIRImportJobResponse

### ImportJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ImportJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes


# ErrorCause

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorCategory
- **Type**: typing.Optional[typing.Literal['NON_RETRYABLE_ERROR', 'RETRYABLE_ERROR']]


# ExportJobProperties

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'SUBMITTED']
- **Required**: Yes

### SubmitTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.OutputDataConfig'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# IdentityProviderConfiguration

### AuthorizationStrategy
- **Type**: typing.Literal['AWS_AUTH', 'SMART_ON_FHIR', 'SMART_ON_FHIR_V1']
- **Required**: Yes

### FineGrainedAuthorizationEnabled
- **Type**: typing.Optional[bool]

### Metadata
- **Type**: typing.Optional[str]

### IdpLambdaArn
- **Type**: typing.Optional[str]


# ImportJobProperties

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'SUBMITTED']
- **Required**: Yes

### SubmitTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.InputDataConfig'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### JobOutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake.healthlake_classes.OutputDataConfig]

### JobProgressReport
- **Type**: <class 'NoneType'>

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# InputDataConfig

### S3Uri
- **Type**: typing.Optional[str]


# JobProgressReport

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


# KmsEncryptionConfig

### CmkType
- **Type**: typing.Literal['AWS_OWNED_KMS_KEY', 'CUSTOMER_MANAGED_KMS_KEY']
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ListFHIRDatastoresRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.healthlake.healthlake_classes.DatastoreFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFHIRDatastoresResponse

### DatastorePropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.healthlake.healthlake_classes.DatastoreProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFHIRExportJobsRequest

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
- **Type**: typing.Optional[typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'SUBMITTED']]

### SubmittedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmittedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListFHIRExportJobsResponse

### ExportJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ExportJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFHIRImportJobsRequest

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
- **Type**: typing.Optional[typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'SUBMITTED']]

### SubmittedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmittedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListFHIRImportJobsResponse

### ImportJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ImportJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.healthlake.healthlake_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes


# OutputDataConfig

### S3Configuration
- **Type**: <class 'NoneType'>


# PreloadDataConfig

### PreloadDataType
- **Type**: typing.Literal['SYNTHEA']
- **Required**: Yes


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


# S3Configuration

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# SseConfiguration

### KmsEncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.KmsEncryptionConfig'>
- **Required**: Yes


# StartFHIRExportJobRequest

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.OutputDataConfig'>
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# StartFHIRExportJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'SUBMITTED']
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes


# StartFHIRImportJobRequest

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.InputDataConfig'>
- **Required**: Yes

### JobOutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.OutputDataConfig'>
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# StartFHIRImportJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['CANCEL_COMPLETED', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_SUBMITTED', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'SUBMITTED']
- **Required**: Yes

### DatastoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.healthlake.healthlake_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.healthlake.healthlake_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


