from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class DataPointTypeDef(BaseValidatorModel):
    Timestamp: Optional[str] = None
    Value: Optional[float] = None

class QueryForecastRequestRequestTypeDef(BaseValidatorModel):
    ForecastArn: str
    Filters: Mapping[str, str]
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    NextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class QueryWhatIfForecastRequestRequestTypeDef(BaseValidatorModel):
    WhatIfForecastArn: str
    Filters: Mapping[str, str]
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    NextToken: Optional[str] = None

class ForecastTypeDef(BaseValidatorModel):
    Predictions: Optional[Dict[str, List[DataPointTypeDef]]] = None

class QueryForecastResponseTypeDef(BaseValidatorModel):
    Forecast: ForecastTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryWhatIfForecastResponseTypeDef(BaseValidatorModel):
    Forecast: ForecastTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

