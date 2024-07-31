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
from aws_resource_validator.pydantic_models.pi_constants import *

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class AnalysisReportTypeDef(BaseModel):
    AnalysisReportId: str
    Identifier: Optional[str] = None
    ServiceType: Optional[ServiceTypeType] = None
    CreateTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[AnalysisStatusType] = None
    Insights: Optional[List["InsightTypeDef"]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DataPointTypeDef(BaseModel):
    Timestamp: datetime
    Value: float

class PerformanceInsightsMetricTypeDef(BaseModel):
    Metric: Optional[str] = None
    DisplayName: Optional[str] = None
    Dimensions: Optional[Dict[str, str]] = None
    Value: Optional[float] = None

class DeletePerformanceAnalysisReportRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    Identifier: str
    AnalysisReportId: str

class DimensionGroupTypeDef(BaseModel):
    Group: str
    Dimensions: Optional[Sequence[str]] = None
    Limit: Optional[int] = None

class DimensionKeyDescriptionTypeDef(BaseModel):
    Dimensions: Optional[Dict[str, str]] = None
    Total: Optional[float] = None
    AdditionalMetrics: Optional[Dict[str, float]] = None
    Partitions: Optional[List[float]] = None

class ResponsePartitionKeyTypeDef(BaseModel):
    Dimensions: Dict[str, str]

class DimensionDetailTypeDef(BaseModel):
    Identifier: Optional[str] = None

class DimensionKeyDetailTypeDef(BaseModel):
    Value: Optional[str] = None
    Dimension: Optional[str] = None
    Status: Optional[DetailStatusType] = None

class FeatureMetadataTypeDef(BaseModel):
    Status: Optional[FeatureStatusType] = None

class GetDimensionKeyDetailsRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    Identifier: str
    Group: str
    GroupIdentifier: str
    RequestedDimensions: Optional[Sequence[str]] = None

class GetPerformanceAnalysisReportRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    Identifier: str
    AnalysisReportId: str
    TextFormat: Optional[TextFormatType] = None
    AcceptLanguage: Optional[Literal["EN_US"]] = None

class GetResourceMetadataRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    Identifier: str

class RecommendationTypeDef(BaseModel):
    RecommendationId: Optional[str] = None
    RecommendationDescription: Optional[str] = None

class ListAvailableResourceDimensionsRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    Identifier: str
    Metrics: Sequence[str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AuthorizedActions: Optional[Sequence[FineGrainedActionType]] = None

class ListAvailableResourceMetricsRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    Identifier: str
    MetricTypes: Sequence[str]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ResponseResourceMetricTypeDef(BaseModel):
    Metric: Optional[str] = None
    Description: Optional[str] = None
    Unit: Optional[str] = None

class ListPerformanceAnalysisReportsRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    Identifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ListTags: Optional[bool] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    ResourceARN: str

class ResponseResourceMetricKeyTypeDef(BaseModel):
    Metric: str
    Dimensions: Optional[Dict[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    ResourceARN: str
    TagKeys: Sequence[str]

class AnalysisReportSummaryTypeDef(BaseModel):
    AnalysisReportId: Optional[str] = None
    CreateTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[AnalysisStatusType] = None
    Tags: Optional[List[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreatePerformanceAnalysisReportRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    Identifier: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreatePerformanceAnalysisReportResponseTypeDef(BaseModel):
    AnalysisReportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPerformanceAnalysisReportResponseTypeDef(BaseModel):
    AnalysisReport: AnalysisReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DataTypeDef(BaseModel):
    PerformanceInsightsMetric: Optional[PerformanceInsightsMetricTypeDef] = None

class DescribeDimensionKeysRequestRequestTypeDef(BaseModel):
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

class MetricQueryTypeDef(BaseModel):
    Metric: str
    GroupBy: Optional[DimensionGroupTypeDef] = None
    Filter: Optional[Mapping[str, str]] = None

class DescribeDimensionKeysResponseTypeDef(BaseModel):
    AlignedStartTime: datetime
    AlignedEndTime: datetime
    PartitionKeys: List[ResponsePartitionKeyTypeDef]
    Keys: List[DimensionKeyDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DimensionGroupDetailTypeDef(BaseModel):
    Group: Optional[str] = None
    Dimensions: Optional[List[DimensionDetailTypeDef]] = None

class GetDimensionKeyDetailsResponseTypeDef(BaseModel):
    Dimensions: List[DimensionKeyDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceMetadataResponseTypeDef(BaseModel):
    Identifier: str
    Features: Dict[str, FeatureMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableResourceMetricsResponseTypeDef(BaseModel):
    Metrics: List[ResponseResourceMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MetricKeyDataPointsTypeDef(BaseModel):
    Key: Optional[ResponseResourceMetricKeyTypeDef] = None
    DataPoints: Optional[List[DataPointTypeDef]] = None

class ListPerformanceAnalysisReportsResponseTypeDef(BaseModel):
    AnalysisReports: List[AnalysisReportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InsightTypeDef(BaseModel):
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

class GetResourceMetricsRequestRequestTypeDef(BaseModel):
    ServiceType: ServiceTypeType
    Identifier: str
    MetricQueries: Sequence[MetricQueryTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    PeriodInSeconds: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PeriodAlignment: Optional[PeriodAlignmentType] = None

class MetricDimensionGroupsTypeDef(BaseModel):
    Metric: Optional[str] = None
    Groups: Optional[List[DimensionGroupDetailTypeDef]] = None

class GetResourceMetricsResponseTypeDef(BaseModel):
    AlignedStartTime: datetime
    AlignedEndTime: datetime
    Identifier: str
    MetricList: List[MetricKeyDataPointsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAvailableResourceDimensionsResponseTypeDef(BaseModel):
    MetricDimensions: List[MetricDimensionGroupsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

