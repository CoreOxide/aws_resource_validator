from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.pi.pi_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: str
    Value: str

Timestamp = Union[datetime, str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DataPoint(BaseValidatorModel):
    Timestamp: datetime
    Value: float


class PerformanceInsightsMetric(BaseValidatorModel):
    Metric: Optional[str] = None
    DisplayName: Optional[str] = None
    Dimensions: Optional[Dict[str, str]] = None
    Filter: Optional[Dict[str, str]] = None
    Value: Optional[float] = None


class DeletePerformanceAnalysisReportRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    AnalysisReportId: str


class DimensionGroup(BaseValidatorModel):
    Group: str
    Dimensions: Optional[List[str]] = None
    Limit: Optional[int] = None


class DimensionKeyDescription(BaseValidatorModel):
    Dimensions: Optional[Dict[str, str]] = None
    Total: Optional[float] = None
    AdditionalMetrics: Optional[Dict[str, float]] = None
    Partitions: Optional[List[float]] = None


class ResponsePartitionKey(BaseValidatorModel):
    Dimensions: Dict[str, str]


class DimensionDetail(BaseValidatorModel):
    Identifier: Optional[str] = None


class DimensionKeyDetail(BaseValidatorModel):
    Value: Optional[str] = None
    Dimension: Optional[str] = None
    Status: Optional[DetailStatusType] = None


class FeatureMetadata(BaseValidatorModel):
    Status: Optional[FeatureStatusType] = None


class GetDimensionKeyDetailsRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    Group: str
    GroupIdentifier: str
    RequestedDimensions: Optional[List[str]] = None


class GetPerformanceAnalysisReportRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    AnalysisReportId: str
    TextFormat: Optional[TextFormatType] = None
    AcceptLanguage: Optional[Literal['EN_US']] = None


class GetResourceMetadataRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str


class Recommendation(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    RecommendationDescription: Optional[str] = None


class ListAvailableResourceDimensionsRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    Metrics: List[str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AuthorizedActions: Optional[List[FineGrainedActionType]] = None


class ListAvailableResourceMetricsRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    MetricTypes: List[str]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResponseResourceMetric(BaseValidatorModel):
    Metric: Optional[str] = None
    Description: Optional[str] = None
    Unit: Optional[str] = None


class ListPerformanceAnalysisReportsRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ListTags: Optional[bool] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    ResourceARN: str


class ResponseResourceMetricKey(BaseValidatorModel):
    Metric: str
    Dimensions: Optional[Dict[str, str]] = None


class UntagResourceRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    ResourceARN: str
    TagKeys: List[str]


class AnalysisReportSummary(BaseValidatorModel):
    AnalysisReportId: Optional[str] = None
    CreateTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[AnalysisStatusType] = None
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    ResourceARN: str
    Tags: List[Tag]


class CreatePerformanceAnalysisReportRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    StartTime: Timestamp
    EndTime: Timestamp
    Tags: Optional[List[Tag]] = None


class CreatePerformanceAnalysisReportResponse(BaseValidatorModel):
    AnalysisReportId: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class Data(BaseValidatorModel):
    PerformanceInsightsMetric: Optional[PerformanceInsightsMetric] = None


class DescribeDimensionKeysRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    StartTime: Timestamp
    EndTime: Timestamp
    Metric: str
    GroupBy: DimensionGroup
    PeriodInSeconds: Optional[int] = None
    AdditionalMetrics: Optional[List[str]] = None
    PartitionBy: Optional[DimensionGroup] = None
    Filter: Optional[Dict[str, str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MetricQuery(BaseValidatorModel):
    Metric: str
    GroupBy: Optional[DimensionGroup] = None
    Filter: Optional[Dict[str, str]] = None


class DescribeDimensionKeysResponse(BaseValidatorModel):
    AlignedStartTime: datetime
    AlignedEndTime: datetime
    PartitionKeys: List[ResponsePartitionKey]
    Keys: List[DimensionKeyDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DimensionGroupDetail(BaseValidatorModel):
    Group: Optional[str] = None
    Dimensions: Optional[List[DimensionDetail]] = None


class GetDimensionKeyDetailsResponse(BaseValidatorModel):
    Dimensions: List[DimensionKeyDetail]
    ResponseMetadata: ResponseMetadata


class GetResourceMetadataResponse(BaseValidatorModel):
    Identifier: str
    Features: Dict[str, FeatureMetadata]
    ResponseMetadata: ResponseMetadata


class ListAvailableResourceMetricsResponse(BaseValidatorModel):
    Metrics: List[ResponseResourceMetric]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MetricKeyDataPoints(BaseValidatorModel):
    Key: Optional[ResponseResourceMetricKey] = None
    DataPoints: Optional[List[DataPoint]] = None


class ListPerformanceAnalysisReportsResponse(BaseValidatorModel):
    AnalysisReports: List[AnalysisReportSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Insight(BaseValidatorModel):
    InsightId: str
    InsightType: Optional[str] = None
    Context: Optional[ContextTypeType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Severity: Optional[SeverityType] = None
    SupportingInsights: Optional[List[Dict[str, Any]]] = None
    Description: Optional[str] = None
    Recommendations: Optional[List[Recommendation]] = None
    InsightData: Optional[List[Data]] = None
    BaselineData: Optional[List[Data]] = None


class GetResourceMetricsRequest(BaseValidatorModel):
    ServiceType: ServiceTypeType
    Identifier: str
    MetricQueries: List[MetricQuery]
    StartTime: Timestamp
    EndTime: Timestamp
    PeriodInSeconds: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PeriodAlignment: Optional[PeriodAlignmentType] = None


class MetricDimensionGroups(BaseValidatorModel):
    Metric: Optional[str] = None
    Groups: Optional[List[DimensionGroupDetail]] = None


class GetResourceMetricsResponse(BaseValidatorModel):
    AlignedStartTime: datetime
    AlignedEndTime: datetime
    Identifier: str
    MetricList: List[MetricKeyDataPoints]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AnalysisReport(BaseValidatorModel):
    AnalysisReportId: str
    Identifier: Optional[str] = None
    ServiceType: Optional[ServiceTypeType] = None
    CreateTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[AnalysisStatusType] = None
    Insights: Optional[List[Insight]] = None


class ListAvailableResourceDimensionsResponse(BaseValidatorModel):
    MetricDimensions: List[MetricDimensionGroups]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetPerformanceAnalysisReportResponse(BaseValidatorModel):
    AnalysisReport: AnalysisReport
    ResponseMetadata: ResponseMetadata