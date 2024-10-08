# Pydantic Models in qldb_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJournalKinesisStreamRequestRequestTypeDef

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJournalKinesisStreamResponseTypeDef

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLedgerRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsMode
- **Type**: typing.Literal['ALLOW_ALL', 'STANDARD']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### KmsKey
- **Type**: typing.Optional[str]


# CreateLedgerResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PermissionsMode
- **Type**: typing.Literal['ALLOW_ALL', 'STANDARD']
- **Required**: Yes

### DeletionProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLedgerRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJournalKinesisStreamRequestRequestTypeDef

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJournalKinesisStreamResponseTypeDef

### Stream
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.JournalKinesisStreamDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJournalS3ExportRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJournalS3ExportResponseTypeDef

### ExportDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.JournalS3ExportDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLedgerRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLedgerResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PermissionsMode
- **Type**: typing.Literal['ALLOW_ALL', 'STANDARD']
- **Required**: Yes

### DeletionProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### EncryptionDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.LedgerEncryptionDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportJournalToS3RequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InclusiveStartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ExclusiveEndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### S3ExportConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.S3ExportConfigurationTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Optional[typing.Literal['ION_BINARY', 'ION_TEXT', 'JSON']]


# ExportJournalToS3ResponseTypeDef

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBlockRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BlockAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ValueHolderTypeDef'>
- **Required**: Yes

### DigestTipAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_classes.ValueHolderTypeDef]


# GetBlockResponseTypeDef

### Block
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ValueHolderTypeDef'>
- **Required**: Yes

### Proof
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ValueHolderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDigestRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDigestResponseTypeDef

### Digest
- **Type**: <class 'bytes'>
- **Required**: Yes

### DigestTipAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ValueHolderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRevisionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BlockAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ValueHolderTypeDef'>
- **Required**: Yes

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### DigestTipAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb_classes.ValueHolderTypeDef]


# GetRevisionResponseTypeDef

### Proof
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ValueHolderTypeDef'>
- **Required**: Yes

### Revision
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ValueHolderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# JournalKinesisStreamDescriptionTypeDef

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CANCELED', 'COMPLETED', 'FAILED', 'IMPAIRED']
- **Required**: Yes

### KinesisConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.KinesisConfigurationTypeDef'>
- **Required**: Yes

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### InclusiveStartTime
- **Type**: typing.Optional[datetime.datetime]

### ExclusiveEndTime
- **Type**: typing.Optional[datetime.datetime]

### Arn
- **Type**: typing.Optional[str]

### ErrorCause
- **Type**: typing.Optional[typing.Literal['IAM_PERMISSION_REVOKED', 'KINESIS_STREAM_NOT_FOUND']]


# JournalS3ExportDescriptionTypeDef

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportCreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'IN_PROGRESS']
- **Required**: Yes

### InclusiveStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExclusiveEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### S3ExportConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.S3ExportConfigurationTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Optional[typing.Literal['ION_BINARY', 'ION_TEXT', 'JSON']]


# KinesisConfigurationTypeDef

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### AggregationEnabled
- **Type**: typing.Optional[bool]


# LedgerEncryptionDescriptionTypeDef

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionStatus
- **Type**: typing.Literal['ENABLED', 'KMS_KEY_INACCESSIBLE', 'UPDATING']
- **Required**: Yes

### InaccessibleKmsKeyDateTime
- **Type**: typing.Optional[datetime.datetime]


# LedgerSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING']]

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]


# ListJournalKinesisStreamsForLedgerRequestRequestTypeDef

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListJournalKinesisStreamsForLedgerResponseTypeDef

### Streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.qldb_classes.JournalKinesisStreamDescriptionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJournalS3ExportsForLedgerRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListJournalS3ExportsForLedgerResponseTypeDef

### JournalS3Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.qldb_classes.JournalS3ExportDescriptionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJournalS3ExportsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListJournalS3ExportsResponseTypeDef

### JournalS3Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.qldb_classes.JournalS3ExportDescriptionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLedgersRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLedgersResponseTypeDef

### Ledgers
- **Type**: typing.List[aws_resource_validator.pydantic_models.qldb_classes.LedgerSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# S3EncryptionConfigurationTypeDef

### ObjectEncryptionType
- **Type**: typing.Literal['NO_ENCRYPTION', 'SSE_KMS', 'SSE_S3']
- **Required**: Yes

### KmsKeyArn
- **Type**: typing.Optional[str]


# S3ExportConfigurationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.S3EncryptionConfigurationTypeDef'>
- **Required**: Yes


# StreamJournalToKinesisRequestRequestTypeDef

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InclusiveStartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KinesisConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.KinesisConfigurationTypeDef'>
- **Required**: Yes

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ExclusiveEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# StreamJournalToKinesisResponseTypeDef

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLedgerPermissionsModeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsMode
- **Type**: typing.Literal['ALLOW_ALL', 'STANDARD']
- **Required**: Yes


# UpdateLedgerPermissionsModeResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsMode
- **Type**: typing.Literal['ALLOW_ALL', 'STANDARD']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLedgerRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtection
- **Type**: typing.Optional[bool]

### KmsKey
- **Type**: typing.Optional[str]


# UpdateLedgerResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING']
- **Required**: Yes

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeletionProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### EncryptionDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.LedgerEncryptionDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValueHolderTypeDef

### IonText
- **Type**: typing.Optional[str]


