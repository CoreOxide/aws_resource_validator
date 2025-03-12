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
from aws_resource_validator.pydantic_models.xray_constants import *

class AnnotationValueTypeDef(BaseValidatorModel):
    NumberValue: Optional[float] = None
    BooleanValue: Optional[bool] = None
    StringValue: Optional[str] = None


class AvailabilityZoneDetailTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class BackendConnectionErrorsTypeDef(BaseValidatorModel):
    TimeoutCount: Optional[int] = None
    ConnectionRefusedCount: Optional[int] = None
    HTTPCode4XXCount: Optional[int] = None
    HTTPCode5XXCount: Optional[int] = None
    UnknownHostCount: Optional[int] = None
    OtherCount: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class BatchGetTracesRequestTypeDef(BaseValidatorModel):
    TraceIds: Sequence[str]
    NextToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelTraceRetrievalRequestTypeDef(BaseValidatorModel):
    RetrievalToken: str


class InsightsConfigurationTypeDef(BaseValidatorModel):
    InsightsEnabled: Optional[bool] = None
    NotificationsEnabled: Optional[bool] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class DeleteGroupRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyRevisionId: Optional[str] = None


class DeleteSamplingRuleRequestTypeDef(BaseValidatorModel):
    RuleName: Optional[str] = None
    RuleARN: Optional[str] = None


class ErrorStatisticsTypeDef(BaseValidatorModel):
    ThrottleCount: Optional[int] = None
    OtherCount: Optional[int] = None
    TotalCount: Optional[int] = None


class FaultStatisticsTypeDef(BaseValidatorModel):
    OtherCount: Optional[int] = None
    TotalCount: Optional[int] = None


class HistogramEntryTypeDef(BaseValidatorModel):
    Value: Optional[float] = None
    Count: Optional[int] = None


class RootCauseExceptionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Message: Optional[str] = None


class ForecastStatisticsTypeDef(BaseValidatorModel):
    FaultCountHigh: Optional[int] = None
    FaultCountLow: Optional[int] = None


class GetGroupRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None


class GetGroupsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class GetIndexingRulesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class GetInsightEventsRequestTypeDef(BaseValidatorModel):
    InsightId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetInsightRequestTypeDef(BaseValidatorModel):
    InsightId: str


class GetRetrievedTracesGraphRequestTypeDef(BaseValidatorModel):
    RetrievalToken: str
    NextToken: Optional[str] = None


class GetSamplingRulesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class GetSamplingStatisticSummariesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class SamplingStatisticSummaryTypeDef(BaseValidatorModel):
    RuleName: Optional[str] = None
    Timestamp: Optional[datetime] = None
    RequestCount: Optional[int] = None
    BorrowCount: Optional[int] = None
    SampledCount: Optional[int] = None


class SamplingTargetDocumentTypeDef(BaseValidatorModel):
    RuleName: Optional[str] = None
    FixedRate: Optional[float] = None
    ReservoirQuota: Optional[int] = None
    ReservoirQuotaTTL: Optional[datetime] = None
    Interval: Optional[int] = None


class UnprocessedStatisticsTypeDef(BaseValidatorModel):
    RuleName: Optional[str] = None
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class GetTraceGraphRequestTypeDef(BaseValidatorModel):
    TraceIds: Sequence[str]
    NextToken: Optional[str] = None


class SamplingStrategyTypeDef(BaseValidatorModel):
    Name: Optional[SamplingStrategyNameType] = None
    Value: Optional[float] = None


class GraphLinkTypeDef(BaseValidatorModel):
    ReferenceType: Optional[str] = None
    SourceTraceId: Optional[str] = None
    DestinationTraceIds: Optional[List[str]] = None


class HttpTypeDef(BaseValidatorModel):
    HttpURL: Optional[str] = None
    HttpStatus: Optional[int] = None
    HttpMethod: Optional[str] = None
    UserAgent: Optional[str] = None
    ClientIp: Optional[str] = None


class ProbabilisticRuleValueTypeDef(BaseValidatorModel):
    DesiredSamplingPercentage: float
    ActualSamplingPercentage: Optional[float] = None


class ProbabilisticRuleValueUpdateTypeDef(BaseValidatorModel):
    DesiredSamplingPercentage: float


class RequestImpactStatisticsTypeDef(BaseValidatorModel):
    FaultCount: Optional[int] = None
    OkCount: Optional[int] = None
    TotalCount: Optional[int] = None


class InsightImpactGraphEdgeTypeDef(BaseValidatorModel):
    ReferenceId: Optional[int] = None


class InstanceIdDetailTypeDef(BaseValidatorModel):
    Id: Optional[str] = None


class ListResourcePoliciesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class ResourcePolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyDocument: Optional[str] = None
    PolicyRevisionId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None


class ListRetrievedTracesRequestTypeDef(BaseValidatorModel):
    RetrievalToken: str
    TraceFormat: Optional[TraceFormatTypeType] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    PolicyRevisionId: Optional[str] = None
    BypassPolicyLockoutCheck: Optional[bool] = None


class PutTraceSegmentsRequestTypeDef(BaseValidatorModel):
    TraceSegmentDocuments: Sequence[str]


class UnprocessedTraceSegmentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class ResourceARNDetailTypeDef(BaseValidatorModel):
    ARN: Optional[str] = None


class ResponseTimeRootCauseEntityTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Coverage: Optional[float] = None
    Remote: Optional[bool] = None


class SpanTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Document: Optional[str] = None


class SegmentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Document: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateTraceSegmentDestinationRequestTypeDef(BaseValidatorModel):
    Destination: Optional[TraceSegmentDestinationType] = None


class ServiceIdTypeDef(BaseValidatorModel):
    pass


class AnomalousServiceTypeDef(BaseValidatorModel):
    ServiceId: Optional[ServiceIdTypeDef] = None


class TraceUserTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    ServiceIds: Optional[List[ServiceIdTypeDef]] = None


class ValueWithServiceIdsTypeDef(BaseValidatorModel):
    AnnotationValue: Optional[AnnotationValueTypeDef] = None
    ServiceIds: Optional[List[ServiceIdTypeDef]] = None


class BatchGetTracesRequestPaginateTypeDef(BaseValidatorModel):
    TraceIds: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetSamplingRulesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetSamplingStatisticSummariesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetTraceGraphRequestPaginateTypeDef(BaseValidatorModel):
    TraceIds: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourcePoliciesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetTraceSegmentDestinationResultTypeDef(BaseValidatorModel):
    Destination: TraceSegmentDestinationType
    Status: TraceSegmentDestinationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class StartTraceRetrievalResultTypeDef(BaseValidatorModel):
    RetrievalToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTraceSegmentDestinationResultTypeDef(BaseValidatorModel):
    Destination: TraceSegmentDestinationType
    Status: TraceSegmentDestinationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GroupSummaryTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfigurationTypeDef] = None


class GroupTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfigurationTypeDef] = None


class UpdateGroupRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfigurationTypeDef] = None


class CreateGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class EdgeStatisticsTypeDef(BaseValidatorModel):
    OkCount: Optional[int] = None
    ErrorStatistics: Optional[ErrorStatisticsTypeDef] = None
    FaultStatistics: Optional[FaultStatisticsTypeDef] = None
    TotalCount: Optional[int] = None
    TotalResponseTime: Optional[float] = None


class ServiceStatisticsTypeDef(BaseValidatorModel):
    OkCount: Optional[int] = None
    ErrorStatistics: Optional[ErrorStatisticsTypeDef] = None
    FaultStatistics: Optional[FaultStatisticsTypeDef] = None
    TotalCount: Optional[int] = None
    TotalResponseTime: Optional[float] = None


class EncryptionConfigTypeDef(BaseValidatorModel):
    pass


class GetEncryptionConfigResultTypeDef(BaseValidatorModel):
    EncryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutEncryptionConfigResultTypeDef(BaseValidatorModel):
    EncryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ErrorRootCauseEntityTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Exceptions: Optional[List[RootCauseExceptionTypeDef]] = None
    Remote: Optional[bool] = None


class FaultRootCauseEntityTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Exceptions: Optional[List[RootCauseExceptionTypeDef]] = None
    Remote: Optional[bool] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetInsightImpactGraphRequestTypeDef(BaseValidatorModel):
    InsightId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: Optional[str] = None


class GetInsightSummariesRequestTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    States: Optional[Sequence[InsightStateType]] = None
    GroupARN: Optional[str] = None
    GroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetServiceGraphRequestPaginateTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetServiceGraphRequestTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    NextToken: Optional[str] = None


class GetTimeSeriesServiceStatisticsRequestPaginateTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    EntitySelectorExpression: Optional[str] = None
    Period: Optional[int] = None
    ForecastStatistics: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetTimeSeriesServiceStatisticsRequestTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    EntitySelectorExpression: Optional[str] = None
    Period: Optional[int] = None
    ForecastStatistics: Optional[bool] = None
    NextToken: Optional[str] = None


class SamplingStatisticsDocumentTypeDef(BaseValidatorModel):
    RuleName: str
    ClientID: str
    Timestamp: TimestampTypeDef
    RequestCount: int
    SampledCount: int
    BorrowCount: Optional[int] = None


class StartTraceRetrievalRequestTypeDef(BaseValidatorModel):
    TraceIds: Sequence[str]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef


class TelemetryRecordTypeDef(BaseValidatorModel):
    Timestamp: TimestampTypeDef
    SegmentsReceivedCount: Optional[int] = None
    SegmentsSentCount: Optional[int] = None
    SegmentsSpilloverCount: Optional[int] = None
    SegmentsRejectedCount: Optional[int] = None
    BackendConnectionErrors: Optional[BackendConnectionErrorsTypeDef] = None


class GetSamplingStatisticSummariesResultTypeDef(BaseValidatorModel):
    SamplingStatisticSummaries: List[SamplingStatisticSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetSamplingTargetsResultTypeDef(BaseValidatorModel):
    SamplingTargetDocuments: List[SamplingTargetDocumentTypeDef]
    LastRuleModification: datetime
    UnprocessedStatistics: List[UnprocessedStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetTraceSummariesRequestPaginateTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    TimeRangeType: Optional[TimeRangeTypeType] = None
    Sampling: Optional[bool] = None
    SamplingStrategy: Optional[SamplingStrategyTypeDef] = None
    FilterExpression: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetTraceSummariesRequestTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    TimeRangeType: Optional[TimeRangeTypeType] = None
    Sampling: Optional[bool] = None
    SamplingStrategy: Optional[SamplingStrategyTypeDef] = None
    FilterExpression: Optional[str] = None
    NextToken: Optional[str] = None


class IndexingRuleValueTypeDef(BaseValidatorModel):
    Probabilistic: Optional[ProbabilisticRuleValueTypeDef] = None


class IndexingRuleValueUpdateTypeDef(BaseValidatorModel):
    Probabilistic: Optional[ProbabilisticRuleValueUpdateTypeDef] = None


class ListResourcePoliciesResultTypeDef(BaseValidatorModel):
    ResourcePolicies: List[ResourcePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutResourcePolicyResultTypeDef(BaseValidatorModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutTraceSegmentsResultTypeDef(BaseValidatorModel):
    UnprocessedTraceSegments: List[UnprocessedTraceSegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RetrievedTraceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Duration: Optional[float] = None
    Spans: Optional[List[SpanTypeDef]] = None


class SamplingRuleOutputTypeDef(BaseValidatorModel):
    pass


class SamplingRuleRecordTypeDef(BaseValidatorModel):
    SamplingRule: Optional[SamplingRuleOutputTypeDef] = None
    CreatedAt: Optional[datetime] = None
    ModifiedAt: Optional[datetime] = None


class SamplingRuleUpdateTypeDef(BaseValidatorModel):
    pass


class UpdateSamplingRuleRequestTypeDef(BaseValidatorModel):
    SamplingRuleUpdate: SamplingRuleUpdateTypeDef


class TraceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Duration: Optional[float] = None
    LimitExceeded: Optional[bool] = None
    Segments: Optional[List[SegmentTypeDef]] = None


class InsightEventTypeDef(BaseValidatorModel):
    Summary: Optional[str] = None
    EventTime: Optional[datetime] = None
    ClientRequestImpactStatistics: Optional[RequestImpactStatisticsTypeDef] = None
    RootCauseServiceRequestImpactStatistics: Optional[RequestImpactStatisticsTypeDef] = None
    TopAnomalousServices: Optional[List[AnomalousServiceTypeDef]] = None


class InsightSummaryTypeDef(BaseValidatorModel):
    InsightId: Optional[str] = None
    GroupARN: Optional[str] = None
    GroupName: Optional[str] = None
    RootCauseServiceId: Optional[ServiceIdTypeDef] = None
    Categories: Optional[List[Literal["FAULT"]]] = None
    State: Optional[InsightStateType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Summary: Optional[str] = None
    ClientRequestImpactStatistics: Optional[RequestImpactStatisticsTypeDef] = None
    RootCauseServiceRequestImpactStatistics: Optional[RequestImpactStatisticsTypeDef] = None
    TopAnomalousServices: Optional[List[AnomalousServiceTypeDef]] = None
    LastUpdateTime: Optional[datetime] = None


class InsightTypeDef(BaseValidatorModel):
    InsightId: Optional[str] = None
    GroupARN: Optional[str] = None
    GroupName: Optional[str] = None
    RootCauseServiceId: Optional[ServiceIdTypeDef] = None
    Categories: Optional[List[Literal["FAULT"]]] = None
    State: Optional[InsightStateType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Summary: Optional[str] = None
    ClientRequestImpactStatistics: Optional[RequestImpactStatisticsTypeDef] = None
    RootCauseServiceRequestImpactStatistics: Optional[RequestImpactStatisticsTypeDef] = None
    TopAnomalousServices: Optional[List[AnomalousServiceTypeDef]] = None


class GetGroupsResultTypeDef(BaseValidatorModel):
    Groups: List[GroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateGroupResultTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetGroupResultTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGroupResultTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AliasTypeDef(BaseValidatorModel):
    pass


class EdgeTypeDef(BaseValidatorModel):
    ReferenceId: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    SummaryStatistics: Optional[EdgeStatisticsTypeDef] = None
    ResponseTimeHistogram: Optional[List[HistogramEntryTypeDef]] = None
    Aliases: Optional[List[AliasTypeDef]] = None
    EdgeType: Optional[str] = None
    ReceivedEventAgeHistogram: Optional[List[HistogramEntryTypeDef]] = None


class TimeSeriesServiceStatisticsTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    EdgeSummaryStatistics: Optional[EdgeStatisticsTypeDef] = None
    ServiceSummaryStatistics: Optional[ServiceStatisticsTypeDef] = None
    ServiceForecastStatistics: Optional[ForecastStatisticsTypeDef] = None
    ResponseTimeHistogram: Optional[List[HistogramEntryTypeDef]] = None


class GetSamplingTargetsRequestTypeDef(BaseValidatorModel):
    SamplingStatisticsDocuments: Sequence[SamplingStatisticsDocumentTypeDef]


class PutTelemetryRecordsRequestTypeDef(BaseValidatorModel):
    TelemetryRecords: Sequence[TelemetryRecordTypeDef]
    EC2InstanceId: Optional[str] = None
    Hostname: Optional[str] = None
    ResourceARN: Optional[str] = None


class IndexingRuleTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ModifiedAt: Optional[datetime] = None
    Rule: Optional[IndexingRuleValueTypeDef] = None


class UpdateIndexingRuleRequestTypeDef(BaseValidatorModel):
    Name: str
    Rule: IndexingRuleValueUpdateTypeDef


class InsightImpactGraphServiceTypeDef(BaseValidatorModel):
    pass


class GetInsightImpactGraphResultTypeDef(BaseValidatorModel):
    InsightId: str
    StartTime: datetime
    EndTime: datetime
    ServiceGraphStartTime: datetime
    ServiceGraphEndTime: datetime
    Services: List[InsightImpactGraphServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResponseTimeRootCauseServiceTypeDef(BaseValidatorModel):
    pass


class ResponseTimeRootCauseTypeDef(BaseValidatorModel):
    Services: Optional[List[ResponseTimeRootCauseServiceTypeDef]] = None
    ClientImpacting: Optional[bool] = None


class ListRetrievedTracesResultTypeDef(BaseValidatorModel):
    RetrievalStatus: RetrievalStatusType
    TraceFormat: TraceFormatTypeType
    Traces: List[RetrievedTraceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateSamplingRuleResultTypeDef(BaseValidatorModel):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSamplingRuleResultTypeDef(BaseValidatorModel):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSamplingRulesResultTypeDef(BaseValidatorModel):
    SamplingRuleRecords: List[SamplingRuleRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateSamplingRuleResultTypeDef(BaseValidatorModel):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SamplingRuleUnionTypeDef(BaseValidatorModel):
    pass


class CreateSamplingRuleRequestTypeDef(BaseValidatorModel):
    SamplingRule: SamplingRuleUnionTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None


class BatchGetTracesResultTypeDef(BaseValidatorModel):
    Traces: List[TraceTypeDef]
    UnprocessedTraceIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetInsightEventsResultTypeDef(BaseValidatorModel):
    InsightEvents: List[InsightEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetInsightSummariesResultTypeDef(BaseValidatorModel):
    InsightSummaries: List[InsightSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetInsightResultTypeDef(BaseValidatorModel):
    Insight: InsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTimeSeriesServiceStatisticsResultTypeDef(BaseValidatorModel):
    TimeSeriesServiceStatistics: List[TimeSeriesServiceStatisticsTypeDef]
    ContainsOldGroupVersions: bool
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ErrorRootCauseServiceTypeDef(BaseValidatorModel):
    pass


class ErrorRootCauseTypeDef(BaseValidatorModel):
    Services: Optional[List[ErrorRootCauseServiceTypeDef]] = None
    ClientImpacting: Optional[bool] = None


class FaultRootCauseServiceTypeDef(BaseValidatorModel):
    pass


class FaultRootCauseTypeDef(BaseValidatorModel):
    Services: Optional[List[FaultRootCauseServiceTypeDef]] = None
    ClientImpacting: Optional[bool] = None


class GetIndexingRulesResultTypeDef(BaseValidatorModel):
    IndexingRules: List[IndexingRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateIndexingRuleResultTypeDef(BaseValidatorModel):
    IndexingRule: IndexingRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ServiceTypeDef(BaseValidatorModel):
    pass


class GetServiceGraphResultTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    Services: List[ServiceTypeDef]
    ContainsOldGroupVersions: bool
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetTraceGraphResultTypeDef(BaseValidatorModel):
    Services: List[ServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RetrievedServiceTypeDef(BaseValidatorModel):
    Service: Optional[ServiceTypeDef] = None
    Links: Optional[List[GraphLinkTypeDef]] = None


class TraceSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[float] = None
    ResponseTime: Optional[float] = None
    HasFault: Optional[bool] = None
    HasError: Optional[bool] = None
    HasThrottle: Optional[bool] = None
    IsPartial: Optional[bool] = None
    Http: Optional[HttpTypeDef] = None
    Annotations: Optional[Dict[str, List[ValueWithServiceIdsTypeDef]]] = None
    Users: Optional[List[TraceUserTypeDef]] = None
    ServiceIds: Optional[List[ServiceIdTypeDef]] = None
    ResourceARNs: Optional[List[ResourceARNDetailTypeDef]] = None
    InstanceIds: Optional[List[InstanceIdDetailTypeDef]] = None
    AvailabilityZones: Optional[List[AvailabilityZoneDetailTypeDef]] = None
    EntryPoint: Optional[ServiceIdTypeDef] = None
    FaultRootCauses: Optional[List[FaultRootCauseTypeDef]] = None
    ErrorRootCauses: Optional[List[ErrorRootCauseTypeDef]] = None
    ResponseTimeRootCauses: Optional[List[ResponseTimeRootCauseTypeDef]] = None
    Revision: Optional[int] = None
    MatchedEventTime: Optional[datetime] = None


class GetRetrievedTracesGraphResultTypeDef(BaseValidatorModel):
    RetrievalStatus: RetrievalStatusType
    Services: List[RetrievedServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetTraceSummariesResultTypeDef(BaseValidatorModel):
    TraceSummaries: List[TraceSummaryTypeDef]
    ApproximateTime: datetime
    TracesProcessedCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


