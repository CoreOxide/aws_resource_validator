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
from aws_resource_validator.pydantic_models.kinesis_constants import *

class AddTagsToStreamInputRequestTypeDef(BaseModel):
    Tags: Mapping[str, str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class HashKeyRangeTypeDef(BaseModel):
    StartingHashKey: str
    EndingHashKey: str

class ConsumerDescriptionTypeDef(BaseModel):
    ConsumerName: str
    ConsumerARN: str
    ConsumerStatus: ConsumerStatusType
    ConsumerCreationTimestamp: datetime
    StreamARN: str

class ConsumerTypeDef(BaseModel):
    ConsumerName: str
    ConsumerARN: str
    ConsumerStatus: ConsumerStatusType
    ConsumerCreationTimestamp: datetime

class StreamModeDetailsTypeDef(BaseModel):
    StreamMode: StreamModeType

class DecreaseStreamRetentionPeriodInputRequestTypeDef(BaseModel):
    RetentionPeriodHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class DeleteResourcePolicyInputRequestTypeDef(BaseModel):
    ResourceARN: str

class DeleteStreamInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    EnforceConsumerDeletion: Optional[bool] = None
    StreamARN: Optional[str] = None

class DeregisterStreamConsumerInputRequestTypeDef(BaseModel):
    StreamARN: Optional[str] = None
    ConsumerName: Optional[str] = None
    ConsumerARN: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeStreamConsumerInputRequestTypeDef(BaseModel):
    StreamARN: Optional[str] = None
    ConsumerName: Optional[str] = None
    ConsumerARN: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeStreamInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamARN: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeStreamSummaryInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class DisableEnhancedMonitoringInputRequestTypeDef(BaseModel):
    ShardLevelMetrics: Sequence[MetricsNameType]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class EnableEnhancedMonitoringInputRequestTypeDef(BaseModel):
    ShardLevelMetrics: Sequence[MetricsNameType]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class EnhancedMetricsTypeDef(BaseModel):
    ShardLevelMetrics: Optional[List[MetricsNameType]] = None

class GetRecordsInputRequestTypeDef(BaseModel):
    ShardIterator: str
    Limit: Optional[int] = None
    StreamARN: Optional[str] = None

class RecordTypeDef(BaseModel):
    SequenceNumber: str
    Data: bytes
    PartitionKey: str
    ApproximateArrivalTimestamp: Optional[datetime] = None
    EncryptionType: Optional[EncryptionTypeType] = None

class GetResourcePolicyInputRequestTypeDef(BaseModel):
    ResourceARN: str

class IncreaseStreamRetentionPeriodInputRequestTypeDef(BaseModel):
    RetentionPeriodHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class InternalFailureExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class KMSAccessDeniedExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class KMSDisabledExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class KMSInvalidStateExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class KMSNotFoundExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class KMSOptInRequiredTypeDef(BaseModel):
    message: Optional[str] = None

class KMSThrottlingExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class ListStreamsInputRequestTypeDef(BaseModel):
    Limit: Optional[int] = None
    ExclusiveStartStreamName: Optional[str] = None
    NextToken: Optional[str] = None

class ListTagsForStreamInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    ExclusiveStartTagKey: Optional[str] = None
    Limit: Optional[int] = None
    StreamARN: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class MergeShardsInputRequestTypeDef(BaseModel):
    ShardToMerge: str
    AdjacentShardToMerge: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class PutRecordsResultEntryTypeDef(BaseModel):
    SequenceNumber: Optional[str] = None
    ShardId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class PutResourcePolicyInputRequestTypeDef(BaseModel):
    ResourceARN: str
    Policy: str

class RegisterStreamConsumerInputRequestTypeDef(BaseModel):
    StreamARN: str
    ConsumerName: str

class RemoveTagsFromStreamInputRequestTypeDef(BaseModel):
    TagKeys: Sequence[str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class ResourceInUseExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class ResourceNotFoundExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class SequenceNumberRangeTypeDef(BaseModel):
    StartingSequenceNumber: str
    EndingSequenceNumber: Optional[str] = None

class SplitShardInputRequestTypeDef(BaseModel):
    ShardToSplit: str
    NewStartingHashKey: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class StartStreamEncryptionInputRequestTypeDef(BaseModel):
    EncryptionType: EncryptionTypeType
    KeyId: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class StopStreamEncryptionInputRequestTypeDef(BaseModel):
    EncryptionType: EncryptionTypeType
    KeyId: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class UpdateShardCountInputRequestTypeDef(BaseModel):
    TargetShardCount: int
    ScalingType: Literal["UNIFORM_SCALING"]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class PutRecordInputRequestTypeDef(BaseModel):
    Data: BlobTypeDef
    PartitionKey: str
    StreamName: Optional[str] = None
    ExplicitHashKey: Optional[str] = None
    SequenceNumberForOrdering: Optional[str] = None
    StreamARN: Optional[str] = None

class PutRecordsRequestEntryTypeDef(BaseModel):
    Data: BlobTypeDef
    PartitionKey: str
    ExplicitHashKey: Optional[str] = None

class ChildShardTypeDef(BaseModel):
    ShardId: str
    ParentShards: List[str]
    HashKeyRange: HashKeyRangeTypeDef

class CreateStreamInputRequestTypeDef(BaseModel):
    StreamName: str
    ShardCount: Optional[int] = None
    StreamModeDetails: Optional[StreamModeDetailsTypeDef] = None

class StreamSummaryTypeDef(BaseModel):
    StreamName: str
    StreamARN: str
    StreamStatus: StreamStatusType
    StreamModeDetails: Optional[StreamModeDetailsTypeDef] = None
    StreamCreationTimestamp: Optional[datetime] = None

class UpdateStreamModeInputRequestTypeDef(BaseModel):
    StreamARN: str
    StreamModeDetails: StreamModeDetailsTypeDef

class DescribeLimitsOutputTypeDef(BaseModel):
    ShardLimit: int
    OpenShardCount: int
    OnDemandStreamCount: int
    OnDemandStreamCountLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStreamConsumerOutputTypeDef(BaseModel):
    ConsumerDescription: ConsumerDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnhancedMonitoringOutputTypeDef(BaseModel):
    StreamName: str
    CurrentShardLevelMetrics: List[MetricsNameType]
    DesiredShardLevelMetrics: List[MetricsNameType]
    StreamARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyOutputTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetShardIteratorOutputTypeDef(BaseModel):
    ShardIterator: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamConsumersOutputTypeDef(BaseModel):
    Consumers: List[ConsumerTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordOutputTypeDef(BaseModel):
    ShardId: str
    SequenceNumber: str
    EncryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterStreamConsumerOutputTypeDef(BaseModel):
    Consumer: ConsumerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateShardCountOutputTypeDef(BaseModel):
    StreamName: str
    CurrentShardCount: int
    TargetShardCount: int
    StreamARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStreamInputDescribeStreamPaginateTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamsInputListStreamsPaginateTypeDef(BaseModel):
    ExclusiveStartStreamName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStreamInputStreamExistsWaitTypeDef(BaseModel):
    StreamName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamARN: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStreamInputStreamNotExistsWaitTypeDef(BaseModel):
    StreamName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamARN: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class StreamDescriptionSummaryTypeDef(BaseModel):
    StreamName: str
    StreamARN: str
    StreamStatus: StreamStatusType
    RetentionPeriodHours: int
    StreamCreationTimestamp: datetime
    EnhancedMonitoring: List[EnhancedMetricsTypeDef]
    OpenShardCount: int
    StreamModeDetails: Optional[StreamModeDetailsTypeDef] = None
    EncryptionType: Optional[EncryptionTypeType] = None
    KeyId: Optional[str] = None
    ConsumerCount: Optional[int] = None

class GetShardIteratorInputRequestTypeDef(BaseModel):
    ShardId: str
    ShardIteratorType: ShardIteratorTypeType
    StreamName: Optional[str] = None
    StartingSequenceNumber: Optional[str] = None
    Timestamp: Optional[TimestampTypeDef] = None
    StreamARN: Optional[str] = None

class ListStreamConsumersInputListStreamConsumersPaginateTypeDef(BaseModel):
    StreamARN: str
    StreamCreationTimestamp: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamConsumersInputRequestTypeDef(BaseModel):
    StreamARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StreamCreationTimestamp: Optional[TimestampTypeDef] = None

class ShardFilterTypeDef(BaseModel):
    Type: ShardFilterTypeType
    ShardId: Optional[str] = None
    Timestamp: Optional[TimestampTypeDef] = None

class StartingPositionTypeDef(BaseModel):
    Type: ShardIteratorTypeType
    SequenceNumber: Optional[str] = None
    Timestamp: Optional[TimestampTypeDef] = None

class ListTagsForStreamOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    HasMoreTags: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordsOutputTypeDef(BaseModel):
    FailedRecordCount: int
    Records: List[PutRecordsResultEntryTypeDef]
    EncryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ShardTypeDef(BaseModel):
    ShardId: str
    HashKeyRange: HashKeyRangeTypeDef
    SequenceNumberRange: SequenceNumberRangeTypeDef
    ParentShardId: Optional[str] = None
    AdjacentParentShardId: Optional[str] = None

class PutRecordsInputRequestTypeDef(BaseModel):
    Records: Sequence[PutRecordsRequestEntryTypeDef]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class GetRecordsOutputTypeDef(BaseModel):
    Records: List[RecordTypeDef]
    NextShardIterator: str
    MillisBehindLatest: int
    ChildShards: List[ChildShardTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribeToShardEventTypeDef(BaseModel):
    Records: List[RecordTypeDef]
    ContinuationSequenceNumber: str
    MillisBehindLatest: int
    ChildShards: Optional[List[ChildShardTypeDef]] = None

class ListStreamsOutputTypeDef(BaseModel):
    StreamNames: List[str]
    HasMoreStreams: bool
    NextToken: str
    StreamSummaries: List[StreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStreamSummaryOutputTypeDef(BaseModel):
    StreamDescriptionSummary: StreamDescriptionSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListShardsInputListShardsPaginateTypeDef(BaseModel):
    StreamName: Optional[str] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamCreationTimestamp: Optional[TimestampTypeDef] = None
    ShardFilter: Optional[ShardFilterTypeDef] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListShardsInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    NextToken: Optional[str] = None
    ExclusiveStartShardId: Optional[str] = None
    MaxResults: Optional[int] = None
    StreamCreationTimestamp: Optional[TimestampTypeDef] = None
    ShardFilter: Optional[ShardFilterTypeDef] = None
    StreamARN: Optional[str] = None

class SubscribeToShardInputRequestTypeDef(BaseModel):
    ConsumerARN: str
    ShardId: str
    StartingPosition: StartingPositionTypeDef

class ListShardsOutputTypeDef(BaseModel):
    Shards: List[ShardTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StreamDescriptionTypeDef(BaseModel):
    StreamName: str
    StreamARN: str
    StreamStatus: StreamStatusType
    Shards: List[ShardTypeDef]
    HasMoreShards: bool
    RetentionPeriodHours: int
    StreamCreationTimestamp: datetime
    EnhancedMonitoring: List[EnhancedMetricsTypeDef]
    StreamModeDetails: Optional[StreamModeDetailsTypeDef] = None
    EncryptionType: Optional[EncryptionTypeType] = None
    KeyId: Optional[str] = None

class SubscribeToShardEventStreamTypeDef(BaseModel):
    SubscribeToShardEvent: SubscribeToShardEventTypeDef
    ResourceNotFoundException: Optional[ResourceNotFoundExceptionTypeDef] = None
    ResourceInUseException: Optional[ResourceInUseExceptionTypeDef] = None
    KMSDisabledException: Optional[KMSDisabledExceptionTypeDef] = None
    KMSInvalidStateException: Optional[KMSInvalidStateExceptionTypeDef] = None
    KMSAccessDeniedException: Optional[KMSAccessDeniedExceptionTypeDef] = None
    KMSNotFoundException: Optional[KMSNotFoundExceptionTypeDef] = None
    KMSOptInRequired: Optional[KMSOptInRequiredTypeDef] = None
    KMSThrottlingException: Optional[KMSThrottlingExceptionTypeDef] = None
    InternalFailureException: Optional[InternalFailureExceptionTypeDef] = None

class DescribeStreamOutputTypeDef(BaseModel):
    StreamDescription: StreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribeToShardOutputTypeDef(BaseModel):
    EventStream: "EventStream[SubscribeToShardEventStreamTypeDef]"
    ResponseMetadata: ResponseMetadataTypeDef

