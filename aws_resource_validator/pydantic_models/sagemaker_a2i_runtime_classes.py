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
from aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_constants import *

class DeleteHumanLoopRequestRequestTypeDef(BaseModel):
    HumanLoopName: str

class DescribeHumanLoopRequestRequestTypeDef(BaseModel):
    HumanLoopName: str

class HumanLoopOutputTypeDef(BaseModel):
    OutputS3Uri: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class HumanLoopDataAttributesTypeDef(BaseModel):
    ContentClassifiers: Sequence[ContentClassifierType]

class HumanLoopInputTypeDef(BaseModel):
    InputContent: str

class HumanLoopSummaryTypeDef(BaseModel):
    HumanLoopName: Optional[str] = None
    HumanLoopStatus: Optional[HumanLoopStatusType] = None
    CreationTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    FlowDefinitionArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class StopHumanLoopRequestRequestTypeDef(BaseModel):
    HumanLoopName: str

class DescribeHumanLoopResponseTypeDef(BaseModel):
    CreationTime: datetime
    FailureReason: str
    FailureCode: str
    HumanLoopStatus: HumanLoopStatusType
    HumanLoopName: str
    HumanLoopArn: str
    FlowDefinitionArn: str
    HumanLoopOutput: HumanLoopOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartHumanLoopResponseTypeDef(BaseModel):
    HumanLoopArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartHumanLoopRequestRequestTypeDef(BaseModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    HumanLoopInput: HumanLoopInputTypeDef
    DataAttributes: Optional[HumanLoopDataAttributesTypeDef] = None

class ListHumanLoopsResponseTypeDef(BaseModel):
    HumanLoopSummaries: List[HumanLoopSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListHumanLoopsRequestListHumanLoopsPaginateTypeDef(BaseModel):
    FlowDefinitionArn: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHumanLoopsRequestRequestTypeDef(BaseModel):
    FlowDefinitionArn: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

