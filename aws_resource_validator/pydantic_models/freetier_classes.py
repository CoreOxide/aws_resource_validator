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
from aws_resource_validator.pydantic_models.freetier_constants import *

class DimensionValuesTypeDef(BaseModel):
    Key: DimensionType
    MatchOptions: Sequence[MatchOptionType]
    Values: Sequence[str]

class FreeTierUsageTypeDef(BaseModel):
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

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetFreeTierUsageRequestRequestTypeDef(BaseModel):
    filter: Optional["ExpressionTypeDef"] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ExpressionTypeDef(BaseModel):
    And: Optional[Sequence[Dict[str, Any]]] = None
    Dimensions: Optional[DimensionValuesTypeDef] = None
    Not: Optional[Dict[str, Any]] = None
    Or: Optional[Sequence[Dict[str, Any]]] = None

class GetFreeTierUsageResponseTypeDef(BaseModel):
    freeTierUsages: List[FreeTierUsageTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFreeTierUsageRequestGetFreeTierUsagePaginateTypeDef(BaseModel):
    filter: Optional[ExpressionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

