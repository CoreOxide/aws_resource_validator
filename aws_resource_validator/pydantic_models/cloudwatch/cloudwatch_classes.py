from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


# This class is the input for the 'delete_alarms' function.
class DeleteAlarmsInput(BaseValidatorModel):
    AlarmNames: List[str]


class DeleteDashboardsInput(BaseValidatorModel):
    DashboardNames: List[str]


# This class is the input for the 'delete_insight_rules' function.
class DeleteInsightRulesInput(BaseValidatorModel):
    RuleNames: List[str]


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

Timestamp = Union[datetime, str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_alarms' function.
class DescribeAlarmsInput(BaseValidatorModel):
    AlarmNames: Optional[List[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[List[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_insight_rules' function.
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


# This class is the input for the 'disable_alarm_actions' function.
class DisableAlarmActionsInput(BaseValidatorModel):
    AlarmNames: List[str]


# This class is the input for the 'disable_insight_rules' function.
class DisableInsightRulesInput(BaseValidatorModel):
    RuleNames: List[str]


# This class is the input for the 'enable_alarm_actions' function.
class EnableAlarmActionsInput(BaseValidatorModel):
    AlarmNames: List[str]


# This class is the input for the 'enable_insight_rules' function.
class EnableInsightRulesInput(BaseValidatorModel):
    RuleNames: List[str]


class Entity(BaseValidatorModel):
    KeyAttributes: Optional[Dict[str, str]] = None
    Attributes: Optional[Dict[str, str]] = None


# This class is the input for the 'get_dashboard' function.
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


# This class is the input for the 'get_metric_stream' function.
class GetMetricStreamInput(BaseValidatorModel):
    Name: str


class MetricStreamFilterOutput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricNames: Optional[List[str]] = None


# This class is the input for the 'get_metric_widget_image' function.
class GetMetricWidgetImageInput(BaseValidatorModel):
    MetricWidget: str
    OutputFormat: Optional[str] = None


class InsightRuleContributorDatapoint(BaseValidatorModel):
    Timestamp: datetime
    ApproximateValue: float


# This class is the input for the 'list_dashboards' function.
class ListDashboardsInput(BaseValidatorModel):
    DashboardNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_managed_insight_rules' function.
class ListManagedInsightRulesInput(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_metric_streams' function.
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


# This class is the input for the 'list_tags_for_resource' function.
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
    MetricNames: Optional[List[str]] = None


class MetricStreamStatisticsMetric(BaseValidatorModel):
    Namespace: str
    MetricName: str


# This class is the input for the 'put_dashboard' function.
class PutDashboardInput(BaseValidatorModel):
    DashboardName: str
    DashboardBody: str


class SetAlarmStateInputAlarmSetState(BaseValidatorModel):
    StateValue: StateValueType
    StateReason: str
    StateReasonData: Optional[str] = None


# This class is the input for the 'set_alarm_state' function.
class SetAlarmStateInput(BaseValidatorModel):
    AlarmName: str
    StateValue: StateValueType
    StateReason: str
    StateReasonData: Optional[str] = None


class StartMetricStreamsInput(BaseValidatorModel):
    Names: List[str]


class StopMetricStreamsInput(BaseValidatorModel):
    Names: List[str]


class UntagResourceInput(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class AnomalyDetectorConfigurationOutput(BaseValidatorModel):
    ExcludedTimeRanges: Optional[List[RangeOutput]] = None
    MetricTimezone: Optional[str] = None


# This class is the input for the 'describe_alarms_for_metric' function.
class DescribeAlarmsForMetricInput(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: Optional[StatisticType] = None
    ExtendedStatistic: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None


# This class is the input for the 'describe_anomaly_detectors' function.
class DescribeAnomalyDetectorsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None
    AnomalyDetectorTypes: Optional[List[AnomalyDetectorTypeType]] = None


class MetricOutput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None


class Metric(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None


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
    Dimensions: Optional[List[Dimension]] = None
    Stat: Optional[str] = None


class CloudwatchEventMetricStats(BaseValidatorModel):
    period: str
    stat: str
    metric: Optional[CloudwatchEventMetricStatsMetric] = None


# This class is the output for the 'delete_insight_rules' function.
class DeleteInsightRulesOutput(BaseValidatorModel):
    Failures: List[PartialFailure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_alarm_history' function.
class DescribeAlarmHistoryOutput(BaseValidatorModel):
    AlarmHistoryItems: List[AlarmHistoryItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'disable_insight_rules' function.
class DisableInsightRulesOutput(BaseValidatorModel):
    Failures: List[PartialFailure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_alarm_state' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_insight_rules' function.
class EnableInsightRulesOutput(BaseValidatorModel):
    Failures: List[PartialFailure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_dashboard' function.
class GetDashboardOutput(BaseValidatorModel):
    DashboardArn: str
    DashboardBody: str
    DashboardName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_metric_statistics' function.
class GetMetricStatisticsOutput(BaseValidatorModel):
    Label: str
    Datapoints: List[Datapoint]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_metric_widget_image' function.
class GetMetricWidgetImageOutput(BaseValidatorModel):
    MetricWidgetImage: bytes
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_dashboards' function.
class ListDashboardsOutput(BaseValidatorModel):
    DashboardEntries: List[DashboardEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_dashboard' function.
class PutDashboardOutput(BaseValidatorModel):
    DashboardValidationMessages: List[DashboardValidationMessage]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_managed_insight_rules' function.
class PutManagedInsightRulesOutput(BaseValidatorModel):
    Failures: List[PartialFailure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_metric_stream' function.
class PutMetricStreamOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class DescribeAlarmHistoryInputAlarmDescribeHistory(BaseValidatorModel):
    AlarmTypes: Optional[List[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[Timestamp] = None
    EndDate: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None


# This class is the input for the 'describe_alarm_history' function.
class DescribeAlarmHistoryInput(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmTypes: Optional[List[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[Timestamp] = None
    EndDate: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None


# This class is the input for the 'get_insight_rule_report' function.
class GetInsightRuleReportInput(BaseValidatorModel):
    RuleName: str
    StartTime: Timestamp
    EndTime: Timestamp
    Period: int
    MaxContributorCount: Optional[int] = None
    Metrics: Optional[List[str]] = None
    OrderBy: Optional[str] = None


class GetMetricStatisticsInputMetricGetStatistics(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    Period: int
    Dimensions: Optional[List[Dimension]] = None
    Statistics: Optional[List[StatisticType]] = None
    ExtendedStatistics: Optional[List[str]] = None
    Unit: Optional[StandardUnitType] = None


# This class is the input for the 'get_metric_statistics' function.
class GetMetricStatisticsInput(BaseValidatorModel):
    Namespace: str
    MetricName: str
    StartTime: Timestamp
    EndTime: Timestamp
    Period: int
    Dimensions: Optional[List[Dimension]] = None
    Statistics: Optional[List[StatisticType]] = None
    ExtendedStatistics: Optional[List[str]] = None
    Unit: Optional[StandardUnitType] = None


class Range(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp


class DescribeAlarmHistoryInputPaginate(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmTypes: Optional[List[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[Timestamp] = None
    EndDate: Optional[Timestamp] = None
    ScanBy: Optional[ScanByType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAlarmsInputPaginate(BaseValidatorModel):
    AlarmNames: Optional[List[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[List[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAnomalyDetectorsInputPaginate(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None
    AnomalyDetectorTypes: Optional[List[AnomalyDetectorTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDashboardsInputPaginate(BaseValidatorModel):
    DashboardNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAlarmsInputWaitExtra(BaseValidatorModel):
    AlarmNames: Optional[List[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[List[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeAlarmsInputWait(BaseValidatorModel):
    AlarmNames: Optional[List[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[List[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'describe_insight_rules' function.
class DescribeInsightRulesOutput(BaseValidatorModel):
    InsightRules: List[InsightRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMetricsInputPaginate(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionFilter]] = None
    RecentlyActive: Optional[Literal['PT3H']] = None
    IncludeLinkedAccounts: Optional[bool] = None
    OwningAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_metrics' function.
class ListMetricsInput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionFilter]] = None
    NextToken: Optional[str] = None
    RecentlyActive: Optional[Literal['PT3H']] = None
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


# This class is the output for the 'list_metric_streams' function.
class ListMetricStreamsOutput(BaseValidatorModel):
    Entries: List[MetricStreamEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ManagedRule(BaseValidatorModel):
    TemplateName: str
    ResourceARN: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'put_composite_alarm' function.
class PutCompositeAlarmInput(BaseValidatorModel):
    AlarmName: str
    AlarmRule: str
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[List[str]] = None
    AlarmDescription: Optional[str] = None
    InsufficientDataActions: Optional[List[str]] = None
    OKActions: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    ActionsSuppressor: Optional[str] = None
    ActionsSuppressorWaitPeriod: Optional[int] = None
    ActionsSuppressorExtensionPeriod: Optional[int] = None


class PutInsightRuleInput(BaseValidatorModel):
    RuleName: str
    RuleDefinition: str
    RuleState: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagResourceInput(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class ManagedRuleDescription(BaseValidatorModel):
    TemplateName: Optional[str] = None
    ResourceARN: Optional[str] = None
    RuleState: Optional[ManagedRuleState] = None


class MetricDatum(BaseValidatorModel):
    MetricName: str
    Dimensions: Optional[List[Dimension]] = None
    Timestamp: Optional[Timestamp] = None
    Value: Optional[float] = None
    StatisticValues: Optional[StatisticSet] = None
    Values: Optional[List[float]] = None
    Counts: Optional[List[float]] = None
    Unit: Optional[StandardUnitType] = None
    StorageResolution: Optional[int] = None

MetricStreamFilterUnion = Union[MetricStreamFilter, MetricStreamFilterOutput]


class MetricStreamStatisticsConfigurationOutput(BaseValidatorModel):
    IncludeMetrics: List[MetricStreamStatisticsMetric]
    AdditionalStatistics: List[str]


class MetricStreamStatisticsConfiguration(BaseValidatorModel):
    IncludeMetrics: List[MetricStreamStatisticsMetric]
    AdditionalStatistics: List[str]


# This class is the output for the 'list_metrics' function.
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

MetricUnion = Union[Metric, MetricOutput]

SingleMetricAnomalyDetectorUnion = Union[SingleMetricAnomalyDetector, SingleMetricAnomalyDetectorOutput]


class CloudwatchEventMetric(BaseValidatorModel):
    id: str
    returnData: bool
    metricStat: Optional[CloudwatchEventMetricStats] = None
    expression: Optional[str] = None
    label: Optional[str] = None
    period: Optional[int] = None


class AnomalyDetectorConfiguration(BaseValidatorModel):
    ExcludedTimeRanges: Optional[List[Range]] = None
    MetricTimezone: Optional[str] = None


# This class is the output for the 'get_metric_data' function.
class GetMetricDataOutput(BaseValidatorModel):
    MetricDataResults: List[MetricDataResult]
    Messages: List[MessageData]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_insight_rule_report' function.
class GetInsightRuleReportOutput(BaseValidatorModel):
    KeyLabels: List[str]
    AggregationStatistic: str
    AggregateValue: float
    ApproximateUniqueCount: int
    Contributors: List[InsightRuleContributor]
    MetricDatapoints: List[InsightRuleMetricDatapoint]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_managed_insight_rules' function.
class PutManagedInsightRulesInput(BaseValidatorModel):
    ManagedRules: List[ManagedRule]


# This class is the output for the 'list_managed_insight_rules' function.
class ListManagedInsightRulesOutput(BaseValidatorModel):
    ManagedRules: List[ManagedRuleDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EntityMetricData(BaseValidatorModel):
    Entity: Optional[Entity] = None
    MetricData: Optional[List[MetricDatum]] = None


# This class is the output for the 'get_metric_stream' function.
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

MetricStreamStatisticsConfigurationUnion = Union[MetricStreamStatisticsConfiguration, MetricStreamStatisticsConfigurationOutput]


class MetricDataQueryOutput(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatOutput] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


class MetricStat(BaseValidatorModel):
    Metric: MetricUnion
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class CloudwatchEventDetailConfiguration(BaseValidatorModel):
    id: Optional[str] = None
    description: Optional[str] = None
    metrics: Optional[List[CloudwatchEventMetric]] = None
    actionsSuppressor: Optional[str] = None
    actionsSuppressorWaitPeriod: Optional[int] = None
    actionsSuppressorExtensionPeriod: Optional[int] = None
    threshold: Optional[int] = None
    evaluationPeriods: Optional[int] = None
    alarmRule: Optional[str] = None
    alarmName: Optional[str] = None
    treatMissingData: Optional[str] = None
    comparisonOperator: Optional[str] = None
    timestamp: Optional[str] = None
    actionsEnabled: Optional[bool] = None
    okActions: Optional[List[str]] = None
    alarmActions: Optional[List[str]] = None
    insufficientDataActions: Optional[List[str]] = None

AnomalyDetectorConfigurationUnion = Union[AnomalyDetectorConfiguration, AnomalyDetectorConfigurationOutput]


class PutMetricDataInputMetricPutData(BaseValidatorModel):
    EntityMetricData: Optional[List[EntityMetricData]] = None
    StrictEntityValidation: Optional[bool] = None


# This class is the input for the 'put_metric_data' function.
class PutMetricDataInput(BaseValidatorModel):
    Namespace: str
    MetricData: Optional[List[MetricDatum]] = None
    EntityMetricData: Optional[List[EntityMetricData]] = None
    StrictEntityValidation: Optional[bool] = None


# This class is the input for the 'put_metric_stream' function.
class PutMetricStreamInput(BaseValidatorModel):
    Name: str
    FirehoseArn: str
    RoleArn: str
    OutputFormat: MetricStreamOutputFormatType
    IncludeFilters: Optional[List[MetricStreamFilterUnion]] = None
    ExcludeFilters: Optional[List[MetricStreamFilterUnion]] = None
    Tags: Optional[List[Tag]] = None
    StatisticsConfigurations: Optional[List[MetricStreamStatisticsConfigurationUnion]] = None
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
    EvaluationState: Optional[Literal['PARTIAL_DATA']] = None
    StateTransitionedTimestamp: Optional[datetime] = None


class MetricMathAnomalyDetectorOutput(BaseValidatorModel):
    MetricDataQueries: Optional[List[MetricDataQueryOutput]] = None

MetricStatUnion = Union[MetricStat, MetricStatOutput]


class CloudwatchEventDetail(BaseValidatorModel):
    alarmName: str
    state: CloudwatchEventState
    operation: Optional[str] = None
    configuration: Optional[CloudwatchEventDetailConfiguration] = None
    previousConfiguration: Optional[CloudwatchEventDetailConfiguration] = None
    previousState: Optional[CloudwatchEventState] = None


# This class is the output for the 'describe_alarms_for_metric' function.
class DescribeAlarmsForMetricOutput(BaseValidatorModel):
    MetricAlarms: List[MetricAlarm]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_alarms' function.
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


class MetricDataQuery(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatUnion] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


class CloudwatchEvent(BaseValidatorModel):
    version: str
    id: str
    detail_type: str
    source: str
    account: str
    time: str
    region: str
    resources: List[str]
    detail: CloudwatchEventDetail


class MetricDataQueryAlarm(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatAlarm] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


# This class is the output for the 'describe_anomaly_detectors' function.
class DescribeAnomalyDetectorsOutput(BaseValidatorModel):
    AnomalyDetectors: List[AnomalyDetector]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

MetricDataQueryUnion = Union[MetricDataQuery, MetricDataQueryOutput]


class MetricMathAnomalyDetector(BaseValidatorModel):
    MetricDataQueries: Optional[List[MetricDataQuery]] = None


class GetMetricDataInputPaginate(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryUnion]
    StartTime: Timestamp
    EndTime: Timestamp
    ScanBy: Optional[ScanByType] = None
    LabelOptions: Optional[LabelOptions] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_metric_data' function.
class GetMetricDataInput(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryUnion]
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
    OKActions: Optional[List[str]] = None
    AlarmActions: Optional[List[str]] = None
    InsufficientDataActions: Optional[List[str]] = None
    Statistic: Optional[StatisticType] = None
    ExtendedStatistic: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None
    DatapointsToAlarm: Optional[int] = None
    Threshold: Optional[float] = None
    TreatMissingData: Optional[str] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    Metrics: Optional[List[MetricDataQueryUnion]] = None
    Tags: Optional[List[Tag]] = None
    ThresholdMetricId: Optional[str] = None


# This class is the input for the 'put_metric_alarm' function.
class PutMetricAlarmInput(BaseValidatorModel):
    AlarmName: str
    EvaluationPeriods: int
    ComparisonOperator: ComparisonOperatorType
    AlarmDescription: Optional[str] = None
    ActionsEnabled: Optional[bool] = None
    OKActions: Optional[List[str]] = None
    AlarmActions: Optional[List[str]] = None
    InsufficientDataActions: Optional[List[str]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Statistic: Optional[StatisticType] = None
    ExtendedStatistic: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None
    DatapointsToAlarm: Optional[int] = None
    Threshold: Optional[float] = None
    TreatMissingData: Optional[str] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    Metrics: Optional[List[MetricDataQueryUnion]] = None
    Tags: Optional[List[Tag]] = None
    ThresholdMetricId: Optional[str] = None

MetricMathAnomalyDetectorUnion = Union[MetricMathAnomalyDetector, MetricMathAnomalyDetectorOutput]


class DeleteAnomalyDetectorInput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None
    Stat: Optional[str] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorUnion] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorUnion] = None


class PutAnomalyDetectorInput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None
    Stat: Optional[str] = None
    Configuration: Optional[AnomalyDetectorConfigurationUnion] = None
    MetricCharacteristics: Optional[MetricCharacteristics] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorUnion] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorUnion] = None