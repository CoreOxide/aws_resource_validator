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
from aws_resource_validator.pydantic_models.forecastquery_constants import *

class DataPoint(BaseValidatorModel):
    Timestamp: Optional[str] = None
    Value: Optional[float] = None


class QueryForecastRequest(BaseValidatorModel):
    ForecastArn: str
    Filters: Mapping[str, str]
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    NextToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class QueryWhatIfForecastRequest(BaseValidatorModel):
    WhatIfForecastArn: str
    Filters: Mapping[str, str]
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    NextToken: Optional[str] = None


class Forecast(BaseValidatorModel):
    Predictions: Optional[Dict[str, List[DataPoint]]] = None


class QueryForecastResponse(BaseValidatorModel):
    Forecast: Forecast
    ResponseMetadata: ResponseMetadata


class QueryWhatIfForecastResponse(BaseValidatorModel):
    Forecast: Forecast
    ResponseMetadata: ResponseMetadata


