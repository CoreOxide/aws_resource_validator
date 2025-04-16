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
from aws_resource_validator.pydantic_models.freetier_constants import *

class DimensionValues(BaseValidatorModel):
    Key: DimensionType
    MatchOptions: Sequence[MatchOptionType]
    Values: Sequence[str]


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
    And: Optional[Sequence[Mapping[str, Any]]] = None
    Dimensions: Optional[DimensionValues] = None
    Not: Optional[Mapping[str, Any]] = None
    Or: Optional[Sequence[Mapping[str, Any]]] = None


class Expression(BaseValidatorModel):
    And: Optional[Sequence[Mapping[str, Any]]] = None
    Dimensions: Optional[DimensionValues] = None
    Not: Optional[Mapping[str, Any]] = None
    Or: Optional[Sequence[Mapping[str, Any]]] = None


class GetFreeTierUsageResponse(BaseValidatorModel):
    freeTierUsages: List[FreeTierUsage]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


