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
from aws_resource_validator.pydantic_models.xray_constants import *

class AliasTypeDef(BaseModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None

class AnnotationValueTypeDef(BaseModel):
    NumberValue: Optional[float] = None
    BooleanValue: Optional[bool] = None
    StringValue: Optional[str] = None

class ServiceIdTypeDef(BaseModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    AccountId: Optional[str] = None
    Type: Optional[str] = None

class AvailabilityZoneDetailTypeDef(BaseModel):
    Name: Optional[str] = None

class BackendConnectionErrorsTypeDef(BaseModel):
    TimeoutCount: Optional[int] = None
    ConnectionRefusedCount: Optional[int] = None
    HTTPCode4XXCount: Optional[int] = None
    HTTPCode5XXCount: Optional[int] = None
    UnknownHostCount: Optional[int] = None
    OtherCount: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class BatchGetTracesRequestRequestTypeDef(BaseModel):
    TraceIds: Sequence[str]
    NextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class InsightsConfigurationTypeDef(BaseModel):
    InsightsEnabled: Optional[bool] = None
    NotificationsEnabled: Optional[bool] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class SamplingRuleTypeDef(BaseModel):
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
    Attributes: Optional[Mapping[str, str]] = None

class DeleteGroupRequestRequestTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    PolicyName: str
    PolicyRevisionId: Optional[str] = None

class DeleteSamplingRuleRequestRequestTypeDef(BaseModel):
    RuleName: Optional[str] = None
    RuleARN: Optional[str] = None

class ErrorStatisticsTypeDef(BaseModel):
    ThrottleCount: Optional[int] = None
    OtherCount: Optional[int] = None
    TotalCount: Optional[int] = None

class FaultStatisticsTypeDef(BaseModel):
    OtherCount: Optional[int] = None
    TotalCount: Optional[int] = None

class HistogramEntryTypeDef(BaseModel):
    Value: Optional[float] = None
    Count: Optional[int] = None

class EncryptionConfigTypeDef(BaseModel):
    KeyId: Optional[str] = None
    Status: Optional[EncryptionStatusType] = None
    Type: Optional[EncryptionTypeType] = None

class RootCauseExceptionTypeDef(BaseModel):
    Name: Optional[str] = None
    Message: Optional[str] = None

class ForecastStatisticsTypeDef(BaseModel):
    FaultCountHigh: Optional[int] = None
    FaultCountLow: Optional[int] = None

class GetGroupRequestRequestTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None

class GetGroupsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class GetInsightEventsRequestRequestTypeDef(BaseModel):
    InsightId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetInsightRequestRequestTypeDef(BaseModel):
    InsightId: str

class GetSamplingRulesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class GetSamplingStatisticSummariesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class SamplingStatisticSummaryTypeDef(BaseModel):
    RuleName: Optional[str] = None
    Timestamp: Optional[datetime] = None
    RequestCount: Optional[int] = None
    BorrowCount: Optional[int] = None
    SampledCount: Optional[int] = None

class SamplingTargetDocumentTypeDef(BaseModel):
    RuleName: Optional[str] = None
    FixedRate: Optional[float] = None
    ReservoirQuota: Optional[int] = None
    ReservoirQuotaTTL: Optional[datetime] = None
    Interval: Optional[int] = None

class UnprocessedStatisticsTypeDef(BaseModel):
    RuleName: Optional[str] = None
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class GetTraceGraphRequestRequestTypeDef(BaseModel):
    TraceIds: Sequence[str]
    NextToken: Optional[str] = None

class SamplingStrategyTypeDef(BaseModel):
    Name: Optional[SamplingStrategyNameType] = None
    Value: Optional[float] = None

class HttpTypeDef(BaseModel):
    HttpURL: Optional[str] = None
    HttpStatus: Optional[int] = None
    HttpMethod: Optional[str] = None
    UserAgent: Optional[str] = None
    ClientIp: Optional[str] = None

class RequestImpactStatisticsTypeDef(BaseModel):
    FaultCount: Optional[int] = None
    OkCount: Optional[int] = None
    TotalCount: Optional[int] = None

class InsightImpactGraphEdgeTypeDef(BaseModel):
    ReferenceId: Optional[int] = None

class InstanceIdDetailTypeDef(BaseModel):
    Id: Optional[str] = None

class ListResourcePoliciesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class ResourcePolicyTypeDef(BaseModel):
    PolicyName: Optional[str] = None
    PolicyDocument: Optional[str] = None
    PolicyRevisionId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    NextToken: Optional[str] = None

class PutEncryptionConfigRequestRequestTypeDef(BaseModel):
    Type: EncryptionTypeType
    KeyId: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    PolicyName: str
    PolicyDocument: str
    PolicyRevisionId: Optional[str] = None
    BypassPolicyLockoutCheck: Optional[bool] = None

class PutTraceSegmentsRequestRequestTypeDef(BaseModel):
    TraceSegmentDocuments: Sequence[str]

class UnprocessedTraceSegmentTypeDef(BaseModel):
    Id: Optional[str] = None
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class ResourceARNDetailTypeDef(BaseModel):
    ARN: Optional[str] = None

class ResponseTimeRootCauseEntityTypeDef(BaseModel):
    Name: Optional[str] = None
    Coverage: Optional[float] = None
    Remote: Optional[bool] = None

class SamplingRulePaginatorTypeDef(BaseModel):
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

class SamplingRuleUpdateTypeDef(BaseModel):
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
    Attributes: Optional[Mapping[str, str]] = None

class SegmentTypeDef(BaseModel):
    Id: Optional[str] = None
    Document: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class AnomalousServiceTypeDef(BaseModel):
    ServiceId: Optional[ServiceIdTypeDef] = None

class TraceUserTypeDef(BaseModel):
    UserName: Optional[str] = None
    ServiceIds: Optional[List[ServiceIdTypeDef]] = None

class ValueWithServiceIdsTypeDef(BaseModel):
    AnnotationValue: Optional[AnnotationValueTypeDef] = None
    ServiceIds: Optional[List[ServiceIdTypeDef]] = None

class BatchGetTracesRequestBatchGetTracesPaginateTypeDef(BaseModel):
    TraceIds: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetGroupsRequestGetGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSamplingRulesRequestGetSamplingRulesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSamplingStatisticSummariesRequestGetSamplingStatisticSummariesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTraceGraphRequestGetTraceGraphPaginateTypeDef(BaseModel):
    TraceIds: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcePoliciesRequestListResourcePoliciesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GroupSummaryTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfigurationTypeDef] = None

class GroupTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfigurationTypeDef] = None

class UpdateGroupRequestRequestTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfigurationTypeDef] = None

class CreateGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateSamplingRuleRequestRequestTypeDef(BaseModel):
    SamplingRule: SamplingRuleTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class SamplingRuleRecordTypeDef(BaseModel):
    SamplingRule: Optional[SamplingRuleTypeDef] = None
    CreatedAt: Optional[datetime] = None
    ModifiedAt: Optional[datetime] = None

class EdgeStatisticsTypeDef(BaseModel):
    OkCount: Optional[int] = None
    ErrorStatistics: Optional[ErrorStatisticsTypeDef] = None
    FaultStatistics: Optional[FaultStatisticsTypeDef] = None
    TotalCount: Optional[int] = None
    TotalResponseTime: Optional[float] = None

class ServiceStatisticsTypeDef(BaseModel):
    OkCount: Optional[int] = None
    ErrorStatistics: Optional[ErrorStatisticsTypeDef] = None
    FaultStatistics: Optional[FaultStatisticsTypeDef] = None
    TotalCount: Optional[int] = None
    TotalResponseTime: Optional[float] = None

class GetEncryptionConfigResultTypeDef(BaseModel):
    EncryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutEncryptionConfigResultTypeDef(BaseModel):
    EncryptionConfig: EncryptionConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ErrorRootCauseEntityTypeDef(BaseModel):
    Name: Optional[str] = None
    Exceptions: Optional[List[RootCauseExceptionTypeDef]] = None
    Remote: Optional[bool] = None

class FaultRootCauseEntityTypeDef(BaseModel):
    Name: Optional[str] = None
    Exceptions: Optional[List[RootCauseExceptionTypeDef]] = None
    Remote: Optional[bool] = None

class GetInsightImpactGraphRequestRequestTypeDef(BaseModel):
    InsightId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: Optional[str] = None

class GetInsightSummariesRequestRequestTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    States: Optional[Sequence[InsightStateType]] = None
    GroupARN: Optional[str] = None
    GroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetServiceGraphRequestGetServiceGraphPaginateTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetServiceGraphRequestRequestTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    NextToken: Optional[str] = None

class GetTimeSeriesServiceStatisticsRequestGetTimeSeriesServiceStatisticsPaginateTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    EntitySelectorExpression: Optional[str] = None
    Period: Optional[int] = None
    ForecastStatistics: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTimeSeriesServiceStatisticsRequestRequestTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    EntitySelectorExpression: Optional[str] = None
    Period: Optional[int] = None
    ForecastStatistics: Optional[bool] = None
    NextToken: Optional[str] = None

class SamplingStatisticsDocumentTypeDef(BaseModel):
    RuleName: str
    ClientID: str
    Timestamp: TimestampTypeDef
    RequestCount: int
    SampledCount: int
    BorrowCount: Optional[int] = None

class TelemetryRecordTypeDef(BaseModel):
    Timestamp: TimestampTypeDef
    SegmentsReceivedCount: Optional[int] = None
    SegmentsSentCount: Optional[int] = None
    SegmentsSpilloverCount: Optional[int] = None
    SegmentsRejectedCount: Optional[int] = None
    BackendConnectionErrors: Optional[BackendConnectionErrorsTypeDef] = None

class GetSamplingStatisticSummariesResultTypeDef(BaseModel):
    SamplingStatisticSummaries: List[SamplingStatisticSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSamplingTargetsResultTypeDef(BaseModel):
    SamplingTargetDocuments: List[SamplingTargetDocumentTypeDef]
    LastRuleModification: datetime
    UnprocessedStatistics: List[UnprocessedStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTraceSummariesRequestGetTraceSummariesPaginateTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    TimeRangeType: Optional[TimeRangeTypeType] = None
    Sampling: Optional[bool] = None
    SamplingStrategy: Optional[SamplingStrategyTypeDef] = None
    FilterExpression: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTraceSummariesRequestRequestTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    TimeRangeType: Optional[TimeRangeTypeType] = None
    Sampling: Optional[bool] = None
    SamplingStrategy: Optional[SamplingStrategyTypeDef] = None
    FilterExpression: Optional[str] = None
    NextToken: Optional[str] = None

class InsightImpactGraphServiceTypeDef(BaseModel):
    ReferenceId: Optional[int] = None
    Type: Optional[str] = None
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    AccountId: Optional[str] = None
    Edges: Optional[List[InsightImpactGraphEdgeTypeDef]] = None

class ListResourcePoliciesResultTypeDef(BaseModel):
    ResourcePolicies: List[ResourcePolicyTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResultTypeDef(BaseModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutTraceSegmentsResultTypeDef(BaseModel):
    UnprocessedTraceSegments: List[UnprocessedTraceSegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResponseTimeRootCauseServiceTypeDef(BaseModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None
    AccountId: Optional[str] = None
    EntityPath: Optional[List[ResponseTimeRootCauseEntityTypeDef]] = None
    Inferred: Optional[bool] = None

class SamplingRuleRecordPaginatorTypeDef(BaseModel):
    SamplingRule: Optional[SamplingRulePaginatorTypeDef] = None
    CreatedAt: Optional[datetime] = None
    ModifiedAt: Optional[datetime] = None

class UpdateSamplingRuleRequestRequestTypeDef(BaseModel):
    SamplingRuleUpdate: SamplingRuleUpdateTypeDef

class TraceTypeDef(BaseModel):
    Id: Optional[str] = None
    Duration: Optional[float] = None
    LimitExceeded: Optional[bool] = None
    Segments: Optional[List[SegmentTypeDef]] = None

class InsightEventTypeDef(BaseModel):
    Summary: Optional[str] = None
    EventTime: Optional[datetime] = None
    ClientRequestImpactStatistics: Optional[RequestImpactStatisticsTypeDef] = None
    RootCauseServiceRequestImpactStatistics: Optional[RequestImpactStatisticsTypeDef] = None
    TopAnomalousServices: Optional[List[AnomalousServiceTypeDef]] = None

class InsightSummaryTypeDef(BaseModel):
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

class InsightTypeDef(BaseModel):
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

class GetGroupsResultTypeDef(BaseModel):
    Groups: List[GroupSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResultTypeDef(BaseModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResultTypeDef(BaseModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupResultTypeDef(BaseModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSamplingRuleResultTypeDef(BaseModel):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSamplingRuleResultTypeDef(BaseModel):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSamplingRulesResultTypeDef(BaseModel):
    SamplingRuleRecords: List[SamplingRuleRecordTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSamplingRuleResultTypeDef(BaseModel):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EdgeTypeDef(BaseModel):
    ReferenceId: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    SummaryStatistics: Optional[EdgeStatisticsTypeDef] = None
    ResponseTimeHistogram: Optional[List[HistogramEntryTypeDef]] = None
    Aliases: Optional[List[AliasTypeDef]] = None
    EdgeType: Optional[str] = None
    ReceivedEventAgeHistogram: Optional[List[HistogramEntryTypeDef]] = None

class TimeSeriesServiceStatisticsTypeDef(BaseModel):
    Timestamp: Optional[datetime] = None
    EdgeSummaryStatistics: Optional[EdgeStatisticsTypeDef] = None
    ServiceSummaryStatistics: Optional[ServiceStatisticsTypeDef] = None
    ServiceForecastStatistics: Optional[ForecastStatisticsTypeDef] = None
    ResponseTimeHistogram: Optional[List[HistogramEntryTypeDef]] = None

class ErrorRootCauseServiceTypeDef(BaseModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None
    AccountId: Optional[str] = None
    EntityPath: Optional[List[ErrorRootCauseEntityTypeDef]] = None
    Inferred: Optional[bool] = None

class FaultRootCauseServiceTypeDef(BaseModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None
    AccountId: Optional[str] = None
    EntityPath: Optional[List[FaultRootCauseEntityTypeDef]] = None
    Inferred: Optional[bool] = None

class GetSamplingTargetsRequestRequestTypeDef(BaseModel):
    SamplingStatisticsDocuments: Sequence[SamplingStatisticsDocumentTypeDef]

class PutTelemetryRecordsRequestRequestTypeDef(BaseModel):
    TelemetryRecords: Sequence[TelemetryRecordTypeDef]
    EC2InstanceId: Optional[str] = None
    Hostname: Optional[str] = None
    ResourceARN: Optional[str] = None

class GetInsightImpactGraphResultTypeDef(BaseModel):
    InsightId: str
    StartTime: datetime
    EndTime: datetime
    ServiceGraphStartTime: datetime
    ServiceGraphEndTime: datetime
    Services: List[InsightImpactGraphServiceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResponseTimeRootCauseTypeDef(BaseModel):
    Services: Optional[List[ResponseTimeRootCauseServiceTypeDef]] = None
    ClientImpacting: Optional[bool] = None

class GetSamplingRulesResultPaginatorTypeDef(BaseModel):
    SamplingRuleRecords: List[SamplingRuleRecordPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetTracesResultTypeDef(BaseModel):
    Traces: List[TraceTypeDef]
    UnprocessedTraceIds: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightEventsResultTypeDef(BaseModel):
    InsightEvents: List[InsightEventTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightSummariesResultTypeDef(BaseModel):
    InsightSummaries: List[InsightSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightResultTypeDef(BaseModel):
    Insight: InsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceTypeDef(BaseModel):
    ReferenceId: Optional[int] = None
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Root: Optional[bool] = None
    AccountId: Optional[str] = None
    Type: Optional[str] = None
    State: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Edges: Optional[List[EdgeTypeDef]] = None
    SummaryStatistics: Optional[ServiceStatisticsTypeDef] = None
    DurationHistogram: Optional[List[HistogramEntryTypeDef]] = None
    ResponseTimeHistogram: Optional[List[HistogramEntryTypeDef]] = None

class GetTimeSeriesServiceStatisticsResultTypeDef(BaseModel):
    TimeSeriesServiceStatistics: List[TimeSeriesServiceStatisticsTypeDef]
    ContainsOldGroupVersions: bool
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ErrorRootCauseTypeDef(BaseModel):
    Services: Optional[List[ErrorRootCauseServiceTypeDef]] = None
    ClientImpacting: Optional[bool] = None

class FaultRootCauseTypeDef(BaseModel):
    Services: Optional[List[FaultRootCauseServiceTypeDef]] = None
    ClientImpacting: Optional[bool] = None

class GetServiceGraphResultTypeDef(BaseModel):
    StartTime: datetime
    EndTime: datetime
    Services: List[ServiceTypeDef]
    ContainsOldGroupVersions: bool
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTraceGraphResultTypeDef(BaseModel):
    Services: List[ServiceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TraceSummaryTypeDef(BaseModel):
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

class GetTraceSummariesResultTypeDef(BaseModel):
    TraceSummaries: List[TraceSummaryTypeDef]
    ApproximateTime: datetime
    TracesProcessedCount: int
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

