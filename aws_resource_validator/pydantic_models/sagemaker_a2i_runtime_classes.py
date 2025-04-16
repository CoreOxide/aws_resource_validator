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

class DeleteHumanLoopRequest(BaseValidatorModel):
    HumanLoopName: str


class DescribeHumanLoopRequest(BaseValidatorModel):
    HumanLoopName: str


class HumanLoopOutput(BaseValidatorModel):
    OutputS3Uri: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class HumanLoopDataAttributes(BaseValidatorModel):
    ContentClassifiers: Sequence[ContentClassifierType]


class HumanLoopInput(BaseValidatorModel):
    InputContent: str


class HumanLoopSummary(BaseValidatorModel):
    HumanLoopName: Optional[str] = None
    HumanLoopStatus: Optional[HumanLoopStatusType] = None
    CreationTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    FlowDefinitionArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class StopHumanLoopRequest(BaseValidatorModel):
    HumanLoopName: str


class DescribeHumanLoopResponse(BaseValidatorModel):
    CreationTime: datetime
    FailureReason: str
    FailureCode: str
    HumanLoopStatus: HumanLoopStatusType
    HumanLoopName: str
    HumanLoopArn: str
    FlowDefinitionArn: str
    HumanLoopOutput: HumanLoopOutput
    ResponseMetadata: ResponseMetadata


class StartHumanLoopResponse(BaseValidatorModel):
    HumanLoopArn: str
    ResponseMetadata: ResponseMetadata


class StartHumanLoopRequest(BaseValidatorModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    HumanLoopInput: HumanLoopInput
    DataAttributes: Optional[HumanLoopDataAttributes] = None


class ListHumanLoopsResponse(BaseValidatorModel):
    HumanLoopSummaries: List[HumanLoopSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Timestamp(BaseValidatorModel):
    pass


class ListHumanLoopsRequestPaginate(BaseValidatorModel):
    FlowDefinitionArn: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHumanLoopsRequest(BaseValidatorModel):
    FlowDefinitionArn: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


