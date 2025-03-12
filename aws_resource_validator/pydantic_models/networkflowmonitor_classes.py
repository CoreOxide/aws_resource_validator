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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteMonitorInputTypeDef(BaseValidatorModel):
    monitorName: str


class DeleteScopeInputTypeDef(BaseValidatorModel):
    scopeId: str


class GetMonitorInputTypeDef(BaseValidatorModel):
    monitorName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetQueryResultsMonitorTopContributorsInputTypeDef(BaseValidatorModel):
    monitorName: str
    queryId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetQueryResultsWorkloadInsightsTopContributorsDataInputTypeDef(BaseValidatorModel):
    scopeId: str
    queryId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkloadInsightsTopContributorsDataPointTypeDef(BaseValidatorModel):
    timestamps: List[datetime]
    values: List[float]
    label: str


class GetQueryResultsWorkloadInsightsTopContributorsInputTypeDef(BaseValidatorModel):
    scopeId: str
    queryId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WorkloadInsightsTopContributorsRowTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    localSubnetId: Optional[str] = None
    localAz: Optional[str] = None
    localVpcId: Optional[str] = None
    localRegion: Optional[str] = None
    remoteIdentifier: Optional[str] = None
    value: Optional[int] = None
    localSubnetArn: Optional[str] = None
    localVpcArn: Optional[str] = None


class GetQueryStatusMonitorTopContributorsInputTypeDef(BaseValidatorModel):
    monitorName: str
    queryId: str


class GetQueryStatusWorkloadInsightsTopContributorsDataInputTypeDef(BaseValidatorModel):
    scopeId: str
    queryId: str


class GetQueryStatusWorkloadInsightsTopContributorsInputTypeDef(BaseValidatorModel):
    scopeId: str
    queryId: str


class GetScopeInputTypeDef(BaseValidatorModel):
    scopeId: str


class KubernetesMetadataTypeDef(BaseValidatorModel):
    localServiceName: Optional[str] = None
    localPodName: Optional[str] = None
    localPodNamespace: Optional[str] = None
    remoteServiceName: Optional[str] = None
    remotePodName: Optional[str] = None
    remotePodNamespace: Optional[str] = None


class ListMonitorsInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    monitorStatus: Optional[MonitorStatusType] = None


class MonitorSummaryTypeDef(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType


class ListScopesInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ScopeSummaryTypeDef(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class TraversedComponentTypeDef(BaseValidatorModel):
    componentId: Optional[str] = None
    componentType: Optional[str] = None
    componentArn: Optional[str] = None
    serviceName: Optional[str] = None


class StopQueryMonitorTopContributorsInputTypeDef(BaseValidatorModel):
    monitorName: str
    queryId: str


class StopQueryWorkloadInsightsTopContributorsDataInputTypeDef(BaseValidatorModel):
    scopeId: str
    queryId: str


class StopQueryWorkloadInsightsTopContributorsInputTypeDef(BaseValidatorModel):
    scopeId: str
    queryId: str


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TargetIdTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class MonitorRemoteResourceTypeDef(BaseValidatorModel):
    pass


class MonitorLocalResourceTypeDef(BaseValidatorModel):
    pass


class CreateMonitorInputTypeDef(BaseValidatorModel):
    monitorName: str
    localResources: Sequence[MonitorLocalResourceTypeDef]
    scopeArn: str
    remoteResources: Optional[Sequence[MonitorRemoteResourceTypeDef]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateMonitorInputTypeDef(BaseValidatorModel):
    monitorName: str
    localResourcesToAdd: Optional[Sequence[MonitorLocalResourceTypeDef]] = None
    localResourcesToRemove: Optional[Sequence[MonitorLocalResourceTypeDef]] = None
    remoteResourcesToAdd: Optional[Sequence[MonitorRemoteResourceTypeDef]] = None
    remoteResourcesToRemove: Optional[Sequence[MonitorRemoteResourceTypeDef]] = None
    clientToken: Optional[str] = None


class CreateMonitorOutputTypeDef(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType
    localResources: List[MonitorLocalResourceTypeDef]
    remoteResources: List[MonitorRemoteResourceTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateScopeOutputTypeDef(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetMonitorOutputTypeDef(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType
    localResources: List[MonitorLocalResourceTypeDef]
    remoteResources: List[MonitorRemoteResourceTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueryStatusMonitorTopContributorsOutputTypeDef(BaseValidatorModel):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueryStatusWorkloadInsightsTopContributorsDataOutputTypeDef(BaseValidatorModel):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueryStatusWorkloadInsightsTopContributorsOutputTypeDef(BaseValidatorModel):
    status: QueryStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartQueryMonitorTopContributorsOutputTypeDef(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartQueryWorkloadInsightsTopContributorsDataOutputTypeDef(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartQueryWorkloadInsightsTopContributorsOutputTypeDef(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMonitorOutputTypeDef(BaseValidatorModel):
    monitorArn: str
    monitorName: str
    monitorStatus: MonitorStatusType
    localResources: List[MonitorLocalResourceTypeDef]
    remoteResources: List[MonitorRemoteResourceTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateScopeOutputTypeDef(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueryResultsMonitorTopContributorsInputPaginateTypeDef(BaseValidatorModel):
    monitorName: str
    queryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetQueryResultsWorkloadInsightsTopContributorsDataInputPaginateTypeDef(BaseValidatorModel):
    scopeId: str
    queryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetQueryResultsWorkloadInsightsTopContributorsInputPaginateTypeDef(BaseValidatorModel):
    scopeId: str
    queryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMonitorsInputPaginateTypeDef(BaseValidatorModel):
    monitorStatus: Optional[MonitorStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListScopesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetQueryResultsWorkloadInsightsTopContributorsDataOutputTypeDef(BaseValidatorModel):
    unit: MetricUnitType
    datapoints: List[WorkloadInsightsTopContributorsDataPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetQueryResultsWorkloadInsightsTopContributorsOutputTypeDef(BaseValidatorModel):
    topContributors: List[WorkloadInsightsTopContributorsRowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListMonitorsOutputTypeDef(BaseValidatorModel):
    monitors: List[MonitorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListScopesOutputTypeDef(BaseValidatorModel):
    scopes: List[ScopeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MonitorTopContributorsRowTypeDef(BaseValidatorModel):
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
    traversedConstructs: Optional[List[TraversedComponentTypeDef]] = None
    kubernetesMetadata: Optional[KubernetesMetadataTypeDef] = None
    localInstanceArn: Optional[str] = None
    localSubnetArn: Optional[str] = None
    localVpcArn: Optional[str] = None
    remoteInstanceArn: Optional[str] = None
    remoteSubnetArn: Optional[str] = None
    remoteVpcArn: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class StartQueryMonitorTopContributorsInputTypeDef(BaseValidatorModel):
    monitorName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    metricName: MonitorMetricType
    destinationCategory: DestinationCategoryType
    limit: Optional[int] = None


class StartQueryWorkloadInsightsTopContributorsDataInputTypeDef(BaseValidatorModel):
    scopeId: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    metricName: WorkloadInsightsMetricType
    destinationCategory: DestinationCategoryType


class StartQueryWorkloadInsightsTopContributorsInputTypeDef(BaseValidatorModel):
    scopeId: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    metricName: WorkloadInsightsMetricType
    destinationCategory: DestinationCategoryType
    limit: Optional[int] = None


class TargetIdentifierTypeDef(BaseValidatorModel):
    targetId: TargetIdTypeDef
    targetType: Literal["ACCOUNT"]


class GetQueryResultsMonitorTopContributorsOutputTypeDef(BaseValidatorModel):
    unit: MetricUnitType
    topContributors: List[MonitorTopContributorsRowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TargetResourceTypeDef(BaseValidatorModel):
    targetIdentifier: TargetIdentifierTypeDef
    region: str


class CreateScopeInputTypeDef(BaseValidatorModel):
    targets: Sequence[TargetResourceTypeDef]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class GetScopeOutputTypeDef(BaseValidatorModel):
    scopeId: str
    status: ScopeStatusType
    scopeArn: str
    targets: List[TargetResourceTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateScopeInputTypeDef(BaseValidatorModel):
    scopeId: str
    resourcesToAdd: Optional[Sequence[TargetResourceTypeDef]] = None
    resourcesToDelete: Optional[Sequence[TargetResourceTypeDef]] = None


