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
from aws_resource_validator.pydantic_models.kinesis_constants import *

class AddTagsToStreamInputRequestTypeDef(BaseValidatorModel):
    Tags: Mapping[str, str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class HashKeyRangeTypeDef(BaseValidatorModel):
    StartingHashKey: str
    EndingHashKey: str

class ConsumerDescriptionTypeDef(BaseValidatorModel):
    ConsumerName: str
    ConsumerARN: str
    ConsumerStatus: ConsumerStatusType
    ConsumerCreationTimestamp: datetime
    StreamARN: str

class ConsumerTypeDef(BaseValidatorModel):
    ConsumerName: str
    ConsumerARN: str
    ConsumerStatus: ConsumerStatusType
    ConsumerCreationTimestamp: datetime

class StreamModeDetailsTypeDef(BaseValidatorModel):
    StreamMode: StreamModeType

class DecreaseStreamRetentionPeriodInputRequestTypeDef(BaseValidatorModel):
    RetentionPeriodHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class DeleteResourcePolicyInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class DeleteStreamInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    EnforceConsumerDeletion: Optional[bool] = None
    StreamARN: Optional[str] = None

class DeregisterStreamConsumerInputRequestTypeDef(BaseValidatorModel):
    StreamARN: Optional[str] = None
    ConsumerName: Optional[str] = None
    ConsumerARN: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeStreamConsumerInputRequestTypeDef(BaseValidatorModel):
    StreamARN: Optional[str] = None
    ConsumerName: Optional[str] = None
    ConsumerARN: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeStreamInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamARN: Optional[str] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeStreamSummaryInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class DisableEnhancedMonitoringInputRequestTypeDef(BaseValidatorModel):
    ShardLevelMetrics: Sequence[MetricsNameType]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class EnableEnhancedMonitoringInputRequestTypeDef(BaseValidatorModel):
    ShardLevelMetrics: Sequence[MetricsNameType]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class EnhancedMetricsTypeDef(BaseValidatorModel):
    ShardLevelMetrics: Optional[List[MetricsNameType]] = None

class GetRecordsInputRequestTypeDef(BaseValidatorModel):
    ShardIterator: str
    Limit: Optional[int] = None
    StreamARN: Optional[str] = None

class RecordTypeDef(BaseValidatorModel):
    SequenceNumber: str
    Data: bytes
    PartitionKey: str
    ApproximateArrivalTimestamp: Optional[datetime] = None
    EncryptionType: Optional[EncryptionTypeType] = None

class GetResourcePolicyInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class IncreaseStreamRetentionPeriodInputRequestTypeDef(BaseValidatorModel):
    RetentionPeriodHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class InternalFailureExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class KMSAccessDeniedExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class KMSDisabledExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class KMSInvalidStateExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class KMSNotFoundExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class KMSOptInRequiredTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class KMSThrottlingExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class ListStreamsInputRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    ExclusiveStartStreamName: Optional[str] = None
    NextToken: Optional[str] = None

class ListTagsForStreamInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    ExclusiveStartTagKey: Optional[str] = None
    Limit: Optional[int] = None
    StreamARN: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class MergeShardsInputRequestTypeDef(BaseValidatorModel):
    ShardToMerge: str
    AdjacentShardToMerge: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class PutRecordsResultEntryTypeDef(BaseValidatorModel):
    SequenceNumber: Optional[str] = None
    ShardId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class PutResourcePolicyInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Policy: str

class RegisterStreamConsumerInputRequestTypeDef(BaseValidatorModel):
    StreamARN: str
    ConsumerName: str

class RemoveTagsFromStreamInputRequestTypeDef(BaseValidatorModel):
    TagKeys: Sequence[str]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class ResourceInUseExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class ResourceNotFoundExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class SequenceNumberRangeTypeDef(BaseValidatorModel):
    StartingSequenceNumber: str
    EndingSequenceNumber: Optional[str] = None

class SplitShardInputRequestTypeDef(BaseValidatorModel):
    ShardToSplit: str
    NewStartingHashKey: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class StartStreamEncryptionInputRequestTypeDef(BaseValidatorModel):
    EncryptionType: EncryptionTypeType
    KeyId: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class StopStreamEncryptionInputRequestTypeDef(BaseValidatorModel):
    EncryptionType: EncryptionTypeType
    KeyId: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class UpdateShardCountInputRequestTypeDef(BaseValidatorModel):
    TargetShardCount: int
    ScalingType: Literal["UNIFORM_SCALING"]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class PutRecordInputRequestTypeDef(BaseValidatorModel):
    Data: BlobTypeDef
    PartitionKey: str
    StreamName: Optional[str] = None
    ExplicitHashKey: Optional[str] = None
    SequenceNumberForOrdering: Optional[str] = None
    StreamARN: Optional[str] = None

class PutRecordsRequestEntryTypeDef(BaseValidatorModel):
    Data: BlobTypeDef
    PartitionKey: str
    ExplicitHashKey: Optional[str] = None

class ChildShardTypeDef(BaseValidatorModel):
    ShardId: str
    ParentShards: List[str]
    HashKeyRange: HashKeyRangeTypeDef

class CreateStreamInputRequestTypeDef(BaseValidatorModel):
    StreamName: str
    ShardCount: Optional[int] = None
    StreamModeDetails: Optional[StreamModeDetailsTypeDef] = None

class StreamSummaryTypeDef(BaseValidatorModel):
    StreamName: str
    StreamARN: str
    StreamStatus: StreamStatusType
    StreamModeDetails: Optional[StreamModeDetailsTypeDef] = None
    StreamCreationTimestamp: Optional[datetime] = None

class UpdateStreamModeInputRequestTypeDef(BaseValidatorModel):
    StreamARN: str
    StreamModeDetails: StreamModeDetailsTypeDef

class DescribeLimitsOutputTypeDef(BaseValidatorModel):
    ShardLimit: int
    OpenShardCount: int
    OnDemandStreamCount: int
    OnDemandStreamCountLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStreamConsumerOutputTypeDef(BaseValidatorModel):
    ConsumerDescription: ConsumerDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnhancedMonitoringOutputTypeDef(BaseValidatorModel):
    StreamName: str
    CurrentShardLevelMetrics: List[MetricsNameType]
    DesiredShardLevelMetrics: List[MetricsNameType]
    StreamARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyOutputTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetShardIteratorOutputTypeDef(BaseValidatorModel):
    ShardIterator: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamConsumersOutputTypeDef(BaseValidatorModel):
    Consumers: List[ConsumerTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordOutputTypeDef(BaseValidatorModel):
    ShardId: str
    SequenceNumber: str
    EncryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterStreamConsumerOutputTypeDef(BaseValidatorModel):
    Consumer: ConsumerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateShardCountOutputTypeDef(BaseValidatorModel):
    StreamName: str
    CurrentShardCount: int
    TargetShardCount: int
    StreamARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStreamInputDescribeStreamPaginateTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamsInputListStreamsPaginateTypeDef(BaseValidatorModel):
    ExclusiveStartStreamName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStreamInputStreamExistsWaitTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamARN: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStreamInputStreamNotExistsWaitTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamARN: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class StreamDescriptionSummaryTypeDef(BaseValidatorModel):
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

class GetShardIteratorInputRequestTypeDef(BaseValidatorModel):
    ShardId: str
    ShardIteratorType: ShardIteratorTypeType
    StreamName: Optional[str] = None
    StartingSequenceNumber: Optional[str] = None
    Timestamp: Optional[TimestampTypeDef] = None
    StreamARN: Optional[str] = None

class ListStreamConsumersInputListStreamConsumersPaginateTypeDef(BaseValidatorModel):
    StreamARN: str
    StreamCreationTimestamp: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamConsumersInputRequestTypeDef(BaseValidatorModel):
    StreamARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StreamCreationTimestamp: Optional[TimestampTypeDef] = None

class ShardFilterTypeDef(BaseValidatorModel):
    Type: ShardFilterTypeType
    ShardId: Optional[str] = None
    Timestamp: Optional[TimestampTypeDef] = None

class StartingPositionTypeDef(BaseValidatorModel):
    Type: ShardIteratorTypeType
    SequenceNumber: Optional[str] = None
    Timestamp: Optional[TimestampTypeDef] = None

class ListTagsForStreamOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    HasMoreTags: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordsOutputTypeDef(BaseValidatorModel):
    FailedRecordCount: int
    Records: List[PutRecordsResultEntryTypeDef]
    EncryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ShardTypeDef(BaseValidatorModel):
    ShardId: str
    HashKeyRange: HashKeyRangeTypeDef
    SequenceNumberRange: SequenceNumberRangeTypeDef
    ParentShardId: Optional[str] = None
    AdjacentParentShardId: Optional[str] = None

class PutRecordsInputRequestTypeDef(BaseValidatorModel):
    Records: Sequence[PutRecordsRequestEntryTypeDef]
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class GetRecordsOutputTypeDef(BaseValidatorModel):
    Records: List[RecordTypeDef]
    NextShardIterator: str
    MillisBehindLatest: int
    ChildShards: List[ChildShardTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribeToShardEventTypeDef(BaseValidatorModel):
    Records: List[RecordTypeDef]
    ContinuationSequenceNumber: str
    MillisBehindLatest: int
    ChildShards: Optional[List[ChildShardTypeDef]] = None

class ListStreamsOutputTypeDef(BaseValidatorModel):
    StreamNames: List[str]
    HasMoreStreams: bool
    NextToken: str
    StreamSummaries: List[StreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStreamSummaryOutputTypeDef(BaseValidatorModel):
    StreamDescriptionSummary: StreamDescriptionSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListShardsInputListShardsPaginateTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    ExclusiveStartShardId: Optional[str] = None
    StreamCreationTimestamp: Optional[TimestampTypeDef] = None
    ShardFilter: Optional[ShardFilterTypeDef] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListShardsInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    NextToken: Optional[str] = None
    ExclusiveStartShardId: Optional[str] = None
    MaxResults: Optional[int] = None
    StreamCreationTimestamp: Optional[TimestampTypeDef] = None
    ShardFilter: Optional[ShardFilterTypeDef] = None
    StreamARN: Optional[str] = None

class SubscribeToShardInputRequestTypeDef(BaseValidatorModel):
    ConsumerARN: str
    ShardId: str
    StartingPosition: StartingPositionTypeDef

class ListShardsOutputTypeDef(BaseValidatorModel):
    Shards: List[ShardTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StreamDescriptionTypeDef(BaseValidatorModel):
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

class SubscribeToShardEventStreamTypeDef(BaseValidatorModel):
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

class DescribeStreamOutputTypeDef(BaseValidatorModel):
    StreamDescription: StreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribeToShardOutputTypeDef(BaseValidatorModel):
    EventStream: "EventStream[SubscribeToShardEventStreamTypeDef]"
    ResponseMetadata: ResponseMetadataTypeDef

