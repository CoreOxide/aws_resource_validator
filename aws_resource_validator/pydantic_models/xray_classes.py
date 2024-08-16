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
from aws_resource_validator.pydantic_models.xray_constants import *

class AliasTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None

class AnnotationValueTypeDef(BaseValidatorModel):
    NumberValue: Optional[float] = None
    BooleanValue: Optional[bool] = None
    StringValue: Optional[str] = None

class ServiceIdTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    AccountId: Optional[str] = None
    Type: Optional[str] = None

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

class BatchGetTracesRequestRequestTypeDef(BaseValidatorModel):
    TraceIds: Sequence[str]
    NextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class InsightsConfigurationTypeDef(BaseValidatorModel):
    InsightsEnabled: Optional[bool] = None
    NotificationsEnabled: Optional[bool] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class SamplingRuleTypeDef(BaseValidatorModel):
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

class DeleteGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyRevisionId: Optional[str] = None

class DeleteSamplingRuleRequestRequestTypeDef(BaseValidatorModel):
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

class EncryptionConfigTypeDef(BaseValidatorModel):
    KeyId: Optional[str] = None
    Status: Optional[EncryptionStatusType] = None
    Type: Optional[EncryptionTypeType] = None

class RootCauseExceptionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Message: Optional[str] = None

class ForecastStatisticsTypeDef(BaseValidatorModel):
    FaultCountHigh: Optional[int] = None
    FaultCountLow: Optional[int] = None

class GetGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None

class GetGroupsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class GetInsightEventsRequestRequestTypeDef(BaseValidatorModel):
    InsightId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetInsightRequestRequestTypeDef(BaseValidatorModel):
    InsightId: str

class GetSamplingRulesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class GetSamplingStatisticSummariesRequestRequestTypeDef(BaseValidatorModel):
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

class GetTraceGraphRequestRequestTypeDef(BaseValidatorModel):
    TraceIds: Sequence[str]
    NextToken: Optional[str] = None

class SamplingStrategyTypeDef(BaseValidatorModel):
    Name: Optional[SamplingStrategyNameType] = None
    Value: Optional[float] = None

class HttpTypeDef(BaseValidatorModel):
    HttpURL: Optional[str] = None
    HttpStatus: Optional[int] = None
    HttpMethod: Optional[str] = None
    UserAgent: Optional[str] = None
    ClientIp: Optional[str] = None

class RequestImpactStatisticsTypeDef(BaseValidatorModel):
    FaultCount: Optional[int] = None
    OkCount: Optional[int] = None
    TotalCount: Optional[int] = None

class InsightImpactGraphEdgeTypeDef(BaseValidatorModel):
    ReferenceId: Optional[int] = None

class InstanceIdDetailTypeDef(BaseValidatorModel):
    Id: Optional[str] = None

class ListResourcePoliciesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class ResourcePolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyDocument: Optional[str] = None
    PolicyRevisionId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None

class PutEncryptionConfigRequestRequestTypeDef(BaseValidatorModel):
    Type: EncryptionTypeType
    KeyId: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyName: str
    PolicyDocument: str
    PolicyRevisionId: Optional[str] = None
    BypassPolicyLockoutCheck: Optional[bool] = None

class PutTraceSegmentsRequestRequestTypeDef(BaseValidatorModel):
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

class SamplingRulePaginatorTypeDef(BaseValidatorModel):
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

class SamplingRuleUpdateTypeDef(BaseValidatorModel):
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

class SegmentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Document: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class AnomalousServiceTypeDef(BaseValidatorModel):
    ServiceId: Optional[ServiceIdTypeDef] = None

class TraceUserTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    ServiceIds: Optional[List[ServiceIdTypeDef]] = None

class ValueWithServiceIdsTypeDef(BaseValidatorModel):
    AnnotationValue: Optional[AnnotationValueTypeDef] = None
    ServiceIds: Optional[List[ServiceIdTypeDef]] = None

class BatchGetTracesRequestBatchGetTracesPaginateTypeDef(BaseValidatorModel):
    TraceIds: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetGroupsRequestGetGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSamplingRulesRequestGetSamplingRulesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSamplingStatisticSummariesRequestGetSamplingStatisticSummariesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTraceGraphRequestGetTraceGraphPaginateTypeDef(BaseValidatorModel):
    TraceIds: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcePoliciesRequestListResourcePoliciesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

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

class UpdateGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfigurationTypeDef] = None

class CreateGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    FilterExpression: Optional[str] = None
    InsightsConfiguration: Optional[InsightsConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateSamplingRuleRequestRequestTypeDef(BaseValidatorModel):
    SamplingRule: SamplingRuleTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class SamplingRuleRecordTypeDef(BaseValidatorModel):
    SamplingRule: Optional[SamplingRuleTypeDef] = None
    CreatedAt: Optional[datetime] = None
    ModifiedAt: Optional[datetime] = None

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

class GetInsightImpactGraphRequestRequestTypeDef(BaseValidatorModel):
    InsightId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: Optional[str] = None

class GetInsightSummariesRequestRequestTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    States: Optional[Sequence[InsightStateType]] = None
    GroupARN: Optional[str] = None
    GroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetServiceGraphRequestGetServiceGraphPaginateTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetServiceGraphRequestRequestTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    NextToken: Optional[str] = None

class GetTimeSeriesServiceStatisticsRequestGetTimeSeriesServiceStatisticsPaginateTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    GroupName: Optional[str] = None
    GroupARN: Optional[str] = None
    EntitySelectorExpression: Optional[str] = None
    Period: Optional[int] = None
    ForecastStatistics: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTimeSeriesServiceStatisticsRequestRequestTypeDef(BaseValidatorModel):
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

class TelemetryRecordTypeDef(BaseValidatorModel):
    Timestamp: TimestampTypeDef
    SegmentsReceivedCount: Optional[int] = None
    SegmentsSentCount: Optional[int] = None
    SegmentsSpilloverCount: Optional[int] = None
    SegmentsRejectedCount: Optional[int] = None
    BackendConnectionErrors: Optional[BackendConnectionErrorsTypeDef] = None

class GetSamplingStatisticSummariesResultTypeDef(BaseValidatorModel):
    SamplingStatisticSummaries: List[SamplingStatisticSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSamplingTargetsResultTypeDef(BaseValidatorModel):
    SamplingTargetDocuments: List[SamplingTargetDocumentTypeDef]
    LastRuleModification: datetime
    UnprocessedStatistics: List[UnprocessedStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTraceSummariesRequestGetTraceSummariesPaginateTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    TimeRangeType: Optional[TimeRangeTypeType] = None
    Sampling: Optional[bool] = None
    SamplingStrategy: Optional[SamplingStrategyTypeDef] = None
    FilterExpression: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTraceSummariesRequestRequestTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    TimeRangeType: Optional[TimeRangeTypeType] = None
    Sampling: Optional[bool] = None
    SamplingStrategy: Optional[SamplingStrategyTypeDef] = None
    FilterExpression: Optional[str] = None
    NextToken: Optional[str] = None

class InsightImpactGraphServiceTypeDef(BaseValidatorModel):
    ReferenceId: Optional[int] = None
    Type: Optional[str] = None
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    AccountId: Optional[str] = None
    Edges: Optional[List[InsightImpactGraphEdgeTypeDef]] = None

class ListResourcePoliciesResultTypeDef(BaseValidatorModel):
    ResourcePolicies: List[ResourcePolicyTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResultTypeDef(BaseValidatorModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutTraceSegmentsResultTypeDef(BaseValidatorModel):
    UnprocessedTraceSegments: List[UnprocessedTraceSegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResponseTimeRootCauseServiceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None
    AccountId: Optional[str] = None
    EntityPath: Optional[List[ResponseTimeRootCauseEntityTypeDef]] = None
    Inferred: Optional[bool] = None

class SamplingRuleRecordPaginatorTypeDef(BaseValidatorModel):
    SamplingRule: Optional[SamplingRulePaginatorTypeDef] = None
    CreatedAt: Optional[datetime] = None
    ModifiedAt: Optional[datetime] = None

class UpdateSamplingRuleRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResultTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResultTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupResultTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSamplingRuleResultTypeDef(BaseValidatorModel):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSamplingRuleResultTypeDef(BaseValidatorModel):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSamplingRulesResultTypeDef(BaseValidatorModel):
    SamplingRuleRecords: List[SamplingRuleRecordTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSamplingRuleResultTypeDef(BaseValidatorModel):
    SamplingRuleRecord: SamplingRuleRecordTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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

class ErrorRootCauseServiceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None
    AccountId: Optional[str] = None
    EntityPath: Optional[List[ErrorRootCauseEntityTypeDef]] = None
    Inferred: Optional[bool] = None

class FaultRootCauseServiceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Names: Optional[List[str]] = None
    Type: Optional[str] = None
    AccountId: Optional[str] = None
    EntityPath: Optional[List[FaultRootCauseEntityTypeDef]] = None
    Inferred: Optional[bool] = None

class GetSamplingTargetsRequestRequestTypeDef(BaseValidatorModel):
    SamplingStatisticsDocuments: Sequence[SamplingStatisticsDocumentTypeDef]

class PutTelemetryRecordsRequestRequestTypeDef(BaseValidatorModel):
    TelemetryRecords: Sequence[TelemetryRecordTypeDef]
    EC2InstanceId: Optional[str] = None
    Hostname: Optional[str] = None
    ResourceARN: Optional[str] = None

class GetInsightImpactGraphResultTypeDef(BaseValidatorModel):
    InsightId: str
    StartTime: datetime
    EndTime: datetime
    ServiceGraphStartTime: datetime
    ServiceGraphEndTime: datetime
    Services: List[InsightImpactGraphServiceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResponseTimeRootCauseTypeDef(BaseValidatorModel):
    Services: Optional[List[ResponseTimeRootCauseServiceTypeDef]] = None
    ClientImpacting: Optional[bool] = None

class GetSamplingRulesResultPaginatorTypeDef(BaseValidatorModel):
    SamplingRuleRecords: List[SamplingRuleRecordPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetTracesResultTypeDef(BaseValidatorModel):
    Traces: List[TraceTypeDef]
    UnprocessedTraceIds: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightEventsResultTypeDef(BaseValidatorModel):
    InsightEvents: List[InsightEventTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightSummariesResultTypeDef(BaseValidatorModel):
    InsightSummaries: List[InsightSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightResultTypeDef(BaseValidatorModel):
    Insight: InsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceTypeDef(BaseValidatorModel):
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

class GetTimeSeriesServiceStatisticsResultTypeDef(BaseValidatorModel):
    TimeSeriesServiceStatistics: List[TimeSeriesServiceStatisticsTypeDef]
    ContainsOldGroupVersions: bool
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ErrorRootCauseTypeDef(BaseValidatorModel):
    Services: Optional[List[ErrorRootCauseServiceTypeDef]] = None
    ClientImpacting: Optional[bool] = None

class FaultRootCauseTypeDef(BaseValidatorModel):
    Services: Optional[List[FaultRootCauseServiceTypeDef]] = None
    ClientImpacting: Optional[bool] = None

class GetServiceGraphResultTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    Services: List[ServiceTypeDef]
    ContainsOldGroupVersions: bool
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTraceGraphResultTypeDef(BaseValidatorModel):
    Services: List[ServiceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class GetTraceSummariesResultTypeDef(BaseValidatorModel):
    TraceSummaries: List[TraceSummaryTypeDef]
    ApproximateTime: datetime
    TracesProcessedCount: int
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

