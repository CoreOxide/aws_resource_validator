from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.forecastquery.forecastquery_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class DataPoint(BaseValidatorModel):
    Timestamp: Optional[str] = None
    Value: Optional[float] = None


class QueryForecastRequest(BaseValidatorModel):
    ForecastArn: str
    Filters: Dict[str, str]
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
    Filters: Dict[str, str]
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