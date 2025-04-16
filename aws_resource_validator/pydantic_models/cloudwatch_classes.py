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
from aws_resource_validator.pydantic_models.cloudwatch_constants import *

class AlarmHistoryItem(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmType: Optional[AlarmTypeType] = None
    Timestamp: Optional[datetime] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    HistorySummary: Optional[str] = None
    HistoryData: Optional[str] = None


class RangeOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime


class Dimension(BaseValidatorModel):
    Name: str
    Value: str


class MetricCharacteristics(BaseValidatorModel):
    PeriodicSpikes: Optional[bool] = None


class CloudwatchEventState(BaseValidatorModel):
    timestamp: str
    value: str
    reason: Optional[str] = None
    reasonData: Optional[str] = None
    actionsSuppressedBy: Optional[str] = None
    actionsSuppressedReason: Optional[str] = None


class CloudwatchEventMetricStatsMetric(BaseValidatorModel):
    metricName: str
    namespace: str
    dimensions: Dict[str, str]


class CompositeAlarm(BaseValidatorModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[List[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[datetime] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    AlarmRule: Optional[str] = None
    InsufficientDataActions: Optional[List[str]] = None
    OKActions: Optional[List[str]] = None
    StateReason: Optional[str] = None
    StateReasonData: Optional[str] = None
    StateUpdatedTimestamp: Optional[datetime] = None
    StateValue: Optional[StateValueType] = None
    StateTransitionedTimestamp: Optional[datetime] = None
    ActionsSuppressedBy: Optional[ActionsSuppressedByType] = None
    ActionsSuppressedReason: Optional[str] = None
    ActionsSuppressor: Optional[str] = None
    ActionsSuppressorWaitPeriod: Optional[int] = None
    ActionsSuppressorExtensionPeriod: Optional[int] = None


class DashboardEntry(BaseValidatorModel):
    DashboardName: Optional[str] = None
    DashboardArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    Size: Optional[int] = None


class DashboardValidationMessage(BaseValidatorModel):
    DataPath: Optional[str] = None
    Message: Optional[str] = None


class Datapoint(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    SampleCount: Optional[float] = None
    Average: Optional[float] = None
    Sum: Optional[float] = None
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None
    Unit: Optional[StandardUnitType] = None
    ExtendedStatistics: Optional[Dict[str, float]] = None


class DeleteAlarmsInput(BaseValidatorModel):
    AlarmNames: Sequence[str]


class DeleteDashboardsInput(BaseValidatorModel):
    DashboardNames: Sequence[str]


class DeleteInsightRulesInput(BaseValidatorModel):
    RuleNames: Sequence[str]


class PartialFailure(BaseValidatorModel):
    FailureResource: Optional[str] = None
    ExceptionType: Optional[str] = None
    FailureCode: Optional[str] = None
    FailureDescription: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteMetricStreamInput(BaseValidatorModel):
    Name: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAlarmsInput(BaseValidatorModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeInsightRulesInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class InsightRule(BaseValidatorModel):
    Name: str
    State: str
    Schema: str
    Definition: str
    ManagedRule: Optional[bool] = None


class DimensionFilter(BaseValidatorModel):
    Name: str
    Value: Optional[str] = None


class DisableAlarmActionsInput(BaseValidatorModel):
    AlarmNames: Sequence[str]


class DisableInsightRulesInput(BaseValidatorModel):
    RuleNames: Sequence[str]


class EnableAlarmActionsInput(BaseValidatorModel):
    AlarmNames: Sequence[str]


class EnableInsightRulesInput(BaseValidatorModel):
    RuleNames: Sequence[str]


class Entity(BaseValidatorModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    Attributes: Optional[Mapping[str, str]] = None


class GetDashboardInput(BaseValidatorModel):
    DashboardName: str


class InsightRuleMetricDatapoint(BaseValidatorModel):
    Timestamp: datetime
    UniqueContributors: Optional[float] = None
    MaxContributorValue: Optional[float] = None
    SampleCount: Optional[float] = None
    Average: Optional[float] = None
    Sum: Optional[float] = None
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None


class LabelOptions(BaseValidatorModel):
    Timezone: Optional[str] = None


class MessageData(BaseValidatorModel):
    Code: Optional[str] = None
    Value: Optional[str] = None


class GetMetricStreamInput(BaseValidatorModel):
    Name: str


class MetricStreamFilterOutput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricNames: Optional[List[str]] = None


class GetMetricWidgetImageInput(BaseValidatorModel):
    MetricWidget: str
    OutputFormat: Optional[str] = None


class InsightRuleContributorDatapoint(BaseValidatorModel):
    Timestamp: datetime
    ApproximateValue: float


class ListDashboardsInput(BaseValidatorModel):
    DashboardNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None


class ListManagedInsightRulesInput(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMetricStreamsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MetricStreamEntry(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastUpdateDate: Optional[datetime] = None
    Name: Optional[str] = None
    FirehoseArn: Optional[str] = None
    State: Optional[str] = None
    OutputFormat: Optional[MetricStreamOutputFormatType] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceARN: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ManagedRuleState(BaseValidatorModel):
    RuleName: str
    State: str


class StatisticSet(BaseValidatorModel):
    SampleCount: float
    Sum: float
    Minimum: float
    Maximum: float


class MetricStreamFilter(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricNames: Optional[Sequence[str]] = None


class MetricStreamStatisticsMetric(BaseValidatorModel):
    Namespace: str
    MetricName: str


class PutDashboardInput(BaseValidatorModel):
    DashboardName: str
    DashboardBody: str


class SetAlarmStateInputAlarmSetState(BaseValidatorModel):
    StateValue: StateValueType
    StateReason: str
    StateReasonData: Optional[str] = None


class SetAlarmStateInput(BaseValidatorModel):
    AlarmName: str
    StateValue: StateValueType
    StateReason: str
    StateReasonData: Optional[str] = None


class StartMetricStreamsInput(BaseValidatorModel):
    Names: Sequence[str]


class StopMetricStreamsInput(BaseValidatorModel):
    Names: Sequence[str]


class UntagResourceInput(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class AnomalyDetectorConfigurationOutput(BaseValidatorModel):
    ExcludedTimeRanges: Optional[List[RangeOutput]] = None
    MetricTimezone: Optional[str] = None


class DescribeAlarmsForMetricInput(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: Optional[StatisticType] = None
    ExtendedStatistic: Optional[str] = None
    Dimensions: Optional[Sequence[Dimension]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None


class DescribeAnomalyDetectorsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[Dimension]] = None
    AnomalyDetectorTypes: Optional[Sequence[AnomalyDetectorTypeType]] = None


class MetricOutput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None


class Metric(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[Dimension]] = None


class SingleMetricAnomalyDetectorOutput(BaseValidatorModel):
    AccountId: Optional[str] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None
    Stat: Optional[str] = None


class SingleMetricAnomalyDetector(BaseValidatorModel):
    AccountId: Optional[str] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[Dimension]] = None
    Stat: Optional[str] = None


class CloudwatchEventMetricStats(BaseValidatorModel):
    period: str
    stat: str
    metric: Optional[CloudwatchEventMetricStatsMetric] = None


class DeleteInsightRulesOutput(BaseValidatorModel):
    Failures: List[PartialFailure]
    ResponseMetadata: ResponseMetadata


class DescribeAlarmHistoryOutput(BaseValidatorModel):
    AlarmHistoryItems: List[AlarmHistoryItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DisableInsightRulesOutput(BaseValidatorModel):
    Failures: List[PartialFailure]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class EnableInsightRulesOutput(BaseValidatorModel):
    Failures: List[PartialFailure]
    ResponseMetadata: ResponseMetadata


class GetDashboardOutput(BaseValidatorModel):
    DashboardArn: str
    DashboardBody: str
    DashboardName: str
    ResponseMetadata: ResponseMetadata


class GetMetricStatisticsOutput(BaseValidatorModel):
    Label: str
    Datapoints: List[Datapoint]
    ResponseMetadata: ResponseMetadata


class GetMetricWidgetImageOutput(BaseValidatorModel):
    MetricWidgetImage: bytes
    ResponseMetadata: ResponseMetadata


class ListDashboardsOutput(BaseValidatorModel):
    DashboardEntries: List[DashboardEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutDashboardOutput(BaseValidatorModel):
    DashboardValidationMessages: List[DashboardValidationMessage]
    ResponseMetadata: ResponseMetadata


class PutManagedInsightRulesOutput(BaseValidatorModel):
    Failures: List[PartialFailure]
    ResponseMetadata: ResponseMetadata


class PutMetricStreamOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class DescribeAlarmHistoryInputAlarmDescribeHistory(BaseValidatorModel):
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[Timestamp] = None
    EndDate: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None


class DescribeAlarmHistoryInput(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[Timestamp] = None
    EndDate: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None


class GetInsightRuleReportInput(BaseValidatorModel):
    RuleName: str
    StartTime: Timestamp
    EndTime: Timestamp
    Period: int
    MaxContributorCount: Optional[int] = None
    Metrics: Optional[Sequence[str]] = None
    OrderBy: Optional[str] = None


class GetMetricStatisticsInputMetricGetStatistics(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    Period: int
    Dimensions: Optional[Sequence[Dimension]] = None
    Statistics: Optional[Sequence[StatisticType]] = None
    ExtendedStatistics: Optional[Sequence[str]] = None
    Unit: Optional[StandardUnitType] = None


class GetMetricStatisticsInput(BaseValidatorModel):
    Namespace: str
    MetricName: str
    StartTime: Timestamp
    EndTime: Timestamp
    Period: int
    Dimensions: Optional[Sequence[Dimension]] = None
    Statistics: Optional[Sequence[StatisticType]] = None
    ExtendedStatistics: Optional[Sequence[str]] = None
    Unit: Optional[StandardUnitType] = None


class Range(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp


class DescribeAlarmHistoryInputPaginate(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[Timestamp] = None
    EndDate: Optional[Timestamp] = None
    ScanBy: Optional[ScanByType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAlarmsInputPaginate(BaseValidatorModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAnomalyDetectorsInputPaginate(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[Dimension]] = None
    AnomalyDetectorTypes: Optional[Sequence[AnomalyDetectorTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDashboardsInputPaginate(BaseValidatorModel):
    DashboardNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAlarmsInputWaitExtra(BaseValidatorModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeAlarmsInputWait(BaseValidatorModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInsightRulesOutput(BaseValidatorModel):
    InsightRules: List[InsightRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMetricsInputPaginate(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionFilter]] = None
    RecentlyActive: Optional[Literal["PT3H"]] = None
    IncludeLinkedAccounts: Optional[bool] = None
    OwningAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMetricsInput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionFilter]] = None
    NextToken: Optional[str] = None
    RecentlyActive: Optional[Literal["PT3H"]] = None
    IncludeLinkedAccounts: Optional[bool] = None
    OwningAccount: Optional[str] = None


class MetricDataResult(BaseValidatorModel):
    Id: Optional[str] = None
    Label: Optional[str] = None
    Timestamps: Optional[List[datetime]] = None
    Values: Optional[List[float]] = None
    StatusCode: Optional[StatusCodeType] = None
    Messages: Optional[List[MessageData]] = None


class InsightRuleContributor(BaseValidatorModel):
    Keys: List[str]
    ApproximateAggregateValue: float
    Datapoints: List[InsightRuleContributorDatapoint]


class ListMetricStreamsOutput(BaseValidatorModel):
    Entries: List[MetricStreamEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ManagedRule(BaseValidatorModel):
    TemplateName: str
    ResourceARN: str
    Tags: Optional[Sequence[Tag]] = None


class PutCompositeAlarmInput(BaseValidatorModel):
    AlarmName: str
    AlarmRule: str
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[Sequence[str]] = None
    AlarmDescription: Optional[str] = None
    InsufficientDataActions: Optional[Sequence[str]] = None
    OKActions: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None
    ActionsSuppressor: Optional[str] = None
    ActionsSuppressorWaitPeriod: Optional[int] = None
    ActionsSuppressorExtensionPeriod: Optional[int] = None


class PutInsightRuleInput(BaseValidatorModel):
    RuleName: str
    RuleDefinition: str
    RuleState: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class TagResourceInput(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class ManagedRuleDescription(BaseValidatorModel):
    TemplateName: Optional[str] = None
    ResourceARN: Optional[str] = None
    RuleState: Optional[ManagedRuleState] = None


class MetricDatum(BaseValidatorModel):
    MetricName: str
    Dimensions: Optional[Sequence[Dimension]] = None
    Timestamp: Optional[Timestamp] = None
    Value: Optional[float] = None
    StatisticValues: Optional[StatisticSet] = None
    Values: Optional[Sequence[float]] = None
    Counts: Optional[Sequence[float]] = None
    Unit: Optional[StandardUnitType] = None
    StorageResolution: Optional[int] = None


class MetricStreamStatisticsConfigurationOutput(BaseValidatorModel):
    IncludeMetrics: List[MetricStreamStatisticsMetric]
    AdditionalStatistics: List[str]


class MetricStreamStatisticsConfiguration(BaseValidatorModel):
    IncludeMetrics: Sequence[MetricStreamStatisticsMetric]
    AdditionalStatistics: Sequence[str]


class ListMetricsOutput(BaseValidatorModel):
    Metrics: List[MetricOutput]
    OwningAccounts: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MetricStatOutput(BaseValidatorModel):
    Metric: MetricOutput
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class AnomalyDetectorConfiguration(BaseValidatorModel):
    ExcludedTimeRanges: Optional[Sequence[Range]] = None
    MetricTimezone: Optional[str] = None


class GetMetricDataOutput(BaseValidatorModel):
    MetricDataResults: List[MetricDataResult]
    Messages: List[MessageData]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetInsightRuleReportOutput(BaseValidatorModel):
    KeyLabels: List[str]
    AggregationStatistic: str
    AggregateValue: float
    ApproximateUniqueCount: int
    Contributors: List[InsightRuleContributor]
    MetricDatapoints: List[InsightRuleMetricDatapoint]
    ResponseMetadata: ResponseMetadata


class PutManagedInsightRulesInput(BaseValidatorModel):
    ManagedRules: Sequence[ManagedRule]


class ListManagedInsightRulesOutput(BaseValidatorModel):
    ManagedRules: List[ManagedRuleDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EntityMetricData(BaseValidatorModel):
    Entity: Optional[Entity] = None
    MetricData: Optional[Sequence[MetricDatum]] = None


class GetMetricStreamOutput(BaseValidatorModel):
    Arn: str
    Name: str
    IncludeFilters: List[MetricStreamFilterOutput]
    ExcludeFilters: List[MetricStreamFilterOutput]
    FirehoseArn: str
    RoleArn: str
    State: str
    CreationDate: datetime
    LastUpdateDate: datetime
    OutputFormat: MetricStreamOutputFormatType
    StatisticsConfigurations: List[MetricStreamStatisticsConfigurationOutput]
    IncludeLinkedAccountsMetrics: bool
    ResponseMetadata: ResponseMetadata


class MetricDataQueryOutput(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatOutput] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


class MetricUnion(BaseValidatorModel):
    pass


class MetricStat(BaseValidatorModel):
    Metric: MetricUnion
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class PutMetricDataInputMetricPutData(BaseValidatorModel):
    EntityMetricData: Optional[Sequence[EntityMetricData]] = None
    StrictEntityValidation: Optional[bool] = None


class PutMetricDataInput(BaseValidatorModel):
    Namespace: str
    MetricData: Optional[Sequence[MetricDatum]] = None
    EntityMetricData: Optional[Sequence[EntityMetricData]] = None
    StrictEntityValidation: Optional[bool] = None


class MetricStreamStatisticsConfigurationUnion(BaseValidatorModel):
    pass


class MetricStreamFilterUnion(BaseValidatorModel):
    pass


class PutMetricStreamInput(BaseValidatorModel):
    Name: str
    FirehoseArn: str
    RoleArn: str
    OutputFormat: MetricStreamOutputFormatType
    IncludeFilters: Optional[Sequence[MetricStreamFilterUnion]] = None
    ExcludeFilters: Optional[Sequence[MetricStreamFilterUnion]] = None
    Tags: Optional[Sequence[Tag]] = None
    StatisticsConfigurations: Optional[Sequence[MetricStreamStatisticsConfigurationUnion]] = None
    IncludeLinkedAccountsMetrics: Optional[bool] = None


class MetricAlarm(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmArn: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[datetime] = None
    ActionsEnabled: Optional[bool] = None
    OKActions: Optional[List[str]] = None
    AlarmActions: Optional[List[str]] = None
    InsufficientDataActions: Optional[List[str]] = None
    StateValue: Optional[StateValueType] = None
    StateReason: Optional[str] = None
    StateReasonData: Optional[str] = None
    StateUpdatedTimestamp: Optional[datetime] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None
    ExtendedStatistic: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None
    EvaluationPeriods: Optional[int] = None
    DatapointsToAlarm: Optional[int] = None
    Threshold: Optional[float] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    TreatMissingData: Optional[str] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    Metrics: Optional[List[MetricDataQueryOutput]] = None
    ThresholdMetricId: Optional[str] = None
    EvaluationState: Optional[Literal["PARTIAL_DATA"]] = None
    StateTransitionedTimestamp: Optional[datetime] = None


class MetricMathAnomalyDetectorOutput(BaseValidatorModel):
    MetricDataQueries: Optional[List[MetricDataQueryOutput]] = None


class CloudwatchEventDetailConfiguration(BaseValidatorModel):
    pass


class CloudwatchEventDetail(BaseValidatorModel):
    alarmName: str
    state: CloudwatchEventState
    operation: Optional[str] = None
    configuration: Optional[CloudwatchEventDetailConfiguration] = None
    previousConfiguration: Optional[CloudwatchEventDetailConfiguration] = None
    previousState: Optional[CloudwatchEventState] = None


class DescribeAlarmsForMetricOutput(BaseValidatorModel):
    MetricAlarms: List[MetricAlarm]
    ResponseMetadata: ResponseMetadata


class DescribeAlarmsOutput(BaseValidatorModel):
    CompositeAlarms: List[CompositeAlarm]
    MetricAlarms: List[MetricAlarm]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MetricStatAlarm(BaseValidatorModel):
    Metric: MetricAlarm
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class AnomalyDetector(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None
    Stat: Optional[str] = None
    Configuration: Optional[AnomalyDetectorConfigurationOutput] = None
    StateValue: Optional[AnomalyDetectorStateValueType] = None
    MetricCharacteristics: Optional[MetricCharacteristics] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorOutput] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorOutput] = None


class MetricStatUnion(BaseValidatorModel):
    pass


class MetricDataQuery(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatUnion] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


class MetricDataQueryAlarm(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatAlarm] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


class DescribeAnomalyDetectorsOutput(BaseValidatorModel):
    AnomalyDetectors: List[AnomalyDetector]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MetricMathAnomalyDetector(BaseValidatorModel):
    MetricDataQueries: Optional[Sequence[MetricDataQuery]] = None


class MetricDataQueryUnion(BaseValidatorModel):
    pass


class GetMetricDataInputPaginate(BaseValidatorModel):
    MetricDataQueries: Sequence[MetricDataQueryUnion]
    StartTime: Timestamp
    EndTime: Timestamp
    ScanBy: Optional[ScanByType] = None
    LabelOptions: Optional[LabelOptions] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetMetricDataInput(BaseValidatorModel):
    MetricDataQueries: Sequence[MetricDataQueryUnion]
    StartTime: Timestamp
    EndTime: Timestamp
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None
    MaxDatapoints: Optional[int] = None
    LabelOptions: Optional[LabelOptions] = None


class PutMetricAlarmInputMetricPutAlarm(BaseValidatorModel):
    AlarmName: str
    EvaluationPeriods: int
    ComparisonOperator: ComparisonOperatorType
    AlarmDescription: Optional[str] = None
    ActionsEnabled: Optional[bool] = None
    OKActions: Optional[Sequence[str]] = None
    AlarmActions: Optional[Sequence[str]] = None
    InsufficientDataActions: Optional[Sequence[str]] = None
    Statistic: Optional[StatisticType] = None
    ExtendedStatistic: Optional[str] = None
    Dimensions: Optional[Sequence[Dimension]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None
    DatapointsToAlarm: Optional[int] = None
    Threshold: Optional[float] = None
    TreatMissingData: Optional[str] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    Metrics: Optional[Sequence[MetricDataQueryUnion]] = None
    Tags: Optional[Sequence[Tag]] = None
    ThresholdMetricId: Optional[str] = None


class PutMetricAlarmInput(BaseValidatorModel):
    AlarmName: str
    EvaluationPeriods: int
    ComparisonOperator: ComparisonOperatorType
    AlarmDescription: Optional[str] = None
    ActionsEnabled: Optional[bool] = None
    OKActions: Optional[Sequence[str]] = None
    AlarmActions: Optional[Sequence[str]] = None
    InsufficientDataActions: Optional[Sequence[str]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None
    ExtendedStatistic: Optional[str] = None
    Dimensions: Optional[Sequence[Dimension]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None
    DatapointsToAlarm: Optional[int] = None
    Threshold: Optional[float] = None
    TreatMissingData: Optional[str] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    Metrics: Optional[Sequence[MetricDataQueryUnion]] = None
    Tags: Optional[Sequence[Tag]] = None
    ThresholdMetricId: Optional[str] = None


class SingleMetricAnomalyDetectorUnion(BaseValidatorModel):
    pass


class MetricMathAnomalyDetectorUnion(BaseValidatorModel):
    pass


class DeleteAnomalyDetectorInput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[Dimension]] = None
    Stat: Optional[str] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorUnion] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorUnion] = None


class AnomalyDetectorConfigurationUnion(BaseValidatorModel):
    pass


class PutAnomalyDetectorInput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[Dimension]] = None
    Stat: Optional[str] = None
    Configuration: Optional[AnomalyDetectorConfigurationUnion] = None
    MetricCharacteristics: Optional[MetricCharacteristics] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorUnion] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorUnion] = None


