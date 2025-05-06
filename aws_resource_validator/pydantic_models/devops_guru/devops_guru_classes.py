from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.devops_guru.devops_guru_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountInsightHealth(BaseValidatorModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AmazonCodeGuruProfilerIntegration(BaseValidatorModel):
    Status: Optional[EventSourceOptInStatusType] = None


class AnomalyReportedTimeRange(BaseValidatorModel):
    OpenTime: datetime
    CloseTime: Optional[datetime] = None


class AnomalyResource(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None


class AnomalySourceMetadata(BaseValidatorModel):
    Source: Optional[str] = None
    SourceResourceName: Optional[str] = None
    SourceResourceType: Optional[str] = None


class AnomalyTimeRange(BaseValidatorModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None


class CloudFormationCollectionFilter(BaseValidatorModel):
    StackNames: Optional[List[str]] = None


class CloudFormationCollectionOutput(BaseValidatorModel):
    StackNames: Optional[List[str]] = None


class CloudFormationCollection(BaseValidatorModel):
    StackNames: Optional[List[str]] = None


class CloudFormationCostEstimationResourceCollectionFilterOutput(BaseValidatorModel):
    StackNames: Optional[List[str]] = None


class CloudFormationCostEstimationResourceCollectionFilter(BaseValidatorModel):
    StackNames: Optional[List[str]] = None


class InsightHealth(BaseValidatorModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None
    MeanTimeToRecoverInMilliseconds: Optional[int] = None


class TimestampMetricValuePair(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    MetricValue: Optional[float] = None


class CloudWatchMetricsDimension(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class TagCostEstimationResourceCollectionFilterOutput(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]


class TagCostEstimationResourceCollectionFilter(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]


class CostEstimationTimeRange(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class DeleteInsightRequest(BaseValidatorModel):
    Id: str

Timestamp = Union[datetime, str]


class DescribeAnomalyRequest(BaseValidatorModel):
    Id: str
    AccountId: Optional[str] = None


class DescribeFeedbackRequest(BaseValidatorModel):
    InsightId: Optional[str] = None


class InsightFeedback(BaseValidatorModel):
    Id: Optional[str] = None
    Feedback: Optional[InsightFeedbackOptionType] = None


class DescribeInsightRequest(BaseValidatorModel):
    Id: str
    AccountId: Optional[str] = None


class DescribeOrganizationHealthRequest(BaseValidatorModel):
    AccountIds: Optional[List[str]] = None
    OrganizationalUnitIds: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeOrganizationResourceCollectionHealthRequest(BaseValidatorModel):
    OrganizationResourceCollectionType: OrganizationResourceCollectionTypeType
    AccountIds: Optional[List[str]] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeResourceCollectionHealthRequest(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    NextToken: Optional[str] = None


class EventResource(BaseValidatorModel):
    Type: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None


class GetCostEstimationRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class ServiceResourceCost(BaseValidatorModel):
    Type: Optional[str] = None
    State: Optional[CostEstimationServiceResourceStateType] = None
    Count: Optional[int] = None
    UnitCost: Optional[float] = None
    Cost: Optional[float] = None


class GetResourceCollectionRequest(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    NextToken: Optional[str] = None


class InsightTimeRange(BaseValidatorModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None


class KMSServerSideEncryptionIntegrationConfig(BaseValidatorModel):
    KMSKeyId: Optional[str] = None
    OptInStatus: Optional[OptInStatusType] = None
    Type: Optional[ServerSideEncryptionTypeType] = None


class KMSServerSideEncryptionIntegration(BaseValidatorModel):
    KMSKeyId: Optional[str] = None
    OptInStatus: Optional[OptInStatusType] = None
    Type: Optional[ServerSideEncryptionTypeType] = None


class ListAnomalousLogGroupsRequest(BaseValidatorModel):
    InsightId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInsightsOngoingStatusFilter(BaseValidatorModel):
    Type: InsightTypeType


class ListMonitoredResourcesFilters(BaseValidatorModel):
    ResourcePermission: ResourcePermissionType
    ResourceTypeFilters: List[ResourceTypeFilterType]


class ListNotificationChannelsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListRecommendationsRequest(BaseValidatorModel):
    InsightId: str
    NextToken: Optional[str] = None
    Locale: Optional[LocaleType] = None
    AccountId: Optional[str] = None


class LogAnomalyClass(BaseValidatorModel):
    LogStreamName: Optional[str] = None
    LogAnomalyType: Optional[LogAnomalyTypeType] = None
    LogAnomalyToken: Optional[str] = None
    LogEventId: Optional[str] = None
    Explanation: Optional[str] = None
    NumberOfLogLinesOccurrences: Optional[int] = None
    LogEventTimestamp: Optional[datetime] = None


class LogsAnomalyDetectionIntegrationConfig(BaseValidatorModel):
    OptInStatus: Optional[OptInStatusType] = None


class LogsAnomalyDetectionIntegration(BaseValidatorModel):
    OptInStatus: Optional[OptInStatusType] = None


class NotificationFilterConfigOutput(BaseValidatorModel):
    Severities: Optional[List[InsightSeverityType]] = None
    MessageTypes: Optional[List[NotificationMessageTypeType]] = None


class SnsChannelConfig(BaseValidatorModel):
    TopicArn: Optional[str] = None


class NotificationFilterConfig(BaseValidatorModel):
    Severities: Optional[List[InsightSeverityType]] = None
    MessageTypes: Optional[List[NotificationMessageTypeType]] = None


class OpsCenterIntegrationConfig(BaseValidatorModel):
    OptInStatus: Optional[OptInStatusType] = None


class OpsCenterIntegration(BaseValidatorModel):
    OptInStatus: Optional[OptInStatusType] = None


class PerformanceInsightsMetricDimensionGroup(BaseValidatorModel):
    Group: Optional[str] = None
    Dimensions: Optional[List[str]] = None
    Limit: Optional[int] = None


class PerformanceInsightsStat(BaseValidatorModel):
    Type: Optional[str] = None
    Value: Optional[float] = None


class PerformanceInsightsReferenceScalar(BaseValidatorModel):
    Value: Optional[float] = None


class PredictionTimeRange(BaseValidatorModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None


class ServiceCollectionOutput(BaseValidatorModel):
    ServiceNames: Optional[List[ServiceNameType]] = None


class RecommendationRelatedAnomalyResource(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None


class RecommendationRelatedCloudWatchMetricsSourceDetail(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None


class RecommendationRelatedEventResource(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None


class RemoveNotificationChannelRequest(BaseValidatorModel):
    Id: str


class TagCollectionFilter(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]


class TagCollectionOutput(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]


class ServiceCollection(BaseValidatorModel):
    ServiceNames: Optional[List[ServiceNameType]] = None


class ServiceInsightHealth(BaseValidatorModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None


class TagCollection(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]


class UpdateCloudFormationCollectionFilter(BaseValidatorModel):
    StackNames: Optional[List[str]] = None


class UpdateTagCollectionFilter(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]


class AccountHealth(BaseValidatorModel):
    AccountId: Optional[str] = None
    Insight: Optional[AccountInsightHealth] = None


class AddNotificationChannelResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class DescribeAccountHealthResponse(BaseValidatorModel):
    OpenReactiveInsights: int
    OpenProactiveInsights: int
    MetricsAnalyzed: int
    ResourceHours: int
    AnalyzedResourceCount: int
    ResponseMetadata: ResponseMetadata


class DescribeAccountOverviewResponse(BaseValidatorModel):
    ReactiveInsights: int
    ProactiveInsights: int
    MeanTimeToRecoverInMilliseconds: int
    ResponseMetadata: ResponseMetadata


class DescribeOrganizationHealthResponse(BaseValidatorModel):
    OpenReactiveInsights: int
    OpenProactiveInsights: int
    MetricsAnalyzed: int
    ResourceHours: int
    ResponseMetadata: ResponseMetadata


class DescribeOrganizationOverviewResponse(BaseValidatorModel):
    ReactiveInsights: int
    ProactiveInsights: int
    ResponseMetadata: ResponseMetadata


class EventSourcesConfig(BaseValidatorModel):
    AmazonCodeGuruProfiler: Optional[AmazonCodeGuruProfilerIntegration] = None

CloudFormationCollectionUnion = Union[CloudFormationCollection, CloudFormationCollectionOutput]


class CloudFormationHealth(BaseValidatorModel):
    StackName: Optional[str] = None
    Insight: Optional[InsightHealth] = None
    AnalyzedResourceCount: Optional[int] = None


class TagHealth(BaseValidatorModel):
    AppBoundaryKey: Optional[str] = None
    TagValue: Optional[str] = None
    Insight: Optional[InsightHealth] = None
    AnalyzedResourceCount: Optional[int] = None


class CloudWatchMetricsDataSummary(BaseValidatorModel):
    TimestampMetricValuePairList: Optional[List[TimestampMetricValuePair]] = None
    StatusCode: Optional[CloudWatchMetricDataStatusCodeType] = None


class CostEstimationResourceCollectionFilterOutput(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCostEstimationResourceCollectionFilterOutput] = None
    Tags: Optional[List[TagCostEstimationResourceCollectionFilterOutput]] = None


class CostEstimationResourceCollectionFilter(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCostEstimationResourceCollectionFilter] = None
    Tags: Optional[List[TagCostEstimationResourceCollectionFilter]] = None


class DescribeAccountOverviewRequest(BaseValidatorModel):
    FromTime: Timestamp
    ToTime: Optional[Timestamp] = None


class DescribeOrganizationOverviewRequest(BaseValidatorModel):
    FromTime: Timestamp
    ToTime: Optional[Timestamp] = None
    AccountIds: Optional[List[str]] = None
    OrganizationalUnitIds: Optional[List[str]] = None


class EndTimeRange(BaseValidatorModel):
    FromTime: Optional[Timestamp] = None
    ToTime: Optional[Timestamp] = None


class EventTimeRange(BaseValidatorModel):
    FromTime: Timestamp
    ToTime: Timestamp


class StartTimeRange(BaseValidatorModel):
    FromTime: Optional[Timestamp] = None
    ToTime: Optional[Timestamp] = None


class DescribeFeedbackResponse(BaseValidatorModel):
    InsightFeedback: InsightFeedback
    ResponseMetadata: ResponseMetadata


class PutFeedbackRequest(BaseValidatorModel):
    InsightFeedback: Optional[InsightFeedback] = None


class DescribeOrganizationResourceCollectionHealthRequestPaginate(BaseValidatorModel):
    OrganizationResourceCollectionType: OrganizationResourceCollectionTypeType
    AccountIds: Optional[List[str]] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeResourceCollectionHealthRequestPaginate(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCostEstimationRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetResourceCollectionRequestPaginate(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnomalousLogGroupsRequestPaginate(BaseValidatorModel):
    InsightId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotificationChannelsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecommendationsRequestPaginate(BaseValidatorModel):
    InsightId: str
    Locale: Optional[LocaleType] = None
    AccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitoredResourcesRequestPaginate(BaseValidatorModel):
    Filters: Optional[ListMonitoredResourcesFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitoredResourcesRequest(BaseValidatorModel):
    Filters: Optional[ListMonitoredResourcesFilters] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LogAnomalyShowcase(BaseValidatorModel):
    LogAnomalyClasses: Optional[List[LogAnomalyClass]] = None


class NotificationChannelConfigOutput(BaseValidatorModel):
    Sns: SnsChannelConfig
    Filters: Optional[NotificationFilterConfigOutput] = None


class NotificationChannelConfig(BaseValidatorModel):
    Sns: SnsChannelConfig
    Filters: Optional[NotificationFilterConfig] = None


class UpdateServiceIntegrationConfig(BaseValidatorModel):
    OpsCenter: Optional[OpsCenterIntegrationConfig] = None
    LogsAnomalyDetection: Optional[LogsAnomalyDetectionIntegrationConfig] = None
    KMSServerSideEncryption: Optional[KMSServerSideEncryptionIntegrationConfig] = None


class ServiceIntegrationConfig(BaseValidatorModel):
    OpsCenter: Optional[OpsCenterIntegration] = None
    LogsAnomalyDetection: Optional[LogsAnomalyDetectionIntegration] = None
    KMSServerSideEncryption: Optional[KMSServerSideEncryptionIntegration] = None


class PerformanceInsightsMetricQuery(BaseValidatorModel):
    Metric: Optional[str] = None
    GroupBy: Optional[PerformanceInsightsMetricDimensionGroup] = None
    Filter: Optional[Dict[str, str]] = None


class RecommendationRelatedAnomalySourceDetail(BaseValidatorModel):
    CloudWatchMetrics: Optional[List[RecommendationRelatedCloudWatchMetricsSourceDetail]] = None


class RecommendationRelatedEvent(BaseValidatorModel):
    Name: Optional[str] = None
    Resources: Optional[List[RecommendationRelatedEventResource]] = None


class ResourceCollectionFilter(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCollectionFilter] = None
    Tags: Optional[List[TagCollectionFilter]] = None


class ResourceCollectionOutput(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCollectionOutput] = None
    Tags: Optional[List[TagCollectionOutput]] = None

ServiceCollectionUnion = Union[ServiceCollection, ServiceCollectionOutput]


class ServiceHealth(BaseValidatorModel):
    ServiceName: Optional[ServiceNameType] = None
    Insight: Optional[ServiceInsightHealth] = None
    AnalyzedResourceCount: Optional[int] = None

TagCollectionUnion = Union[TagCollection, TagCollectionOutput]


class UpdateResourceCollectionFilter(BaseValidatorModel):
    CloudFormation: Optional[UpdateCloudFormationCollectionFilter] = None
    Tags: Optional[List[UpdateTagCollectionFilter]] = None


class DescribeEventSourcesConfigResponse(BaseValidatorModel):
    EventSources: EventSourcesConfig
    ResponseMetadata: ResponseMetadata


class UpdateEventSourcesConfigRequest(BaseValidatorModel):
    EventSources: Optional[EventSourcesConfig] = None


class CloudWatchMetricsDetail(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[CloudWatchMetricsDimension]] = None
    Stat: Optional[CloudWatchMetricsStatType] = None
    Unit: Optional[str] = None
    Period: Optional[int] = None
    MetricDataSummary: Optional[CloudWatchMetricsDataSummary] = None


class GetCostEstimationResponse(BaseValidatorModel):
    ResourceCollection: CostEstimationResourceCollectionFilterOutput
    Status: CostEstimationStatusType
    Costs: List[ServiceResourceCost]
    TimeRange: CostEstimationTimeRange
    TotalCost: float
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

CostEstimationResourceCollectionFilterUnion = Union[CostEstimationResourceCollectionFilter, CostEstimationResourceCollectionFilterOutput]


class ListInsightsClosedStatusFilter(BaseValidatorModel):
    Type: InsightTypeType
    EndTimeRange: EndTimeRange


class ListInsightsAnyStatusFilter(BaseValidatorModel):
    Type: InsightTypeType
    StartTimeRange: StartTimeRange


class AnomalousLogGroup(BaseValidatorModel):
    LogGroupName: Optional[str] = None
    ImpactStartTime: Optional[datetime] = None
    ImpactEndTime: Optional[datetime] = None
    NumberOfLogLinesScanned: Optional[int] = None
    LogAnomalyShowcases: Optional[List[LogAnomalyShowcase]] = None


class NotificationChannel(BaseValidatorModel):
    Id: Optional[str] = None
    Config: Optional[NotificationChannelConfigOutput] = None

NotificationChannelConfigUnion = Union[NotificationChannelConfig, NotificationChannelConfigOutput]


class UpdateServiceIntegrationRequest(BaseValidatorModel):
    ServiceIntegration: UpdateServiceIntegrationConfig


class DescribeServiceIntegrationResponse(BaseValidatorModel):
    ServiceIntegration: ServiceIntegrationConfig
    ResponseMetadata: ResponseMetadata


class PerformanceInsightsReferenceMetric(BaseValidatorModel):
    MetricQuery: Optional[PerformanceInsightsMetricQuery] = None


class RecommendationRelatedAnomaly(BaseValidatorModel):
    Resources: Optional[List[RecommendationRelatedAnomalyResource]] = None
    SourceDetails: Optional[List[RecommendationRelatedAnomalySourceDetail]] = None
    AnomalyId: Optional[str] = None


class GetResourceCollectionResponse(BaseValidatorModel):
    ResourceCollection: ResourceCollectionFilter
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Event(BaseValidatorModel):
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    Id: Optional[str] = None
    Time: Optional[datetime] = None
    EventSource: Optional[str] = None
    Name: Optional[str] = None
    DataSource: Optional[EventDataSourceType] = None
    EventClass: Optional[EventClassType] = None
    Resources: Optional[List[EventResource]] = None


class MonitoredResourceIdentifier(BaseValidatorModel):
    MonitoredResourceName: Optional[str] = None
    Type: Optional[str] = None
    ResourcePermission: Optional[ResourcePermissionType] = None
    LastUpdated: Optional[datetime] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None


class ProactiveInsightSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRange] = None
    PredictionTimeRange: Optional[PredictionTimeRange] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    ServiceCollection: Optional[ServiceCollectionOutput] = None
    AssociatedResourceArns: Optional[List[str]] = None


class ProactiveInsight(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRange] = None
    PredictionTimeRange: Optional[PredictionTimeRange] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    SsmOpsItemId: Optional[str] = None
    Description: Optional[str] = None


class ProactiveOrganizationInsightSummary(BaseValidatorModel):
    Id: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRange] = None
    PredictionTimeRange: Optional[PredictionTimeRange] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    ServiceCollection: Optional[ServiceCollectionOutput] = None


class ReactiveInsightSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRange] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    ServiceCollection: Optional[ServiceCollectionOutput] = None
    AssociatedResourceArns: Optional[List[str]] = None


class ReactiveInsight(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRange] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    SsmOpsItemId: Optional[str] = None
    Description: Optional[str] = None


class ReactiveOrganizationInsightSummary(BaseValidatorModel):
    Id: Optional[str] = None
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRange] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    ServiceCollection: Optional[ServiceCollectionOutput] = None


class ListAnomaliesForInsightFilters(BaseValidatorModel):
    ServiceCollection: Optional[ServiceCollectionUnion] = None


class DescribeOrganizationResourceCollectionHealthResponse(BaseValidatorModel):
    CloudFormation: List[CloudFormationHealth]
    Service: List[ServiceHealth]
    Account: List[AccountHealth]
    Tags: List[TagHealth]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeResourceCollectionHealthResponse(BaseValidatorModel):
    CloudFormation: List[CloudFormationHealth]
    Service: List[ServiceHealth]
    Tags: List[TagHealth]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResourceCollection(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCollectionUnion] = None
    Tags: Optional[List[TagCollectionUnion]] = None


class UpdateResourceCollectionRequest(BaseValidatorModel):
    Action: UpdateResourceCollectionActionType
    ResourceCollection: UpdateResourceCollectionFilter


class StartCostEstimationRequest(BaseValidatorModel):
    ResourceCollection: CostEstimationResourceCollectionFilterUnion
    ClientToken: Optional[str] = None


class ListInsightsStatusFilter(BaseValidatorModel):
    Ongoing: Optional[ListInsightsOngoingStatusFilter] = None
    Closed: Optional[ListInsightsClosedStatusFilter] = None
    Any: Optional[ListInsightsAnyStatusFilter] = None


class ListAnomalousLogGroupsResponse(BaseValidatorModel):
    InsightId: str
    AnomalousLogGroups: List[AnomalousLogGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNotificationChannelsResponse(BaseValidatorModel):
    Channels: List[NotificationChannel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AddNotificationChannelRequest(BaseValidatorModel):
    Config: NotificationChannelConfigUnion


class PerformanceInsightsReferenceComparisonValues(BaseValidatorModel):
    ReferenceScalar: Optional[PerformanceInsightsReferenceScalar] = None
    ReferenceMetric: Optional[PerformanceInsightsReferenceMetric] = None


class Recommendation(BaseValidatorModel):
    Description: Optional[str] = None
    Link: Optional[str] = None
    Name: Optional[str] = None
    Reason: Optional[str] = None
    RelatedEvents: Optional[List[RecommendationRelatedEvent]] = None
    RelatedAnomalies: Optional[List[RecommendationRelatedAnomaly]] = None
    Category: Optional[str] = None


class ListEventsResponse(BaseValidatorModel):
    Events: List[Event]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMonitoredResourcesResponse(BaseValidatorModel):
    MonitoredResourceIdentifiers: List[MonitoredResourceIdentifier]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListInsightsResponse(BaseValidatorModel):
    ProactiveInsights: List[ProactiveInsightSummary]
    ReactiveInsights: List[ReactiveInsightSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchInsightsResponse(BaseValidatorModel):
    ProactiveInsights: List[ProactiveInsightSummary]
    ReactiveInsights: List[ReactiveInsightSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchOrganizationInsightsResponse(BaseValidatorModel):
    ProactiveInsights: List[ProactiveInsightSummary]
    ReactiveInsights: List[ReactiveInsightSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInsightResponse(BaseValidatorModel):
    ProactiveInsight: ProactiveInsight
    ReactiveInsight: ReactiveInsight
    ResponseMetadata: ResponseMetadata


class ListOrganizationInsightsResponse(BaseValidatorModel):
    ProactiveInsights: List[ProactiveOrganizationInsightSummary]
    ReactiveInsights: List[ReactiveOrganizationInsightSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAnomaliesForInsightRequestPaginate(BaseValidatorModel):
    InsightId: str
    StartTimeRange: Optional[StartTimeRange] = None
    AccountId: Optional[str] = None
    Filters: Optional[ListAnomaliesForInsightFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnomaliesForInsightRequest(BaseValidatorModel):
    InsightId: str
    StartTimeRange: Optional[StartTimeRange] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None
    Filters: Optional[ListAnomaliesForInsightFilters] = None

ResourceCollectionUnion = Union[ResourceCollection, ResourceCollectionOutput]


class ListInsightsRequestPaginate(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilter
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInsightsRequest(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilter
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOrganizationInsightsRequestPaginate(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilter
    AccountIds: Optional[List[str]] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationInsightsRequest(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilter
    MaxResults: Optional[int] = None
    AccountIds: Optional[List[str]] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    NextToken: Optional[str] = None


class PerformanceInsightsReferenceData(BaseValidatorModel):
    Name: Optional[str] = None
    ComparisonValues: Optional[PerformanceInsightsReferenceComparisonValues] = None


class ListRecommendationsResponse(BaseValidatorModel):
    Recommendations: List[Recommendation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEventsFilters(BaseValidatorModel):
    InsightId: Optional[str] = None
    EventTimeRange: Optional[EventTimeRange] = None
    EventClass: Optional[EventClassType] = None
    EventSource: Optional[str] = None
    DataSource: Optional[EventDataSourceType] = None
    ResourceCollection: Optional[ResourceCollectionUnion] = None


class SearchInsightsFilters(BaseValidatorModel):
    Severities: Optional[List[InsightSeverityType]] = None
    Statuses: Optional[List[InsightStatusType]] = None
    ResourceCollection: Optional[ResourceCollectionUnion] = None
    ServiceCollection: Optional[ServiceCollectionUnion] = None


class SearchOrganizationInsightsFilters(BaseValidatorModel):
    Severities: Optional[List[InsightSeverityType]] = None
    Statuses: Optional[List[InsightStatusType]] = None
    ResourceCollection: Optional[ResourceCollectionUnion] = None
    ServiceCollection: Optional[ServiceCollectionUnion] = None


class PerformanceInsightsMetricsDetail(BaseValidatorModel):
    MetricDisplayName: Optional[str] = None
    Unit: Optional[str] = None
    MetricQuery: Optional[PerformanceInsightsMetricQuery] = None
    ReferenceData: Optional[List[PerformanceInsightsReferenceData]] = None
    StatsAtAnomaly: Optional[List[PerformanceInsightsStat]] = None
    StatsAtBaseline: Optional[List[PerformanceInsightsStat]] = None


class ListEventsRequestPaginate(BaseValidatorModel):
    Filters: ListEventsFilters
    AccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventsRequest(BaseValidatorModel):
    Filters: ListEventsFilters
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class SearchInsightsRequestPaginate(BaseValidatorModel):
    StartTimeRange: StartTimeRange
    Type: InsightTypeType
    Filters: Optional[SearchInsightsFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchInsightsRequest(BaseValidatorModel):
    StartTimeRange: StartTimeRange
    Type: InsightTypeType
    Filters: Optional[SearchInsightsFilters] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SearchOrganizationInsightsRequestPaginate(BaseValidatorModel):
    AccountIds: List[str]
    StartTimeRange: StartTimeRange
    Type: InsightTypeType
    Filters: Optional[SearchOrganizationInsightsFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchOrganizationInsightsRequest(BaseValidatorModel):
    AccountIds: List[str]
    StartTimeRange: StartTimeRange
    Type: InsightTypeType
    Filters: Optional[SearchOrganizationInsightsFilters] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class AnomalySourceDetails(BaseValidatorModel):
    CloudWatchMetrics: Optional[List[CloudWatchMetricsDetail]] = None
    PerformanceInsightsMetrics: Optional[List[PerformanceInsightsMetricsDetail]] = None


class ProactiveAnomalySummary(BaseValidatorModel):
    Id: Optional[str] = None
    Severity: Optional[AnomalySeverityType] = None
    Status: Optional[AnomalyStatusType] = None
    UpdateTime: Optional[datetime] = None
    AnomalyTimeRange: Optional[AnomalyTimeRange] = None
    AnomalyReportedTimeRange: Optional[AnomalyReportedTimeRange] = None
    PredictionTimeRange: Optional[PredictionTimeRange] = None
    SourceDetails: Optional[AnomalySourceDetails] = None
    AssociatedInsightId: Optional[str] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    Limit: Optional[float] = None
    SourceMetadata: Optional[AnomalySourceMetadata] = None
    AnomalyResources: Optional[List[AnomalyResource]] = None
    Description: Optional[str] = None


class ProactiveAnomaly(BaseValidatorModel):
    Id: Optional[str] = None
    Severity: Optional[AnomalySeverityType] = None
    Status: Optional[AnomalyStatusType] = None
    UpdateTime: Optional[datetime] = None
    AnomalyTimeRange: Optional[AnomalyTimeRange] = None
    AnomalyReportedTimeRange: Optional[AnomalyReportedTimeRange] = None
    PredictionTimeRange: Optional[PredictionTimeRange] = None
    SourceDetails: Optional[AnomalySourceDetails] = None
    AssociatedInsightId: Optional[str] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    Limit: Optional[float] = None
    SourceMetadata: Optional[AnomalySourceMetadata] = None
    AnomalyResources: Optional[List[AnomalyResource]] = None
    Description: Optional[str] = None


class ReactiveAnomalySummary(BaseValidatorModel):
    Id: Optional[str] = None
    Severity: Optional[AnomalySeverityType] = None
    Status: Optional[AnomalyStatusType] = None
    AnomalyTimeRange: Optional[AnomalyTimeRange] = None
    AnomalyReportedTimeRange: Optional[AnomalyReportedTimeRange] = None
    SourceDetails: Optional[AnomalySourceDetails] = None
    AssociatedInsightId: Optional[str] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    Type: Optional[AnomalyTypeType] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CausalAnomalyId: Optional[str] = None
    AnomalyResources: Optional[List[AnomalyResource]] = None


class ReactiveAnomaly(BaseValidatorModel):
    Id: Optional[str] = None
    Severity: Optional[AnomalySeverityType] = None
    Status: Optional[AnomalyStatusType] = None
    AnomalyTimeRange: Optional[AnomalyTimeRange] = None
    AnomalyReportedTimeRange: Optional[AnomalyReportedTimeRange] = None
    SourceDetails: Optional[AnomalySourceDetails] = None
    AssociatedInsightId: Optional[str] = None
    ResourceCollection: Optional[ResourceCollectionOutput] = None
    Type: Optional[AnomalyTypeType] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CausalAnomalyId: Optional[str] = None
    AnomalyResources: Optional[List[AnomalyResource]] = None


class ListAnomaliesForInsightResponse(BaseValidatorModel):
    ProactiveAnomalies: List[ProactiveAnomalySummary]
    ReactiveAnomalies: List[ReactiveAnomalySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeAnomalyResponse(BaseValidatorModel):
    ProactiveAnomaly: ProactiveAnomaly
    ReactiveAnomaly: ReactiveAnomaly
    ResponseMetadata: ResponseMetadata