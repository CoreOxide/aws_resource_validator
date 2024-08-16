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
from aws_resource_validator.pydantic_models.forecast_constants import *

class ActionTypeDef(BaseValidatorModel):
    AttributeName: str
    Operation: OperationType
    Value: float

class AdditionalDatasetTypeDef(BaseValidatorModel):
    Name: str
    Configuration: Optional[Mapping[str, Sequence[str]]] = None

class AttributeConfigTypeDef(BaseValidatorModel):
    AttributeName: str
    Transformations: Mapping[str, str]

class BaselineMetricTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[float] = None

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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class DeleteDatasetGroupRequestRequestTypeDef(BaseValidatorModel):
    DatasetGroupArn: str

class DeleteDatasetImportJobRequestRequestTypeDef(BaseValidatorModel):
    DatasetImportJobArn: str

class DeleteDatasetRequestRequestTypeDef(BaseValidatorModel):
    DatasetArn: str

class DeleteExplainabilityExportRequestRequestTypeDef(BaseValidatorModel):
    ExplainabilityExportArn: str

class DeleteExplainabilityRequestRequestTypeDef(BaseValidatorModel):
    ExplainabilityArn: str

class DeleteForecastExportJobRequestRequestTypeDef(BaseValidatorModel):
    ForecastExportJobArn: str

class DeleteForecastRequestRequestTypeDef(BaseValidatorModel):
    ForecastArn: str

class DeleteMonitorRequestRequestTypeDef(BaseValidatorModel):
    MonitorArn: str

class DeletePredictorBacktestExportJobRequestRequestTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobArn: str

class DeletePredictorRequestRequestTypeDef(BaseValidatorModel):
    PredictorArn: str

class DeleteResourceTreeRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DeleteWhatIfAnalysisRequestRequestTypeDef(BaseValidatorModel):
    WhatIfAnalysisArn: str

class DeleteWhatIfForecastExportRequestRequestTypeDef(BaseValidatorModel):
    WhatIfForecastExportArn: str

class DeleteWhatIfForecastRequestRequestTypeDef(BaseValidatorModel):
    WhatIfForecastArn: str

class DescribeAutoPredictorRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeDatasetGroupRequestRequestTypeDef(BaseValidatorModel):
    DatasetGroupArn: str

class DescribeDatasetImportJobRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeDatasetRequestRequestTypeDef(BaseValidatorModel):
    DatasetArn: str

class DescribeExplainabilityExportRequestRequestTypeDef(BaseValidatorModel):
    ExplainabilityExportArn: str

class DescribeExplainabilityRequestRequestTypeDef(BaseValidatorModel):
    ExplainabilityArn: str

class DescribeForecastExportJobRequestRequestTypeDef(BaseValidatorModel):
    ForecastExportJobArn: str

class DescribeForecastRequestRequestTypeDef(BaseValidatorModel):
    ForecastArn: str

class DescribeMonitorRequestRequestTypeDef(BaseValidatorModel):
    MonitorArn: str

class DescribePredictorBacktestExportJobRequestRequestTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobArn: str

class DescribePredictorRequestRequestTypeDef(BaseValidatorModel):
    PredictorArn: str

class DescribeWhatIfAnalysisRequestRequestTypeDef(BaseValidatorModel):
    WhatIfAnalysisArn: str

class DescribeWhatIfForecastExportRequestRequestTypeDef(BaseValidatorModel):
    WhatIfForecastExportArn: str

class DescribeWhatIfForecastRequestRequestTypeDef(BaseValidatorModel):
    WhatIfForecastArn: str

class ErrorMetricTypeDef(BaseValidatorModel):
    ForecastType: Optional[str] = None
    WAPE: Optional[float] = None
    RMSE: Optional[float] = None
    MASE: Optional[float] = None
    MAPE: Optional[float] = None

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

class GetAccuracyMetricsRequestRequestTypeDef(BaseValidatorModel):
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

class ListDatasetGroupsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDatasetsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MonitorSummaryTypeDef(BaseValidatorModel):
    MonitorArn: Optional[str] = None
    MonitorName: Optional[str] = None
    ResourceArn: Optional[str] = None
    Status: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
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

class ResumeResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class SchemaAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[AttributeTypeType] = None

class StopResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class TimeSeriesConditionTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str
    Condition: ConditionType

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDatasetGroupRequestRequestTypeDef(BaseValidatorModel):
    DatasetGroupArn: str
    DatasetArns: Sequence[str]

class DataConfigTypeDef(BaseValidatorModel):
    DatasetGroupArn: str
    AttributeConfigs: Optional[Sequence[AttributeConfigTypeDef]] = None
    AdditionalDatasets: Optional[Sequence[AdditionalDatasetTypeDef]] = None

class PredictorBaselineTypeDef(BaseValidatorModel):
    BaselineMetrics: Optional[List[BaselineMetricTypeDef]] = None

class CreateDatasetGroupRequestRequestTypeDef(BaseValidatorModel):
    DatasetGroupName: str
    Domain: DomainType
    DatasetArns: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMonitorRequestRequestTypeDef(BaseValidatorModel):
    MonitorName: str
    ResourceArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(BaseValidatorModel):
    Datasets: List[DatasetSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class FeaturizationTypeDef(BaseValidatorModel):
    AttributeName: str
    FeaturizationPipeline: Optional[Sequence[FeaturizationMethodTypeDef]] = None

class ListDatasetImportJobsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListExplainabilitiesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListExplainabilityExportsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListForecastExportJobsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListForecastsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListMonitorEvaluationsRequestRequestTypeDef(BaseValidatorModel):
    MonitorArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListMonitorsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListPredictorBacktestExportJobsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListPredictorsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListWhatIfAnalysesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListWhatIfForecastExportsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListWhatIfForecastsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListForecastsResponseTypeDef(BaseValidatorModel):
    Forecasts: List[ForecastSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InputDataConfigTypeDef(BaseValidatorModel):
    DatasetGroupArn: str
    SupplementaryFeatures: Optional[Sequence[SupplementaryFeatureTypeDef]] = None

class ParameterRangesTypeDef(BaseValidatorModel):
    CategoricalParameterRanges: Optional[Sequence[CategoricalParameterRangeTypeDef]] = None
    ContinuousParameterRanges: Optional[Sequence[ContinuousParameterRangeTypeDef]] = None
    IntegerParameterRanges: Optional[Sequence[IntegerParameterRangeTypeDef]] = None

class ListDatasetGroupsRequestListDatasetGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetImportJobsRequestListDatasetImportJobsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetsRequestListDatasetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExplainabilitiesRequestListExplainabilitiesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExplainabilityExportsRequestListExplainabilityExportsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListForecastExportJobsRequestListForecastExportJobsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListForecastsRequestListForecastsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitorEvaluationsRequestListMonitorEvaluationsPaginateTypeDef(BaseValidatorModel):
    MonitorArn: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitorsRequestListMonitorsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPredictorBacktestExportJobsRequestListPredictorBacktestExportJobsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPredictorsRequestListPredictorsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWhatIfAnalysesRequestListWhatIfAnalysesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWhatIfForecastExportsRequestListWhatIfForecastExportsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWhatIfForecastsRequestListWhatIfForecastsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitorsResponseTypeDef(BaseValidatorModel):
    Monitors: List[MonitorSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWhatIfAnalysesResponseTypeDef(BaseValidatorModel):
    WhatIfAnalyses: List[WhatIfAnalysisSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWhatIfForecastsResponseTypeDef(BaseValidatorModel):
    WhatIfForecasts: List[WhatIfForecastSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class SchemaTypeDef(BaseValidatorModel):
    Attributes: Optional[Sequence[SchemaAttributeTypeDef]] = None

class TimeSeriesTransformationTypeDef(BaseValidatorModel):
    Action: Optional[ActionTypeDef] = None
    TimeSeriesConditions: Optional[Sequence[TimeSeriesConditionTypeDef]] = None

class CreateAutoPredictorRequestRequestTypeDef(BaseValidatorModel):
    PredictorName: str
    ForecastHorizon: Optional[int] = None
    ForecastTypes: Optional[Sequence[str]] = None
    ForecastDimensions: Optional[Sequence[str]] = None
    ForecastFrequency: Optional[str] = None
    DataConfig: Optional[DataConfigTypeDef] = None
    EncryptionConfig: Optional[EncryptionConfigTypeDef] = None
    ReferencePredictorArn: Optional[str] = None
    OptimizationMetric: Optional[OptimizationMetricType] = None
    ExplainPredictor: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    MonitorConfig: Optional[MonitorConfigTypeDef] = None
    TimeAlignmentBoundary: Optional[TimeAlignmentBoundaryTypeDef] = None

class DescribeAutoPredictorResponseTypeDef(BaseValidatorModel):
    PredictorArn: str
    PredictorName: str
    ForecastHorizon: int
    ForecastTypes: List[str]
    ForecastFrequency: str
    ForecastDimensions: List[str]
    DatasetImportJobArns: List[str]
    DataConfig: DataConfigTypeDef
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExplainabilityExportRequestRequestTypeDef(BaseValidatorModel):
    ExplainabilityExportName: str
    ExplainabilityArn: str
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None

class CreateForecastExportJobRequestRequestTypeDef(BaseValidatorModel):
    ForecastExportJobName: str
    ForecastArn: str
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None

class CreatePredictorBacktestExportJobRequestRequestTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobName: str
    PredictorArn: str
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None

class CreateWhatIfForecastExportRequestRequestTypeDef(BaseValidatorModel):
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

class CreateDatasetImportJobRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FeaturizationConfigTypeDef(BaseValidatorModel):
    ForecastFrequency: str
    ForecastDimensions: Optional[Sequence[str]] = None
    Featurizations: Optional[Sequence[FeaturizationTypeDef]] = None

class HyperParameterTuningJobConfigTypeDef(BaseValidatorModel):
    ParameterRanges: Optional[ParameterRangesTypeDef] = None

class WindowSummaryTypeDef(BaseValidatorModel):
    TestWindowStart: Optional[datetime] = None
    TestWindowEnd: Optional[datetime] = None
    ItemCount: Optional[int] = None
    EvaluationType: Optional[EvaluationTypeType] = None
    Metrics: Optional[MetricsTypeDef] = None

class ListMonitorEvaluationsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    PredictorMonitorEvaluations: List[PredictorMonitorEvaluationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PredictorExecutionDetailsTypeDef(BaseValidatorModel):
    PredictorExecutions: Optional[List[PredictorExecutionTypeDef]] = None

class CreateDatasetRequestRequestTypeDef(BaseValidatorModel):
    DatasetName: str
    Domain: DomainType
    DatasetType: DatasetTypeType
    Schema: SchemaTypeDef
    DataFrequency: Optional[str] = None
    EncryptionConfig: Optional[EncryptionConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateExplainabilityRequestRequestTypeDef(BaseValidatorModel):
    ExplainabilityName: str
    ResourceArn: str
    ExplainabilityConfig: ExplainabilityConfigTypeDef
    DataSource: Optional[DataSourceTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None
    EnableVisualization: Optional[bool] = None
    StartDateTime: Optional[str] = None
    EndDateTime: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    DatasetArn: str
    DatasetName: str
    Domain: DomainType
    DatasetType: DatasetTypeType
    DataFrequency: str
    Schema: SchemaTypeDef
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
    Schema: SchemaTypeDef
    StartDateTime: str
    EndDateTime: str
    EstimatedTimeRemainingInMinutes: int
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class TimeSeriesIdentifiersTypeDef(BaseValidatorModel):
    DataSource: Optional[DataSourceTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None
    Format: Optional[str] = None

class TimeSeriesReplacementsDataSourceTypeDef(BaseValidatorModel):
    S3Config: S3ConfigTypeDef
    Schema: SchemaTypeDef
    Format: Optional[str] = None
    TimestampFormat: Optional[str] = None

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListForecastExportJobsResponseTypeDef(BaseValidatorModel):
    ForecastExportJobs: List[ForecastExportJobSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPredictorBacktestExportJobsResponseTypeDef(BaseValidatorModel):
    PredictorBacktestExportJobs: List[PredictorBacktestExportJobSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWhatIfForecastExportsResponseTypeDef(BaseValidatorModel):
    WhatIfForecastExports: List[WhatIfForecastExportSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetImportJobsResponseTypeDef(BaseValidatorModel):
    DatasetImportJobs: List[DatasetImportJobSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePredictorRequestRequestTypeDef(BaseValidatorModel):
    PredictorName: str
    ForecastHorizon: int
    InputDataConfig: InputDataConfigTypeDef
    FeaturizationConfig: FeaturizationConfigTypeDef
    AlgorithmArn: Optional[str] = None
    ForecastTypes: Optional[Sequence[str]] = None
    PerformAutoML: Optional[bool] = None
    AutoMLOverrideStrategy: Optional[AutoMLOverrideStrategyType] = None
    PerformHPO: Optional[bool] = None
    TrainingParameters: Optional[Mapping[str, str]] = None
    EvaluationParameters: Optional[EvaluationParametersTypeDef] = None
    HPOConfig: Optional[HyperParameterTuningJobConfigTypeDef] = None
    EncryptionConfig: Optional[EncryptionConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    OptimizationMetric: Optional[OptimizationMetricType] = None

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
    HPOConfig: HyperParameterTuningJobConfigTypeDef
    InputDataConfig: InputDataConfigTypeDef
    FeaturizationConfig: FeaturizationConfigTypeDef
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

class TimeSeriesSelectorTypeDef(BaseValidatorModel):
    TimeSeriesIdentifiers: Optional[TimeSeriesIdentifiersTypeDef] = None

class CreateWhatIfForecastRequestRequestTypeDef(BaseValidatorModel):
    WhatIfForecastName: str
    WhatIfAnalysisArn: str
    TimeSeriesTransformations: Optional[Sequence[TimeSeriesTransformationTypeDef]] = None
    TimeSeriesReplacementsDataSource: Optional[TimeSeriesReplacementsDataSourceTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeWhatIfForecastResponseTypeDef(BaseValidatorModel):
    WhatIfForecastName: str
    WhatIfForecastArn: str
    WhatIfAnalysisArn: str
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    TimeSeriesTransformations: List[TimeSeriesTransformationTypeDef]
    TimeSeriesReplacementsDataSource: TimeSeriesReplacementsDataSourceTypeDef
    ForecastTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccuracyMetricsResponseTypeDef(BaseValidatorModel):
    PredictorEvaluationResults: List[EvaluationResultTypeDef]
    IsAutoPredictor: bool
    AutoMLOverrideStrategy: AutoMLOverrideStrategyType
    OptimizationMetric: OptimizationMetricType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateForecastRequestRequestTypeDef(BaseValidatorModel):
    ForecastName: str
    PredictorArn: str
    ForecastTypes: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    TimeSeriesSelector: Optional[TimeSeriesSelectorTypeDef] = None

class CreateWhatIfAnalysisRequestRequestTypeDef(BaseValidatorModel):
    WhatIfAnalysisName: str
    ForecastArn: str
    TimeSeriesSelector: Optional[TimeSeriesSelectorTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

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
    TimeSeriesSelector: TimeSeriesSelectorTypeDef
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
    TimeSeriesSelector: TimeSeriesSelectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

