# Sqs Classes

# AddPermissionRequest

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


# AddPermissionRequestQueueAddPermission

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

# BatchResultErrorEntry

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


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelMessageMoveTaskRequest

### TaskHandle
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMessageMoveTaskResult

### ApproximateNumberOfMessagesMoved
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# ChangeMessageVisibilityBatchRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.ChangeMessageVisibilityBatchRequestEntry]
- **Required**: Yes


# ChangeMessageVisibilityBatchRequestEntry

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiptHandle
- **Type**: <class 'str'>
- **Required**: Yes

### VisibilityTimeout
- **Type**: typing.Optional[int]


# ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatch

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.ChangeMessageVisibilityBatchRequestEntry]
- **Required**: Yes


# ChangeMessageVisibilityBatchResult

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.ChangeMessageVisibilityBatchResultEntry]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.BatchResultErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# ChangeMessageVisibilityBatchResultEntry

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ChangeMessageVisibilityRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiptHandle
- **Type**: <class 'str'>
- **Required**: Yes

### VisibilityTimeout
- **Type**: <class 'int'>
- **Required**: Yes


# ChangeMessageVisibilityRequestMessageChangeVisibility

### VisibilityTimeout
- **Type**: <class 'int'>
- **Required**: Yes


# CreateQueueRequest

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['All', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SqsManagedSseEnabled', 'VisibilityTimeout'], str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQueueRequestServiceResourceCreateQueue

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['All', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SqsManagedSseEnabled', 'VisibilityTimeout'], str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQueueResult

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMessageBatchRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.DeleteMessageBatchRequestEntry]
- **Required**: Yes


# DeleteMessageBatchRequestEntry

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiptHandle
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessageBatchRequestQueueDeleteMessages

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.DeleteMessageBatchRequestEntry]
- **Required**: Yes


# DeleteMessageBatchResult

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.DeleteMessageBatchResultEntry]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.BatchResultErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMessageBatchResultEntry

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessageRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiptHandle
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueueAttributesRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWSTraceHeader', 'All', 'ApproximateFirstReceiveTimestamp', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ApproximateReceiveCount', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageDeduplicationId', 'MessageGroupId', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SenderId', 'SentTimestamp', 'SequenceNumber', 'SqsManagedSseEnabled', 'VisibilityTimeout']]]


# GetQueueAttributesResult

### Attributes
- **Type**: typing.Dict[typing.Literal['All', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SqsManagedSseEnabled', 'VisibilityTimeout'], str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueueUrlRequest

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### QueueOwnerAWSAccountId
- **Type**: typing.Optional[str]


# GetQueueUrlRequestServiceResourceGetQueueByName

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### QueueOwnerAWSAccountId
- **Type**: typing.Optional[str]


# GetQueueUrlResult

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# ListDeadLetterSourceQueuesRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDeadLetterSourceQueuesRequestPaginate

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sqs_classes.PaginatorConfig]


# ListDeadLetterSourceQueuesResult

### queueUrls
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMessageMoveTasksRequest

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]


# ListMessageMoveTasksResult

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.ListMessageMoveTasksResultEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# ListMessageMoveTasksResultEntry

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


# ListQueueTagsRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ListQueueTagsResult

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# ListQueuesRequest

### QueueNamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListQueuesRequestPaginate

### QueueNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sqs_classes.PaginatorConfig]


# ListQueuesResult

### QueueUrls
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Message

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sqs_classes.MessageAttributeValueOutput]]


# MessageAttributeValue

### DataType
- **Type**: <class 'str'>
- **Required**: Yes

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sqs_classes.Blob]

### StringListValues
- **Type**: typing.Optional[typing.Sequence[str]]

### BinaryListValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.Blob]]


# MessageAttributeValueOutput

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


# MessageAttributeValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageSystemAttributeValue

### DataType
- **Type**: <class 'str'>
- **Required**: Yes

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sqs_classes.Blob]

### StringListValues
- **Type**: typing.Optional[typing.Sequence[str]]

### BinaryListValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.Blob]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PurgeQueueRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ReceiveMessageRequest

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


# ReceiveMessageRequestQueueReceiveMessages

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


# ReceiveMessageResult

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.Message]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# RemovePermissionRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes


# RemovePermissionRequestQueueRemovePermission

### Label
- **Type**: <class 'str'>
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


# SendMessageBatchRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.SendMessageBatchRequestEntry]
- **Required**: Yes


# SendMessageBatchRequestEntry

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MessageBody
- **Type**: <class 'str'>
- **Required**: Yes

### DelaySeconds
- **Type**: typing.Optional[int]

### MessageAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sqs_classes.MessageAttributeValueUnion]]

### MessageSystemAttributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AWSTraceHeader'], aws_resource_validator.pydantic_models.sqs_classes.MessageSystemAttributeValue]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# SendMessageBatchRequestQueueSendMessages

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sqs_classes.SendMessageBatchRequestEntry]
- **Required**: Yes


# SendMessageBatchResult

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.SendMessageBatchResultEntry]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.sqs_classes.BatchResultErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# SendMessageBatchResultEntry

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


# SendMessageRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### MessageBody
- **Type**: <class 'str'>
- **Required**: Yes

### DelaySeconds
- **Type**: typing.Optional[int]

### MessageAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sqs_classes.MessageAttributeValueUnion]]

### MessageSystemAttributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AWSTraceHeader'], aws_resource_validator.pydantic_models.sqs_classes.MessageSystemAttributeValue]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# SendMessageRequestQueueSendMessage

### MessageBody
- **Type**: <class 'str'>
- **Required**: Yes

### DelaySeconds
- **Type**: typing.Optional[int]

### MessageAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sqs_classes.MessageAttributeValueUnion]]

### MessageSystemAttributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AWSTraceHeader'], aws_resource_validator.pydantic_models.sqs_classes.MessageSystemAttributeValue]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# SendMessageResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# SetQueueAttributesRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Mapping[typing.Literal['All', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SqsManagedSseEnabled', 'VisibilityTimeout'], str]
- **Required**: Yes


# SetQueueAttributesRequestQueueSetAttributes

### Attributes
- **Type**: typing.Mapping[typing.Literal['All', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesDelayed', 'ApproximateNumberOfMessagesNotVisible', 'ContentBasedDeduplication', 'CreatedTimestamp', 'DeduplicationScope', 'DelaySeconds', 'FifoQueue', 'FifoThroughputLimit', 'KmsDataKeyReusePeriodSeconds', 'KmsMasterKeyId', 'LastModifiedTimestamp', 'MaximumMessageSize', 'MessageRetentionPeriod', 'Policy', 'QueueArn', 'ReceiveMessageWaitTimeSeconds', 'RedriveAllowPolicy', 'RedrivePolicy', 'SqsManagedSseEnabled', 'VisibilityTimeout'], str]
- **Required**: Yes


# StartMessageMoveTaskRequest

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]

### MaxNumberOfMessagesPerSecond
- **Type**: typing.Optional[int]


# StartMessageMoveTaskResult

### TaskHandle
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sqs_classes.ResponseMetadata'>
- **Required**: Yes


# TagQueueRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagQueueRequest

### QueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


