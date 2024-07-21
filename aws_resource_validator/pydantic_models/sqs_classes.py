from datetime import datetime
from pydantic import BaseModel
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

class AddPermissionRequestQueueAddPermissionTypeDef(BaseModel):
    Label: str
    AWSAccountIds: Sequence[str]
    Actions: Sequence[str]

class AddPermissionRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    Label: str
    AWSAccountIds: Sequence[str]
    Actions: Sequence[str]

class BatchResultErrorEntryTypeDef(BaseModel):
    Id: str
    SenderFault: bool
    Code: str
    Message: Optional[str] = None

class CancelMessageMoveTaskRequestRequestTypeDef(BaseModel):
    TaskHandle: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ChangeMessageVisibilityBatchRequestEntryTypeDef(BaseModel):
    Id: str
    ReceiptHandle: str
    VisibilityTimeout: Optional[int] = None

class ChangeMessageVisibilityBatchResultEntryTypeDef(BaseModel):
    Id: str

class ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef(BaseModel):
    VisibilityTimeout: int

class ChangeMessageVisibilityRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    ReceiptHandle: str
    VisibilityTimeout: int

class CreateQueueRequestRequestTypeDef(BaseModel):
    QueueName: str
    Attributes: Optional[Mapping[QueueAttributeNameType, str]] = None
    tags: Optional[Mapping[str, str]] = None

class CreateQueueRequestServiceResourceCreateQueueTypeDef(BaseModel):
    QueueName: str
    Attributes: Optional[Mapping[QueueAttributeNameType, str]] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteMessageBatchRequestEntryTypeDef(BaseModel):
    Id: str
    ReceiptHandle: str

class DeleteMessageBatchResultEntryTypeDef(BaseModel):
    Id: str

class DeleteMessageRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    ReceiptHandle: str

class DeleteQueueRequestRequestTypeDef(BaseModel):
    QueueUrl: str

class GetQueueAttributesRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    AttributeNames: Optional[Sequence[QueueAttributeFilterType]] = None

class GetQueueUrlRequestRequestTypeDef(BaseModel):
    QueueName: str
    QueueOwnerAWSAccountId: Optional[str] = None

class GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef(BaseModel):
    QueueName: str
    QueueOwnerAWSAccountId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDeadLetterSourceQueuesRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMessageMoveTasksRequestRequestTypeDef(BaseModel):
    SourceArn: str
    MaxResults: Optional[int] = None

class ListMessageMoveTasksResultEntryTypeDef(BaseModel):
    TaskHandle: Optional[str] = None
    Status: Optional[str] = None
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    MaxNumberOfMessagesPerSecond: Optional[int] = None
    ApproximateNumberOfMessagesMoved: Optional[int] = None
    ApproximateNumberOfMessagesToMove: Optional[int] = None
    FailureReason: Optional[str] = None
    StartedTimestamp: Optional[int] = None

class ListQueueTagsRequestRequestTypeDef(BaseModel):
    QueueUrl: str

class ListQueuesRequestRequestTypeDef(BaseModel):
    QueueNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MessageAttributeValueExtraOutputTypeDef(BaseModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[bytes] = None
    StringListValues: Optional[List[str]] = None
    BinaryListValues: Optional[List[bytes]] = None

class MessageAttributeValueOutputTypeDef(BaseModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[bytes] = None
    StringListValues: Optional[List[str]] = None
    BinaryListValues: Optional[List[bytes]] = None

class PurgeQueueRequestRequestTypeDef(BaseModel):
    QueueUrl: str

class ReceiveMessageRequestQueueReceiveMessagesTypeDef(BaseModel):
    AttributeNames: Optional[Sequence[QueueAttributeFilterType]] = None
    MessageSystemAttributeNames: Optional[Sequence[MessageSystemAttributeNameType]] = None
    MessageAttributeNames: Optional[Sequence[str]] = None
    MaxNumberOfMessages: Optional[int] = None
    VisibilityTimeout: Optional[int] = None
    WaitTimeSeconds: Optional[int] = None
    ReceiveRequestAttemptId: Optional[str] = None

class ReceiveMessageRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    AttributeNames: Optional[Sequence[QueueAttributeFilterType]] = None
    MessageSystemAttributeNames: Optional[Sequence[MessageSystemAttributeNameType]] = None
    MessageAttributeNames: Optional[Sequence[str]] = None
    MaxNumberOfMessages: Optional[int] = None
    VisibilityTimeout: Optional[int] = None
    WaitTimeSeconds: Optional[int] = None
    ReceiveRequestAttemptId: Optional[str] = None

class RemovePermissionRequestQueueRemovePermissionTypeDef(BaseModel):
    Label: str

class RemovePermissionRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    Label: str

class SendMessageBatchResultEntryTypeDef(BaseModel):
    Id: str
    MessageId: str
    MD5OfMessageBody: str
    MD5OfMessageAttributes: Optional[str] = None
    MD5OfMessageSystemAttributes: Optional[str] = None
    SequenceNumber: Optional[str] = None

class SetQueueAttributesRequestQueueSetAttributesTypeDef(BaseModel):
    Attributes: Mapping[QueueAttributeNameType, str]

class SetQueueAttributesRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    Attributes: Mapping[QueueAttributeNameType, str]

class StartMessageMoveTaskRequestRequestTypeDef(BaseModel):
    SourceArn: str
    DestinationArn: Optional[str] = None
    MaxNumberOfMessagesPerSecond: Optional[int] = None

class TagQueueRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    Tags: Mapping[str, str]

class UntagQueueRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    TagKeys: Sequence[str]

class MessageAttributeValueTypeDef(BaseModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[BlobTypeDef] = None
    StringListValues: Optional[Sequence[str]] = None
    BinaryListValues: Optional[Sequence[BlobTypeDef]] = None

class MessageSystemAttributeValueTypeDef(BaseModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[BlobTypeDef] = None
    StringListValues: Optional[Sequence[str]] = None
    BinaryListValues: Optional[Sequence[BlobTypeDef]] = None

class CancelMessageMoveTaskResultTypeDef(BaseModel):
    ApproximateNumberOfMessagesMoved: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueResultTypeDef(BaseModel):
    QueueUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueAttributesResultTypeDef(BaseModel):
    Attributes: Dict[QueueAttributeNameType, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueUrlResultTypeDef(BaseModel):
    QueueUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeadLetterSourceQueuesResultTypeDef(BaseModel):
    queueUrls: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQueueTagsResultTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueuesResultTypeDef(BaseModel):
    QueueUrls: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SendMessageResultTypeDef(BaseModel):
    MD5OfMessageBody: str
    MD5OfMessageAttributes: str
    MD5OfMessageSystemAttributes: str
    MessageId: str
    SequenceNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMessageMoveTaskResultTypeDef(BaseModel):
    TaskHandle: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef(BaseModel):
    Entries: Sequence[ChangeMessageVisibilityBatchRequestEntryTypeDef]

class ChangeMessageVisibilityBatchRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    Entries: Sequence[ChangeMessageVisibilityBatchRequestEntryTypeDef]

class ChangeMessageVisibilityBatchResultTypeDef(BaseModel):
    Successful: List[ChangeMessageVisibilityBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMessageBatchRequestQueueDeleteMessagesTypeDef(BaseModel):
    Entries: Sequence[DeleteMessageBatchRequestEntryTypeDef]

class DeleteMessageBatchRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    Entries: Sequence[DeleteMessageBatchRequestEntryTypeDef]

class DeleteMessageBatchResultTypeDef(BaseModel):
    Successful: List[DeleteMessageBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeadLetterSourceQueuesRequestListDeadLetterSourceQueuesPaginateTypeDef(BaseModel):
    QueueUrl: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueuesRequestListQueuesPaginateTypeDef(BaseModel):
    QueueNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMessageMoveTasksResultTypeDef(BaseModel):
    Results: List[ListMessageMoveTasksResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MessageTypeDef(BaseModel):
    MessageId: Optional[str] = None
    ReceiptHandle: Optional[str] = None
    MD5OfBody: Optional[str] = None
    Body: Optional[str] = None
    Attributes: Optional[Dict[MessageSystemAttributeNameType, str]] = None
    MD5OfMessageAttributes: Optional[str] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueOutputTypeDef]] = None

class SendMessageBatchResultTypeDef(BaseModel):
    Successful: List[SendMessageBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendMessageBatchRequestEntryTypeDef(BaseModel):
    Id: str
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageSystemAttributes: Optional[       Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None

class SendMessageRequestQueueSendMessageTypeDef(BaseModel):
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageSystemAttributes: Optional[       Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None

class ReceiveMessageResultTypeDef(BaseModel):
    Messages: List[MessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendMessageRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueUnionTypeDef]] = None
    MessageSystemAttributes: Optional[       Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None

class SendMessageBatchRequestQueueSendMessagesTypeDef(BaseModel):
    Entries: Sequence[SendMessageBatchRequestEntryTypeDef]

class SendMessageBatchRequestRequestTypeDef(BaseModel):
    QueueUrl: str
    Entries: Sequence[SendMessageBatchRequestEntryTypeDef]

