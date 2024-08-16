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
from aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_constants import *

class DeleteHumanLoopRequestRequestTypeDef(BaseValidatorModel):
    HumanLoopName: str

class DescribeHumanLoopRequestRequestTypeDef(BaseValidatorModel):
    HumanLoopName: str

class HumanLoopOutputTypeDef(BaseValidatorModel):
    OutputS3Uri: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class HumanLoopDataAttributesTypeDef(BaseValidatorModel):
    ContentClassifiers: Sequence[ContentClassifierType]

class HumanLoopInputTypeDef(BaseValidatorModel):
    InputContent: str

class HumanLoopSummaryTypeDef(BaseValidatorModel):
    HumanLoopName: Optional[str] = None
    HumanLoopStatus: Optional[HumanLoopStatusType] = None
    CreationTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    FlowDefinitionArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class StopHumanLoopRequestRequestTypeDef(BaseValidatorModel):
    HumanLoopName: str

class DescribeHumanLoopResponseTypeDef(BaseValidatorModel):
    CreationTime: datetime
    FailureReason: str
    FailureCode: str
    HumanLoopStatus: HumanLoopStatusType
    HumanLoopName: str
    HumanLoopArn: str
    FlowDefinitionArn: str
    HumanLoopOutput: HumanLoopOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartHumanLoopResponseTypeDef(BaseValidatorModel):
    HumanLoopArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartHumanLoopRequestRequestTypeDef(BaseValidatorModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    HumanLoopInput: HumanLoopInputTypeDef
    DataAttributes: Optional[HumanLoopDataAttributesTypeDef] = None

class ListHumanLoopsResponseTypeDef(BaseValidatorModel):
    HumanLoopSummaries: List[HumanLoopSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListHumanLoopsRequestListHumanLoopsPaginateTypeDef(BaseValidatorModel):
    FlowDefinitionArn: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHumanLoopsRequestRequestTypeDef(BaseValidatorModel):
    FlowDefinitionArn: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

