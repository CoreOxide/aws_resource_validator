from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sqs.sqs_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AddPermissionRequestQueueAddPermission(BaseValidatorModel):
    Label: str
    AWSAccountIds: List[str]
    Actions: List[str]


class AddPermissionRequest(BaseValidatorModel):
    QueueUrl: str
    Label: str
    AWSAccountIds: List[str]
    Actions: List[str]


class BatchResultErrorEntry(BaseValidatorModel):
    Id: str
    SenderFault: bool
    Code: str
    Message: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CancelMessageMoveTaskRequest(BaseValidatorModel):
    TaskHandle: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ChangeMessageVisibilityBatchRequestEntry(BaseValidatorModel):
    Id: str
    ReceiptHandle: str
    VisibilityTimeout: Optional[int] = None


class ChangeMessageVisibilityBatchResultEntry(BaseValidatorModel):
    Id: str


class ChangeMessageVisibilityRequestMessageChangeVisibility(BaseValidatorModel):
    VisibilityTimeout: int


class ChangeMessageVisibilityRequest(BaseValidatorModel):
    QueueUrl: str
    ReceiptHandle: str
    VisibilityTimeout: int


class CreateQueueRequestServiceResourceCreateQueue(BaseValidatorModel):
    QueueName: str
    Attributes: Optional[Dict[QueueAttributeNameType, str]] = None
    tags: Optional[Dict[str, str]] = None


class CreateQueueRequest(BaseValidatorModel):
    QueueName: str
    Attributes: Optional[Dict[QueueAttributeNameType, str]] = None
    tags: Optional[Dict[str, str]] = None


class DeleteMessageBatchRequestEntry(BaseValidatorModel):
    Id: str
    ReceiptHandle: str


class DeleteMessageBatchResultEntry(BaseValidatorModel):
    Id: str


class DeleteMessageRequest(BaseValidatorModel):
    QueueUrl: str
    ReceiptHandle: str


class DeleteQueueRequest(BaseValidatorModel):
    QueueUrl: str


class GetQueueAttributesRequest(BaseValidatorModel):
    QueueUrl: str
    AttributeNames: Optional[List[QueueAttributeFilterType]] = None


class GetQueueUrlRequestServiceResourceGetQueueByName(BaseValidatorModel):
    QueueName: str
    QueueOwnerAWSAccountId: Optional[str] = None


class GetQueueUrlRequest(BaseValidatorModel):
    QueueName: str
    QueueOwnerAWSAccountId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDeadLetterSourceQueuesRequest(BaseValidatorModel):
    QueueUrl: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMessageMoveTasksRequest(BaseValidatorModel):
    SourceArn: str
    MaxResults: Optional[int] = None


class ListMessageMoveTasksResultEntry(BaseValidatorModel):
    TaskHandle: Optional[str] = None
    Status: Optional[str] = None
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    MaxNumberOfMessagesPerSecond: Optional[int] = None
    ApproximateNumberOfMessagesMoved: Optional[int] = None
    ApproximateNumberOfMessagesToMove: Optional[int] = None
    FailureReason: Optional[str] = None
    StartedTimestamp: Optional[int] = None


class ListQueueTagsRequest(BaseValidatorModel):
    QueueUrl: str


class ListQueuesRequest(BaseValidatorModel):
    QueueNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MessageAttributeValueOutput(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[bytes] = None
    StringListValues: Optional[List[str]] = None
    BinaryListValues: Optional[List[bytes]] = None


class PurgeQueueRequest(BaseValidatorModel):
    QueueUrl: str


class ReceiveMessageRequestQueueReceiveMessages(BaseValidatorModel):
    AttributeNames: Optional[List[QueueAttributeFilterType]] = None
    MessageSystemAttributeNames: Optional[List[MessageSystemAttributeNameType]] = None
    MessageAttributeNames: Optional[List[str]] = None
    MaxNumberOfMessages: Optional[int] = None
    VisibilityTimeout: Optional[int] = None
    WaitTimeSeconds: Optional[int] = None
    ReceiveRequestAttemptId: Optional[str] = None


class ReceiveMessageRequest(BaseValidatorModel):
    QueueUrl: str
    AttributeNames: Optional[List[QueueAttributeFilterType]] = None
    MessageSystemAttributeNames: Optional[List[MessageSystemAttributeNameType]] = None
    MessageAttributeNames: Optional[List[str]] = None
    MaxNumberOfMessages: Optional[int] = None
    VisibilityTimeout: Optional[int] = None
    WaitTimeSeconds: Optional[int] = None
    ReceiveRequestAttemptId: Optional[str] = None


class RemovePermissionRequestQueueRemovePermission(BaseValidatorModel):
    Label: str


class RemovePermissionRequest(BaseValidatorModel):
    QueueUrl: str
    Label: str


class SendMessageBatchResultEntry(BaseValidatorModel):
    Id: str
    MessageId: str
    MD5OfMessageBody: str
    MD5OfMessageAttributes: Optional[str] = None
    MD5OfMessageSystemAttributes: Optional[str] = None
    SequenceNumber: Optional[str] = None


class SetQueueAttributesRequestQueueSetAttributes(BaseValidatorModel):
    Attributes: Dict[QueueAttributeNameType, str]


class SetQueueAttributesRequest(BaseValidatorModel):
    QueueUrl: str
    Attributes: Dict[QueueAttributeNameType, str]


class StartMessageMoveTaskRequest(BaseValidatorModel):
    SourceArn: str
    DestinationArn: Optional[str] = None
    MaxNumberOfMessagesPerSecond: Optional[int] = None


class TagQueueRequest(BaseValidatorModel):
    QueueUrl: str
    Tags: Dict[str, str]


class UntagQueueRequest(BaseValidatorModel):
    QueueUrl: str
    TagKeys: List[str]


class MessageAttributeValue(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[Blob] = None
    StringListValues: Optional[List[str]] = None
    BinaryListValues: Optional[List[Blob]] = None


class MessageSystemAttributeValue(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[Blob] = None
    StringListValues: Optional[List[str]] = None
    BinaryListValues: Optional[List[Blob]] = None


class CancelMessageMoveTaskResult(BaseValidatorModel):
    ApproximateNumberOfMessagesMoved: int
    ResponseMetadata: ResponseMetadata


class CreateQueueResult(BaseValidatorModel):
    QueueUrl: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetQueueAttributesResult(BaseValidatorModel):
    Attributes: Dict[QueueAttributeNameType, str]
    ResponseMetadata: ResponseMetadata


class GetQueueUrlResult(BaseValidatorModel):
    QueueUrl: str
    ResponseMetadata: ResponseMetadata


class ListDeadLetterSourceQueuesResult(BaseValidatorModel):
    queueUrls: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListQueueTagsResult(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListQueuesResult(BaseValidatorModel):
    QueueUrls: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SendMessageResult(BaseValidatorModel):
    MD5OfMessageBody: str
    MD5OfMessageAttributes: str
    MD5OfMessageSystemAttributes: str
    MessageId: str
    SequenceNumber: str
    ResponseMetadata: ResponseMetadata


class StartMessageMoveTaskResult(BaseValidatorModel):
    TaskHandle: str
    ResponseMetadata: ResponseMetadata


class ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatch(BaseValidatorModel):
    Entries: List[ChangeMessageVisibilityBatchRequestEntry]


class ChangeMessageVisibilityBatchRequest(BaseValidatorModel):
    QueueUrl: str
    Entries: List[ChangeMessageVisibilityBatchRequestEntry]


class ChangeMessageVisibilityBatchResult(BaseValidatorModel):
    Successful: List[ChangeMessageVisibilityBatchResultEntry]
    Failed: List[BatchResultErrorEntry]
    ResponseMetadata: ResponseMetadata


class DeleteMessageBatchRequestQueueDeleteMessages(BaseValidatorModel):
    Entries: List[DeleteMessageBatchRequestEntry]


class DeleteMessageBatchRequest(BaseValidatorModel):
    QueueUrl: str
    Entries: List[DeleteMessageBatchRequestEntry]


class DeleteMessageBatchResult(BaseValidatorModel):
    Successful: List[DeleteMessageBatchResultEntry]
    Failed: List[BatchResultErrorEntry]
    ResponseMetadata: ResponseMetadata


class ListDeadLetterSourceQueuesRequestPaginate(BaseValidatorModel):
    QueueUrl: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueuesRequestPaginate(BaseValidatorModel):
    QueueNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMessageMoveTasksResult(BaseValidatorModel):
    Results: List[ListMessageMoveTasksResultEntry]
    ResponseMetadata: ResponseMetadata


class Message(BaseValidatorModel):
    MessageId: Optional[str] = None
    ReceiptHandle: Optional[str] = None
    MD5OfBody: Optional[str] = None
    Body: Optional[str] = None
    Attributes: Optional[Dict[MessageSystemAttributeNameType, str]] = None
    MD5OfMessageAttributes: Optional[str] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueOutput]] = None


class SendMessageBatchResult(BaseValidatorModel):
    Successful: List[SendMessageBatchResultEntry]
    Failed: List[BatchResultErrorEntry]
    ResponseMetadata: ResponseMetadata

MessageAttributeValueUnion = Union[MessageAttributeValue, MessageAttributeValueOutput]


class ReceiveMessageResult(BaseValidatorModel):
    Messages: List[Message]
    ResponseMetadata: ResponseMetadata


class SendMessageBatchRequestEntry(BaseValidatorModel):
    Id: str
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueUnion]] = None
    MessageSystemAttributes: Optional[Dict[Literal['AWSTraceHeader'], MessageSystemAttributeValue]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class SendMessageRequestQueueSendMessage(BaseValidatorModel):
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueUnion]] = None
    MessageSystemAttributes: Optional[Dict[Literal['AWSTraceHeader'], MessageSystemAttributeValue]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class SendMessageRequest(BaseValidatorModel):
    QueueUrl: str
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueUnion]] = None
    MessageSystemAttributes: Optional[Dict[Literal['AWSTraceHeader'], MessageSystemAttributeValue]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class SendMessageBatchRequestQueueSendMessages(BaseValidatorModel):
    Entries: List[SendMessageBatchRequestEntry]


class SendMessageBatchRequest(BaseValidatorModel):
    QueueUrl: str
    Entries: List[SendMessageBatchRequestEntry]