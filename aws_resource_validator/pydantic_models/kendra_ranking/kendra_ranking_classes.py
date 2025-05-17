from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.kendra_ranking.kendra_ranking_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CapacityUnitsConfiguration(BaseValidatorModel):
    RescoreCapacityUnits: int


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'delete_rescore_execution_plan' function.
class DeleteRescoreExecutionPlanRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'describe_rescore_execution_plan' function.
class DescribeRescoreExecutionPlanRequest(BaseValidatorModel):
    Id: str


class Document(BaseValidatorModel):
    Id: str
    OriginalScore: float
    GroupId: Optional[str] = None
    Title: Optional[str] = None
    Body: Optional[str] = None
    TokenizedTitle: Optional[List[str]] = None
    TokenizedBody: Optional[List[str]] = None


# This class is the input for the 'list_rescore_execution_plans' function.
class ListRescoreExecutionPlansRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RescoreExecutionPlanSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Status: Optional[RescoreExecutionPlanStatusType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class RescoreResultItem(BaseValidatorModel):
    DocumentId: Optional[str] = None
    Score: Optional[float] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_rescore_execution_plan' function.
class UpdateRescoreExecutionPlanRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    CapacityUnits: Optional[CapacityUnitsConfiguration] = None


# This class is the input for the 'create_rescore_execution_plan' function.
class CreateRescoreExecutionPlanRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    CapacityUnits: Optional[CapacityUnitsConfiguration] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the output for the 'create_rescore_execution_plan' function.
class CreateRescoreExecutionPlanResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_rescore_execution_plan' function.
class DescribeRescoreExecutionPlanResponse(BaseValidatorModel):
    Id: str
    Arn: str
    Name: str
    Description: str
    CapacityUnits: CapacityUnitsConfiguration
    CreatedAt: datetime
    UpdatedAt: datetime
    Status: RescoreExecutionPlanStatusType
    ErrorMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_rescore_execution_plan' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'rescore' function.
class RescoreRequest(BaseValidatorModel):
    RescoreExecutionPlanId: str
    SearchQuery: str
    Documents: List[Document]


# This class is the output for the 'list_rescore_execution_plans' function.
class ListRescoreExecutionPlansResponse(BaseValidatorModel):
    SummaryItems: List[RescoreExecutionPlanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'rescore' function.
class RescoreResult(BaseValidatorModel):
    RescoreId: str
    ResultItems: List[RescoreResultItem]
    ResponseMetadata: ResponseMetadata