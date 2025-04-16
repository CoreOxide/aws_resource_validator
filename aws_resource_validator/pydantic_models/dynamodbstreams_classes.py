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
from aws_resource_validator.pydantic_models.dynamodbstreams_constants import *

class AttributeValue(BaseValidatorModel):
    S: Optional[str] = None
    N: Optional[str] = None
    B: Optional[bytes] = None
    SS: Optional[List[str]] = None
    NS: Optional[List[str]] = None
    BS: Optional[List[bytes]] = None
    M: Optional[Dict[str, Dict[str, Any]]] = None
    L: Optional[List[Dict[str, Any]]] = None
    NULL: Optional[bool] = None
    BOOL: Optional[bool] = None


class DescribeStreamInput(BaseValidatorModel):
    StreamArn: str
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetRecordsInput(BaseValidatorModel):
    ShardIterator: str
    Limit: Optional[int] = None


class GetShardIteratorInput(BaseValidatorModel):
    StreamArn: str
    ShardId: str
    ShardIteratorType: ShardIteratorTypeType
    SequenceNumber: Optional[str] = None


class KeySchemaElement(BaseValidatorModel):
    AttributeName: str
    KeyType: KeyTypeType


class ListStreamsInput(BaseValidatorModel):
    TableName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartStreamArn: Optional[str] = None


class Stream(BaseValidatorModel):
    StreamArn: Optional[str] = None
    TableName: Optional[str] = None
    StreamLabel: Optional[str] = None


class SequenceNumberRange(BaseValidatorModel):
    StartingSequenceNumber: Optional[str] = None
    EndingSequenceNumber: Optional[str] = None


class StreamRecord(BaseValidatorModel):
    ApproximateCreationDateTime: Optional[datetime] = None
    Keys: Optional[Dict[str, AttributeValue]] = None
    NewImage: Optional[Dict[str, AttributeValue]] = None
    OldImage: Optional[Dict[str, AttributeValue]] = None
    SequenceNumber: Optional[str] = None
    SizeBytes: Optional[int] = None
    StreamViewType: Optional[StreamViewTypeType] = None


class GetShardIteratorOutput(BaseValidatorModel):
    ShardIterator: str
    ResponseMetadata: ResponseMetadata


class ListStreamsOutput(BaseValidatorModel):
    Streams: List[Stream]
    LastEvaluatedStreamArn: str
    ResponseMetadata: ResponseMetadata


class Shard(BaseValidatorModel):
    ShardId: Optional[str] = None
    SequenceNumberRange: Optional[SequenceNumberRange] = None
    ParentShardId: Optional[str] = None


class Identity(BaseValidatorModel):
    pass


class Record(BaseValidatorModel):
    eventID: Optional[str] = None
    eventName: Optional[OperationTypeType] = None
    eventVersion: Optional[str] = None
    eventSource: Optional[str] = None
    awsRegion: Optional[str] = None
    dynamodb: Optional[StreamRecord] = None
    userIdentity: Optional[Identity] = None


class StreamDescription(BaseValidatorModel):
    StreamArn: Optional[str] = None
    StreamLabel: Optional[str] = None
    StreamStatus: Optional[StreamStatusType] = None
    StreamViewType: Optional[StreamViewTypeType] = None
    CreationRequestDateTime: Optional[datetime] = None
    TableName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElement]] = None
    Shards: Optional[List[Shard]] = None
    LastEvaluatedShardId: Optional[str] = None


class GetRecordsOutput(BaseValidatorModel):
    Records: List[Record]
    NextShardIterator: str
    ResponseMetadata: ResponseMetadata


class DescribeStreamOutput(BaseValidatorModel):
    StreamDescription: StreamDescription
    ResponseMetadata: ResponseMetadata


