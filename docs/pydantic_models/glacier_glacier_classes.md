# Glacier Glacier Classes

# AbortMultipartUploadInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# AbortVaultLockInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# AddTagsToVaultInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ArchiveCreationOutput

### location
- **Type**: <class 'str'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### archiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CSVInput

### FileHeaderInfo
- **Type**: typing.Optional[typing.Literal['IGNORE', 'NONE', 'USE']]

### Comments
- **Type**: typing.Optional[str]

### QuoteEscapeCharacter
- **Type**: typing.Optional[str]

### RecordDelimiter
- **Type**: typing.Optional[str]

### FieldDelimiter
- **Type**: typing.Optional[str]

### QuoteCharacter
- **Type**: typing.Optional[str]


# CSVOutput

### QuoteFields
- **Type**: typing.Optional[typing.Literal['ALWAYS', 'ASNEEDED']]

### QuoteEscapeCharacter
- **Type**: typing.Optional[str]

### RecordDelimiter
- **Type**: typing.Optional[str]

### FieldDelimiter
- **Type**: typing.Optional[str]

### QuoteCharacter
- **Type**: typing.Optional[str]


# CompleteMultipartUploadInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### archiveSize
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]


# CompleteMultipartUploadInputMultipartUploadComplete

### archiveSize
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]


# CompleteVaultLockInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### lockId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# CreateVaultInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# CreateVaultInputAccountCreateVault

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateVaultInputServiceResourceCreateVault

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# CreateVaultOutput

### location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# DataRetrievalPolicy

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glacier.glacier_classes.DataRetrievalRule]]


# DataRetrievalPolicyOutput

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glacier.glacier_classes.DataRetrievalRule]]


# DataRetrievalRule

### Strategy
- **Type**: typing.Optional[str]

### BytesPerHour
- **Type**: typing.Optional[int]


# DeleteArchiveInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### archiveId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DeleteVaultAccessPolicyInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DeleteVaultInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DeleteVaultNotificationsInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DescribeJobInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DescribeVaultInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DescribeVaultInputWait

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeVaultInputWaitExtra

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeVaultOutput

### VaultARN
- **Type**: typing.Optional[str]

### VaultName
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### LastInventoryDate
- **Type**: typing.Optional[str]

### NumberOfArchives
- **Type**: typing.Optional[int]

### SizeInBytes
- **Type**: typing.Optional[int]


# DescribeVaultResponse

### VaultARN
- **Type**: <class 'str'>
- **Required**: Yes

### VaultName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### LastInventoryDate
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfArchives
- **Type**: <class 'int'>
- **Required**: Yes

### SizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# Encryption

### EncryptionType
- **Type**: typing.Optional[typing.Literal['AES256', 'aws:kms']]

### KMSKeyId
- **Type**: typing.Optional[str]

### KMSContext
- **Type**: typing.Optional[str]


# GetDataRetrievalPolicyInput

### accountId
- **Type**: typing.Optional[str]


# GetDataRetrievalPolicyOutput

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.DataRetrievalPolicyOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobOutputInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### range
- **Type**: typing.Optional[str]


# GetJobOutputInputJobGetOutput

### range
- **Type**: typing.Optional[str]


# GetJobOutputOutput

### body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'int'>
- **Required**: Yes

### contentRange
- **Type**: <class 'str'>
- **Required**: Yes

### acceptRanges
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### archiveDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# GetVaultAccessPolicyInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# GetVaultAccessPolicyOutput

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.VaultAccessPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# GetVaultLockInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# GetVaultLockOutput

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationDate
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# GetVaultNotificationsInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# GetVaultNotificationsOutput

### vaultNotificationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.VaultNotificationConfigOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# GlacierJobDescription

### JobId
- **Type**: typing.Optional[str]

### JobDescription
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[typing.Literal['ArchiveRetrieval', 'InventoryRetrieval', 'Select']]

### ArchiveId
- **Type**: typing.Optional[str]

### VaultARN
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### Completed
- **Type**: typing.Optional[bool]

### StatusCode
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Succeeded']]

### StatusMessage
- **Type**: typing.Optional[str]

### ArchiveSizeInBytes
- **Type**: typing.Optional[int]

### InventorySizeInBytes
- **Type**: typing.Optional[int]

### SNSTopic
- **Type**: typing.Optional[str]

### CompletionDate
- **Type**: typing.Optional[str]

### SHA256TreeHash
- **Type**: typing.Optional[str]

### ArchiveSHA256TreeHash
- **Type**: typing.Optional[str]

### RetrievalByteRange
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[str]

### InventoryRetrievalParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.InventoryRetrievalJobDescription]

### JobOutputPath
- **Type**: typing.Optional[str]

### SelectParameters
- **Type**: <class 'NoneType'>

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.OutputLocationOutput]


# GlacierJobDescriptionResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['ArchiveRetrieval', 'InventoryRetrieval', 'Select']
- **Required**: Yes

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### VaultARN
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### Completed
- **Type**: <class 'bool'>
- **Required**: Yes

### StatusCode
- **Type**: typing.Literal['Failed', 'InProgress', 'Succeeded']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### InventorySizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### SNSTopic
- **Type**: <class 'str'>
- **Required**: Yes

### CompletionDate
- **Type**: <class 'str'>
- **Required**: Yes

### SHA256TreeHash
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveSHA256TreeHash
- **Type**: <class 'str'>
- **Required**: Yes

### RetrievalByteRange
- **Type**: <class 'str'>
- **Required**: Yes

### Tier
- **Type**: <class 'str'>
- **Required**: Yes

### InventoryRetrievalParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.InventoryRetrievalJobDescription'>
- **Required**: Yes

### JobOutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### SelectParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.SelectParameters'>
- **Required**: Yes

### OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.OutputLocationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# Grant

### Grantee
- **Type**: <class 'NoneType'>

### Permission
- **Type**: typing.Optional[typing.Literal['FULL_CONTROL', 'READ', 'READ_ACP', 'WRITE', 'WRITE_ACP']]


# Grantee

### Type
- **Type**: typing.Literal['AmazonCustomerByEmail', 'CanonicalUser', 'Group']
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### URI
- **Type**: typing.Optional[str]

### ID
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]


# InitiateJobInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### jobParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.JobParameters]


# InitiateJobOutput

### location
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobOutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# InitiateMultipartUploadInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### archiveDescription
- **Type**: typing.Optional[str]

### partSize
- **Type**: typing.Optional[str]


# InitiateMultipartUploadInputVaultInitiateMultipartUpload

### archiveDescription
- **Type**: typing.Optional[str]

### partSize
- **Type**: typing.Optional[str]


# InitiateMultipartUploadOutput

### location
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# InitiateVaultLockInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.VaultLockPolicy]


# InitiateVaultLockOutput

### lockId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# InputSerialization

### csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.CSVInput]


# InventoryRetrievalJobDescription

### Format
- **Type**: typing.Optional[str]

### StartDate
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]


# InventoryRetrievalJobInput

### StartDate
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]


# JobParameters

### Format
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### ArchiveId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SNSTopic
- **Type**: typing.Optional[str]

### RetrievalByteRange
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[str]

### InventoryRetrievalParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.InventoryRetrievalJobInput]

### SelectParameters
- **Type**: <class 'NoneType'>

### OutputLocation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glacier.glacier_classes.OutputLocation, aws_resource_validator.pydantic_models.glacier.glacier_classes.OutputLocationOutput, NoneType]


# ListJobsInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[str]

### marker
- **Type**: typing.Optional[str]

### statuscode
- **Type**: typing.Optional[str]

### completed
- **Type**: typing.Optional[str]


# ListJobsInputPaginate

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### statuscode
- **Type**: typing.Optional[str]

### completed
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.PaginatorConfig]


# ListJobsOutput

### JobList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glacier.glacier_classes.GlacierJobDescription]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# ListMultipartUploadsInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### marker
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[str]


# ListMultipartUploadsInputPaginate

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.PaginatorConfig]


# ListMultipartUploadsOutput

### UploadsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glacier.glacier_classes.UploadListElement]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# ListPartsInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### marker
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[str]


# ListPartsInputMultipartUploadParts

### marker
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[str]


# ListPartsInputPaginate

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.PaginatorConfig]


# ListPartsOutput

### MultipartUploadId
- **Type**: <class 'str'>
- **Required**: Yes

### VaultARN
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveDescription
- **Type**: <class 'str'>
- **Required**: Yes

### PartSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### Parts
- **Type**: typing.List[aws_resource_validator.pydantic_models.glacier.glacier_classes.PartListElement]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# ListProvisionedCapacityInput

### accountId
- **Type**: typing.Optional[str]


# ListProvisionedCapacityOutput

### ProvisionedCapacityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glacier.glacier_classes.ProvisionedCapacityDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForVaultInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# ListTagsForVaultOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# ListVaultsInput

### accountId
- **Type**: typing.Optional[str]

### marker
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[str]


# ListVaultsInputPaginate

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.PaginatorConfig]


# ListVaultsOutput

### VaultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glacier.glacier_classes.DescribeVaultOutput]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# OutputLocation

### S3
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glacier.glacier_classes.S3Location, aws_resource_validator.pydantic_models.glacier.glacier_classes.S3LocationOutput, NoneType]


# OutputLocationOutput

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.S3LocationOutput]


# OutputSerialization

### csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.CSVOutput]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartListElement

### RangeInBytes
- **Type**: typing.Optional[str]

### SHA256TreeHash
- **Type**: typing.Optional[str]


# ProvisionedCapacityDescription

### CapacityId
- **Type**: typing.Optional[str]

### StartDate
- **Type**: typing.Optional[str]

### ExpirationDate
- **Type**: typing.Optional[str]


# PurchaseProvisionedCapacityInput

### accountId
- **Type**: typing.Optional[str]


# PurchaseProvisionedCapacityOutput

### capacityId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsFromVaultInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]


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


# S3Location

### BucketName
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### Encryption
- **Type**: <class 'NoneType'>

### CannedACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### AccessControlList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glacier.glacier_classes.Grant]]

### Tagging
- **Type**: typing.Optional[typing.Dict[str, str]]

### UserMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### StorageClass
- **Type**: typing.Optional[typing.Literal['REDUCED_REDUNDANCY', 'STANDARD', 'STANDARD_IA']]


# S3LocationOutput

### BucketName
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### Encryption
- **Type**: <class 'NoneType'>

### CannedACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### AccessControlList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glacier.glacier_classes.Grant]]

### Tagging
- **Type**: typing.Optional[typing.Dict[str, str]]

### UserMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### StorageClass
- **Type**: typing.Optional[typing.Literal['REDUCED_REDUNDANCY', 'STANDARD', 'STANDARD_IA']]


# SelectParameters

### InputSerialization
- **Type**: <class 'NoneType'>

### ExpressionType
- **Type**: typing.Optional[typing.Literal['SQL']]

### Expression
- **Type**: typing.Optional[str]

### OutputSerialization
- **Type**: <class 'NoneType'>


# SetDataRetrievalPolicyInput

### accountId
- **Type**: typing.Optional[str]

### Policy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glacier.glacier_classes.DataRetrievalPolicy, aws_resource_validator.pydantic_models.glacier.glacier_classes.DataRetrievalPolicyOutput, NoneType]


# SetVaultAccessPolicyInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier.glacier_classes.VaultAccessPolicy]


# SetVaultNotificationsInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### vaultNotificationConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glacier.glacier_classes.VaultNotificationConfig, aws_resource_validator.pydantic_models.glacier.glacier_classes.VaultNotificationConfigOutput, NoneType]


# SetVaultNotificationsInputNotificationSet

### vaultNotificationConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.glacier.glacier_classes.VaultNotificationConfig, aws_resource_validator.pydantic_models.glacier.glacier_classes.VaultNotificationConfigOutput, NoneType]


# UploadArchiveInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### archiveDescription
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# UploadArchiveInputVaultUploadArchive

### archiveDescription
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# UploadListElement

### MultipartUploadId
- **Type**: typing.Optional[str]

### VaultARN
- **Type**: typing.Optional[str]

### ArchiveDescription
- **Type**: typing.Optional[str]

### PartSizeInBytes
- **Type**: typing.Optional[int]

### CreationDate
- **Type**: typing.Optional[str]


# UploadMultipartPartInput

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]

### range
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# UploadMultipartPartInputMultipartUploadUploadPart

### checksum
- **Type**: typing.Optional[str]

### range
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# UploadMultipartPartOutput

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier.glacier_classes.ResponseMetadata'>
- **Required**: Yes


# VaultAccessPolicy

### Policy
- **Type**: typing.Optional[str]


# VaultLockPolicy

### Policy
- **Type**: typing.Optional[str]


# VaultNotificationConfig

### SNSTopic
- **Type**: typing.Optional[str]

### Events
- **Type**: typing.Optional[typing.List[str]]


# VaultNotificationConfigOutput

### SNSTopic
- **Type**: typing.Optional[str]

### Events
- **Type**: typing.Optional[typing.List[str]]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


