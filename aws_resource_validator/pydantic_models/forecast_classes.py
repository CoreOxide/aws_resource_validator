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

class ActionTypeDef(BaseValidatorModel):
    AttributeName: str
    Operation: OperationType
    Value: float


class AdditionalDatasetOutputTypeDef(BaseValidatorModel):
    Name: str
    Configuration: Optional[Dict[str, List[str]]] = None


class AdditionalDatasetTypeDef(BaseValidatorModel):
    Name: str
    Configuration: Optional[Mapping[str, Sequence[str]]] = None


class AttributeConfigOutputTypeDef(BaseValidatorModel):
    AttributeName: str
    Transformations: Dict[str, str]


class AttributeConfigTypeDef(BaseValidatorModel):
    AttributeName: str
    Transformations: Mapping[str, str]


class BaselineMetricTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[float] = None


class CategoricalParameterRangeOutputTypeDef(BaseValidatorModel):
    Name: str
    Values: List[str]


class CategoricalParameterRangeTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[str]


class ContinuousParameterRangeTypeDef(BaseValidatorModel):
    Name: str
    MaxValue: float
    MinValue: float
    ScalingType: Optional[ScalingTypeType] = None


class EncryptionConfigTypeDef(BaseValidatorModel):
    RoleArn: str
    KMSKeyArn: str


class MonitorConfigTypeDef(BaseValidatorModel):
    MonitorName: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class TimeAlignmentBoundaryTypeDef(BaseValidatorModel):
    Month: Optional[MonthType] = None
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[DayOfWeekType] = None
    Hour: Optional[int] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ExplainabilityConfigTypeDef(BaseValidatorModel):
    TimeSeriesGranularity: TimeSeriesGranularityType
    TimePointGranularity: TimePointGranularityType


class EvaluationParametersTypeDef(BaseValidatorModel):
    NumberOfBacktestWindows: Optional[int] = None
    BackTestWindowOffset: Optional[int] = None


class S3ConfigTypeDef(BaseValidatorModel):
    Path: str
    RoleArn: str
    KMSKeyArn: Optional[str] = None


class DatasetGroupSummaryTypeDef(BaseValidatorModel):
    DatasetGroupArn: Optional[str] = None
    DatasetGroupName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class DatasetSummaryTypeDef(BaseValidatorModel):
    DatasetArn: Optional[str] = None
    DatasetName: Optional[str] = None
    DatasetType: Optional[DatasetTypeType] = None
    Domain: Optional[DomainType] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class DeleteDatasetGroupRequestTypeDef(BaseValidatorModel):
    DatasetGroupArn: str


class DeleteDatasetImportJobRequestTypeDef(BaseValidatorModel):
    DatasetImportJobArn: str


class DeleteDatasetRequestTypeDef(BaseValidatorModel):
    DatasetArn: str


class DeleteExplainabilityExportRequestTypeDef(BaseValidatorModel):
    ExplainabilityExportArn: str


class DeleteExplainabilityRequestTypeDef(BaseValidatorModel):
    ExplainabilityArn: str


class DeleteForecastExportJobRequestTypeDef(BaseValidatorModel):
    ForecastExportJobArn: str


class DeleteForecastRequestTypeDef(BaseValidatorModel):
    ForecastArn: str


class DeleteMonitorRequestTypeDef(BaseValidatorModel):
    MonitorArn: str


class DeletePredictorBacktestExportJobRequestTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobArn: str


class DeletePredictorRequestTypeDef(BaseValidatorModel):
    PredictorArn: str


class DeleteResourceTreeRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DeleteWhatIfAnalysisRequestTypeDef(BaseValidatorModel):
    WhatIfAnalysisArn: str


class DeleteWhatIfForecastExportRequestTypeDef(BaseValidatorModel):
    WhatIfForecastExportArn: str


class DeleteWhatIfForecastRequestTypeDef(BaseValidatorModel):
    WhatIfForecastArn: str


class DescribeAutoPredictorRequestTypeDef(BaseValidatorModel):
    PredictorArn: str


class ExplainabilityInfoTypeDef(BaseValidatorModel):
    ExplainabilityArn: Optional[str] = None
    Status: Optional[str] = None


class MonitorInfoTypeDef(BaseValidatorModel):
    MonitorArn: Optional[str] = None
    Status: Optional[str] = None


class ReferencePredictorSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    State: Optional[StateType] = None


class DescribeDatasetGroupRequestTypeDef(BaseValidatorModel):
    DatasetGroupArn: str


class DescribeDatasetImportJobRequestTypeDef(BaseValidatorModel):
    DatasetImportJobArn: str


class StatisticsTypeDef(BaseValidatorModel):
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


class DescribeDatasetRequestTypeDef(BaseValidatorModel):
    DatasetArn: str


class DescribeExplainabilityExportRequestTypeDef(BaseValidatorModel):
    ExplainabilityExportArn: str


class DescribeExplainabilityRequestTypeDef(BaseValidatorModel):
    ExplainabilityArn: str


class DescribeForecastExportJobRequestTypeDef(BaseValidatorModel):
    ForecastExportJobArn: str


class DescribeForecastRequestTypeDef(BaseValidatorModel):
    ForecastArn: str


class DescribeMonitorRequestTypeDef(BaseValidatorModel):
    MonitorArn: str


class DescribePredictorBacktestExportJobRequestTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobArn: str


class DescribePredictorRequestTypeDef(BaseValidatorModel):
    PredictorArn: str


class DescribeWhatIfAnalysisRequestTypeDef(BaseValidatorModel):
    WhatIfAnalysisArn: str


class DescribeWhatIfForecastExportRequestTypeDef(BaseValidatorModel):
    WhatIfForecastExportArn: str


class DescribeWhatIfForecastRequestTypeDef(BaseValidatorModel):
    WhatIfForecastArn: str


class ErrorMetricTypeDef(BaseValidatorModel):
    ForecastType: Optional[str] = None
    WAPE: Optional[float] = None
    RMSE: Optional[float] = None
    MASE: Optional[float] = None
    MAPE: Optional[float] = None


class FeaturizationMethodOutputTypeDef(BaseValidatorModel):
    FeaturizationMethodName: Literal["filling"]
    FeaturizationMethodParameters: Optional[Dict[str, str]] = None


class FeaturizationMethodTypeDef(BaseValidatorModel):
    FeaturizationMethodName: Literal["filling"]
    FeaturizationMethodParameters: Optional[Mapping[str, str]] = None


class FilterTypeDef(BaseValidatorModel):
    Key: str
    Value: str
    Condition: FilterConditionStringType


class ForecastSummaryTypeDef(BaseValidatorModel):
    ForecastArn: Optional[str] = None
    ForecastName: Optional[str] = None
    PredictorArn: Optional[str] = None
    CreatedUsingAutoPredictor: Optional[bool] = None
    DatasetGroupArn: Optional[str] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class GetAccuracyMetricsRequestTypeDef(BaseValidatorModel):
    PredictorArn: str


class SupplementaryFeatureTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class IntegerParameterRangeTypeDef(BaseValidatorModel):
    Name: str
    MaxValue: int
    MinValue: int
    ScalingType: Optional[ScalingTypeType] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDatasetGroupsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDatasetsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MonitorSummaryTypeDef(BaseValidatorModel):
    MonitorArn: Optional[str] = None
    MonitorName: Optional[str] = None
    ResourceArn: Optional[str] = None
    Status: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class WhatIfAnalysisSummaryTypeDef(BaseValidatorModel):
    WhatIfAnalysisArn: Optional[str] = None
    WhatIfAnalysisName: Optional[str] = None
    ForecastArn: Optional[str] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class WhatIfForecastSummaryTypeDef(BaseValidatorModel):
    WhatIfForecastArn: Optional[str] = None
    WhatIfForecastName: Optional[str] = None
    WhatIfAnalysisArn: Optional[str] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class MetricResultTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    MetricValue: Optional[float] = None


class WeightedQuantileLossTypeDef(BaseValidatorModel):
    Quantile: Optional[float] = None
    LossValue: Optional[float] = None


class MonitorDataSourceTypeDef(BaseValidatorModel):
    DatasetImportJobArn: Optional[str] = None
    ForecastArn: Optional[str] = None
    PredictorArn: Optional[str] = None


class PredictorEventTypeDef(BaseValidatorModel):
    Detail: Optional[str] = None
    Datetime: Optional[datetime] = None


class TestWindowSummaryTypeDef(BaseValidatorModel):
    TestWindowStart: Optional[datetime] = None
    TestWindowEnd: Optional[datetime] = None
    Status: Optional[str] = None
    Message: Optional[str] = None


class ResumeResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class SchemaAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[AttributeTypeType] = None


class StopResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class TimeSeriesConditionTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str
    Condition: ConditionType


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateDatasetGroupRequestTypeDef(BaseValidatorModel):
    DatasetGroupArn: str
    DatasetArns: Sequence[str]


class DataConfigOutputTypeDef(BaseValidatorModel):
    DatasetGroupArn: str
    AttributeConfigs: Optional[List[AttributeConfigOutputTypeDef]] = None
    AdditionalDatasets: Optional[List[AdditionalDatasetOutputTypeDef]] = None


class DataConfigTypeDef(BaseValidatorModel):
    DatasetGroupArn: str
    AttributeConfigs: Optional[Sequence[AttributeConfigTypeDef]] = None
    AdditionalDatasets: Optional[Sequence[AdditionalDatasetTypeDef]] = None


class PredictorBaselineTypeDef(BaseValidatorModel):
    BaselineMetrics: Optional[List[BaselineMetricTypeDef]] = None


class CreateDatasetGroupRequestTypeDef(BaseValidatorModel):
    DatasetGroupName: str
    Domain: DomainType
    DatasetArns: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateMonitorRequestTypeDef(BaseValidatorModel):
    MonitorName: str
    ResourceArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateAutoPredictorResponseTypeDef(BaseValidatorModel):
    PredictorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetGroupResponseTypeDef(BaseValidatorModel):
    DatasetGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetImportJobResponseTypeDef(BaseValidatorModel):
    DatasetImportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetResponseTypeDef(BaseValidatorModel):
    DatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateExplainabilityExportResponseTypeDef(BaseValidatorModel):
    ExplainabilityExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateExplainabilityResponseTypeDef(BaseValidatorModel):
    ExplainabilityArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateForecastExportJobResponseTypeDef(BaseValidatorModel):
    ForecastExportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateForecastResponseTypeDef(BaseValidatorModel):
    ForecastArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMonitorResponseTypeDef(BaseValidatorModel):
    MonitorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePredictorBacktestExportJobResponseTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePredictorResponseTypeDef(BaseValidatorModel):
    PredictorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWhatIfAnalysisResponseTypeDef(BaseValidatorModel):
    WhatIfAnalysisArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWhatIfForecastExportResponseTypeDef(BaseValidatorModel):
    WhatIfForecastExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWhatIfForecastResponseTypeDef(BaseValidatorModel):
    WhatIfForecastArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDatasetGroupResponseTypeDef(BaseValidatorModel):
    DatasetGroupName: str
    DatasetGroupArn: str
    DatasetArns: List[str]
    Domain: DomainType
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ExplainabilitySummaryTypeDef(BaseValidatorModel):
    ExplainabilityArn: Optional[str] = None
    ExplainabilityName: Optional[str] = None
    ResourceArn: Optional[str] = None
    ExplainabilityConfig: Optional[ExplainabilityConfigTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class DataDestinationTypeDef(BaseValidatorModel):
    S3Config: S3ConfigTypeDef


class DataSourceTypeDef(BaseValidatorModel):
    S3Config: S3ConfigTypeDef


class ListDatasetGroupsResponseTypeDef(BaseValidatorModel):
    DatasetGroups: List[DatasetGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDatasetsResponseTypeDef(BaseValidatorModel):
    Datasets: List[DatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PredictorSummaryTypeDef(BaseValidatorModel):
    PredictorArn: Optional[str] = None
    PredictorName: Optional[str] = None
    DatasetGroupArn: Optional[str] = None
    IsAutoPredictor: Optional[bool] = None
    ReferencePredictorSummary: Optional[ReferencePredictorSummaryTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class FeaturizationOutputTypeDef(BaseValidatorModel):
    AttributeName: str
    FeaturizationPipeline: Optional[List[FeaturizationMethodOutputTypeDef]] = None


class FeaturizationTypeDef(BaseValidatorModel):
    AttributeName: str
    FeaturizationPipeline: Optional[Sequence[FeaturizationMethodTypeDef]] = None


class ListDatasetImportJobsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListExplainabilitiesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListExplainabilityExportsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListForecastExportJobsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListForecastsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListMonitorEvaluationsRequestTypeDef(BaseValidatorModel):
    MonitorArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListMonitorsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListPredictorBacktestExportJobsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListPredictorsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListWhatIfAnalysesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListWhatIfForecastExportsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListWhatIfForecastsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListForecastsResponseTypeDef(BaseValidatorModel):
    Forecasts: List[ForecastSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class InputDataConfigOutputTypeDef(BaseValidatorModel):
    DatasetGroupArn: str
    SupplementaryFeatures: Optional[List[SupplementaryFeatureTypeDef]] = None


class InputDataConfigTypeDef(BaseValidatorModel):
    DatasetGroupArn: str
    SupplementaryFeatures: Optional[Sequence[SupplementaryFeatureTypeDef]] = None


class ParameterRangesOutputTypeDef(BaseValidatorModel):
    CategoricalParameterRanges: Optional[List[CategoricalParameterRangeOutputTypeDef]] = None
    ContinuousParameterRanges: Optional[List[ContinuousParameterRangeTypeDef]] = None
    IntegerParameterRanges: Optional[List[IntegerParameterRangeTypeDef]] = None


class ParameterRangesTypeDef(BaseValidatorModel):
    CategoricalParameterRanges: Optional[Sequence[CategoricalParameterRangeTypeDef]] = None
    ContinuousParameterRanges: Optional[Sequence[ContinuousParameterRangeTypeDef]] = None
    IntegerParameterRanges: Optional[Sequence[IntegerParameterRangeTypeDef]] = None


class ListDatasetGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetImportJobsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExplainabilitiesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExplainabilityExportsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListForecastExportJobsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListForecastsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMonitorEvaluationsRequestPaginateTypeDef(BaseValidatorModel):
    MonitorArn: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMonitorsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPredictorBacktestExportJobsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPredictorsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWhatIfAnalysesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWhatIfForecastExportsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWhatIfForecastsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMonitorsResponseTypeDef(BaseValidatorModel):
    Monitors: List[MonitorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListWhatIfAnalysesResponseTypeDef(BaseValidatorModel):
    WhatIfAnalyses: List[WhatIfAnalysisSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListWhatIfForecastsResponseTypeDef(BaseValidatorModel):
    WhatIfForecasts: List[WhatIfForecastSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MetricsTypeDef(BaseValidatorModel):
    RMSE: Optional[float] = None
    WeightedQuantileLosses: Optional[List[WeightedQuantileLossTypeDef]] = None
    ErrorMetrics: Optional[List[ErrorMetricTypeDef]] = None
    AverageWeightedQuantileLoss: Optional[float] = None


class PredictorMonitorEvaluationTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    MonitorArn: Optional[str] = None
    EvaluationTime: Optional[datetime] = None
    EvaluationState: Optional[str] = None
    WindowStartDatetime: Optional[datetime] = None
    WindowEndDatetime: Optional[datetime] = None
    PredictorEvent: Optional[PredictorEventTypeDef] = None
    MonitorDataSource: Optional[MonitorDataSourceTypeDef] = None
    MetricResults: Optional[List[MetricResultTypeDef]] = None
    NumItemsEvaluated: Optional[int] = None
    Message: Optional[str] = None


class PredictorExecutionTypeDef(BaseValidatorModel):
    AlgorithmArn: Optional[str] = None
    TestWindows: Optional[List[TestWindowSummaryTypeDef]] = None


class SchemaOutputTypeDef(BaseValidatorModel):
    Attributes: Optional[List[SchemaAttributeTypeDef]] = None


class SchemaTypeDef(BaseValidatorModel):
    Attributes: Optional[Sequence[SchemaAttributeTypeDef]] = None


class TimeSeriesTransformationOutputTypeDef(BaseValidatorModel):
    Action: Optional[ActionTypeDef] = None
    TimeSeriesConditions: Optional[List[TimeSeriesConditionTypeDef]] = None


class TimeSeriesTransformationTypeDef(BaseValidatorModel):
    Action: Optional[ActionTypeDef] = None
    TimeSeriesConditions: Optional[Sequence[TimeSeriesConditionTypeDef]] = None


class DescribeAutoPredictorResponseTypeDef(BaseValidatorModel):
    PredictorArn: str
    PredictorName: str
    ForecastHorizon: int
    ForecastTypes: List[str]
    ForecastFrequency: str
    ForecastDimensions: List[str]
    DatasetImportJobArns: List[str]
    DataConfig: DataConfigOutputTypeDef
    EncryptionConfig: EncryptionConfigTypeDef
    ReferencePredictorSummary: ReferencePredictorSummaryTypeDef
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    OptimizationMetric: OptimizationMetricType
    ExplainabilityInfo: ExplainabilityInfoTypeDef
    MonitorInfo: MonitorInfoTypeDef
    TimeAlignmentBoundary: TimeAlignmentBoundaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BaselineTypeDef(BaseValidatorModel):
    PredictorBaseline: Optional[PredictorBaselineTypeDef] = None


class ListExplainabilitiesResponseTypeDef(BaseValidatorModel):
    Explainabilities: List[ExplainabilitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateExplainabilityExportRequestTypeDef(BaseValidatorModel):
    ExplainabilityExportName: str
    ExplainabilityArn: str
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None


class CreateForecastExportJobRequestTypeDef(BaseValidatorModel):
    ForecastExportJobName: str
    ForecastArn: str
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None


class CreatePredictorBacktestExportJobRequestTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobName: str
    PredictorArn: str
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None


class CreateWhatIfForecastExportRequestTypeDef(BaseValidatorModel):
    WhatIfForecastExportName: str
    WhatIfForecastArns: Sequence[str]
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None


class DescribeExplainabilityExportResponseTypeDef(BaseValidatorModel):
    ExplainabilityExportArn: str
    ExplainabilityExportName: str
    ExplainabilityArn: str
    Destination: DataDestinationTypeDef
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeForecastExportJobResponseTypeDef(BaseValidatorModel):
    ForecastExportJobArn: str
    ForecastExportJobName: str
    ForecastArn: str
    Destination: DataDestinationTypeDef
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePredictorBacktestExportJobResponseTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobArn: str
    PredictorBacktestExportJobName: str
    PredictorArn: str
    Destination: DataDestinationTypeDef
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWhatIfForecastExportResponseTypeDef(BaseValidatorModel):
    WhatIfForecastExportArn: str
    WhatIfForecastExportName: str
    WhatIfForecastArns: List[str]
    Destination: DataDestinationTypeDef
    Message: str
    Status: str
    CreationTime: datetime
    EstimatedTimeRemainingInMinutes: int
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadataTypeDef


class ExplainabilityExportSummaryTypeDef(BaseValidatorModel):
    ExplainabilityExportArn: Optional[str] = None
    ExplainabilityExportName: Optional[str] = None
    Destination: Optional[DataDestinationTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class ForecastExportJobSummaryTypeDef(BaseValidatorModel):
    ForecastExportJobArn: Optional[str] = None
    ForecastExportJobName: Optional[str] = None
    Destination: Optional[DataDestinationTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class PredictorBacktestExportJobSummaryTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobArn: Optional[str] = None
    PredictorBacktestExportJobName: Optional[str] = None
    Destination: Optional[DataDestinationTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class WhatIfForecastExportSummaryTypeDef(BaseValidatorModel):
    WhatIfForecastExportArn: Optional[str] = None
    WhatIfForecastArns: Optional[List[str]] = None
    WhatIfForecastExportName: Optional[str] = None
    Destination: Optional[DataDestinationTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None


class CreateDatasetImportJobRequestTypeDef(BaseValidatorModel):
    DatasetImportJobName: str
    DatasetArn: str
    DataSource: DataSourceTypeDef
    TimestampFormat: Optional[str] = None
    TimeZone: Optional[str] = None
    UseGeolocationForTimeZone: Optional[bool] = None
    GeolocationFormat: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None
    ImportMode: Optional[ImportModeType] = None


class DatasetImportJobSummaryTypeDef(BaseValidatorModel):
    DatasetImportJobArn: Optional[str] = None
    DatasetImportJobName: Optional[str] = None
    DataSource: Optional[DataSourceTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None
    ImportMode: Optional[ImportModeType] = None


class DescribeDatasetImportJobResponseTypeDef(BaseValidatorModel):
    DatasetImportJobName: str
    DatasetImportJobArn: str
    DatasetArn: str
    TimestampFormat: str
    TimeZone: str
    UseGeolocationForTimeZone: bool
    GeolocationFormat: str
    DataSource: DataSourceTypeDef
    EstimatedTimeRemainingInMinutes: int
    FieldStatistics: Dict[str, StatisticsTypeDef]
    DataSize: float
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ImportMode: ImportModeType
    ResponseMetadata: ResponseMetadataTypeDef


class ListPredictorsResponseTypeDef(BaseValidatorModel):
    Predictors: List[PredictorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class FeaturizationConfigOutputTypeDef(BaseValidatorModel):
    ForecastFrequency: str
    ForecastDimensions: Optional[List[str]] = None
    Featurizations: Optional[List[FeaturizationOutputTypeDef]] = None


class FeaturizationConfigTypeDef(BaseValidatorModel):
    ForecastFrequency: str
    ForecastDimensions: Optional[Sequence[str]] = None
    Featurizations: Optional[Sequence[FeaturizationTypeDef]] = None


class HyperParameterTuningJobConfigOutputTypeDef(BaseValidatorModel):
    ParameterRanges: Optional[ParameterRangesOutputTypeDef] = None


class HyperParameterTuningJobConfigTypeDef(BaseValidatorModel):
    ParameterRanges: Optional[ParameterRangesTypeDef] = None


class WindowSummaryTypeDef(BaseValidatorModel):
    TestWindowStart: Optional[datetime] = None
    TestWindowEnd: Optional[datetime] = None
    ItemCount: Optional[int] = None
    EvaluationType: Optional[EvaluationTypeType] = None
    Metrics: Optional[MetricsTypeDef] = None


class ListMonitorEvaluationsResponseTypeDef(BaseValidatorModel):
    PredictorMonitorEvaluations: List[PredictorMonitorEvaluationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PredictorExecutionDetailsTypeDef(BaseValidatorModel):
    PredictorExecutions: Optional[List[PredictorExecutionTypeDef]] = None


class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    DatasetArn: str
    DatasetName: str
    Domain: DomainType
    DatasetType: DatasetTypeType
    DataFrequency: str
    Schema: SchemaOutputTypeDef
    EncryptionConfig: EncryptionConfigTypeDef
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeExplainabilityResponseTypeDef(BaseValidatorModel):
    ExplainabilityArn: str
    ExplainabilityName: str
    ResourceArn: str
    ExplainabilityConfig: ExplainabilityConfigTypeDef
    EnableVisualization: bool
    DataSource: DataSourceTypeDef
    Schema: SchemaOutputTypeDef
    StartDateTime: str
    EndDateTime: str
    EstimatedTimeRemainingInMinutes: int
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class TimeSeriesIdentifiersOutputTypeDef(BaseValidatorModel):
    DataSource: Optional[DataSourceTypeDef] = None
    Schema: Optional[SchemaOutputTypeDef] = None
    Format: Optional[str] = None


class TimeSeriesReplacementsDataSourceOutputTypeDef(BaseValidatorModel):
    S3Config: S3ConfigTypeDef
    Schema: SchemaOutputTypeDef
    Format: Optional[str] = None
    TimestampFormat: Optional[str] = None


class TimeSeriesIdentifiersTypeDef(BaseValidatorModel):
    DataSource: Optional[DataSourceTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None
    Format: Optional[str] = None


class TimeSeriesReplacementsDataSourceTypeDef(BaseValidatorModel):
    S3Config: S3ConfigTypeDef
    Schema: SchemaTypeDef
    Format: Optional[str] = None
    TimestampFormat: Optional[str] = None


class DataConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateAutoPredictorRequestTypeDef(BaseValidatorModel):
    PredictorName: str
    ForecastHorizon: Optional[int] = None
    ForecastTypes: Optional[Sequence[str]] = None
    ForecastDimensions: Optional[Sequence[str]] = None
    ForecastFrequency: Optional[str] = None
    DataConfig: Optional[DataConfigUnionTypeDef] = None
    EncryptionConfig: Optional[EncryptionConfigTypeDef] = None
    ReferencePredictorArn: Optional[str] = None
    OptimizationMetric: Optional[OptimizationMetricType] = None
    ExplainPredictor: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    MonitorConfig: Optional[MonitorConfigTypeDef] = None
    TimeAlignmentBoundary: Optional[TimeAlignmentBoundaryTypeDef] = None


class DescribeMonitorResponseTypeDef(BaseValidatorModel):
    MonitorName: str
    MonitorArn: str
    ResourceArn: str
    Status: str
    LastEvaluationTime: datetime
    LastEvaluationState: str
    Baseline: BaselineTypeDef
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    EstimatedEvaluationTimeRemainingInMinutes: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListExplainabilityExportsResponseTypeDef(BaseValidatorModel):
    ExplainabilityExports: List[ExplainabilityExportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListForecastExportJobsResponseTypeDef(BaseValidatorModel):
    ForecastExportJobs: List[ForecastExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPredictorBacktestExportJobsResponseTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobs: List[PredictorBacktestExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListWhatIfForecastExportsResponseTypeDef(BaseValidatorModel):
    WhatIfForecastExports: List[WhatIfForecastExportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDatasetImportJobsResponseTypeDef(BaseValidatorModel):
    DatasetImportJobs: List[DatasetImportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EvaluationResultTypeDef(BaseValidatorModel):
    AlgorithmArn: Optional[str] = None
    TestWindows: Optional[List[WindowSummaryTypeDef]] = None


class DescribePredictorResponseTypeDef(BaseValidatorModel):
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
    EvaluationParameters: EvaluationParametersTypeDef
    HPOConfig: HyperParameterTuningJobConfigOutputTypeDef
    InputDataConfig: InputDataConfigOutputTypeDef
    FeaturizationConfig: FeaturizationConfigOutputTypeDef
    EncryptionConfig: EncryptionConfigTypeDef
    PredictorExecutionDetails: PredictorExecutionDetailsTypeDef
    EstimatedTimeRemainingInMinutes: int
    IsAutoPredictor: bool
    DatasetImportJobArns: List[str]
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    OptimizationMetric: OptimizationMetricType
    ResponseMetadata: ResponseMetadataTypeDef


class TimeSeriesSelectorOutputTypeDef(BaseValidatorModel):
    TimeSeriesIdentifiers: Optional[TimeSeriesIdentifiersOutputTypeDef] = None


class DescribeWhatIfForecastResponseTypeDef(BaseValidatorModel):
    WhatIfForecastName: str
    WhatIfForecastArn: str
    WhatIfAnalysisArn: str
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    TimeSeriesTransformations: List[TimeSeriesTransformationOutputTypeDef]
    TimeSeriesReplacementsDataSource: TimeSeriesReplacementsDataSourceOutputTypeDef
    ForecastTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class SchemaUnionTypeDef(BaseValidatorModel):
    pass


class CreateDatasetRequestTypeDef(BaseValidatorModel):
    DatasetName: str
    Domain: DomainType
    DatasetType: DatasetTypeType
    Schema: SchemaUnionTypeDef
    DataFrequency: Optional[str] = None
    EncryptionConfig: Optional[EncryptionConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateExplainabilityRequestTypeDef(BaseValidatorModel):
    ExplainabilityName: str
    ResourceArn: str
    ExplainabilityConfig: ExplainabilityConfigTypeDef
    DataSource: Optional[DataSourceTypeDef] = None
    Schema: Optional[SchemaUnionTypeDef] = None
    EnableVisualization: Optional[bool] = None
    StartDateTime: Optional[str] = None
    EndDateTime: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TimeSeriesSelectorTypeDef(BaseValidatorModel):
    TimeSeriesIdentifiers: Optional[TimeSeriesIdentifiersTypeDef] = None


class HyperParameterTuningJobConfigUnionTypeDef(BaseValidatorModel):
    pass


class InputDataConfigUnionTypeDef(BaseValidatorModel):
    pass


class FeaturizationConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreatePredictorRequestTypeDef(BaseValidatorModel):
    PredictorName: str
    ForecastHorizon: int
    InputDataConfig: InputDataConfigUnionTypeDef
    FeaturizationConfig: FeaturizationConfigUnionTypeDef
    AlgorithmArn: Optional[str] = None
    ForecastTypes: Optional[Sequence[str]] = None
    PerformAutoML: Optional[bool] = None
    AutoMLOverrideStrategy: Optional[AutoMLOverrideStrategyType] = None
    PerformHPO: Optional[bool] = None
    TrainingParameters: Optional[Mapping[str, str]] = None
    EvaluationParameters: Optional[EvaluationParametersTypeDef] = None
    HPOConfig: Optional[HyperParameterTuningJobConfigUnionTypeDef] = None
    EncryptionConfig: Optional[EncryptionConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    OptimizationMetric: Optional[OptimizationMetricType] = None


class GetAccuracyMetricsResponseTypeDef(BaseValidatorModel):
    PredictorEvaluationResults: List[EvaluationResultTypeDef]
    IsAutoPredictor: bool
    AutoMLOverrideStrategy: AutoMLOverrideStrategyType
    OptimizationMetric: OptimizationMetricType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeForecastResponseTypeDef(BaseValidatorModel):
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
    TimeSeriesSelector: TimeSeriesSelectorOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWhatIfAnalysisResponseTypeDef(BaseValidatorModel):
    WhatIfAnalysisName: str
    WhatIfAnalysisArn: str
    ForecastArn: str
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    TimeSeriesSelector: TimeSeriesSelectorOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TimeSeriesReplacementsDataSourceUnionTypeDef(BaseValidatorModel):
    pass


class TimeSeriesTransformationUnionTypeDef(BaseValidatorModel):
    pass


class CreateWhatIfForecastRequestTypeDef(BaseValidatorModel):
    WhatIfForecastName: str
    WhatIfAnalysisArn: str
    TimeSeriesTransformations: Optional[Sequence[TimeSeriesTransformationUnionTypeDef]] = None
    TimeSeriesReplacementsDataSource: Optional[TimeSeriesReplacementsDataSourceUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TimeSeriesSelectorUnionTypeDef(BaseValidatorModel):
    pass


class CreateForecastRequestTypeDef(BaseValidatorModel):
    ForecastName: str
    PredictorArn: str
    ForecastTypes: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    TimeSeriesSelector: Optional[TimeSeriesSelectorUnionTypeDef] = None


class CreateWhatIfAnalysisRequestTypeDef(BaseValidatorModel):
    WhatIfAnalysisName: str
    ForecastArn: str
    TimeSeriesSelector: Optional[TimeSeriesSelectorUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


