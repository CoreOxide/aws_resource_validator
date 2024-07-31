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
from aws_resource_validator.pydantic_models.codeguruprofiler_constants import *

class ChannelTypeDef(BaseModel):
    eventPublishers: Sequence[Literal["AnomalyDetection"]]
    uri: str
    id: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AgentConfigurationTypeDef(BaseModel):
    periodInSeconds: int
    shouldProfile: bool
    agentParameters: Optional[Dict[AgentParameterFieldType, str]] = None

class AgentOrchestrationConfigTypeDef(BaseModel):
    profilingEnabled: bool

class AggregatedProfileTimeTypeDef(BaseModel):
    period: Optional[AggregationPeriodType] = None
    start: Optional[datetime] = None

class UserFeedbackTypeDef(BaseModel):
    type: FeedbackTypeType

class MetricTypeDef(BaseModel):
    frameName: str
    threadStates: List[str]
    type: Literal["AggregatedRelativeTotalTime"]

class FrameMetricTypeDef(BaseModel):
    frameName: str
    threadStates: Sequence[str]
    type: Literal["AggregatedRelativeTotalTime"]

class TimestampStructureTypeDef(BaseModel):
    value: datetime

class ConfigureAgentRequestRequestTypeDef(BaseModel):
    profilingGroupName: str
    fleetInstanceId: Optional[str] = None
    metadata: Optional[Mapping[MetadataFieldType, str]] = None

class DeleteProfilingGroupRequestRequestTypeDef(BaseModel):
    profilingGroupName: str

class DescribeProfilingGroupRequestRequestTypeDef(BaseModel):
    profilingGroupName: str

class FindingsReportSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    profileEndTime: Optional[datetime] = None
    profileStartTime: Optional[datetime] = None
    profilingGroupName: Optional[str] = None
    totalNumberOfFindings: Optional[int] = None

class GetFindingsReportAccountSummaryRequestRequestTypeDef(BaseModel):
    dailyReportsOnly: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetNotificationConfigurationRequestRequestTypeDef(BaseModel):
    profilingGroupName: str

class GetPolicyRequestRequestTypeDef(BaseModel):
    profilingGroupName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ProfileTimeTypeDef(BaseModel):
    start: Optional[datetime] = None

class ListProfilingGroupsRequestRequestTypeDef(BaseModel):
    includeDescription: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class MatchTypeDef(BaseModel):
    frameAddress: Optional[str] = None
    targetFramesIndex: Optional[int] = None
    thresholdBreachValue: Optional[float] = None

class PatternTypeDef(BaseModel):
    countersToAggregate: Optional[List[str]] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    resolutionSteps: Optional[str] = None
    targetFrames: Optional[List[List[str]]] = None
    thresholdPercent: Optional[float] = None

class PutPermissionRequestRequestTypeDef(BaseModel):
    actionGroup: Literal["agentPermissions"]
    principals: Sequence[str]
    profilingGroupName: str
    revisionId: Optional[str] = None

class RemoveNotificationChannelRequestRequestTypeDef(BaseModel):
    channelId: str
    profilingGroupName: str

class RemovePermissionRequestRequestTypeDef(BaseModel):
    actionGroup: Literal["agentPermissions"]
    profilingGroupName: str
    revisionId: str

class SubmitFeedbackRequestRequestTypeDef(BaseModel):
    anomalyInstanceId: str
    profilingGroupName: str
    type: FeedbackTypeType
    comment: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AddNotificationChannelsRequestRequestTypeDef(BaseModel):
    channels: Sequence[ChannelTypeDef]
    profilingGroupName: str

class NotificationConfigurationTypeDef(BaseModel):
    channels: Optional[List[ChannelTypeDef]] = None

class GetPolicyResponseTypeDef(BaseModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileResponseTypeDef(BaseModel):
    contentEncoding: str
    contentType: str
    profile: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutPermissionResponseTypeDef(BaseModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemovePermissionResponseTypeDef(BaseModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigureAgentResponseTypeDef(BaseModel):
    configuration: AgentConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfilingGroupRequestRequestTypeDef(BaseModel):
    clientToken: str
    profilingGroupName: str
    agentOrchestrationConfig: Optional[AgentOrchestrationConfigTypeDef] = None
    computePlatform: Optional[ComputePlatformType] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateProfilingGroupRequestRequestTypeDef(BaseModel):
    agentOrchestrationConfig: AgentOrchestrationConfigTypeDef
    profilingGroupName: str

class ProfilingStatusTypeDef(BaseModel):
    latestAgentOrchestratedAt: Optional[datetime] = None
    latestAgentProfileReportedAt: Optional[datetime] = None
    latestAggregatedProfile: Optional[AggregatedProfileTimeTypeDef] = None

class AnomalyInstanceTypeDef(BaseModel):
    id: str
    startTime: datetime
    endTime: Optional[datetime] = None
    userFeedback: Optional[UserFeedbackTypeDef] = None

class FrameMetricDatumTypeDef(BaseModel):
    frameMetric: FrameMetricTypeDef
    values: List[float]

class BatchGetFrameMetricDataRequestRequestTypeDef(BaseModel):
    profilingGroupName: str
    endTime: Optional[TimestampTypeDef] = None
    frameMetrics: Optional[Sequence[FrameMetricTypeDef]] = None
    period: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    targetResolution: Optional[AggregationPeriodType] = None

class GetProfileRequestRequestTypeDef(BaseModel):
    profilingGroupName: str
    accept: Optional[str] = None
    endTime: Optional[TimestampTypeDef] = None
    maxDepth: Optional[int] = None
    period: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None

class GetRecommendationsRequestRequestTypeDef(BaseModel):
    endTime: TimestampTypeDef
    profilingGroupName: str
    startTime: TimestampTypeDef
    locale: Optional[str] = None

class ListFindingsReportsRequestRequestTypeDef(BaseModel):
    endTime: TimestampTypeDef
    profilingGroupName: str
    startTime: TimestampTypeDef
    dailyReportsOnly: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListProfileTimesRequestRequestTypeDef(BaseModel):
    endTime: TimestampTypeDef
    period: AggregationPeriodType
    profilingGroupName: str
    startTime: TimestampTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    orderBy: Optional[OrderByType] = None

class PostAgentProfileRequestRequestTypeDef(BaseModel):
    agentProfile: BlobTypeDef
    contentType: str
    profilingGroupName: str
    profileToken: Optional[str] = None

class GetFindingsReportAccountSummaryResponseTypeDef(BaseModel):
    nextToken: str
    reportSummaries: List[FindingsReportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFindingsReportsResponseTypeDef(BaseModel):
    findingsReportSummaries: List[FindingsReportSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileTimesRequestListProfileTimesPaginateTypeDef(BaseModel):
    endTime: TimestampTypeDef
    period: AggregationPeriodType
    profilingGroupName: str
    startTime: TimestampTypeDef
    orderBy: Optional[OrderByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfileTimesResponseTypeDef(BaseModel):
    nextToken: str
    profileTimes: List[ProfileTimeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationTypeDef(BaseModel):
    allMatchesCount: int
    allMatchesSum: float
    endTime: datetime
    pattern: PatternTypeDef
    startTime: datetime
    topMatches: List[MatchTypeDef]

class AddNotificationChannelsResponseTypeDef(BaseModel):
    notificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNotificationConfigurationResponseTypeDef(BaseModel):
    notificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveNotificationChannelResponseTypeDef(BaseModel):
    notificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProfilingGroupDescriptionTypeDef(BaseModel):
    agentOrchestrationConfig: Optional[AgentOrchestrationConfigTypeDef] = None
    arn: Optional[str] = None
    computePlatform: Optional[ComputePlatformType] = None
    createdAt: Optional[datetime] = None
    name: Optional[str] = None
    profilingStatus: Optional[ProfilingStatusTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None

class AnomalyTypeDef(BaseModel):
    instances: List[AnomalyInstanceTypeDef]
    metric: MetricTypeDef
    reason: str

class BatchGetFrameMetricDataResponseTypeDef(BaseModel):
    endTime: datetime
    endTimes: List[TimestampStructureTypeDef]
    frameMetricData: List[FrameMetricDatumTypeDef]
    resolution: AggregationPeriodType
    startTime: datetime
    unprocessedEndTimes: Dict[str, List[TimestampStructureTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfilingGroupResponseTypeDef(BaseModel):
    profilingGroup: ProfilingGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProfilingGroupResponseTypeDef(BaseModel):
    profilingGroup: ProfilingGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfilingGroupsResponseTypeDef(BaseModel):
    nextToken: str
    profilingGroupNames: List[str]
    profilingGroups: List[ProfilingGroupDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfilingGroupResponseTypeDef(BaseModel):
    profilingGroup: ProfilingGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationsResponseTypeDef(BaseModel):
    anomalies: List[AnomalyTypeDef]
    profileEndTime: datetime
    profileStartTime: datetime
    profilingGroupName: str
    recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

