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
from aws_resource_validator.pydantic_models.networkflowmonitor_constants import *

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


class GetMonitorInput(BaseValidatorModel):
    monitorName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetQueryResultsMonitorTopContributorsInput(BaseValidatorModel):
    monitorName: str
    queryId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetQueryResultsWorkloadInsightsTopContributorsDataInput(BaseValidatorModel):
    scopeId: str
    queryId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkloadInsightsTopContributorsDataPoint(BaseValidatorModel):
    timestamps: List[datetime]
    values: List[float]
    label: str


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


class GetQueryStatusMonitorTopContributorsInput(BaseValidatorModel):
    monitorName: str
    queryId: str


class GetQueryStatusWorkloadInsightsTopContributorsDataInput(BaseValidatorModel):
    scopeId: str
    queryId: str


class GetQueryStatusWorkloadInsightsTopContributorsInput(BaseValidatorModel):
    scopeId: str
    queryId: str


class GetScopeInput(BaseValidatorModel):
    scopeId: str


class KubernetesMetadata(BaseValidatorModel):
    localServiceName: Optional[str] = None
    localPodName: Optional[str] = None
    localPodNamespace: Optional[str] = None
    remoteServiceName: Optional[str] = None
    remotePodName: Optional[str] = None
    remotePodNamespace: Optional[str] = None


class ListMonitorsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    monitorStatus: Optional[MonitorStatusType] = None


class MonitorSummary(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType


class ListScopesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ScopeSummary(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class TraversedComponent(BaseValidatorModel):
    componentId: Optional[str] = None
    componentType: Optional[str] = None
    componentArn: Optional[str] = None
    serviceName: Optional[str] = None


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
    tags: Mapping[str, str]


class TargetId(BaseValidatorModel):
    accountId: Optional[str] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class MonitorRemoteResource(BaseValidatorModel):
    pass


class MonitorLocalResource(BaseValidatorModel):
    pass


class CreateMonitorInput(BaseValidatorModel):
    monitorName: str
    localResources: Sequence[MonitorLocalResource]
    scopeArn: str
    remoteResources: Optional[Sequence[MonitorRemoteResource]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateMonitorInput(BaseValidatorModel):
    monitorName: str
    localResourcesToAdd: Optional[Sequence[MonitorLocalResource]] = None
    localResourcesToRemove: Optional[Sequence[MonitorLocalResource]] = None
    remoteResourcesToAdd: Optional[Sequence[MonitorRemoteResource]] = None
    remoteResourcesToRemove: Optional[Sequence[MonitorRemoteResource]] = None
    clientToken: Optional[str] = None


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


class CreateScopeOutput(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


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


class GetQueryStatusMonitorTopContributorsOutput(BaseValidatorModel):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadata


class GetQueryStatusWorkloadInsightsTopContributorsDataOutput(BaseValidatorModel):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadata


class GetQueryStatusWorkloadInsightsTopContributorsOutput(BaseValidatorModel):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartQueryMonitorTopContributorsOutput(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadata


class StartQueryWorkloadInsightsTopContributorsDataOutput(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadata


class StartQueryWorkloadInsightsTopContributorsOutput(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadata


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


class GetQueryResultsWorkloadInsightsTopContributorsDataOutput(BaseValidatorModel):
    unit: MetricUnitType
    datapoints: List[WorkloadInsightsTopContributorsDataPoint]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetQueryResultsWorkloadInsightsTopContributorsOutput(BaseValidatorModel):
    topContributors: List[WorkloadInsightsTopContributorsRow]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListMonitorsOutput(BaseValidatorModel):
    monitors: List[MonitorSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class Timestamp(BaseValidatorModel):
    pass


class StartQueryMonitorTopContributorsInput(BaseValidatorModel):
    monitorName: str
    startTime: Timestamp
    endTime: Timestamp
    metricName: MonitorMetricType
    destinationCategory: DestinationCategoryType
    limit: Optional[int] = None


class StartQueryWorkloadInsightsTopContributorsDataInput(BaseValidatorModel):
    scopeId: str
    startTime: Timestamp
    endTime: Timestamp
    metricName: WorkloadInsightsMetricType
    destinationCategory: DestinationCategoryType


class StartQueryWorkloadInsightsTopContributorsInput(BaseValidatorModel):
    scopeId: str
    startTime: Timestamp
    endTime: Timestamp
    metricName: WorkloadInsightsMetricType
    destinationCategory: DestinationCategoryType
    limit: Optional[int] = None


class TargetIdentifier(BaseValidatorModel):
    targetId: TargetId
    targetType: Literal["ACCOUNT"]


class GetQueryResultsMonitorTopContributorsOutput(BaseValidatorModel):
    unit: MetricUnitType
    topContributors: List[MonitorTopContributorsRow]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TargetResource(BaseValidatorModel):
    targetIdentifier: TargetIdentifier
    region: str


class CreateScopeInput(BaseValidatorModel):
    targets: Sequence[TargetResource]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class GetScopeOutput(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    targets: List[TargetResource]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateScopeInput(BaseValidatorModel):
    scopeId: str
    resourcesToAdd: Optional[Sequence[TargetResource]] = None
    resourcesToDelete: Optional[Sequence[TargetResource]] = None


