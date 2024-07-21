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
from aws_resource_validator.pydantic_models.cloudwatch_constants import *

class AlarmHistoryItemTypeDef(BaseModel):
    AlarmName: Optional[str] = None
    AlarmType: Optional[AlarmTypeType] = None
    Timestamp: Optional[datetime] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    HistorySummary: Optional[str] = None
    HistoryData: Optional[str] = None

class RangeTypeDef(BaseModel):
    StartTime: datetime
    EndTime: datetime

class DimensionTypeDef(BaseModel):
    Name: str
    Value: str

class MetricCharacteristicsTypeDef(BaseModel):
    PeriodicSpikes: Optional[bool] = None

class CloudwatchEventStateTypeDef(BaseModel):
    timestamp: str
    value: str
    reason: Optional[str] = None
    reasonData: Optional[str] = None
    actionsSuppressedBy: Optional[str] = None
    actionsSuppressedReason: Optional[str] = None

class CloudwatchEventMetricStatsMetricTypeDef(BaseModel):
    metricName: str
    namespace: str
    dimensions: Dict[str, str]

class CompositeAlarmTypeDef(BaseModel):
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

class DashboardEntryTypeDef(BaseModel):
    DashboardName: Optional[str] = None
    DashboardArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    Size: Optional[int] = None

class DashboardValidationMessageTypeDef(BaseModel):
    DataPath: Optional[str] = None
    Message: Optional[str] = None

class DatapointTypeDef(BaseModel):
    Timestamp: Optional[datetime] = None
    SampleCount: Optional[float] = None
    Average: Optional[float] = None
    Sum: Optional[float] = None
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None
    Unit: Optional[StandardUnitType] = None
    ExtendedStatistics: Optional[Dict[str, float]] = None

class DeleteAlarmsInputRequestTypeDef(BaseModel):
    AlarmNames: Sequence[str]

class DeleteDashboardsInputRequestTypeDef(BaseModel):
    DashboardNames: Sequence[str]

class DeleteInsightRulesInputRequestTypeDef(BaseModel):
    RuleNames: Sequence[str]

class PartialFailureTypeDef(BaseModel):
    FailureResource: Optional[str] = None
    ExceptionType: Optional[str] = None
    FailureCode: Optional[str] = None
    FailureDescription: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteMetricStreamInputRequestTypeDef(BaseModel):
    Name: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeAlarmsInputRequestTypeDef(BaseModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInsightRulesInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class InsightRuleTypeDef(BaseModel):
    Name: str
    State: str
    Schema: str
    Definition: str
    ManagedRule: Optional[bool] = None

class DimensionFilterTypeDef(BaseModel):
    Name: str
    Value: Optional[str] = None

class DisableAlarmActionsInputRequestTypeDef(BaseModel):
    AlarmNames: Sequence[str]

class DisableInsightRulesInputRequestTypeDef(BaseModel):
    RuleNames: Sequence[str]

class EnableAlarmActionsInputRequestTypeDef(BaseModel):
    AlarmNames: Sequence[str]

class EnableInsightRulesInputRequestTypeDef(BaseModel):
    RuleNames: Sequence[str]

class GetDashboardInputRequestTypeDef(BaseModel):
    DashboardName: str

class InsightRuleMetricDatapointTypeDef(BaseModel):
    Timestamp: datetime
    UniqueContributors: Optional[float] = None
    MaxContributorValue: Optional[float] = None
    SampleCount: Optional[float] = None
    Average: Optional[float] = None
    Sum: Optional[float] = None
    Minimum: Optional[float] = None
    Maximum: Optional[float] = None

class LabelOptionsTypeDef(BaseModel):
    Timezone: Optional[str] = None

class MessageDataTypeDef(BaseModel):
    Code: Optional[str] = None
    Value: Optional[str] = None

class GetMetricStreamInputRequestTypeDef(BaseModel):
    Name: str

class MetricStreamFilterTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricNames: Optional[List[str]] = None

class GetMetricWidgetImageInputRequestTypeDef(BaseModel):
    MetricWidget: str
    OutputFormat: Optional[str] = None

class InsightRuleContributorDatapointTypeDef(BaseModel):
    Timestamp: datetime
    ApproximateValue: float

class ListDashboardsInputRequestTypeDef(BaseModel):
    DashboardNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None

class ListManagedInsightRulesInputRequestTypeDef(BaseModel):
    ResourceARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMetricStreamsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MetricStreamEntryTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastUpdateDate: Optional[datetime] = None
    Name: Optional[str] = None
    FirehoseArn: Optional[str] = None
    State: Optional[str] = None
    OutputFormat: Optional[MetricStreamOutputFormatType] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ManagedRuleStateTypeDef(BaseModel):
    RuleName: str
    State: str

class StatisticSetTypeDef(BaseModel):
    SampleCount: float
    Sum: float
    Minimum: float
    Maximum: float

class MetricStreamStatisticsMetricTypeDef(BaseModel):
    Namespace: str
    MetricName: str

class PutDashboardInputRequestTypeDef(BaseModel):
    DashboardName: str
    DashboardBody: str

class SetAlarmStateInputAlarmSetStateTypeDef(BaseModel):
    StateValue: StateValueType
    StateReason: str
    StateReasonData: Optional[str] = None

class SetAlarmStateInputRequestTypeDef(BaseModel):
    AlarmName: str
    StateValue: StateValueType
    StateReason: str
    StateReasonData: Optional[str] = None

class StartMetricStreamsInputRequestTypeDef(BaseModel):
    Names: Sequence[str]

class StopMetricStreamsInputRequestTypeDef(BaseModel):
    Names: Sequence[str]

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class AnomalyDetectorConfigurationTypeDef(BaseModel):
    ExcludedTimeRanges: Optional[List[RangeTypeDef]] = None
    MetricTimezone: Optional[str] = None

class DescribeAlarmsForMetricInputRequestTypeDef(BaseModel):
    MetricName: str
    Namespace: str
    Statistic: Optional[StatisticType] = None
    ExtendedStatistic: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Period: Optional[int] = None
    Unit: Optional[StandardUnitType] = None

class DescribeAnomalyDetectorsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    AnomalyDetectorTypes: Optional[Sequence[AnomalyDetectorTypeType]] = None

class MetricPaginatorTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None

class MetricTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None

class SingleMetricAnomalyDetectorPaginatorTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None
    Stat: Optional[str] = None

class SingleMetricAnomalyDetectorTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Stat: Optional[str] = None

class CloudwatchEventMetricStatsTypeDef(BaseModel):
    period: str
    stat: str
    metric: Optional[CloudwatchEventMetricStatsMetricTypeDef] = None

class DeleteInsightRulesOutputTypeDef(BaseModel):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlarmHistoryOutputTypeDef(BaseModel):
    AlarmHistoryItems: List[AlarmHistoryItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableInsightRulesOutputTypeDef(BaseModel):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableInsightRulesOutputTypeDef(BaseModel):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDashboardOutputTypeDef(BaseModel):
    DashboardArn: str
    DashboardBody: str
    DashboardName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMetricStatisticsOutputTypeDef(BaseModel):
    Label: str
    Datapoints: List[DatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMetricWidgetImageOutputTypeDef(BaseModel):
    MetricWidgetImage: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class ListDashboardsOutputTypeDef(BaseModel):
    DashboardEntries: List[DashboardEntryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutDashboardOutputTypeDef(BaseModel):
    DashboardValidationMessages: List[DashboardValidationMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutManagedInsightRulesOutputTypeDef(BaseModel):
    Failures: List[PartialFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutMetricStreamOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef(BaseModel):
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None

class DescribeAlarmHistoryInputRequestTypeDef(BaseModel):
    AlarmName: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None

class GetInsightRuleReportInputRequestTypeDef(BaseModel):
    RuleName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Period: int
    MaxContributorCount: Optional[int] = None
    Metrics: Optional[Sequence[str]] = None
    OrderBy: Optional[str] = None

class GetMetricStatisticsInputMetricGetStatisticsTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Period: int
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Statistics: Optional[Sequence[StatisticType]] = None
    ExtendedStatistics: Optional[Sequence[str]] = None
    Unit: Optional[StandardUnitType] = None

class GetMetricStatisticsInputRequestTypeDef(BaseModel):
    Namespace: str
    MetricName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Period: int
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Statistics: Optional[Sequence[StatisticType]] = None
    ExtendedStatistics: Optional[Sequence[str]] = None
    Unit: Optional[StandardUnitType] = None

class DescribeAlarmHistoryInputDescribeAlarmHistoryPaginateTypeDef(BaseModel):
    AlarmName: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    HistoryItemType: Optional[HistoryItemTypeType] = None
    StartDate: Optional[TimestampTypeDef] = None
    EndDate: Optional[TimestampTypeDef] = None
    ScanBy: Optional[ScanByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAlarmsInputDescribeAlarmsPaginateTypeDef(BaseModel):
    AlarmNames: Optional[Sequence[str]] = None
    AlarmNamePrefix: Optional[str] = None
    AlarmTypes: Optional[Sequence[AlarmTypeType]] = None
    ChildrenOfAlarmName: Optional[str] = None
    ParentsOfAlarmName: Optional[str] = None
    StateValue: Optional[StateValueType] = None
    ActionPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAnomalyDetectorsInputDescribeAnomalyDetectorsPaginateTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    AnomalyDetectorTypes: Optional[Sequence[AnomalyDetectorTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDashboardsInputListDashboardsPaginateTypeDef(BaseModel):
    DashboardNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAlarmsInputAlarmExistsWaitTypeDef(BaseModel):
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

class DescribeAlarmsInputCompositeAlarmExistsWaitTypeDef(BaseModel):
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

class DescribeInsightRulesOutputTypeDef(BaseModel):
    NextToken: str
    InsightRules: List[InsightRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMetricsInputListMetricsPaginateTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionFilterTypeDef]] = None
    RecentlyActive: Optional[Literal["PT3H"]] = None
    IncludeLinkedAccounts: Optional[bool] = None
    OwningAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMetricsInputRequestTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionFilterTypeDef]] = None
    NextToken: Optional[str] = None
    RecentlyActive: Optional[Literal["PT3H"]] = None
    IncludeLinkedAccounts: Optional[bool] = None
    OwningAccount: Optional[str] = None

class MetricDataResultTypeDef(BaseModel):
    Id: Optional[str] = None
    Label: Optional[str] = None
    Timestamps: Optional[List[datetime]] = None
    Values: Optional[List[float]] = None
    StatusCode: Optional[StatusCodeType] = None
    Messages: Optional[List[MessageDataTypeDef]] = None

class InsightRuleContributorTypeDef(BaseModel):
    Keys: List[str]
    ApproximateAggregateValue: float
    Datapoints: List[InsightRuleContributorDatapointTypeDef]

class ListMetricStreamsOutputTypeDef(BaseModel):
    NextToken: str
    Entries: List[MetricStreamEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedRuleTypeDef(BaseModel):
    TemplateName: str
    ResourceARN: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class PutCompositeAlarmInputRequestTypeDef(BaseModel):
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

class PutInsightRuleInputRequestTypeDef(BaseModel):
    RuleName: str
    RuleDefinition: str
    RuleState: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class ManagedRuleDescriptionTypeDef(BaseModel):
    TemplateName: Optional[str] = None
    ResourceARN: Optional[str] = None
    RuleState: Optional[ManagedRuleStateTypeDef] = None

class MetricDatumTypeDef(BaseModel):
    MetricName: str
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Timestamp: Optional[TimestampTypeDef] = None
    Value: Optional[float] = None
    StatisticValues: Optional[StatisticSetTypeDef] = None
    Values: Optional[Sequence[float]] = None
    Counts: Optional[Sequence[float]] = None
    Unit: Optional[StandardUnitType] = None
    StorageResolution: Optional[int] = None

class MetricStreamStatisticsConfigurationTypeDef(BaseModel):
    IncludeMetrics: List[MetricStreamStatisticsMetricTypeDef]
    AdditionalStatistics: List[str]

class ListMetricsOutputPaginatorTypeDef(BaseModel):
    Metrics: List[MetricPaginatorTypeDef]
    NextToken: str
    OwningAccounts: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricStatPaginatorTypeDef(BaseModel):
    Metric: MetricPaginatorTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None

class ListMetricsOutputTypeDef(BaseModel):
    Metrics: List[MetricTypeDef]
    NextToken: str
    OwningAccounts: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricStatTypeDef(BaseModel):
    Metric: MetricTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None

class CloudwatchEventMetricTypeDef(BaseModel):
    id: str
    returnData: bool
    metricStat: Optional[CloudwatchEventMetricStatsTypeDef] = None
    expression: Optional[str] = None
    label: Optional[str] = None
    period: Optional[int] = None

class GetMetricDataOutputTypeDef(BaseModel):
    MetricDataResults: List[MetricDataResultTypeDef]
    NextToken: str
    Messages: List[MessageDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightRuleReportOutputTypeDef(BaseModel):
    KeyLabels: List[str]
    AggregationStatistic: str
    AggregateValue: float
    ApproximateUniqueCount: int
    Contributors: List[InsightRuleContributorTypeDef]
    MetricDatapoints: List[InsightRuleMetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutManagedInsightRulesInputRequestTypeDef(BaseModel):
    ManagedRules: Sequence[ManagedRuleTypeDef]

class ListManagedInsightRulesOutputTypeDef(BaseModel):
    ManagedRules: List[ManagedRuleDescriptionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutMetricDataInputRequestTypeDef(BaseModel):
    Namespace: str
    MetricData: Sequence[MetricDatumTypeDef]

class GetMetricStreamOutputTypeDef(BaseModel):
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

class PutMetricStreamInputRequestTypeDef(BaseModel):
    Name: str
    FirehoseArn: str
    RoleArn: str
    OutputFormat: MetricStreamOutputFormatType
    IncludeFilters: Optional[Sequence[MetricStreamFilterTypeDef]] = None
    ExcludeFilters: Optional[Sequence[MetricStreamFilterTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    StatisticsConfigurations: Optional[       Sequence[MetricStreamStatisticsConfigurationTypeDef]     ] = None
    IncludeLinkedAccountsMetrics: Optional[bool] = None

class MetricDataQueryPaginatorTypeDef(BaseModel):
    Id: str
    MetricStat: Optional[MetricStatPaginatorTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None

class MetricDataQueryTypeDef(BaseModel):
    Id: str
    MetricStat: Optional[MetricStatTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None

class CloudwatchEventDetailConfigurationTypeDef(BaseModel):
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

class GetMetricDataInputGetMetricDataPaginateTypeDef(BaseModel):
    MetricDataQueries: Sequence[MetricDataQueryPaginatorTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    ScanBy: Optional[ScanByType] = None
    LabelOptions: Optional[LabelOptionsTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class MetricAlarmPaginatorTypeDef(BaseModel):
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

class MetricMathAnomalyDetectorPaginatorTypeDef(BaseModel):
    MetricDataQueries: Optional[List[MetricDataQueryPaginatorTypeDef]] = None

class GetMetricDataInputRequestTypeDef(BaseModel):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: Optional[str] = None
    ScanBy: Optional[ScanByType] = None
    MaxDatapoints: Optional[int] = None
    LabelOptions: Optional[LabelOptionsTypeDef] = None

class MetricAlarmTypeDef(BaseModel):
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

class MetricMathAnomalyDetectorTypeDef(BaseModel):
    MetricDataQueries: Optional[Sequence[MetricDataQueryTypeDef]] = None

class PutMetricAlarmInputMetricPutAlarmTypeDef(BaseModel):
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

class PutMetricAlarmInputRequestTypeDef(BaseModel):
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

class CloudwatchEventDetailTypeDef(BaseModel):
    alarmName: str
    state: CloudwatchEventStateTypeDef
    operation: Optional[str] = None
    configuration: Optional[CloudwatchEventDetailConfigurationTypeDef] = None
    previousConfiguration: Optional[CloudwatchEventDetailConfigurationTypeDef] = None
    previousState: Optional[CloudwatchEventStateTypeDef] = None

class DescribeAlarmsOutputPaginatorTypeDef(BaseModel):
    CompositeAlarms: List[CompositeAlarmTypeDef]
    MetricAlarms: List[MetricAlarmPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AnomalyDetectorPaginatorTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None
    Stat: Optional[str] = None
    Configuration: Optional[AnomalyDetectorConfigurationTypeDef] = None
    StateValue: Optional[AnomalyDetectorStateValueType] = None
    MetricCharacteristics: Optional[MetricCharacteristicsTypeDef] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorPaginatorTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorPaginatorTypeDef] = None

class DescribeAlarmsForMetricOutputTypeDef(BaseModel):
    MetricAlarms: List[MetricAlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlarmsOutputTypeDef(BaseModel):
    CompositeAlarms: List[CompositeAlarmTypeDef]
    MetricAlarms: List[MetricAlarmTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricStatAlarmTypeDef(BaseModel):
    Metric: MetricAlarmTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None

class AnomalyDetectorTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None
    Stat: Optional[str] = None
    Configuration: Optional[AnomalyDetectorConfigurationTypeDef] = None
    StateValue: Optional[AnomalyDetectorStateValueType] = None
    MetricCharacteristics: Optional[MetricCharacteristicsTypeDef] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorTypeDef] = None

class DeleteAnomalyDetectorInputRequestTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Stat: Optional[str] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorTypeDef] = None

class PutAnomalyDetectorInputRequestTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None
    Stat: Optional[str] = None
    Configuration: Optional[AnomalyDetectorConfigurationTypeDef] = None
    MetricCharacteristics: Optional[MetricCharacteristicsTypeDef] = None
    SingleMetricAnomalyDetector: Optional[SingleMetricAnomalyDetectorTypeDef] = None
    MetricMathAnomalyDetector: Optional[MetricMathAnomalyDetectorTypeDef] = None

class CloudwatchEventTypeDef(BaseModel):
    version: str
    id: str
    source: str
    account: str
    time: str
    region: str
    resources: List[str]
    detail: CloudwatchEventDetailTypeDef

class DescribeAnomalyDetectorsOutputPaginatorTypeDef(BaseModel):
    AnomalyDetectors: List[AnomalyDetectorPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricDataQueryAlarmTypeDef(BaseModel):
    Id: str
    MetricStat: Optional[MetricStatAlarmTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None

class DescribeAnomalyDetectorsOutputTypeDef(BaseModel):
    AnomalyDetectors: List[AnomalyDetectorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

