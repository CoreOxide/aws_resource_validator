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
from aws_resource_validator.pydantic_models.dynamodbstreams_constants import *

class AttributeValueTypeDef(BaseModel):
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

class DescribeStreamInputRequestTypeDef(BaseModel):
    StreamArn: str
    Limit: Optional[int] = None
    ExclusiveStartShardId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetRecordsInputRequestTypeDef(BaseModel):
    ShardIterator: str
    Limit: Optional[int] = None

class GetShardIteratorInputRequestTypeDef(BaseModel):
    StreamArn: str
    ShardId: str
    ShardIteratorType: ShardIteratorTypeType
    SequenceNumber: Optional[str] = None

class IdentityTypeDef(BaseModel):
    PrincipalId: Optional[str] = None
    Type: Optional[str] = None

class KeySchemaElementTypeDef(BaseModel):
    AttributeName: str
    KeyType: KeyTypeType

class ListStreamsInputRequestTypeDef(BaseModel):
    TableName: Optional[str] = None
    Limit: Optional[int] = None
    ExclusiveStartStreamArn: Optional[str] = None

class StreamTypeDef(BaseModel):
    StreamArn: Optional[str] = None
    TableName: Optional[str] = None
    StreamLabel: Optional[str] = None

class StreamRecordTypeDef(BaseModel):
    ApproximateCreationDateTime: Optional[datetime] = None
    Keys: Optional[Dict[str, "AttributeValueTypeDef"]] = None
    NewImage: Optional[Dict[str, "AttributeValueTypeDef"]] = None
    OldImage: Optional[Dict[str, "AttributeValueTypeDef"]] = None
    SequenceNumber: Optional[str] = None
    SizeBytes: Optional[int] = None
    StreamViewType: Optional[StreamViewTypeType] = None

class SequenceNumberRangeTypeDef(BaseModel):
    StartingSequenceNumber: Optional[str] = None
    EndingSequenceNumber: Optional[str] = None

class GetShardIteratorOutputTypeDef(BaseModel):
    ShardIterator: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamsOutputTypeDef(BaseModel):
    Streams: List[StreamTypeDef]
    LastEvaluatedStreamArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecordTypeDef(BaseModel):
    eventID: Optional[str] = None
    eventName: Optional[OperationTypeType] = None
    eventVersion: Optional[str] = None
    eventSource: Optional[str] = None
    awsRegion: Optional[str] = None
    dynamodb: Optional[StreamRecordTypeDef] = None
    userIdentity: Optional[IdentityTypeDef] = None

class ShardTypeDef(BaseModel):
    ShardId: Optional[str] = None
    SequenceNumberRange: Optional[SequenceNumberRangeTypeDef] = None
    ParentShardId: Optional[str] = None

class GetRecordsOutputTypeDef(BaseModel):
    Records: List[RecordTypeDef]
    NextShardIterator: str
    ResponseMetadata: ResponseMetadataTypeDef

class StreamDescriptionTypeDef(BaseModel):
    StreamArn: Optional[str] = None
    StreamLabel: Optional[str] = None
    StreamStatus: Optional[StreamStatusType] = None
    StreamViewType: Optional[StreamViewTypeType] = None
    CreationRequestDateTime: Optional[datetime] = None
    TableName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElementTypeDef]] = None
    Shards: Optional[List[ShardTypeDef]] = None
    LastEvaluatedShardId: Optional[str] = None

class DescribeStreamOutputTypeDef(BaseModel):
    StreamDescription: StreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

