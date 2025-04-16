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

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ServiceLevelObjectiveBudgetReportError(BaseValidatorModel):
    Name: str
    Arn: str
    ErrorCode: str
    ErrorMessage: str


class BurnRateConfiguration(BaseValidatorModel):
    LookBackWindowMinutes: int


class CalendarIntervalOutput(BaseValidatorModel):
    StartTime: datetime
    DurationUnit: DurationUnitType
    Duration: int


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class DeleteServiceLevelObjectiveInput(BaseValidatorModel):
    Id: str


class Dimension(BaseValidatorModel):
    Name: str
    Value: str


class GetServiceLevelObjectiveInput(BaseValidatorModel):
    Id: str


class RollingInterval(BaseValidatorModel):
    DurationUnit: DurationUnitType
    Duration: int


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListServiceLevelObjectivesInput(BaseValidatorModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    SloOwnerAwsAccountId: Optional[str] = None


class ServiceLevelObjectiveSummary(BaseValidatorModel):
    Arn: str
    Name: str
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    CreatedTime: Optional[datetime] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class Timestamp(BaseValidatorModel):
    pass


class BatchGetServiceLevelObjectiveBudgetReportInput(BaseValidatorModel):
    Timestamp: Timestamp
    SloIds: Sequence[str]


class CalendarInterval(BaseValidatorModel):
    StartTime: Timestamp
    DurationUnit: DurationUnitType
    Duration: int


class GetServiceInput(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Mapping[str, str]


class ListServiceDependenciesInput(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Mapping[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServiceDependentsInput(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Mapping[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServiceOperationsInput(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Mapping[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServicesInput(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    AwsAccountId: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class MetricOutput(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[Dimension]] = None


class MetricReference(BaseValidatorModel):
    Namespace: str
    MetricType: str
    MetricName: str
    Dimensions: Optional[List[Dimension]] = None
    AccountId: Optional[str] = None


class Metric(BaseValidatorModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[Dimension]] = None


class IntervalOutput(BaseValidatorModel):
    RollingInterval: Optional[RollingInterval] = None
    CalendarInterval: Optional[CalendarIntervalOutput] = None


class ListServiceDependenciesInputPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Mapping[str, str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceDependentsInputPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Mapping[str, str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceLevelObjectivesInputPaginate(BaseValidatorModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    SloOwnerAwsAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceOperationsInputPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Mapping[str, str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicesInputPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    IncludeLinkedAccounts: Optional[bool] = None
    AwsAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceLevelObjectivesOutput(BaseValidatorModel):
    SloSummaries: List[ServiceLevelObjectiveSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Interval(BaseValidatorModel):
    RollingInterval: Optional[RollingInterval] = None
    CalendarInterval: Optional[CalendarInterval] = None


class MetricStatOutput(BaseValidatorModel):
    Metric: MetricOutput
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class ServiceDependency(BaseValidatorModel):
    OperationName: str
    DependencyKeyAttributes: Dict[str, str]
    DependencyOperationName: str
    MetricReferences: List[MetricReference]


class ServiceDependent(BaseValidatorModel):
    DependentKeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReference]
    OperationName: Optional[str] = None
    DependentOperationName: Optional[str] = None


class ServiceOperation(BaseValidatorModel):
    Name: str
    MetricReferences: List[MetricReference]


class ServiceSummary(BaseValidatorModel):
    KeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReference]
    AttributeMaps: Optional[List[Dict[str, str]]] = None


class Service(BaseValidatorModel):
    KeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReference]
    AttributeMaps: Optional[List[Dict[str, str]]] = None
    LogGroupReferences: Optional[List[Dict[str, str]]] = None


class GoalOutput(BaseValidatorModel):
    Interval: Optional[IntervalOutput] = None
    AttainmentGoal: Optional[float] = None
    WarningThreshold: Optional[float] = None


class Goal(BaseValidatorModel):
    Interval: Optional[Interval] = None
    AttainmentGoal: Optional[float] = None
    WarningThreshold: Optional[float] = None


class MetricDataQueryOutput(BaseValidatorModel):
    Id: str
    MetricStat: Optional[MetricStatOutput] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None


class ListServiceDependenciesOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceDependencies: List[ServiceDependency]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListServiceDependentsOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceDependents: List[ServiceDependent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListServiceOperationsOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceOperations: List[ServiceOperation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListServicesOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceSummaries: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetServiceOutput(BaseValidatorModel):
    Service: Service
    StartTime: datetime
    EndTime: datetime
    LogGroupReferences: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata


class MetricUnion(BaseValidatorModel):
    pass


class MetricStat(BaseValidatorModel):
    Metric: MetricUnion
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None


class MonitoredRequestCountMetricDataQueriesOutput(BaseValidatorModel):
    GoodCountMetric: Optional[List[MetricDataQueryOutput]] = None
    BadCountMetric: Optional[List[MetricDataQueryOutput]] = None


class ServiceLevelIndicatorMetric(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryOutput]
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None


class RequestBasedServiceLevelIndicatorMetric(BaseValidatorModel):
    TotalRequestCountMetric: List[MetricDataQueryOutput]
    MonitoredRequestCountMetric: MonitoredRequestCountMetricDataQueriesOutput
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None


class ServiceLevelIndicator(BaseValidatorModel):
    SliMetric: ServiceLevelIndicatorMetric
    MetricThreshold: float
    ComparisonOperator: ServiceLevelIndicatorComparisonOperatorType


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


class RequestBasedServiceLevelIndicator(BaseValidatorModel):
    RequestBasedSliMetric: RequestBasedServiceLevelIndicatorMetric
    MetricThreshold: Optional[float] = None
    ComparisonOperator: Optional[ServiceLevelIndicatorComparisonOperatorType] = None


class ServiceLevelObjectiveBudgetReport(BaseValidatorModel):
    Arn: str
    Name: str
    BudgetStatus: ServiceLevelObjectiveBudgetStatusType
    EvaluationType: Optional[EvaluationTypeType] = None
    Attainment: Optional[float] = None
    TotalBudgetSeconds: Optional[int] = None
    BudgetSecondsRemaining: Optional[int] = None
    TotalBudgetRequests: Optional[int] = None
    BudgetRequestsRemaining: Optional[int] = None
    Sli: Optional[ServiceLevelIndicator] = None
    RequestBasedSli: Optional[RequestBasedServiceLevelIndicator] = None
    Goal: Optional[GoalOutput] = None


class ServiceLevelObjective(BaseValidatorModel):
    Arn: str
    Name: str
    CreatedTime: datetime
    LastUpdatedTime: datetime
    Goal: GoalOutput
    Description: Optional[str] = None
    Sli: Optional[ServiceLevelIndicator] = None
    RequestBasedSli: Optional[RequestBasedServiceLevelIndicator] = None
    EvaluationType: Optional[EvaluationTypeType] = None
    BurnRateConfigurations: Optional[List[BurnRateConfiguration]] = None


class MetricDataQueryUnion(BaseValidatorModel):
    pass


class MonitoredRequestCountMetricDataQueries(BaseValidatorModel):
    GoodCountMetric: Optional[Sequence[MetricDataQueryUnion]] = None
    BadCountMetric: Optional[Sequence[MetricDataQuery]] = None


class ServiceLevelIndicatorMetricConfig(BaseValidatorModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None
    Statistic: Optional[str] = None
    PeriodSeconds: Optional[int] = None
    MetricDataQueries: Optional[Sequence[MetricDataQueryUnion]] = None


class BatchGetServiceLevelObjectiveBudgetReportOutput(BaseValidatorModel):
    Timestamp: datetime
    Reports: List[ServiceLevelObjectiveBudgetReport]
    Errors: List[ServiceLevelObjectiveBudgetReportError]
    ResponseMetadata: ResponseMetadata


class CreateServiceLevelObjectiveOutput(BaseValidatorModel):
    Slo: ServiceLevelObjective
    ResponseMetadata: ResponseMetadata


class GetServiceLevelObjectiveOutput(BaseValidatorModel):
    Slo: ServiceLevelObjective
    ResponseMetadata: ResponseMetadata


class UpdateServiceLevelObjectiveOutput(BaseValidatorModel):
    Slo: ServiceLevelObjective
    ResponseMetadata: ResponseMetadata


class ServiceLevelIndicatorConfig(BaseValidatorModel):
    SliMetricConfig: ServiceLevelIndicatorMetricConfig
    MetricThreshold: float
    ComparisonOperator: ServiceLevelIndicatorComparisonOperatorType


class MonitoredRequestCountMetricDataQueriesUnion(BaseValidatorModel):
    pass


class RequestBasedServiceLevelIndicatorMetricConfig(BaseValidatorModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None
    TotalRequestCountMetric: Optional[Sequence[MetricDataQueryUnion]] = None
    MonitoredRequestCountMetric: Optional[MonitoredRequestCountMetricDataQueriesUnion] = None


class RequestBasedServiceLevelIndicatorConfig(BaseValidatorModel):
    RequestBasedSliMetricConfig: RequestBasedServiceLevelIndicatorMetricConfig
    MetricThreshold: Optional[float] = None
    ComparisonOperator: Optional[ServiceLevelIndicatorComparisonOperatorType] = None


class GoalUnion(BaseValidatorModel):
    pass


class CreateServiceLevelObjectiveInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    SliConfig: Optional[ServiceLevelIndicatorConfig] = None
    RequestBasedSliConfig: Optional[RequestBasedServiceLevelIndicatorConfig] = None
    Goal: Optional[GoalUnion] = None
    Tags: Optional[Sequence[Tag]] = None
    BurnRateConfigurations: Optional[Sequence[BurnRateConfiguration]] = None


class UpdateServiceLevelObjectiveInput(BaseValidatorModel):
    Id: str
    Description: Optional[str] = None
    SliConfig: Optional[ServiceLevelIndicatorConfig] = None
    RequestBasedSliConfig: Optional[RequestBasedServiceLevelIndicatorConfig] = None
    Goal: Optional[GoalUnion] = None
    BurnRateConfigurations: Optional[Sequence[BurnRateConfiguration]] = None


