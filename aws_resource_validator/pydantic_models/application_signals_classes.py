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
from aws_resource_validator.pydantic_models.application_signals_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ServiceLevelObjectiveBudgetReportErrorTypeDef(BaseModel):
    Name: str
    Arn: str
    ErrorCode: str
    ErrorMessage: str

class CalendarIntervalOutputTypeDef(BaseModel):
    StartTime: datetime
    DurationUnit: DurationUnitType
    Duration: int

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class DeleteServiceLevelObjectiveInputRequestTypeDef(BaseModel):
    Id: str

class DimensionTypeDef(BaseModel):
    Name: str
    Value: str

class GetServiceLevelObjectiveInputRequestTypeDef(BaseModel):
    Id: str

class RollingIntervalTypeDef(BaseModel):
    DurationUnit: DurationUnitType
    Duration: int

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListServiceLevelObjectivesInputRequestTypeDef(BaseModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ServiceLevelObjectiveSummaryTypeDef(BaseModel):
    Arn: str
    Name: str
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    CreatedTime: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class BatchGetServiceLevelObjectiveBudgetReportInputRequestTypeDef(BaseModel):
    Timestamp: TimestampTypeDef
    SloIds: Sequence[str]

class CalendarIntervalTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    DurationUnit: DurationUnitType
    Duration: int

class GetServiceInputRequestTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]

class ListServiceDependenciesInputRequestTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListServiceDependentsInputRequestTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListServiceOperationsInputRequestTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListServicesInputRequestTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class MetricOutputTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[List[DimensionTypeDef]] = None

class MetricReferenceTypeDef(BaseModel):
    Namespace: str
    MetricType: str
    MetricName: str
    Dimensions: Optional[List[DimensionTypeDef]] = None

class MetricTypeDef(BaseModel):
    Namespace: Optional[str] = None
    MetricName: Optional[str] = None
    Dimensions: Optional[Sequence[DimensionTypeDef]] = None

class IntervalOutputTypeDef(BaseModel):
    RollingInterval: Optional[RollingIntervalTypeDef] = None
    CalendarInterval: Optional[CalendarIntervalOutputTypeDef] = None

class ListServiceDependenciesInputListServiceDependenciesPaginateTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceDependentsInputListServiceDependentsPaginateTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceLevelObjectivesInputListServiceLevelObjectivesPaginateTypeDef(BaseModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceOperationsInputListServiceOperationsPaginateTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    KeyAttributes: Mapping[str, str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesInputListServicesPaginateTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceLevelObjectivesOutputTypeDef(BaseModel):
    SloSummaries: List[ServiceLevelObjectiveSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class IntervalTypeDef(BaseModel):
    RollingInterval: Optional[RollingIntervalTypeDef] = None
    CalendarInterval: Optional[CalendarIntervalTypeDef] = None

class MetricStatOutputTypeDef(BaseModel):
    Metric: MetricOutputTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None

class ServiceDependencyTypeDef(BaseModel):
    OperationName: str
    DependencyKeyAttributes: Dict[str, str]
    DependencyOperationName: str
    MetricReferences: List[MetricReferenceTypeDef]

class ServiceDependentTypeDef(BaseModel):
    DependentKeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReferenceTypeDef]
    OperationName: Optional[str] = None
    DependentOperationName: Optional[str] = None

class ServiceOperationTypeDef(BaseModel):
    Name: str
    MetricReferences: List[MetricReferenceTypeDef]

class ServiceSummaryTypeDef(BaseModel):
    KeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReferenceTypeDef]
    AttributeMaps: Optional[List[Dict[str, str]]] = None

class ServiceTypeDef(BaseModel):
    KeyAttributes: Dict[str, str]
    MetricReferences: List[MetricReferenceTypeDef]
    AttributeMaps: Optional[List[Dict[str, str]]] = None

class MetricStatTypeDef(BaseModel):
    Metric: MetricTypeDef
    Period: int
    Stat: str
    Unit: Optional[StandardUnitType] = None

class GoalOutputTypeDef(BaseModel):
    Interval: Optional[IntervalOutputTypeDef] = None
    AttainmentGoal: Optional[float] = None
    WarningThreshold: Optional[float] = None

class GoalTypeDef(BaseModel):
    Interval: Optional[IntervalTypeDef] = None
    AttainmentGoal: Optional[float] = None
    WarningThreshold: Optional[float] = None

class MetricDataQueryOutputTypeDef(BaseModel):
    Id: str
    MetricStat: Optional[MetricStatOutputTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None

class ListServiceDependenciesOutputTypeDef(BaseModel):
    StartTime: datetime
    EndTime: datetime
    ServiceDependencies: List[ServiceDependencyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListServiceDependentsOutputTypeDef(BaseModel):
    StartTime: datetime
    EndTime: datetime
    ServiceDependents: List[ServiceDependentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListServiceOperationsOutputTypeDef(BaseModel):
    StartTime: datetime
    EndTime: datetime
    ServiceOperations: List[ServiceOperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListServicesOutputTypeDef(BaseModel):
    StartTime: datetime
    EndTime: datetime
    ServiceSummaries: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetServiceOutputTypeDef(BaseModel):
    Service: ServiceTypeDef
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class MetricDataQueryTypeDef(BaseModel):
    Id: str
    MetricStat: Optional[MetricStatTypeDef] = None
    Expression: Optional[str] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None
    Period: Optional[int] = None
    AccountId: Optional[str] = None

class ServiceLevelIndicatorMetricTypeDef(BaseModel):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]
    KeyAttributes: Optional[Dict[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None

class ServiceLevelIndicatorMetricConfigTypeDef(BaseModel):
    KeyAttributes: Optional[Mapping[str, str]] = None
    OperationName: Optional[str] = None
    MetricType: Optional[ServiceLevelIndicatorMetricTypeType] = None
    Statistic: Optional[str] = None
    PeriodSeconds: Optional[int] = None
    MetricDataQueries: Optional[Sequence[MetricDataQueryTypeDef]] = None

class ServiceLevelIndicatorTypeDef(BaseModel):
    SliMetric: ServiceLevelIndicatorMetricTypeDef
    MetricThreshold: float
    ComparisonOperator: ServiceLevelIndicatorComparisonOperatorType

class ServiceLevelIndicatorConfigTypeDef(BaseModel):
    SliMetricConfig: ServiceLevelIndicatorMetricConfigTypeDef
    MetricThreshold: float
    ComparisonOperator: ServiceLevelIndicatorComparisonOperatorType

class ServiceLevelObjectiveBudgetReportTypeDef(BaseModel):
    Arn: str
    Name: str
    BudgetStatus: ServiceLevelObjectiveBudgetStatusType
    Attainment: Optional[float] = None
    TotalBudgetSeconds: Optional[int] = None
    BudgetSecondsRemaining: Optional[int] = None
    Sli: Optional[ServiceLevelIndicatorTypeDef] = None
    Goal: Optional[GoalOutputTypeDef] = None

class ServiceLevelObjectiveTypeDef(BaseModel):
    Arn: str
    Name: str
    CreatedTime: datetime
    LastUpdatedTime: datetime
    Sli: ServiceLevelIndicatorTypeDef
    Goal: GoalOutputTypeDef
    Description: Optional[str] = None

class CreateServiceLevelObjectiveInputRequestTypeDef(BaseModel):
    Name: str
    SliConfig: ServiceLevelIndicatorConfigTypeDef
    Description: Optional[str] = None
    Goal: Optional[GoalTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateServiceLevelObjectiveInputRequestTypeDef(BaseModel):
    Id: str
    Description: Optional[str] = None
    SliConfig: Optional[ServiceLevelIndicatorConfigTypeDef] = None
    Goal: Optional[GoalTypeDef] = None

class BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef(BaseModel):
    Timestamp: datetime
    Reports: List[ServiceLevelObjectiveBudgetReportTypeDef]
    Errors: List[ServiceLevelObjectiveBudgetReportErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceLevelObjectiveOutputTypeDef(BaseModel):
    Slo: ServiceLevelObjectiveTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceLevelObjectiveOutputTypeDef(BaseModel):
    Slo: ServiceLevelObjectiveTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceLevelObjectiveOutputTypeDef(BaseModel):
    Slo: ServiceLevelObjectiveTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

