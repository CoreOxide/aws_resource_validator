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
from aws_resource_validator.pydantic_models.rum_constants import *

class AppMonitorConfigurationTypeDef(BaseModel):
    AllowCookies: Optional[bool] = None
    EnableXRay: Optional[bool] = None
    ExcludedPages: Optional[Sequence[str]] = None
    FavoritePages: Optional[Sequence[str]] = None
    GuestRoleArn: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    IncludedPages: Optional[Sequence[str]] = None
    SessionSampleRate: Optional[float] = None
    Telemetries: Optional[Sequence[TelemetryType]] = None

class AppMonitorDetailsTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None

class AppMonitorSummaryTypeDef(BaseModel):
    Created: Optional[str] = None
    Id: Optional[str] = None
    LastModified: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[StateEnumType] = None

class CustomEventsTypeDef(BaseModel):
    Status: Optional[CustomEventsStatusType] = None

class MetricDefinitionRequestTypeDef(BaseModel):
    Name: str
    DimensionKeys: Optional[Mapping[str, str]] = None
    EventPattern: Optional[str] = None
    Namespace: Optional[str] = None
    UnitLabel: Optional[str] = None
    ValueKey: Optional[str] = None

class MetricDefinitionTypeDef(BaseModel):
    MetricDefinitionId: str
    Name: str
    DimensionKeys: Optional[Dict[str, str]] = None
    EventPattern: Optional[str] = None
    Namespace: Optional[str] = None
    UnitLabel: Optional[str] = None
    ValueKey: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDeleteRumMetricDefinitionsErrorTypeDef(BaseModel):
    ErrorCode: str
    ErrorMessage: str
    MetricDefinitionId: str

class BatchDeleteRumMetricDefinitionsRequestRequestTypeDef(BaseModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinitionIds: Sequence[str]
    DestinationArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class BatchGetRumMetricDefinitionsRequestRequestTypeDef(BaseModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class CwLogTypeDef(BaseModel):
    CwLogEnabled: Optional[bool] = None
    CwLogGroup: Optional[str] = None

class DeleteAppMonitorRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteRumMetricsDestinationRequestRequestTypeDef(BaseModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None

class QueryFilterTypeDef(BaseModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class TimeRangeTypeDef(BaseModel):
    After: int
    Before: Optional[int] = None

class GetAppMonitorRequestRequestTypeDef(BaseModel):
    Name: str

class ListAppMonitorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRumMetricsDestinationsRequestRequestTypeDef(BaseModel):
    AppMonitorName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MetricDestinationSummaryTypeDef(BaseModel):
    Destination: Optional[MetricDestinationType] = None
    DestinationArn: Optional[str] = None
    IamRoleArn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class UserDetailsTypeDef(BaseModel):
    sessionId: Optional[str] = None
    userId: Optional[str] = None

class PutRumMetricsDestinationRequestRequestTypeDef(BaseModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    IamRoleArn: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateAppMonitorRequestRequestTypeDef(BaseModel):
    Domain: str
    Name: str
    AppMonitorConfiguration: Optional[AppMonitorConfigurationTypeDef] = None
    CustomEvents: Optional[CustomEventsTypeDef] = None
    CwLogEnabled: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateAppMonitorRequestRequestTypeDef(BaseModel):
    Name: str
    AppMonitorConfiguration: Optional[AppMonitorConfigurationTypeDef] = None
    CustomEvents: Optional[CustomEventsTypeDef] = None
    CwLogEnabled: Optional[bool] = None
    Domain: Optional[str] = None

class BatchCreateRumMetricDefinitionsErrorTypeDef(BaseModel):
    ErrorCode: str
    ErrorMessage: str
    MetricDefinition: MetricDefinitionRequestTypeDef

class BatchCreateRumMetricDefinitionsRequestRequestTypeDef(BaseModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinitions: Sequence[MetricDefinitionRequestTypeDef]
    DestinationArn: Optional[str] = None

class UpdateRumMetricDefinitionRequestRequestTypeDef(BaseModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinition: MetricDefinitionRequestTypeDef
    MetricDefinitionId: str
    DestinationArn: Optional[str] = None

class BatchGetRumMetricDefinitionsResponseTypeDef(BaseModel):
    MetricDefinitions: List[MetricDefinitionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppMonitorResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppMonitorDataResponseTypeDef(BaseModel):
    Events: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppMonitorsResponseTypeDef(BaseModel):
    AppMonitorSummaries: List[AppMonitorSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    ResourceArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteRumMetricDefinitionsResponseTypeDef(BaseModel):
    Errors: List[BatchDeleteRumMetricDefinitionsErrorTypeDef]
    MetricDefinitionIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetRumMetricDefinitionsRequestBatchGetRumMetricDefinitionsPaginateTypeDef(BaseModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppMonitorsRequestListAppMonitorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRumMetricsDestinationsRequestListRumMetricsDestinationsPaginateTypeDef(BaseModel):
    AppMonitorName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DataStorageTypeDef(BaseModel):
    CwLog: Optional[CwLogTypeDef] = None

class GetAppMonitorDataRequestGetAppMonitorDataPaginateTypeDef(BaseModel):
    Name: str
    TimeRange: TimeRangeTypeDef
    Filters: Optional[Sequence[QueryFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAppMonitorDataRequestRequestTypeDef(BaseModel):
    Name: str
    TimeRange: TimeRangeTypeDef
    Filters: Optional[Sequence[QueryFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRumMetricsDestinationsResponseTypeDef(BaseModel):
    Destinations: List[MetricDestinationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RumEventTypeDef(BaseModel):
    details: str
    id: str
    timestamp: TimestampTypeDef
    type: str
    metadata: Optional[str] = None

class BatchCreateRumMetricDefinitionsResponseTypeDef(BaseModel):
    Errors: List[BatchCreateRumMetricDefinitionsErrorTypeDef]
    MetricDefinitions: List[MetricDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AppMonitorTypeDef(BaseModel):
    AppMonitorConfiguration: Optional[AppMonitorConfigurationTypeDef] = None
    Created: Optional[str] = None
    CustomEvents: Optional[CustomEventsTypeDef] = None
    DataStorage: Optional[DataStorageTypeDef] = None
    Domain: Optional[str] = None
    Id: Optional[str] = None
    LastModified: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[StateEnumType] = None
    Tags: Optional[Dict[str, str]] = None

class PutRumEventsRequestRequestTypeDef(BaseModel):
    AppMonitorDetails: AppMonitorDetailsTypeDef
    BatchId: str
    Id: str
    RumEvents: Sequence[RumEventTypeDef]
    UserDetails: UserDetailsTypeDef

class GetAppMonitorResponseTypeDef(BaseModel):
    AppMonitor: AppMonitorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

