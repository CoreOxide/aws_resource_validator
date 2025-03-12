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
from aws_resource_validator.pydantic_models.pi_constants import *

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DataPointTypeDef(BaseValidatorModel):
    Timestamp: datetime
    Value: float


class PerformanceInsightsMetricTypeDef(BaseValidatorModel):
    Metric: Optional[str] = None
    DisplayName: Optional[str] = None
    Dimensions: Optional[Dict[str, str]] = None
    Filter: Optional[Dict[str, str]] = None
    Value: Optional[float] = None


class DeletePerformanceAnalysisReportRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    AnalysisReportId: str


class DimensionGroupTypeDef(BaseValidatorModel):
    Group: str
    Dimensions: Optional[Sequence[str]] = None
    Limit: Optional[int] = None


class DimensionKeyDescriptionTypeDef(BaseValidatorModel):
    Dimensions: Optional[Dict[str, str]] = None
    Total: Optional[float] = None
    AdditionalMetrics: Optional[Dict[str, float]] = None
    Partitions: Optional[List[float]] = None


class ResponsePartitionKeyTypeDef(BaseValidatorModel):
    Dimensions: Dict[str, str]


class DimensionDetailTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None


class DimensionKeyDetailTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Dimension: Optional[str] = None
    Status: Optional[DetailStatusType] = None


class FeatureMetadataTypeDef(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None


class GetDimensionKeyDetailsRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    Group: str
    GroupIdentifier: str
    RequestedDimensions: Optional[Sequence[str]] = None


class GetPerformanceAnalysisReportRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    AnalysisReportId: str
    TextFormat: Optional[TextFormatType] = None
    AcceptLanguage: Optional[Literal["EN_US"]] = None


class GetResourceMetadataRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str


class RecommendationTypeDef(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    RecommendationDescription: Optional[str] = None


class ListAvailableResourceDimensionsRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    Metrics: Sequence[str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AuthorizedActions: Optional[Sequence[FineGrainedActionType]] = None


class ListAvailableResourceMetricsRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    MetricTypes: Sequence[str]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResponseResourceMetricTypeDef(BaseValidatorModel):
    Metric: Optional[str] = None
    Description: Optional[str] = None
    Unit: Optional[str] = None


class ListPerformanceAnalysisReportsRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ListTags: Optional[bool] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    ResourceARN: str


class ResponseResourceMetricKeyTypeDef(BaseValidatorModel):
    Metric: str
    Dimensions: Optional[Dict[str, str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    ResourceARN: str
    TagKeys: Sequence[str]


class AnalysisReportSummaryTypeDef(BaseValidatorModel):
    AnalysisReportId: Optional[str] = None
    CreateTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[AnalysisStatusType] = None
    Tags: Optional[List[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreatePerformanceAnalysisReportRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreatePerformanceAnalysisReportResponseTypeDef(BaseValidatorModel):
    AnalysisReportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DataTypeDef(BaseValidatorModel):
    PerformanceInsightsMetric: Optional[PerformanceInsightsMetricTypeDef] = None


class DescribeDimensionKeysRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Metric: str
    GroupBy: DimensionGroupTypeDef
    PeriodInSeconds: Optional[int] = None
    AdditionalMetrics: Optional[Sequence[str]] = None
    PartitionBy: Optional[DimensionGroupTypeDef] = None
    Filter: Optional[Mapping[str, str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MetricQueryTypeDef(BaseValidatorModel):
    Metric: str
    GroupBy: Optional[DimensionGroupTypeDef] = None
    Filter: Optional[Mapping[str, str]] = None


class DescribeDimensionKeysResponseTypeDef(BaseValidatorModel):
    AlignedStartTime: datetime
    AlignedEndTime: datetime
    PartitionKeys: List[ResponsePartitionKeyTypeDef]
    Keys: List[DimensionKeyDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DimensionGroupDetailTypeDef(BaseValidatorModel):
    Group: Optional[str] = None
    Dimensions: Optional[List[DimensionDetailTypeDef]] = None


class GetDimensionKeyDetailsResponseTypeDef(BaseValidatorModel):
    Dimensions: List[DimensionKeyDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceMetadataResponseTypeDef(BaseValidatorModel):
    Identifier: str
    Features: Dict[str, FeatureMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAvailableResourceMetricsResponseTypeDef(BaseValidatorModel):
    Metrics: List[ResponseResourceMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MetricKeyDataPointsTypeDef(BaseValidatorModel):
    Key: Optional[ResponseResourceMetricKeyTypeDef] = None
    DataPoints: Optional[List[DataPointTypeDef]] = None


class ListPerformanceAnalysisReportsResponseTypeDef(BaseValidatorModel):
    AnalysisReports: List[AnalysisReportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class InsightTypeDef(BaseValidatorModel):
    InsightId: str
    InsightType: Optional[str] = None
    Context: Optional[ContextTypeType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Severity: Optional[SeverityType] = None
    SupportingInsights: Optional[List[Dict[str, Any]]] = None
    Description: Optional[str] = None
    Recommendations: Optional[List[RecommendationTypeDef]] = None
    InsightData: Optional[List[DataTypeDef]] = None
    BaselineData: Optional[List[DataTypeDef]] = None


class GetResourceMetricsRequestTypeDef(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    MetricQueries: Sequence[MetricQueryTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    PeriodInSeconds: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PeriodAlignment: Optional[PeriodAlignmentType] = None


class MetricDimensionGroupsTypeDef(BaseValidatorModel):
    Metric: Optional[str] = None
    Groups: Optional[List[DimensionGroupDetailTypeDef]] = None


class GetResourceMetricsResponseTypeDef(BaseValidatorModel):
    AlignedStartTime: datetime
    AlignedEndTime: datetime
    Identifier: str
    MetricList: List[MetricKeyDataPointsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AnalysisReportTypeDef(BaseValidatorModel):
    AnalysisReportId: str
    Identifier: Optional[str] = None
    ServiceType: Optional[ServiceTypeType] = None
    CreateTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[AnalysisStatusType] = None
    Insights: Optional[List[InsightTypeDef]] = None


class ListAvailableResourceDimensionsResponseTypeDef(BaseValidatorModel):
    MetricDimensions: List[MetricDimensionGroupsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetPerformanceAnalysisReportResponseTypeDef(BaseValidatorModel):
    AnalysisReport: AnalysisReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


