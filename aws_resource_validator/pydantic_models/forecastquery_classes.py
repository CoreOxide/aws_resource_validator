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

class DataPointTypeDef(BaseValidatorModel):
    Timestamp: Optional[str] = None
    Value: Optional[float] = None


class QueryForecastRequestTypeDef(BaseValidatorModel):
    ForecastArn: str
    Filters: Mapping[str, str]
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    NextToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class QueryWhatIfForecastRequestTypeDef(BaseValidatorModel):
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


