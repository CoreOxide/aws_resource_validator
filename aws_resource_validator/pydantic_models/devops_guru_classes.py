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
from aws_resource_validator.pydantic_models.devops_guru_constants import *

class AccountInsightHealthTypeDef(BaseValidatorModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AmazonCodeGuruProfilerIntegrationTypeDef(BaseValidatorModel):
    Status: Optional[EventSourceOptInStatusType] = None


class AnomalyReportedTimeRangeTypeDef(BaseValidatorModel):
    OpenTime: datetime
    CloseTime: Optional[datetime] = None


class AnomalySourceMetadataTypeDef(BaseValidatorModel):
    Source: Optional[str] = None
    SourceResourceName: Optional[str] = None
    SourceResourceType: Optional[str] = None


class AnomalyTimeRangeTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None


class CloudFormationCollectionFilterTypeDef(BaseValidatorModel):
    StackNames: Optional[List[str]] = None


class CloudFormationCollectionOutputTypeDef(BaseValidatorModel):
    StackNames: Optional[List[str]] = None


class CloudFormationCollectionTypeDef(BaseValidatorModel):
    StackNames: Optional[Sequence[str]] = None


class CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef(BaseValidatorModel):
    StackNames: Optional[List[str]] = None


class CloudFormationCostEstimationResourceCollectionFilterTypeDef(BaseValidatorModel):
    StackNames: Optional[Sequence[str]] = None


class InsightHealthTypeDef(BaseValidatorModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None
    MeanTimeToRecoverInMilliseconds: Optional[int] = None


class TimestampMetricValuePairTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    MetricValue: Optional[float] = None


class CloudWatchMetricsDimensionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class TagCostEstimationResourceCollectionFilterOutputTypeDef(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]


class TagCostEstimationResourceCollectionFilterTypeDef(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: Sequence[str]


class CostEstimationTimeRangeTypeDef(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class DeleteInsightRequestTypeDef(BaseValidatorModel):
    Id: str


class DescribeAnomalyRequestTypeDef(BaseValidatorModel):
    Id: str
    AccountId: Optional[str] = None


class DescribeFeedbackRequestTypeDef(BaseValidatorModel):
    InsightId: Optional[str] = None


class InsightFeedbackTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Feedback: Optional[InsightFeedbackOptionType] = None


class DescribeInsightRequestTypeDef(BaseValidatorModel):
    Id: str
    AccountId: Optional[str] = None


class DescribeOrganizationHealthRequestTypeDef(BaseValidatorModel):
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeOrganizationResourceCollectionHealthRequestTypeDef(BaseValidatorModel):
    OrganizationResourceCollectionType: OrganizationResourceCollectionTypeType
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeResourceCollectionHealthRequestTypeDef(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    NextToken: Optional[str] = None


class GetCostEstimationRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class GetResourceCollectionRequestTypeDef(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    NextToken: Optional[str] = None


class InsightTimeRangeTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None


class ListAnomalousLogGroupsRequestTypeDef(BaseValidatorModel):
    InsightId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMonitoredResourcesFiltersTypeDef(BaseValidatorModel):
    ResourcePermission: ResourcePermissionType
    ResourceTypeFilters: Sequence[ResourceTypeFilterType]


class ListNotificationChannelsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListRecommendationsRequestTypeDef(BaseValidatorModel):
    InsightId: str
    NextToken: Optional[str] = None
    Locale: Optional[LocaleType] = None
    AccountId: Optional[str] = None


class LogAnomalyClassTypeDef(BaseValidatorModel):
    LogStreamName: Optional[str] = None
    LogAnomalyType: Optional[LogAnomalyTypeType] = None
    LogAnomalyToken: Optional[str] = None
    LogEventId: Optional[str] = None
    Explanation: Optional[str] = None
    NumberOfLogLinesOccurrences: Optional[int] = None
    LogEventTimestamp: Optional[datetime] = None


class LogsAnomalyDetectionIntegrationConfigTypeDef(BaseValidatorModel):
    OptInStatus: Optional[OptInStatusType] = None


class LogsAnomalyDetectionIntegrationTypeDef(BaseValidatorModel):
    OptInStatus: Optional[OptInStatusType] = None


class NotificationFilterConfigOutputTypeDef(BaseValidatorModel):
    Severities: Optional[List[InsightSeverityType]] = None
    MessageTypes: Optional[List[NotificationMessageTypeType]] = None


class SnsChannelConfigTypeDef(BaseValidatorModel):
    TopicArn: Optional[str] = None


class NotificationFilterConfigTypeDef(BaseValidatorModel):
    Severities: Optional[Sequence[InsightSeverityType]] = None
    MessageTypes: Optional[Sequence[NotificationMessageTypeType]] = None


class OpsCenterIntegrationConfigTypeDef(BaseValidatorModel):
    OptInStatus: Optional[OptInStatusType] = None


class OpsCenterIntegrationTypeDef(BaseValidatorModel):
    OptInStatus: Optional[OptInStatusType] = None


class PerformanceInsightsMetricDimensionGroupTypeDef(BaseValidatorModel):
    Group: Optional[str] = None
    Dimensions: Optional[List[str]] = None
    Limit: Optional[int] = None


class PerformanceInsightsReferenceScalarTypeDef(BaseValidatorModel):
    Value: Optional[float] = None


class PredictionTimeRangeTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None


class ServiceCollectionOutputTypeDef(BaseValidatorModel):
    ServiceNames: Optional[List[ServiceNameType]] = None


class RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None


class RemoveNotificationChannelRequestTypeDef(BaseValidatorModel):
    Id: str


class TagCollectionFilterTypeDef(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]


class TagCollectionOutputTypeDef(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]


class ServiceCollectionTypeDef(BaseValidatorModel):
    ServiceNames: Optional[Sequence[ServiceNameType]] = None


class ServiceInsightHealthTypeDef(BaseValidatorModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None


class TagCollectionTypeDef(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: Sequence[str]


class UpdateCloudFormationCollectionFilterTypeDef(BaseValidatorModel):
    StackNames: Optional[Sequence[str]] = None


class UpdateTagCollectionFilterTypeDef(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: Sequence[str]


class AccountHealthTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Insight: Optional[AccountInsightHealthTypeDef] = None


class AddNotificationChannelResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountHealthResponseTypeDef(BaseValidatorModel):
    OpenReactiveInsights: int
    OpenProactiveInsights: int
    MetricsAnalyzed: int
    ResourceHours: int
    AnalyzedResourceCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountOverviewResponseTypeDef(BaseValidatorModel):
    ReactiveInsights: int
    ProactiveInsights: int
    MeanTimeToRecoverInMilliseconds: int
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeOrganizationHealthResponseTypeDef(BaseValidatorModel):
    OpenReactiveInsights: int
    OpenProactiveInsights: int
    MetricsAnalyzed: int
    ResourceHours: int
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeOrganizationOverviewResponseTypeDef(BaseValidatorModel):
    ReactiveInsights: int
    ProactiveInsights: int
    ResponseMetadata: ResponseMetadataTypeDef


class EventSourcesConfigTypeDef(BaseValidatorModel):
    AmazonCodeGuruProfiler: Optional[AmazonCodeGuruProfilerIntegrationTypeDef] = None


class CloudFormationHealthTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    Insight: Optional[InsightHealthTypeDef] = None
    AnalyzedResourceCount: Optional[int] = None


class TagHealthTypeDef(BaseValidatorModel):
    AppBoundaryKey: Optional[str] = None
    TagValue: Optional[str] = None
    Insight: Optional[InsightHealthTypeDef] = None
    AnalyzedResourceCount: Optional[int] = None


class CloudWatchMetricsDataSummaryTypeDef(BaseValidatorModel):
    TimestampMetricValuePairList: Optional[List[TimestampMetricValuePairTypeDef]] = None
    StatusCode: Optional[CloudWatchMetricDataStatusCodeType] = None


class CostEstimationResourceCollectionFilterOutputTypeDef(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef] = None
    Tags: Optional[List[TagCostEstimationResourceCollectionFilterOutputTypeDef]] = None


class CostEstimationResourceCollectionFilterTypeDef(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCostEstimationResourceCollectionFilterTypeDef] = None
    Tags: Optional[Sequence[TagCostEstimationResourceCollectionFilterTypeDef]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DescribeAccountOverviewRequestTypeDef(BaseValidatorModel):
    FromTime: TimestampTypeDef
    ToTime: Optional[TimestampTypeDef] = None


class DescribeOrganizationOverviewRequestTypeDef(BaseValidatorModel):
    FromTime: TimestampTypeDef
    ToTime: Optional[TimestampTypeDef] = None
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None


class EndTimeRangeTypeDef(BaseValidatorModel):
    FromTime: Optional[TimestampTypeDef] = None
    ToTime: Optional[TimestampTypeDef] = None


class EventTimeRangeTypeDef(BaseValidatorModel):
    FromTime: TimestampTypeDef
    ToTime: TimestampTypeDef


class StartTimeRangeTypeDef(BaseValidatorModel):
    FromTime: Optional[TimestampTypeDef] = None
    ToTime: Optional[TimestampTypeDef] = None


class DescribeFeedbackResponseTypeDef(BaseValidatorModel):
    InsightFeedback: InsightFeedbackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutFeedbackRequestTypeDef(BaseValidatorModel):
    InsightFeedback: Optional[InsightFeedbackTypeDef] = None


class DescribeOrganizationResourceCollectionHealthRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationResourceCollectionType: OrganizationResourceCollectionTypeType
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeResourceCollectionHealthRequestPaginateTypeDef(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetCostEstimationRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourceCollectionRequestPaginateTypeDef(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAnomalousLogGroupsRequestPaginateTypeDef(BaseValidatorModel):
    InsightId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNotificationChannelsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecommendationsRequestPaginateTypeDef(BaseValidatorModel):
    InsightId: str
    Locale: Optional[LocaleType] = None
    AccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMonitoredResourcesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[ListMonitoredResourcesFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMonitoredResourcesRequestTypeDef(BaseValidatorModel):
    Filters: Optional[ListMonitoredResourcesFiltersTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LogAnomalyShowcaseTypeDef(BaseValidatorModel):
    LogAnomalyClasses: Optional[List[LogAnomalyClassTypeDef]] = None


class NotificationChannelConfigOutputTypeDef(BaseValidatorModel):
    Sns: SnsChannelConfigTypeDef
    Filters: Optional[NotificationFilterConfigOutputTypeDef] = None


class NotificationChannelConfigTypeDef(BaseValidatorModel):
    Sns: SnsChannelConfigTypeDef
    Filters: Optional[NotificationFilterConfigTypeDef] = None


class KMSServerSideEncryptionIntegrationConfigTypeDef(BaseValidatorModel):
    pass


class UpdateServiceIntegrationConfigTypeDef(BaseValidatorModel):
    OpsCenter: Optional[OpsCenterIntegrationConfigTypeDef] = None
    LogsAnomalyDetection: Optional[LogsAnomalyDetectionIntegrationConfigTypeDef] = None
    KMSServerSideEncryption: Optional[KMSServerSideEncryptionIntegrationConfigTypeDef] = None


class KMSServerSideEncryptionIntegrationTypeDef(BaseValidatorModel):
    pass


class ServiceIntegrationConfigTypeDef(BaseValidatorModel):
    OpsCenter: Optional[OpsCenterIntegrationTypeDef] = None
    LogsAnomalyDetection: Optional[LogsAnomalyDetectionIntegrationTypeDef] = None
    KMSServerSideEncryption: Optional[KMSServerSideEncryptionIntegrationTypeDef] = None


class PerformanceInsightsMetricQueryTypeDef(BaseValidatorModel):
    Metric: Optional[str] = None
    GroupBy: Optional[PerformanceInsightsMetricDimensionGroupTypeDef] = None
    Filter: Optional[Dict[str, str]] = None


class RecommendationRelatedAnomalySourceDetailTypeDef(BaseValidatorModel):
    CloudWatchMetrics: Optional[List[RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef]] = None


class RecommendationRelatedEventResourceTypeDef(BaseValidatorModel):
    pass


class RecommendationRelatedEventTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Resources: Optional[List[RecommendationRelatedEventResourceTypeDef]] = None


class ResourceCollectionFilterTypeDef(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCollectionFilterTypeDef] = None
    Tags: Optional[List[TagCollectionFilterTypeDef]] = None


class ResourceCollectionOutputTypeDef(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCollectionOutputTypeDef] = None
    Tags: Optional[List[TagCollectionOutputTypeDef]] = None


class UpdateResourceCollectionFilterTypeDef(BaseValidatorModel):
    CloudFormation: Optional[UpdateCloudFormationCollectionFilterTypeDef] = None
    Tags: Optional[Sequence[UpdateTagCollectionFilterTypeDef]] = None


class DescribeEventSourcesConfigResponseTypeDef(BaseValidatorModel):
    EventSources: EventSourcesConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEventSourcesConfigRequestTypeDef(BaseValidatorModel):
    EventSources: Optional[EventSourcesConfigTypeDef] = None


class CloudWatchMetricsDetailTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[CloudWatchMetricsDimensionTypeDef]] = None
    Stat: Optional[CloudWatchMetricsStatType] = None
    Unit: Optional[str] = None
    Period: Optional[int] = None
    MetricDataSummary: Optional[CloudWatchMetricsDataSummaryTypeDef] = None


class ServiceResourceCostTypeDef(BaseValidatorModel):
    pass


class GetCostEstimationResponseTypeDef(BaseValidatorModel):
    ResourceCollection: CostEstimationResourceCollectionFilterOutputTypeDef
    Status: CostEstimationStatusType
    Costs: List[ServiceResourceCostTypeDef]
    TimeRange: CostEstimationTimeRangeTypeDef
    TotalCost: float
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AnomalousLogGroupTypeDef(BaseValidatorModel):
    LogGroupName: Optional[str] = None
    ImpactStartTime: Optional[datetime] = None
    ImpactEndTime: Optional[datetime] = None
    NumberOfLogLinesScanned: Optional[int] = None
    LogAnomalyShowcases: Optional[List[LogAnomalyShowcaseTypeDef]] = None


class NotificationChannelTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Config: Optional[NotificationChannelConfigOutputTypeDef] = None


class UpdateServiceIntegrationRequestTypeDef(BaseValidatorModel):
    ServiceIntegration: UpdateServiceIntegrationConfigTypeDef


class DescribeServiceIntegrationResponseTypeDef(BaseValidatorModel):
    ServiceIntegration: ServiceIntegrationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PerformanceInsightsReferenceMetricTypeDef(BaseValidatorModel):
    MetricQuery: Optional[PerformanceInsightsMetricQueryTypeDef] = None


class RecommendationRelatedAnomalyResourceTypeDef(BaseValidatorModel):
    pass


class RecommendationRelatedAnomalyTypeDef(BaseValidatorModel):
    Resources: Optional[List[RecommendationRelatedAnomalyResourceTypeDef]] = None
    SourceDetails: Optional[List[RecommendationRelatedAnomalySourceDetailTypeDef]] = None
    AnomalyId: Optional[str] = None


class GetResourceCollectionResponseTypeDef(BaseValidatorModel):
    ResourceCollection: ResourceCollectionFilterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EventResourceTypeDef(BaseValidatorModel):
    pass


class EventTypeDef(BaseValidatorModel):
    ResourceCollection: Optional[ResourceCollectionOutputTypeDef] = None
    Id: Optional[str] = None
    Time: Optional[datetime] = None
    EventSource: Optional[str] = None
    Name: Optional[str] = None
    DataSource: Optional[EventDataSourceType] = None
    EventClass: Optional[EventClassType] = None
    Resources: Optional[List[EventResourceTypeDef]] = None


class ProactiveInsightSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionOutputTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionOutputTypeDef] = None
    AssociatedResourceArns: Optional[List[str]] = None


class ProactiveInsightTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionOutputTypeDef] = None
    SsmOpsItemId: Optional[str] = None
    Description: Optional[str] = None


class ProactiveOrganizationInsightSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionOutputTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionOutputTypeDef] = None


class ReactiveInsightSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionOutputTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionOutputTypeDef] = None
    AssociatedResourceArns: Optional[List[str]] = None


class ReactiveInsightTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionOutputTypeDef] = None
    SsmOpsItemId: Optional[str] = None
    Description: Optional[str] = None


class ReactiveOrganizationInsightSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionOutputTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionOutputTypeDef] = None


class ServiceCollectionUnionTypeDef(BaseValidatorModel):
    pass


class ListAnomaliesForInsightFiltersTypeDef(BaseValidatorModel):
    ServiceCollection: Optional[ServiceCollectionUnionTypeDef] = None


class ServiceHealthTypeDef(BaseValidatorModel):
    pass


class DescribeOrganizationResourceCollectionHealthResponseTypeDef(BaseValidatorModel):
    CloudFormation: List[CloudFormationHealthTypeDef]
    Service: List[ServiceHealthTypeDef]
    Account: List[AccountHealthTypeDef]
    Tags: List[TagHealthTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeResourceCollectionHealthResponseTypeDef(BaseValidatorModel):
    CloudFormation: List[CloudFormationHealthTypeDef]
    Service: List[ServiceHealthTypeDef]
    Tags: List[TagHealthTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CloudFormationCollectionUnionTypeDef(BaseValidatorModel):
    pass


class TagCollectionUnionTypeDef(BaseValidatorModel):
    pass


class ResourceCollectionTypeDef(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCollectionUnionTypeDef] = None
    Tags: Optional[Sequence[TagCollectionUnionTypeDef]] = None


class UpdateResourceCollectionRequestTypeDef(BaseValidatorModel):
    Action: UpdateResourceCollectionActionType
    ResourceCollection: UpdateResourceCollectionFilterTypeDef


class CostEstimationResourceCollectionFilterUnionTypeDef(BaseValidatorModel):
    pass


class StartCostEstimationRequestTypeDef(BaseValidatorModel):
    ResourceCollection: CostEstimationResourceCollectionFilterUnionTypeDef
    ClientToken: Optional[str] = None


class ListAnomalousLogGroupsResponseTypeDef(BaseValidatorModel):
    InsightId: str
    AnomalousLogGroups: List[AnomalousLogGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListNotificationChannelsResponseTypeDef(BaseValidatorModel):
    Channels: List[NotificationChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class NotificationChannelConfigUnionTypeDef(BaseValidatorModel):
    pass


class AddNotificationChannelRequestTypeDef(BaseValidatorModel):
    Config: NotificationChannelConfigUnionTypeDef


class PerformanceInsightsReferenceComparisonValuesTypeDef(BaseValidatorModel):
    ReferenceScalar: Optional[PerformanceInsightsReferenceScalarTypeDef] = None
    ReferenceMetric: Optional[PerformanceInsightsReferenceMetricTypeDef] = None


class RecommendationTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Link: Optional[str] = None
    Name: Optional[str] = None
    Reason: Optional[str] = None
    RelatedEvents: Optional[List[RecommendationRelatedEventTypeDef]] = None
    RelatedAnomalies: Optional[List[RecommendationRelatedAnomalyTypeDef]] = None
    Category: Optional[str] = None


class ListEventsResponseTypeDef(BaseValidatorModel):
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MonitoredResourceIdentifierTypeDef(BaseValidatorModel):
    pass


class ListMonitoredResourcesResponseTypeDef(BaseValidatorModel):
    MonitoredResourceIdentifiers: List[MonitoredResourceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListInsightsResponseTypeDef(BaseValidatorModel):
    ProactiveInsights: List[ProactiveInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveInsightSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchInsightsResponseTypeDef(BaseValidatorModel):
    ProactiveInsights: List[ProactiveInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveInsightSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchOrganizationInsightsResponseTypeDef(BaseValidatorModel):
    ProactiveInsights: List[ProactiveInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveInsightSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeInsightResponseTypeDef(BaseValidatorModel):
    ProactiveInsight: ProactiveInsightTypeDef
    ReactiveInsight: ReactiveInsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListOrganizationInsightsResponseTypeDef(BaseValidatorModel):
    ProactiveInsights: List[ProactiveOrganizationInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveOrganizationInsightSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAnomaliesForInsightRequestPaginateTypeDef(BaseValidatorModel):
    InsightId: str
    StartTimeRange: Optional[StartTimeRangeTypeDef] = None
    AccountId: Optional[str] = None
    Filters: Optional[ListAnomaliesForInsightFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAnomaliesForInsightRequestTypeDef(BaseValidatorModel):
    InsightId: str
    StartTimeRange: Optional[StartTimeRangeTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None
    Filters: Optional[ListAnomaliesForInsightFiltersTypeDef] = None


class ListInsightsStatusFilterTypeDef(BaseValidatorModel):
    pass


class ListInsightsRequestPaginateTypeDef(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInsightsRequestTypeDef(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOrganizationInsightsRequestPaginateTypeDef(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOrganizationInsightsRequestTypeDef(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    MaxResults: Optional[int] = None
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None


class PerformanceInsightsReferenceDataTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ComparisonValues: Optional[PerformanceInsightsReferenceComparisonValuesTypeDef] = None


class ListRecommendationsResponseTypeDef(BaseValidatorModel):
    Recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResourceCollectionUnionTypeDef(BaseValidatorModel):
    pass


class ListEventsFiltersTypeDef(BaseValidatorModel):
    InsightId: Optional[str] = None
    EventTimeRange: Optional[EventTimeRangeTypeDef] = None
    EventClass: Optional[EventClassType] = None
    EventSource: Optional[str] = None
    DataSource: Optional[EventDataSourceType] = None
    ResourceCollection: Optional[ResourceCollectionUnionTypeDef] = None


class SearchInsightsFiltersTypeDef(BaseValidatorModel):
    Severities: Optional[Sequence[InsightSeverityType]] = None
    Statuses: Optional[Sequence[InsightStatusType]] = None
    ResourceCollection: Optional[ResourceCollectionUnionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionUnionTypeDef] = None


class SearchOrganizationInsightsFiltersTypeDef(BaseValidatorModel):
    Severities: Optional[Sequence[InsightSeverityType]] = None
    Statuses: Optional[Sequence[InsightStatusType]] = None
    ResourceCollection: Optional[ResourceCollectionUnionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionUnionTypeDef] = None


class PerformanceInsightsStatTypeDef(BaseValidatorModel):
    pass


class PerformanceInsightsMetricsDetailTypeDef(BaseValidatorModel):
    MetricDisplayName: Optional[str] = None
    Unit: Optional[str] = None
    MetricQuery: Optional[PerformanceInsightsMetricQueryTypeDef] = None
    ReferenceData: Optional[List[PerformanceInsightsReferenceDataTypeDef]] = None
    StatsAtAnomaly: Optional[List[PerformanceInsightsStatTypeDef]] = None
    StatsAtBaseline: Optional[List[PerformanceInsightsStatTypeDef]] = None


class ListEventsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: ListEventsFiltersTypeDef
    AccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventsRequestTypeDef(BaseValidatorModel):
    Filters: ListEventsFiltersTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class AnomalySourceDetailsTypeDef(BaseValidatorModel):
    CloudWatchMetrics: Optional[List[CloudWatchMetricsDetailTypeDef]] = None
    PerformanceInsightsMetrics: Optional[List[PerformanceInsightsMetricsDetailTypeDef]] = None


class AnomalyResourceTypeDef(BaseValidatorModel):
    pass


class ProactiveAnomalySummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Severity: Optional[AnomalySeverityType] = None
    Status: Optional[AnomalyStatusType] = None
    UpdateTime: Optional[datetime] = None
    AnomalyTimeRange: Optional[AnomalyTimeRangeTypeDef] = None
    AnomalyReportedTimeRange: Optional[AnomalyReportedTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    SourceDetails: Optional[AnomalySourceDetailsTypeDef] = None
    AssociatedInsightId: Optional[str] = None
    ResourceCollection: Optional[ResourceCollectionOutputTypeDef] = None
    Limit: Optional[float] = None
    SourceMetadata: Optional[AnomalySourceMetadataTypeDef] = None
    AnomalyResources: Optional[List[AnomalyResourceTypeDef]] = None
    Description: Optional[str] = None


class ProactiveAnomalyTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Severity: Optional[AnomalySeverityType] = None
    Status: Optional[AnomalyStatusType] = None
    UpdateTime: Optional[datetime] = None
    AnomalyTimeRange: Optional[AnomalyTimeRangeTypeDef] = None
    AnomalyReportedTimeRange: Optional[AnomalyReportedTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    SourceDetails: Optional[AnomalySourceDetailsTypeDef] = None
    AssociatedInsightId: Optional[str] = None
    ResourceCollection: Optional[ResourceCollectionOutputTypeDef] = None
    Limit: Optional[float] = None
    SourceMetadata: Optional[AnomalySourceMetadataTypeDef] = None
    AnomalyResources: Optional[List[AnomalyResourceTypeDef]] = None
    Description: Optional[str] = None


class ReactiveAnomalySummaryTypeDef(BaseValidatorModel):
    pass


class ListAnomaliesForInsightResponseTypeDef(BaseValidatorModel):
    ProactiveAnomalies: List[ProactiveAnomalySummaryTypeDef]
    ReactiveAnomalies: List[ReactiveAnomalySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ReactiveAnomalyTypeDef(BaseValidatorModel):
    pass


class DescribeAnomalyResponseTypeDef(BaseValidatorModel):
    ProactiveAnomaly: ProactiveAnomalyTypeDef
    ReactiveAnomaly: ReactiveAnomalyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


