from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sagemaker_a2i_runtime.sagemaker_a2i_runtime_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class DeleteHumanLoopRequest(BaseValidatorModel):
    HumanLoopName: str


# This class is the input for the 'describe_human_loop' function.
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
    ContentClassifiers: List[ContentClassifierType]


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

Timestamp = Union[datetime, str]


class StopHumanLoopRequest(BaseValidatorModel):
    HumanLoopName: str


# This class is the output for the 'describe_human_loop' function.
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


# This class is the output for the 'start_human_loop' function.
class StartHumanLoopResponse(BaseValidatorModel):
    HumanLoopArn: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_human_loop' function.
class StartHumanLoopRequest(BaseValidatorModel):
    HumanLoopName: str
    FlowDefinitionArn: str
    HumanLoopInput: HumanLoopInput
    DataAttributes: Optional[HumanLoopDataAttributes] = None


# This class is the output for the 'list_human_loops' function.
class ListHumanLoopsResponse(BaseValidatorModel):
    HumanLoopSummaries: List[HumanLoopSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListHumanLoopsRequestPaginate(BaseValidatorModel):
    FlowDefinitionArn: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_human_loops' function.
class ListHumanLoopsRequest(BaseValidatorModel):
    FlowDefinitionArn: str
    CreationTimeAfter: Optional[Timestamp] = None
    CreationTimeBefore: Optional[Timestamp] = None
    SortOrder: Optional[SortOrderType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None