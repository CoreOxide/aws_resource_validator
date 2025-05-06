from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.freetier.freetier_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class DimensionValues(BaseValidatorModel):
    Key: DimensionType
    MatchOptions: List[MatchOptionType]
    Values: List[str]


class FreeTierUsage(BaseValidatorModel):
    actualUsageAmount: Optional[float] = None
    description: Optional[str] = None
    forecastedUsageAmount: Optional[float] = None
    freeTierType: Optional[str] = None
    limit: Optional[float] = None
    operation: Optional[str] = None
    region: Optional[str] = None
    service: Optional[str] = None
    unit: Optional[str] = None
    usageType: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ExpressionPaginator(BaseValidatorModel):
    And: Optional[List[Dict[str, Any]]] = None
    Dimensions: Optional[DimensionValues] = None
    Not: Optional[Dict[str, Any]] = None
    or_: Optional[List[Dict[str, Any]]] = None


class Expression(BaseValidatorModel):
    And: Optional[List[Dict[str, Any]]] = None
    Dimensions: Optional[DimensionValues] = None
    Not: Optional[Dict[str, Any]] = None
    or_: Optional[List[Dict[str, Any]]] = None


class GetFreeTierUsageResponse(BaseValidatorModel):
    freeTierUsages: List[FreeTierUsage]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetFreeTierUsageRequestPaginate(BaseValidatorModel):
    filter: Optional[ExpressionPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetFreeTierUsageRequest(BaseValidatorModel):
    filter: Optional[Expression] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None