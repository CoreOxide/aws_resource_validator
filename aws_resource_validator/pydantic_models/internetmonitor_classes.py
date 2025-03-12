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
from aws_resource_validator.pydantic_models.internetmonitor_constants import *

class AvailabilityMeasurementTypeDef(BaseValidatorModel):
    ExperienceScore: Optional[float] = None
    PercentOfTotalTrafficImpacted: Optional[float] = None
    PercentOfClientLocationImpacted: Optional[float] = None


class ClientLocationTypeDef(BaseValidatorModel):
    ASName: str
    ASNumber: int
    Country: str
    City: str
    Latitude: float
    Longitude: float
    Subdivision: Optional[str] = None
    Metro: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteMonitorInputTypeDef(BaseValidatorModel):
    MonitorName: str


class FilterParameterTypeDef(BaseValidatorModel):
    Field: Optional[str] = None
    Operator: Optional[OperatorType] = None
    Values: Optional[Sequence[str]] = None


class GetHealthEventInputTypeDef(BaseValidatorModel):
    MonitorName: str
    EventId: str
    LinkedAccountId: Optional[str] = None


class GetInternetEventInputTypeDef(BaseValidatorModel):
    EventId: str


class GetMonitorInputTypeDef(BaseValidatorModel):
    MonitorName: str
    LinkedAccountId: Optional[str] = None


class GetQueryResultsInputTypeDef(BaseValidatorModel):
    MonitorName: str
    QueryId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetQueryStatusInputTypeDef(BaseValidatorModel):
    MonitorName: str
    QueryId: str


class LocalHealthEventsConfigTypeDef(BaseValidatorModel):
    Status: Optional[LocalHealthEventsConfigStatusType] = None
    HealthScoreThreshold: Optional[float] = None
    MinTrafficImpact: Optional[float] = None


class S3ConfigTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    BucketPrefix: Optional[str] = None
    LogDeliveryStatus: Optional[LogDeliveryStatusType] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListMonitorsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    MonitorStatus: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None


class MonitorTypeDef(BaseValidatorModel):
    MonitorName: str
    MonitorArn: str
    Status: MonitorConfigStateType
    ProcessingStatus: Optional[MonitorProcessingStatusCodeType] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class NetworkTypeDef(BaseValidatorModel):
    ASName: str
    ASNumber: int


class RoundTripTimeTypeDef(BaseValidatorModel):
    P50: Optional[float] = None
    P90: Optional[float] = None
    P95: Optional[float] = None


class StopQueryInputTypeDef(BaseValidatorModel):
    MonitorName: str
    QueryId: str


class TagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class InternetEventSummaryTypeDef(BaseValidatorModel):
    EventId: str
    EventArn: str
    StartedAt: datetime
    ClientLocation: ClientLocationTypeDef
    EventType: InternetEventTypeType
    EventStatus: InternetEventStatusType
    EndedAt: Optional[datetime] = None


class CreateMonitorOutputTypeDef(BaseValidatorModel):
    Arn: str
    Status: MonitorConfigStateType
    ResponseMetadata: ResponseMetadataTypeDef


class GetInternetEventOutputTypeDef(BaseValidatorModel):
    EventId: str
    EventArn: str
    StartedAt: datetime
    EndedAt: datetime
    ClientLocation: ClientLocationTypeDef
    EventType: InternetEventTypeType
    EventStatus: InternetEventStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueryStatusOutputTypeDef(BaseValidatorModel):
    Status: QueryStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartQueryOutputTypeDef(BaseValidatorModel):
    QueryId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMonitorOutputTypeDef(BaseValidatorModel):
    MonitorArn: str
    Status: MonitorConfigStateType
    ResponseMetadata: ResponseMetadataTypeDef


class QueryFieldTypeDef(BaseValidatorModel):
    pass


class GetQueryResultsOutputTypeDef(BaseValidatorModel):
    Fields: List[QueryFieldTypeDef]
    Data: List[List[str]]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class HealthEventsConfigTypeDef(BaseValidatorModel):
    AvailabilityScoreThreshold: Optional[float] = None
    PerformanceScoreThreshold: Optional[float] = None
    AvailabilityLocalHealthEventsConfig: Optional[LocalHealthEventsConfigTypeDef] = None
    PerformanceLocalHealthEventsConfig: Optional[LocalHealthEventsConfigTypeDef] = None


class InternetMeasurementsLogDeliveryTypeDef(BaseValidatorModel):
    S3Config: Optional[S3ConfigTypeDef] = None


class ListMonitorsInputPaginateTypeDef(BaseValidatorModel):
    MonitorStatus: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListHealthEventsInputPaginateTypeDef(BaseValidatorModel):
    MonitorName: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventStatus: Optional[HealthEventStatusType] = None
    LinkedAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHealthEventsInputTypeDef(BaseValidatorModel):
    MonitorName: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    EventStatus: Optional[HealthEventStatusType] = None
    LinkedAccountId: Optional[str] = None


class ListInternetEventsInputPaginateTypeDef(BaseValidatorModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventStatus: Optional[str] = None
    EventType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInternetEventsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventStatus: Optional[str] = None
    EventType: Optional[str] = None


class StartQueryInputTypeDef(BaseValidatorModel):
    MonitorName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    QueryType: QueryTypeType
    FilterParameters: Optional[Sequence[FilterParameterTypeDef]] = None
    LinkedAccountId: Optional[str] = None


class ListMonitorsOutputTypeDef(BaseValidatorModel):
    Monitors: List[MonitorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class NetworkImpairmentTypeDef(BaseValidatorModel):
    Networks: List[NetworkTypeDef]
    AsPath: List[NetworkTypeDef]
    NetworkEventType: TriangulationEventTypeType


class PerformanceMeasurementTypeDef(BaseValidatorModel):
    ExperienceScore: Optional[float] = None
    PercentOfTotalTrafficImpacted: Optional[float] = None
    PercentOfClientLocationImpacted: Optional[float] = None
    RoundTripTime: Optional[RoundTripTimeTypeDef] = None


class ListInternetEventsOutputTypeDef(BaseValidatorModel):
    InternetEvents: List[InternetEventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateMonitorInputTypeDef(BaseValidatorModel):
    MonitorName: str
    Resources: Optional[Sequence[str]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    MaxCityNetworksToMonitor: Optional[int] = None
    InternetMeasurementsLogDelivery: Optional[InternetMeasurementsLogDeliveryTypeDef] = None
    TrafficPercentageToMonitor: Optional[int] = None
    HealthEventsConfig: Optional[HealthEventsConfigTypeDef] = None


class GetMonitorOutputTypeDef(BaseValidatorModel):
    MonitorName: str
    MonitorArn: str
    Resources: List[str]
    Status: MonitorConfigStateType
    CreatedAt: datetime
    ModifiedAt: datetime
    ProcessingStatus: MonitorProcessingStatusCodeType
    ProcessingStatusInfo: str
    Tags: Dict[str, str]
    MaxCityNetworksToMonitor: int
    InternetMeasurementsLogDelivery: InternetMeasurementsLogDeliveryTypeDef
    TrafficPercentageToMonitor: int
    HealthEventsConfig: HealthEventsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMonitorInputTypeDef(BaseValidatorModel):
    MonitorName: str
    ResourcesToAdd: Optional[Sequence[str]] = None
    ResourcesToRemove: Optional[Sequence[str]] = None
    Status: Optional[MonitorConfigStateType] = None
    ClientToken: Optional[str] = None
    MaxCityNetworksToMonitor: Optional[int] = None
    InternetMeasurementsLogDelivery: Optional[InternetMeasurementsLogDeliveryTypeDef] = None
    TrafficPercentageToMonitor: Optional[int] = None
    HealthEventsConfig: Optional[HealthEventsConfigTypeDef] = None


class InternetHealthTypeDef(BaseValidatorModel):
    Availability: Optional[AvailabilityMeasurementTypeDef] = None
    Performance: Optional[PerformanceMeasurementTypeDef] = None


class ImpactedLocationTypeDef(BaseValidatorModel):
    ASName: str
    ASNumber: int
    Country: str
    Status: HealthEventStatusType
    Subdivision: Optional[str] = None
    Metro: Optional[str] = None
    City: Optional[str] = None
    Latitude: Optional[float] = None
    Longitude: Optional[float] = None
    CountryCode: Optional[str] = None
    SubdivisionCode: Optional[str] = None
    ServiceLocation: Optional[str] = None
    CausedBy: Optional[NetworkImpairmentTypeDef] = None
    InternetHealth: Optional[InternetHealthTypeDef] = None
    Ipv4Prefixes: Optional[List[str]] = None


class GetHealthEventOutputTypeDef(BaseValidatorModel):
    EventArn: str
    EventId: str
    StartedAt: datetime
    EndedAt: datetime
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ImpactedLocations: List[ImpactedLocationTypeDef]
    Status: HealthEventStatusType
    PercentOfTotalTrafficImpacted: float
    ImpactType: HealthEventImpactTypeType
    HealthScoreThreshold: float
    ResponseMetadata: ResponseMetadataTypeDef


class HealthEventTypeDef(BaseValidatorModel):
    EventArn: str
    EventId: str
    StartedAt: datetime
    LastUpdatedAt: datetime
    ImpactedLocations: List[ImpactedLocationTypeDef]
    Status: HealthEventStatusType
    ImpactType: HealthEventImpactTypeType
    EndedAt: Optional[datetime] = None
    CreatedAt: Optional[datetime] = None
    PercentOfTotalTrafficImpacted: Optional[float] = None
    HealthScoreThreshold: Optional[float] = None


class ListHealthEventsOutputTypeDef(BaseValidatorModel):
    HealthEvents: List[HealthEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


