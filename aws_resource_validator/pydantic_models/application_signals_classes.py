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
from aws_resource_validator.pydantic_models.application_signals_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ServiceLevelObjectiveBudgetReportErrorTypeDef(BaseValidatorModel):
    Name: str
    Arn: str
    ErrorCode: str
    ErrorMessage: str


class BurnRateConfigurationTypeDef(BaseValidatorModel):
    LookBackWindowMinutes: int


class CalendarIntervalOutputTypeDef(BaseValidatorModel):
    StartTime: datetime
    DurationUnit: DurationUnitType
    Duration: int


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class DeleteServiceLevelObjectiveInputTypeDef(BaseValidatorModel):
    Id: str


class DimensionTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class GetServiceLevelObjectiveInputTypeDef(BaseValidatorModel):
    Id: str


class RollingIntervalTypeDef(BaseValidatorModel):
    DurationUnit: DurationUnitType
    Duration: int


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListServiceLevelObjectivesInputTypeDef(BaseValidatorModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    SloOwnerAwsAccountId: Optional[str] = None


class ServiceLevelObjectiveSummaryTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    CreatedTime: Optional[datetime] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class TimestampTypeDef(BaseValidatorModel):
    pass


class BatchGetServiceLevelObjectiveBudgetReportInputTypeDef(BaseValidatorModel):
    Timestamp: TimestampTypeDef
    SloIds: Sequence[str]


class CalendarIntervalTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    DurationUnit: DurationUnitType
    Duration: int


class GetServiceInputTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]


class ListServiceDependenciesInputTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServiceDependentsInputTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServiceOperationsInputTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServicesInputTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    AwsAccountId: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class MetricOutputTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None


class MetricReferenceTypeDef(BaseValidatorModel):
    Namespace: str
    MetricType: str
    MetricName: str
    Dimensions: Optional[List[DimensionTypeDef]] = None
    AccountId: Optional[str] = None


class MetricTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None


class IntervalOutputTypeDef(BaseValidatorModel):
    RollingInterval: Optional[RollingIntervalTypeDef] = None
    CalendarInterval: Optional[CalendarIntervalOutputTypeDef] = None


class ListServiceDependenciesInputPaginateTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceDependentsInputPaginateTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceLevelObjectivesInputPaginateTypeDef(BaseValidatorModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    SloOwnerAwsAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceOperationsInputPaginateTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicesInputPaginateTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    IncludeLinkedAccounts: Optional[bool] = None
    AwsAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceLevelObjectivesOutputTypeDef(BaseValidatorModel):
    SloSummaries: List[ServiceLevelObjectiveSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class IntervalTypeDef(BaseValidatorModel):
    RollingInterval: Optional[RollingIntervalTypeDef] = None
    CalendarInterval: Optional[CalendarIntervalTypeDef] = None


class MetricStatOutputTypeDef(BaseValidatorModel):
    Metric: MetricOutputTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class ServiceDependencyTypeDef(BaseValidatorModel):
    OperationName: str
    DependencyKeyAttributes: Dict[str, str]
    DependencyOperationName: str
    MetricReferences: List[MetricReferenceTypeDef]


class ServiceDependentTypeDef(BaseValidatorModel):
    DependentKeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReferenceTypeDef]
    OperationName: Optional[str] = None
    DependentOperationName: Optional[str] = None


class ServiceOperationTypeDef(BaseValidatorModel):
    Name: str
    MetricReferences: List[MetricReferenceTypeDef]


class ServiceSummaryTypeDef(BaseValidatorModel):
    KeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReferenceTypeDef]
    AttributeMaps: Optional[List[Dict[str, str]]] = None


class ServiceTypeDef(BaseValidatorModel):
    KeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReferenceTypeDef]
    AttributeMaps: Optional[List[Dict[str, str]]] = None
    LogGroupReferences: Optional[List[Dict[str, str]]] = None


class GoalOutputTypeDef(BaseValidatorModel):
    Interval: Optional[IntervalOutputTypeDef] = None
    AttainmentGoal: Optional[float] = None
    WarningThreshold: Optional[float] = None


class GoalTypeDef(BaseValidatorModel):
    Interval: Optional[IntervalTypeDef] = None
    AttainmentGoal: Optional[float] = None
    WarningThreshold: Optional[float] = None


class MetricDataQueryOutputTypeDef(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatOutputTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


class ListServiceDependenciesOutputTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceDependencies: List[ServiceDependencyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListServiceDependentsOutputTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceDependents: List[ServiceDependentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListServiceOperationsOutputTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceOperations: List[ServiceOperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListServicesOutputTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceSummaries: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetServiceOutputTypeDef(BaseValidatorModel):
    Service: ServiceTypeDef
    StartTime: datetime
    EndTime: datetime
    LogGroupReferences: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef


class MetricUnionTypeDef(BaseValidatorModel):
    pass


class MetricStatTypeDef(BaseValidatorModel):
    Metric: MetricUnionTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class MonitoredRequestCountMetricDataQueriesOutputTypeDef(BaseValidatorModel):
    GoodCountMetric: Optional[List[MetricDataQueryOutputTypeDef]] = None
    BadCountMetric: Optional[List[MetricDataQueryOutputTypeDef]] = None


class ServiceLevelIndicatorMetricTypeDef(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None


class RequestBasedServiceLevelIndicatorMetricTypeDef(BaseValidatorModel):
    TotalRequestCountMetric: List[MetricDataQueryOutputTypeDef]
    MonitoredRequestCountMetric: MonitoredRequestCountMetricDataQueriesOutputTypeDef
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None


class ServiceLevelIndicatorTypeDef(BaseValidatorModel):
    SliMetric: ServiceLevelIndicatorMetricTypeDef
    MetricThreshold: float
    ComparisonOperator: ServiceLevelIndicatorComparisonOperatorType


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


class RequestBasedServiceLevelIndicatorTypeDef(BaseValidatorModel):
    RequestBasedSliMetric: RequestBasedServiceLevelIndicatorMetricTypeDef
    MetricThreshold: Optional[float] = None
    ComparisonOperator: Optional[ServiceLevelIndicatorComparisonOperatorType] = None


class ServiceLevelObjectiveBudgetReportTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    BudgetStatus: ServiceLevelObjectiveBudgetStatusType
    EvaluationType: Optional[EvaluationTypeType] = None
    Attainment: Optional[float] = None
    TotalBudgetSeconds: Optional[int] = None
    BudgetSecondsRemaining: Optional[int] = None
    TotalBudgetRequests: Optional[int] = None
    BudgetRequestsRemaining: Optional[int] = None
    Sli: Optional[ServiceLevelIndicatorTypeDef] = None
    RequestBasedSli: Optional[RequestBasedServiceLevelIndicatorTypeDef] = None
    Goal: Optional[GoalOutputTypeDef] = None


class ServiceLevelObjectiveTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    CreatedTime: datetime
    LastUpdatedTime: datetime
    Goal: GoalOutputTypeDef
    Description: Optional[str] = None
    Sli: Optional[ServiceLevelIndicatorTypeDef] = None
    RequestBasedSli: Optional[RequestBasedServiceLevelIndicatorTypeDef] = None
    EvaluationType: Optional[EvaluationTypeType] = None
    BurnRateConfigurations: Optional[List[BurnRateConfigurationTypeDef]] = None


class MetricDataQueryUnionTypeDef(BaseValidatorModel):
    pass


class MonitoredRequestCountMetricDataQueriesTypeDef(BaseValidatorModel):
    GoodCountMetric: Optional[Sequence[MetricDataQueryUnionTypeDef]] = None
    BadCountMetric: Optional[Sequence[MetricDataQueryTypeDef]] = None


class ServiceLevelIndicatorMetricConfigTypeDef(BaseValidatorModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None
    Statistic: Optional[str] = None
    PeriodSeconds: Optional[int] = None
    MetricDataQueries: Optional[Sequence[MetricDataQueryUnionTypeDef]] = None


class BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef(BaseValidatorModel):
    Timestamp: datetime
    Reports: List[ServiceLevelObjectiveBudgetReportTypeDef]
    Errors: List[ServiceLevelObjectiveBudgetReportErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateServiceLevelObjectiveOutputTypeDef(BaseValidatorModel):
    Slo: ServiceLevelObjectiveTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetServiceLevelObjectiveOutputTypeDef(BaseValidatorModel):
    Slo: ServiceLevelObjectiveTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateServiceLevelObjectiveOutputTypeDef(BaseValidatorModel):
    Slo: ServiceLevelObjectiveTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ServiceLevelIndicatorConfigTypeDef(BaseValidatorModel):
    SliMetricConfig: ServiceLevelIndicatorMetricConfigTypeDef
    MetricThreshold: float
    ComparisonOperator: ServiceLevelIndicatorComparisonOperatorType


class MonitoredRequestCountMetricDataQueriesUnionTypeDef(BaseValidatorModel):
    pass


class RequestBasedServiceLevelIndicatorMetricConfigTypeDef(BaseValidatorModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None
    TotalRequestCountMetric: Optional[Sequence[MetricDataQueryUnionTypeDef]] = None
    MonitoredRequestCountMetric: Optional[MonitoredRequestCountMetricDataQueriesUnionTypeDef] = None


class RequestBasedServiceLevelIndicatorConfigTypeDef(BaseValidatorModel):
    RequestBasedSliMetricConfig: RequestBasedServiceLevelIndicatorMetricConfigTypeDef
    MetricThreshold: Optional[float] = None
    ComparisonOperator: Optional[ServiceLevelIndicatorComparisonOperatorType] = None


class GoalUnionTypeDef(BaseValidatorModel):
    pass


class CreateServiceLevelObjectiveInputTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    SliConfig: Optional[ServiceLevelIndicatorConfigTypeDef] = None
    RequestBasedSliConfig: Optional[RequestBasedServiceLevelIndicatorConfigTypeDef] = None
    Goal: Optional[GoalUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    BurnRateConfigurations: Optional[Sequence[BurnRateConfigurationTypeDef]] = None


class UpdateServiceLevelObjectiveInputTypeDef(BaseValidatorModel):
    Id: str
    Description: Optional[str] = None
    SliConfig: Optional[ServiceLevelIndicatorConfigTypeDef] = None
    RequestBasedSliConfig: Optional[RequestBasedServiceLevelIndicatorConfigTypeDef] = None
    Goal: Optional[GoalUnionTypeDef] = None
    BurnRateConfigurations: Optional[Sequence[BurnRateConfigurationTypeDef]] = None


