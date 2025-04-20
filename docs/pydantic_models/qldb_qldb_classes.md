# Qldb Qldb Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJournalKinesisStreamRequest

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJournalKinesisStreamResponse

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLedgerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsMode
- **Type**: typing.Literal['ALLOW_ALL', 'STANDARD']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### DeletionProtection
- **Type**: typing.Optional[bool]

### KmsKey
- **Type**: typing.Optional[str]


# CreateLedgerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLedgerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJournalKinesisStreamRequest

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJournalKinesisStreamResponse

### Stream
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.JournalKinesisStreamDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJournalS3ExportRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJournalS3ExportResponse

### ExportDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.JournalS3ExportDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLedgerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLedgerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.LedgerEncryptionDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# ExportJournalToS3Request

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.S3ExportConfiguration'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Optional[typing.Literal['ION_BINARY', 'ION_TEXT', 'JSON']]


# ExportJournalToS3Response

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# GetBlockRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BlockAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ValueHolder'>
- **Required**: Yes

### DigestTipAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb.qldb_classes.ValueHolder]


# GetBlockResponse

### Block
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ValueHolder'>
- **Required**: Yes

### Proof
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ValueHolder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# GetDigestRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDigestResponse

### Digest
- **Type**: <class 'bytes'>
- **Required**: Yes

### DigestTipAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ValueHolder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# GetRevisionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BlockAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ValueHolder'>
- **Required**: Yes

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### DigestTipAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qldb.qldb_classes.ValueHolder]


# GetRevisionResponse

### Proof
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ValueHolder'>
- **Required**: Yes

### Revision
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ValueHolder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# JournalKinesisStreamDescription

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.KinesisConfiguration'>
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


# JournalS3ExportDescription

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.S3ExportConfiguration'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Optional[typing.Literal['ION_BINARY', 'ION_TEXT', 'JSON']]


# KinesisConfiguration

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### AggregationEnabled
- **Type**: typing.Optional[bool]


# LedgerEncryptionDescription

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionStatus
- **Type**: typing.Literal['ENABLED', 'KMS_KEY_INACCESSIBLE', 'UPDATING']
- **Required**: Yes

### InaccessibleKmsKeyDateTime
- **Type**: typing.Optional[datetime.datetime]


# LedgerSummary

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING']]

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]


# ListJournalKinesisStreamsForLedgerRequest

### LedgerName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListJournalKinesisStreamsForLedgerResponse

### Streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.qldb.qldb_classes.JournalKinesisStreamDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJournalS3ExportsForLedgerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListJournalS3ExportsForLedgerResponse

### JournalS3Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.qldb.qldb_classes.JournalS3ExportDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJournalS3ExportsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListJournalS3ExportsResponse

### JournalS3Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.qldb.qldb_classes.JournalS3ExportDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLedgersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLedgersResponse

### Ledgers
- **Type**: typing.List[aws_resource_validator.pydantic_models.qldb.qldb_classes.LedgerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
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


# S3EncryptionConfiguration

### ObjectEncryptionType
- **Type**: typing.Literal['NO_ENCRYPTION', 'SSE_KMS', 'SSE_S3']
- **Required**: Yes

### KmsKeyArn
- **Type**: typing.Optional[str]


# S3ExportConfiguration

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.S3EncryptionConfiguration'>
- **Required**: Yes


# StreamJournalToKinesisRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.KinesisConfiguration'>
- **Required**: Yes

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ExclusiveEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# StreamJournalToKinesisResponse

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateLedgerPermissionsModeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsMode
- **Type**: typing.Literal['ALLOW_ALL', 'STANDARD']
- **Required**: Yes


# UpdateLedgerPermissionsModeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateLedgerRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtection
- **Type**: typing.Optional[bool]

### KmsKey
- **Type**: typing.Optional[str]


# UpdateLedgerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.LedgerEncryptionDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qldb.qldb_classes.ResponseMetadata'>
- **Required**: Yes


# ValueHolder

### IonText
- **Type**: typing.Optional[str]


