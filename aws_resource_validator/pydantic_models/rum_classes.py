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
from aws_resource_validator.pydantic_models.rum_constants import *

class AppMonitorConfigurationOutputTypeDef(BaseValidatorModel):
    AllowCookies: Optional[bool] = None
    EnableXRay: Optional[bool] = None
    ExcludedPages: Optional[List[str]] = None
    FavoritePages: Optional[List[str]] = None
    GuestRoleArn: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    IncludedPages: Optional[List[str]] = None
    SessionSampleRate: Optional[float] = None
    Telemetries: Optional[List[TelemetryType]] = None


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


class AppMonitorSummaryTypeDef(BaseValidatorModel):
    Created: Optional[str] = None
    Id: Optional[str] = None
    LastModified: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[StateEnumType] = None


class CustomEventsTypeDef(BaseValidatorModel):
    Status: Optional[CustomEventsStatusType] = None


class MetricDefinitionRequestOutputTypeDef(BaseValidatorModel):
    Name: str
    DimensionKeys: Optional[Dict[str, str]] = None
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
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeleteRumMetricDefinitionsErrorTypeDef(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: str
    MetricDefinitionId: str


class BatchDeleteRumMetricDefinitionsRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinitionIds: Sequence[str]
    DestinationArn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class BatchGetRumMetricDefinitionsRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class CwLogTypeDef(BaseValidatorModel):
    CwLogEnabled: Optional[bool] = None
    CwLogGroup: Optional[str] = None


class DeleteAppMonitorRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    Name: str
    PolicyRevisionId: Optional[str] = None


class DeleteRumMetricsDestinationRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None


class QueryFilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class TimeRangeTypeDef(BaseValidatorModel):
    After: int
    Before: Optional[int] = None


class GetAppMonitorRequestTypeDef(BaseValidatorModel):
    Name: str


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    Name: str


class ListAppMonitorsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRumMetricsDestinationsRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MetricDestinationSummaryTypeDef(BaseValidatorModel):
    Destination: Optional[MetricDestinationType] = None
    DestinationArn: Optional[str] = None
    IamRoleArn: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class MetricDefinitionRequestTypeDef(BaseValidatorModel):
    Name: str
    DimensionKeys: Optional[Mapping[str, str]] = None
    EventPattern: Optional[str] = None
    Namespace: Optional[str] = None
    UnitLabel: Optional[str] = None
    ValueKey: Optional[str] = None


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    Name: str
    PolicyDocument: str
    PolicyRevisionId: Optional[str] = None


class UserDetailsTypeDef(BaseValidatorModel):
    sessionId: Optional[str] = None
    userId: Optional[str] = None


class PutRumMetricsDestinationRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    IamRoleArn: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class BatchCreateRumMetricDefinitionsErrorTypeDef(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: str
    MetricDefinition: MetricDefinitionRequestOutputTypeDef


class BatchGetRumMetricDefinitionsResponseTypeDef(BaseValidatorModel):
    MetricDefinitions: List[MetricDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateAppMonitorResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteResourcePolicyResponseTypeDef(BaseValidatorModel):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppMonitorDataResponseTypeDef(BaseValidatorModel):
    Events: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    PolicyDocument: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppMonitorsResponseTypeDef(BaseValidatorModel):
    AppMonitorSummaries: List[AppMonitorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    PolicyDocument: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteRumMetricDefinitionsResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchDeleteRumMetricDefinitionsErrorTypeDef]
    MetricDefinitionIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetRumMetricDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    DestinationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAppMonitorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRumMetricsDestinationsRequestPaginateTypeDef(BaseValidatorModel):
    AppMonitorName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DataStorageTypeDef(BaseValidatorModel):
    CwLog: Optional[CwLogTypeDef] = None


class GetAppMonitorDataRequestPaginateTypeDef(BaseValidatorModel):
    Name: str
    TimeRange: TimeRangeTypeDef
    Filters: Optional[Sequence[QueryFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetAppMonitorDataRequestTypeDef(BaseValidatorModel):
    Name: str
    TimeRange: TimeRangeTypeDef
    Filters: Optional[Sequence[QueryFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRumMetricsDestinationsResponseTypeDef(BaseValidatorModel):
    Destinations: List[MetricDestinationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AppMonitorConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateAppMonitorRequestTypeDef(BaseValidatorModel):
    Domain: str
    Name: str
    AppMonitorConfiguration: Optional[AppMonitorConfigurationUnionTypeDef] = None
    CustomEvents: Optional[CustomEventsTypeDef] = None
    CwLogEnabled: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateAppMonitorRequestTypeDef(BaseValidatorModel):
    Name: str
    AppMonitorConfiguration: Optional[AppMonitorConfigurationUnionTypeDef] = None
    CustomEvents: Optional[CustomEventsTypeDef] = None
    CwLogEnabled: Optional[bool] = None
    Domain: Optional[str] = None


class BatchCreateRumMetricDefinitionsResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchCreateRumMetricDefinitionsErrorTypeDef]
    MetricDefinitions: List[MetricDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AppMonitorTypeDef(BaseValidatorModel):
    AppMonitorConfiguration: Optional[AppMonitorConfigurationOutputTypeDef] = None
    Created: Optional[str] = None
    CustomEvents: Optional[CustomEventsTypeDef] = None
    DataStorage: Optional[DataStorageTypeDef] = None
    Domain: Optional[str] = None
    Id: Optional[str] = None
    LastModified: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[StateEnumType] = None
    Tags: Optional[Dict[str, str]] = None


class MetricDefinitionRequestUnionTypeDef(BaseValidatorModel):
    pass


class BatchCreateRumMetricDefinitionsRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinitions: Sequence[MetricDefinitionRequestUnionTypeDef]
    DestinationArn: Optional[str] = None


class UpdateRumMetricDefinitionRequestTypeDef(BaseValidatorModel):
    AppMonitorName: str
    Destination: MetricDestinationType
    MetricDefinition: MetricDefinitionRequestUnionTypeDef
    MetricDefinitionId: str
    DestinationArn: Optional[str] = None


class RumEventTypeDef(BaseValidatorModel):
    pass


class AppMonitorDetailsTypeDef(BaseValidatorModel):
    pass


class PutRumEventsRequestTypeDef(BaseValidatorModel):
    AppMonitorDetails: AppMonitorDetailsTypeDef
    BatchId: str
    Id: str
    RumEvents: Sequence[RumEventTypeDef]
    UserDetails: UserDetailsTypeDef
    Alias: Optional[str] = None


class GetAppMonitorResponseTypeDef(BaseValidatorModel):
    AppMonitor: AppMonitorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


