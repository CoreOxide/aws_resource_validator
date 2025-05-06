from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


class UserFeedback(BaseValidatorModel):
    type: FeedbackTypeType


class Metric(BaseValidatorModel):
    frameName: str
    threadStates: List[str]
    type: Literal['AggregatedRelativeTotalTime']

Timestamp = Union[datetime, str]


class TimestampStructure(BaseValidatorModel):
    value: datetime

Blob = Union[str, bytes, IO[Any], StreamingBody]


class ChannelOutput(BaseValidatorModel):
    eventPublishers: List[Literal['AnomalyDetection']]
    uri: str
    id: Optional[str] = None


class Channel(BaseValidatorModel):
    eventPublishers: List[Literal['AnomalyDetection']]
    uri: str
    id: Optional[str] = None


class ConfigureAgentRequest(BaseValidatorModel):
    profilingGroupName: str
    fleetInstanceId: Optional[str] = None
    metadata: Optional[Dict[MetadataFieldType, str]] = None


class DeleteProfilingGroupRequest(BaseValidatorModel):
    profilingGroupName: str


class DescribeProfilingGroupRequest(BaseValidatorModel):
    profilingGroupName: str


class FindingsReportSummary(BaseValidatorModel):
    id: Optional[str] = None
    profileEndTime: Optional[datetime] = None
    profileStartTime: Optional[datetime] = None
    profilingGroupName: Optional[str] = None
    totalNumberOfFindings: Optional[int] = None


class FrameMetricOutput(BaseValidatorModel):
    frameName: str
    threadStates: List[str]
    type: Literal['AggregatedRelativeTotalTime']


class FrameMetric(BaseValidatorModel):
    frameName: str
    threadStates: List[str]
    type: Literal['AggregatedRelativeTotalTime']


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


class Pattern(BaseValidatorModel):
    countersToAggregate: Optional[List[str]] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    resolutionSteps: Optional[str] = None
    targetFrames: Optional[List[List[str]]] = None
    thresholdPercent: Optional[float] = None


class PutPermissionRequest(BaseValidatorModel):
    actionGroup: Literal['agentPermissions']
    principals: List[str]
    profilingGroupName: str
    revisionId: Optional[str] = None


class RemoveNotificationChannelRequest(BaseValidatorModel):
    channelId: str
    profilingGroupName: str


class RemovePermissionRequest(BaseValidatorModel):
    actionGroup: Literal['agentPermissions']
    profilingGroupName: str
    revisionId: str


class SubmitFeedbackRequest(BaseValidatorModel):
    anomalyInstanceId: str
    profilingGroupName: str
    type: FeedbackTypeType
    comment: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


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
    tags: Optional[Dict[str, str]] = None


class UpdateProfilingGroupRequest(BaseValidatorModel):
    agentOrchestrationConfig: AgentOrchestrationConfig
    profilingGroupName: str


class ProfilingStatus(BaseValidatorModel):
    latestAgentOrchestratedAt: Optional[datetime] = None
    latestAgentProfileReportedAt: Optional[datetime] = None
    latestAggregatedProfile: Optional[AggregatedProfileTime] = None


class AnomalyInstance(BaseValidatorModel):
    id: str
    startTime: datetime
    endTime: Optional[datetime] = None
    userFeedback: Optional[UserFeedback] = None


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


class PostAgentProfileRequest(BaseValidatorModel):
    agentProfile: Blob
    contentType: str
    profilingGroupName: str
    profileToken: Optional[str] = None


class NotificationConfiguration(BaseValidatorModel):
    channels: Optional[List[ChannelOutput]] = None

ChannelUnion = Union[Channel, ChannelOutput]


class GetFindingsReportAccountSummaryResponse(BaseValidatorModel):
    reportSummaries: List[FindingsReportSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListFindingsReportsResponse(BaseValidatorModel):
    findingsReportSummaries: List[FindingsReportSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FrameMetricDatum(BaseValidatorModel):
    frameMetric: FrameMetricOutput
    values: List[float]

FrameMetricUnion = Union[FrameMetric, FrameMetricOutput]


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


class AddNotificationChannelsRequest(BaseValidatorModel):
    channels: List[ChannelUnion]
    profilingGroupName: str


class BatchGetFrameMetricDataResponse(BaseValidatorModel):
    endTime: datetime
    endTimes: List[TimestampStructure]
    frameMetricData: List[FrameMetricDatum]
    resolution: AggregationPeriodType
    startTime: datetime
    unprocessedEndTimes: Dict[str, List[TimestampStructure]]
    ResponseMetadata: ResponseMetadata


class BatchGetFrameMetricDataRequest(BaseValidatorModel):
    profilingGroupName: str
    endTime: Optional[Timestamp] = None
    frameMetrics: Optional[List[FrameMetricUnion]] = None
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
