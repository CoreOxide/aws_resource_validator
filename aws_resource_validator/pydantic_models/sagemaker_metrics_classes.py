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

class MetricQueryTypeDef(BaseValidatorModel):
    MetricName: str
    ResourceArn: str
    MetricStat: MetricStatisticType
    Period: PeriodType
    XAxisType: XAxisTypeType
    Start: Optional[int] = None
    End: Optional[int] = None


class MetricQueryResultTypeDef(BaseValidatorModel):
    Status: MetricQueryResultStatusType
    XAxisValues: List[int]
    MetricValues: List[float]
    Message: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchPutMetricsErrorTypeDef(BaseValidatorModel):
    Code: Optional[PutMetricsErrorCodeType] = None
    MetricIndex: Optional[int] = None


class BatchGetMetricsRequestTypeDef(BaseValidatorModel):
    MetricQueries: Sequence[MetricQueryTypeDef]


class BatchGetMetricsResponseTypeDef(BaseValidatorModel):
    MetricQueryResults: List[MetricQueryResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchPutMetricsResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchPutMetricsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class RawMetricDataTypeDef(BaseValidatorModel):
    MetricName: str
    Timestamp: TimestampTypeDef
    Value: float
    Step: Optional[int] = None


class BatchPutMetricsRequestTypeDef(BaseValidatorModel):
    TrialComponentName: str
    MetricData: Sequence[RawMetricDataTypeDef]


