from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ebs.ebs_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


class Block(BaseValidatorModel):
    BlockIndex: Optional[int] = None
    BlockToken: Optional[str] = None


class ChangedBlock(BaseValidatorModel):
    BlockIndex: Optional[int] = None
    FirstBlockToken: Optional[str] = None
    SecondBlockToken: Optional[str] = None


# This class is the input for the 'complete_snapshot' function.
class CompleteSnapshotRequest(BaseValidatorModel):
    SnapshotId: str
    ChangedBlocksCount: int
    Checksum: Optional[str] = None
    ChecksumAlgorithm: Optional[Literal['SHA256']] = None
    ChecksumAggregationMethod: Optional[Literal['LINEAR']] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'get_snapshot_block' function.
class GetSnapshotBlockRequest(BaseValidatorModel):
    SnapshotId: str
    BlockIndex: int
    BlockToken: str


# This class is the input for the 'list_changed_blocks' function.
class ListChangedBlocksRequest(BaseValidatorModel):
    SecondSnapshotId: str
    FirstSnapshotId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartingBlockIndex: Optional[int] = None


# This class is the input for the 'list_snapshot_blocks' function.
class ListSnapshotBlocksRequest(BaseValidatorModel):
    SnapshotId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartingBlockIndex: Optional[int] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'put_snapshot_block' function.
class PutSnapshotBlockRequest(BaseValidatorModel):
    SnapshotId: str
    BlockIndex: int
    BlockData: Blob
    DataLength: int
    Checksum: str
    ChecksumAlgorithm: Literal['SHA256']
    Progress: Optional[int] = None


# This class is the output for the 'complete_snapshot' function.
class CompleteSnapshotResponse(BaseValidatorModel):
    Status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_snapshot_block' function.
class GetSnapshotBlockResponse(BaseValidatorModel):
    DataLength: int
    BlockData: StreamingBody
    Checksum: str
    ChecksumAlgorithm: Literal['SHA256']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_changed_blocks' function.
class ListChangedBlocksResponse(BaseValidatorModel):
    ChangedBlocks: List[ChangedBlock]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_snapshot_blocks' function.
class ListSnapshotBlocksResponse(BaseValidatorModel):
    Blocks: List[Block]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_snapshot_block' function.
class PutSnapshotBlockResponse(BaseValidatorModel):
    Checksum: str
    ChecksumAlgorithm: Literal['SHA256']
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_snapshot' function.
class StartSnapshotRequest(BaseValidatorModel):
    VolumeSize: int
    ParentSnapshotId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyArn: Optional[str] = None
    Timeout: Optional[int] = None


# This class is the output for the 'start_snapshot' function.
class StartSnapshotResponse(BaseValidatorModel):
    Description: str
    SnapshotId: str
    OwnerId: str
    Status: StatusType
    StartTime: datetime
    VolumeSize: int
    BlockSize: int
    Tags: List[Tag]
    ParentSnapshotId: str
    KmsKeyArn: str
    SseType: SSETypeType
    ResponseMetadata: ResponseMetadata