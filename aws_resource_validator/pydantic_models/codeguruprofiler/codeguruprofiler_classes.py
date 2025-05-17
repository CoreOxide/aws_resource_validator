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


# This class is the input for the 'configure_agent' function.
class ConfigureAgentRequest(BaseValidatorModel):
    profilingGroupName: str
    fleetInstanceId: Optional[str] = None
    metadata: Optional[Dict[MetadataFieldType, str]] = None


class DeleteProfilingGroupRequest(BaseValidatorModel):
    profilingGroupName: str


# This class is the input for the 'describe_profiling_group' function.
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


# This class is the input for the 'get_findings_report_account_summary' function.
class GetFindingsReportAccountSummaryRequest(BaseValidatorModel):
    dailyReportsOnly: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'get_notification_configuration' function.
class GetNotificationConfigurationRequest(BaseValidatorModel):
    profilingGroupName: str


# This class is the input for the 'get_policy' function.
class GetPolicyRequest(BaseValidatorModel):
    profilingGroupName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ProfileTime(BaseValidatorModel):
    start: Optional[datetime] = None


# This class is the input for the 'list_profiling_groups' function.
class ListProfilingGroupsRequest(BaseValidatorModel):
    includeDescription: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
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


# This class is the input for the 'put_permission' function.
class PutPermissionRequest(BaseValidatorModel):
    actionGroup: Literal['agentPermissions']
    principals: List[str]
    profilingGroupName: str
    revisionId: Optional[str] = None


# This class is the input for the 'remove_notification_channel' function.
class RemoveNotificationChannelRequest(BaseValidatorModel):
    channelId: str
    profilingGroupName: str


# This class is the input for the 'remove_permission' function.
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


# This class is the output for the 'get_policy' function.
class GetPolicyResponse(BaseValidatorModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_profile' function.
class GetProfileResponse(BaseValidatorModel):
    contentEncoding: str
    contentType: str
    profile: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_permission' function.
class PutPermissionResponse(BaseValidatorModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_permission' function.
class RemovePermissionResponse(BaseValidatorModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'configure_agent' function.
class ConfigureAgentResponse(BaseValidatorModel):
    configuration: AgentConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_profiling_group' function.
class CreateProfilingGroupRequest(BaseValidatorModel):
    clientToken: str
    profilingGroupName: str
    agentOrchestrationConfig: Optional[AgentOrchestrationConfig] = None
    computePlatform: Optional[ComputePlatformType] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_profiling_group' function.
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


# This class is the input for the 'get_profile' function.
class GetProfileRequest(BaseValidatorModel):
    profilingGroupName: str
    accept: Optional[str] = None
    endTime: Optional[Timestamp] = None
    maxDepth: Optional[int] = None
    period: Optional[str] = None
    startTime: Optional[Timestamp] = None


# This class is the input for the 'get_recommendations' function.
class GetRecommendationsRequest(BaseValidatorModel):
    endTime: Timestamp
    profilingGroupName: str
    startTime: Timestamp
    locale: Optional[str] = None


# This class is the input for the 'list_findings_reports' function.
class ListFindingsReportsRequest(BaseValidatorModel):
    endTime: Timestamp
    profilingGroupName: str
    startTime: Timestamp
    dailyReportsOnly: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_profile_times' function.
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


# This class is the output for the 'get_findings_report_account_summary' function.
class GetFindingsReportAccountSummaryResponse(BaseValidatorModel):
    reportSummaries: List[FindingsReportSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_findings_reports' function.
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


# This class is the output for the 'list_profile_times' function.
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


# This class is the output for the 'add_notification_channels' function.
class AddNotificationChannelsResponse(BaseValidatorModel):
    notificationConfiguration: NotificationConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_notification_configuration' function.
class GetNotificationConfigurationResponse(BaseValidatorModel):
    notificationConfiguration: NotificationConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_notification_channel' function.
class RemoveNotificationChannelResponse(BaseValidatorModel):
    notificationConfiguration: NotificationConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'add_notification_channels' function.
class AddNotificationChannelsRequest(BaseValidatorModel):
    channels: List[ChannelUnion]
    profilingGroupName: str


# This class is the output for the 'batch_get_frame_metric_data' function.
class BatchGetFrameMetricDataResponse(BaseValidatorModel):
    endTime: datetime
    endTimes: List[TimestampStructure]
    frameMetricData: List[FrameMetricDatum]
    resolution: AggregationPeriodType
    startTime: datetime
    unprocessedEndTimes: Dict[str, List[TimestampStructure]]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_get_frame_metric_data' function.
class BatchGetFrameMetricDataRequest(BaseValidatorModel):
    profilingGroupName: str
    endTime: Optional[Timestamp] = None
    frameMetrics: Optional[List[FrameMetricUnion]] = None
    period: Optional[str] = None
    startTime: Optional[Timestamp] = None
    targetResolution: Optional[AggregationPeriodType] = None


# This class is the output for the 'create_profiling_group' function.
class CreateProfilingGroupResponse(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_profiling_group' function.
class DescribeProfilingGroupResponse(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_profiling_groups' function.
class ListProfilingGroupsResponse(BaseValidatorModel):
    profilingGroupNames: List[str]
    profilingGroups: List[ProfilingGroupDescription]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_profiling_group' function.
class UpdateProfilingGroupResponse(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_recommendations' function.
class GetRecommendationsResponse(BaseValidatorModel):
    anomalies: List[Anomaly]
    profileEndTime: datetime
    profileStartTime: datetime
    profilingGroupName: str
    recommendations: List[Recommendation]
