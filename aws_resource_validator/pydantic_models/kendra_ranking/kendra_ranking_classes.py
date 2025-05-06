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
    TokenizedTitle: Optional[List[str]] = None
    TokenizedBody: Optional[List[str]] = None


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
    TagKeys: List[str]


class UpdateRescoreExecutionPlanRequest(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    CapacityUnits: Optional[CapacityUnitsConfiguration] = None


class CreateRescoreExecutionPlanRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    CapacityUnits: Optional[CapacityUnitsConfiguration] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


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
    Documents: List[Document]


class ListRescoreExecutionPlansResponse(BaseValidatorModel):
    SummaryItems: List[RescoreExecutionPlanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RescoreResult(BaseValidatorModel):
    RescoreId: str
    ResultItems: List[RescoreResultItem]
    ResponseMetadata: ResponseMetadata