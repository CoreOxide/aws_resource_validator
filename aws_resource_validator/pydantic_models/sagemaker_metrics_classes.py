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
from aws_resource_validator.pydantic_models.sagemaker_metrics_constants import *

class MetricQuery(BaseValidatorModel):
    MetricName: str
    ResourceArn: str
    MetricStat: MetricStatisticType
    Period: PeriodType
    XAxisType: XAxisTypeType
    Start: Optional[int] = None
    End: Optional[int] = None


class MetricQueryResult(BaseValidatorModel):
    Status: MetricQueryResultStatusType
    XAxisValues: List[int]
    MetricValues: List[float]
    Message: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchPutMetricsError(BaseValidatorModel):
    Code: Optional[PutMetricsErrorCodeType] = None
    MetricIndex: Optional[int] = None


class BatchGetMetricsRequest(BaseValidatorModel):
    MetricQueries: Sequence[MetricQuery]


class BatchGetMetricsResponse(BaseValidatorModel):
    MetricQueryResults: List[MetricQueryResult]
    ResponseMetadata: ResponseMetadata


class BatchPutMetricsResponse(BaseValidatorModel):
    Errors: List[BatchPutMetricsError]
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class RawMetricData(BaseValidatorModel):
    MetricName: str
    Timestamp: Timestamp
    Value: float
    Step: Optional[int] = None


class BatchPutMetricsRequest(BaseValidatorModel):
    TrialComponentName: str
    MetricData: Sequence[RawMetricData]


