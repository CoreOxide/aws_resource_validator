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
from aws_resource_validator.pydantic_models.ebs_constants import *

class BlockTypeDef(BaseValidatorModel):
    BlockIndex: Optional[int] = None
    BlockToken: Optional[str] = None

class ChangedBlockTypeDef(BaseValidatorModel):
    BlockIndex: Optional[int] = None
    FirstBlockToken: Optional[str] = None
    SecondBlockToken: Optional[str] = None

class CompleteSnapshotRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    ChangedBlocksCount: int
    Checksum: Optional[str] = None
    ChecksumAlgorithm: Optional[Literal["SHA256"]] = None
    ChecksumAggregationMethod: Optional[Literal["LINEAR"]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetSnapshotBlockRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    BlockIndex: int
    BlockToken: str

class ListChangedBlocksRequestRequestTypeDef(BaseValidatorModel):
    SecondSnapshotId: str
    FirstSnapshotId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartingBlockIndex: Optional[int] = None

class ListSnapshotBlocksRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartingBlockIndex: Optional[int] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class PutSnapshotBlockRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSnapshotBlocksResponseTypeDef(BaseValidatorModel):
    Blocks: List[BlockTypeDef]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSnapshotBlockResponseTypeDef(BaseValidatorModel):
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]
    ResponseMetadata: ResponseMetadataTypeDef

class StartSnapshotRequestRequestTypeDef(BaseValidatorModel):
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

