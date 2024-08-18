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
from aws_resource_validator.pydantic_models.rum_constants import *

class AppMonitorConfigurationTypeDef(BaseValidatorModel):
    AllowCookies: Optional[bool] = None
    EnableXRay: Optional[bool] = None
    ExcludedPages: Optional[Sequence[str]] = None
    FavoritePages: Optional[Sequence[str]] = None
    GuestRoleArn: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    IncludedPages: Optional[Sequence[str]] = None
    SessionSampleRate: Optional[float] = None
    Telemetries: Optional[Sequence[TelemetryType]] = None

class AppMonitorDetailsTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None

class AppMonitorSummaryTypeDef(BaseValidatorModel):
    Created: Optional[str] = None
    Id: Optional[str] = None
    LastModified: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[StateEnumType] = None

class CustomEventsTypeDef(BaseValidatorModel):
    Status: Optional[CustomEventsStatusType] = None

class MetricDefinitionRequestTypeDef(BaseValidatorModel):
    Name: str
    DimensionKeys: Optional[Mapping[str, str]] = None
    EventPattern: Optional[str] = None
    Namespace: Optional[str] = None
    UnitLabel: Optional[str] = None
    ValueKey: Optional[str] = None

class MetricDefinitionTypeDef(BaseValidatorModel):
    MetricDefinitionId: str
    Name: str
    DimensionKeys: Optional[Dict[str, str]] = None
    EventPattern: Optional[str] = None
    Namespace: Optional[str] = None
    UnitLabel: Optional[str] = None
    ValueKey: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDeleteRumMetricDefinitionsErrorTypeDef(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: str
    MetricDefinitionId: str

class BatchDeleteRumMetricDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinitionIds: Sequence[str]
    DestinationArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class BatchGetRumMetricDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class CwLogTypeDef(BaseValidatorModel):
    CwLogEnabled: Optional[bool] = None
    CwLogGroup: Optional[str] = None

class DeleteAppMonitorRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteRumMetricsDestinationRequestRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None

class QueryFilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class TimeRangeTypeDef(BaseValidatorModel):
    After: int
    Before: Optional[int] = None

class GetAppMonitorRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class ListAppMonitorsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRumMetricsDestinationsRequestRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MetricDestinationSummaryTypeDef(BaseValidatorModel):
    Destination: Optional[MetricDestinationType] = None
    DestinationArn: Optional[str] = None
    IamRoleArn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class UserDetailsTypeDef(BaseValidatorModel):
    sessionId: Optional[str] = None
    userId: Optional[str] = None

class PutRumMetricsDestinationRequestRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    IamRoleArn: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateAppMonitorRequestRequestTypeDef(BaseValidatorModel):
    Domain: str
    Name: str
    AppMonitorConfiguration: Optional[AppMonitorConfigurationTypeDef] = None
    CustomEvents: Optional[CustomEventsTypeDef] = None
    CwLogEnabled: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateAppMonitorRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    AppMonitorConfiguration: Optional[AppMonitorConfigurationTypeDef] = None
    CustomEvents: Optional[CustomEventsTypeDef] = None
    CwLogEnabled: Optional[bool] = None
    Domain: Optional[str] = None

class BatchCreateRumMetricDefinitionsErrorTypeDef(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: str
    MetricDefinition: MetricDefinitionRequestTypeDef

class BatchCreateRumMetricDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinitions: Sequence[MetricDefinitionRequestTypeDef]
    DestinationArn: Optional[str] = None

class UpdateRumMetricDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinition: MetricDefinitionRequestTypeDef
    MetricDefinitionId: str
    DestinationArn: Optional[str] = None

class BatchGetRumMetricDefinitionsResponseTypeDef(BaseValidatorModel):
    MetricDefinitions: List[MetricDefinitionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppMonitorResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppMonitorDataResponseTypeDef(BaseValidatorModel):
    Events: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppMonitorsResponseTypeDef(BaseValidatorModel):
    AppMonitorSummaries: List[AppMonitorSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteRumMetricDefinitionsResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchDeleteRumMetricDefinitionsErrorTypeDef]
    MetricDefinitionIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetRumMetricDefinitionsRequestBatchGetRumMetricDefinitionsPaginateTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppMonitorsRequestListAppMonitorsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRumMetricsDestinationsRequestListRumMetricsDestinationsPaginateTypeDef(BaseValidatorModel):
    AppMonitorName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DataStorageTypeDef(BaseValidatorModel):
    CwLog: Optional[CwLogTypeDef] = None

class GetAppMonitorDataRequestGetAppMonitorDataPaginateTypeDef(BaseValidatorModel):
    Name: str
    TimeRange: TimeRangeTypeDef
    Filters: Optional[Sequence[QueryFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAppMonitorDataRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    TimeRange: TimeRangeTypeDef
    Filters: Optional[Sequence[QueryFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRumMetricsDestinationsResponseTypeDef(BaseValidatorModel):
    Destinations: List[MetricDestinationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RumEventTypeDef(BaseValidatorModel):
    details: str
    id: str
    timestamp: TimestampTypeDef
    type: str
    metadata: Optional[str] = None

class BatchCreateRumMetricDefinitionsResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchCreateRumMetricDefinitionsErrorTypeDef]
    MetricDefinitions: List[MetricDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AppMonitorTypeDef(BaseValidatorModel):
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

class PutRumEventsRequestRequestTypeDef(BaseValidatorModel):
    AppMonitorDetails: AppMonitorDetailsTypeDef
    BatchId: str
    Id: str
    RumEvents: Sequence[RumEventTypeDef]
    UserDetails: UserDetailsTypeDef

class GetAppMonitorResponseTypeDef(BaseValidatorModel):
    AppMonitor: AppMonitorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

