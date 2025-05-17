from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.networkflowmonitor.networkflowmonitor_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class MonitorLocalResource(BaseValidatorModel):
    type: MonitorLocalResourceTypeType
    identifier: str


class MonitorRemoteResource(BaseValidatorModel):
    type: MonitorRemoteResourceTypeType
    identifier: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteMonitorInput(BaseValidatorModel):
    monitorName: str


class DeleteScopeInput(BaseValidatorModel):
    scopeId: str


# This class is the input for the 'get_monitor' function.
class GetMonitorInput(BaseValidatorModel):
    monitorName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_query_results_monitor_top_contributors' function.
class GetQueryResultsMonitorTopContributorsInput(BaseValidatorModel):
    monitorName: str
    queryId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_query_results_workload_insights_top_contributors_data' function.
class GetQueryResultsWorkloadInsightsTopContributorsDataInput(BaseValidatorModel):
    scopeId: str
    queryId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkloadInsightsTopContributorsDataPoint(BaseValidatorModel):
    timestamps: List[datetime]
    values: List[float]
    label: str


# This class is the input for the 'get_query_results_workload_insights_top_contributors' function.
class GetQueryResultsWorkloadInsightsTopContributorsInput(BaseValidatorModel):
    scopeId: str
    queryId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkloadInsightsTopContributorsRow(BaseValidatorModel):
    accountId: Optional[str] = None
    localSubnetId: Optional[str] = None
    localAz: Optional[str] = None
    localVpcId: Optional[str] = None
    localRegion: Optional[str] = None
    remoteIdentifier: Optional[str] = None
    value: Optional[int] = None
    localSubnetArn: Optional[str] = None
    localVpcArn: Optional[str] = None


# This class is the input for the 'get_query_status_monitor_top_contributors' function.
class GetQueryStatusMonitorTopContributorsInput(BaseValidatorModel):
    monitorName: str
    queryId: str


# This class is the input for the 'get_query_status_workload_insights_top_contributors_data' function.
class GetQueryStatusWorkloadInsightsTopContributorsDataInput(BaseValidatorModel):
    scopeId: str
    queryId: str


# This class is the input for the 'get_query_status_workload_insights_top_contributors' function.
class GetQueryStatusWorkloadInsightsTopContributorsInput(BaseValidatorModel):
    scopeId: str
    queryId: str


# This class is the input for the 'get_scope' function.
class GetScopeInput(BaseValidatorModel):
    scopeId: str


class KubernetesMetadata(BaseValidatorModel):
    localServiceName: Optional[str] = None
    localPodName: Optional[str] = None
    localPodNamespace: Optional[str] = None
    remoteServiceName: Optional[str] = None
    remotePodName: Optional[str] = None
    remotePodNamespace: Optional[str] = None


# This class is the input for the 'list_monitors' function.
class ListMonitorsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    monitorStatus: Optional[MonitorStatusType] = None


class MonitorSummary(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType


# This class is the input for the 'list_scopes' function.
class ListScopesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ScopeSummary(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class TraversedComponent(BaseValidatorModel):
    componentId: Optional[str] = None
    componentType: Optional[str] = None
    componentArn: Optional[str] = None
    serviceName: Optional[str] = None

Timestamp = Union[datetime, str]


class StopQueryMonitorTopContributorsInput(BaseValidatorModel):
    monitorName: str
    queryId: str


class StopQueryWorkloadInsightsTopContributorsDataInput(BaseValidatorModel):
    scopeId: str
    queryId: str


class StopQueryWorkloadInsightsTopContributorsInput(BaseValidatorModel):
    scopeId: str
    queryId: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class TargetId(BaseValidatorModel):
    accountId: Optional[str] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'create_monitor' function.
class CreateMonitorInput(BaseValidatorModel):
    monitorName: str
    localResources: List[MonitorLocalResource]
    scopeArn: str
    remoteResources: Optional[List[MonitorRemoteResource]] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_monitor' function.
class UpdateMonitorInput(BaseValidatorModel):
    monitorName: str
    localResourcesToAdd: Optional[List[MonitorLocalResource]] = None
    localResourcesToRemove: Optional[List[MonitorLocalResource]] = None
    remoteResourcesToAdd: Optional[List[MonitorRemoteResource]] = None
    remoteResourcesToRemove: Optional[List[MonitorRemoteResource]] = None
    clientToken: Optional[str] = None


# This class is the output for the 'create_monitor' function.
class CreateMonitorOutput(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType
    localResources: List[MonitorLocalResource]
    remoteResources: List[MonitorRemoteResource]
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_scope' function.
class CreateScopeOutput(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_monitor' function.
class GetMonitorOutput(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType
    localResources: List[MonitorLocalResource]
    remoteResources: List[MonitorRemoteResource]
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_query_status_monitor_top_contributors' function.
class GetQueryStatusMonitorTopContributorsOutput(BaseValidatorModel):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_query_status_workload_insights_top_contributors_data' function.
class GetQueryStatusWorkloadInsightsTopContributorsDataOutput(BaseValidatorModel):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_query_status_workload_insights_top_contributors' function.
class GetQueryStatusWorkloadInsightsTopContributorsOutput(BaseValidatorModel):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_query_monitor_top_contributors' function.
class StartQueryMonitorTopContributorsOutput(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_query_workload_insights_top_contributors_data' function.
class StartQueryWorkloadInsightsTopContributorsDataOutput(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_query_workload_insights_top_contributors' function.
class StartQueryWorkloadInsightsTopContributorsOutput(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_monitor' function.
class UpdateMonitorOutput(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType
    localResources: List[MonitorLocalResource]
    remoteResources: List[MonitorRemoteResource]
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_scope' function.
class UpdateScopeOutput(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetQueryResultsMonitorTopContributorsInputPaginate(BaseValidatorModel):
    monitorName: str
    queryId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginate(BaseValidatorModel):
    scopeId: str
    queryId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetQueryResultsWorkloadInsightsTopContributorsInputPaginate(BaseValidatorModel):
    scopeId: str
    queryId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMonitorsInputPaginate(BaseValidatorModel):
    monitorStatus: Optional[MonitorStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListScopesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'get_query_results_workload_insights_top_contributors_data' function.
class GetQueryResultsWorkloadInsightsTopContributorsDataOutput(BaseValidatorModel):
    unit: MetricUnitType
    datapoints: List[WorkloadInsightsTopContributorsDataPoint]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_query_results_workload_insights_top_contributors' function.
class GetQueryResultsWorkloadInsightsTopContributorsOutput(BaseValidatorModel):
    topContributors: List[WorkloadInsightsTopContributorsRow]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_monitors' function.
class ListMonitorsOutput(BaseValidatorModel):
    monitors: List[MonitorSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_scopes' function.
class ListScopesOutput(BaseValidatorModel):
    scopes: List[ScopeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MonitorTopContributorsRow(BaseValidatorModel):
    localIp: Optional[str] = None
    snatIp: Optional[str] = None
    localInstanceId: Optional[str] = None
    localVpcId: Optional[str] = None
    localRegion: Optional[str] = None
    localAz: Optional[str] = None
    localSubnetId: Optional[str] = None
    targetPort: Optional[int] = None
    destinationCategory: Optional[DestinationCategoryType] = None
    remoteVpcId: Optional[str] = None
    remoteRegion: Optional[str] = None
    remoteAz: Optional[str] = None
    remoteSubnetId: Optional[str] = None
    remoteInstanceId: Optional[str] = None
    remoteIp: Optional[str] = None
    dnatIp: Optional[str] = None
    value: Optional[int] = None
    traversedConstructs: Optional[List[TraversedComponent]] = None
    kubernetesMetadata: Optional[KubernetesMetadata] = None
    localInstanceArn: Optional[str] = None
    localSubnetArn: Optional[str] = None
    localVpcArn: Optional[str] = None
    remoteInstanceArn: Optional[str] = None
    remoteSubnetArn: Optional[str] = None
    remoteVpcArn: Optional[str] = None


# This class is the input for the 'start_query_monitor_top_contributors' function.
class StartQueryMonitorTopContributorsInput(BaseValidatorModel):
    monitorName: str
    startTime: Timestamp
    endTime: Timestamp
    metricName: MonitorMetricType
    destinationCategory: DestinationCategoryType
    limit: Optional[int] = None


# This class is the input for the 'start_query_workload_insights_top_contributors_data' function.
class StartQueryWorkloadInsightsTopContributorsDataInput(BaseValidatorModel):
    scopeId: str
    startTime: Timestamp
    endTime: Timestamp
    metricName: WorkloadInsightsMetricType
    destinationCategory: DestinationCategoryType


# This class is the input for the 'start_query_workload_insights_top_contributors' function.
class StartQueryWorkloadInsightsTopContributorsInput(BaseValidatorModel):
    scopeId: str
    startTime: Timestamp
    endTime: Timestamp
    metricName: WorkloadInsightsMetricType
    destinationCategory: DestinationCategoryType
    limit: Optional[int] = None


class TargetIdentifier(BaseValidatorModel):
    targetId: TargetId
    targetType: Literal['ACCOUNT']


# This class is the output for the 'get_query_results_monitor_top_contributors' function.
class GetQueryResultsMonitorTopContributorsOutput(BaseValidatorModel):
    unit: MetricUnitType
    topContributors: List[MonitorTopContributorsRow]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TargetResource(BaseValidatorModel):
    targetIdentifier: TargetIdentifier
    region: str


# This class is the input for the 'create_scope' function.
class CreateScopeInput(BaseValidatorModel):
    targets: List[TargetResource]
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_scope' function.
class GetScopeOutput(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    targets: List[TargetResource]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_scope' function.
class UpdateScopeInput(BaseValidatorModel):
    scopeId: str
    resourcesToAdd: Optional[List[TargetResource]] = None
    resourcesToDelete: Optional[List[TargetResource]] = None