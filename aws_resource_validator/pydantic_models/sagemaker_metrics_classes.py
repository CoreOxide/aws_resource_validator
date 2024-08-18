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
from aws_resource_validator.pydantic_models.sagemaker_metrics_constants import *

class BatchPutMetricsErrorTypeDef(BaseValidatorModel):
    Code: Optional[PutMetricsErrorCodeType] = None
    MetricIndex: Optional[int] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchPutMetricsResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchPutMetricsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RawMetricDataTypeDef(BaseValidatorModel):
    MetricName: str
    Timestamp: TimestampTypeDef
    Value: float
    Step: Optional[int] = None

class BatchPutMetricsRequestRequestTypeDef(BaseValidatorModel):
    TrialComponentName: str
    MetricData: Sequence[RawMetricDataTypeDef]

