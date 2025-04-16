from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel, EventStream
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
from aws_resource_validator.pydantic_models.kinesis_constants import *

class AddTagsToStreamInput(BaseValidatorModel):
    Tags: Mapping[str, str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class HashKeyRange(BaseValidatorModel):
    StartingHashKey: str
    EndingHashKey: str


class ConsumerDescription(BaseValidatorModel):
    ConsumerName: str
    ConsumerARN: str
    ConsumerStatus: ConsumerStatusType
    ConsumerCreationTimestamp: datetime
    StreamARN: str


class Consumer(BaseValidatorModel):
    ConsumerName: str
    ConsumerARN: str
    ConsumerStatus: ConsumerStatusType
    ConsumerCreationTimestamp: datetime


class StreamModeDetails(BaseValidatorModel):
    StreamMode: StreamModeType


class DecreaseStreamRetentionPeriodInput(BaseValidatorModel):
    RetentionPeriodHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class DeleteResourcePolicyInput(BaseValidatorModel):
    ResourceARN: str


class DeleteStreamInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    EnforceConsumerDeletion: Optional[bool] = None
    StreamARN: Optional[str] = None


class DeregisterStreamConsumerInput(BaseValidatorModel):
    StreamARN: Optional[str] = None
    ConsumerName: Optional[str] = None
    ConsumerARN: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DescribeStreamConsumerInput(BaseValidatorModel):
    StreamARN: Optional[str] = None
    ConsumerName: Optional[str] = None
    ConsumerARN: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeStreamInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamARN: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeStreamSummaryInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class DisableEnhancedMonitoringInput(BaseValidatorModel):
    ShardLevelMetrics: Sequence[MetricsNameType]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class EnableEnhancedMonitoringInput(BaseValidatorModel):
    ShardLevelMetrics: Sequence[MetricsNameType]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class EnhancedMetrics(BaseValidatorModel):
    ShardLevelMetrics: Optional[List[MetricsNameType]] = None


class GetRecordsInput(BaseValidatorModel):
    ShardIterator: str
    Limit: Optional[int] = None
    StreamARN: Optional[str] = None


class Record(BaseValidatorModel):
    SequenceNumber: str
    Data: bytes
    PartitionKey: str
    ApproximateArrivalTimestamp: Optional[datetime] = None
    EncryptionType: Optional[EncryptionTypeType] = None


class GetResourcePolicyInput(BaseValidatorModel):
    ResourceARN: str


class IncreaseStreamRetentionPeriodInput(BaseValidatorModel):
    RetentionPeriodHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class InternalFailureException(BaseValidatorModel):
    message: Optional[str] = None


class KMSAccessDeniedException(BaseValidatorModel):
    message: Optional[str] = None


class KMSDisabledException(BaseValidatorModel):
    message: Optional[str] = None


class KMSInvalidStateException(BaseValidatorModel):
    message: Optional[str] = None


class KMSNotFoundException(BaseValidatorModel):
    message: Optional[str] = None


class KMSOptInRequired(BaseValidatorModel):
    message: Optional[str] = None


class KMSThrottlingException(BaseValidatorModel):
    message: Optional[str] = None


class ListStreamsInput(BaseValidatorModel):
    Limit: Optional[int] = None
    ExclusiveStartStreamName: Optional[str] = None
    NextToken: Optional[str] = None


class ListTagsForStreamInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    ExclusiveStartTagKey: Optional[str] = None
    Limit: Optional[int] = None
    StreamARN: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class MergeShardsInput(BaseValidatorModel):
    ShardToMerge: str
    AdjacentShardToMerge: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class PutRecordsResultEntry(BaseValidatorModel):
    SequenceNumber: Optional[str] = None
    ShardId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class PutResourcePolicyInput(BaseValidatorModel):
    ResourceARN: str
    Policy: str


class RegisterStreamConsumerInput(BaseValidatorModel):
    StreamARN: str
    ConsumerName: str


class RemoveTagsFromStreamInput(BaseValidatorModel):
    TagKeys: Sequence[str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class ResourceInUseException(BaseValidatorModel):
    message: Optional[str] = None


class ResourceNotFoundException(BaseValidatorModel):
    message: Optional[str] = None


class SequenceNumberRange(BaseValidatorModel):
    StartingSequenceNumber: str
    EndingSequenceNumber: Optional[str] = None


class SplitShardInput(BaseValidatorModel):
    ShardToSplit: str
    NewStartingHashKey: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class StartStreamEncryptionInput(BaseValidatorModel):
    EncryptionType: EncryptionTypeType
    KeyId: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class StopStreamEncryptionInput(BaseValidatorModel):
    EncryptionType: EncryptionTypeType
    KeyId: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class UpdateShardCountInput(BaseValidatorModel):
    TargetShardCount: int
    ScalingType: Literal["UNIFORM_SCALING"]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class Blob(BaseValidatorModel):
    pass


class PutRecordInput(BaseValidatorModel):
    Data: Blob
    PartitionKey: str
    StreamName: Optional[str] = None
    ExplicitHashKey: Optional[str] = None
    SequenceNumberForOrdering: Optional[str] = None
    StreamARN: Optional[str] = None


class PutRecordsRequestEntry(BaseValidatorModel):
    Data: Blob
    PartitionKey: str
    ExplicitHashKey: Optional[str] = None


class ChildShard(BaseValidatorModel):
    ShardId: str
    ParentShards: List[str]
    HashKeyRange: HashKeyRange


class CreateStreamInput(BaseValidatorModel):
    StreamName: str
    ShardCount: Optional[int] = None
    StreamModeDetails: Optional[StreamModeDetails] = None
    Tags: Optional[Mapping[str, str]] = None


class StreamSummary(BaseValidatorModel):
    StreamName: str
    StreamARN: str
    StreamStatus: StreamStatusType
    StreamModeDetails: Optional[StreamModeDetails] = None
    StreamCreationTimestamp: Optional[datetime] = None


class UpdateStreamModeInput(BaseValidatorModel):
    StreamARN: str
    StreamModeDetails: StreamModeDetails


class DescribeLimitsOutput(BaseValidatorModel):
    ShardLimit: int
    OpenShardCount: int
    OnDemandStreamCount: int
    OnDemandStreamCountLimit: int
    ResponseMetadata: ResponseMetadata


class DescribeStreamConsumerOutput(BaseValidatorModel):
    ConsumerDescription: ConsumerDescription
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class EnhancedMonitoringOutput(BaseValidatorModel):
    StreamName: str
    CurrentShardLevelMetrics: List[MetricsNameType]
    DesiredShardLevelMetrics: List[MetricsNameType]
    StreamARN: str
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetShardIteratorOutput(BaseValidatorModel):
    ShardIterator: str
    ResponseMetadata: ResponseMetadata


class ListStreamConsumersOutput(BaseValidatorModel):
    Consumers: List[Consumer]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutRecordOutput(BaseValidatorModel):
    ShardId: str
    SequenceNumber: str
    EncryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadata


class RegisterStreamConsumerOutput(BaseValidatorModel):
    Consumer: Consumer
    ResponseMetadata: ResponseMetadata


class UpdateShardCountOutput(BaseValidatorModel):
    StreamName: str
    CurrentShardCount: int
    TargetShardCount: int
    StreamARN: str
    ResponseMetadata: ResponseMetadata


class DescribeStreamInputPaginate(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamsInputPaginate(BaseValidatorModel):
    ExclusiveStartStreamName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStreamInputWaitExtra(BaseValidatorModel):
    StreamName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamARN: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStreamInputWait(BaseValidatorModel):
    StreamName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamARN: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class StreamDescriptionSummary(BaseValidatorModel):
    StreamName: str
    StreamARN: str
    StreamStatus: StreamStatusType
    RetentionPeriodHours: int
    StreamCreationTimestamp: datetime
    EnhancedMonitoring: List[EnhancedMetrics]
    OpenShardCount: int
    StreamModeDetails: Optional[StreamModeDetails] = None
    EncryptionType: Optional[EncryptionTypeType] = None
    KeyId: Optional[str] = None
    ConsumerCount: Optional[int] = None


class Timestamp(BaseValidatorModel):
    pass


class GetShardIteratorInput(BaseValidatorModel):
    ShardId: str
    ShardIteratorType: ShardIteratorTypeType
    StreamName: Optional[str] = None
    StartingSequenceNumber: Optional[str] = None
    Timestamp: Optional[Timestamp] = None
    StreamARN: Optional[str] = None


class ListStreamConsumersInputPaginate(BaseValidatorModel):
    StreamARN: str
    StreamCreationTimestamp: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamConsumersInput(BaseValidatorModel):
    StreamARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StreamCreationTimestamp: Optional[Timestamp] = None


class ListTagsForStreamOutput(BaseValidatorModel):
    Tags: List[Tag]
    HasMoreTags: bool
    ResponseMetadata: ResponseMetadata


class PutRecordsOutput(BaseValidatorModel):
    FailedRecordCount: int
    Records: List[PutRecordsResultEntry]
    EncryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadata


class Shard(BaseValidatorModel):
    ShardId: str
    HashKeyRange: HashKeyRange
    SequenceNumberRange: SequenceNumberRange
    ParentShardId: Optional[str] = None
    AdjacentParentShardId: Optional[str] = None


class PutRecordsInput(BaseValidatorModel):
    Records: Sequence[PutRecordsRequestEntry]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class GetRecordsOutput(BaseValidatorModel):
    Records: List[Record]
    NextShardIterator: str
    MillisBehindLatest: int
    ChildShards: List[ChildShard]
    ResponseMetadata: ResponseMetadata


class SubscribeToShardEvent(BaseValidatorModel):
    Records: List[Record]
    ContinuationSequenceNumber: str
    MillisBehindLatest: int
    ChildShards: Optional[List[ChildShard]] = None


class ListStreamsOutput(BaseValidatorModel):
    StreamNames: List[str]
    HasMoreStreams: bool
    StreamSummaries: List[StreamSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeStreamSummaryOutput(BaseValidatorModel):
    StreamDescriptionSummary: StreamDescriptionSummary
    ResponseMetadata: ResponseMetadata


class ShardFilter(BaseValidatorModel):
    pass


class ListShardsInputPaginate(BaseValidatorModel):
    StreamName: Optional[str] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamCreationTimestamp: Optional[Timestamp] = None
    ShardFilter: Optional[ShardFilter] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListShardsInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    NextToken: Optional[str] = None
    ExclusiveStartShardId: Optional[str] = None
    MaxResults: Optional[int] = None
    StreamCreationTimestamp: Optional[Timestamp] = None
    ShardFilter: Optional[ShardFilter] = None
    StreamARN: Optional[str] = None


class StartingPosition(BaseValidatorModel):
    pass


class SubscribeToShardInput(BaseValidatorModel):
    ConsumerARN: str
    ShardId: str
    StartingPosition: StartingPosition


class ListShardsOutput(BaseValidatorModel):
    Shards: List[Shard]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StreamDescription(BaseValidatorModel):
    StreamName: str
    StreamARN: str
    StreamStatus: StreamStatusType
    Shards: List[Shard]
    HasMoreShards: bool
    RetentionPeriodHours: int
    StreamCreationTimestamp: datetime
    EnhancedMonitoring: List[EnhancedMetrics]
    StreamModeDetails: Optional[StreamModeDetails] = None
    EncryptionType: Optional[EncryptionTypeType] = None
    KeyId: Optional[str] = None


class SubscribeToShardEventStream(BaseValidatorModel):
    SubscribeToShardEvent: SubscribeToShardEvent
    ResourceNotFoundException: Optional[ResourceNotFoundException] = None
    ResourceInUseException: Optional[ResourceInUseException] = None
    KMSDisabledException: Optional[KMSDisabledException] = None
    KMSInvalidStateException: Optional[KMSInvalidStateException] = None
    KMSAccessDeniedException: Optional[KMSAccessDeniedException] = None
    KMSNotFoundException: Optional[KMSNotFoundException] = None
    KMSOptInRequired: Optional[KMSOptInRequired] = None
    KMSThrottlingException: Optional[KMSThrottlingException] = None
    InternalFailureException: Optional[InternalFailureException] = None


class DescribeStreamOutput(BaseValidatorModel):
    StreamDescription: StreamDescription
    ResponseMetadata: ResponseMetadata


class SubscribeToShardOutput(BaseValidatorModel):
    EventStream: EventStream[SubscribeToShardEventStream]
    ResponseMetadata: ResponseMetadata


