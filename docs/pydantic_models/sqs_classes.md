# Sqs Classes

# AddPermissionRequestQueueAddPermissionTypeDef

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### AWSAccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AddPermissionRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### AWSAccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchResultErrorEntryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SenderFault
- **Type**: <class 'bool'>
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]


# CancelMessageMoveTaskRequestRequestTypeDef

### TaskHandle
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMessageMoveTaskResultTypeDef

### ApproximateNumberOfMessagesMoved
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChangeMessageVisibilityBatchRequestEntryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiptHandle
- **Type**: <class 'str'>
- **Required**: Yes

### VisibilityTimeout
- **Type**: typing.Optional[int]


# ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.ChangeMessageVisibilityBatchRequestEntryTypeDef]
- **Required**: Yes


# ChangeMessageVisibilityBatchRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.ChangeMessageVisibilityBatchRequestEntryTypeDef]
- **Required**: Yes


# ChangeMessageVisibilityBatchResultEntryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ChangeMessageVisibilityBatchResultTypeDef

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.ChangeMessageVisibilityBatchResultEntryTypeDef]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.BatchResultErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef

### VisibilityTimeout
- **Type**: <class 'int'>
- **Required**: Yes


# ChangeMessageVisibilityRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiptHandle
- **Type**: <class 'str'>
- **Required**: Yes

### VisibilityTimeout
- **Type**: <class 'int'>
- **Required**: Yes


# CreateQueueRequestRequestTypeDef

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['All', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SqsManagedSseEnabled', 'VisibilityTimeout'], str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQueueRequestServiceResourceCreateQueueTypeDef

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['All', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SqsManagedSseEnabled', 'VisibilityTimeout'], str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQueueResultTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMessageBatchRequestEntryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiptHandle
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessageBatchRequestQueueDeleteMessagesTypeDef

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.DeleteMessageBatchRequestEntryTypeDef]
- **Required**: Yes


# DeleteMessageBatchRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.DeleteMessageBatchRequestEntryTypeDef]
- **Required**: Yes


# DeleteMessageBatchResultEntryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessageBatchResultTypeDef

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.DeleteMessageBatchResultEntryTypeDef]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.BatchResultErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMessageRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiptHandle
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueueAttributesRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWSTraceHeader', 'All', 'ApproximateFirstReceiveTimestamp', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ApproximateReceiveCount', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageDeduplicationId', 'MessageGroupId', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SenderId', 'SentTimestamp', 'SequenceNumber', 'SqsManagedSseEnabled', 'VisibilityTimeout']]]


# GetQueueAttributesResultTypeDef

### Attributes
- **Type**: typing.Dict[typing.Literal['All', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SqsManagedSseEnabled', 'VisibilityTimeout'], str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueueUrlRequestRequestTypeDef

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### QueueOwnerAWSAccountId
- **Type**: typing.Optional[str]


# GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### QueueOwnerAWSAccountId
- **Type**: typing.Optional[str]


# GetQueueUrlResultTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeadLetterSourceQueuesRequestListDeadLetterSourceQueuesPaginateTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sqs_classes.PaginatorConfigTypeDef]


# ListDeadLetterSourceQueuesRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDeadLetterSourceQueuesResultTypeDef

### queueUrls
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMessageMoveTasksRequestRequestTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]


# ListMessageMoveTasksResultEntryTypeDef

### TaskHandle
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]

### MaxNumberOfMessagesPerSecond
- **Type**: typing.Optional[int]

### ApproximateNumberOfMessagesMoved
- **Type**: typing.Optional[int]

### ApproximateNumberOfMessagesToMove
- **Type**: typing.Optional[int]

### FailureReason
- **Type**: typing.Optional[str]

### StartedTimestamp
- **Type**: typing.Optional[int]


# ListMessageMoveTasksResultTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.ListMessageMoveTasksResultEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQueueTagsRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ListQueueTagsResultTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQueuesRequestListQueuesPaginateTypeDef

### QueueNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sqs_classes.PaginatorConfigTypeDef]


# ListQueuesRequestRequestTypeDef

### QueueNamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListQueuesResultTypeDef

### QueueUrls
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MessageAttributeValueExtraOutputTypeDef

### DataType
- **Type**: <class 'str'>
- **Required**: Yes

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Optional[bytes]

### StringListValues
- **Type**: typing.Optional[typing.List[str]]

### BinaryListValues
- **Type**: typing.Optional[typing.List[bytes]]


# MessageAttributeValueOutputTypeDef

### DataType
- **Type**: <class 'str'>
- **Required**: Yes

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Optional[bytes]

### StringListValues
- **Type**: typing.Optional[typing.List[str]]

### BinaryListValues
- **Type**: typing.Optional[typing.List[bytes]]


# MessageAttributeValueTypeDef

### DataType
- **Type**: <class 'str'>
- **Required**: Yes

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### StringListValues
- **Type**: typing.Optional[typing.Sequence[str]]

### BinaryListValues
- **Type**: typing.Optional[typing.Sequence[typing.Union[str, bytes, typing.IO[typing.Any]]]]


# MessageSystemAttributeValueTypeDef

### DataType
- **Type**: <class 'str'>
- **Required**: Yes

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### StringListValues
- **Type**: typing.Optional[typing.Sequence[str]]

### BinaryListValues
- **Type**: typing.Optional[typing.Sequence[typing.Union[str, bytes, typing.IO[typing.Any]]]]


# MessageTypeDef

### MessageId
- **Type**: typing.Optional[str]

### ReceiptHandle
- **Type**: typing.Optional[str]

### MD5OfBody
- **Type**: typing.Optional[str]

### Body
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[typing.Literal['AWSTraceHeader', 'All', 'ApproximateFirstReceiveTimestamp', 'ApproximateReceiveCount', 'DeadLetterQueueSourceArn', 'MessageDeduplicationId', 'MessageGroupId', 'SenderId', 'SentTimestamp', 'SequenceNumber'], str]]

### MD5OfMessageAttributes
- **Type**: typing.Optional[str]

### MessageAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sqs_classes.MessageAttributeValueOutputTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PurgeQueueRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ReceiveMessageRequestQueueReceiveMessagesTypeDef

### AttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWSTraceHeader', 'All', 'ApproximateFirstReceiveTimestamp', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ApproximateReceiveCount', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageDeduplicationId', 'MessageGroupId', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SenderId', 'SentTimestamp', 'SequenceNumber', 'SqsManagedSseEnabled', 'VisibilityTimeout']]]

### MessageSystemAttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWSTraceHeader', 'All', 'ApproximateFirstReceiveTimestamp', 'ApproximateReceiveCount', 'DeadLetterQueueSourceArn', 'MessageDeduplicationId', 'MessageGroupId', 'SenderId', 'SentTimestamp', 'SequenceNumber']]]

### MessageAttributeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxNumberOfMessages
- **Type**: typing.Optional[int]

### VisibilityTimeout
- **Type**: typing.Optional[int]

### WaitTimeSeconds
- **Type**: typing.Optional[int]

### ReceiveRequestAttemptId
- **Type**: typing.Optional[str]


# ReceiveMessageRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWSTraceHeader', 'All', 'ApproximateFirstReceiveTimestamp', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ApproximateReceiveCount', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageDeduplicationId', 'MessageGroupId', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SenderId', 'SentTimestamp', 'SequenceNumber', 'SqsManagedSseEnabled', 'VisibilityTimeout']]]

### MessageSystemAttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWSTraceHeader', 'All', 'ApproximateFirstReceiveTimestamp', 'ApproximateReceiveCount', 'DeadLetterQueueSourceArn', 'MessageDeduplicationId', 'MessageGroupId', 'SenderId', 'SentTimestamp', 'SequenceNumber']]]

### MessageAttributeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxNumberOfMessages
- **Type**: typing.Optional[int]

### VisibilityTimeout
- **Type**: typing.Optional[int]

### WaitTimeSeconds
- **Type**: typing.Optional[int]

### ReceiveRequestAttemptId
- **Type**: typing.Optional[str]


# ReceiveMessageResultTypeDef

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.MessageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemovePermissionRequestQueueRemovePermissionTypeDef

### Label
- **Type**: <class 'str'>
- **Required**: Yes


# RemovePermissionRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
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


# SendMessageBatchRequestEntryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MessageBody
- **Type**: <class 'str'>
- **Required**: Yes

### DelaySeconds
- **Type**: typing.Optional[int]

### MessageAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sqs_classes.MessageAttributeValueTypeDef]]

### MessageSystemAttributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AWSTraceHeader'], aws_resource_validator.pydantic_models.sqs_classes.MessageSystemAttributeValueTypeDef]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# SendMessageBatchRequestQueueSendMessagesTypeDef

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.SendMessageBatchRequestEntryTypeDef]
- **Required**: Yes


# SendMessageBatchRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.SendMessageBatchRequestEntryTypeDef]
- **Required**: Yes


# SendMessageBatchResultEntryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### MD5OfMessageBody
- **Type**: <class 'str'>
- **Required**: Yes

### MD5OfMessageAttributes
- **Type**: typing.Optional[str]

### MD5OfMessageSystemAttributes
- **Type**: typing.Optional[str]

### SequenceNumber
- **Type**: typing.Optional[str]


# SendMessageBatchResultTypeDef

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.SendMessageBatchResultEntryTypeDef]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.BatchResultErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendMessageRequestQueueSendMessageTypeDef

### MessageBody
- **Type**: <class 'str'>
- **Required**: Yes

### DelaySeconds
- **Type**: typing.Optional[int]

### MessageAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sqs_classes.MessageAttributeValueTypeDef]]

### MessageSystemAttributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AWSTraceHeader'], aws_resource_validator.pydantic_models.sqs_classes.MessageSystemAttributeValueTypeDef]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# SendMessageRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### MessageBody
- **Type**: <class 'str'>
- **Required**: Yes

### DelaySeconds
- **Type**: typing.Optional[int]

### MessageAttributes
- **Type**: typing.Optional[typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.sqs_classes.MessageAttributeValueTypeDef, aws_resource_validator.pydantic_models.sqs_classes.MessageAttributeValueExtraOutputTypeDef]]]

### MessageSystemAttributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AWSTraceHeader'], aws_resource_validator.pydantic_models.sqs_classes.MessageSystemAttributeValueTypeDef]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# SendMessageResultTypeDef

### MD5OfMessageBody
- **Type**: <class 'str'>
- **Required**: Yes

### MD5OfMessageAttributes
- **Type**: <class 'str'>
- **Required**: Yes

### MD5OfMessageSystemAttributes
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### SequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetQueueAttributesRequestQueueSetAttributesTypeDef

### Attributes
- **Type**: typing.Mapping[typing.Literal['All', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SqsManagedSseEnabled', 'VisibilityTimeout'], str]
- **Required**: Yes


# SetQueueAttributesRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Mapping[typing.Literal['All', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SqsManagedSseEnabled', 'VisibilityTimeout'], str]
- **Required**: Yes


# StartMessageMoveTaskRequestRequestTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]

### MaxNumberOfMessagesPerSecond
- **Type**: typing.Optional[int]


# StartMessageMoveTaskResultTypeDef

### TaskHandle
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagQueueRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagQueueRequestRequestTypeDef

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


