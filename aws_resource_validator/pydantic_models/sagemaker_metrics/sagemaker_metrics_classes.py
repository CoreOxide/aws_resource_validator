from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sagemaker_metrics.sagemaker_metrics_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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

Timestamp = Union[datetime, str]


class BatchGetMetricsRequest(BaseValidatorModel):
    MetricQueries: List[MetricQuery]


class BatchGetMetricsResponse(BaseValidatorModel):
    MetricQueryResults: List[MetricQueryResult]
    ResponseMetadata: ResponseMetadata


class BatchPutMetricsResponse(BaseValidatorModel):
    Errors: List[BatchPutMetricsError]
    ResponseMetadata: ResponseMetadata


class RawMetricData(BaseValidatorModel):
    MetricName: str
    Timestamp: Timestamp
    Value: float
    Step: Optional[int] = None


class BatchPutMetricsRequest(BaseValidatorModel):
    TrialComponentName: str
    MetricData: List[RawMetricData]