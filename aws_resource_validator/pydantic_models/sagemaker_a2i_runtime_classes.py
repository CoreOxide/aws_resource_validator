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
from aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_constants import *

class DeleteHumanLoopRequestTypeDef(BaseValidatorModel):
    HumanLoopName: str


class DescribeHumanLoopRequestTypeDef(BaseValidatorModel):
    HumanLoopName: str


class HumanLoopOutputTypeDef(BaseValidatorModel):
    OutputS3Uri: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class StopHumanLoopRequestTypeDef(BaseValidatorModel):
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


class StartHumanLoopRequestTypeDef(BaseValidatorModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    HumanLoopInput: HumanLoopInputTypeDef
    DataAttributes: Optional[HumanLoopDataAttributesTypeDef] = None


class ListHumanLoopsResponseTypeDef(BaseValidatorModel):
    HumanLoopSummaries: List[HumanLoopSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListHumanLoopsRequestPaginateTypeDef(BaseValidatorModel):
    FlowDefinitionArn: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHumanLoopsRequestTypeDef(BaseValidatorModel):
    FlowDefinitionArn: str
    CreationTimeAfter: Optional[TimestampTypeDef] = None
    CreationTimeBefore: Optional[TimestampTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


