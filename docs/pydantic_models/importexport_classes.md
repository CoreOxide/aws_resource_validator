# Importexport Classes

# Artifact

### Description
- **Type**: typing.Optional[str]

### URL
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobInput

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### APIVersion
- **Type**: typing.Optional[str]


# CancelJobOutput

### Success
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.importexport.importexport_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJobInput

### JobType
- **Type**: typing.Literal['Export', 'Import']
- **Required**: Yes

### Manifest
- **Type**: <class 'str'>
- **Required**: Yes

### ValidateOnly
- **Type**: <class 'bool'>
- **Required**: Yes

### ManifestAddendum
- **Type**: typing.Optional[str]

### APIVersion
- **Type**: typing.Optional[str]


# CreateJobOutput

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['Export', 'Import']
- **Required**: Yes

### Signature
- **Type**: <class 'str'>
- **Required**: Yes

### SignatureFileContents
- **Type**: <class 'str'>
- **Required**: Yes

### WarningMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.importexport.importexport_classes.Artifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.importexport.importexport_classes.ResponseMetadata'>
- **Required**: Yes


# GetShippingLabelInput

### jobIds
- **Type**: typing.List[str]
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### company
- **Type**: typing.Optional[str]

### phoneNumber
- **Type**: typing.Optional[str]

### country
- **Type**: typing.Optional[str]

### stateOrProvince
- **Type**: typing.Optional[str]

### city
- **Type**: typing.Optional[str]

### postalCode
- **Type**: typing.Optional[str]

### street1
- **Type**: typing.Optional[str]

### street2
- **Type**: typing.Optional[str]

### street3
- **Type**: typing.Optional[str]

### APIVersion
- **Type**: typing.Optional[str]


# GetShippingLabelOutput

### ShippingLabelURL
- **Type**: <class 'str'>
- **Required**: Yes

### Warning
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.importexport.importexport_classes.ResponseMetadata'>
- **Required**: Yes


# GetStatusInput

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### APIVersion
- **Type**: typing.Optional[str]


# GetStatusOutput

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['Export', 'Import']
- **Required**: Yes

### LocationCode
- **Type**: <class 'str'>
- **Required**: Yes

### LocationMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ProgressCode
- **Type**: <class 'str'>
- **Required**: Yes

### ProgressMessage
- **Type**: <class 'str'>
- **Required**: Yes

### Carrier
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingNumber
- **Type**: <class 'str'>
- **Required**: Yes

### LogBucket
- **Type**: <class 'str'>
- **Required**: Yes

### LogKey
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCount
- **Type**: <class 'int'>
- **Required**: Yes

### Signature
- **Type**: <class 'str'>
- **Required**: Yes

### SignatureFileContents
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentManifest
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ArtifactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.importexport.importexport_classes.Artifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.importexport.importexport_classes.ResponseMetadata'>
- **Required**: Yes


# Job

### JobId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### IsCanceled
- **Type**: typing.Optional[bool]

### JobType
- **Type**: typing.Optional[typing.Literal['Export', 'Import']]


# ListJobsInput

### MaxJobs
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### APIVersion
- **Type**: typing.Optional[str]


# ListJobsInputPaginate

### APIVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.importexport.importexport_classes.PaginatorConfig]


# ListJobsOutput

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.importexport.importexport_classes.Job]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.importexport.importexport_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# UpdateJobInput

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Manifest
- **Type**: <class 'str'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['Export', 'Import']
- **Required**: Yes

### ValidateOnly
- **Type**: <class 'bool'>
- **Required**: Yes

### APIVersion
- **Type**: typing.Optional[str]


# UpdateJobOutput

### Success
- **Type**: <class 'bool'>
- **Required**: Yes

### WarningMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.importexport.importexport_classes.Artifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.importexport.importexport_classes.ResponseMetadata'>
- **Required**: Yes


