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

class DeleteMonitorInputRequestTypeDef(BaseValidatorModel):
    MonitorName: str

class FilterParameterTypeDef(BaseValidatorModel):
    Field: Optional[str] = None
    Operator: Optional[OperatorType] = None
    Values: Optional[Sequence[str]] = None

class GetHealthEventInputRequestTypeDef(BaseValidatorModel):
    MonitorName: str
    EventId: str
    LinkedAccountId: Optional[str] = None

class GetInternetEventInputRequestTypeDef(BaseValidatorModel):
    EventId: str

class GetMonitorInputRequestTypeDef(BaseValidatorModel):
    MonitorName: str
    LinkedAccountId: Optional[str] = None

class GetQueryResultsInputRequestTypeDef(BaseValidatorModel):
    MonitorName: str
    QueryId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QueryFieldTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None

class GetQueryStatusInputRequestTypeDef(BaseValidatorModel):
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

class ListMonitorsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    MonitorStatus: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None

class MonitorTypeDef(BaseValidatorModel):
    MonitorName: str
    MonitorArn: str
    Status: MonitorConfigStateType
    ProcessingStatus: Optional[MonitorProcessingStatusCodeType] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class NetworkTypeDef(BaseValidatorModel):
    ASName: str
    ASNumber: int

class RoundTripTimeTypeDef(BaseValidatorModel):
    P50: Optional[float] = None
    P90: Optional[float] = None
    P95: Optional[float] = None

class StopQueryInputRequestTypeDef(BaseValidatorModel):
    MonitorName: str
    QueryId: str

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
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

class GetQueryResultsOutputTypeDef(BaseValidatorModel):
    Fields: List[QueryFieldTypeDef]
    Data: List[List[str]]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class HealthEventsConfigTypeDef(BaseValidatorModel):
    AvailabilityScoreThreshold: Optional[float] = None
    PerformanceScoreThreshold: Optional[float] = None
    AvailabilityLocalHealthEventsConfig: Optional[LocalHealthEventsConfigTypeDef] = None
    PerformanceLocalHealthEventsConfig: Optional[LocalHealthEventsConfigTypeDef] = None

class InternetMeasurementsLogDeliveryTypeDef(BaseValidatorModel):
    S3Config: Optional[S3ConfigTypeDef] = None

class ListMonitorsInputListMonitorsPaginateTypeDef(BaseValidatorModel):
    MonitorStatus: Optional[str] = None
    IncludeLinkedAccounts: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHealthEventsInputListHealthEventsPaginateTypeDef(BaseValidatorModel):
    MonitorName: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventStatus: Optional[HealthEventStatusType] = None
    LinkedAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHealthEventsInputRequestTypeDef(BaseValidatorModel):
    MonitorName: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    EventStatus: Optional[HealthEventStatusType] = None
    LinkedAccountId: Optional[str] = None

class ListInternetEventsInputListInternetEventsPaginateTypeDef(BaseValidatorModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventStatus: Optional[str] = None
    EventType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInternetEventsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventStatus: Optional[str] = None
    EventType: Optional[str] = None

class StartQueryInputRequestTypeDef(BaseValidatorModel):
    MonitorName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    QueryType: QueryTypeType
    FilterParameters: Optional[Sequence[FilterParameterTypeDef]] = None
    LinkedAccountId: Optional[str] = None

class ListMonitorsOutputTypeDef(BaseValidatorModel):
    Monitors: List[MonitorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMonitorInputRequestTypeDef(BaseValidatorModel):
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

class UpdateMonitorInputRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

