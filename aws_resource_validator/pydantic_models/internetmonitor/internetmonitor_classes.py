from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AvailabilityMeasurement(BaseValidatorModel):
    ExperienceScore: Optional[float] = None
    PercentOfTotalTrafficImpacted: Optional[float] = None
    PercentOfClientLocationImpacted: Optional[float] = None


class ClientLocation(BaseValidatorModel):
    ASName: str
    ASNumber: int
    Country: str
    City: str
    Latitude: float
    Longitude: float
    Subdivision: Optional[str] = None
    Metro: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteMonitorInput(BaseValidatorModel):
    MonitorName: str


class FilterParameter(BaseValidatorModel):
    Field: Optional[str] = None
    Operator: Optional[OperatorType] = None
    Values: Optional[List[str]] = None


# This class is the input for the 'get_health_event' function.
class GetHealthEventInput(BaseValidatorModel):
    MonitorName: str
    EventId: str
    LinkedAccountId: Optional[str] = None


# This class is the input for the 'get_internet_event' function.
class GetInternetEventInput(BaseValidatorModel):
    EventId: str


# This class is the input for the 'get_monitor' function.
class GetMonitorInput(BaseValidatorModel):
    MonitorName: str
    LinkedAccountId: Optional[str] = None


# This class is the input for the 'get_query_results' function.
class GetQueryResultsInput(BaseValidatorModel):
    MonitorName: str
    QueryId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class QueryField(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None


# This class is the input for the 'get_query_status' function.
class GetQueryStatusInput(BaseValidatorModel):
    MonitorName: str
    QueryId: str


class LocalHealthEventsConfig(BaseValidatorModel):
    Status: Optional[LocalHealthEventsConfigStatusType] = None
    HealthScoreThreshold: Optional[float] = None
    MinTrafficImpact: Optional[float] = None


class S3Config(BaseValidatorModel):
    BucketName: Optional[str] = None
    BucketPrefix: Optional[str] = None
    LogDeliveryStatus: Optional[LogDeliveryStatusType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'list_monitors' function.
class ListMonitorsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    MonitorStatus: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None


class Monitor(BaseValidatorModel):
    MonitorName: str
    MonitorArn: str
    Status: MonitorConfigStateType
    ProcessingStatus: Optional[MonitorProcessingStatusCodeType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str


class Network(BaseValidatorModel):
    ASName: str
    ASNumber: int


class RoundTripTime(BaseValidatorModel):
    P50: Optional[float] = None
    P90: Optional[float] = None
    P95: Optional[float] = None


class StopQueryInput(BaseValidatorModel):
    MonitorName: str
    QueryId: str


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class InternetEventSummary(BaseValidatorModel):
    EventId: str
    EventArn: str
    StartedAt: datetime
    ClientLocation: ClientLocation
    EventType: InternetEventTypeType
    EventStatus: InternetEventStatusType
    EndedAt: Optional[datetime] = None


# This class is the output for the 'create_monitor' function.
class CreateMonitorOutput(BaseValidatorModel):
    Arn: str
    Status: MonitorConfigStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_internet_event' function.
class GetInternetEventOutput(BaseValidatorModel):
    EventId: str
    EventArn: str
    StartedAt: datetime
    EndedAt: datetime
    ClientLocation: ClientLocation
    EventType: InternetEventTypeType
    EventStatus: InternetEventStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_query_status' function.
class GetQueryStatusOutput(BaseValidatorModel):
    Status: QueryStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_query' function.
class StartQueryOutput(BaseValidatorModel):
    QueryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_monitor' function.
class UpdateMonitorOutput(BaseValidatorModel):
    MonitorArn: str
    Status: MonitorConfigStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_query_results' function.
class GetQueryResultsOutput(BaseValidatorModel):
    Fields: List[QueryField]
    Data: List[List[str]]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class HealthEventsConfig(BaseValidatorModel):
    AvailabilityScoreThreshold: Optional[float] = None
    PerformanceScoreThreshold: Optional[float] = None
    AvailabilityLocalHealthEventsConfig: Optional[LocalHealthEventsConfig] = None
    PerformanceLocalHealthEventsConfig: Optional[LocalHealthEventsConfig] = None


class InternetMeasurementsLogDelivery(BaseValidatorModel):
    S3Config: Optional[S3Config] = None


class ListMonitorsInputPaginate(BaseValidatorModel):
    MonitorStatus: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHealthEventsInputPaginate(BaseValidatorModel):
    MonitorName: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    EventStatus: Optional[HealthEventStatusType] = None
    LinkedAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_health_events' function.
class ListHealthEventsInput(BaseValidatorModel):
    MonitorName: str
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    EventStatus: Optional[HealthEventStatusType] = None
    LinkedAccountId: Optional[str] = None


class ListInternetEventsInputPaginate(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    EventStatus: Optional[str] = None
    EventType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_internet_events' function.
class ListInternetEventsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    EventStatus: Optional[str] = None
    EventType: Optional[str] = None


# This class is the input for the 'start_query' function.
class StartQueryInput(BaseValidatorModel):
    MonitorName: str
    StartTime: Timestamp
    EndTime: Timestamp
    QueryType: QueryTypeType
    FilterParameters: Optional[List[FilterParameter]] = None
    LinkedAccountId: Optional[str] = None


# This class is the output for the 'list_monitors' function.
class ListMonitorsOutput(BaseValidatorModel):
    Monitors: List[Monitor]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class NetworkImpairment(BaseValidatorModel):
    Networks: List[Network]
    AsPath: List[Network]
    NetworkEventType: TriangulationEventTypeType


class PerformanceMeasurement(BaseValidatorModel):
    ExperienceScore: Optional[float] = None
    PercentOfTotalTrafficImpacted: Optional[float] = None
    PercentOfClientLocationImpacted: Optional[float] = None
    RoundTripTime: Optional[RoundTripTime] = None


# This class is the output for the 'list_internet_events' function.
class ListInternetEventsOutput(BaseValidatorModel):
    InternetEvents: List[InternetEventSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_monitor' function.
class CreateMonitorInput(BaseValidatorModel):
    MonitorName: str
    Resources: Optional[List[str]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    MaxCityNetworksToMonitor: Optional[int] = None
    InternetMeasurementsLogDelivery: Optional[InternetMeasurementsLogDelivery] = None
    TrafficPercentageToMonitor: Optional[int] = None
    HealthEventsConfig: Optional[HealthEventsConfig] = None


# This class is the output for the 'get_monitor' function.
class GetMonitorOutput(BaseValidatorModel):
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
    InternetMeasurementsLogDelivery: InternetMeasurementsLogDelivery
    TrafficPercentageToMonitor: int
    HealthEventsConfig: HealthEventsConfig
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_monitor' function.
class UpdateMonitorInput(BaseValidatorModel):
    MonitorName: str
    ResourcesToAdd: Optional[List[str]] = None
    ResourcesToRemove: Optional[List[str]] = None
    Status: Optional[MonitorConfigStateType] = None
    ClientToken: Optional[str] = None
    MaxCityNetworksToMonitor: Optional[int] = None
    InternetMeasurementsLogDelivery: Optional[InternetMeasurementsLogDelivery] = None
    TrafficPercentageToMonitor: Optional[int] = None
    HealthEventsConfig: Optional[HealthEventsConfig] = None


class InternetHealth(BaseValidatorModel):
    Availability: Optional[AvailabilityMeasurement] = None
    Performance: Optional[PerformanceMeasurement] = None


class ImpactedLocation(BaseValidatorModel):
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
    CausedBy: Optional[NetworkImpairment] = None
    InternetHealth: Optional[InternetHealth] = None
    Ipv4Prefixes: Optional[List[str]] = None


# This class is the output for the 'get_health_event' function.
class GetHealthEventOutput(BaseValidatorModel):
    EventArn: str
    EventId: str
    StartedAt: datetime
    EndedAt: datetime
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ImpactedLocations: List[ImpactedLocation]
    Status: HealthEventStatusType
    PercentOfTotalTrafficImpacted: float
    ImpactType: HealthEventImpactTypeType
    HealthScoreThreshold: float
    ResponseMetadata: ResponseMetadata


class HealthEvent(BaseValidatorModel):
    EventArn: str
    EventId: str
    StartedAt: datetime
    LastUpdatedAt: datetime
    ImpactedLocations: List[ImpactedLocation]
    Status: HealthEventStatusType
    ImpactType: HealthEventImpactTypeType
    EndedAt: Optional[datetime] = None
    CreatedAt: Optional[datetime] = None
    PercentOfTotalTrafficImpacted: Optional[float] = None
    HealthScoreThreshold: Optional[float] = None


# This class is the output for the 'list_health_events' function.
class ListHealthEventsOutput(BaseValidatorModel):
    HealthEvents: List[HealthEvent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None