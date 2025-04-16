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
from aws_resource_validator.pydantic_models.kendra_ranking_constants import *

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


class DeleteRescoreExecutionPlanRequest(BaseValidatorModel):
    Id: str


class DescribeRescoreExecutionPlanRequest(BaseValidatorModel):
    Id: str


class Document(BaseValidatorModel):
    Id: str
    OriginalScore: float
    GroupId: Optional[str] = None
    Title: Optional[str] = None
    Body: Optional[str] = None
    TokenizedTitle: Optional[Sequence[str]] = None
    TokenizedBody: Optional[Sequence[str]] = None


class ListRescoreExecutionPlansRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RescoreExecutionPlanSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Status: Optional[RescoreExecutionPlanStatusType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class RescoreResultItem(BaseValidatorModel):
    DocumentId: Optional[str] = None
    Score: Optional[float] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateRescoreExecutionPlanRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    CapacityUnits: Optional[CapacityUnitsConfiguration] = None


class CreateRescoreExecutionPlanRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    CapacityUnits: Optional[CapacityUnitsConfiguration] = None
    Tags: Optional[Sequence[Tag]] = None
    ClientToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateRescoreExecutionPlanResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


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


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class RescoreRequest(BaseValidatorModel):
    RescoreExecutionPlanId: str
    SearchQuery: str
    Documents: Sequence[Document]


class ListRescoreExecutionPlansResponse(BaseValidatorModel):
    SummaryItems: List[RescoreExecutionPlanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RescoreResult(BaseValidatorModel):
    RescoreId: str
    ResultItems: List[RescoreResultItem]
    ResponseMetadata: ResponseMetadata


