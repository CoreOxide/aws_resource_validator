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
from aws_resource_validator.pydantic_models.devops_guru_constants import *

class AccountInsightHealthTypeDef(BaseValidatorModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AmazonCodeGuruProfilerIntegrationTypeDef(BaseValidatorModel):
    Status: Optional[EventSourceOptInStatusType] = None

class AnomalyReportedTimeRangeTypeDef(BaseValidatorModel):
    OpenTime: datetime
    CloseTime: Optional[datetime] = None

class AnomalyResourceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None

class AnomalySourceMetadataTypeDef(BaseValidatorModel):
    Source: Optional[str] = None
    SourceResourceName: Optional[str] = None
    SourceResourceType: Optional[str] = None

class AnomalyTimeRangeTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None

class CloudFormationCollectionFilterTypeDef(BaseValidatorModel):
    StackNames: Optional[List[str]] = None

class CloudFormationCollectionTypeDef(BaseValidatorModel):
    StackNames: Optional[List[str]] = None

class CloudFormationCostEstimationResourceCollectionFilterTypeDef(BaseValidatorModel):
    StackNames: Optional[List[str]] = None

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

class TagCostEstimationResourceCollectionFilterTypeDef(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]

class CostEstimationTimeRangeTypeDef(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class DeleteInsightRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DescribeAnomalyRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    AccountId: Optional[str] = None

class DescribeFeedbackRequestRequestTypeDef(BaseValidatorModel):
    InsightId: Optional[str] = None

class InsightFeedbackTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Feedback: Optional[InsightFeedbackOptionType] = None

class DescribeInsightRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    AccountId: Optional[str] = None

class DescribeOrganizationHealthRequestRequestTypeDef(BaseValidatorModel):
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef(BaseValidatorModel):
    OrganizationResourceCollectionType: OrganizationResourceCollectionTypeType
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeResourceCollectionHealthRequestRequestTypeDef(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    NextToken: Optional[str] = None

class EventResourceTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None

class GetCostEstimationRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class ServiceResourceCostTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    State: Optional[CostEstimationServiceResourceStateType] = None
    Count: Optional[int] = None
    UnitCost: Optional[float] = None
    Cost: Optional[float] = None

class GetResourceCollectionRequestRequestTypeDef(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    NextToken: Optional[str] = None

class InsightTimeRangeTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None

class KMSServerSideEncryptionIntegrationConfigTypeDef(BaseValidatorModel):
    KMSKeyId: Optional[str] = None
    OptInStatus: Optional[OptInStatusType] = None
    Type: Optional[ServerSideEncryptionTypeType] = None

class KMSServerSideEncryptionIntegrationTypeDef(BaseValidatorModel):
    KMSKeyId: Optional[str] = None
    OptInStatus: Optional[OptInStatusType] = None
    Type: Optional[ServerSideEncryptionTypeType] = None

class ServiceCollectionTypeDef(BaseValidatorModel):
    ServiceNames: Optional[Sequence[ServiceNameType]] = None

class ListAnomalousLogGroupsRequestRequestTypeDef(BaseValidatorModel):
    InsightId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInsightsOngoingStatusFilterTypeDef(BaseValidatorModel):
    Type: InsightTypeType

class ListMonitoredResourcesFiltersTypeDef(BaseValidatorModel):
    ResourcePermission: ResourcePermissionType
    ResourceTypeFilters: Sequence[ResourceTypeFilterType]

class ListNotificationChannelsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class ListRecommendationsRequestRequestTypeDef(BaseValidatorModel):
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

class NotificationFilterConfigPaginatorTypeDef(BaseValidatorModel):
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

class PerformanceInsightsStatTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Value: Optional[float] = None

class PerformanceInsightsReferenceScalarTypeDef(BaseValidatorModel):
    Value: Optional[float] = None

class PredictionTimeRangeTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: Optional[datetime] = None

class RecommendationRelatedAnomalyResourceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None

class RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None

class RecommendationRelatedEventResourceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None

class RemoveNotificationChannelRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class TagCollectionFilterTypeDef(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]

class TagCollectionTypeDef(BaseValidatorModel):
    AppBoundaryKey: str
    TagValues: List[str]

class ServiceInsightHealthTypeDef(BaseValidatorModel):
    OpenProactiveInsights: Optional[int] = None
    OpenReactiveInsights: Optional[int] = None

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

class CostEstimationResourceCollectionFilterTypeDef(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCostEstimationResourceCollectionFilterTypeDef] = None
    Tags: Optional[List[TagCostEstimationResourceCollectionFilterTypeDef]] = None

class DescribeAccountOverviewRequestRequestTypeDef(BaseValidatorModel):
    FromTime: TimestampTypeDef
    ToTime: Optional[TimestampTypeDef] = None

class DescribeOrganizationOverviewRequestRequestTypeDef(BaseValidatorModel):
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

class PutFeedbackRequestRequestTypeDef(BaseValidatorModel):
    InsightFeedback: Optional[InsightFeedbackTypeDef] = None

class DescribeOrganizationResourceCollectionHealthRequestDescribeOrganizationResourceCollectionHealthPaginateTypeDef(BaseValidatorModel):
    OrganizationResourceCollectionType: OrganizationResourceCollectionTypeType
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeResourceCollectionHealthRequestDescribeResourceCollectionHealthPaginateTypeDef(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCostEstimationRequestGetCostEstimationPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceCollectionRequestGetResourceCollectionPaginateTypeDef(BaseValidatorModel):
    ResourceCollectionType: ResourceCollectionTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnomalousLogGroupsRequestListAnomalousLogGroupsPaginateTypeDef(BaseValidatorModel):
    InsightId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotificationChannelsRequestListNotificationChannelsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationsRequestListRecommendationsPaginateTypeDef(BaseValidatorModel):
    InsightId: str
    Locale: Optional[LocaleType] = None
    AccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnomaliesForInsightFiltersTypeDef(BaseValidatorModel):
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None

class ListMonitoredResourcesRequestListMonitoredResourcesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[ListMonitoredResourcesFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMonitoredResourcesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[ListMonitoredResourcesFiltersTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LogAnomalyShowcaseTypeDef(BaseValidatorModel):
    LogAnomalyClasses: Optional[List[LogAnomalyClassTypeDef]] = None

class NotificationChannelConfigPaginatorTypeDef(BaseValidatorModel):
    Sns: SnsChannelConfigTypeDef
    Filters: Optional[NotificationFilterConfigPaginatorTypeDef] = None

class NotificationChannelConfigTypeDef(BaseValidatorModel):
    Sns: SnsChannelConfigTypeDef
    Filters: Optional[NotificationFilterConfigTypeDef] = None

class UpdateServiceIntegrationConfigTypeDef(BaseValidatorModel):
    OpsCenter: Optional[OpsCenterIntegrationConfigTypeDef] = None
    LogsAnomalyDetection: Optional[LogsAnomalyDetectionIntegrationConfigTypeDef] = None
    KMSServerSideEncryption: Optional[KMSServerSideEncryptionIntegrationConfigTypeDef] = None

class ServiceIntegrationConfigTypeDef(BaseValidatorModel):
    OpsCenter: Optional[OpsCenterIntegrationTypeDef] = None
    LogsAnomalyDetection: Optional[LogsAnomalyDetectionIntegrationTypeDef] = None
    KMSServerSideEncryption: Optional[KMSServerSideEncryptionIntegrationTypeDef] = None

class PerformanceInsightsMetricQueryTypeDef(BaseValidatorModel):
    Metric: Optional[str] = None
    GroupBy: Optional[PerformanceInsightsMetricDimensionGroupTypeDef] = None
    Filter: Optional[Dict[str, str]] = None

class RecommendationRelatedAnomalySourceDetailTypeDef(BaseValidatorModel):
    CloudWatchMetrics: Optional[       List[RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef]     ] = None

class RecommendationRelatedEventTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Resources: Optional[List[RecommendationRelatedEventResourceTypeDef]] = None

class ResourceCollectionFilterTypeDef(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCollectionFilterTypeDef] = None
    Tags: Optional[List[TagCollectionFilterTypeDef]] = None

class ResourceCollectionTypeDef(BaseValidatorModel):
    CloudFormation: Optional[CloudFormationCollectionTypeDef] = None
    Tags: Optional[List[TagCollectionTypeDef]] = None

class ServiceHealthTypeDef(BaseValidatorModel):
    ServiceName: Optional[ServiceNameType] = None
    Insight: Optional[ServiceInsightHealthTypeDef] = None
    AnalyzedResourceCount: Optional[int] = None

class UpdateResourceCollectionFilterTypeDef(BaseValidatorModel):
    CloudFormation: Optional[UpdateCloudFormationCollectionFilterTypeDef] = None
    Tags: Optional[Sequence[UpdateTagCollectionFilterTypeDef]] = None

class DescribeEventSourcesConfigResponseTypeDef(BaseValidatorModel):
    EventSources: EventSourcesConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventSourcesConfigRequestRequestTypeDef(BaseValidatorModel):
    EventSources: Optional[EventSourcesConfigTypeDef] = None

class CloudWatchMetricsDetailTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[CloudWatchMetricsDimensionTypeDef]] = None
    Stat: Optional[CloudWatchMetricsStatType] = None
    Unit: Optional[str] = None
    Period: Optional[int] = None
    MetricDataSummary: Optional[CloudWatchMetricsDataSummaryTypeDef] = None

class GetCostEstimationResponseTypeDef(BaseValidatorModel):
    ResourceCollection: CostEstimationResourceCollectionFilterTypeDef
    Status: CostEstimationStatusType
    Costs: List[ServiceResourceCostTypeDef]
    TimeRange: CostEstimationTimeRangeTypeDef
    TotalCost: float
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCostEstimationRequestRequestTypeDef(BaseValidatorModel):
    ResourceCollection: CostEstimationResourceCollectionFilterTypeDef
    ClientToken: Optional[str] = None

class ListInsightsClosedStatusFilterTypeDef(BaseValidatorModel):
    Type: InsightTypeType
    EndTimeRange: EndTimeRangeTypeDef

class ListInsightsAnyStatusFilterTypeDef(BaseValidatorModel):
    Type: InsightTypeType
    StartTimeRange: StartTimeRangeTypeDef

class ListAnomaliesForInsightRequestListAnomaliesForInsightPaginateTypeDef(BaseValidatorModel):
    InsightId: str
    StartTimeRange: Optional[StartTimeRangeTypeDef] = None
    AccountId: Optional[str] = None
    Filters: Optional[ListAnomaliesForInsightFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAnomaliesForInsightRequestRequestTypeDef(BaseValidatorModel):
    InsightId: str
    StartTimeRange: Optional[StartTimeRangeTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None
    Filters: Optional[ListAnomaliesForInsightFiltersTypeDef] = None

class AnomalousLogGroupTypeDef(BaseValidatorModel):
    LogGroupName: Optional[str] = None
    ImpactStartTime: Optional[datetime] = None
    ImpactEndTime: Optional[datetime] = None
    NumberOfLogLinesScanned: Optional[int] = None
    LogAnomalyShowcases: Optional[List[LogAnomalyShowcaseTypeDef]] = None

class NotificationChannelPaginatorTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Config: Optional[NotificationChannelConfigPaginatorTypeDef] = None

class AddNotificationChannelRequestRequestTypeDef(BaseValidatorModel):
    Config: NotificationChannelConfigTypeDef

class NotificationChannelTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Config: Optional[NotificationChannelConfigTypeDef] = None

class UpdateServiceIntegrationRequestRequestTypeDef(BaseValidatorModel):
    ServiceIntegration: UpdateServiceIntegrationConfigTypeDef

class DescribeServiceIntegrationResponseTypeDef(BaseValidatorModel):
    ServiceIntegration: ServiceIntegrationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PerformanceInsightsReferenceMetricTypeDef(BaseValidatorModel):
    MetricQuery: Optional[PerformanceInsightsMetricQueryTypeDef] = None

class RecommendationRelatedAnomalyTypeDef(BaseValidatorModel):
    Resources: Optional[List[RecommendationRelatedAnomalyResourceTypeDef]] = None
    SourceDetails: Optional[List[RecommendationRelatedAnomalySourceDetailTypeDef]] = None
    AnomalyId: Optional[str] = None

class GetResourceCollectionResponseTypeDef(BaseValidatorModel):
    ResourceCollection: ResourceCollectionFilterTypeDef
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventTypeDef(BaseValidatorModel):
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    Id: Optional[str] = None
    Time: Optional[datetime] = None
    EventSource: Optional[str] = None
    Name: Optional[str] = None
    DataSource: Optional[EventDataSourceType] = None
    EventClass: Optional[EventClassType] = None
    Resources: Optional[List[EventResourceTypeDef]] = None

class ListEventsFiltersTypeDef(BaseValidatorModel):
    InsightId: Optional[str] = None
    EventTimeRange: Optional[EventTimeRangeTypeDef] = None
    EventClass: Optional[EventClassType] = None
    EventSource: Optional[str] = None
    DataSource: Optional[EventDataSourceType] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None

class MonitoredResourceIdentifierTypeDef(BaseValidatorModel):
    MonitoredResourceName: Optional[str] = None
    Type: Optional[str] = None
    ResourcePermission: Optional[ResourcePermissionType] = None
    LastUpdated: Optional[datetime] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None

class ProactiveInsightSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None
    AssociatedResourceArns: Optional[List[str]] = None

class ProactiveInsightTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    PredictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
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
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None

class ReactiveInsightSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None
    AssociatedResourceArns: Optional[List[str]] = None

class ReactiveInsightTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Severity: Optional[InsightSeverityType] = None
    Status: Optional[InsightStatusType] = None
    InsightTimeRange: Optional[InsightTimeRangeTypeDef] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
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
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None

class SearchInsightsFiltersTypeDef(BaseValidatorModel):
    Severities: Optional[Sequence[InsightSeverityType]] = None
    Statuses: Optional[Sequence[InsightStatusType]] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None

class SearchOrganizationInsightsFiltersTypeDef(BaseValidatorModel):
    Severities: Optional[Sequence[InsightSeverityType]] = None
    Statuses: Optional[Sequence[InsightStatusType]] = None
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    ServiceCollection: Optional[ServiceCollectionTypeDef] = None

class DescribeOrganizationResourceCollectionHealthResponseTypeDef(BaseValidatorModel):
    CloudFormation: List[CloudFormationHealthTypeDef]
    Service: List[ServiceHealthTypeDef]
    Account: List[AccountHealthTypeDef]
    NextToken: str
    Tags: List[TagHealthTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourceCollectionHealthResponseTypeDef(BaseValidatorModel):
    CloudFormation: List[CloudFormationHealthTypeDef]
    Service: List[ServiceHealthTypeDef]
    NextToken: str
    Tags: List[TagHealthTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResourceCollectionRequestRequestTypeDef(BaseValidatorModel):
    Action: UpdateResourceCollectionActionType
    ResourceCollection: UpdateResourceCollectionFilterTypeDef

class ListInsightsStatusFilterTypeDef(BaseValidatorModel):
    Ongoing: Optional[ListInsightsOngoingStatusFilterTypeDef] = None
    Closed: Optional[ListInsightsClosedStatusFilterTypeDef] = None
    Any: Optional[ListInsightsAnyStatusFilterTypeDef] = None

class ListAnomalousLogGroupsResponseTypeDef(BaseValidatorModel):
    InsightId: str
    AnomalousLogGroups: List[AnomalousLogGroupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotificationChannelsResponsePaginatorTypeDef(BaseValidatorModel):
    Channels: List[NotificationChannelPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotificationChannelsResponseTypeDef(BaseValidatorModel):
    Channels: List[NotificationChannelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventsRequestListEventsPaginateTypeDef(BaseValidatorModel):
    Filters: ListEventsFiltersTypeDef
    AccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventsRequestRequestTypeDef(BaseValidatorModel):
    Filters: ListEventsFiltersTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None

class ListMonitoredResourcesResponseTypeDef(BaseValidatorModel):
    MonitoredResourceIdentifiers: List[MonitoredResourceIdentifierTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInsightsResponseTypeDef(BaseValidatorModel):
    ProactiveInsights: List[ProactiveInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveInsightSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchInsightsResponseTypeDef(BaseValidatorModel):
    ProactiveInsights: List[ProactiveInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveInsightSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchOrganizationInsightsResponseTypeDef(BaseValidatorModel):
    ProactiveInsights: List[ProactiveInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveInsightSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInsightResponseTypeDef(BaseValidatorModel):
    ProactiveInsight: ProactiveInsightTypeDef
    ReactiveInsight: ReactiveInsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationInsightsResponseTypeDef(BaseValidatorModel):
    ProactiveInsights: List[ProactiveOrganizationInsightSummaryTypeDef]
    ReactiveInsights: List[ReactiveOrganizationInsightSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchInsightsRequestRequestTypeDef(BaseValidatorModel):
    StartTimeRange: StartTimeRangeTypeDef
    Type: InsightTypeType
    Filters: Optional[SearchInsightsFiltersTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SearchInsightsRequestSearchInsightsPaginateTypeDef(BaseValidatorModel):
    StartTimeRange: StartTimeRangeTypeDef
    Type: InsightTypeType
    Filters: Optional[SearchInsightsFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchOrganizationInsightsRequestRequestTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]
    StartTimeRange: StartTimeRangeTypeDef
    Type: InsightTypeType
    Filters: Optional[SearchOrganizationInsightsFiltersTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SearchOrganizationInsightsRequestSearchOrganizationInsightsPaginateTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]
    StartTimeRange: StartTimeRangeTypeDef
    Type: InsightTypeType
    Filters: Optional[SearchOrganizationInsightsFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInsightsRequestListInsightsPaginateTypeDef(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInsightsRequestRequestTypeDef(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOrganizationInsightsRequestListOrganizationInsightsPaginateTypeDef(BaseValidatorModel):
    StatusFilter: ListInsightsStatusFilterTypeDef
    AccountIds: Optional[Sequence[str]] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationInsightsRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PerformanceInsightsMetricsDetailTypeDef(BaseValidatorModel):
    MetricDisplayName: Optional[str] = None
    Unit: Optional[str] = None
    MetricQuery: Optional[PerformanceInsightsMetricQueryTypeDef] = None
    ReferenceData: Optional[List[PerformanceInsightsReferenceDataTypeDef]] = None
    StatsAtAnomaly: Optional[List[PerformanceInsightsStatTypeDef]] = None
    StatsAtBaseline: Optional[List[PerformanceInsightsStatTypeDef]] = None

class AnomalySourceDetailsTypeDef(BaseValidatorModel):
    CloudWatchMetrics: Optional[List[CloudWatchMetricsDetailTypeDef]] = None
    PerformanceInsightsMetrics: Optional[List[PerformanceInsightsMetricsDetailTypeDef]] = None

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
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
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
    ResourceCollection: Optional[ResourceCollectionTypeDef] = None
    Limit: Optional[float] = None
    SourceMetadata: Optional[AnomalySourceMetadataTypeDef] = None
    AnomalyResources: Optional[List[AnomalyResourceTypeDef]] = None
    Description: Optional[str] = None

class ReactiveAnomalySummaryTypeDef(BaseValidatorModel):
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

class ReactiveAnomalyTypeDef(BaseValidatorModel):
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

class ListAnomaliesForInsightResponseTypeDef(BaseValidatorModel):
    ProactiveAnomalies: List[ProactiveAnomalySummaryTypeDef]
    ReactiveAnomalies: List[ReactiveAnomalySummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAnomalyResponseTypeDef(BaseValidatorModel):
    ProactiveAnomaly: ProactiveAnomalyTypeDef
    ReactiveAnomaly: ReactiveAnomalyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

