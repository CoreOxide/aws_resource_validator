from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.xray.xray_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Alias(BaseValidatorModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None


class AnnotationValue(BaseValidatorModel):
    NumberValue: Optional[float] = None
    BooleanValue: Optional[bool] = None
    StringValue: Optional[str] = None


class ServiceId(BaseValidatorModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    AccountId: Optional[str] = None
    Type: Optional[str] = None


class AvailabilityZoneDetail(BaseValidatorModel):
    Name: Optional[str] = None


class BackendConnectionErrors(BaseValidatorModel):
    TimeoutCount: Optional[int] = None
    ConnectionRefusedCount: Optional[int] = None
    HTTPCode4XXCount: Optional[int] = None
    HTTPCode5XXCount: Optional[int] = None
    UnknownHostCount: Optional[int] = None
    OtherCount: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'batch_get_traces' function.
class BatchGetTracesRequest(BaseValidatorModel):
    TraceIds: List[str]
    NextToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelTraceRetrievalRequest(BaseValidatorModel):
    RetrievalToken: str


class InsightsConfiguration(BaseValidatorModel):
    InsightsEnabled: Optional[bool] = None
    NotificationsEnabled: Optional[bool] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class DeleteGroupRequest(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None


class DeleteResourcePolicyRequest(BaseValidatorModel):
    PolicyName: str
    PolicyRevisionId: Optional[str] = None


# This class is the input for the 'delete_sampling_rule' function.
class DeleteSamplingRuleRequest(BaseValidatorModel):
    RuleName: Optional[str] = None
    RuleARN: Optional[str] = None


class ErrorStatistics(BaseValidatorModel):
    ThrottleCount: Optional[int] = None
    OtherCount: Optional[int] = None
    TotalCount: Optional[int] = None


class FaultStatistics(BaseValidatorModel):
    OtherCount: Optional[int] = None
    TotalCount: Optional[int] = None


class HistogramEntry(BaseValidatorModel):
    Value: Optional[float] = None
    Count: Optional[int] = None


class EncryptionConfig(BaseValidatorModel):
    KeyId: Optional[str] = None
    Status: Optional[EncryptionStatusType] = None
    Type: Optional[EncryptionTypeType] = None


class RootCauseException(BaseValidatorModel):
    Name: Optional[str] = None
    Message: Optional[str] = None


class ForecastStatistics(BaseValidatorModel):
    FaultCountHigh: Optional[int] = None
    FaultCountLow: Optional[int] = None


# This class is the input for the 'get_group' function.
class GetGroupRequest(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None


# This class is the input for the 'get_groups' function.
class GetGroupsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'get_indexing_rules' function.
class GetIndexingRulesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'get_insight_events' function.
class GetInsightEventsRequest(BaseValidatorModel):
    InsightId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'get_insight' function.
class GetInsightRequest(BaseValidatorModel):
    InsightId: str


# This class is the input for the 'get_retrieved_traces_graph' function.
class GetRetrievedTracesGraphRequest(BaseValidatorModel):
    RetrievalToken: str
    NextToken: Optional[str] = None


# This class is the input for the 'get_sampling_rules' function.
class GetSamplingRulesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'get_sampling_statistic_summaries' function.
class GetSamplingStatisticSummariesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class SamplingStatisticSummary(BaseValidatorModel):
    RuleName: Optional[str] = None
    Timestamp: Optional[datetime] = None
    RequestCount: Optional[int] = None
    BorrowCount: Optional[int] = None
    SampledCount: Optional[int] = None


class SamplingTargetDocument(BaseValidatorModel):
    RuleName: Optional[str] = None
    FixedRate: Optional[float] = None
    ReservoirQuota: Optional[int] = None
    ReservoirQuotaTTL: Optional[datetime] = None
    Interval: Optional[int] = None


class UnprocessedStatistics(BaseValidatorModel):
    RuleName: Optional[str] = None
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


# This class is the input for the 'get_trace_graph' function.
class GetTraceGraphRequest(BaseValidatorModel):
    TraceIds: List[str]
    NextToken: Optional[str] = None


class SamplingStrategy(BaseValidatorModel):
    Name: Optional[SamplingStrategyNameType] = None
    Value: Optional[float] = None


class GraphLink(BaseValidatorModel):
    ReferenceType: Optional[str] = None
    SourceTraceId: Optional[str] = None
    DestinationTraceIds: Optional[List[str]] = None


class Http(BaseValidatorModel):
    HttpURL: Optional[str] = None
    HttpStatus: Optional[int] = None
    HttpMethod: Optional[str] = None
    UserAgent: Optional[str] = None
    ClientIp: Optional[str] = None


class ProbabilisticRuleValue(BaseValidatorModel):
    DesiredSamplingPercentage: float
    ActualSamplingPercentage: Optional[float] = None


class ProbabilisticRuleValueUpdate(BaseValidatorModel):
    DesiredSamplingPercentage: float


class RequestImpactStatistics(BaseValidatorModel):
    FaultCount: Optional[int] = None
    OkCount: Optional[int] = None
    TotalCount: Optional[int] = None


class InsightImpactGraphEdge(BaseValidatorModel):
    ReferenceId: Optional[int] = None


class InstanceIdDetail(BaseValidatorModel):
    Id: Optional[str] = None


# This class is the input for the 'list_resource_policies' function.
class ListResourcePoliciesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class ResourcePolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyDocument: Optional[str] = None
    PolicyRevisionId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None


# This class is the input for the 'list_retrieved_traces' function.
class ListRetrievedTracesRequest(BaseValidatorModel):
    RetrievalToken: str
    TraceFormat: Optional[TraceFormatTypeType] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None


# This class is the input for the 'put_encryption_config' function.
class PutEncryptionConfigRequest(BaseValidatorModel):
    Type: EncryptionTypeType
    KeyId: Optional[str] = None


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    PolicyRevisionId: Optional[str] = None
    BypassPolicyLockoutCheck: Optional[bool] = None


# This class is the input for the 'put_trace_segments' function.
class PutTraceSegmentsRequest(BaseValidatorModel):
    TraceSegmentDocuments: List[str]


class UnprocessedTraceSegment(BaseValidatorModel):
    Id: Optional[str] = None
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class ResourceARNDetail(BaseValidatorModel):
    ARN: Optional[str] = None


class ResponseTimeRootCauseEntity(BaseValidatorModel):
    Name: Optional[str] = None
    Coverage: Optional[float] = None
    Remote: Optional[bool] = None


class Span(BaseValidatorModel):
    Id: Optional[str] = None
    Document: Optional[str] = None


class SamplingRuleOutput(BaseValidatorModel):
    ResourceARN: str
    Priority: int
    FixedRate: float
    ReservoirSize: int
    ServiceName: str
    ServiceType: str
    Host: str
    HTTPMethod: str
    URLPath: str
    Version: int
    RuleName: Optional[str] = None
    RuleARN: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class SamplingRule(BaseValidatorModel):
    ResourceARN: str
    Priority: int
    FixedRate: float
    ReservoirSize: int
    ServiceName: str
    ServiceType: str
    Host: str
    HTTPMethod: str
    URLPath: str
    Version: int
    RuleName: Optional[str] = None
    RuleARN: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class SamplingRuleUpdate(BaseValidatorModel):
    RuleName: Optional[str] = None
    RuleARN: Optional[str] = None
    ResourceARN: Optional[str] = None
    Priority: Optional[int] = None
    FixedRate: Optional[float] = None
    ReservoirSize: Optional[int] = None
    Host: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceType: Optional[str] = None
    HTTPMethod: Optional[str] = None
    URLPath: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class Segment(BaseValidatorModel):
    Id: Optional[str] = None
    Document: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_trace_segment_destination' function.
class UpdateTraceSegmentDestinationRequest(BaseValidatorModel):
    Destination: Optional[TraceSegmentDestinationType] = None


class AnomalousService(BaseValidatorModel):
    ServiceId: Optional[ServiceId] = None


class TraceUser(BaseValidatorModel):
    UserName: Optional[str] = None
    ServiceIds: Optional[List[ServiceId]] = None


class ValueWithServiceIds(BaseValidatorModel):
    AnnotationValue: Optional[AnnotationValue] = None
    ServiceIds: Optional[List[ServiceId]] = None


class BatchGetTracesRequestPaginate(BaseValidatorModel):
    TraceIds: List[str]
    PaginationConfig: Optional[PaginatorConfig] = None


class GetGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetSamplingRulesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetSamplingStatisticSummariesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTraceGraphRequestPaginate(BaseValidatorModel):
    TraceIds: List[str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourcePoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTraceSegmentDestinationResult(BaseValidatorModel):
    Destination: TraceSegmentDestinationType
    Status: TraceSegmentDestinationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_trace_retrieval' function.
class StartTraceRetrievalResult(BaseValidatorModel):
    RetrievalToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_trace_segment_destination' function.
class UpdateTraceSegmentDestinationResult(BaseValidatorModel):
    Destination: TraceSegmentDestinationType
    Status: TraceSegmentDestinationStatusType
    ResponseMetadata: ResponseMetadata


class GroupSummary(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfiguration] = None


class Group(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfiguration] = None


# This class is the input for the 'update_group' function.
class UpdateGroupRequest(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfiguration] = None


# This class is the input for the 'create_group' function.
class CreateGroupRequest(BaseValidatorModel):
    GroupName: str
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfiguration] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class EdgeStatistics(BaseValidatorModel):
    OkCount: Optional[int] = None
    ErrorStatistics: Optional[ErrorStatistics] = None
    FaultStatistics: Optional[FaultStatistics] = None
    TotalCount: Optional[int] = None
    TotalResponseTime: Optional[float] = None


class ServiceStatistics(BaseValidatorModel):
    OkCount: Optional[int] = None
    ErrorStatistics: Optional[ErrorStatistics] = None
    FaultStatistics: Optional[FaultStatistics] = None
    TotalCount: Optional[int] = None
    TotalResponseTime: Optional[float] = None


class GetEncryptionConfigResult(BaseValidatorModel):
    EncryptionConfig: EncryptionConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_encryption_config' function.
class PutEncryptionConfigResult(BaseValidatorModel):
    EncryptionConfig: EncryptionConfig
    ResponseMetadata: ResponseMetadata


class ErrorRootCauseEntity(BaseValidatorModel):
    Name: Optional[str] = None
    Exceptions: Optional[List[RootCauseException]] = None
    Remote: Optional[bool] = None


class FaultRootCauseEntity(BaseValidatorModel):
    Name: Optional[str] = None
    Exceptions: Optional[List[RootCauseException]] = None
    Remote: Optional[bool] = None


# This class is the input for the 'get_insight_impact_graph' function.
class GetInsightImpactGraphRequest(BaseValidatorModel):
    InsightId: str
    StartTime: Timestamp
    EndTime: Timestamp
    NextToken: Optional[str] = None


# This class is the input for the 'get_insight_summaries' function.
class GetInsightSummariesRequest(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    States: Optional[List[InsightStateType]] = None
    GroupARN: Optional[str] = None
    GroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetServiceGraphRequestPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_service_graph' function.
class GetServiceGraphRequest(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    NextToken: Optional[str] = None


class GetTimeSeriesServiceStatisticsRequestPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    EntitySelectorExpression: Optional[str] = None
    Period: Optional[int] = None
    ForecastStatistics: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_time_series_service_statistics' function.
class GetTimeSeriesServiceStatisticsRequest(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    EntitySelectorExpression: Optional[str] = None
    Period: Optional[int] = None
    ForecastStatistics: Optional[bool] = None
    NextToken: Optional[str] = None


class SamplingStatisticsDocument(BaseValidatorModel):
    RuleName: str
    ClientID: str
    Timestamp: Timestamp
    RequestCount: int
    SampledCount: int
    BorrowCount: Optional[int] = None


# This class is the input for the 'start_trace_retrieval' function.
class StartTraceRetrievalRequest(BaseValidatorModel):
    TraceIds: List[str]
    StartTime: Timestamp
    EndTime: Timestamp


class TelemetryRecord(BaseValidatorModel):
    Timestamp: Timestamp
    SegmentsReceivedCount: Optional[int] = None
    SegmentsSentCount: Optional[int] = None
    SegmentsSpilloverCount: Optional[int] = None
    SegmentsRejectedCount: Optional[int] = None
    BackendConnectionErrors: Optional[BackendConnectionErrors] = None


# This class is the output for the 'get_sampling_statistic_summaries' function.
class GetSamplingStatisticSummariesResult(BaseValidatorModel):
    SamplingStatisticSummaries: List[SamplingStatisticSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_sampling_targets' function.
class GetSamplingTargetsResult(BaseValidatorModel):
    SamplingTargetDocuments: List[SamplingTargetDocument]
    LastRuleModification: datetime
    UnprocessedStatistics: List[UnprocessedStatistics]
    ResponseMetadata: ResponseMetadata


class GetTraceSummariesRequestPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    TimeRangeType: Optional[TimeRangeTypeType] = None
    Sampling: Optional[bool] = None
    SamplingStrategy: Optional[SamplingStrategy] = None
    FilterExpression: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_trace_summaries' function.
class GetTraceSummariesRequest(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    TimeRangeType: Optional[TimeRangeTypeType] = None
    Sampling: Optional[bool] = None
    SamplingStrategy: Optional[SamplingStrategy] = None
    FilterExpression: Optional[str] = None
    NextToken: Optional[str] = None


class IndexingRuleValue(BaseValidatorModel):
    Probabilistic: Optional[ProbabilisticRuleValue] = None


class IndexingRuleValueUpdate(BaseValidatorModel):
    Probabilistic: Optional[ProbabilisticRuleValueUpdate] = None


class InsightImpactGraphService(BaseValidatorModel):
    ReferenceId: Optional[int] = None
    Type: Optional[str] = None
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    AccountId: Optional[str] = None
    Edges: Optional[List[InsightImpactGraphEdge]] = None


# This class is the output for the 'list_resource_policies' function.
class ListResourcePoliciesResult(BaseValidatorModel):
    ResourcePolicies: List[ResourcePolicy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResult(BaseValidatorModel):
    ResourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_trace_segments' function.
class PutTraceSegmentsResult(BaseValidatorModel):
    UnprocessedTraceSegments: List[UnprocessedTraceSegment]
    ResponseMetadata: ResponseMetadata


class ResponseTimeRootCauseService(BaseValidatorModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None
    AccountId: Optional[str] = None
    EntityPath: Optional[List[ResponseTimeRootCauseEntity]] = None
    Inferred: Optional[bool] = None


class RetrievedTrace(BaseValidatorModel):
    Id: Optional[str] = None
    Duration: Optional[float] = None
    Spans: Optional[List[Span]] = None


class SamplingRuleRecord(BaseValidatorModel):
    SamplingRule: Optional[SamplingRuleOutput] = None
    CreatedAt: Optional[datetime] = None
    ModifiedAt: Optional[datetime] = None

SamplingRuleUnion = Union[SamplingRule, SamplingRuleOutput]


# This class is the input for the 'update_sampling_rule' function.
class UpdateSamplingRuleRequest(BaseValidatorModel):
    SamplingRuleUpdate: SamplingRuleUpdate


class Trace(BaseValidatorModel):
    Id: Optional[str] = None
    Duration: Optional[float] = None
    LimitExceeded: Optional[bool] = None
    Segments: Optional[List[Segment]] = None


class InsightEvent(BaseValidatorModel):
    Summary: Optional[str] = None
    EventTime: Optional[datetime] = None
    ClientRequestImpactStatistics: Optional[RequestImpactStatistics] = None
    RootCauseServiceRequestImpactStatistics: Optional[RequestImpactStatistics] = None
    TopAnomalousServices: Optional[List[AnomalousService]] = None


class InsightSummary(BaseValidatorModel):
    InsightId: Optional[str] = None
    GroupARN: Optional[str] = None
    GroupName: Optional[str] = None
    RootCauseServiceId: Optional[ServiceId] = None
    Categories: Optional[List[Literal['FAULT']]] = None
    State: Optional[InsightStateType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Summary: Optional[str] = None
    ClientRequestImpactStatistics: Optional[RequestImpactStatistics] = None
    RootCauseServiceRequestImpactStatistics: Optional[RequestImpactStatistics] = None
    TopAnomalousServices: Optional[List[AnomalousService]] = None
    LastUpdateTime: Optional[datetime] = None


class Insight(BaseValidatorModel):
    InsightId: Optional[str] = None
    GroupARN: Optional[str] = None
    GroupName: Optional[str] = None
    RootCauseServiceId: Optional[ServiceId] = None
    Categories: Optional[List[Literal['FAULT']]] = None
    State: Optional[InsightStateType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Summary: Optional[str] = None
    ClientRequestImpactStatistics: Optional[RequestImpactStatistics] = None
    RootCauseServiceRequestImpactStatistics: Optional[RequestImpactStatistics] = None
    TopAnomalousServices: Optional[List[AnomalousService]] = None


# This class is the output for the 'get_groups' function.
class GetGroupsResult(BaseValidatorModel):
    Groups: List[GroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_group' function.
class CreateGroupResult(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_group' function.
class GetGroupResult(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_group' function.
class UpdateGroupResult(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


class Edge(BaseValidatorModel):
    ReferenceId: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    SummaryStatistics: Optional[EdgeStatistics] = None
    ResponseTimeHistogram: Optional[List[HistogramEntry]] = None
    Aliases: Optional[List[Alias]] = None
    EdgeType: Optional[str] = None
    ReceivedEventAgeHistogram: Optional[List[HistogramEntry]] = None


class TimeSeriesServiceStatistics(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    EdgeSummaryStatistics: Optional[EdgeStatistics] = None
    ServiceSummaryStatistics: Optional[ServiceStatistics] = None
    ServiceForecastStatistics: Optional[ForecastStatistics] = None
    ResponseTimeHistogram: Optional[List[HistogramEntry]] = None


class ErrorRootCauseService(BaseValidatorModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None
    AccountId: Optional[str] = None
    EntityPath: Optional[List[ErrorRootCauseEntity]] = None
    Inferred: Optional[bool] = None


class FaultRootCauseService(BaseValidatorModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None
    AccountId: Optional[str] = None
    EntityPath: Optional[List[FaultRootCauseEntity]] = None
    Inferred: Optional[bool] = None


# This class is the input for the 'get_sampling_targets' function.
class GetSamplingTargetsRequest(BaseValidatorModel):
    SamplingStatisticsDocuments: List[SamplingStatisticsDocument]


class PutTelemetryRecordsRequest(BaseValidatorModel):
    TelemetryRecords: List[TelemetryRecord]
    EC2InstanceId: Optional[str] = None
    Hostname: Optional[str] = None
    ResourceARN: Optional[str] = None


class IndexingRule(BaseValidatorModel):
    Name: Optional[str] = None
    ModifiedAt: Optional[datetime] = None
    Rule: Optional[IndexingRuleValue] = None


# This class is the input for the 'update_indexing_rule' function.
class UpdateIndexingRuleRequest(BaseValidatorModel):
    Name: str
    Rule: IndexingRuleValueUpdate


# This class is the output for the 'get_insight_impact_graph' function.
class GetInsightImpactGraphResult(BaseValidatorModel):
    InsightId: str
    StartTime: datetime
    EndTime: datetime
    ServiceGraphStartTime: datetime
    ServiceGraphEndTime: datetime
    Services: List[InsightImpactGraphService]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResponseTimeRootCause(BaseValidatorModel):
    Services: Optional[List[ResponseTimeRootCauseService]] = None
    ClientImpacting: Optional[bool] = None


# This class is the output for the 'list_retrieved_traces' function.
class ListRetrievedTracesResult(BaseValidatorModel):
    RetrievalStatus: RetrievalStatusType
    TraceFormat: TraceFormatTypeType
    Traces: List[RetrievedTrace]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_sampling_rule' function.
class CreateSamplingRuleResult(BaseValidatorModel):
    SamplingRuleRecord: SamplingRuleRecord
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_sampling_rule' function.
class DeleteSamplingRuleResult(BaseValidatorModel):
    SamplingRuleRecord: SamplingRuleRecord
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sampling_rules' function.
class GetSamplingRulesResult(BaseValidatorModel):
    SamplingRuleRecords: List[SamplingRuleRecord]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_sampling_rule' function.
class UpdateSamplingRuleResult(BaseValidatorModel):
    SamplingRuleRecord: SamplingRuleRecord
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_sampling_rule' function.
class CreateSamplingRuleRequest(BaseValidatorModel):
    SamplingRule: SamplingRuleUnion
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'batch_get_traces' function.
class BatchGetTracesResult(BaseValidatorModel):
    Traces: List[Trace]
    UnprocessedTraceIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_insight_events' function.
class GetInsightEventsResult(BaseValidatorModel):
    InsightEvents: List[InsightEvent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_insight_summaries' function.
class GetInsightSummariesResult(BaseValidatorModel):
    InsightSummaries: List[InsightSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_insight' function.
class GetInsightResult(BaseValidatorModel):
    Insight: Insight
    ResponseMetadata: ResponseMetadata


class Service(BaseValidatorModel):
    ReferenceId: Optional[int] = None
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Root: Optional[bool] = None
    AccountId: Optional[str] = None
    Type: Optional[str] = None
    State: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Edges: Optional[List[Edge]] = None
    SummaryStatistics: Optional[ServiceStatistics] = None
    DurationHistogram: Optional[List[HistogramEntry]] = None
    ResponseTimeHistogram: Optional[List[HistogramEntry]] = None


# This class is the output for the 'get_time_series_service_statistics' function.
class GetTimeSeriesServiceStatisticsResult(BaseValidatorModel):
    TimeSeriesServiceStatistics: List[TimeSeriesServiceStatistics]
    ContainsOldGroupVersions: bool
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ErrorRootCause(BaseValidatorModel):
    Services: Optional[List[ErrorRootCauseService]] = None
    ClientImpacting: Optional[bool] = None


class FaultRootCause(BaseValidatorModel):
    Services: Optional[List[FaultRootCauseService]] = None
    ClientImpacting: Optional[bool] = None


# This class is the output for the 'get_indexing_rules' function.
class GetIndexingRulesResult(BaseValidatorModel):
    IndexingRules: List[IndexingRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_indexing_rule' function.
class UpdateIndexingRuleResult(BaseValidatorModel):
    IndexingRule: IndexingRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_graph' function.
class GetServiceGraphResult(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    Services: List[Service]
    ContainsOldGroupVersions: bool
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_trace_graph' function.
class GetTraceGraphResult(BaseValidatorModel):
    Services: List[Service]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RetrievedService(BaseValidatorModel):
    Service: Optional[Service] = None
    Links: Optional[List[GraphLink]] = None


class TraceSummary(BaseValidatorModel):
    Id: Optional[str] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[float] = None
    ResponseTime: Optional[float] = None
    HasFault: Optional[bool] = None
    HasError: Optional[bool] = None
    HasThrottle: Optional[bool] = None
    IsPartial: Optional[bool] = None
    Http: Optional[Http] = None
    Annotations: Optional[Dict[str, List[ValueWithServiceIds]]] = None
    Users: Optional[List[TraceUser]] = None
    ServiceIds: Optional[List[ServiceId]] = None
    ResourceARNs: Optional[List[ResourceARNDetail]] = None
    InstanceIds: Optional[List[InstanceIdDetail]] = None
    AvailabilityZones: Optional[List[AvailabilityZoneDetail]] = None
    EntryPoint: Optional[ServiceId] = None
    FaultRootCauses: Optional[List[FaultRootCause]] = None
    ErrorRootCauses: Optional[List[ErrorRootCause]] = None
    ResponseTimeRootCauses: Optional[List[ResponseTimeRootCause]] = None
    Revision: Optional[int] = None
    MatchedEventTime: Optional[datetime] = None


# This class is the output for the 'get_retrieved_traces_graph' function.
class GetRetrievedTracesGraphResult(BaseValidatorModel):
    RetrievalStatus: RetrievalStatusType
    Services: List[RetrievedService]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_trace_summaries' function.
class GetTraceSummariesResult(BaseValidatorModel):
    TraceSummaries: List[TraceSummary]
    ApproximateTime: datetime
    TracesProcessedCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None