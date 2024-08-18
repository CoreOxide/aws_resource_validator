from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AddPermissionRequestQueueAddPermissionTypeDef(BaseValidatorModel):
    Label: str
    AWSAccountIds: Sequence[str]
    Actions: Sequence[str]

class AddPermissionRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    Label: str
    AWSAccountIds: Sequence[str]
    Actions: Sequence[str]

class BatchResultErrorEntryTypeDef(BaseValidatorModel):
    Id: str
    SenderFault: bool
    Code: str
    Message: Optional[str] = None

class CancelMessageMoveTaskRequestRequestTypeDef(BaseValidatorModel):
    TaskHandle: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ChangeMessageVisibilityBatchRequestEntryTypeDef(BaseValidatorModel):
    Id: str
    ReceiptHandle: str
    VisibilityTimeout: Optional[int] = None

class ChangeMessageVisibilityBatchResultEntryTypeDef(BaseValidatorModel):
    Id: str

class ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef(BaseValidatorModel):
    VisibilityTimeout: int

class ChangeMessageVisibilityRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    ReceiptHandle: str
    VisibilityTimeout: int

class CreateQueueRequestRequestTypeDef(BaseValidatorModel):
    QueueName: str
    Attributes: Optional[Mapping[QueueAttributeNameType, str]] = None
    tags: Optional[Mapping[str, str]] = None

class CreateQueueRequestServiceResourceCreateQueueTypeDef(BaseValidatorModel):
    QueueName: str
    Attributes: Optional[Mapping[QueueAttributeNameType, str]] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteMessageBatchRequestEntryTypeDef(BaseValidatorModel):
    Id: str
    ReceiptHandle: str

class DeleteMessageBatchResultEntryTypeDef(BaseValidatorModel):
    Id: str

class DeleteMessageRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    ReceiptHandle: str

class DeleteQueueRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str

class GetQueueAttributesRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    AttributeNames: Optional[Sequence[QueueAttributeFilterType]] = None

class GetQueueUrlRequestRequestTypeDef(BaseValidatorModel):
    QueueName: str
    QueueOwnerAWSAccountId: Optional[str] = None

class GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef(BaseValidatorModel):
    QueueName: str
    QueueOwnerAWSAccountId: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDeadLetterSourceQueuesRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMessageMoveTasksRequestRequestTypeDef(BaseValidatorModel):
    SourceArn: str
    MaxResults: Optional[int] = None

class ListMessageMoveTasksResultEntryTypeDef(BaseValidatorModel):
    TaskHandle: Optional[str] = None
    Status: Optional[str] = None
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    MaxNumberOfMessagesPerSecond: Optional[int] = None
    ApproximateNumberOfMessagesMoved: Optional[int] = None
    ApproximateNumberOfMessagesToMove: Optional[int] = None
    FailureReason: Optional[str] = None
    StartedTimestamp: Optional[int] = None

class ListQueueTagsRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str

class ListQueuesRequestRequestTypeDef(BaseValidatorModel):
    QueueNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MessageAttributeValueExtraOutputTypeDef(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[bytes] = None
    StringListValues: Optional[List[str]] = None
    BinaryListValues: Optional[List[bytes]] = None

class MessageAttributeValueOutputTypeDef(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[bytes] = None
    StringListValues: Optional[List[str]] = None
    BinaryListValues: Optional[List[bytes]] = None

class PurgeQueueRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str

class ReceiveMessageRequestQueueReceiveMessagesTypeDef(BaseValidatorModel):
    AttributeNames: Optional[Sequence[QueueAttributeFilterType]] = None
    MessageSystemAttributeNames: Optional[Sequence[MessageSystemAttributeNameType]] = None
    MessageAttributeNames: Optional[Sequence[str]] = None
    MaxNumberOfMessages: Optional[int] = None
    VisibilityTimeout: Optional[int] = None
    WaitTimeSeconds: Optional[int] = None
    ReceiveRequestAttemptId: Optional[str] = None

class ReceiveMessageRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    AttributeNames: Optional[Sequence[QueueAttributeFilterType]] = None
    MessageSystemAttributeNames: Optional[Sequence[MessageSystemAttributeNameType]] = None
    MessageAttributeNames: Optional[Sequence[str]] = None
    MaxNumberOfMessages: Optional[int] = None
    VisibilityTimeout: Optional[int] = None
    WaitTimeSeconds: Optional[int] = None
    ReceiveRequestAttemptId: Optional[str] = None

class RemovePermissionRequestQueueRemovePermissionTypeDef(BaseValidatorModel):
    Label: str

class RemovePermissionRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    Label: str

class SendMessageBatchResultEntryTypeDef(BaseValidatorModel):
    Id: str
    MessageId: str
    MD5OfMessageBody: str
    MD5OfMessageAttributes: Optional[str] = None
    MD5OfMessageSystemAttributes: Optional[str] = None
    SequenceNumber: Optional[str] = None

class SetQueueAttributesRequestQueueSetAttributesTypeDef(BaseValidatorModel):
    Attributes: Mapping[QueueAttributeNameType, str]

class SetQueueAttributesRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    Attributes: Mapping[QueueAttributeNameType, str]

class StartMessageMoveTaskRequestRequestTypeDef(BaseValidatorModel):
    SourceArn: str
    DestinationArn: Optional[str] = None
    MaxNumberOfMessagesPerSecond: Optional[int] = None

class TagQueueRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    Tags: Mapping[str, str]

class UntagQueueRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    TagKeys: Sequence[str]

class MessageAttributeValueTypeDef(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[BlobTypeDef] = None
    StringListValues: Optional[Sequence[str]] = None
    BinaryListValues: Optional[Sequence[BlobTypeDef]] = None

class MessageSystemAttributeValueTypeDef(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[BlobTypeDef] = None
    StringListValues: Optional[Sequence[str]] = None
    BinaryListValues: Optional[Sequence[BlobTypeDef]] = None

class CancelMessageMoveTaskResultTypeDef(BaseValidatorModel):
    ApproximateNumberOfMessagesMoved: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueResultTypeDef(BaseValidatorModel):
    QueueUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueAttributesResultTypeDef(BaseValidatorModel):
    Attributes: Dict[QueueAttributeNameType, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueueUrlResultTypeDef(BaseValidatorModel):
    QueueUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeadLetterSourceQueuesResultTypeDef(BaseValidatorModel):
    queueUrls: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQueueTagsResultTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueuesResultTypeDef(BaseValidatorModel):
    QueueUrls: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SendMessageResultTypeDef(BaseValidatorModel):
    MD5OfMessageBody: str
    MD5OfMessageAttributes: str
    MD5OfMessageSystemAttributes: str
    MessageId: str
    SequenceNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMessageMoveTaskResultTypeDef(BaseValidatorModel):
    TaskHandle: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef(BaseValidatorModel):
    Entries: Sequence[ChangeMessageVisibilityBatchRequestEntryTypeDef]

class ChangeMessageVisibilityBatchRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    Entries: Sequence[ChangeMessageVisibilityBatchRequestEntryTypeDef]

class ChangeMessageVisibilityBatchResultTypeDef(BaseValidatorModel):
    Successful: List[ChangeMessageVisibilityBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMessageBatchRequestQueueDeleteMessagesTypeDef(BaseValidatorModel):
    Entries: Sequence[DeleteMessageBatchRequestEntryTypeDef]

class DeleteMessageBatchRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    Entries: Sequence[DeleteMessageBatchRequestEntryTypeDef]

class DeleteMessageBatchResultTypeDef(BaseValidatorModel):
    Successful: List[DeleteMessageBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeadLetterSourceQueuesRequestListDeadLetterSourceQueuesPaginateTypeDef(BaseValidatorModel):
    QueueUrl: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueuesRequestListQueuesPaginateTypeDef(BaseValidatorModel):
    QueueNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMessageMoveTasksResultTypeDef(BaseValidatorModel):
    Results: List[ListMessageMoveTasksResultEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MessageTypeDef(BaseValidatorModel):
    MessageId: Optional[str] = None
    ReceiptHandle: Optional[str] = None
    MD5OfBody: Optional[str] = None
    Body: Optional[str] = None
    Attributes: Optional[Dict[MessageSystemAttributeNameType, str]] = None
    MD5OfMessageAttributes: Optional[str] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValueOutputTypeDef]] = None

class SendMessageBatchResultTypeDef(BaseValidatorModel):
    Successful: List[SendMessageBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendMessageBatchRequestEntryTypeDef(BaseValidatorModel):
    Id: str
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageSystemAttributes: Optional[       Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None

class SendMessageRequestQueueSendMessageTypeDef(BaseValidatorModel):
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageSystemAttributes: Optional[       Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None

class ReceiveMessageResultTypeDef(BaseValidatorModel):
    Messages: List[MessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendMessageRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    MessageBody: str
    DelaySeconds: Optional[int] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueUnionTypeDef]] = None
    MessageSystemAttributes: Optional[       Mapping[Literal["AWSTraceHeader"], MessageSystemAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None

class SendMessageBatchRequestQueueSendMessagesTypeDef(BaseValidatorModel):
    Entries: Sequence[SendMessageBatchRequestEntryTypeDef]

class SendMessageBatchRequestRequestTypeDef(BaseValidatorModel):
    QueueUrl: str
    Entries: Sequence[SendMessageBatchRequestEntryTypeDef]

