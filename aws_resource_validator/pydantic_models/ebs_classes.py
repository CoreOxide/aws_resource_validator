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

class BlockTypeDef(BaseValidatorModel):
    BlockIndex: Optional[int] = None
    BlockToken: Optional[str] = None


class ChangedBlockTypeDef(BaseValidatorModel):
    BlockIndex: Optional[int] = None
    FirstBlockToken: Optional[str] = None
    SecondBlockToken: Optional[str] = None


class CompleteSnapshotRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    ChangedBlocksCount: int
    Checksum: Optional[str] = None
    ChecksumAlgorithm: Optional[Literal["SHA256"]] = None
    ChecksumAggregationMethod: Optional[Literal["LINEAR"]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetSnapshotBlockRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    BlockIndex: int
    BlockToken: str


class ListChangedBlocksRequestTypeDef(BaseValidatorModel):
    SecondSnapshotId: str
    FirstSnapshotId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartingBlockIndex: Optional[int] = None


class ListSnapshotBlocksRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartingBlockIndex: Optional[int] = None


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class PutSnapshotBlockRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    BlockIndex: int
    BlockData: BlobTypeDef
    DataLength: int
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]
    Progress: Optional[int] = None


class CompleteSnapshotResponseTypeDef(BaseValidatorModel):
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetSnapshotBlockResponseTypeDef(BaseValidatorModel):
    DataLength: int
    BlockData: StreamingBody
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]
    ResponseMetadata: ResponseMetadataTypeDef


class ListChangedBlocksResponseTypeDef(BaseValidatorModel):
    ChangedBlocks: List[ChangedBlockTypeDef]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSnapshotBlocksResponseTypeDef(BaseValidatorModel):
    Blocks: List[BlockTypeDef]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutSnapshotBlockResponseTypeDef(BaseValidatorModel):
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]
    ResponseMetadata: ResponseMetadataTypeDef


class StartSnapshotRequestTypeDef(BaseValidatorModel):
    VolumeSize: int
    ParentSnapshotId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyArn: Optional[str] = None
    Timeout: Optional[int] = None


class StartSnapshotResponseTypeDef(BaseValidatorModel):
    Description: str
    SnapshotId: str
    OwnerId: str
    Status: StatusType
    StartTime: datetime
    VolumeSize: int
    BlockSize: int
    Tags: List[TagTypeDef]
    ParentSnapshotId: str
    KmsKeyArn: str
    SseType: SSETypeType
    ResponseMetadata: ResponseMetadataTypeDef


