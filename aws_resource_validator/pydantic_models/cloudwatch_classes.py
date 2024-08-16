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
from aws_resource_validator.pydantic_models.cloudwatch_constants import *

class AlarmHistoryItemTypeDef(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmType: Optional[AlarmTypeType] = None
    Timestamp: Optional[datetime] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    HistorySummary: Optional[str] = None
    HistoryData: Optional[str] = None

class RangeTypeDef(BaseValidatorModel):
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

class DeleteAlarmsInputRequestTypeDef(BaseValidatorModel):
    AlarmNames: Sequence[str]

class DeleteDashboardsInputRequestTypeDef(BaseValidatorModel):
    DashboardNames: Sequence[str]

class DeleteInsightRulesInputRequestTypeDef(BaseValidatorModel):
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

class DeleteMetricStreamInputRequestTypeDef(BaseValidatorModel):
    Name: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeAlarmsInputRequestTypeDef(BaseValidatorModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInsightRulesInputRequestTypeDef(BaseValidatorModel):
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

class DisableAlarmActionsInputRequestTypeDef(BaseValidatorModel):
    AlarmNames: Sequence[str]

class DisableInsightRulesInputRequestTypeDef(BaseValidatorModel):
    RuleNames: Sequence[str]

class EnableAlarmActionsInputRequestTypeDef(BaseValidatorModel):
    AlarmNames: Sequence[str]

class EnableInsightRulesInputRequestTypeDef(BaseValidatorModel):
    RuleNames: Sequence[str]

class GetDashboardInputRequestTypeDef(BaseValidatorModel):
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

class GetMetricStreamInputRequestTypeDef(BaseValidatorModel):
    Name: str

class MetricStreamFilterTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricNames: Optional[List[str]] = None

class GetMetricWidgetImageInputRequestTypeDef(BaseValidatorModel):
    MetricWidget: str
    OutputFormat: Optional[str] = None

class InsightRuleContributorDatapointTypeDef(BaseValidatorModel):
    Timestamp: datetime
    ApproximateValue: float

class ListDashboardsInputRequestTypeDef(BaseValidatorModel):
    DashboardNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None

class ListManagedInsightRulesInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMetricStreamsInputRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
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

class MetricStreamStatisticsMetricTypeDef(BaseValidatorModel):
    Namespace: str
    MetricName: str

class PutDashboardInputRequestTypeDef(BaseValidatorModel):
    DashboardName: str
    DashboardBody: str

class SetAlarmStateInputAlarmSetStateTypeDef(BaseValidatorModel):
    StateValue: StateValueType
    StateReason: str
    StateReasonData: Optional[str] = None

class SetAlarmStateInputRequestTypeDef(BaseValidatorModel):
    AlarmName: str
    StateValue: StateValueType
    StateReason: str
    StateReasonData: Optional[str] = None

class StartMetricStreamsInputRequestTypeDef(BaseValidatorModel):
    Names: Sequence[str]

class StopMetricStreamsInputRequestTypeDef(BaseValidatorModel):
    Names: Sequence[str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class AnomalyDetectorConfigurationTypeDef(BaseValidatorModel):
    ExcludedTimeRanges: Optional[List[RangeTypeDef]] = None
    MetricTimezone: Optional[str] = None

class DescribeAlarmsForMetricInputRequestTypeDef(BaseValidatorModel):
    MetricName: str
    Namespace: str
    Statistic: Optional[StatisticType] = None
    ExtendedStatistic: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None

class DescribeAnomalyDetectorsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    AnomalyDetectorTypes: Optional[Sequence[AnomalyDetectorTypeType]] = None

class MetricPaginatorTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None

class MetricTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None

class SingleMetricAnomalyDetectorPaginatorTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutDashboardOutputTypeDef(BaseValidatorModel):
    DashboardValidationMessages: List[DashboardValidationMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutManagedInsightRulesOutputTypeDef(BaseValidatorModel):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutMetricStreamOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef(BaseValidatorModel):
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None

class DescribeAlarmHistoryInputRequestTypeDef(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None

class GetInsightRuleReportInputRequestTypeDef(BaseValidatorModel):
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

class GetMetricStatisticsInputRequestTypeDef(BaseValidatorModel):
    Namespace: str
    MetricName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Period: int
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Statistics: Optional[Sequence[StatisticType]] = None
    ExtendedStatistics: Optional[Sequence[str]] = None
    Unit: Optional[StandardUnitType] = None

class DescribeAlarmHistoryInputDescribeAlarmHistoryPaginateTypeDef(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    ScanBy: Optional[ScanByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAlarmsInputDescribeAlarmsPaginateTypeDef(BaseValidatorModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAnomalyDetectorsInputDescribeAnomalyDetectorsPaginateTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    AnomalyDetectorTypes: Optional[Sequence[AnomalyDetectorTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDashboardsInputListDashboardsPaginateTypeDef(BaseValidatorModel):
    DashboardNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAlarmsInputAlarmExistsWaitTypeDef(BaseValidatorModel):
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

class DescribeAlarmsInputCompositeAlarmExistsWaitTypeDef(BaseValidatorModel):
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
    NextToken: str
    InsightRules: List[InsightRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMetricsInputListMetricsPaginateTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionFilterTypeDef]] = None
    RecentlyActive: Optional[Literal["PT3H"]] = None
    IncludeLinkedAccounts: Optional[bool] = None
    OwningAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMetricsInputRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    Entries: List[MetricStreamEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedRuleTypeDef(BaseValidatorModel):
    TemplateName: str
    ResourceARN: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class PutCompositeAlarmInputRequestTypeDef(BaseValidatorModel):
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

class PutInsightRuleInputRequestTypeDef(BaseValidatorModel):
    RuleName: str
    RuleDefinition: str
    RuleState: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
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

class MetricStreamStatisticsConfigurationTypeDef(BaseValidatorModel):
    IncludeMetrics: List[MetricStreamStatisticsMetricTypeDef]
    AdditionalStatistics: List[str]

class ListMetricsOutputPaginatorTypeDef(BaseValidatorModel):
    Metrics: List[MetricPaginatorTypeDef]
    NextToken: str
    OwningAccounts: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricStatPaginatorTypeDef(BaseValidatorModel):
    Metric: MetricPaginatorTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None

class ListMetricsOutputTypeDef(BaseValidatorModel):
    Metrics: List[MetricTypeDef]
    NextToken: str
    OwningAccounts: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricStatTypeDef(BaseValidatorModel):
    Metric: MetricTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None

class CloudwatchEventMetricTypeDef(BaseValidatorModel):
    id: str
    returnData: bool
    metricStat: Optional[CloudwatchEventMetricStatsTypeDef] = None
    expression: Optional[str] = None
    label: Optional[str] = None
    period: Optional[int] = None

class GetMetricDataOutputTypeDef(BaseValidatorModel):
    MetricDataResults: List[MetricDataResultTypeDef]
    NextToken: str
    Messages: List[MessageDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightRuleReportOutputTypeDef(BaseValidatorModel):
    KeyLabels: List[str]
    AggregationStatistic: str
    AggregateValue: float
    ApproximateUniqueCount: int
    Contributors: List[InsightRuleContributorTypeDef]
    MetricDatapoints: List[InsightRuleMetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutManagedInsightRulesInputRequestTypeDef(BaseValidatorModel):
    ManagedRules: Sequence[ManagedRuleTypeDef]

class ListManagedInsightRulesOutputTypeDef(BaseValidatorModel):
    ManagedRules: List[ManagedRuleDescriptionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutMetricDataInputRequestTypeDef(BaseValidatorModel):
    Namespace: str
    MetricData: Sequence[MetricDatumTypeDef]

class GetMetricStreamOutputTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    IncludeFilters: List[MetricStreamFilterTypeDef]
    ExcludeFilters: List[MetricStreamFilterTypeDef]
    FirehoseArn: str
    RoleArn: str
    State: str
    CreationDate: datetime
    LastUpdateDate: datetime
    OutputFormat: MetricStreamOutputFormatType
    StatisticsConfigurations: List[MetricStreamStatisticsConfigurationTypeDef]
    IncludeLinkedAccountsMetrics: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutMetricStreamInputRequestTypeDef(BaseValidatorModel):
    Name: str
    FirehoseArn: str
    RoleArn: str
    OutputFormat: MetricStreamOutputFormatType
    IncludeFilters: Optional[Sequence[MetricStreamFilterTypeDef]] = None
    ExcludeFilters: Optional[Sequence[MetricStreamFilterTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    StatisticsConfigurations: Optional[       Sequence[MetricStreamStatisticsConfigurationTypeDef]     ] = None
    IncludeLinkedAccountsMetrics: Optional[bool] = None

class MetricDataQueryPaginatorTypeDef(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatPaginatorTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None

class MetricDataQueryTypeDef(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None

class CloudwatchEventDetailConfigurationTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    description: Optional[str] = None
    metrics: Optional[List[CloudwatchEventMetricTypeDef]] = None
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

class GetMetricDataInputGetMetricDataPaginateTypeDef(BaseValidatorModel):
    MetricDataQueries: Sequence[MetricDataQueryPaginatorTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    ScanBy: Optional[ScanByType] = None
    LabelOptions: Optional[LabelOptionsTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class MetricAlarmPaginatorTypeDef(BaseValidatorModel):
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
    Metrics: Optional[List[MetricDataQueryPaginatorTypeDef]] = None
    ThresholdMetricId: Optional[str] = None
    EvaluationState: Optional[Literal["PARTIAL_DATA"]] = None
    StateTransitionedTimestamp: Optional[datetime] = None

class MetricMathAnomalyDetectorPaginatorTypeDef(BaseValidatorModel):
    MetricDataQueries: Optional[List[MetricDataQueryPaginatorTypeDef]] = None

class GetMetricDataInputRequestTypeDef(BaseValidatorModel):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None
    MaxDatapoints: Optional[int] = None
    LabelOptions: Optional[LabelOptionsTypeDef] = None

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
    Metrics: Optional[List[MetricDataQueryTypeDef]] = None
    ThresholdMetricId: Optional[str] = None
    EvaluationState: Optional[Literal["PARTIAL_DATA"]] = None
    StateTransitionedTimestamp: Optional[datetime] = None

class MetricMathAnomalyDetectorTypeDef(BaseValidatorModel):
    MetricDataQueries: Optional[Sequence[MetricDataQueryTypeDef]] = None

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
    Metrics: Optional[Sequence[MetricDataQueryTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ThresholdMetricId: Optional[str] = None

class PutMetricAlarmInputRequestTypeDef(BaseValidatorModel):
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
    Metrics: Optional[Sequence[MetricDataQueryTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ThresholdMetricId: Optional[str] = None

class CloudwatchEventDetailTypeDef(BaseValidatorModel):
    alarmName: str
    state: CloudwatchEventStateTypeDef
    operation: Optional[str] = None
    configuration: Optional[CloudwatchEventDetailConfigurationTypeDef] = None
    previousConfiguration: Optional[CloudwatchEventDetailConfigurationTypeDef] = None
    previousState: Optional[CloudwatchEventStateTypeDef] = None

class DescribeAlarmsOutputPaginatorTypeDef(BaseValidatorModel):
    CompositeAlarms: List[CompositeAlarmTypeDef]
    MetricAlarms: List[MetricAlarmPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AnomalyDetectorPaginatorTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None
    Stat: Optional[str] = None
    Configuration: Optional[AnomalyDetectorConfigurationTypeDef] = None
    StateValue: Optional[AnomalyDetectorStateValueType] = None
    MetricCharacteristics: Optional[MetricCharacteristicsTypeDef] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorPaginatorTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorPaginatorTypeDef] = None

class DescribeAlarmsForMetricOutputTypeDef(BaseValidatorModel):
    MetricAlarms: List[MetricAlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlarmsOutputTypeDef(BaseValidatorModel):
    CompositeAlarms: List[CompositeAlarmTypeDef]
    MetricAlarms: List[MetricAlarmTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    Configuration: Optional[AnomalyDetectorConfigurationTypeDef] = None
    StateValue: Optional[AnomalyDetectorStateValueType] = None
    MetricCharacteristics: Optional[MetricCharacteristicsTypeDef] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorTypeDef] = None

class DeleteAnomalyDetectorInputRequestTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Stat: Optional[str] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorTypeDef] = None

class PutAnomalyDetectorInputRequestTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Stat: Optional[str] = None
    Configuration: Optional[AnomalyDetectorConfigurationTypeDef] = None
    MetricCharacteristics: Optional[MetricCharacteristicsTypeDef] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorTypeDef] = None

class CloudwatchEventTypeDef(BaseValidatorModel):
    version: str
    id: str
    source: str
    account: str
    time: str
    region: str
    resources: List[str]
    detail: CloudwatchEventDetailTypeDef

class DescribeAnomalyDetectorsOutputPaginatorTypeDef(BaseValidatorModel):
    AnomalyDetectors: List[AnomalyDetectorPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

