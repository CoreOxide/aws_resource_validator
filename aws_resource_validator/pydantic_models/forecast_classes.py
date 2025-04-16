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
from aws_resource_validator.pydantic_models.forecast_constants import *

class Action(BaseValidatorModel):
    AttributeName: str
    Operation: OperationType
    Value: float


class AdditionalDatasetOutput(BaseValidatorModel):
    Name: str
    Configuration: Optional[Dict[str, List[str]]] = None


class AdditionalDataset(BaseValidatorModel):
    Name: str
    Configuration: Optional[Mapping[str, Sequence[str]]] = None


class AttributeConfigOutput(BaseValidatorModel):
    AttributeName: str
    Transformations: Dict[str, str]


class AttributeConfig(BaseValidatorModel):
    AttributeName: str
    Transformations: Mapping[str, str]


class BaselineMetric(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[float] = None


class CategoricalParameterRangeOutput(BaseValidatorModel):
    Name: str
    Values: List[str]


class CategoricalParameterRange(BaseValidatorModel):
    Name: str
    Values: Sequence[str]


class ContinuousParameterRange(BaseValidatorModel):
    Name: str
    MaxValue: float
    MinValue: float
    ScalingType: Optional[ScalingTypeType] = None


class EncryptionConfig(BaseValidatorModel):
    RoleArn: str
    KMSKeyArn: str


class MonitorConfig(BaseValidatorModel):
    MonitorName: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class TimeAlignmentBoundary(BaseValidatorModel):
    Month: Optional[MonthType] = None
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[DayOfWeekType] = None
    Hour: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ExplainabilityConfig(BaseValidatorModel):
    TimeSeriesGranularity: TimeSeriesGranularityType
    TimePointGranularity: TimePointGranularityType


class EvaluationParameters(BaseValidatorModel):
    NumberOfBacktestWindows: Optional[int] = None
    BackTestWindowOffset: Optional[int] = None


class S3Config(BaseValidatorModel):
    Path: str
    RoleArn: str
    KMSKeyArn: Optional[str] = None


class DatasetGroupSummary(BaseValidatorModel):
    DatasetGroupArn: Optional[str] = None
    DatasetGroupName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class DatasetSummary(BaseValidatorModel):
    DatasetArn: Optional[str] = None
    DatasetName: Optional[str] = None
    DatasetType: Optional[DatasetTypeType] = None
    Domain: Optional[DomainType] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class DeleteDatasetGroupRequest(BaseValidatorModel):
    DatasetGroupArn: str


class DeleteDatasetImportJobRequest(BaseValidatorModel):
    DatasetImportJobArn: str


class DeleteDatasetRequest(BaseValidatorModel):
    DatasetArn: str


class DeleteExplainabilityExportRequest(BaseValidatorModel):
    ExplainabilityExportArn: str


class DeleteExplainabilityRequest(BaseValidatorModel):
    ExplainabilityArn: str


class DeleteForecastExportJobRequest(BaseValidatorModel):
    ForecastExportJobArn: str


class DeleteForecastRequest(BaseValidatorModel):
    ForecastArn: str


class DeleteMonitorRequest(BaseValidatorModel):
    MonitorArn: str


class DeletePredictorBacktestExportJobRequest(BaseValidatorModel):
    PredictorBacktestExportJobArn: str


class DeletePredictorRequest(BaseValidatorModel):
    PredictorArn: str


class DeleteResourceTreeRequest(BaseValidatorModel):
    ResourceArn: str


class DeleteWhatIfAnalysisRequest(BaseValidatorModel):
    WhatIfAnalysisArn: str


class DeleteWhatIfForecastExportRequest(BaseValidatorModel):
    WhatIfForecastExportArn: str


class DeleteWhatIfForecastRequest(BaseValidatorModel):
    WhatIfForecastArn: str


class DescribeAutoPredictorRequest(BaseValidatorModel):
    PredictorArn: str


class ExplainabilityInfo(BaseValidatorModel):
    ExplainabilityArn: Optional[str] = None
    Status: Optional[str] = None


class MonitorInfo(BaseValidatorModel):
    MonitorArn: Optional[str] = None
    Status: Optional[str] = None


class ReferencePredictorSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    State: Optional[StateType] = None


class DescribeDatasetGroupRequest(BaseValidatorModel):
    DatasetGroupArn: str


class DescribeDatasetImportJobRequest(BaseValidatorModel):
    DatasetImportJobArn: str


class Statistics(BaseValidatorModel):
    Count: Optional[int] = None
    CountDistinct: Optional[int] = None
    CountNull: Optional[int] = None
    CountNan: Optional[int] = None
    Min: Optional[str] = None
    Max: Optional[str] = None
    Avg: Optional[float] = None
    Stddev: Optional[float] = None
    CountLong: Optional[int] = None
    CountDistinctLong: Optional[int] = None
    CountNullLong: Optional[int] = None
    CountNanLong: Optional[int] = None


class DescribeDatasetRequest(BaseValidatorModel):
    DatasetArn: str


class DescribeExplainabilityExportRequest(BaseValidatorModel):
    ExplainabilityExportArn: str


class DescribeExplainabilityRequest(BaseValidatorModel):
    ExplainabilityArn: str


class DescribeForecastExportJobRequest(BaseValidatorModel):
    ForecastExportJobArn: str


class DescribeForecastRequest(BaseValidatorModel):
    ForecastArn: str


class DescribeMonitorRequest(BaseValidatorModel):
    MonitorArn: str


class DescribePredictorBacktestExportJobRequest(BaseValidatorModel):
    PredictorBacktestExportJobArn: str


class DescribePredictorRequest(BaseValidatorModel):
    PredictorArn: str


class DescribeWhatIfAnalysisRequest(BaseValidatorModel):
    WhatIfAnalysisArn: str


class DescribeWhatIfForecastExportRequest(BaseValidatorModel):
    WhatIfForecastExportArn: str


class DescribeWhatIfForecastRequest(BaseValidatorModel):
    WhatIfForecastArn: str


class ErrorMetric(BaseValidatorModel):
    ForecastType: Optional[str] = None
    WAPE: Optional[float] = None
    RMSE: Optional[float] = None
    MASE: Optional[float] = None
    MAPE: Optional[float] = None


class FeaturizationMethodOutput(BaseValidatorModel):
    FeaturizationMethodName: Literal["filling"]
    FeaturizationMethodParameters: Optional[Dict[str, str]] = None


class FeaturizationMethod(BaseValidatorModel):
    FeaturizationMethodName: Literal["filling"]
    FeaturizationMethodParameters: Optional[Mapping[str, str]] = None


class Filter(BaseValidatorModel):
    Key: str
    Value: str
    Condition: FilterConditionStringType


class ForecastSummary(BaseValidatorModel):
    ForecastArn: Optional[str] = None
    ForecastName: Optional[str] = None
    PredictorArn: Optional[str] = None
    CreatedUsingAutoPredictor: Optional[bool] = None
    DatasetGroupArn: Optional[str] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class GetAccuracyMetricsRequest(BaseValidatorModel):
    PredictorArn: str


class SupplementaryFeature(BaseValidatorModel):
    Name: str
    Value: str


class IntegerParameterRange(BaseValidatorModel):
    Name: str
    MaxValue: int
    MinValue: int
    ScalingType: Optional[ScalingTypeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDatasetGroupsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDatasetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MonitorSummary(BaseValidatorModel):
    MonitorArn: Optional[str] = None
    MonitorName: Optional[str] = None
    ResourceArn: Optional[str] = None
    Status: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class WhatIfAnalysisSummary(BaseValidatorModel):
    WhatIfAnalysisArn: Optional[str] = None
    WhatIfAnalysisName: Optional[str] = None
    ForecastArn: Optional[str] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class WhatIfForecastSummary(BaseValidatorModel):
    WhatIfForecastArn: Optional[str] = None
    WhatIfForecastName: Optional[str] = None
    WhatIfAnalysisArn: Optional[str] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class MetricResult(BaseValidatorModel):
    MetricName: Optional[str] = None
    MetricValue: Optional[float] = None


class WeightedQuantileLoss(BaseValidatorModel):
    Quantile: Optional[float] = None
    LossValue: Optional[float] = None


class MonitorDataSource(BaseValidatorModel):
    DatasetImportJobArn: Optional[str] = None
    ForecastArn: Optional[str] = None
    PredictorArn: Optional[str] = None


class PredictorEvent(BaseValidatorModel):
    Detail: Optional[str] = None
    Datetime: Optional[datetime] = None


class TestWindowSummary(BaseValidatorModel):
    TestWindowStart: Optional[datetime] = None
    TestWindowEnd: Optional[datetime] = None
    Status: Optional[str] = None
    Message: Optional[str] = None


class ResumeResourceRequest(BaseValidatorModel):
    ResourceArn: str


class SchemaAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[AttributeTypeType] = None


class StopResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TimeSeriesCondition(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str
    Condition: ConditionType


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateDatasetGroupRequest(BaseValidatorModel):
    DatasetGroupArn: str
    DatasetArns: Sequence[str]


class DataConfigOutput(BaseValidatorModel):
    DatasetGroupArn: str
    AttributeConfigs: Optional[List[AttributeConfigOutput]] = None
    AdditionalDatasets: Optional[List[AdditionalDatasetOutput]] = None


class DataConfig(BaseValidatorModel):
    DatasetGroupArn: str
    AttributeConfigs: Optional[Sequence[AttributeConfig]] = None
    AdditionalDatasets: Optional[Sequence[AdditionalDataset]] = None


class PredictorBaseline(BaseValidatorModel):
    BaselineMetrics: Optional[List[BaselineMetric]] = None


class CreateDatasetGroupRequest(BaseValidatorModel):
    DatasetGroupName: str
    Domain: DomainType
    DatasetArns: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateMonitorRequest(BaseValidatorModel):
    MonitorName: str
    ResourceArn: str
    Tags: Optional[Sequence[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class CreateAutoPredictorResponse(BaseValidatorModel):
    PredictorArn: str
    ResponseMetadata: ResponseMetadata


class CreateDatasetGroupResponse(BaseValidatorModel):
    DatasetGroupArn: str
    ResponseMetadata: ResponseMetadata


class CreateDatasetImportJobResponse(BaseValidatorModel):
    DatasetImportJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateDatasetResponse(BaseValidatorModel):
    DatasetArn: str
    ResponseMetadata: ResponseMetadata


class CreateExplainabilityExportResponse(BaseValidatorModel):
    ExplainabilityExportArn: str
    ResponseMetadata: ResponseMetadata


class CreateExplainabilityResponse(BaseValidatorModel):
    ExplainabilityArn: str
    ResponseMetadata: ResponseMetadata


class CreateForecastExportJobResponse(BaseValidatorModel):
    ForecastExportJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateForecastResponse(BaseValidatorModel):
    ForecastArn: str
    ResponseMetadata: ResponseMetadata


class CreateMonitorResponse(BaseValidatorModel):
    MonitorArn: str
    ResponseMetadata: ResponseMetadata


class CreatePredictorBacktestExportJobResponse(BaseValidatorModel):
    PredictorBacktestExportJobArn: str
    ResponseMetadata: ResponseMetadata


class CreatePredictorResponse(BaseValidatorModel):
    PredictorArn: str
    ResponseMetadata: ResponseMetadata


class CreateWhatIfAnalysisResponse(BaseValidatorModel):
    WhatIfAnalysisArn: str
    ResponseMetadata: ResponseMetadata


class CreateWhatIfForecastExportResponse(BaseValidatorModel):
    WhatIfForecastExportArn: str
    ResponseMetadata: ResponseMetadata


class CreateWhatIfForecastResponse(BaseValidatorModel):
    WhatIfForecastArn: str
    ResponseMetadata: ResponseMetadata


class DescribeDatasetGroupResponse(BaseValidatorModel):
    DatasetGroupName: str
    DatasetGroupArn: str
    DatasetArns: List[str]
    Domain: DomainType
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ExplainabilitySummary(BaseValidatorModel):
    ExplainabilityArn: Optional[str] = None
    ExplainabilityName: Optional[str] = None
    ResourceArn: Optional[str] = None
    ExplainabilityConfig: Optional[ExplainabilityConfig] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class DataDestination(BaseValidatorModel):
    S3Config: S3Config


class DataSource(BaseValidatorModel):
    S3Config: S3Config


class ListDatasetGroupsResponse(BaseValidatorModel):
    DatasetGroups: List[DatasetGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDatasetsResponse(BaseValidatorModel):
    Datasets: List[DatasetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PredictorSummary(BaseValidatorModel):
    PredictorArn: Optional[str] = None
    PredictorName: Optional[str] = None
    DatasetGroupArn: Optional[str] = None
    IsAutoPredictor: Optional[bool] = None
    ReferencePredictorSummary: Optional[ReferencePredictorSummary] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class FeaturizationOutput(BaseValidatorModel):
    AttributeName: str
    FeaturizationPipeline: Optional[List[FeaturizationMethodOutput]] = None


class Featurization(BaseValidatorModel):
    AttributeName: str
    FeaturizationPipeline: Optional[Sequence[FeaturizationMethod]] = None


class ListDatasetImportJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListExplainabilitiesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListExplainabilityExportsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListForecastExportJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListForecastsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListMonitorEvaluationsRequest(BaseValidatorModel):
    MonitorArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListMonitorsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListPredictorBacktestExportJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListPredictorsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListWhatIfAnalysesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListWhatIfForecastExportsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListWhatIfForecastsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListForecastsResponse(BaseValidatorModel):
    Forecasts: List[ForecastSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InputDataConfigOutput(BaseValidatorModel):
    DatasetGroupArn: str
    SupplementaryFeatures: Optional[List[SupplementaryFeature]] = None


class InputDataConfig(BaseValidatorModel):
    DatasetGroupArn: str
    SupplementaryFeatures: Optional[Sequence[SupplementaryFeature]] = None


class ParameterRangesOutput(BaseValidatorModel):
    CategoricalParameterRanges: Optional[List[CategoricalParameterRangeOutput]] = None
    ContinuousParameterRanges: Optional[List[ContinuousParameterRange]] = None
    IntegerParameterRanges: Optional[List[IntegerParameterRange]] = None


class ParameterRanges(BaseValidatorModel):
    CategoricalParameterRanges: Optional[Sequence[CategoricalParameterRange]] = None
    ContinuousParameterRanges: Optional[Sequence[ContinuousParameterRange]] = None
    IntegerParameterRanges: Optional[Sequence[IntegerParameterRange]] = None


class ListDatasetGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetImportJobsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExplainabilitiesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExplainabilityExportsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListForecastExportJobsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListForecastsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitorEvaluationsRequestPaginate(BaseValidatorModel):
    MonitorArn: str
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitorsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPredictorBacktestExportJobsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPredictorsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWhatIfAnalysesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWhatIfForecastExportsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWhatIfForecastsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitorsResponse(BaseValidatorModel):
    Monitors: List[MonitorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListWhatIfAnalysesResponse(BaseValidatorModel):
    WhatIfAnalyses: List[WhatIfAnalysisSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListWhatIfForecastsResponse(BaseValidatorModel):
    WhatIfForecasts: List[WhatIfForecastSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Metrics(BaseValidatorModel):
    RMSE: Optional[float] = None
    WeightedQuantileLosses: Optional[List[WeightedQuantileLoss]] = None
    ErrorMetrics: Optional[List[ErrorMetric]] = None
    AverageWeightedQuantileLoss: Optional[float] = None


class PredictorMonitorEvaluation(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    MonitorArn: Optional[str] = None
    EvaluationTime: Optional[datetime] = None
    EvaluationState: Optional[str] = None
    WindowStartDatetime: Optional[datetime] = None
    WindowEndDatetime: Optional[datetime] = None
    PredictorEvent: Optional[PredictorEvent] = None
    MonitorDataSource: Optional[MonitorDataSource] = None
    MetricResults: Optional[List[MetricResult]] = None
    NumItemsEvaluated: Optional[int] = None
    Message: Optional[str] = None


class PredictorExecution(BaseValidatorModel):
    AlgorithmArn: Optional[str] = None
    TestWindows: Optional[List[TestWindowSummary]] = None


class SchemaOutput(BaseValidatorModel):
    Attributes: Optional[List[SchemaAttribute]] = None


class Schema(BaseValidatorModel):
    Attributes: Optional[Sequence[SchemaAttribute]] = None


class TimeSeriesTransformationOutput(BaseValidatorModel):
    Action: Optional[Action] = None
    TimeSeriesConditions: Optional[List[TimeSeriesCondition]] = None


class TimeSeriesTransformation(BaseValidatorModel):
    Action: Optional[Action] = None
    TimeSeriesConditions: Optional[Sequence[TimeSeriesCondition]] = None


class DescribeAutoPredictorResponse(BaseValidatorModel):
    PredictorArn: str
    PredictorName: str
    ForecastHorizon: int
    ForecastTypes: List[str]
    ForecastFrequency: str
    ForecastDimensions: List[str]
    DatasetImportJobArns: List[str]
    DataConfig: DataConfigOutput
    EncryptionConfig: EncryptionConfig
    ReferencePredictorSummary: ReferencePredictorSummary
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    OptimizationMetric: OptimizationMetricType
    ExplainabilityInfo: ExplainabilityInfo
    MonitorInfo: MonitorInfo
    TimeAlignmentBoundary: TimeAlignmentBoundary
    ResponseMetadata: ResponseMetadata


class Baseline(BaseValidatorModel):
    PredictorBaseline: Optional[PredictorBaseline] = None


class ListExplainabilitiesResponse(BaseValidatorModel):
    Explainabilities: List[ExplainabilitySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateExplainabilityExportRequest(BaseValidatorModel):
    ExplainabilityExportName: str
    ExplainabilityArn: str
    Destination: DataDestination
    Tags: Optional[Sequence[Tag]] = None
    Format: Optional[str] = None


class CreateForecastExportJobRequest(BaseValidatorModel):
    ForecastExportJobName: str
    ForecastArn: str
    Destination: DataDestination
    Tags: Optional[Sequence[Tag]] = None
    Format: Optional[str] = None


class CreatePredictorBacktestExportJobRequest(BaseValidatorModel):
    PredictorBacktestExportJobName: str
    PredictorArn: str
    Destination: DataDestination
    Tags: Optional[Sequence[Tag]] = None
    Format: Optional[str] = None


class CreateWhatIfForecastExportRequest(BaseValidatorModel):
    WhatIfForecastExportName: str
    WhatIfForecastArns: Sequence[str]
    Destination: DataDestination
    Tags: Optional[Sequence[Tag]] = None
    Format: Optional[str] = None


class DescribeExplainabilityExportResponse(BaseValidatorModel):
    ExplainabilityExportArn: str
    ExplainabilityExportName: str
    ExplainabilityArn: str
    Destination: DataDestination
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadata


class DescribeForecastExportJobResponse(BaseValidatorModel):
    ForecastExportJobArn: str
    ForecastExportJobName: str
    ForecastArn: str
    Destination: DataDestination
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadata


class DescribePredictorBacktestExportJobResponse(BaseValidatorModel):
    PredictorBacktestExportJobArn: str
    PredictorBacktestExportJobName: str
    PredictorArn: str
    Destination: DataDestination
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadata


class DescribeWhatIfForecastExportResponse(BaseValidatorModel):
    WhatIfForecastExportArn: str
    WhatIfForecastExportName: str
    WhatIfForecastArns: List[str]
    Destination: DataDestination
    Message: str
    Status: str
    CreationTime: datetime
    EstimatedTimeRemainingInMinutes: int
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadata


class ExplainabilityExportSummary(BaseValidatorModel):
    ExplainabilityExportArn: Optional[str] = None
    ExplainabilityExportName: Optional[str] = None
    Destination: Optional[DataDestination] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class ForecastExportJobSummary(BaseValidatorModel):
    ForecastExportJobArn: Optional[str] = None
    ForecastExportJobName: Optional[str] = None
    Destination: Optional[DataDestination] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class PredictorBacktestExportJobSummary(BaseValidatorModel):
    PredictorBacktestExportJobArn: Optional[str] = None
    PredictorBacktestExportJobName: Optional[str] = None
    Destination: Optional[DataDestination] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class WhatIfForecastExportSummary(BaseValidatorModel):
    WhatIfForecastExportArn: Optional[str] = None
    WhatIfForecastArns: Optional[List[str]] = None
    WhatIfForecastExportName: Optional[str] = None
    Destination: Optional[DataDestination] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class CreateDatasetImportJobRequest(BaseValidatorModel):
    DatasetImportJobName: str
    DatasetArn: str
    DataSource: DataSource
    TimestampFormat: Optional[str] = None
    TimeZone: Optional[str] = None
    UseGeolocationForTimeZone: Optional[bool] = None
    GeolocationFormat: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    Format: Optional[str] = None
    ImportMode: Optional[ImportModeType] = None


class DatasetImportJobSummary(BaseValidatorModel):
    DatasetImportJobArn: Optional[str] = None
    DatasetImportJobName: Optional[str] = None
    DataSource: Optional[DataSource] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None
    ImportMode: Optional[ImportModeType] = None


class DescribeDatasetImportJobResponse(BaseValidatorModel):
    DatasetImportJobName: str
    DatasetImportJobArn: str
    DatasetArn: str
    TimestampFormat: str
    TimeZone: str
    UseGeolocationForTimeZone: bool
    GeolocationFormat: str
    DataSource: DataSource
    EstimatedTimeRemainingInMinutes: int
    FieldStatistics: Dict[str, Statistics]
    DataSize: float
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ImportMode: ImportModeType
    ResponseMetadata: ResponseMetadata


class ListPredictorsResponse(BaseValidatorModel):
    Predictors: List[PredictorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FeaturizationConfigOutput(BaseValidatorModel):
    ForecastFrequency: str
    ForecastDimensions: Optional[List[str]] = None
    Featurizations: Optional[List[FeaturizationOutput]] = None


class FeaturizationConfig(BaseValidatorModel):
    ForecastFrequency: str
    ForecastDimensions: Optional[Sequence[str]] = None
    Featurizations: Optional[Sequence[Featurization]] = None


class HyperParameterTuningJobConfigOutput(BaseValidatorModel):
    ParameterRanges: Optional[ParameterRangesOutput] = None


class HyperParameterTuningJobConfig(BaseValidatorModel):
    ParameterRanges: Optional[ParameterRanges] = None


class WindowSummary(BaseValidatorModel):
    TestWindowStart: Optional[datetime] = None
    TestWindowEnd: Optional[datetime] = None
    ItemCount: Optional[int] = None
    EvaluationType: Optional[EvaluationTypeType] = None
    Metrics: Optional[Metrics] = None


class ListMonitorEvaluationsResponse(BaseValidatorModel):
    PredictorMonitorEvaluations: List[PredictorMonitorEvaluation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PredictorExecutionDetails(BaseValidatorModel):
    PredictorExecutions: Optional[List[PredictorExecution]] = None


class DescribeDatasetResponse(BaseValidatorModel):
    DatasetArn: str
    DatasetName: str
    Domain: DomainType
    DatasetType: DatasetTypeType
    DataFrequency: str
    Schema: SchemaOutput
    EncryptionConfig: EncryptionConfig
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribeExplainabilityResponse(BaseValidatorModel):
    ExplainabilityArn: str
    ExplainabilityName: str
    ResourceArn: str
    ExplainabilityConfig: ExplainabilityConfig
    EnableVisualization: bool
    DataSource: DataSource
    Schema: SchemaOutput
    StartDateTime: str
    EndDateTime: str
    EstimatedTimeRemainingInMinutes: int
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


class TimeSeriesIdentifiersOutput(BaseValidatorModel):
    DataSource: Optional[DataSource] = None
    Schema: Optional[SchemaOutput] = None
    Format: Optional[str] = None


class TimeSeriesReplacementsDataSourceOutput(BaseValidatorModel):
    S3Config: S3Config
    Schema: SchemaOutput
    Format: Optional[str] = None
    TimestampFormat: Optional[str] = None


class TimeSeriesIdentifiers(BaseValidatorModel):
    DataSource: Optional[DataSource] = None
    Schema: Optional[Schema] = None
    Format: Optional[str] = None


class TimeSeriesReplacementsDataSource(BaseValidatorModel):
    S3Config: S3Config
    Schema: Schema
    Format: Optional[str] = None
    TimestampFormat: Optional[str] = None


class DataConfigUnion(BaseValidatorModel):
    pass


class CreateAutoPredictorRequest(BaseValidatorModel):
    PredictorName: str
    ForecastHorizon: Optional[int] = None
    ForecastTypes: Optional[Sequence[str]] = None
    ForecastDimensions: Optional[Sequence[str]] = None
    ForecastFrequency: Optional[str] = None
    DataConfig: Optional[DataConfigUnion] = None
    EncryptionConfig: Optional[EncryptionConfig] = None
    ReferencePredictorArn: Optional[str] = None
    OptimizationMetric: Optional[OptimizationMetricType] = None
    ExplainPredictor: Optional[bool] = None
    Tags: Optional[Sequence[Tag]] = None
    MonitorConfig: Optional[MonitorConfig] = None
    TimeAlignmentBoundary: Optional[TimeAlignmentBoundary] = None


class DescribeMonitorResponse(BaseValidatorModel):
    MonitorName: str
    MonitorArn: str
    ResourceArn: str
    Status: str
    LastEvaluationTime: datetime
    LastEvaluationState: str
    Baseline: Baseline
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    EstimatedEvaluationTimeRemainingInMinutes: int
    ResponseMetadata: ResponseMetadata


class ListExplainabilityExportsResponse(BaseValidatorModel):
    ExplainabilityExports: List[ExplainabilityExportSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListForecastExportJobsResponse(BaseValidatorModel):
    ForecastExportJobs: List[ForecastExportJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPredictorBacktestExportJobsResponse(BaseValidatorModel):
    PredictorBacktestExportJobs: List[PredictorBacktestExportJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListWhatIfForecastExportsResponse(BaseValidatorModel):
    WhatIfForecastExports: List[WhatIfForecastExportSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDatasetImportJobsResponse(BaseValidatorModel):
    DatasetImportJobs: List[DatasetImportJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EvaluationResult(BaseValidatorModel):
    AlgorithmArn: Optional[str] = None
    TestWindows: Optional[List[WindowSummary]] = None


class DescribePredictorResponse(BaseValidatorModel):
    PredictorArn: str
    PredictorName: str
    AlgorithmArn: str
    AutoMLAlgorithmArns: List[str]
    ForecastHorizon: int
    ForecastTypes: List[str]
    PerformAutoML: bool
    AutoMLOverrideStrategy: AutoMLOverrideStrategyType
    PerformHPO: bool
    TrainingParameters: Dict[str, str]
    EvaluationParameters: EvaluationParameters
    HPOConfig: HyperParameterTuningJobConfigOutput
    InputDataConfig: InputDataConfigOutput
    FeaturizationConfig: FeaturizationConfigOutput
    EncryptionConfig: EncryptionConfig
    PredictorExecutionDetails: PredictorExecutionDetails
    EstimatedTimeRemainingInMinutes: int
    IsAutoPredictor: bool
    DatasetImportJobArns: List[str]
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    OptimizationMetric: OptimizationMetricType
    ResponseMetadata: ResponseMetadata


class TimeSeriesSelectorOutput(BaseValidatorModel):
    TimeSeriesIdentifiers: Optional[TimeSeriesIdentifiersOutput] = None


class DescribeWhatIfForecastResponse(BaseValidatorModel):
    WhatIfForecastName: str
    WhatIfForecastArn: str
    WhatIfAnalysisArn: str
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    TimeSeriesTransformations: List[TimeSeriesTransformationOutput]
    TimeSeriesReplacementsDataSource: TimeSeriesReplacementsDataSourceOutput
    ForecastTypes: List[str]
    ResponseMetadata: ResponseMetadata


class SchemaUnion(BaseValidatorModel):
    pass


class CreateDatasetRequest(BaseValidatorModel):
    DatasetName: str
    Domain: DomainType
    DatasetType: DatasetTypeType
    Schema: SchemaUnion
    DataFrequency: Optional[str] = None
    EncryptionConfig: Optional[EncryptionConfig] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateExplainabilityRequest(BaseValidatorModel):
    ExplainabilityName: str
    ResourceArn: str
    ExplainabilityConfig: ExplainabilityConfig
    DataSource: Optional[DataSource] = None
    Schema: Optional[SchemaUnion] = None
    EnableVisualization: Optional[bool] = None
    StartDateTime: Optional[str] = None
    EndDateTime: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class TimeSeriesSelector(BaseValidatorModel):
    TimeSeriesIdentifiers: Optional[TimeSeriesIdentifiers] = None


class HyperParameterTuningJobConfigUnion(BaseValidatorModel):
    pass


class InputDataConfigUnion(BaseValidatorModel):
    pass


class FeaturizationConfigUnion(BaseValidatorModel):
    pass


class CreatePredictorRequest(BaseValidatorModel):
    PredictorName: str
    ForecastHorizon: int
    InputDataConfig: InputDataConfigUnion
    FeaturizationConfig: FeaturizationConfigUnion
    AlgorithmArn: Optional[str] = None
    ForecastTypes: Optional[Sequence[str]] = None
    PerformAutoML: Optional[bool] = None
    AutoMLOverrideStrategy: Optional[AutoMLOverrideStrategyType] = None
    PerformHPO: Optional[bool] = None
    TrainingParameters: Optional[Mapping[str, str]] = None
    EvaluationParameters: Optional[EvaluationParameters] = None
    HPOConfig: Optional[HyperParameterTuningJobConfigUnion] = None
    EncryptionConfig: Optional[EncryptionConfig] = None
    Tags: Optional[Sequence[Tag]] = None
    OptimizationMetric: Optional[OptimizationMetricType] = None


class GetAccuracyMetricsResponse(BaseValidatorModel):
    PredictorEvaluationResults: List[EvaluationResult]
    IsAutoPredictor: bool
    AutoMLOverrideStrategy: AutoMLOverrideStrategyType
    OptimizationMetric: OptimizationMetricType
    ResponseMetadata: ResponseMetadata


class DescribeForecastResponse(BaseValidatorModel):
    ForecastArn: str
    ForecastName: str
    ForecastTypes: List[str]
    PredictorArn: str
    DatasetGroupArn: str
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    TimeSeriesSelector: TimeSeriesSelectorOutput
    ResponseMetadata: ResponseMetadata


class DescribeWhatIfAnalysisResponse(BaseValidatorModel):
    WhatIfAnalysisName: str
    WhatIfAnalysisArn: str
    ForecastArn: str
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    TimeSeriesSelector: TimeSeriesSelectorOutput
    ResponseMetadata: ResponseMetadata


class TimeSeriesReplacementsDataSourceUnion(BaseValidatorModel):
    pass


class TimeSeriesTransformationUnion(BaseValidatorModel):
    pass


class CreateWhatIfForecastRequest(BaseValidatorModel):
    WhatIfForecastName: str
    WhatIfAnalysisArn: str
    TimeSeriesTransformations: Optional[Sequence[TimeSeriesTransformationUnion]] = None
    TimeSeriesReplacementsDataSource: Optional[TimeSeriesReplacementsDataSourceUnion] = None
    Tags: Optional[Sequence[Tag]] = None


class TimeSeriesSelectorUnion(BaseValidatorModel):
    pass


class CreateForecastRequest(BaseValidatorModel):
    ForecastName: str
    PredictorArn: str
    ForecastTypes: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None
    TimeSeriesSelector: Optional[TimeSeriesSelectorUnion] = None


class CreateWhatIfAnalysisRequest(BaseValidatorModel):
    WhatIfAnalysisName: str
    ForecastArn: str
    TimeSeriesSelector: Optional[TimeSeriesSelectorUnion] = None
    Tags: Optional[Sequence[Tag]] = None


