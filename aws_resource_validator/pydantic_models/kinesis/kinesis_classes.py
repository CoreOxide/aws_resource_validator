from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.kinesis.kinesis_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'add_tags_to_stream' function.
class AddTagsToStreamInput(BaseValidatorModel):
    Tags: Dict[str, str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


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


# This class is the input for the 'decrease_stream_retention_period' function.
class DecreaseStreamRetentionPeriodInput(BaseValidatorModel):
    RetentionPeriodHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyInput(BaseValidatorModel):
    ResourceARN: str


# This class is the input for the 'delete_stream' function.
class DeleteStreamInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    EnforceConsumerDeletion: Optional[bool] = None
    StreamARN: Optional[str] = None


# This class is the input for the 'deregister_stream_consumer' function.
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


# This class is the input for the 'describe_stream_consumer' function.
class DescribeStreamConsumerInput(BaseValidatorModel):
    StreamARN: Optional[str] = None
    ConsumerName: Optional[str] = None
    ConsumerARN: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_stream' function.
class DescribeStreamInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamARN: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_stream_summary' function.
class DescribeStreamSummaryInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


# This class is the input for the 'disable_enhanced_monitoring' function.
class DisableEnhancedMonitoringInput(BaseValidatorModel):
    ShardLevelMetrics: List[MetricsNameType]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


# This class is the input for the 'enable_enhanced_monitoring' function.
class EnableEnhancedMonitoringInput(BaseValidatorModel):
    ShardLevelMetrics: List[MetricsNameType]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class EnhancedMetrics(BaseValidatorModel):
    ShardLevelMetrics: Optional[List[MetricsNameType]] = None


# This class is the input for the 'get_records' function.
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


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyInput(BaseValidatorModel):
    ResourceARN: str

Timestamp = Union[datetime, str]


# This class is the input for the 'increase_stream_retention_period' function.
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


# This class is the input for the 'list_streams' function.
class ListStreamsInput(BaseValidatorModel):
    Limit: Optional[int] = None
    ExclusiveStartStreamName: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_stream' function.
class ListTagsForStreamInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    ExclusiveStartTagKey: Optional[str] = None
    Limit: Optional[int] = None
    StreamARN: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


# This class is the input for the 'merge_shards' function.
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


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyInput(BaseValidatorModel):
    ResourceARN: str
    Policy: str


# This class is the input for the 'register_stream_consumer' function.
class RegisterStreamConsumerInput(BaseValidatorModel):
    StreamARN: str
    ConsumerName: str


# This class is the input for the 'remove_tags_from_stream' function.
class RemoveTagsFromStreamInput(BaseValidatorModel):
    TagKeys: List[str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class ResourceInUseException(BaseValidatorModel):
    message: Optional[str] = None


class ResourceNotFoundException(BaseValidatorModel):
    message: Optional[str] = None


class SequenceNumberRange(BaseValidatorModel):
    StartingSequenceNumber: str
    EndingSequenceNumber: Optional[str] = None


# This class is the input for the 'split_shard' function.
class SplitShardInput(BaseValidatorModel):
    ShardToSplit: str
    NewStartingHashKey: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


# This class is the input for the 'start_stream_encryption' function.
class StartStreamEncryptionInput(BaseValidatorModel):
    EncryptionType: EncryptionTypeType
    KeyId: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


# This class is the input for the 'stop_stream_encryption' function.
class StopStreamEncryptionInput(BaseValidatorModel):
    EncryptionType: EncryptionTypeType
    KeyId: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


# This class is the input for the 'update_shard_count' function.
class UpdateShardCountInput(BaseValidatorModel):
    TargetShardCount: int
    ScalingType: Literal['UNIFORM_SCALING']
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


# This class is the input for the 'put_record' function.
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


# This class is the input for the 'create_stream' function.
class CreateStreamInput(BaseValidatorModel):
    StreamName: str
    ShardCount: Optional[int] = None
    StreamModeDetails: Optional[StreamModeDetails] = None
    Tags: Optional[Dict[str, str]] = None


class StreamSummary(BaseValidatorModel):
    StreamName: str
    StreamARN: str
    StreamStatus: StreamStatusType
    StreamModeDetails: Optional[StreamModeDetails] = None
    StreamCreationTimestamp: Optional[datetime] = None


# This class is the input for the 'update_stream_mode' function.
class UpdateStreamModeInput(BaseValidatorModel):
    StreamARN: str
    StreamModeDetails: StreamModeDetails


class DescribeLimitsOutput(BaseValidatorModel):
    ShardLimit: int
    OpenShardCount: int
    OnDemandStreamCount: int
    OnDemandStreamCountLimit: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_stream_consumer' function.
class DescribeStreamConsumerOutput(BaseValidatorModel):
    ConsumerDescription: ConsumerDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_stream_mode' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_enhanced_monitoring' function.
class EnhancedMonitoringOutput(BaseValidatorModel):
    StreamName: str
    CurrentShardLevelMetrics: List[MetricsNameType]
    DesiredShardLevelMetrics: List[MetricsNameType]
    StreamARN: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_shard_iterator' function.
class GetShardIteratorOutput(BaseValidatorModel):
    ShardIterator: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_stream_consumers' function.
class ListStreamConsumersOutput(BaseValidatorModel):
    Consumers: List[Consumer]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_record' function.
class PutRecordOutput(BaseValidatorModel):
    ShardId: str
    SequenceNumber: str
    EncryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_stream_consumer' function.
class RegisterStreamConsumerOutput(BaseValidatorModel):
    Consumer: Consumer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_shard_count' function.
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


# This class is the input for the 'get_shard_iterator' function.
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


# This class is the input for the 'list_stream_consumers' function.
class ListStreamConsumersInput(BaseValidatorModel):
    StreamARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StreamCreationTimestamp: Optional[Timestamp] = None


class ShardFilter(BaseValidatorModel):
    Type: ShardFilterTypeType
    ShardId: Optional[str] = None
    Timestamp: Optional[Timestamp] = None


class StartingPosition(BaseValidatorModel):
    Type: ShardIteratorTypeType
    SequenceNumber: Optional[str] = None
    Timestamp: Optional[Timestamp] = None


# This class is the output for the 'list_tags_for_stream' function.
class ListTagsForStreamOutput(BaseValidatorModel):
    Tags: List[Tag]
    HasMoreTags: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_records' function.
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


# This class is the input for the 'put_records' function.
class PutRecordsInput(BaseValidatorModel):
    Records: List[PutRecordsRequestEntry]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


# This class is the output for the 'get_records' function.
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


# This class is the output for the 'list_streams' function.
class ListStreamsOutput(BaseValidatorModel):
    StreamNames: List[str]
    HasMoreStreams: bool
    StreamSummaries: List[StreamSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_stream_summary' function.
class DescribeStreamSummaryOutput(BaseValidatorModel):
    StreamDescriptionSummary: StreamDescriptionSummary
    ResponseMetadata: ResponseMetadata


class ListShardsInputPaginate(BaseValidatorModel):
    StreamName: Optional[str] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamCreationTimestamp: Optional[Timestamp] = None
    ShardFilter: Optional[ShardFilter] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_shards' function.
class ListShardsInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    NextToken: Optional[str] = None
    ExclusiveStartShardId: Optional[str] = None
    MaxResults: Optional[int] = None
    StreamCreationTimestamp: Optional[Timestamp] = None
    ShardFilter: Optional[ShardFilter] = None
    StreamARN: Optional[str] = None


# This class is the input for the 'subscribe_to_shard' function.
class SubscribeToShardInput(BaseValidatorModel):
    ConsumerARN: str
    ShardId: str
    StartingPosition: StartingPosition


# This class is the output for the 'list_shards' function.
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


# This class is the output for the 'describe_stream' function.
class DescribeStreamOutput(BaseValidatorModel):
    StreamDescription: StreamDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'subscribe_to_shard' function.
class SubscribeToShardOutput(BaseValidatorModel):
    EventStream: EventStream[SubscribeToShardEventStream]
