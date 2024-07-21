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
from aws_resource_validator.pydantic_models.forecastquery_constants import *

class DataPointTypeDef(BaseModel):
    Timestamp: Optional[str] = None
    Value: Optional[float] = None

class QueryForecastRequestRequestTypeDef(BaseModel):
    ForecastArn: str
    Filters: Mapping[str, str]
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    NextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class QueryWhatIfForecastRequestRequestTypeDef(BaseModel):
    WhatIfForecastArn: str
    Filters: Mapping[str, str]
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    NextToken: Optional[str] = None

class ForecastTypeDef(BaseModel):
    Predictions: Optional[Dict[str, List[DataPointTypeDef]]] = None

class QueryForecastResponseTypeDef(BaseModel):
    Forecast: ForecastTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryWhatIfForecastResponseTypeDef(BaseModel):
    Forecast: ForecastTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

