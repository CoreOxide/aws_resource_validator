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
from aws_resource_validator.pydantic_models.sagemaker_metrics_constants import *

class BatchPutMetricsErrorTypeDef(BaseModel):
    Code: Optional[PutMetricsErrorCodeType] = None
    MetricIndex: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchPutMetricsResponseTypeDef(BaseModel):
    Errors: List[BatchPutMetricsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RawMetricDataTypeDef(BaseModel):
    MetricName: str
    Timestamp: TimestampTypeDef
    Value: float
    Step: Optional[int] = None

class BatchPutMetricsRequestRequestTypeDef(BaseModel):
    TrialComponentName: str
    MetricData: Sequence[RawMetricDataTypeDef]

