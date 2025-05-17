from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.application_signals.application_signals_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Timestamp = Union[datetime, str]


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


# This class is the input for the 'get_service_level_objective' function.
class GetServiceLevelObjectiveInput(BaseValidatorModel):
    Id: str


class RollingInterval(BaseValidatorModel):
    DurationUnit: DurationUnitType
    Duration: int


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_service_level_objectives' function.
class ListServiceLevelObjectivesInput(BaseValidatorModel):
    KeyAttributes: Optional[Dict[str, str]] = None
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'batch_get_service_level_objective_budget_report' function.
class BatchGetServiceLevelObjectiveBudgetReportInput(BaseValidatorModel):
    Timestamp: Timestamp
    SloIds: List[str]


class CalendarInterval(BaseValidatorModel):
    StartTime: Timestamp
    DurationUnit: DurationUnitType
    Duration: int


# This class is the input for the 'get_service' function.
class GetServiceInput(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Dict[str, str]


# This class is the input for the 'list_service_dependencies' function.
class ListServiceDependenciesInput(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Dict[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_service_dependents' function.
class ListServiceDependentsInput(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Dict[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_service_operations' function.
class ListServiceOperationsInput(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Dict[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_services' function.
class ListServicesInput(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    AwsAccountId: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


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
    Dimensions: Optional[List[Dimension]] = None


class IntervalOutput(BaseValidatorModel):
    RollingInterval: Optional[RollingInterval] = None
    CalendarInterval: Optional[CalendarIntervalOutput] = None


class ListServiceDependenciesInputPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Dict[str, str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceDependentsInputPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Dict[str, str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceLevelObjectivesInputPaginate(BaseValidatorModel):
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    SloOwnerAwsAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceOperationsInputPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    KeyAttributes: Dict[str, str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicesInputPaginate(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp
    IncludeLinkedAccounts: Optional[bool] = None
    AwsAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_service_level_objectives' function.
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

MetricUnion = Union[Metric, MetricOutput]


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


# This class is the output for the 'list_service_dependencies' function.
class ListServiceDependenciesOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceDependencies: List[ServiceDependency]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_service_dependents' function.
class ListServiceDependentsOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceDependents: List[ServiceDependent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_service_operations' function.
class ListServiceOperationsOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceOperations: List[ServiceOperation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_services' function.
class ListServicesOutput(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ServiceSummaries: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_service' function.
class GetServiceOutput(BaseValidatorModel):
    Service: Service
    StartTime: datetime
    EndTime: datetime
    LogGroupReferences: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata


class MetricStat(BaseValidatorModel):
    Metric: MetricUnion
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None

GoalUnion = Union[Goal, GoalOutput]


class MonitoredRequestCountMetricDataQueriesOutput(BaseValidatorModel):
    GoodCountMetric: Optional[List[MetricDataQueryOutput]] = None
    BadCountMetric: Optional[List[MetricDataQueryOutput]] = None


class ServiceLevelIndicatorMetric(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryOutput]
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None

MetricStatUnion = Union[MetricStat, MetricStatOutput]


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

MetricDataQueryUnion = Union[MetricDataQuery, MetricDataQueryOutput]


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


class MonitoredRequestCountMetricDataQueries(BaseValidatorModel):
    GoodCountMetric: Optional[List[MetricDataQueryUnion]] = None
    BadCountMetric: Optional[List[MetricDataQuery]] = None


class ServiceLevelIndicatorMetricConfig(BaseValidatorModel):
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None
    Statistic: Optional[str] = None
    PeriodSeconds: Optional[int] = None
    MetricDataQueries: Optional[List[MetricDataQueryUnion]] = None


# This class is the output for the 'batch_get_service_level_objective_budget_report' function.
class BatchGetServiceLevelObjectiveBudgetReportOutput(BaseValidatorModel):
    Timestamp: datetime
    Reports: List[ServiceLevelObjectiveBudgetReport]
    Errors: List[ServiceLevelObjectiveBudgetReportError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_service_level_objective' function.
class CreateServiceLevelObjectiveOutput(BaseValidatorModel):
    Slo: ServiceLevelObjective
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_level_objective' function.
class GetServiceLevelObjectiveOutput(BaseValidatorModel):
    Slo: ServiceLevelObjective
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service_level_objective' function.
class UpdateServiceLevelObjectiveOutput(BaseValidatorModel):
    Slo: ServiceLevelObjective
    ResponseMetadata: ResponseMetadata

MonitoredRequestCountMetricDataQueriesUnion = Union[MonitoredRequestCountMetricDataQueries, MonitoredRequestCountMetricDataQueriesOutput]


class ServiceLevelIndicatorConfig(BaseValidatorModel):
    SliMetricConfig: ServiceLevelIndicatorMetricConfig
    MetricThreshold: float
    ComparisonOperator: ServiceLevelIndicatorComparisonOperatorType


class RequestBasedServiceLevelIndicatorMetricConfig(BaseValidatorModel):
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None
    TotalRequestCountMetric: Optional[List[MetricDataQueryUnion]] = None
    MonitoredRequestCountMetric: Optional[MonitoredRequestCountMetricDataQueriesUnion] = None


class RequestBasedServiceLevelIndicatorConfig(BaseValidatorModel):
    RequestBasedSliMetricConfig: RequestBasedServiceLevelIndicatorMetricConfig
    MetricThreshold: Optional[float] = None
    ComparisonOperator: Optional[ServiceLevelIndicatorComparisonOperatorType] = None


# This class is the input for the 'create_service_level_objective' function.
class CreateServiceLevelObjectiveInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    SliConfig: Optional[ServiceLevelIndicatorConfig] = None
    RequestBasedSliConfig: Optional[RequestBasedServiceLevelIndicatorConfig] = None
    Goal: Optional[GoalUnion] = None
    Tags: Optional[List[Tag]] = None
    BurnRateConfigurations: Optional[List[BurnRateConfiguration]] = None


# This class is the input for the 'update_service_level_objective' function.
class UpdateServiceLevelObjectiveInput(BaseValidatorModel):
    Id: str
    Description: Optional[str] = None
    SliConfig: Optional[ServiceLevelIndicatorConfig] = None
    RequestBasedSliConfig: Optional[RequestBasedServiceLevelIndicatorConfig] = None
    Goal: Optional[GoalUnion] = None
    BurnRateConfigurations: Optional[List[BurnRateConfiguration]] = None