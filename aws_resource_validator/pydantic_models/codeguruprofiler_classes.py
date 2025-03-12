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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AgentConfigurationTypeDef(BaseValidatorModel):
    periodInSeconds: int
    shouldProfile: bool
    agentParameters: Optional[Dict[AgentParameterFieldType, str]] = None


class AgentOrchestrationConfigTypeDef(BaseValidatorModel):
    profilingEnabled: bool


class AggregatedProfileTimeTypeDef(BaseValidatorModel):
    period: Optional[AggregationPeriodType] = None
    start: Optional[datetime] = None


class TimestampStructureTypeDef(BaseValidatorModel):
    value: datetime


class ConfigureAgentRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str
    fleetInstanceId: Optional[str] = None
    metadata: Optional[Mapping[MetadataFieldType, str]] = None


class DeleteProfilingGroupRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str


class DescribeProfilingGroupRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str


class GetFindingsReportAccountSummaryRequestTypeDef(BaseValidatorModel):
    dailyReportsOnly: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str


class GetPolicyRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ProfileTimeTypeDef(BaseValidatorModel):
    start: Optional[datetime] = None


class ListProfilingGroupsRequestTypeDef(BaseValidatorModel):
    includeDescription: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class MatchTypeDef(BaseValidatorModel):
    frameAddress: Optional[str] = None
    targetFramesIndex: Optional[int] = None
    thresholdBreachValue: Optional[float] = None


class PutPermissionRequestTypeDef(BaseValidatorModel):
    actionGroup: Literal["agentPermissions"]
    principals: Sequence[str]
    profilingGroupName: str
    revisionId: Optional[str] = None


class RemoveNotificationChannelRequestTypeDef(BaseValidatorModel):
    channelId: str
    profilingGroupName: str


class RemovePermissionRequestTypeDef(BaseValidatorModel):
    actionGroup: Literal["agentPermissions"]
    profilingGroupName: str
    revisionId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


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


class CreateProfilingGroupRequestTypeDef(BaseValidatorModel):
    clientToken: str
    profilingGroupName: str
    agentOrchestrationConfig: Optional[AgentOrchestrationConfigTypeDef] = None
    computePlatform: Optional[ComputePlatformType] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateProfilingGroupRequestTypeDef(BaseValidatorModel):
    agentOrchestrationConfig: AgentOrchestrationConfigTypeDef
    profilingGroupName: str


class ProfilingStatusTypeDef(BaseValidatorModel):
    latestAgentOrchestratedAt: Optional[datetime] = None
    latestAgentProfileReportedAt: Optional[datetime] = None
    latestAggregatedProfile: Optional[AggregatedProfileTimeTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetProfileRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str
    accept: Optional[str] = None
    endTime: Optional[TimestampTypeDef] = None
    maxDepth: Optional[int] = None
    period: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None


class GetRecommendationsRequestTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    profilingGroupName: str
    startTime: TimestampTypeDef
    locale: Optional[str] = None


class ListFindingsReportsRequestTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    profilingGroupName: str
    startTime: TimestampTypeDef
    dailyReportsOnly: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListProfileTimesRequestTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    period: AggregationPeriodType
    profilingGroupName: str
    startTime: TimestampTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    orderBy: Optional[OrderByType] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class PostAgentProfileRequestTypeDef(BaseValidatorModel):
    agentProfile: BlobTypeDef
    contentType: str
    profilingGroupName: str
    profileToken: Optional[str] = None


class ChannelOutputTypeDef(BaseValidatorModel):
    pass


class NotificationConfigurationTypeDef(BaseValidatorModel):
    channels: Optional[List[ChannelOutputTypeDef]] = None


class FindingsReportSummaryTypeDef(BaseValidatorModel):
    pass


class GetFindingsReportAccountSummaryResponseTypeDef(BaseValidatorModel):
    reportSummaries: List[FindingsReportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListFindingsReportsResponseTypeDef(BaseValidatorModel):
    findingsReportSummaries: List[FindingsReportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FrameMetricOutputTypeDef(BaseValidatorModel):
    pass


class FrameMetricDatumTypeDef(BaseValidatorModel):
    frameMetric: FrameMetricOutputTypeDef
    values: List[float]


class ListProfileTimesRequestPaginateTypeDef(BaseValidatorModel):
    endTime: TimestampTypeDef
    period: AggregationPeriodType
    profilingGroupName: str
    startTime: TimestampTypeDef
    orderBy: Optional[OrderByType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProfileTimesResponseTypeDef(BaseValidatorModel):
    profileTimes: List[ProfileTimeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PatternTypeDef(BaseValidatorModel):
    pass


class RecommendationTypeDef(BaseValidatorModel):
    allMatchesCount: int
    allMatchesSum: float
    endTime: datetime
    pattern: PatternTypeDef
    startTime: datetime
    topMatches: List[MatchTypeDef]


class ProfilingGroupDescriptionTypeDef(BaseValidatorModel):
    agentOrchestrationConfig: Optional[AgentOrchestrationConfigTypeDef] = None
    arn: Optional[str] = None
    computePlatform: Optional[ComputePlatformType] = None
    createdAt: Optional[datetime] = None
    name: Optional[str] = None
    profilingStatus: Optional[ProfilingStatusTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None


class AnomalyInstanceTypeDef(BaseValidatorModel):
    pass


class MetricTypeDef(BaseValidatorModel):
    pass


class AnomalyTypeDef(BaseValidatorModel):
    instances: List[AnomalyInstanceTypeDef]
    metric: MetricTypeDef
    reason: str


class AddNotificationChannelsResponseTypeDef(BaseValidatorModel):
    notificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetNotificationConfigurationResponseTypeDef(BaseValidatorModel):
    notificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveNotificationChannelResponseTypeDef(BaseValidatorModel):
    notificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ChannelUnionTypeDef(BaseValidatorModel):
    pass


class AddNotificationChannelsRequestTypeDef(BaseValidatorModel):
    channels: Sequence[ChannelUnionTypeDef]
    profilingGroupName: str


class BatchGetFrameMetricDataResponseTypeDef(BaseValidatorModel):
    endTime: datetime
    endTimes: List[TimestampStructureTypeDef]
    frameMetricData: List[FrameMetricDatumTypeDef]
    resolution: AggregationPeriodType
    startTime: datetime
    unprocessedEndTimes: Dict[str, List[TimestampStructureTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef


class FrameMetricUnionTypeDef(BaseValidatorModel):
    pass


class BatchGetFrameMetricDataRequestTypeDef(BaseValidatorModel):
    profilingGroupName: str
    endTime: Optional[TimestampTypeDef] = None
    frameMetrics: Optional[Sequence[FrameMetricUnionTypeDef]] = None
    period: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    targetResolution: Optional[AggregationPeriodType] = None


class CreateProfilingGroupResponseTypeDef(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeProfilingGroupResponseTypeDef(BaseValidatorModel):
    profilingGroup: ProfilingGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListProfilingGroupsResponseTypeDef(BaseValidatorModel):
    profilingGroupNames: List[str]
    profilingGroups: List[ProfilingGroupDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


