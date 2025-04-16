# Dynamodbstreams Classes

# AttributeValue

### S
- **Type**: typing.Optional[str]

### N
- **Type**: typing.Optional[str]

### B
- **Type**: typing.Optional[bytes]

### SS
- **Type**: typing.Optional[typing.List[str]]

### NS
- **Type**: typing.Optional[typing.List[str]]

### BS
- **Type**: typing.Optional[typing.List[bytes]]

### M
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### L
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### NULL
- **Type**: typing.Optional[bool]

### BOOL
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DescribeStreamInput

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]


# DescribeStreamOutput

### StreamDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.dynamodbstreams_classes.StreamDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dynamodbstreams_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecordsInput

### ShardIterator
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]


# GetRecordsOutput

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.dynamodbstreams_classes.Record]
- **Required**: Yes

### NextShardIterator
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dynamodbstreams_classes.ResponseMetadata'>
- **Required**: Yes


# GetShardIteratorInput

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### ShardId
- **Type**: <class 'str'>
- **Required**: Yes

### ShardIteratorType
- **Type**: typing.Literal['AFTER_SEQUENCE_NUMBER', 'AT_SEQUENCE_NUMBER', 'LATEST', 'TRIM_HORIZON']
- **Required**: Yes

### SequenceNumber
- **Type**: typing.Optional[str]


# GetShardIteratorOutput

### ShardIterator
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dynamodbstreams_classes.ResponseMetadata'>
- **Required**: Yes


# Identity

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KeySchemaElement

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### KeyType
- **Type**: typing.Literal['HASH', 'RANGE']
- **Required**: Yes


# ListStreamsInput

### TableName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartStreamArn
- **Type**: typing.Optional[str]


# ListStreamsOutput

### Streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.dynamodbstreams_classes.Stream]
- **Required**: Yes

### LastEvaluatedStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dynamodbstreams_classes.ResponseMetadata'>
- **Required**: Yes


# Record

### eventID
- **Type**: typing.Optional[str]

### eventName
- **Type**: typing.Optional[typing.Literal['INSERT', 'MODIFY', 'REMOVE']]

### eventVersion
- **Type**: typing.Optional[str]

### eventSource
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]

### dynamodb
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dynamodbstreams_classes.StreamRecord]

### userIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dynamodbstreams_classes.Identity]


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


# SequenceNumberRange

### StartingSequenceNumber
- **Type**: typing.Optional[str]

### EndingSequenceNumber
- **Type**: typing.Optional[str]


# Shard

### ShardId
- **Type**: typing.Optional[str]

### SequenceNumberRange
- **Type**: <class 'NoneType'>

### ParentShardId
- **Type**: typing.Optional[str]


# Stream

### StreamArn
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### StreamLabel
- **Type**: typing.Optional[str]


# StreamDescription

### StreamArn
- **Type**: typing.Optional[str]

### StreamLabel
- **Type**: typing.Optional[str]

### StreamStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING']]

### StreamViewType
- **Type**: typing.Optional[typing.Literal['KEYS_ONLY', 'NEW_AND_OLD_IMAGES', 'NEW_IMAGE', 'OLD_IMAGE']]

### CreationRequestDateTime
- **Type**: typing.Optional[datetime.datetime]

### TableName
- **Type**: typing.Optional[str]

### KeySchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dynamodbstreams_classes.KeySchemaElement]]

### Shards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dynamodbstreams_classes.Shard]]

### LastEvaluatedShardId
- **Type**: typing.Optional[str]


# StreamRecord

### ApproximateCreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### Keys
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.dynamodbstreams_classes.AttributeValue]]

### NewImage
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.dynamodbstreams_classes.AttributeValue]]

### OldImage
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.dynamodbstreams_classes.AttributeValue]]

### SequenceNumber
- **Type**: typing.Optional[str]

### SizeBytes
- **Type**: typing.Optional[int]

### StreamViewType
- **Type**: typing.Optional[typing.Literal['KEYS_ONLY', 'NEW_AND_OLD_IMAGES', 'NEW_IMAGE', 'OLD_IMAGE']]


