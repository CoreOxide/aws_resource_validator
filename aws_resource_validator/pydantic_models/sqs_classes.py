from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.sqs_constants import *

class AddPermissionRequestQueueAddPermission(BaseValidatorModel):
    Label: str
    AWSAccountIds: Sequence[str]
    Actions: Sequence[str]


class AddPermissionRequest(BaseValidatorModel):
    QueueUrl: str
    Label: str
    AWSAccountIds: Sequence[str]
    Actions: Sequence[str]


class BatchResultErrorEntry(BaseValidatorModel):
    Id: str
    SenderFault: bool
    Code: str
    Message: Optional[str] = None


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
    Attributes: Optional[Mapping[QueueAttributeNameType, str]] = None
    tags: Optional[Mapping[str, str]] = None


class CreateQueueRequest(BaseValidatorModel):
    QueueName: str
    Attributes: Optional[Mapping[QueueAttributeNameType, str]] = None
    tags: Optional[Mapping[str, str]] = None


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
    AttributeNames: Optional[Sequence[QueueAttributeFilterType]] = None


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
    AttributeNames: Optional[Sequence[QueueAttributeFilterType]] = None
    MessageSystemAttributeNames: Optional[Sequence[MessageSystemAttributeNameType]] = None
    MessageAttributeNames: Optional[Sequence[str]] = None
    MaxNumberOfMessages: Optional[int] = None
    VisibilityTimeout: Optional[int] = None
    WaitTimeSeconds: Optional[int] = None
    ReceiveRequestAttemptId: Optional[str] = None


class ReceiveMessageRequest(BaseValidatorModel):
    QueueUrl: str
    AttributeNames: Optional[Sequence[QueueAttributeFilterType]] = None
    MessageSystemAttributeNames: Optional[Sequence[MessageSystemAttributeNameType]] = None
    MessageAttributeNames: Optional[Sequence[str]] = None
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
    Attributes: Mapping[QueueAttributeNameType, str]


class SetQueueAttributesRequest(BaseValidatorModel):
    QueueUrl: str
    Attributes: Mapping[QueueAttributeNameType, str]


class StartMessageMoveTaskRequest(BaseValidatorModel):
    SourceArn: str
    DestinationArn: Optional[str] = None
    MaxNumberOfMessagesPerSecond: Optional[int] = None


class TagQueueRequest(BaseValidatorModel):
    QueueUrl: str
    Tags: Mapping[str, str]


class UntagQueueRequest(BaseValidatorModel):
    QueueUrl: str
    TagKeys: Sequence[str]


class Blob(BaseValidatorModel):
    pass


class MessageAttributeValue(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[Blob] = None
    StringListValues: Optional[Sequence[str]] = None
    BinaryListValues: Optional[Sequence[Blob]] = None


class MessageSystemAttributeValue(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[Blob] = None
    StringListValues: Optional[Sequence[str]] = None
    BinaryListValues: Optional[Sequence[Blob]] = None


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
    Entries: Sequence[ChangeMessageVisibilityBatchRequestEntry]


class ChangeMessageVisibilityBatchRequest(BaseValidatorModel):
    QueueUrl: str
    Entries: Sequence[ChangeMessageVisibilityBatchRequestEntry]


class ChangeMessageVisibilityBatchResult(BaseValidatorModel):
    Successful: List[ChangeMessageVisibilityBatchResultEntry]
    Failed: List[BatchResultErrorEntry]
    ResponseMetadata: ResponseMetadata


class DeleteMessageBatchRequestQueueDeleteMessages(BaseValidatorModel):
    Entries: Sequence[DeleteMessageBatchRequestEntry]


class DeleteMessageBatchRequest(BaseValidatorModel):
    QueueUrl: str
    Entries: Sequence[DeleteMessageBatchRequestEntry]


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


class ReceiveMessageResult(BaseValidatorModel):
    Messages: List[Message]
    ResponseMetadata: ResponseMetadata


class MessageAttributeValueUnion(BaseValidatorModel):
    pass


class SendMessageBatchRequestEntry(BaseValidatorModel):
    Id: str
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueUnion]] = None
    MessageSystemAttributes: Optional[ Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValue] ] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class SendMessageRequestQueueSendMessage(BaseValidatorModel):
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueUnion]] = None
    MessageSystemAttributes: Optional[ Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValue] ] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class SendMessageRequest(BaseValidatorModel):
    QueueUrl: str
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueUnion]] = None
    MessageSystemAttributes: Optional[ Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValue] ] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class SendMessageBatchRequestQueueSendMessages(BaseValidatorModel):
    Entries: Sequence[SendMessageBatchRequestEntry]


class SendMessageBatchRequest(BaseValidatorModel):
    QueueUrl: str
    Entries: Sequence[SendMessageBatchRequestEntry]


