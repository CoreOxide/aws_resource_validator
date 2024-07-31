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
from aws_resource_validator.pydantic_models.forecast_constants import *

class ActionTypeDef(BaseModel):
    AttributeName: str
    Operation: OperationType
    Value: float

class AdditionalDatasetTypeDef(BaseModel):
    Name: str
    Configuration: Optional[Mapping[str, Sequence[str]]] = None

class AttributeConfigTypeDef(BaseModel):
    AttributeName: str
    Transformations: Mapping[str, str]

class BaselineMetricTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[float] = None

class CategoricalParameterRangeTypeDef(BaseModel):
    Name: str
    Values: Sequence[str]

class ContinuousParameterRangeTypeDef(BaseModel):
    Name: str
    MaxValue: float
    MinValue: float
    ScalingType: Optional[ScalingTypeType] = None

class EncryptionConfigTypeDef(BaseModel):
    RoleArn: str
    KMSKeyArn: str

class MonitorConfigTypeDef(BaseModel):
    MonitorName: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class TimeAlignmentBoundaryTypeDef(BaseModel):
    Month: Optional[MonthType] = None
    DayOfMonth: Optional[int] = None
    DayOfWeek: Optional[DayOfWeekType] = None
    Hour: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ExplainabilityConfigTypeDef(BaseModel):
    TimeSeriesGranularity: TimeSeriesGranularityType
    TimePointGranularity: TimePointGranularityType

class EvaluationParametersTypeDef(BaseModel):
    NumberOfBacktestWindows: Optional[int] = None
    BackTestWindowOffset: Optional[int] = None

class S3ConfigTypeDef(BaseModel):
    Path: str
    RoleArn: str
    KMSKeyArn: Optional[str] = None

class DatasetGroupSummaryTypeDef(BaseModel):
    DatasetGroupArn: Optional[str] = None
    DatasetGroupName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class DatasetSummaryTypeDef(BaseModel):
    DatasetArn: Optional[str] = None
    DatasetName: Optional[str] = None
    DatasetType: Optional[DatasetTypeType] = None
    Domain: Optional[DomainType] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class DeleteDatasetGroupRequestRequestTypeDef(BaseModel):
    DatasetGroupArn: str

class DeleteDatasetImportJobRequestRequestTypeDef(BaseModel):
    DatasetImportJobArn: str

class DeleteDatasetRequestRequestTypeDef(BaseModel):
    DatasetArn: str

class DeleteExplainabilityExportRequestRequestTypeDef(BaseModel):
    ExplainabilityExportArn: str

class DeleteExplainabilityRequestRequestTypeDef(BaseModel):
    ExplainabilityArn: str

class DeleteForecastExportJobRequestRequestTypeDef(BaseModel):
    ForecastExportJobArn: str

class DeleteForecastRequestRequestTypeDef(BaseModel):
    ForecastArn: str

class DeleteMonitorRequestRequestTypeDef(BaseModel):
    MonitorArn: str

class DeletePredictorBacktestExportJobRequestRequestTypeDef(BaseModel):
    PredictorBacktestExportJobArn: str

class DeletePredictorRequestRequestTypeDef(BaseModel):
    PredictorArn: str

class DeleteResourceTreeRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DeleteWhatIfAnalysisRequestRequestTypeDef(BaseModel):
    WhatIfAnalysisArn: str

class DeleteWhatIfForecastExportRequestRequestTypeDef(BaseModel):
    WhatIfForecastExportArn: str

class DeleteWhatIfForecastRequestRequestTypeDef(BaseModel):
    WhatIfForecastArn: str

class DescribeAutoPredictorRequestRequestTypeDef(BaseModel):
    PredictorArn: str

class ExplainabilityInfoTypeDef(BaseModel):
    ExplainabilityArn: Optional[str] = None
    Status: Optional[str] = None

class MonitorInfoTypeDef(BaseModel):
    MonitorArn: Optional[str] = None
    Status: Optional[str] = None

class ReferencePredictorSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    State: Optional[StateType] = None

class DescribeDatasetGroupRequestRequestTypeDef(BaseModel):
    DatasetGroupArn: str

class DescribeDatasetImportJobRequestRequestTypeDef(BaseModel):
    DatasetImportJobArn: str

class StatisticsTypeDef(BaseModel):
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

class DescribeDatasetRequestRequestTypeDef(BaseModel):
    DatasetArn: str

class DescribeExplainabilityExportRequestRequestTypeDef(BaseModel):
    ExplainabilityExportArn: str

class DescribeExplainabilityRequestRequestTypeDef(BaseModel):
    ExplainabilityArn: str

class DescribeForecastExportJobRequestRequestTypeDef(BaseModel):
    ForecastExportJobArn: str

class DescribeForecastRequestRequestTypeDef(BaseModel):
    ForecastArn: str

class DescribeMonitorRequestRequestTypeDef(BaseModel):
    MonitorArn: str

class DescribePredictorBacktestExportJobRequestRequestTypeDef(BaseModel):
    PredictorBacktestExportJobArn: str

class DescribePredictorRequestRequestTypeDef(BaseModel):
    PredictorArn: str

class DescribeWhatIfAnalysisRequestRequestTypeDef(BaseModel):
    WhatIfAnalysisArn: str

class DescribeWhatIfForecastExportRequestRequestTypeDef(BaseModel):
    WhatIfForecastExportArn: str

class DescribeWhatIfForecastRequestRequestTypeDef(BaseModel):
    WhatIfForecastArn: str

class ErrorMetricTypeDef(BaseModel):
    ForecastType: Optional[str] = None
    WAPE: Optional[float] = None
    RMSE: Optional[float] = None
    MASE: Optional[float] = None
    MAPE: Optional[float] = None

class FeaturizationMethodTypeDef(BaseModel):
    FeaturizationMethodName: Literal["filling"]
    FeaturizationMethodParameters: Optional[Mapping[str, str]] = None

class FilterTypeDef(BaseModel):
    Key: str
    Value: str
    Condition: FilterConditionStringType

class ForecastSummaryTypeDef(BaseModel):
    ForecastArn: Optional[str] = None
    ForecastName: Optional[str] = None
    PredictorArn: Optional[str] = None
    CreatedUsingAutoPredictor: Optional[bool] = None
    DatasetGroupArn: Optional[str] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class GetAccuracyMetricsRequestRequestTypeDef(BaseModel):
    PredictorArn: str

class SupplementaryFeatureTypeDef(BaseModel):
    Name: str
    Value: str

class IntegerParameterRangeTypeDef(BaseModel):
    Name: str
    MaxValue: int
    MinValue: int
    ScalingType: Optional[ScalingTypeType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDatasetGroupsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDatasetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MonitorSummaryTypeDef(BaseModel):
    MonitorArn: Optional[str] = None
    MonitorName: Optional[str] = None
    ResourceArn: Optional[str] = None
    Status: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class WhatIfAnalysisSummaryTypeDef(BaseModel):
    WhatIfAnalysisArn: Optional[str] = None
    WhatIfAnalysisName: Optional[str] = None
    ForecastArn: Optional[str] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class WhatIfForecastSummaryTypeDef(BaseModel):
    WhatIfForecastArn: Optional[str] = None
    WhatIfForecastName: Optional[str] = None
    WhatIfAnalysisArn: Optional[str] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class MetricResultTypeDef(BaseModel):
    MetricName: Optional[str] = None
    MetricValue: Optional[float] = None

class WeightedQuantileLossTypeDef(BaseModel):
    Quantile: Optional[float] = None
    LossValue: Optional[float] = None

class MonitorDataSourceTypeDef(BaseModel):
    DatasetImportJobArn: Optional[str] = None
    ForecastArn: Optional[str] = None
    PredictorArn: Optional[str] = None

class PredictorEventTypeDef(BaseModel):
    Detail: Optional[str] = None
    Datetime: Optional[datetime] = None

class TestWindowSummaryTypeDef(BaseModel):
    TestWindowStart: Optional[datetime] = None
    TestWindowEnd: Optional[datetime] = None
    Status: Optional[str] = None
    Message: Optional[str] = None

class ResumeResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class SchemaAttributeTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[AttributeTypeType] = None

class StopResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class TimeSeriesConditionTypeDef(BaseModel):
    AttributeName: str
    AttributeValue: str
    Condition: ConditionType

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDatasetGroupRequestRequestTypeDef(BaseModel):
    DatasetGroupArn: str
    DatasetArns: Sequence[str]

class DataConfigTypeDef(BaseModel):
    DatasetGroupArn: str
    AttributeConfigs: Optional[Sequence[AttributeConfigTypeDef]] = None
    AdditionalDatasets: Optional[Sequence[AdditionalDatasetTypeDef]] = None

class PredictorBaselineTypeDef(BaseModel):
    BaselineMetrics: Optional[List[BaselineMetricTypeDef]] = None

class CreateDatasetGroupRequestRequestTypeDef(BaseModel):
    DatasetGroupName: str
    Domain: DomainType
    DatasetArns: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMonitorRequestRequestTypeDef(BaseModel):
    MonitorName: str
    ResourceArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateAutoPredictorResponseTypeDef(BaseModel):
    PredictorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetGroupResponseTypeDef(BaseModel):
    DatasetGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetImportJobResponseTypeDef(BaseModel):
    DatasetImportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(BaseModel):
    DatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExplainabilityExportResponseTypeDef(BaseModel):
    ExplainabilityExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExplainabilityResponseTypeDef(BaseModel):
    ExplainabilityArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateForecastExportJobResponseTypeDef(BaseModel):
    ForecastExportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateForecastResponseTypeDef(BaseModel):
    ForecastArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMonitorResponseTypeDef(BaseModel):
    MonitorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePredictorBacktestExportJobResponseTypeDef(BaseModel):
    PredictorBacktestExportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePredictorResponseTypeDef(BaseModel):
    PredictorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWhatIfAnalysisResponseTypeDef(BaseModel):
    WhatIfAnalysisArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWhatIfForecastExportResponseTypeDef(BaseModel):
    WhatIfForecastExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWhatIfForecastResponseTypeDef(BaseModel):
    WhatIfForecastArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetGroupResponseTypeDef(BaseModel):
    DatasetGroupName: str
    DatasetGroupArn: str
    DatasetArns: List[str]
    Domain: DomainType
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExplainabilitySummaryTypeDef(BaseModel):
    ExplainabilityArn: Optional[str] = None
    ExplainabilityName: Optional[str] = None
    ResourceArn: Optional[str] = None
    ExplainabilityConfig: Optional[ExplainabilityConfigTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class DataDestinationTypeDef(BaseModel):
    S3Config: S3ConfigTypeDef

class DataSourceTypeDef(BaseModel):
    S3Config: S3ConfigTypeDef

class ListDatasetGroupsResponseTypeDef(BaseModel):
    DatasetGroups: List[DatasetGroupSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(BaseModel):
    Datasets: List[DatasetSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PredictorSummaryTypeDef(BaseModel):
    PredictorArn: Optional[str] = None
    PredictorName: Optional[str] = None
    DatasetGroupArn: Optional[str] = None
    IsAutoPredictor: Optional[bool] = None
    ReferencePredictorSummary: Optional[ReferencePredictorSummaryTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class FeaturizationTypeDef(BaseModel):
    AttributeName: str
    FeaturizationPipeline: Optional[Sequence[FeaturizationMethodTypeDef]] = None

class ListDatasetImportJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListExplainabilitiesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListExplainabilityExportsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListForecastExportJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListForecastsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListMonitorEvaluationsRequestRequestTypeDef(BaseModel):
    MonitorArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListMonitorsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListPredictorBacktestExportJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListPredictorsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListWhatIfAnalysesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListWhatIfForecastExportsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListWhatIfForecastsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListForecastsResponseTypeDef(BaseModel):
    Forecasts: List[ForecastSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InputDataConfigTypeDef(BaseModel):
    DatasetGroupArn: str
    SupplementaryFeatures: Optional[Sequence[SupplementaryFeatureTypeDef]] = None

class ParameterRangesTypeDef(BaseModel):
    CategoricalParameterRanges: Optional[Sequence[CategoricalParameterRangeTypeDef]] = None
    ContinuousParameterRanges: Optional[Sequence[ContinuousParameterRangeTypeDef]] = None
    IntegerParameterRanges: Optional[Sequence[IntegerParameterRangeTypeDef]] = None

class ListDatasetGroupsRequestListDatasetGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetImportJobsRequestListDatasetImportJobsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetsRequestListDatasetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExplainabilitiesRequestListExplainabilitiesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExplainabilityExportsRequestListExplainabilityExportsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListForecastExportJobsRequestListForecastExportJobsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListForecastsRequestListForecastsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitorEvaluationsRequestListMonitorEvaluationsPaginateTypeDef(BaseModel):
    MonitorArn: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitorsRequestListMonitorsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPredictorBacktestExportJobsRequestListPredictorBacktestExportJobsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPredictorsRequestListPredictorsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWhatIfAnalysesRequestListWhatIfAnalysesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWhatIfForecastExportsRequestListWhatIfForecastExportsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWhatIfForecastsRequestListWhatIfForecastsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitorsResponseTypeDef(BaseModel):
    Monitors: List[MonitorSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWhatIfAnalysesResponseTypeDef(BaseModel):
    WhatIfAnalyses: List[WhatIfAnalysisSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWhatIfForecastsResponseTypeDef(BaseModel):
    WhatIfForecasts: List[WhatIfForecastSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricsTypeDef(BaseModel):
    RMSE: Optional[float] = None
    WeightedQuantileLosses: Optional[List[WeightedQuantileLossTypeDef]] = None
    ErrorMetrics: Optional[List[ErrorMetricTypeDef]] = None
    AverageWeightedQuantileLoss: Optional[float] = None

class PredictorMonitorEvaluationTypeDef(BaseModel):
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

class PredictorExecutionTypeDef(BaseModel):
    AlgorithmArn: Optional[str] = None
    TestWindows: Optional[List[TestWindowSummaryTypeDef]] = None

class SchemaTypeDef(BaseModel):
    Attributes: Optional[Sequence[SchemaAttributeTypeDef]] = None

class TimeSeriesTransformationTypeDef(BaseModel):
    Action: Optional[ActionTypeDef] = None
    TimeSeriesConditions: Optional[Sequence[TimeSeriesConditionTypeDef]] = None

class CreateAutoPredictorRequestRequestTypeDef(BaseModel):
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

class DescribeAutoPredictorResponseTypeDef(BaseModel):
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

class BaselineTypeDef(BaseModel):
    PredictorBaseline: Optional[PredictorBaselineTypeDef] = None

class ListExplainabilitiesResponseTypeDef(BaseModel):
    Explainabilities: List[ExplainabilitySummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExplainabilityExportRequestRequestTypeDef(BaseModel):
    ExplainabilityExportName: str
    ExplainabilityArn: str
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None

class CreateForecastExportJobRequestRequestTypeDef(BaseModel):
    ForecastExportJobName: str
    ForecastArn: str
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None

class CreatePredictorBacktestExportJobRequestRequestTypeDef(BaseModel):
    PredictorBacktestExportJobName: str
    PredictorArn: str
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None

class CreateWhatIfForecastExportRequestRequestTypeDef(BaseModel):
    WhatIfForecastExportName: str
    WhatIfForecastArns: Sequence[str]
    Destination: DataDestinationTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    Format: Optional[str] = None

class DescribeExplainabilityExportResponseTypeDef(BaseModel):
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

class DescribeForecastExportJobResponseTypeDef(BaseModel):
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

class DescribePredictorBacktestExportJobResponseTypeDef(BaseModel):
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

class DescribeWhatIfForecastExportResponseTypeDef(BaseModel):
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

class ExplainabilityExportSummaryTypeDef(BaseModel):
    ExplainabilityExportArn: Optional[str] = None
    ExplainabilityExportName: Optional[str] = None
    Destination: Optional[DataDestinationTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class ForecastExportJobSummaryTypeDef(BaseModel):
    ForecastExportJobArn: Optional[str] = None
    ForecastExportJobName: Optional[str] = None
    Destination: Optional[DataDestinationTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class PredictorBacktestExportJobSummaryTypeDef(BaseModel):
    PredictorBacktestExportJobArn: Optional[str] = None
    PredictorBacktestExportJobName: Optional[str] = None
    Destination: Optional[DataDestinationTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class WhatIfForecastExportSummaryTypeDef(BaseModel):
    WhatIfForecastExportArn: Optional[str] = None
    WhatIfForecastArns: Optional[List[str]] = None
    WhatIfForecastExportName: Optional[str] = None
    Destination: Optional[DataDestinationTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None

class CreateDatasetImportJobRequestRequestTypeDef(BaseModel):
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

class DatasetImportJobSummaryTypeDef(BaseModel):
    DatasetImportJobArn: Optional[str] = None
    DatasetImportJobName: Optional[str] = None
    DataSource: Optional[DataSourceTypeDef] = None
    Status: Optional[str] = None
    Message: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None
    ImportMode: Optional[ImportModeType] = None

class DescribeDatasetImportJobResponseTypeDef(BaseModel):
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

class ListPredictorsResponseTypeDef(BaseModel):
    Predictors: List[PredictorSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FeaturizationConfigTypeDef(BaseModel):
    ForecastFrequency: str
    ForecastDimensions: Optional[Sequence[str]] = None
    Featurizations: Optional[Sequence[FeaturizationTypeDef]] = None

class HyperParameterTuningJobConfigTypeDef(BaseModel):
    ParameterRanges: Optional[ParameterRangesTypeDef] = None

class WindowSummaryTypeDef(BaseModel):
    TestWindowStart: Optional[datetime] = None
    TestWindowEnd: Optional[datetime] = None
    ItemCount: Optional[int] = None
    EvaluationType: Optional[EvaluationTypeType] = None
    Metrics: Optional[MetricsTypeDef] = None

class ListMonitorEvaluationsResponseTypeDef(BaseModel):
    NextToken: str
    PredictorMonitorEvaluations: List[PredictorMonitorEvaluationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PredictorExecutionDetailsTypeDef(BaseModel):
    PredictorExecutions: Optional[List[PredictorExecutionTypeDef]] = None

class CreateDatasetRequestRequestTypeDef(BaseModel):
    DatasetName: str
    Domain: DomainType
    DatasetType: DatasetTypeType
    Schema: SchemaTypeDef
    DataFrequency: Optional[str] = None
    EncryptionConfig: Optional[EncryptionConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateExplainabilityRequestRequestTypeDef(BaseModel):
    ExplainabilityName: str
    ResourceArn: str
    ExplainabilityConfig: ExplainabilityConfigTypeDef
    DataSource: Optional[DataSourceTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None
    EnableVisualization: Optional[bool] = None
    StartDateTime: Optional[str] = None
    EndDateTime: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeDatasetResponseTypeDef(BaseModel):
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

class DescribeExplainabilityResponseTypeDef(BaseModel):
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

class TimeSeriesIdentifiersTypeDef(BaseModel):
    DataSource: Optional[DataSourceTypeDef] = None
    Schema: Optional[SchemaTypeDef] = None
    Format: Optional[str] = None

class TimeSeriesReplacementsDataSourceTypeDef(BaseModel):
    S3Config: S3ConfigTypeDef
    Schema: SchemaTypeDef
    Format: Optional[str] = None
    TimestampFormat: Optional[str] = None

class DescribeMonitorResponseTypeDef(BaseModel):
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

class ListExplainabilityExportsResponseTypeDef(BaseModel):
    ExplainabilityExports: List[ExplainabilityExportSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListForecastExportJobsResponseTypeDef(BaseModel):
    ForecastExportJobs: List[ForecastExportJobSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPredictorBacktestExportJobsResponseTypeDef(BaseModel):
    PredictorBacktestExportJobs: List[PredictorBacktestExportJobSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWhatIfForecastExportsResponseTypeDef(BaseModel):
    WhatIfForecastExports: List[WhatIfForecastExportSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetImportJobsResponseTypeDef(BaseModel):
    DatasetImportJobs: List[DatasetImportJobSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePredictorRequestRequestTypeDef(BaseModel):
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

class EvaluationResultTypeDef(BaseModel):
    AlgorithmArn: Optional[str] = None
    TestWindows: Optional[List[WindowSummaryTypeDef]] = None

class DescribePredictorResponseTypeDef(BaseModel):
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

class TimeSeriesSelectorTypeDef(BaseModel):
    TimeSeriesIdentifiers: Optional[TimeSeriesIdentifiersTypeDef] = None

class CreateWhatIfForecastRequestRequestTypeDef(BaseModel):
    WhatIfForecastName: str
    WhatIfAnalysisArn: str
    TimeSeriesTransformations: Optional[Sequence[TimeSeriesTransformationTypeDef]] = None
    TimeSeriesReplacementsDataSource: Optional[TimeSeriesReplacementsDataSourceTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeWhatIfForecastResponseTypeDef(BaseModel):
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

class GetAccuracyMetricsResponseTypeDef(BaseModel):
    PredictorEvaluationResults: List[EvaluationResultTypeDef]
    IsAutoPredictor: bool
    AutoMLOverrideStrategy: AutoMLOverrideStrategyType
    OptimizationMetric: OptimizationMetricType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateForecastRequestRequestTypeDef(BaseModel):
    ForecastName: str
    PredictorArn: str
    ForecastTypes: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    TimeSeriesSelector: Optional[TimeSeriesSelectorTypeDef] = None

class CreateWhatIfAnalysisRequestRequestTypeDef(BaseModel):
    WhatIfAnalysisName: str
    ForecastArn: str
    TimeSeriesSelector: Optional[TimeSeriesSelectorTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeForecastResponseTypeDef(BaseModel):
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

class DescribeWhatIfAnalysisResponseTypeDef(BaseModel):
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

