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

class AlarmHistoryItemTypeDef(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmType: Optional[AlarmTypeType] = None
    Timestamp: Optional[datetime] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    HistorySummary: Optional[str] = None
    HistoryData: Optional[str] = None


class RangeOutputTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime


class DimensionTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class MetricCharacteristicsTypeDef(BaseValidatorModel):
    PeriodicSpikes: Optional[bool] = None


class CloudwatchEventStateTypeDef(BaseValidatorModel):
    timestamp: str
    value: str
    reason: Optional[str] = None
    reasonData: Optional[str] = None
    actionsSuppressedBy: Optional[str] = None
    actionsSuppressedReason: Optional[str] = None


class CloudwatchEventMetricStatsMetricTypeDef(BaseValidatorModel):
    metricName: str
    namespace: str
    dimensions: Dict[str, str]


class CompositeAlarmTypeDef(BaseValidatorModel):
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


class DashboardEntryTypeDef(BaseValidatorModel):
    DashboardName: Optional[str] = None
    DashboardArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    Size: Optional[int] = None


class DashboardValidationMessageTypeDef(BaseValidatorModel):
    DataPath: Optional[str] = None
    Message: Optional[str] = None


class DatapointTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    SampleCount: Optional[float] = None
    Average: Optional[float] = None
    Sum: Optional[float] = None
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None
    Unit: Optional[StandardUnitType] = None
    ExtendedStatistics: Optional[Dict[str, float]] = None


class DeleteAlarmsInputTypeDef(BaseValidatorModel):
    AlarmNames: Sequence[str]


class DeleteDashboardsInputTypeDef(BaseValidatorModel):
    DashboardNames: Sequence[str]


class DeleteInsightRulesInputTypeDef(BaseValidatorModel):
    RuleNames: Sequence[str]


class PartialFailureTypeDef(BaseValidatorModel):
    FailureResource: Optional[str] = None
    ExceptionType: Optional[str] = None
    FailureCode: Optional[str] = None
    FailureDescription: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteMetricStreamInputTypeDef(BaseValidatorModel):
    Name: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAlarmsInputTypeDef(BaseValidatorModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeInsightRulesInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class InsightRuleTypeDef(BaseValidatorModel):
    Name: str
    State: str
    Schema: str
    Definition: str
    ManagedRule: Optional[bool] = None


class DimensionFilterTypeDef(BaseValidatorModel):
    Name: str
    Value: Optional[str] = None


class DisableAlarmActionsInputTypeDef(BaseValidatorModel):
    AlarmNames: Sequence[str]


class DisableInsightRulesInputTypeDef(BaseValidatorModel):
    RuleNames: Sequence[str]


class EnableAlarmActionsInputTypeDef(BaseValidatorModel):
    AlarmNames: Sequence[str]


class EnableInsightRulesInputTypeDef(BaseValidatorModel):
    RuleNames: Sequence[str]


class EntityTypeDef(BaseValidatorModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    Attributes: Optional[Mapping[str, str]] = None


class GetDashboardInputTypeDef(BaseValidatorModel):
    DashboardName: str


class InsightRuleMetricDatapointTypeDef(BaseValidatorModel):
    Timestamp: datetime
    UniqueContributors: Optional[float] = None
    MaxContributorValue: Optional[float] = None
    SampleCount: Optional[float] = None
    Average: Optional[float] = None
    Sum: Optional[float] = None
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None


class LabelOptionsTypeDef(BaseValidatorModel):
    Timezone: Optional[str] = None


class MessageDataTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Value: Optional[str] = None


class GetMetricStreamInputTypeDef(BaseValidatorModel):
    Name: str


class MetricStreamFilterOutputTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricNames: Optional[List[str]] = None


class GetMetricWidgetImageInputTypeDef(BaseValidatorModel):
    MetricWidget: str
    OutputFormat: Optional[str] = None


class InsightRuleContributorDatapointTypeDef(BaseValidatorModel):
    Timestamp: datetime
    ApproximateValue: float


class ListDashboardsInputTypeDef(BaseValidatorModel):
    DashboardNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None


class ListManagedInsightRulesInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMetricStreamsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MetricStreamEntryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastUpdateDate: Optional[datetime] = None
    Name: Optional[str] = None
    FirehoseArn: Optional[str] = None
    State: Optional[str] = None
    OutputFormat: Optional[MetricStreamOutputFormatType] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    ResourceARN: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ManagedRuleStateTypeDef(BaseValidatorModel):
    RuleName: str
    State: str


class StatisticSetTypeDef(BaseValidatorModel):
    SampleCount: float
    Sum: float
    Minimum: float
    Maximum: float


class MetricStreamFilterTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricNames: Optional[Sequence[str]] = None


class MetricStreamStatisticsMetricTypeDef(BaseValidatorModel):
    Namespace: str
    MetricName: str


class PutDashboardInputTypeDef(BaseValidatorModel):
    DashboardName: str
    DashboardBody: str


class SetAlarmStateInputAlarmSetStateTypeDef(BaseValidatorModel):
    StateValue: StateValueType
    StateReason: str
    StateReasonData: Optional[str] = None


class SetAlarmStateInputTypeDef(BaseValidatorModel):
    AlarmName: str
    StateValue: StateValueType
    StateReason: str
    StateReasonData: Optional[str] = None


class StartMetricStreamsInputTypeDef(BaseValidatorModel):
    Names: Sequence[str]


class StopMetricStreamsInputTypeDef(BaseValidatorModel):
    Names: Sequence[str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class AnomalyDetectorConfigurationOutputTypeDef(BaseValidatorModel):
    ExcludedTimeRanges: Optional[List[RangeOutputTypeDef]] = None
    MetricTimezone: Optional[str] = None


class DescribeAlarmsForMetricInputTypeDef(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: Optional[StatisticType] = None
    ExtendedStatistic: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None


class DescribeAnomalyDetectorsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    AnomalyDetectorTypes: Optional[Sequence[AnomalyDetectorTypeType]] = None


class MetricOutputTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None


class MetricTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None


class SingleMetricAnomalyDetectorOutputTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None
    Stat: Optional[str] = None


class SingleMetricAnomalyDetectorTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Stat: Optional[str] = None


class CloudwatchEventMetricStatsTypeDef(BaseValidatorModel):
    period: str
    stat: str
    metric: Optional[CloudwatchEventMetricStatsMetricTypeDef] = None


class DeleteInsightRulesOutputTypeDef(BaseValidatorModel):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAlarmHistoryOutputTypeDef(BaseValidatorModel):
    AlarmHistoryItems: List[AlarmHistoryItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DisableInsightRulesOutputTypeDef(BaseValidatorModel):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class EnableInsightRulesOutputTypeDef(BaseValidatorModel):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDashboardOutputTypeDef(BaseValidatorModel):
    DashboardArn: str
    DashboardBody: str
    DashboardName: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMetricStatisticsOutputTypeDef(BaseValidatorModel):
    Label: str
    Datapoints: List[DatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetMetricWidgetImageOutputTypeDef(BaseValidatorModel):
    MetricWidgetImage: bytes
    ResponseMetadata: ResponseMetadataTypeDef


class ListDashboardsOutputTypeDef(BaseValidatorModel):
    DashboardEntries: List[DashboardEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutDashboardOutputTypeDef(BaseValidatorModel):
    DashboardValidationMessages: List[DashboardValidationMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutManagedInsightRulesOutputTypeDef(BaseValidatorModel):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutMetricStreamOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef(BaseValidatorModel):
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None


class DescribeAlarmHistoryInputTypeDef(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None


class GetInsightRuleReportInputTypeDef(BaseValidatorModel):
    RuleName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Period: int
    MaxContributorCount: Optional[int] = None
    Metrics: Optional[Sequence[str]] = None
    OrderBy: Optional[str] = None


class GetMetricStatisticsInputMetricGetStatisticsTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Period: int
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Statistics: Optional[Sequence[StatisticType]] = None
    ExtendedStatistics: Optional[Sequence[str]] = None
    Unit: Optional[StandardUnitType] = None


class GetMetricStatisticsInputTypeDef(BaseValidatorModel):
    Namespace: str
    MetricName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Period: int
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Statistics: Optional[Sequence[StatisticType]] = None
    ExtendedStatistics: Optional[Sequence[str]] = None
    Unit: Optional[StandardUnitType] = None


class RangeTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef


class DescribeAlarmHistoryInputPaginateTypeDef(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    ScanBy: Optional[ScanByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAlarmsInputPaginateTypeDef(BaseValidatorModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAnomalyDetectorsInputPaginateTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    AnomalyDetectorTypes: Optional[Sequence[AnomalyDetectorTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDashboardsInputPaginateTypeDef(BaseValidatorModel):
    DashboardNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAlarmsInputWaitExtraTypeDef(BaseValidatorModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeAlarmsInputWaitTypeDef(BaseValidatorModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeInsightRulesOutputTypeDef(BaseValidatorModel):
    InsightRules: List[InsightRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMetricsInputPaginateTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionFilterTypeDef]] = None
    RecentlyActive: Optional[Literal["PT3H"]] = None
    IncludeLinkedAccounts: Optional[bool] = None
    OwningAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMetricsInputTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionFilterTypeDef]] = None
    NextToken: Optional[str] = None
    RecentlyActive: Optional[Literal["PT3H"]] = None
    IncludeLinkedAccounts: Optional[bool] = None
    OwningAccount: Optional[str] = None


class MetricDataResultTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Label: Optional[str] = None
    Timestamps: Optional[List[datetime]] = None
    Values: Optional[List[float]] = None
    StatusCode: Optional[StatusCodeType] = None
    Messages: Optional[List[MessageDataTypeDef]] = None


class InsightRuleContributorTypeDef(BaseValidatorModel):
    Keys: List[str]
    ApproximateAggregateValue: float
    Datapoints: List[InsightRuleContributorDatapointTypeDef]


class ListMetricStreamsOutputTypeDef(BaseValidatorModel):
    Entries: List[MetricStreamEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ManagedRuleTypeDef(BaseValidatorModel):
    TemplateName: str
    ResourceARN: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class PutCompositeAlarmInputTypeDef(BaseValidatorModel):
    AlarmName: str
    AlarmRule: str
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[Sequence[str]] = None
    AlarmDescription: Optional[str] = None
    InsufficientDataActions: Optional[Sequence[str]] = None
    OKActions: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ActionsSuppressor: Optional[str] = None
    ActionsSuppressorWaitPeriod: Optional[int] = None
    ActionsSuppressorExtensionPeriod: Optional[int] = None


class PutInsightRuleInputTypeDef(BaseValidatorModel):
    RuleName: str
    RuleDefinition: str
    RuleState: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class ManagedRuleDescriptionTypeDef(BaseValidatorModel):
    TemplateName: Optional[str] = None
    ResourceARN: Optional[str] = None
    RuleState: Optional[ManagedRuleStateTypeDef] = None


class MetricDatumTypeDef(BaseValidatorModel):
    MetricName: str
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Timestamp: Optional[TimestampTypeDef] = None
    Value: Optional[float] = None
    StatisticValues: Optional[StatisticSetTypeDef] = None
    Values: Optional[Sequence[float]] = None
    Counts: Optional[Sequence[float]] = None
    Unit: Optional[StandardUnitType] = None
    StorageResolution: Optional[int] = None


class MetricStreamStatisticsConfigurationOutputTypeDef(BaseValidatorModel):
    IncludeMetrics: List[MetricStreamStatisticsMetricTypeDef]
    AdditionalStatistics: List[str]


class MetricStreamStatisticsConfigurationTypeDef(BaseValidatorModel):
    IncludeMetrics: Sequence[MetricStreamStatisticsMetricTypeDef]
    AdditionalStatistics: Sequence[str]


class ListMetricsOutputTypeDef(BaseValidatorModel):
    Metrics: List[MetricOutputTypeDef]
    OwningAccounts: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MetricStatOutputTypeDef(BaseValidatorModel):
    Metric: MetricOutputTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class AnomalyDetectorConfigurationTypeDef(BaseValidatorModel):
    ExcludedTimeRanges: Optional[Sequence[RangeTypeDef]] = None
    MetricTimezone: Optional[str] = None


class GetMetricDataOutputTypeDef(BaseValidatorModel):
    MetricDataResults: List[MetricDataResultTypeDef]
    Messages: List[MessageDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetInsightRuleReportOutputTypeDef(BaseValidatorModel):
    KeyLabels: List[str]
    AggregationStatistic: str
    AggregateValue: float
    ApproximateUniqueCount: int
    Contributors: List[InsightRuleContributorTypeDef]
    MetricDatapoints: List[InsightRuleMetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutManagedInsightRulesInputTypeDef(BaseValidatorModel):
    ManagedRules: Sequence[ManagedRuleTypeDef]


class ListManagedInsightRulesOutputTypeDef(BaseValidatorModel):
    ManagedRules: List[ManagedRuleDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EntityMetricDataTypeDef(BaseValidatorModel):
    Entity: Optional[EntityTypeDef] = None
    MetricData: Optional[Sequence[MetricDatumTypeDef]] = None


class GetMetricStreamOutputTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    IncludeFilters: List[MetricStreamFilterOutputTypeDef]
    ExcludeFilters: List[MetricStreamFilterOutputTypeDef]
    FirehoseArn: str
    RoleArn: str
    State: str
    CreationDate: datetime
    LastUpdateDate: datetime
    OutputFormat: MetricStreamOutputFormatType
    StatisticsConfigurations: List[MetricStreamStatisticsConfigurationOutputTypeDef]
    IncludeLinkedAccountsMetrics: bool
    ResponseMetadata: ResponseMetadataTypeDef


class MetricDataQueryOutputTypeDef(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatOutputTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


class MetricUnionTypeDef(BaseValidatorModel):
    pass


class MetricStatTypeDef(BaseValidatorModel):
    Metric: MetricUnionTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class PutMetricDataInputMetricPutDataTypeDef(BaseValidatorModel):
    EntityMetricData: Optional[Sequence[EntityMetricDataTypeDef]] = None
    StrictEntityValidation: Optional[bool] = None


class PutMetricDataInputTypeDef(BaseValidatorModel):
    Namespace: str
    MetricData: Optional[Sequence[MetricDatumTypeDef]] = None
    EntityMetricData: Optional[Sequence[EntityMetricDataTypeDef]] = None
    StrictEntityValidation: Optional[bool] = None


class MetricStreamStatisticsConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class MetricStreamFilterUnionTypeDef(BaseValidatorModel):
    pass


class PutMetricStreamInputTypeDef(BaseValidatorModel):
    Name: str
    FirehoseArn: str
    RoleArn: str
    OutputFormat: MetricStreamOutputFormatType
    IncludeFilters: Optional[Sequence[MetricStreamFilterUnionTypeDef]] = None
    ExcludeFilters: Optional[Sequence[MetricStreamFilterUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    StatisticsConfigurations: Optional[Sequence[MetricStreamStatisticsConfigurationUnionTypeDef]] = None
    IncludeLinkedAccountsMetrics: Optional[bool] = None


class MetricAlarmTypeDef(BaseValidatorModel):
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
    Dimensions: Optional[List[DimensionTypeDef]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None
    EvaluationPeriods: Optional[int] = None
    DatapointsToAlarm: Optional[int] = None
    Threshold: Optional[float] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    TreatMissingData: Optional[str] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    Metrics: Optional[List[MetricDataQueryOutputTypeDef]] = None
    ThresholdMetricId: Optional[str] = None
    EvaluationState: Optional[Literal["PARTIAL_DATA"]] = None
    StateTransitionedTimestamp: Optional[datetime] = None


class MetricMathAnomalyDetectorOutputTypeDef(BaseValidatorModel):
    MetricDataQueries: Optional[List[MetricDataQueryOutputTypeDef]] = None


class CloudwatchEventDetailConfigurationTypeDef(BaseValidatorModel):
    pass


class CloudwatchEventDetailTypeDef(BaseValidatorModel):
    alarmName: str
    state: CloudwatchEventStateTypeDef
    operation: Optional[str] = None
    configuration: Optional[CloudwatchEventDetailConfigurationTypeDef] = None
    previousConfiguration: Optional[CloudwatchEventDetailConfigurationTypeDef] = None
    previousState: Optional[CloudwatchEventStateTypeDef] = None


class DescribeAlarmsForMetricOutputTypeDef(BaseValidatorModel):
    MetricAlarms: List[MetricAlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAlarmsOutputTypeDef(BaseValidatorModel):
    CompositeAlarms: List[CompositeAlarmTypeDef]
    MetricAlarms: List[MetricAlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MetricStatAlarmTypeDef(BaseValidatorModel):
    Metric: MetricAlarmTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class AnomalyDetectorTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None
    Stat: Optional[str] = None
    Configuration: Optional[AnomalyDetectorConfigurationOutputTypeDef] = None
    StateValue: Optional[AnomalyDetectorStateValueType] = None
    MetricCharacteristics: Optional[MetricCharacteristicsTypeDef] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorOutputTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorOutputTypeDef] = None


class MetricStatUnionTypeDef(BaseValidatorModel):
    pass


class MetricDataQueryTypeDef(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatUnionTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


class MetricDataQueryAlarmTypeDef(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatAlarmTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


class DescribeAnomalyDetectorsOutputTypeDef(BaseValidatorModel):
    AnomalyDetectors: List[AnomalyDetectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MetricMathAnomalyDetectorTypeDef(BaseValidatorModel):
    MetricDataQueries: Optional[Sequence[MetricDataQueryTypeDef]] = None


class MetricDataQueryUnionTypeDef(BaseValidatorModel):
    pass


class GetMetricDataInputPaginateTypeDef(BaseValidatorModel):
    MetricDataQueries: Sequence[MetricDataQueryUnionTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    ScanBy: Optional[ScanByType] = None
    LabelOptions: Optional[LabelOptionsTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetMetricDataInputTypeDef(BaseValidatorModel):
    MetricDataQueries: Sequence[MetricDataQueryUnionTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None
    MaxDatapoints: Optional[int] = None
    LabelOptions: Optional[LabelOptionsTypeDef] = None


class PutMetricAlarmInputMetricPutAlarmTypeDef(BaseValidatorModel):
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
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None
    DatapointsToAlarm: Optional[int] = None
    Threshold: Optional[float] = None
    TreatMissingData: Optional[str] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    Metrics: Optional[Sequence[MetricDataQueryUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ThresholdMetricId: Optional[str] = None


class PutMetricAlarmInputTypeDef(BaseValidatorModel):
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
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None
    DatapointsToAlarm: Optional[int] = None
    Threshold: Optional[float] = None
    TreatMissingData: Optional[str] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    Metrics: Optional[Sequence[MetricDataQueryUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ThresholdMetricId: Optional[str] = None


class SingleMetricAnomalyDetectorUnionTypeDef(BaseValidatorModel):
    pass


class MetricMathAnomalyDetectorUnionTypeDef(BaseValidatorModel):
    pass


class DeleteAnomalyDetectorInputTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Stat: Optional[str] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorUnionTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorUnionTypeDef] = None


class AnomalyDetectorConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutAnomalyDetectorInputTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Stat: Optional[str] = None
    Configuration: Optional[AnomalyDetectorConfigurationUnionTypeDef] = None
    MetricCharacteristics: Optional[MetricCharacteristicsTypeDef] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorUnionTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorUnionTypeDef] = None


