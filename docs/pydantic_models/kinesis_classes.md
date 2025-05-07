# Kinesis Classes

# AddTagsToStreamInput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChildShard

### ShardId
- **Type**: <class 'str'>
- **Required**: Yes

### ParentShards
- **Type**: typing.List[str]
- **Required**: Yes

### HashKeyRange
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.HashKeyRange'>
- **Required**: Yes


# Consumer

### ConsumerName
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerARN
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING']
- **Required**: Yes

### ConsumerCreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ConsumerDescription

### ConsumerName
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerARN
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING']
- **Required**: Yes

### ConsumerCreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes


# CreateStreamInput

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### ShardCount
- **Type**: typing.Optional[int]

### StreamModeDetails
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DecreaseStreamRetentionPeriodInput

### RetentionPeriodHours
- **Type**: <class 'int'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DeleteResourcePolicyInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStreamInput

### StreamName
- **Type**: typing.Optional[str]

### EnforceConsumerDeletion
- **Type**: typing.Optional[bool]

### StreamARN
- **Type**: typing.Optional[str]


# DeregisterStreamConsumerInput

### StreamARN
- **Type**: typing.Optional[str]

### ConsumerName
- **Type**: typing.Optional[str]

### ConsumerARN
- **Type**: typing.Optional[str]


# DescribeLimitsOutput

### ShardLimit
- **Type**: <class 'int'>
- **Required**: Yes

### OpenShardCount
- **Type**: <class 'int'>
- **Required**: Yes

### OnDemandStreamCount
- **Type**: <class 'int'>
- **Required**: Yes

### OnDemandStreamCountLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStreamConsumerInput

### StreamARN
- **Type**: typing.Optional[str]

### ConsumerName
- **Type**: typing.Optional[str]

### ConsumerARN
- **Type**: typing.Optional[str]


# DescribeStreamConsumerOutput

### ConsumerDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ConsumerDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStreamInput

### StreamName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeStreamInputPaginate

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.PaginatorConfig]


# DescribeStreamInputWait

### StreamName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStreamInputWaitExtra

### StreamName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStreamOutput

### StreamDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.StreamDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStreamSummaryInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeStreamSummaryOutput

### StreamDescriptionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.StreamDescriptionSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# DisableEnhancedMonitoringInput

### ShardLevelMetrics
- **Type**: typing.List[typing.Literal['ALL', 'IncomingBytes', 'IncomingRecords', 'IteratorAgeMilliseconds', 'OutgoingBytes', 'OutgoingRecords', 'ReadProvisionedThroughputExceeded', 'WriteProvisionedThroughputExceeded']]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# EnableEnhancedMonitoringInput

### ShardLevelMetrics
- **Type**: typing.List[typing.Literal['ALL', 'IncomingBytes', 'IncomingRecords', 'IteratorAgeMilliseconds', 'OutgoingBytes', 'OutgoingRecords', 'ReadProvisionedThroughputExceeded', 'WriteProvisionedThroughputExceeded']]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# EnhancedMetrics

### ShardLevelMetrics
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'IncomingBytes', 'IncomingRecords', 'IteratorAgeMilliseconds', 'OutgoingBytes', 'OutgoingRecords', 'ReadProvisionedThroughputExceeded', 'WriteProvisionedThroughputExceeded']]]


# EnhancedMonitoringOutput

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentShardLevelMetrics
- **Type**: typing.List[typing.Literal['ALL', 'IncomingBytes', 'IncomingRecords', 'IteratorAgeMilliseconds', 'OutgoingBytes', 'OutgoingRecords', 'ReadProvisionedThroughputExceeded', 'WriteProvisionedThroughputExceeded']]
- **Required**: Yes

### DesiredShardLevelMetrics
- **Type**: typing.List[typing.Literal['ALL', 'IncomingBytes', 'IncomingRecords', 'IteratorAgeMilliseconds', 'OutgoingBytes', 'OutgoingRecords', 'ReadProvisionedThroughputExceeded', 'WriteProvisionedThroughputExceeded']]
- **Required**: Yes

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecordsInput

### ShardIterator
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### StreamARN
- **Type**: typing.Optional[str]


# GetRecordsOutput

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.Record]
- **Required**: Yes

### NextShardIterator
- **Type**: <class 'str'>
- **Required**: Yes

### MillisBehindLatest
- **Type**: <class 'int'>
- **Required**: Yes

### ChildShards
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ChildShard]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePolicyInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyOutput

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# GetShardIteratorInput

### ShardId
- **Type**: <class 'str'>
- **Required**: Yes

### ShardIteratorType
- **Type**: typing.Literal['AFTER_SEQUENCE_NUMBER', 'AT_SEQUENCE_NUMBER', 'AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StartingSequenceNumber
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: <class 'NoneType'>

### StreamARN
- **Type**: typing.Optional[str]


# GetShardIteratorOutput

### ShardIterator
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# HashKeyRange

### StartingHashKey
- **Type**: <class 'str'>
- **Required**: Yes

### EndingHashKey
- **Type**: <class 'str'>
- **Required**: Yes


# IncreaseStreamRetentionPeriodInput

### RetentionPeriodHours
- **Type**: <class 'int'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# InternalFailureException

### message
- **Type**: typing.Optional[str]


# KMSAccessDeniedException

### message
- **Type**: typing.Optional[str]


# KMSDisabledException

### message
- **Type**: typing.Optional[str]


# KMSInvalidStateException

### message
- **Type**: typing.Optional[str]


# KMSNotFoundException

### message
- **Type**: typing.Optional[str]


# KMSOptInRequired

### message
- **Type**: typing.Optional[str]


# KMSThrottlingException

### message
- **Type**: typing.Optional[str]


# ListShardsInput

### StreamName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StreamCreationTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ShardFilter
- **Type**: <class 'NoneType'>

### StreamARN
- **Type**: typing.Optional[str]


# ListShardsInputPaginate

### StreamName
- **Type**: typing.Optional[str]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]

### StreamCreationTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ShardFilter
- **Type**: <class 'NoneType'>

### StreamARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.PaginatorConfig]


# ListShardsOutput

### Shards
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.Shard]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamConsumersInput

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StreamCreationTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListStreamConsumersInputPaginate

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### StreamCreationTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.PaginatorConfig]


# ListStreamConsumersOutput

### Consumers
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.Consumer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamsInput

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartStreamName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListStreamsInputPaginate

### ExclusiveStartStreamName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.PaginatorConfig]


# ListStreamsOutput

### StreamNames
- **Type**: typing.List[str]
- **Required**: Yes

### HasMoreStreams
- **Type**: <class 'bool'>
- **Required**: Yes

### StreamSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.StreamSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForStreamInput

### StreamName
- **Type**: typing.Optional[str]

### ExclusiveStartTagKey
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### StreamARN
- **Type**: typing.Optional[str]


# ListTagsForStreamOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.Tag]
- **Required**: Yes

### HasMoreTags
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# MergeShardsInput

### ShardToMerge
- **Type**: <class 'str'>
- **Required**: Yes

### AdjacentShardToMerge
- **Type**: <class 'str'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutRecordInput

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### PartitionKey
- **Type**: <class 'str'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### ExplicitHashKey
- **Type**: typing.Optional[str]

### SequenceNumberForOrdering
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# PutRecordOutput

### ShardId
- **Type**: <class 'str'>
- **Required**: Yes

### SequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionType
- **Type**: typing.Literal['KMS', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# PutRecordsInput

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.PutRecordsRequestEntry]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# PutRecordsOutput

### FailedRecordCount
- **Type**: <class 'int'>
- **Required**: Yes

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.PutRecordsResultEntry]
- **Required**: Yes

### EncryptionType
- **Type**: typing.Literal['KMS', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# PutRecordsRequestEntry

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### PartitionKey
- **Type**: <class 'str'>
- **Required**: Yes

### ExplicitHashKey
- **Type**: typing.Optional[str]


# PutRecordsResultEntry

### SequenceNumber
- **Type**: typing.Optional[str]

### ShardId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# PutResourcePolicyInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# Record

### SequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: <class 'bytes'>
- **Required**: Yes

### PartitionKey
- **Type**: <class 'str'>
- **Required**: Yes

### ApproximateArrivalTimestamp
- **Type**: typing.Optional[datetime.datetime]

### EncryptionType
- **Type**: typing.Optional[typing.Literal['KMS', 'NONE']]


# RegisterStreamConsumerInput

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerName
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterStreamConsumerOutput

### Consumer
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.Consumer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsFromStreamInput

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# ResourceInUseException

### message
- **Type**: typing.Optional[str]


# ResourceNotFoundException

### message
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


# SequenceNumberRange

### StartingSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### EndingSequenceNumber
- **Type**: typing.Optional[str]


# Shard

### ShardId
- **Type**: <class 'str'>
- **Required**: Yes

### HashKeyRange
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.HashKeyRange'>
- **Required**: Yes

### SequenceNumberRange
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.SequenceNumberRange'>
- **Required**: Yes

### ParentShardId
- **Type**: typing.Optional[str]

### AdjacentParentShardId
- **Type**: typing.Optional[str]


# ShardFilter

### Type
- **Type**: typing.Literal['AFTER_SHARD_ID', 'AT_LATEST', 'AT_TIMESTAMP', 'AT_TRIM_HORIZON', 'FROM_TIMESTAMP', 'FROM_TRIM_HORIZON']
- **Required**: Yes

### ShardId
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: <class 'NoneType'>


# SplitShardInput

### ShardToSplit
- **Type**: <class 'str'>
- **Required**: Yes

### NewStartingHashKey
- **Type**: <class 'str'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# StartStreamEncryptionInput

### EncryptionType
- **Type**: typing.Literal['KMS', 'NONE']
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# StartingPosition

### Type
- **Type**: typing.Literal['AFTER_SEQUENCE_NUMBER', 'AT_SEQUENCE_NUMBER', 'AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']
- **Required**: Yes

### SequenceNumber
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: <class 'NoneType'>


# StopStreamEncryptionInput

### EncryptionType
- **Type**: typing.Literal['KMS', 'NONE']
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# StreamDescription

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### StreamStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'UPDATING']
- **Required**: Yes

### Shards
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.Shard]
- **Required**: Yes

### HasMoreShards
- **Type**: <class 'bool'>
- **Required**: Yes

### RetentionPeriodHours
- **Type**: <class 'int'>
- **Required**: Yes

### StreamCreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EnhancedMonitoring
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.EnhancedMetrics]
- **Required**: Yes

### StreamModeDetails
- **Type**: <class 'NoneType'>

### EncryptionType
- **Type**: typing.Optional[typing.Literal['KMS', 'NONE']]

### KeyId
- **Type**: typing.Optional[str]


# StreamDescriptionSummary

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### StreamStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'UPDATING']
- **Required**: Yes

### RetentionPeriodHours
- **Type**: <class 'int'>
- **Required**: Yes

### StreamCreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EnhancedMonitoring
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.EnhancedMetrics]
- **Required**: Yes

### OpenShardCount
- **Type**: <class 'int'>
- **Required**: Yes

### StreamModeDetails
- **Type**: <class 'NoneType'>

### EncryptionType
- **Type**: typing.Optional[typing.Literal['KMS', 'NONE']]

### KeyId
- **Type**: typing.Optional[str]

### ConsumerCount
- **Type**: typing.Optional[int]


# StreamModeDetails

### StreamMode
- **Type**: typing.Literal['ON_DEMAND', 'PROVISIONED']
- **Required**: Yes


# StreamSummary

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### StreamStatus
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'UPDATING']
- **Required**: Yes

### StreamModeDetails
- **Type**: <class 'NoneType'>

### StreamCreationTimestamp
- **Type**: typing.Optional[datetime.datetime]


# SubscribeToShardEvent

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.Record]
- **Required**: Yes

### ContinuationSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### MillisBehindLatest
- **Type**: <class 'int'>
- **Required**: Yes

### ChildShards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ChildShard]]


# SubscribeToShardEventStream

### SubscribeToShardEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.SubscribeToShardEvent'>
- **Required**: Yes

### ResourceNotFoundException
- **Type**: <class 'NoneType'>

### ResourceInUseException
- **Type**: <class 'NoneType'>

### KMSDisabledException
- **Type**: <class 'NoneType'>

### KMSInvalidStateException
- **Type**: <class 'NoneType'>

### KMSAccessDeniedException
- **Type**: <class 'NoneType'>

### KMSNotFoundException
- **Type**: <class 'NoneType'>

### KMSOptInRequired
- **Type**: <class 'NoneType'>

### KMSThrottlingException
- **Type**: <class 'NoneType'>

### InternalFailureException
- **Type**: <class 'NoneType'>


# SubscribeToShardInput

### ConsumerARN
- **Type**: <class 'str'>
- **Required**: Yes

### ShardId
- **Type**: <class 'str'>
- **Required**: Yes

### StartingPosition
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.StartingPosition'>
- **Required**: Yes


# SubscribeToShardOutput

### EventStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.kinesis.kinesis_classes.SubscribeToShardEventStream]
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# UpdateShardCountInput

### TargetShardCount
- **Type**: <class 'int'>
- **Required**: Yes

### ScalingType
- **Type**: typing.Literal['UNIFORM_SCALING']
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# UpdateShardCountOutput

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentShardCount
- **Type**: <class 'int'>
- **Required**: Yes

### TargetShardCount
- **Type**: <class 'int'>
- **Required**: Yes

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStreamModeInput

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### StreamModeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis.kinesis_classes.StreamModeDetails'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


