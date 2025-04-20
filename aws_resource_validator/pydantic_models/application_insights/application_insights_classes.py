from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.application_insights.application_insights_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class WorkloadConfiguration(BaseValidatorModel):
    WorkloadName: Optional[str] = None
    Tier: Optional[TierType] = None
    Configuration: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ApplicationComponent(BaseValidatorModel):
    ComponentName: Optional[str] = None
    ComponentRemarks: Optional[str] = None
    ResourceType: Optional[str] = None
    OsType: Optional[OsTypeType] = None
    Tier: Optional[TierType] = None
    Monitor: Optional[bool] = None
    DetectedWorkload: Optional[Dict[TierType, Dict[str, str]]] = None


class ApplicationInfo(BaseValidatorModel):
    AccountId: Optional[str] = None
    ResourceGroupName: Optional[str] = None
    LifeCycle: Optional[str] = None
    OpsItemSNSTopicArn: Optional[str] = None
    SNSNotificationArn: Optional[str] = None
    OpsCenterEnabled: Optional[bool] = None
    CWEMonitorEnabled: Optional[bool] = None
    Remarks: Optional[str] = None
    AutoConfigEnabled: Optional[bool] = None
    DiscoveryType: Optional[DiscoveryTypeType] = None
    AttachMissingPermission: Optional[bool] = None


class ConfigurationEvent(BaseValidatorModel):
    ResourceGroupName: Optional[str] = None
    AccountId: Optional[str] = None
    MonitoredResourceARN: Optional[str] = None
    EventStatus: Optional[ConfigurationEventStatusType] = None
    EventResourceType: Optional[ConfigurationEventResourceTypeType] = None
    EventTime: Optional[datetime] = None
    EventDetail: Optional[str] = None
    EventResourceName: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CreateComponentRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    ResourceList: List[str]


class CreateLogPatternRequest(BaseValidatorModel):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str
    Pattern: str
    Rank: int


class LogPattern(BaseValidatorModel):
    PatternSetName: Optional[str] = None
    PatternName: Optional[str] = None
    Pattern: Optional[str] = None
    Rank: Optional[int] = None


class DeleteApplicationRequest(BaseValidatorModel):
    ResourceGroupName: str


class DeleteComponentRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str


class DeleteLogPatternRequest(BaseValidatorModel):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str


class DescribeApplicationRequest(BaseValidatorModel):
    ResourceGroupName: str
    AccountId: Optional[str] = None


class DescribeComponentConfigurationRecommendationRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    Tier: TierType
    WorkloadName: Optional[str] = None
    RecommendationType: Optional[RecommendationTypeType] = None


class DescribeComponentConfigurationRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    AccountId: Optional[str] = None


class DescribeComponentRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    AccountId: Optional[str] = None


class DescribeLogPatternRequest(BaseValidatorModel):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str
    AccountId: Optional[str] = None


class DescribeObservationRequest(BaseValidatorModel):
    ObservationId: str
    AccountId: Optional[str] = None


class Observation(BaseValidatorModel):
    Id: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    SourceType: Optional[str] = None
    SourceARN: Optional[str] = None
    LogGroup: Optional[str] = None
    LineTime: Optional[datetime] = None
    LogText: Optional[str] = None
    LogFilter: Optional[LogFilterType] = None
    MetricNamespace: Optional[str] = None
    MetricName: Optional[str] = None
    Unit: Optional[str] = None
    Value: Optional[float] = None
    CloudWatchEventId: Optional[str] = None
    CloudWatchEventSource: Optional[CloudWatchEventSourceType] = None
    CloudWatchEventDetailType: Optional[str] = None
    HealthEventArn: Optional[str] = None
    HealthService: Optional[str] = None
    HealthEventTypeCode: Optional[str] = None
    HealthEventTypeCategory: Optional[str] = None
    HealthEventDescription: Optional[str] = None
    CodeDeployDeploymentId: Optional[str] = None
    CodeDeployDeploymentGroup: Optional[str] = None
    CodeDeployState: Optional[str] = None
    CodeDeployApplication: Optional[str] = None
    CodeDeployInstanceGroupId: Optional[str] = None
    Ec2State: Optional[str] = None
    RdsEventCategories: Optional[str] = None
    RdsEventMessage: Optional[str] = None
    S3EventName: Optional[str] = None
    StatesExecutionArn: Optional[str] = None
    StatesArn: Optional[str] = None
    StatesStatus: Optional[str] = None
    StatesInput: Optional[str] = None
    EbsEvent: Optional[str] = None
    EbsResult: Optional[str] = None
    EbsCause: Optional[str] = None
    EbsRequestId: Optional[str] = None
    XRayFaultPercent: Optional[int] = None
    XRayThrottlePercent: Optional[int] = None
    XRayErrorPercent: Optional[int] = None
    XRayRequestCount: Optional[int] = None
    XRayRequestAverageLatency: Optional[int] = None
    XRayNodeName: Optional[str] = None
    XRayNodeType: Optional[str] = None


class DescribeProblemObservationsRequest(BaseValidatorModel):
    ProblemId: str
    AccountId: Optional[str] = None


class DescribeProblemRequest(BaseValidatorModel):
    ProblemId: str
    AccountId: Optional[str] = None


class Problem(BaseValidatorModel):
    Id: Optional[str] = None
    Title: Optional[str] = None
    ShortName: Optional[str] = None
    Insights: Optional[str] = None
    Status: Optional[StatusType] = None
    AffectedResource: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    SeverityLevel: Optional[SeverityLevelType] = None
    AccountId: Optional[str] = None
    ResourceGroupName: Optional[str] = None
    Feedback: Optional[Dict[Literal['INSIGHTS_FEEDBACK'], FeedbackValueType]] = None
    RecurringCount: Optional[int] = None
    LastRecurrenceTime: Optional[datetime] = None
    Visibility: Optional[VisibilityType] = None
    ResolutionMethod: Optional[ResolutionMethodType] = None


class DescribeWorkloadRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadId: str
    AccountId: Optional[str] = None


class ListApplicationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class ListComponentsRequest(BaseValidatorModel):
    ResourceGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None

Timestamp = Union[datetime, str]


class ListLogPatternSetsRequest(BaseValidatorModel):
    ResourceGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class ListLogPatternsRequest(BaseValidatorModel):
    ResourceGroupName: str
    PatternSetName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class ListWorkloadsRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class Workload(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    ComponentName: Optional[str] = None
    WorkloadName: Optional[str] = None
    Tier: Optional[TierType] = None
    WorkloadRemarks: Optional[str] = None
    MissingWorkloadConfig: Optional[bool] = None


class RemoveWorkloadRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


class UpdateApplicationRequest(BaseValidatorModel):
    ResourceGroupName: str
    OpsCenterEnabled: Optional[bool] = None
    CWEMonitorEnabled: Optional[bool] = None
    OpsItemSNSTopicArn: Optional[str] = None
    SNSNotificationArn: Optional[str] = None
    RemoveSNSTopic: Optional[bool] = None
    AutoConfigEnabled: Optional[bool] = None
    AttachMissingPermission: Optional[bool] = None


class UpdateComponentConfigurationRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    Monitor: Optional[bool] = None
    Tier: Optional[TierType] = None
    ComponentConfiguration: Optional[str] = None
    AutoConfigEnabled: Optional[bool] = None


class UpdateComponentRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    NewComponentName: Optional[str] = None
    ResourceList: Optional[List[str]] = None


class UpdateLogPatternRequest(BaseValidatorModel):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str
    Pattern: Optional[str] = None
    Rank: Optional[int] = None


class UpdateProblemRequest(BaseValidatorModel):
    ProblemId: str
    UpdateStatus: Optional[Literal['RESOLVED']] = None
    Visibility: Optional[VisibilityType] = None


class AddWorkloadRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadConfiguration: WorkloadConfiguration


class UpdateWorkloadRequest(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadConfiguration: WorkloadConfiguration
    WorkloadId: Optional[str] = None


class AddWorkloadResponse(BaseValidatorModel):
    WorkloadId: str
    WorkloadConfiguration: WorkloadConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeComponentConfigurationRecommendationResponse(BaseValidatorModel):
    ComponentConfiguration: str
    ResponseMetadata: ResponseMetadata


class DescribeComponentConfigurationResponse(BaseValidatorModel):
    Monitor: bool
    Tier: TierType
    ComponentConfiguration: str
    ResponseMetadata: ResponseMetadata


class DescribeWorkloadResponse(BaseValidatorModel):
    WorkloadId: str
    WorkloadRemarks: str
    WorkloadConfiguration: WorkloadConfiguration
    ResponseMetadata: ResponseMetadata


class ListLogPatternSetsResponse(BaseValidatorModel):
    ResourceGroupName: str
    AccountId: str
    LogPatternSets: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateWorkloadResponse(BaseValidatorModel):
    WorkloadId: str
    WorkloadConfiguration: WorkloadConfiguration
    ResponseMetadata: ResponseMetadata


class DescribeComponentResponse(BaseValidatorModel):
    ApplicationComponent: ApplicationComponent
    ResourceList: List[str]
    ResponseMetadata: ResponseMetadata


class ListComponentsResponse(BaseValidatorModel):
    ApplicationComponentList: List[ApplicationComponent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateApplicationResponse(BaseValidatorModel):
    ApplicationInfo: ApplicationInfo
    ResponseMetadata: ResponseMetadata


class DescribeApplicationResponse(BaseValidatorModel):
    ApplicationInfo: ApplicationInfo
    ResponseMetadata: ResponseMetadata


class ListApplicationsResponse(BaseValidatorModel):
    ApplicationInfoList: List[ApplicationInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateApplicationResponse(BaseValidatorModel):
    ApplicationInfo: ApplicationInfo
    ResponseMetadata: ResponseMetadata


class ListConfigurationHistoryResponse(BaseValidatorModel):
    EventList: List[ConfigurationEvent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateApplicationRequest(BaseValidatorModel):
    ResourceGroupName: Optional[str] = None
    OpsCenterEnabled: Optional[bool] = None
    CWEMonitorEnabled: Optional[bool] = None
    OpsItemSNSTopicArn: Optional[str] = None
    SNSNotificationArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    AutoConfigEnabled: Optional[bool] = None
    AutoCreate: Optional[bool] = None
    GroupingType: Optional[Literal['ACCOUNT_BASED']] = None
    AttachMissingPermission: Optional[bool] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class CreateLogPatternResponse(BaseValidatorModel):
    LogPattern: LogPattern
    ResourceGroupName: str
    ResponseMetadata: ResponseMetadata


class DescribeLogPatternResponse(BaseValidatorModel):
    ResourceGroupName: str
    AccountId: str
    LogPattern: LogPattern
    ResponseMetadata: ResponseMetadata


class ListLogPatternsResponse(BaseValidatorModel):
    ResourceGroupName: str
    AccountId: str
    LogPatterns: List[LogPattern]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateLogPatternResponse(BaseValidatorModel):
    ResourceGroupName: str
    LogPattern: LogPattern
    ResponseMetadata: ResponseMetadata


class DescribeObservationResponse(BaseValidatorModel):
    Observation: Observation
    ResponseMetadata: ResponseMetadata


class RelatedObservations(BaseValidatorModel):
    ObservationList: Optional[List[Observation]] = None


class DescribeProblemResponse(BaseValidatorModel):
    Problem: Problem
    SNSNotificationArn: str
    ResponseMetadata: ResponseMetadata


class ListProblemsResponse(BaseValidatorModel):
    ProblemList: List[Problem]
    ResourceGroupName: str
    AccountId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListConfigurationHistoryRequest(BaseValidatorModel):
    ResourceGroupName: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    EventStatus: Optional[ConfigurationEventStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class ListProblemsRequest(BaseValidatorModel):
    AccountId: Optional[str] = None
    ResourceGroupName: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ComponentName: Optional[str] = None
    Visibility: Optional[VisibilityType] = None


class ListWorkloadsResponse(BaseValidatorModel):
    WorkloadList: List[Workload]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeProblemObservationsResponse(BaseValidatorModel):
    RelatedObservations: RelatedObservations
    ResponseMetadata: ResponseMetadata