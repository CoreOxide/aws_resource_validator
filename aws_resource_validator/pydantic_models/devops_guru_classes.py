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
from aws_resource_validator.pydantic_models.devops_guru_constants import *

class AccountInsightHealthTypeDef(BaseModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AmazonCodeGuruProfilerIntegrationTypeDef(BaseModel):
    Status: Optional[EventSourceOptInStatusType] = None

class AnomalyReportedTimeRangeTypeDef(BaseModel):
    OpenTime: datetime
    CloseTime: Optional[datetime] = None

class AnomalyResourceTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[str] = None

class AnomalySourceMetadataTypeDef(BaseModel):
    Source: Optional[str] = None
    SourceResourceName: Optional[str] = None
    SourceResourceType: Optional[str] = None

class AnomalyTimeRangeTypeDef(BaseModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None

class CloudFormationCollectionFilterTypeDef(BaseModel):
    StackNames: Optional[List[str]] = None

class CloudFormationCollectionTypeDef(BaseModel):
    StackNames: Optional[List[str]] = None

class CloudFormationCostEstimationResourceCollectionFilterTypeDef(BaseModel):
    StackNames: Optional[List[str]] = None

class InsightHealthTypeDef(BaseModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None
    MeanTimeToRecoverInMilliseconds: Optional[int] = None

class TimestampMetricValuePairTypeDef(BaseModel):
    Timestamp: Optional[datetime] = None
    MetricValue: Optional[float] = None

class CloudWatchMetricsDimensionTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class TagCostEstimationResourceCollectionFilterTypeDef(BaseModel):
    AppBoundaryKey: str
    TagValues: List[str]

class CostEstimationTimeRangeTypeDef(BaseModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class DeleteInsightRequestRequestTypeDef(BaseModel):
    Id: str

class DescribeAnomalyRequestRequestTypeDef(BaseModel):
    Id: str
    AccountId: Optional[str] = None

class DescribeFeedbackRequestRequestTypeDef(BaseModel):
    InsightId: Optional[str] = None

class InsightFeedbackTypeDef(BaseModel):
    Id: Optional[str] = None
    Feedback: Optional[InsightFeedbackOptionType] = None

class DescribeInsightRequestRequestTypeDef(BaseModel):
    Id: str
    AccountId: Optional[str] = None

class DescribeOrganizationHealthRequestRequestTypeDef(BaseModel):
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef(BaseModel):
    OrganizationResourceCollectionType: OrganizationResourceCollectionTypeType
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeResourceCollectionHealthRequestRequestTypeDef(BaseModel):
    ResourceCollectionType: ResourceCollectionTypeType
    NextToken: Optional[str] = None

class EventResourceTypeDef(BaseModel):
    Type: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None

class GetCostEstimationRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class ServiceResourceCostTypeDef(BaseModel):
    Type: Optional[str] = None
    State: Optional[CostEstimationServiceResourceStateType] = None
    Count: Optional[int] = None
    UnitCost: Optional[float] = None
    Cost: Optional[float] = None

class GetResourceCollectionRequestRequestTypeDef(BaseModel):
    ResourceCollectionType: ResourceCollectionTypeType
    NextToken: Optional[str] = None

class InsightTimeRangeTypeDef(BaseModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None

class KMSServerSideEncryptionIntegrationConfigTypeDef(BaseModel):
    KMSKeyId: Optional[str] = None
    OptInStatus: Optional[OptInStatusType] = None
    Type: Optional[ServerSideEncryptionTypeType] = None

class KMSServerSideEncryptionIntegrationTypeDef(BaseModel):
    KMSKeyId: Optional[str] = None
    OptInStatus: Optional[OptInStatusType] = None
    Type: Optional[ServerSideEncryptionTypeType] = None

class ServiceCollectionTypeDef(BaseModel):
    ServiceNames: Optional[Sequence[ServiceNameType]] = None

class ListAnomalousLogGroupsRequestRequestTypeDef(BaseModel):
    InsightId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInsightsOngoingStatusFilterTypeDef(BaseModel):
    Type: InsightTypeType

class ListMonitoredResourcesFiltersTypeDef(BaseModel):
    ResourcePermission: ResourcePermissionType
    ResourceTypeFilters: Sequence[ResourceTypeFilterType]

class ListNotificationChannelsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class ListRecommendationsRequestRequestTypeDef(BaseModel):
    InsightId: str
    NextToken: Optional[str] = None
    Locale: Optional[LocaleType] = None
    AccountId: Optional[str] = None

class LogAnomalyClassTypeDef(BaseModel):
    LogStreamName: Optional[str] = None
    LogAnomalyType: Optional[LogAnomalyTypeType] = None
    LogAnomalyToken: Optional[str] = None
    LogEventId: Optional[str] = None
    Explanation: Optional[str] = None
    NumberOfLogLinesOccurrences: Optional[int] = None
    LogEventTimestamp: Optional[datetime] = None

class LogsAnomalyDetectionIntegrationConfigTypeDef(BaseModel):
    OptInStatus: Optional[OptInStatusType] = None

class LogsAnomalyDetectionIntegrationTypeDef(BaseModel):
    OptInStatus: Optional[OptInStatusType] = None

class NotificationFilterConfigPaginatorTypeDef(BaseModel):
    Severities: Optional[List[InsightSeverityType]] = None
    MessageTypes: Optional[List[NotificationMessageTypeType]] = None

class SnsChannelConfigTypeDef(BaseModel):
    TopicArn: Optional[str] = None

class NotificationFilterConfigTypeDef(BaseModel):
    Severities: Optional[Sequence[InsightSeverityType]] = None
    MessageTypes: Optional[Sequence[NotificationMessageTypeType]] = None

class OpsCenterIntegrationConfigTypeDef(BaseModel):
    OptInStatus: Optional[OptInStatusType] = None

class OpsCenterIntegrationTypeDef(BaseModel):
    OptInStatus: Optional[OptInStatusType] = None

class PerformanceInsightsMetricDimensionGroupTypeDef(BaseModel):
    Group: Optional[str] = None
    Dimensions: Optional[List[str]] = None
    Limit: Optional[int] = None

class PerformanceInsightsStatTypeDef(BaseModel):
    Type: Optional[str] = None
    Value: Optional[float] = None

class PerformanceInsightsReferenceScalarTypeDef(BaseModel):
    Value: Optional[float] = None

class PredictionTimeRangeTypeDef(BaseModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None

class RecommendationRelatedAnomalyResourceTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[str] = None

class RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None

class RecommendationRelatedEventResourceTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[str] = None

class RemoveNotificationChannelRequestRequestTypeDef(BaseModel):
    Id: str

class TagCollectionFilterTypeDef(BaseModel):
    AppBoundaryKey: str
    TagValues: List[str]

class TagCollectionTypeDef(BaseModel):
    AppBoundaryKey: str
    TagValues: List[str]

class ServiceInsightHealthTypeDef(BaseModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None

class UpdateCloudFormationCollectionFilterTypeDef(BaseModel):
    StackNames: Optional[Sequence[str]] = None

class UpdateTagCollectionFilterTypeDef(BaseModel):
    AppBoundaryKey: str
    TagValues: Sequence[str]

class AccountHealthTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Insight: Optional[AccountInsightHealthTypeDef] = None

class AddNotificationChannelResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountHealthResponseTypeDef(BaseModel):
    OpenReactiveInsights: int
    OpenProactiveInsights: int
    MetricsAnalyzed: int
    ResourceHours: int
    AnalyzedResourceCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountOverviewResponseTypeDef(BaseModel):
    ReactiveInsights: int
    ProactiveInsights: int
    MeanTimeToRecoverInMilliseconds: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationHealthResponseTypeDef(BaseModel):
    OpenReactiveInsights: int
    OpenProactiveInsights: int
    MetricsAnalyzed: int
    ResourceHours: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationOverviewResponseTypeDef(BaseModel):
    ReactiveInsights: int
    ProactiveInsights: int
    ResponseMetadata: ResponseMetadataTypeDef

class EventSourcesConfigTypeDef(BaseModel):
    AmazonCodeGuruProfiler: Optional[AmazonCodeGuruProfilerIntegrationTypeDef] = None

class CloudFormationHealthTypeDef(BaseModel):
    StackName: Optional[str] = None
    Insight: Optional[InsightHealthTypeDef] = None
    AnalyzedResourceCount: Optional[int] = None

class TagHealthTypeDef(BaseModel):
    AppBoundaryKey: Optional[str] = None
    TagValue: Optional[str] = None
    Insight: Optional[InsightHealthTypeDef] = None
    AnalyzedResourceCount: Optional[int] = None

class CloudWatchMetricsDataSummaryTypeDef(BaseModel):
    TimestampMetricValuePairList: Optional[List[TimestampMetricValuePairTypeDef]] = None
    StatusCode: Optional[CloudWatchMetricDataStatusCodeType] = None

class CostEstimationResourceCollectionFilterTypeDef(BaseModel):
    CloudFormation: Optional[CloudFormationCostEstimationResourceCollectionFilterTypeDef] = None
    Tags: Optional[List[TagCostEstimationResourceCollectionFilterTypeDef]] = None

class DescribeAccountOverviewRequestRequestTypeDef(BaseModel):
    FromTime: TimestampTypeDef
    ToTime: Optional[TimestampTypeDef] = None

class DescribeOrganizationOverviewRequestRequestTypeDef(BaseModel):
    FromTime: TimestampTypeDef
    ToTime: Optional[TimestampTypeDef] = None
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None

class EndTimeRangeTypeDef(BaseModel):
    FromTime: Optional[TimestampTypeDef] = None
    ToTime: Optional[TimestampTypeDef] = None

class EventTimeRangeTypeDef(BaseModel):
    FromTime: TimestampTypeDef
    ToTime: TimestampTypeDef

class StartTimeRangeTypeDef(BaseModel):
    FromTime: Optional[TimestampTypeDef] = None
    ToTime: Optional[TimestampTypeDef] = None

class DescribeFeedbackResponseTypeDef(BaseModel):
    InsightFeedback: InsightFeedbackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutFeedbackRequestRequestTypeDef(BaseModel):
    InsightFeedback: Optional[InsightFeedbackTypeDef] = None

class DescribeOrganizationResourceCollectionHealthRequestDescribeOrganizationResourceCollectionHealthPaginateTypeDef(BaseModel):
    OrganizationResourceCollectionType: OrganizationResourceCollectionTypeType
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeResourceCollectionHealthRequestDescribeResourceCollectionHealthPaginateTypeDef(BaseModel):
    ResourceCollectionType: ResourceCollectionTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCostEstimationRequestGetCostEstimationPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceCollectionRequestGetResourceCollectionPaginateTypeDef(BaseModel):
    ResourceCollectionType: ResourceCollectionTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnomalousLogGroupsRequestListAnomalousLogGroupsPaginateTypeDef(BaseModel):
    InsightId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotificationChannelsRequestListNotificationChannelsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationsRequestListRecommendationsPaginateTypeDef(BaseModel):
    InsightId: str
    Locale: Optional[LocaleType] = None
    AccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnomaliesForInsightFiltersTypeDef(BaseModel):
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None

class ListMonitoredResourcesRequestListMonitoredResourcesPaginateTypeDef(BaseModel):
    Filters: Optional[ListMonitoredResourcesFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitoredResourcesRequestRequestTypeDef(BaseModel):
    Filters: Optional[ListMonitoredResourcesFiltersTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LogAnomalyShowcaseTypeDef(BaseModel):
    LogAnomalyClasses: Optional[List[LogAnomalyClassTypeDef]] = None

class NotificationChannelConfigPaginatorTypeDef(BaseModel):
    Sns: SnsChannelConfigTypeDef
    Filters: Optional[NotificationFilterConfigPaginatorTypeDef] = None

class NotificationChannelConfigTypeDef(BaseModel):
    Sns: SnsChannelConfigTypeDef
    Filters: Optional[NotificationFilterConfigTypeDef] = None

class UpdateServiceIntegrationConfigTypeDef(BaseModel):
    OpsCenter: Optional[OpsCenterIntegrationConfigTypeDef] = None
    LogsAnomalyDetection: Optional[LogsAnomalyDetectionIntegrationConfigTypeDef] = None
    KMSServerSideEncryption: Optional[KMSServerSideEncryptionIntegrationConfigTypeDef] = None

class ServiceIntegrationConfigTypeDef(BaseModel):
    OpsCenter: Optional[OpsCenterIntegrationTypeDef] = None
    LogsAnomalyDetection: Optional[LogsAnomalyDetectionIntegrationTypeDef] = None
    KMSServerSideEncryption: Optional[KMSServerSideEncryptionIntegrationTypeDef] = None

class PerformanceInsightsMetricQueryTypeDef(BaseModel):
    Metric: Optional[str] = None
    GroupBy: Optional[PerformanceInsightsMetricDimensionGroupTypeDef] = None
    Filter: Optional[Dict[str, str]] = None

class RecommendationRelatedAnomalySourceDetailTypeDef(BaseModel):
    CloudWatchMetrics: Optional[       List[RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef]     ] = None

class RecommendationRelatedEventTypeDef(BaseModel):
    Name: Optional[str] = None
    Resources: Optional[List[RecommendationRelatedEventResourceTypeDef]] = None

class ResourceCollectionFilterTypeDef(BaseModel):
    CloudFormation: Optional[CloudFormationCollectionFilterTypeDef] = None
    Tags: Optional[List[TagCollectionFilterTypeDef]] = None

class ResourceCollectionTypeDef(BaseModel):
    CloudFormation: Optional[CloudFormationCollectionTypeDef] = None
    Tags: Optional[List[TagCollectionTypeDef]] = None

class ServiceHealthTypeDef(BaseModel):
    ServiceName: Optional[ServiceNameType] = None
    Insight: Optional[ServiceInsightHealthTypeDef] = None
    AnalyzedResourceCount: Optional[int] = None

class UpdateResourceCollectionFilterTypeDef(BaseModel):
    CloudFormation: Optional[UpdateCloudFormationCollectionFilterTypeDef] = None
    Tags: Optional[Sequence[UpdateTagCollectionFilterTypeDef]] = None

class DescribeEventSourcesConfigResponseTypeDef(BaseModel):
    EventSources: EventSourcesConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventSourcesConfigRequestRequestTypeDef(BaseModel):
    EventSources: Optional[EventSourcesConfigTypeDef] = None

class CloudWatchMetricsDetailTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[CloudWatchMetricsDimensionTypeDef]] = None
    Stat: Optional[CloudWatchMetricsStatType] = None
    Unit: Optional[str] = None
    Period: Optional[int] = None
    MetricDataSummary: Optional[CloudWatchMetricsDataSummaryTypeDef] = None

class GetCostEstimationResponseTypeDef(BaseModel):
    ResourceCollection: CostEstimationResourceCollectionFilterTypeDef
    Status: CostEstimationStatusType
    Costs: List[ServiceResourceCostTypeDef]
    TimeRange: CostEstimationTimeRangeTypeDef
    TotalCost: float
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCostEstimationRequestRequestTypeDef(BaseModel):
    ResourceCollection: CostEstimationResourceCollectionFilterTypeDef
    ClientToken: Optional[str] = None

class ListInsightsClosedStatusFilterTypeDef(BaseModel):
    Type: InsightTypeType
    EndTimeRange: EndTimeRangeTypeDef

class ListInsightsAnyStatusFilterTypeDef(BaseModel):
    Type: InsightTypeType
    StartTimeRange: StartTimeRangeTypeDef

class ListAnomaliesForInsightRequestListAnomaliesForInsightPaginateTypeDef(BaseModel):
    InsightId: str
    StartTimeRange: Optional[StartTimeRangeTypeDef] = None
    AccountId: Optional[str] = None
    Filters: Optional[ListAnomaliesForInsightFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnomaliesForInsightRequestRequestTypeDef(BaseModel):
    InsightId: str
    StartTimeRange: Optional[StartTimeRangeTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None
    Filters: Optional[ListAnomaliesForInsightFiltersTypeDef] = None

class AnomalousLogGroupTypeDef(BaseModel):
    LogGroupName: Optional[str] = None
    ImpactStartTime: Optional[datetime] = None
    ImpactEndTime: Optional[datetime] = None
    NumberOfLogLinesScanned: Optional[int] = None
    LogAnomalyShowcases: Optional[List[LogAnomalyShowcaseTypeDef]] = None

class NotificationChannelPaginatorTypeDef(BaseModel):
    Id: Optional[str] = None
    Config: Optional[NotificationChannelConfigPaginatorTypeDef] = None

class AddNotificationChannelRequestRequestTypeDef(BaseModel):
    Config: NotificationChannelConfigTypeDef

class NotificationChannelTypeDef(BaseModel):
    Id: Optional[str] = None
    Config: Optional[NotificationChannelConfigTypeDef] = None

class UpdateServiceIntegrationRequestRequestTypeDef(BaseModel):
    ServiceIntegration: UpdateServiceIntegrationConfigTypeDef

class DescribeServiceIntegrationResponseTypeDef(BaseModel):
    ServiceIntegration: ServiceIntegrationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PerformanceInsightsReferenceMetricTypeDef(BaseModel):
    MetricQuery: Optional[PerformanceInsightsMetricQueryTypeDef] = None

class RecommendationRelatedAnomalyTypeDef(BaseModel):
    Resources: Optional[List[RecommendationRelatedAnomalyResourceTypeDef]] = None
    SourceDetails: Optional[List[RecommendationRelatedAnomalySourceDetailTypeDef]] = None
    AnomalyId: Optional[str] = None

class GetResourceCollectionResponseTypeDef(BaseModel):
    ResourceCollection: ResourceCollectionFilterTypeDef
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventTypeDef(BaseModel):
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    Id: Optional[str] = None
    Time: Optional[datetime] = None
    EventSource: Optional[str] = None
    Name: Optional[str] = None
    DataSource: Optional[EventDataSourceType] = None
    EventClass: Optional[EventClassType] = None
    Resources: Optional[List[EventResourceTypeDef]] = None

class ListEventsFiltersTypeDef(BaseModel):
    InsightId: Optional[str] = None
    EventTimeRange: Optional[EventTimeRangeTypeDef] = None
    EventClass: Optional[EventClassType] = None
    EventSource: Optional[str] = None
    DataSource: Optional[EventDataSourceType] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None

class MonitoredResourceIdentifierTypeDef(BaseModel):
    MonitoredResourceName: Optional[str] = None
    Type: Optional[str] = None
    ResourcePermission: Optional[ResourcePermissionType] = None
    LastUpdated: Optional[datetime] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None

class ProactiveInsightSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None
    AssociatedResourceArns: Optional[List[str]] = None

class ProactiveInsightTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    SsmOpsItemId: Optional[str] = None
    Description: Optional[str] = None

class ProactiveOrganizationInsightSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None

class ReactiveInsightSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None
    AssociatedResourceArns: Optional[List[str]] = None

class ReactiveInsightTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    SsmOpsItemId: Optional[str] = None
    Description: Optional[str] = None

class ReactiveOrganizationInsightSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None

class SearchInsightsFiltersTypeDef(BaseModel):
    Severities: Optional[Sequence[InsightSeverityType]] = None
    Statuses: Optional[Sequence[InsightStatusType]] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None

class SearchOrganizationInsightsFiltersTypeDef(BaseModel):
    Severities: Optional[Sequence[InsightSeverityType]] = None
    Statuses: Optional[Sequence[InsightStatusType]] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None

class DescribeOrganizationResourceCollectionHealthResponseTypeDef(BaseModel):
    CloudFormation: List[CloudFormationHealthTypeDef]
    Service: List[ServiceHealthTypeDef]
    Account: List[AccountHealthTypeDef]
    NextToken: str
    Tags: List[TagHealthTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourceCollectionHealthResponseTypeDef(BaseModel):
    CloudFormation: List[CloudFormationHealthTypeDef]
    Service: List[ServiceHealthTypeDef]
    NextToken: str
    Tags: List[TagHealthTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResourceCollectionRequestRequestTypeDef(BaseModel):
    Action: UpdateResourceCollectionActionType
    ResourceCollection: UpdateResourceCollectionFilterTypeDef

class ListInsightsStatusFilterTypeDef(BaseModel):
    Ongoing: Optional[ListInsightsOngoingStatusFilterTypeDef] = None
    Closed: Optional[ListInsightsClosedStatusFilterTypeDef] = None
    Any: Optional[ListInsightsAnyStatusFilterTypeDef] = None

class ListAnomalousLogGroupsResponseTypeDef(BaseModel):
    InsightId: str
    AnomalousLogGroups: List[AnomalousLogGroupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotificationChannelsResponsePaginatorTypeDef(BaseModel):
    Channels: List[NotificationChannelPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotificationChannelsResponseTypeDef(BaseModel):
    Channels: List[NotificationChannelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PerformanceInsightsReferenceComparisonValuesTypeDef(BaseModel):
    ReferenceScalar: Optional[PerformanceInsightsReferenceScalarTypeDef] = None
    ReferenceMetric: Optional[PerformanceInsightsReferenceMetricTypeDef] = None

class RecommendationTypeDef(BaseModel):
    Description: Optional[str] = None
    Link: Optional[str] = None
    Name: Optional[str] = None
    Reason: Optional[str] = None
    RelatedEvents: Optional[List[RecommendationRelatedEventTypeDef]] = None
    RelatedAnomalies: Optional[List[RecommendationRelatedAnomalyTypeDef]] = None
    Category: Optional[str] = None

class ListEventsResponseTypeDef(BaseModel):
    Events: List[EventTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventsRequestListEventsPaginateTypeDef(BaseModel):
    Filters: ListEventsFiltersTypeDef
    AccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventsRequestRequestTypeDef(BaseModel):
    Filters: ListEventsFiltersTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None

class ListMonitoredResourcesResponseTypeDef(BaseModel):
    MonitoredResourceIdentifiers: List[MonitoredResourceIdentifierTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInsightsResponseTypeDef(BaseModel):
    ProactiveInsights: List[ProactiveInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveInsightSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchInsightsResponseTypeDef(BaseModel):
    ProactiveInsights: List[ProactiveInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveInsightSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchOrganizationInsightsResponseTypeDef(BaseModel):
    ProactiveInsights: List[ProactiveInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveInsightSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInsightResponseTypeDef(BaseModel):
    ProactiveInsight: ProactiveInsightTypeDef
    ReactiveInsight: ReactiveInsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationInsightsResponseTypeDef(BaseModel):
    ProactiveInsights: List[ProactiveOrganizationInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveOrganizationInsightSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchInsightsRequestRequestTypeDef(BaseModel):
    StartTimeRange: StartTimeRangeTypeDef
    Type: InsightTypeType
    Filters: Optional[SearchInsightsFiltersTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SearchInsightsRequestSearchInsightsPaginateTypeDef(BaseModel):
    StartTimeRange: StartTimeRangeTypeDef
    Type: InsightTypeType
    Filters: Optional[SearchInsightsFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchOrganizationInsightsRequestRequestTypeDef(BaseModel):
    AccountIds: Sequence[str]
    StartTimeRange: StartTimeRangeTypeDef
    Type: InsightTypeType
    Filters: Optional[SearchOrganizationInsightsFiltersTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SearchOrganizationInsightsRequestSearchOrganizationInsightsPaginateTypeDef(BaseModel):
    AccountIds: Sequence[str]
    StartTimeRange: StartTimeRangeTypeDef
    Type: InsightTypeType
    Filters: Optional[SearchOrganizationInsightsFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInsightsRequestListInsightsPaginateTypeDef(BaseModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInsightsRequestRequestTypeDef(BaseModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOrganizationInsightsRequestListOrganizationInsightsPaginateTypeDef(BaseModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationInsightsRequestRequestTypeDef(BaseModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    MaxResults: Optional[int] = None
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class PerformanceInsightsReferenceDataTypeDef(BaseModel):
    Name: Optional[str] = None
    ComparisonValues: Optional[PerformanceInsightsReferenceComparisonValuesTypeDef] = None

class ListRecommendationsResponseTypeDef(BaseModel):
    Recommendations: List[RecommendationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PerformanceInsightsMetricsDetailTypeDef(BaseModel):
    MetricDisplayName: Optional[str] = None
    Unit: Optional[str] = None
    MetricQuery: Optional[PerformanceInsightsMetricQueryTypeDef] = None
    ReferenceData: Optional[List[PerformanceInsightsReferenceDataTypeDef]] = None
    StatsAtAnomaly: Optional[List[PerformanceInsightsStatTypeDef]] = None
    StatsAtBaseline: Optional[List[PerformanceInsightsStatTypeDef]] = None

class AnomalySourceDetailsTypeDef(BaseModel):
    CloudWatchMetrics: Optional[List[CloudWatchMetricsDetailTypeDef]] = None
    PerformanceInsightsMetrics: Optional[List[PerformanceInsightsMetricsDetailTypeDef]] = None

class ProactiveAnomalySummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Severity: Optional[AnomalySeverityType] = None
    Status: Optional[AnomalyStatusType] = None
    UpdateTime: Optional[datetime] = None
    AnomalyTimeRange: Optional[AnomalyTimeRangeTypeDef] = None
    AnomalyReportedTimeRange: Optional[AnomalyReportedTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    SourceDetails: Optional[AnomalySourceDetailsTypeDef] = None
    AssociatedInsightId: Optional[str] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    Limit: Optional[float] = None
    SourceMetadata: Optional[AnomalySourceMetadataTypeDef] = None
    AnomalyResources: Optional[List[AnomalyResourceTypeDef]] = None
    Description: Optional[str] = None

class ProactiveAnomalyTypeDef(BaseModel):
    Id: Optional[str] = None
    Severity: Optional[AnomalySeverityType] = None
    Status: Optional[AnomalyStatusType] = None
    UpdateTime: Optional[datetime] = None
    AnomalyTimeRange: Optional[AnomalyTimeRangeTypeDef] = None
    AnomalyReportedTimeRange: Optional[AnomalyReportedTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    SourceDetails: Optional[AnomalySourceDetailsTypeDef] = None
    AssociatedInsightId: Optional[str] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    Limit: Optional[float] = None
    SourceMetadata: Optional[AnomalySourceMetadataTypeDef] = None
    AnomalyResources: Optional[List[AnomalyResourceTypeDef]] = None
    Description: Optional[str] = None

class ReactiveAnomalySummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Severity: Optional[AnomalySeverityType] = None
    Status: Optional[AnomalyStatusType] = None
    AnomalyTimeRange: Optional[AnomalyTimeRangeTypeDef] = None
    AnomalyReportedTimeRange: Optional[AnomalyReportedTimeRangeTypeDef] = None
    SourceDetails: Optional[AnomalySourceDetailsTypeDef] = None
    AssociatedInsightId: Optional[str] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    Type: Optional[AnomalyTypeType] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CausalAnomalyId: Optional[str] = None
    AnomalyResources: Optional[List[AnomalyResourceTypeDef]] = None

class ReactiveAnomalyTypeDef(BaseModel):
    Id: Optional[str] = None
    Severity: Optional[AnomalySeverityType] = None
    Status: Optional[AnomalyStatusType] = None
    AnomalyTimeRange: Optional[AnomalyTimeRangeTypeDef] = None
    AnomalyReportedTimeRange: Optional[AnomalyReportedTimeRangeTypeDef] = None
    SourceDetails: Optional[AnomalySourceDetailsTypeDef] = None
    AssociatedInsightId: Optional[str] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    Type: Optional[AnomalyTypeType] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CausalAnomalyId: Optional[str] = None
    AnomalyResources: Optional[List[AnomalyResourceTypeDef]] = None

class ListAnomaliesForInsightResponseTypeDef(BaseModel):
    ProactiveAnomalies: List[ProactiveAnomalySummaryTypeDef]
    ReactiveAnomalies: List[ReactiveAnomalySummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAnomalyResponseTypeDef(BaseModel):
    ProactiveAnomaly: ProactiveAnomalyTypeDef
    ReactiveAnomaly: ReactiveAnomalyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

