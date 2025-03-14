# Glacier Classes

# AbortMultipartUploadInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# AbortVaultLockInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# AddTagsToVaultInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ArchiveCreationOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CSVInputTypeDef

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


# CSVOutputTypeDef

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


# CompleteMultipartUploadInputMultipartUploadCompleteTypeDef

### archiveSize
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]


# CompleteMultipartUploadInputTypeDef

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


# CompleteVaultLockInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### lockId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# CreateVaultInputAccountCreateVaultTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateVaultInputServiceResourceCreateVaultTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# CreateVaultInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# CreateVaultOutputTypeDef

### location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataRetrievalPolicyOutputTypeDef

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glacier_classes.DataRetrievalRuleTypeDef]]


# DataRetrievalPolicyTypeDef

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glacier_classes.DataRetrievalRuleTypeDef]]


# DataRetrievalPolicyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataRetrievalRuleTypeDef

### Strategy
- **Type**: typing.Optional[str]

### BytesPerHour
- **Type**: typing.Optional[int]


# DeleteArchiveInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### archiveId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DeleteVaultAccessPolicyInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DeleteVaultInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DeleteVaultNotificationsInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DescribeJobInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DescribeVaultInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# DescribeVaultInputWaitExtraTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.WaiterConfigTypeDef]


# DescribeVaultInputWaitTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.WaiterConfigTypeDef]


# DescribeVaultOutputTypeDef

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


# DescribeVaultResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionTypeDef

### EncryptionType
- **Type**: typing.Optional[typing.Literal['AES256', 'aws:kms']]

### KMSKeyId
- **Type**: typing.Optional[str]

### KMSContext
- **Type**: typing.Optional[str]


# GetDataRetrievalPolicyInputTypeDef

### accountId
- **Type**: typing.Optional[str]


# GetDataRetrievalPolicyOutputTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.DataRetrievalPolicyOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobOutputOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVaultAccessPolicyInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# GetVaultAccessPolicyOutputTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.VaultAccessPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVaultLockInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# GetVaultLockOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVaultNotificationsInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# GetVaultNotificationsOutputTypeDef

### vaultNotificationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.VaultNotificationConfigOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlacierJobDescriptionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.InventoryRetrievalJobDescriptionTypeDef'>
- **Required**: Yes

### JobOutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### SelectParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.SelectParametersTypeDef'>
- **Required**: Yes

### OutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.OutputLocationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlacierJobDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.InventoryRetrievalJobDescriptionTypeDef]

### JobOutputPath
- **Type**: typing.Optional[str]

### SelectParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.SelectParametersTypeDef]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.OutputLocationOutputTypeDef]


# GrantTypeDef

### Grantee
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.GranteeTypeDef]

### Permission
- **Type**: typing.Optional[typing.Literal['FULL_CONTROL', 'READ', 'READ_ACP', 'WRITE', 'WRITE_ACP']]


# GranteeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InitiateJobInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### jobParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.JobParametersTypeDef]


# InitiateJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InitiateMultipartUploadInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### archiveDescription
- **Type**: typing.Optional[str]

### partSize
- **Type**: typing.Optional[str]


# InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef

### archiveDescription
- **Type**: typing.Optional[str]

### partSize
- **Type**: typing.Optional[str]


# InitiateMultipartUploadOutputTypeDef

### location
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InitiateVaultLockInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.VaultLockPolicyTypeDef]


# InitiateVaultLockOutputTypeDef

### lockId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputSerializationTypeDef

### csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.CSVInputTypeDef]


# InventoryRetrievalJobDescriptionTypeDef

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


# InventoryRetrievalJobInputTypeDef

### StartDate
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]


# JobParametersTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListJobsInputPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.PaginatorConfigTypeDef]


# ListJobsInputTypeDef

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


# ListJobsOutputTypeDef

### JobList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glacier_classes.GlacierJobDescriptionTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMultipartUploadsInputPaginateTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.PaginatorConfigTypeDef]


# ListMultipartUploadsInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### marker
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[str]


# ListMultipartUploadsOutputTypeDef

### UploadsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glacier_classes.UploadListElementTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPartsInputMultipartUploadPartsTypeDef

### marker
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[str]


# ListPartsInputPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.PaginatorConfigTypeDef]


# ListPartsInputTypeDef

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


# ListPartsOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.glacier_classes.PartListElementTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProvisionedCapacityInputTypeDef

### accountId
- **Type**: typing.Optional[str]


# ListProvisionedCapacityOutputTypeDef

### ProvisionedCapacityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glacier_classes.ProvisionedCapacityDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForVaultInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]


# ListTagsForVaultOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVaultsInputPaginateTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.PaginatorConfigTypeDef]


# ListVaultsInputTypeDef

### accountId
- **Type**: typing.Optional[str]

### marker
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[str]


# ListVaultsOutputTypeDef

### VaultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.glacier_classes.DescribeVaultOutputTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OutputLocationOutputTypeDef

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.S3LocationOutputTypeDef]


# OutputLocationTypeDef

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.S3LocationUnionTypeDef]


# OutputSerializationTypeDef

### csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.CSVOutputTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartListElementTypeDef

### RangeInBytes
- **Type**: typing.Optional[str]

### SHA256TreeHash
- **Type**: typing.Optional[str]


# ProvisionedCapacityDescriptionTypeDef

### CapacityId
- **Type**: typing.Optional[str]

### StartDate
- **Type**: typing.Optional[str]

### ExpirationDate
- **Type**: typing.Optional[str]


# PurchaseProvisionedCapacityInputTypeDef

### accountId
- **Type**: typing.Optional[str]


# PurchaseProvisionedCapacityOutputTypeDef

### capacityId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveTagsFromVaultInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]


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


# S3LocationOutputTypeDef

### BucketName
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.EncryptionTypeDef]

### CannedACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### AccessControlList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.glacier_classes.GrantTypeDef]]

### Tagging
- **Type**: typing.Optional[typing.Dict[str, str]]

### UserMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### StorageClass
- **Type**: typing.Optional[typing.Literal['REDUCED_REDUNDANCY', 'STANDARD', 'STANDARD_IA']]


# S3LocationTypeDef

### BucketName
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.EncryptionTypeDef]

### CannedACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### AccessControlList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.glacier_classes.GrantTypeDef]]

### Tagging
- **Type**: typing.Optional[typing.Mapping[str, str]]

### UserMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### StorageClass
- **Type**: typing.Optional[typing.Literal['REDUCED_REDUNDANCY', 'STANDARD', 'STANDARD_IA']]


# S3LocationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SelectParametersTypeDef

### InputSerialization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.InputSerializationTypeDef]

### ExpressionType
- **Type**: typing.Optional[typing.Literal['SQL']]

### Expression
- **Type**: typing.Optional[str]

### OutputSerialization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.OutputSerializationTypeDef]


# SetDataRetrievalPolicyInputTypeDef

### accountId
- **Type**: typing.Optional[str]

### Policy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.DataRetrievalPolicyUnionTypeDef]


# SetVaultAccessPolicyInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.VaultAccessPolicyTypeDef]


# SetVaultNotificationsInputNotificationSetTypeDef

### vaultNotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.VaultNotificationConfigUnionTypeDef]


# SetVaultNotificationsInputTypeDef

### vaultName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### vaultNotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.VaultNotificationConfigUnionTypeDef]


# UploadArchiveInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.BlobTypeDef]


# UploadArchiveInputVaultUploadArchiveTypeDef

### archiveDescription
- **Type**: typing.Optional[str]

### checksum
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.glacier_classes.BlobTypeDef]


# UploadListElementTypeDef

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


# UploadMultipartPartOutputTypeDef

### checksum
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.glacier_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VaultAccessPolicyTypeDef

### Policy
- **Type**: typing.Optional[str]


# VaultLockPolicyTypeDef

### Policy
- **Type**: typing.Optional[str]


# VaultNotificationConfigOutputTypeDef

### SNSTopic
- **Type**: typing.Optional[str]

### Events
- **Type**: typing.Optional[typing.List[str]]


# VaultNotificationConfigTypeDef

### SNSTopic
- **Type**: typing.Optional[str]

### Events
- **Type**: typing.Optional[typing.Sequence[str]]


# VaultNotificationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


