# Kinesis Classes

# AddTagsToStreamInputTypeDef

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChildShardTypeDef

### ShardId
- **Type**: <class 'str'>
- **Required**: Yes

### ParentShards
- **Type**: typing.List[str]
- **Required**: Yes

### HashKeyRange
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.HashKeyRangeTypeDef'>
- **Required**: Yes


# ConsumerDescriptionTypeDef

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


# ConsumerTypeDef

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


# CreateStreamInputTypeDef

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### ShardCount
- **Type**: typing.Optional[int]

### StreamModeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.StreamModeDetailsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DecreaseStreamRetentionPeriodInputTypeDef

### RetentionPeriodHours
- **Type**: <class 'int'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DeleteResourcePolicyInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStreamInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### EnforceConsumerDeletion
- **Type**: typing.Optional[bool]

### StreamARN
- **Type**: typing.Optional[str]


# DeregisterStreamConsumerInputTypeDef

### StreamARN
- **Type**: typing.Optional[str]

### ConsumerName
- **Type**: typing.Optional[str]

### ConsumerARN
- **Type**: typing.Optional[str]


# DescribeLimitsOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStreamConsumerInputTypeDef

### StreamARN
- **Type**: typing.Optional[str]

### ConsumerName
- **Type**: typing.Optional[str]

### ConsumerARN
- **Type**: typing.Optional[str]


# DescribeStreamConsumerOutputTypeDef

### ConsumerDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ConsumerDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStreamInputPaginateTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.PaginatorConfigTypeDef]


# DescribeStreamInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeStreamInputWaitExtraTypeDef

### StreamName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.WaiterConfigTypeDef]


# DescribeStreamInputWaitTypeDef

### StreamName
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.WaiterConfigTypeDef]


# DescribeStreamOutputTypeDef

### StreamDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.StreamDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStreamSummaryInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeStreamSummaryOutputTypeDef

### StreamDescriptionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.StreamDescriptionSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableEnhancedMonitoringInputTypeDef

### ShardLevelMetrics
- **Type**: typing.Sequence[typing.Literal['ALL', 'IncomingBytes', 'IncomingRecords', 'IteratorAgeMilliseconds', 'OutgoingBytes', 'OutgoingRecords', 'ReadProvisionedThroughputExceeded', 'WriteProvisionedThroughputExceeded']]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableEnhancedMonitoringInputTypeDef

### ShardLevelMetrics
- **Type**: typing.Sequence[typing.Literal['ALL', 'IncomingBytes', 'IncomingRecords', 'IteratorAgeMilliseconds', 'OutgoingBytes', 'OutgoingRecords', 'ReadProvisionedThroughputExceeded', 'WriteProvisionedThroughputExceeded']]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# EnhancedMetricsTypeDef

### ShardLevelMetrics
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'IncomingBytes', 'IncomingRecords', 'IteratorAgeMilliseconds', 'OutgoingBytes', 'OutgoingRecords', 'ReadProvisionedThroughputExceeded', 'WriteProvisionedThroughputExceeded']]]


# EnhancedMonitoringOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecordsInputTypeDef

### ShardIterator
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### StreamARN
- **Type**: typing.Optional[str]


# GetRecordsOutputTypeDef

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.RecordTypeDef]
- **Required**: Yes

### NextShardIterator
- **Type**: <class 'str'>
- **Required**: Yes

### MillisBehindLatest
- **Type**: <class 'int'>
- **Required**: Yes

### ChildShards
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.ChildShardTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyOutputTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetShardIteratorInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.TimestampTypeDef]

### StreamARN
- **Type**: typing.Optional[str]


# GetShardIteratorOutputTypeDef

### ShardIterator
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HashKeyRangeTypeDef

### StartingHashKey
- **Type**: <class 'str'>
- **Required**: Yes

### EndingHashKey
- **Type**: <class 'str'>
- **Required**: Yes


# IncreaseStreamRetentionPeriodInputTypeDef

### RetentionPeriodHours
- **Type**: <class 'int'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# InternalFailureExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# KMSAccessDeniedExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# KMSDisabledExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# KMSInvalidStateExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# KMSNotFoundExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# KMSOptInRequiredTypeDef

### message
- **Type**: typing.Optional[str]


# KMSThrottlingExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# ListShardsInputPaginateTypeDef

### StreamName
- **Type**: typing.Optional[str]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]

### StreamCreationTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.TimestampTypeDef]

### ShardFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.ShardFilterTypeDef]

### StreamARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.PaginatorConfigTypeDef]


# ListShardsInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### ExclusiveStartShardId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StreamCreationTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.TimestampTypeDef]

### ShardFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.ShardFilterTypeDef]

### StreamARN
- **Type**: typing.Optional[str]


# ListShardsOutputTypeDef

### Shards
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.ShardTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamConsumersInputPaginateTypeDef

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### StreamCreationTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.PaginatorConfigTypeDef]


# ListStreamConsumersInputTypeDef

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StreamCreationTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.TimestampTypeDef]


# ListStreamConsumersOutputTypeDef

### Consumers
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.ConsumerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamsInputPaginateTypeDef

### ExclusiveStartStreamName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.PaginatorConfigTypeDef]


# ListStreamsInputTypeDef

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartStreamName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListStreamsOutputTypeDef

### StreamNames
- **Type**: typing.List[str]
- **Required**: Yes

### HasMoreStreams
- **Type**: <class 'bool'>
- **Required**: Yes

### StreamSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.StreamSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForStreamInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### ExclusiveStartTagKey
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### StreamARN
- **Type**: typing.Optional[str]


# ListTagsForStreamOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.TagTypeDef]
- **Required**: Yes

### HasMoreTags
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MergeShardsInputTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutRecordInputTypeDef

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.BlobTypeDef'>
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


# PutRecordOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRecordsInputTypeDef

### Records
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesis_classes.PutRecordsRequestEntryTypeDef]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# PutRecordsOutputTypeDef

### FailedRecordCount
- **Type**: <class 'int'>
- **Required**: Yes

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.PutRecordsResultEntryTypeDef]
- **Required**: Yes

### EncryptionType
- **Type**: typing.Literal['KMS', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRecordsRequestEntryTypeDef

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.BlobTypeDef'>
- **Required**: Yes

### PartitionKey
- **Type**: <class 'str'>
- **Required**: Yes

### ExplicitHashKey
- **Type**: typing.Optional[str]


# PutRecordsResultEntryTypeDef

### SequenceNumber
- **Type**: typing.Optional[str]

### ShardId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# PutResourcePolicyInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# RecordTypeDef

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


# RegisterStreamConsumerInputTypeDef

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerName
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterStreamConsumerOutputTypeDef

### Consumer
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ConsumerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveTagsFromStreamInputTypeDef

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# ResourceInUseExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# ResourceNotFoundExceptionTypeDef

### message
- **Type**: typing.Optional[str]


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


# SequenceNumberRangeTypeDef

### StartingSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### EndingSequenceNumber
- **Type**: typing.Optional[str]


# ShardFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ShardTypeDef

### ShardId
- **Type**: <class 'str'>
- **Required**: Yes

### HashKeyRange
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.HashKeyRangeTypeDef'>
- **Required**: Yes

### SequenceNumberRange
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.SequenceNumberRangeTypeDef'>
- **Required**: Yes

### ParentShardId
- **Type**: typing.Optional[str]

### AdjacentParentShardId
- **Type**: typing.Optional[str]


# SplitShardInputTypeDef

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


# StartStreamEncryptionInputTypeDef

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


# StartingPositionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StopStreamEncryptionInputTypeDef

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


# StreamDescriptionSummaryTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.EnhancedMetricsTypeDef]
- **Required**: Yes

### OpenShardCount
- **Type**: <class 'int'>
- **Required**: Yes

### StreamModeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.StreamModeDetailsTypeDef]

### EncryptionType
- **Type**: typing.Optional[typing.Literal['KMS', 'NONE']]

### KeyId
- **Type**: typing.Optional[str]

### ConsumerCount
- **Type**: typing.Optional[int]


# StreamDescriptionTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.ShardTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.EnhancedMetricsTypeDef]
- **Required**: Yes

### StreamModeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.StreamModeDetailsTypeDef]

### EncryptionType
- **Type**: typing.Optional[typing.Literal['KMS', 'NONE']]

### KeyId
- **Type**: typing.Optional[str]


# StreamModeDetailsTypeDef

### StreamMode
- **Type**: typing.Literal['ON_DEMAND', 'PROVISIONED']
- **Required**: Yes


# StreamSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.StreamModeDetailsTypeDef]

### StreamCreationTimestamp
- **Type**: typing.Optional[datetime.datetime]


# SubscribeToShardEventStreamTypeDef

### SubscribeToShardEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.SubscribeToShardEventTypeDef'>
- **Required**: Yes

### ResourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.ResourceNotFoundExceptionTypeDef]

### ResourceInUseException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.ResourceInUseExceptionTypeDef]

### KMSDisabledException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.KMSDisabledExceptionTypeDef]

### KMSInvalidStateException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.KMSInvalidStateExceptionTypeDef]

### KMSAccessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.KMSAccessDeniedExceptionTypeDef]

### KMSNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.KMSNotFoundExceptionTypeDef]

### KMSOptInRequired
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.KMSOptInRequiredTypeDef]

### KMSThrottlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.KMSThrottlingExceptionTypeDef]

### InternalFailureException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_classes.InternalFailureExceptionTypeDef]


# SubscribeToShardEventTypeDef

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_classes.RecordTypeDef]
- **Required**: Yes

### ContinuationSequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### MillisBehindLatest
- **Type**: <class 'int'>
- **Required**: Yes

### ChildShards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesis_classes.ChildShardTypeDef]]


# SubscribeToShardInputTypeDef

### ConsumerARN
- **Type**: <class 'str'>
- **Required**: Yes

### ShardId
- **Type**: <class 'str'>
- **Required**: Yes

### StartingPosition
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.StartingPositionTypeDef'>
- **Required**: Yes


# SubscribeToShardOutputTypeDef

### EventStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.kinesis_classes.SubscribeToShardEventStreamTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateShardCountInputTypeDef

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


# UpdateShardCountOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStreamModeInputTypeDef

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### StreamModeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_classes.StreamModeDetailsTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


