from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.rum.rum_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AppMonitorConfigurationOutput(BaseValidatorModel):
    AllowCookies: Optional[bool] = None
    EnableXRay: Optional[bool] = None
    ExcludedPages: Optional[List[str]] = None
    FavoritePages: Optional[List[str]] = None
    GuestRoleArn: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    IncludedPages: Optional[List[str]] = None
    SessionSampleRate: Optional[float] = None
    Telemetries: Optional[List[TelemetryType]] = None


class AppMonitorConfiguration(BaseValidatorModel):
    AllowCookies: Optional[bool] = None
    EnableXRay: Optional[bool] = None
    ExcludedPages: Optional[List[str]] = None
    FavoritePages: Optional[List[str]] = None
    GuestRoleArn: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    IncludedPages: Optional[List[str]] = None
    SessionSampleRate: Optional[float] = None
    Telemetries: Optional[List[TelemetryType]] = None


class AppMonitorDetails(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None


class AppMonitorSummary(BaseValidatorModel):
    Created: Optional[str] = None
    Id: Optional[str] = None
    LastModified: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[StateEnumType] = None


class CustomEvents(BaseValidatorModel):
    Status: Optional[CustomEventsStatusType] = None


class MetricDefinitionRequestOutput(BaseValidatorModel):
    Name: str
    DimensionKeys: Optional[Dict[str, str]] = None
    EventPattern: Optional[str] = None
    Namespace: Optional[str] = None
    UnitLabel: Optional[str] = None
    ValueKey: Optional[str] = None


class MetricDefinition(BaseValidatorModel):
    MetricDefinitionId: str
    Name: str
    DimensionKeys: Optional[Dict[str, str]] = None
    EventPattern: Optional[str] = None
    Namespace: Optional[str] = None
    UnitLabel: Optional[str] = None
    ValueKey: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeleteRumMetricDefinitionsError(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: str
    MetricDefinitionId: str


# This class is the input for the 'batch_delete_rum_metric_definitions' function.
class BatchDeleteRumMetricDefinitionsRequest(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinitionIds: List[str]
    DestinationArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'batch_get_rum_metric_definitions' function.
class BatchGetRumMetricDefinitionsRequest(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class CwLog(BaseValidatorModel):
    CwLogEnabled: Optional[bool] = None
    CwLogGroup: Optional[str] = None


class DeleteAppMonitorRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyRequest(BaseValidatorModel):
    Name: str
    PolicyRevisionId: Optional[str] = None


class DeleteRumMetricsDestinationRequest(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None


class QueryFilter(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[List[str]] = None


class TimeRange(BaseValidatorModel):
    After: int
    Before: Optional[int] = None


# This class is the input for the 'get_app_monitor' function.
class GetAppMonitorRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'list_app_monitors' function.
class ListAppMonitorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_rum_metrics_destinations' function.
class ListRumMetricsDestinationsRequest(BaseValidatorModel):
    AppMonitorName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MetricDestinationSummary(BaseValidatorModel):
    Destination: Optional[MetricDestinationType] = None
    DestinationArn: Optional[str] = None
    IamRoleArn: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class MetricDefinitionRequest(BaseValidatorModel):
    Name: str
    DimensionKeys: Optional[Dict[str, str]] = None
    EventPattern: Optional[str] = None
    Namespace: Optional[str] = None
    UnitLabel: Optional[str] = None
    ValueKey: Optional[str] = None


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    Name: str
    PolicyDocument: str
    PolicyRevisionId: Optional[str] = None


class UserDetails(BaseValidatorModel):
    sessionId: Optional[str] = None
    userId: Optional[str] = None


class PutRumMetricsDestinationRequest(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    IamRoleArn: Optional[str] = None

Timestamp = Union[datetime, str]


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]

AppMonitorConfigurationUnion = Union[AppMonitorConfiguration, AppMonitorConfigurationOutput]


class BatchCreateRumMetricDefinitionsError(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: str
    MetricDefinition: MetricDefinitionRequestOutput


# This class is the output for the 'batch_get_rum_metric_definitions' function.
class BatchGetRumMetricDefinitionsResponse(BaseValidatorModel):
    MetricDefinitions: List[MetricDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_app_monitor' function.
class CreateAppMonitorResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resource_policy' function.
class DeleteResourcePolicyResponse(BaseValidatorModel):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_app_monitor_data' function.
class GetAppMonitorDataResponse(BaseValidatorModel):
    Events: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    PolicyDocument: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_app_monitors' function.
class ListAppMonitorsResponse(BaseValidatorModel):
    AppMonitorSummaries: List[AppMonitorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResponse(BaseValidatorModel):
    PolicyDocument: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_delete_rum_metric_definitions' function.
class BatchDeleteRumMetricDefinitionsResponse(BaseValidatorModel):
    Errors: List[BatchDeleteRumMetricDefinitionsError]
    MetricDefinitionIds: List[str]
    ResponseMetadata: ResponseMetadata


class BatchGetRumMetricDefinitionsRequestPaginate(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAppMonitorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRumMetricsDestinationsRequestPaginate(BaseValidatorModel):
    AppMonitorName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DataStorage(BaseValidatorModel):
    CwLog: Optional[CwLog] = None


class GetAppMonitorDataRequestPaginate(BaseValidatorModel):
    Name: str
    TimeRange: TimeRange
    Filters: Optional[List[QueryFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_app_monitor_data' function.
class GetAppMonitorDataRequest(BaseValidatorModel):
    Name: str
    TimeRange: TimeRange
    Filters: Optional[List[QueryFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'list_rum_metrics_destinations' function.
class ListRumMetricsDestinationsResponse(BaseValidatorModel):
    Destinations: List[MetricDestinationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

MetricDefinitionRequestUnion = Union[MetricDefinitionRequest, MetricDefinitionRequestOutput]


class RumEvent(BaseValidatorModel):
    details: str
    id: str
    timestamp: Timestamp
    type: str
    metadata: Optional[str] = None


# This class is the input for the 'create_app_monitor' function.
class CreateAppMonitorRequest(BaseValidatorModel):
    Domain: str
    Name: str
    AppMonitorConfiguration: Optional[AppMonitorConfigurationUnion] = None
    CustomEvents: Optional[CustomEvents] = None
    CwLogEnabled: Optional[bool] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateAppMonitorRequest(BaseValidatorModel):
    Name: str
    AppMonitorConfiguration: Optional[AppMonitorConfigurationUnion] = None
    CustomEvents: Optional[CustomEvents] = None
    CwLogEnabled: Optional[bool] = None
    Domain: Optional[str] = None


# This class is the output for the 'batch_create_rum_metric_definitions' function.
class BatchCreateRumMetricDefinitionsResponse(BaseValidatorModel):
    Errors: List[BatchCreateRumMetricDefinitionsError]
    MetricDefinitions: List[MetricDefinition]
    ResponseMetadata: ResponseMetadata


class AppMonitor(BaseValidatorModel):
    AppMonitorConfiguration: Optional[AppMonitorConfigurationOutput] = None
    Created: Optional[str] = None
    CustomEvents: Optional[CustomEvents] = None
    DataStorage: Optional[DataStorage] = None
    Domain: Optional[str] = None
    Id: Optional[str] = None
    LastModified: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[StateEnumType] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'batch_create_rum_metric_definitions' function.
class BatchCreateRumMetricDefinitionsRequest(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinitions: List[MetricDefinitionRequestUnion]
    DestinationArn: Optional[str] = None


class UpdateRumMetricDefinitionRequest(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinition: MetricDefinitionRequestUnion
    MetricDefinitionId: str
    DestinationArn: Optional[str] = None


class PutRumEventsRequest(BaseValidatorModel):
    AppMonitorDetails: AppMonitorDetails
    BatchId: str
    Id: str
    RumEvents: List[RumEvent]
    UserDetails: UserDetails
    Alias: Optional[str] = None


# This class is the output for the 'get_app_monitor' function.
class GetAppMonitorResponse(BaseValidatorModel):
    AppMonitor: AppMonitor
    ResponseMetadata: ResponseMetadata