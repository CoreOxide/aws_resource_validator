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
from aws_resource_validator.pydantic_models.codeguruprofiler_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AgentConfiguration(BaseValidatorModel):
    periodInSeconds: int
    shouldProfile: bool
    agentParameters: Optional[Dict[AgentParameterFieldType, str]] = None


class AgentOrchestrationConfig(BaseValidatorModel):
    profilingEnabled: bool


class AggregatedProfileTime(BaseValidatorModel):
    period: Optional[AggregationPeriodType] = None
    start: Optional[datetime] = None


class TimestampStructure(BaseValidatorModel):
    value: datetime


class ConfigureAgentRequest(BaseValidatorModel):
    profilingGroupName: str
    fleetInstanceId: Optional[str] = None
    metadata: Optional[Mapping[MetadataFieldType, str]] = None


class DeleteProfilingGroupRequest(BaseValidatorModel):
    profilingGroupName: str


class DescribeProfilingGroupRequest(BaseValidatorModel):
    profilingGroupName: str


class GetFindingsReportAccountSummaryRequest(BaseValidatorModel):
    dailyReportsOnly: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetNotificationConfigurationRequest(BaseValidatorModel):
    profilingGroupName: str


class GetPolicyRequest(BaseValidatorModel):
    profilingGroupName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ProfileTime(BaseValidatorModel):
    start: Optional[datetime] = None


class ListProfilingGroupsRequest(BaseValidatorModel):
    includeDescription: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class Match(BaseValidatorModel):
    frameAddress: Optional[str] = None
    targetFramesIndex: Optional[int] = None
    thresholdBreachValue: Optional[float] = None


class PutPermissionRequest(BaseValidatorModel):
    actionGroup: Literal["agentPermissions"]
    principals: Sequence[str]
    profilingGroupName: str
    revisionId: Optional[str] = None


class RemoveNotificationChannelRequest(BaseValidatorModel):
    channelId: str
    profilingGroupName: str


class RemovePermissionRequest(BaseValidatorModel):
    actionGroup: Literal["agentPermissions"]
    profilingGroupName: str
    revisionId: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class GetPolicyResponse(BaseValidatorModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


class GetProfileResponse(BaseValidatorModel):
    contentEncoding: str
    contentType: str
    profile: StreamingBody
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutPermissionResponse(BaseValidatorModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


class RemovePermissionResponse(BaseValidatorModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


class ConfigureAgentResponse(BaseValidatorModel):
    configuration: AgentConfiguration
    ResponseMetadata: ResponseMetadata


class CreateProfilingGroupRequest(BaseValidatorModel):
    clientToken: str
    profilingGroupName: str
    agentOrchestrationConfig: Optional[AgentOrchestrationConfig] = None
    computePlatform: Optional[ComputePlatformType] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateProfilingGroupRequest(BaseValidatorModel):
    agentOrchestrationConfig: AgentOrchestrationConfig
    profilingGroupName: str


class ProfilingStatus(BaseValidatorModel):
    latestAgentOrchestratedAt: Optional[datetime] = None
    latestAgentProfileReportedAt: Optional[datetime] = None
    latestAggregatedProfile: Optional[AggregatedProfileTime] = None


class Timestamp(BaseValidatorModel):
    pass


class GetProfileRequest(BaseValidatorModel):
    profilingGroupName: str
    accept: Optional[str] = None
    endTime: Optional[Timestamp] = None
    maxDepth: Optional[int] = None
    period: Optional[str] = None
    startTime: Optional[Timestamp] = None


class GetRecommendationsRequest(BaseValidatorModel):
    endTime: Timestamp
    profilingGroupName: str
    startTime: Timestamp
    locale: Optional[str] = None


class ListFindingsReportsRequest(BaseValidatorModel):
    endTime: Timestamp
    profilingGroupName: str
    startTime: Timestamp
    dailyReportsOnly: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListProfileTimesRequest(BaseValidatorModel):
    endTime: Timestamp
    period: AggregationPeriodType
    profilingGroupName: str
    startTime: Timestamp
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    orderBy: Optional[OrderByType] = None


class Blob(BaseValidatorModel):
    pass


class PostAgentProfileRequest(BaseValidatorModel):
    agentProfile: Blob
    contentType: str
    profilingGroupName: str
    profileToken: Optional[str] = None


class ChannelOutput(BaseValidatorModel):
    pass


class NotificationConfiguration(BaseValidatorModel):
    channels: Optional[List[ChannelOutput]] = None


class FindingsReportSummary(BaseValidatorModel):
    pass


class GetFindingsReportAccountSummaryResponse(BaseValidatorModel):
    reportSummaries: List[FindingsReportSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListFindingsReportsResponse(BaseValidatorModel):
    findingsReportSummaries: List[FindingsReportSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FrameMetricOutput(BaseValidatorModel):
    pass


class FrameMetricDatum(BaseValidatorModel):
    frameMetric: FrameMetricOutput
    values: List[float]


class ListProfileTimesRequestPaginate(BaseValidatorModel):
    endTime: Timestamp
    period: AggregationPeriodType
    profilingGroupName: str
    startTime: Timestamp
    orderBy: Optional[OrderByType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProfileTimesResponse(BaseValidatorModel):
    profileTimes: List[ProfileTime]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Pattern(BaseValidatorModel):
    pass


class Recommendation(BaseValidatorModel):
    allMatchesCount: int
    allMatchesSum: float
    endTime: datetime
    pattern: Pattern
    startTime: datetime
    topMatches: List[Match]


class ProfilingGroupDescription(BaseValidatorModel):
    agentOrchestrationConfig: Optional[AgentOrchestrationConfig] = None
    arn: Optional[str] = None
    computePlatform: Optional[ComputePlatformType] = None
    createdAt: Optional[datetime] = None
    name: Optional[str] = None
    profilingStatus: Optional[ProfilingStatus] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None


class AnomalyInstance(BaseValidatorModel):
    pass


class Metric(BaseValidatorModel):
    pass


class Anomaly(BaseValidatorModel):
    instances: List[AnomalyInstance]
    metric: Metric
    reason: str


class AddNotificationChannelsResponse(BaseValidatorModel):
    notificationConfiguration: NotificationConfiguration
    ResponseMetadata: ResponseMetadata


class GetNotificationConfigurationResponse(BaseValidatorModel):
    notificationConfiguration: NotificationConfiguration
    ResponseMetadata: ResponseMetadata


class RemoveNotificationChannelResponse(BaseValidatorModel):
    notificationConfiguration: NotificationConfiguration
    ResponseMetadata: ResponseMetadata


class ChannelUnion(BaseValidatorModel):
    pass


class AddNotificationChannelsRequest(BaseValidatorModel):
    channels: Sequence[ChannelUnion]
    profilingGroupName: str


class BatchGetFrameMetricDataResponse(BaseValidatorModel):
    endTime: datetime
    endTimes: List[TimestampStructure]
    frameMetricData: List[FrameMetricDatum]
    resolution: AggregationPeriodType
    startTime: datetime
    unprocessedEndTimes: Dict[str, List[TimestampStructure]]
    ResponseMetadata: ResponseMetadata


class FrameMetricUnion(BaseValidatorModel):
    pass


class BatchGetFrameMetricDataRequest(BaseValidatorModel):
    profilingGroupName: str
    endTime: Optional[Timestamp] = None
    frameMetrics: Optional[Sequence[FrameMetricUnion]] = None
    period: Optional[str] = None
    startTime: Optional[Timestamp] = None
    targetResolution: Optional[AggregationPeriodType] = None


class CreateProfilingGroupResponse(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescription
    ResponseMetadata: ResponseMetadata


class DescribeProfilingGroupResponse(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescription
    ResponseMetadata: ResponseMetadata


class ListProfilingGroupsResponse(BaseValidatorModel):
    profilingGroupNames: List[str]
    profilingGroups: List[ProfilingGroupDescription]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateProfilingGroupResponse(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescription
    ResponseMetadata: ResponseMetadata


class GetRecommendationsResponse(BaseValidatorModel):
    anomalies: List[Anomaly]
    profileEndTime: datetime
    profileStartTime: datetime
    profilingGroupName: str
    recommendations: List[Recommendation]
    ResponseMetadata: ResponseMetadata


