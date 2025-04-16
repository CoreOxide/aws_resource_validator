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
from aws_resource_validator.pydantic_models.ebs_constants import *

class Block(BaseValidatorModel):
    BlockIndex: Optional[int] = None
    BlockToken: Optional[str] = None


class ChangedBlock(BaseValidatorModel):
    BlockIndex: Optional[int] = None
    FirstBlockToken: Optional[str] = None
    SecondBlockToken: Optional[str] = None


class CompleteSnapshotRequest(BaseValidatorModel):
    SnapshotId: str
    ChangedBlocksCount: int
    Checksum: Optional[str] = None
    ChecksumAlgorithm: Optional[Literal["SHA256"]] = None
    ChecksumAggregationMethod: Optional[Literal["LINEAR"]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetSnapshotBlockRequest(BaseValidatorModel):
    SnapshotId: str
    BlockIndex: int
    BlockToken: str


class ListChangedBlocksRequest(BaseValidatorModel):
    SecondSnapshotId: str
    FirstSnapshotId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartingBlockIndex: Optional[int] = None


class ListSnapshotBlocksRequest(BaseValidatorModel):
    SnapshotId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartingBlockIndex: Optional[int] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class Blob(BaseValidatorModel):
    pass


class PutSnapshotBlockRequest(BaseValidatorModel):
    SnapshotId: str
    BlockIndex: int
    BlockData: Blob
    DataLength: int
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]
    Progress: Optional[int] = None


class CompleteSnapshotResponse(BaseValidatorModel):
    Status: StatusType
    ResponseMetadata: ResponseMetadata


class GetSnapshotBlockResponse(BaseValidatorModel):
    DataLength: int
    BlockData: StreamingBody
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]
    ResponseMetadata: ResponseMetadata


class ListChangedBlocksResponse(BaseValidatorModel):
    ChangedBlocks: List[ChangedBlock]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSnapshotBlocksResponse(BaseValidatorModel):
    Blocks: List[Block]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutSnapshotBlockResponse(BaseValidatorModel):
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]
    ResponseMetadata: ResponseMetadata


class StartSnapshotRequest(BaseValidatorModel):
    VolumeSize: int
    ParentSnapshotId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyArn: Optional[str] = None
    Timeout: Optional[int] = None


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


