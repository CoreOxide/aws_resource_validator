from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.codeguruprofiler_constants import *

class ChannelTypeDef(BaseValidatorModel):
    eventPublishers: Sequence[Literal["AnomalyDetection"]]
    uri: str
    id: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AgentConfigurationTypeDef(BaseValidatorModel):
    periodInSeconds: int
    shouldProfile: bool
    agentParameters: Optional[Dict[AgentParameterFieldType, str]] = None

class AgentOrchestrationConfigTypeDef(BaseValidatorModel):
    profilingEnabled: bool

class AggregatedProfileTimeTypeDef(BaseValidatorModel):
    period: Optional[AggregationPeriodType] = None
    start: Optional[datetime] = None

class UserFeedbackTypeDef(BaseValidatorModel):
    type: FeedbackTypeType

class MetricTypeDef(BaseValidatorModel):
    frameName: str
    threadStates: List[str]
    type: Literal["AggregatedRelativeTotalTime"]

class FrameMetricTypeDef(BaseValidatorModel):
    frameName: str
    threadStates: Sequence[str]
    type: Literal["AggregatedRelativeTotalTime"]

class TimestampStructureTypeDef(BaseValidatorModel):
    value: datetime

class ConfigureAgentRequestRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str
    fleetInstanceId: Optional[str] = None
    metadata: Optional[Mapping[MetadataFieldType, str]] = None

class DeleteProfilingGroupRequestRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str

class DescribeProfilingGroupRequestRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str

class FindingsReportSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    profileEndTime: Optional[datetime] = None
    profileStartTime: Optional[datetime] = None
    profilingGroupName: Optional[str] = None
    totalNumberOfFindings: Optional[int] = None

class GetFindingsReportAccountSummaryRequestRequestTypeDef(BaseValidatorModel):
    dailyReportsOnly: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetNotificationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str

class GetPolicyRequestRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ProfileTimeTypeDef(BaseValidatorModel):
    start: Optional[datetime] = None

class ListProfilingGroupsRequestRequestTypeDef(BaseValidatorModel):
    includeDescription: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class MatchTypeDef(BaseValidatorModel):
    frameAddress: Optional[str] = None
    targetFramesIndex: Optional[int] = None
    thresholdBreachValue: Optional[float] = None

class PatternTypeDef(BaseValidatorModel):
    countersToAggregate: Optional[List[str]] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    resolutionSteps: Optional[str] = None
    targetFrames: Optional[List[List[str]]] = None
    thresholdPercent: Optional[float] = None

class PutPermissionRequestRequestTypeDef(BaseValidatorModel):
    actionGroup: Literal["agentPermissions"]
    principals: Sequence[str]
    profilingGroupName: str
    revisionId: Optional[str] = None

class RemoveNotificationChannelRequestRequestTypeDef(BaseValidatorModel):
    channelId: str
    profilingGroupName: str

class RemovePermissionRequestRequestTypeDef(BaseValidatorModel):
    actionGroup: Literal["agentPermissions"]
    profilingGroupName: str
    revisionId: str

class SubmitFeedbackRequestRequestTypeDef(BaseValidatorModel):
    anomalyInstanceId: str
    profilingGroupName: str
    type: FeedbackTypeType
    comment: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AddNotificationChannelsRequestRequestTypeDef(BaseValidatorModel):
    channels: Sequence[ChannelTypeDef]
    profilingGroupName: str

class NotificationConfigurationTypeDef(BaseValidatorModel):
    channels: Optional[List[ChannelTypeDef]] = None

class GetPolicyResponseTypeDef(BaseValidatorModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileResponseTypeDef(BaseValidatorModel):
    contentEncoding: str
    contentType: str
    profile: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutPermissionResponseTypeDef(BaseValidatorModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemovePermissionResponseTypeDef(BaseValidatorModel):
    policy: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigureAgentResponseTypeDef(BaseValidatorModel):
    configuration: AgentConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfilingGroupRequestRequestTypeDef(BaseValidatorModel):
    clientToken: str
    profilingGroupName: str
    agentOrchestrationConfig: Optional[AgentOrchestrationConfigTypeDef] = None
    computePlatform: Optional[ComputePlatformType] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateProfilingGroupRequestRequestTypeDef(BaseValidatorModel):
    agentOrchestrationConfig: AgentOrchestrationConfigTypeDef
    profilingGroupName: str

class ProfilingStatusTypeDef(BaseValidatorModel):
    latestAgentOrchestratedAt: Optional[datetime] = None
    latestAgentProfileReportedAt: Optional[datetime] = None
    latestAggregatedProfile: Optional[AggregatedProfileTimeTypeDef] = None

class AnomalyInstanceTypeDef(BaseValidatorModel):
    id: str
    startTime: datetime
    endTime: Optional[datetime] = None
    userFeedback: Optional[UserFeedbackTypeDef] = None

class FrameMetricDatumTypeDef(BaseValidatorModel):
    frameMetric: FrameMetricTypeDef
    values: List[float]

class BatchGetFrameMetricDataRequestRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str
    endTime: Optional[TimestampTypeDef] = None
    frameMetrics: Optional[Sequence[FrameMetricTypeDef]] = None
    period: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    targetResolution: Optional[AggregationPeriodType] = None

class GetProfileRequestRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str
    accept: Optional[str] = None
    endTime: Optional[TimestampTypeDef] = None
    maxDepth: Optional[int] = None
    period: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None

class GetRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    profilingGroupName: str
    startTime: TimestampTypeDef
    locale: Optional[str] = None

class ListFindingsReportsRequestRequestTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    profilingGroupName: str
    startTime: TimestampTypeDef
    dailyReportsOnly: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListProfileTimesRequestRequestTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    period: AggregationPeriodType
    profilingGroupName: str
    startTime: TimestampTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    orderBy: Optional[OrderByType] = None

class PostAgentProfileRequestRequestTypeDef(BaseValidatorModel):
    agentProfile: BlobTypeDef
    contentType: str
    profilingGroupName: str
    profileToken: Optional[str] = None

class GetFindingsReportAccountSummaryResponseTypeDef(BaseValidatorModel):
    nextToken: str
    reportSummaries: List[FindingsReportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFindingsReportsResponseTypeDef(BaseValidatorModel):
    findingsReportSummaries: List[FindingsReportSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileTimesRequestListProfileTimesPaginateTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    period: AggregationPeriodType
    profilingGroupName: str
    startTime: TimestampTypeDef
    orderBy: Optional[OrderByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfileTimesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    profileTimes: List[ProfileTimeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationTypeDef(BaseValidatorModel):
    allMatchesCount: int
    allMatchesSum: float
    endTime: datetime
    pattern: PatternTypeDef
    startTime: datetime
    topMatches: List[MatchTypeDef]

class AddNotificationChannelsResponseTypeDef(BaseValidatorModel):
    notificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNotificationConfigurationResponseTypeDef(BaseValidatorModel):
    notificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveNotificationChannelResponseTypeDef(BaseValidatorModel):
    notificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProfilingGroupDescriptionTypeDef(BaseValidatorModel):
    agentOrchestrationConfig: Optional[AgentOrchestrationConfigTypeDef] = None
    arn: Optional[str] = None
    computePlatform: Optional[ComputePlatformType] = None
    createdAt: Optional[datetime] = None
    name: Optional[str] = None
    profilingStatus: Optional[ProfilingStatusTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None

class AnomalyTypeDef(BaseValidatorModel):
    instances: List[AnomalyInstanceTypeDef]
    metric: MetricTypeDef
    reason: str

class BatchGetFrameMetricDataResponseTypeDef(BaseValidatorModel):
    endTime: datetime
    endTimes: List[TimestampStructureTypeDef]
    frameMetricData: List[FrameMetricDatumTypeDef]
    resolution: AggregationPeriodType
    startTime: datetime
    unprocessedEndTimes: Dict[str, List[TimestampStructureTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfilingGroupResponseTypeDef(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProfilingGroupResponseTypeDef(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfilingGroupsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    profilingGroupNames: List[str]
    profilingGroups: List[ProfilingGroupDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfilingGroupResponseTypeDef(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationsResponseTypeDef(BaseValidatorModel):
    anomalies: List[AnomalyTypeDef]
    profileEndTime: datetime
    profileStartTime: datetime
    profilingGroupName: str
    recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

