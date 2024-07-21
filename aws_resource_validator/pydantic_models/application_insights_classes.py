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
from aws_resource_validator.pydantic_models.application_insights_constants import *

class WorkloadConfigurationTypeDef(BaseModel):
    WorkloadName: Optional[str] = None
    Tier: Optional[TierType] = None
    Configuration: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ApplicationComponentTypeDef(BaseModel):
    ComponentName: Optional[str] = None
    ComponentRemarks: Optional[str] = None
    ResourceType: Optional[str] = None
    OsType: Optional[OsTypeType] = None
    Tier: Optional[TierType] = None
    Monitor: Optional[bool] = None
    DetectedWorkload: Optional[Dict[TierType, Dict[str, str]]] = None

class ApplicationInfoTypeDef(BaseModel):
    AccountId: Optional[str] = None
    ResourceGroupName: Optional[str] = None
    LifeCycle: Optional[str] = None
    OpsItemSNSTopicArn: Optional[str] = None
    OpsCenterEnabled: Optional[bool] = None
    CWEMonitorEnabled: Optional[bool] = None
    Remarks: Optional[str] = None
    AutoConfigEnabled: Optional[bool] = None
    DiscoveryType: Optional[DiscoveryTypeType] = None
    AttachMissingPermission: Optional[bool] = None

class ConfigurationEventTypeDef(BaseModel):
    ResourceGroupName: Optional[str] = None
    AccountId: Optional[str] = None
    MonitoredResourceARN: Optional[str] = None
    EventStatus: Optional[ConfigurationEventStatusType] = None
    EventResourceType: Optional[ConfigurationEventResourceTypeType] = None
    EventTime: Optional[datetime] = None
    EventDetail: Optional[str] = None
    EventResourceName: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CreateComponentRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    ResourceList: Sequence[str]

class CreateLogPatternRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str
    Pattern: str
    Rank: int

class LogPatternTypeDef(BaseModel):
    PatternSetName: Optional[str] = None
    PatternName: Optional[str] = None
    Pattern: Optional[str] = None
    Rank: Optional[int] = None

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str

class DeleteComponentRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str

class DeleteLogPatternRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str

class DescribeApplicationRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    AccountId: Optional[str] = None

class DescribeComponentConfigurationRecommendationRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    Tier: TierType
    WorkloadName: Optional[str] = None
    RecommendationType: Optional[RecommendationTypeType] = None

class DescribeComponentConfigurationRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    AccountId: Optional[str] = None

class DescribeComponentRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    AccountId: Optional[str] = None

class DescribeLogPatternRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str
    AccountId: Optional[str] = None

class DescribeObservationRequestRequestTypeDef(BaseModel):
    ObservationId: str
    AccountId: Optional[str] = None

class ObservationTypeDef(BaseModel):
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

class DescribeProblemObservationsRequestRequestTypeDef(BaseModel):
    ProblemId: str
    AccountId: Optional[str] = None

class DescribeProblemRequestRequestTypeDef(BaseModel):
    ProblemId: str
    AccountId: Optional[str] = None

class ProblemTypeDef(BaseModel):
    Id: Optional[str] = None
    Title: Optional[str] = None
    Insights: Optional[str] = None
    Status: Optional[StatusType] = None
    AffectedResource: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    SeverityLevel: Optional[SeverityLevelType] = None
    AccountId: Optional[str] = None
    ResourceGroupName: Optional[str] = None
    Feedback: Optional[Dict[Literal["INSIGHTS_FEEDBACK"], FeedbackValueType]] = None
    RecurringCount: Optional[int] = None
    LastRecurrenceTime: Optional[datetime] = None
    Visibility: Optional[VisibilityType] = None
    ResolutionMethod: Optional[ResolutionMethodType] = None

class DescribeWorkloadRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadId: str
    AccountId: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None

class ListComponentsRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None

class ListLogPatternSetsRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None

class ListLogPatternsRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    PatternSetName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class ListWorkloadsRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None

class WorkloadTypeDef(BaseModel):
    WorkloadId: Optional[str] = None
    ComponentName: Optional[str] = None
    WorkloadName: Optional[str] = None
    Tier: Optional[TierType] = None
    WorkloadRemarks: Optional[str] = None

class RemoveWorkloadRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    OpsCenterEnabled: Optional[bool] = None
    CWEMonitorEnabled: Optional[bool] = None
    OpsItemSNSTopicArn: Optional[str] = None
    RemoveSNSTopic: Optional[bool] = None
    AutoConfigEnabled: Optional[bool] = None
    AttachMissingPermission: Optional[bool] = None

class UpdateComponentConfigurationRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    Monitor: Optional[bool] = None
    Tier: Optional[TierType] = None
    ComponentConfiguration: Optional[str] = None
    AutoConfigEnabled: Optional[bool] = None

class UpdateComponentRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    NewComponentName: Optional[str] = None
    ResourceList: Optional[Sequence[str]] = None

class UpdateLogPatternRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str
    Pattern: Optional[str] = None
    Rank: Optional[int] = None

class UpdateProblemRequestRequestTypeDef(BaseModel):
    ProblemId: str
    UpdateStatus: Optional[Literal["RESOLVED"]] = None
    Visibility: Optional[VisibilityType] = None

class AddWorkloadRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef

class UpdateWorkloadRequestRequestTypeDef(BaseModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    WorkloadId: Optional[str] = None

class AddWorkloadResponseTypeDef(BaseModel):
    WorkloadId: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeComponentConfigurationRecommendationResponseTypeDef(BaseModel):
    ComponentConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeComponentConfigurationResponseTypeDef(BaseModel):
    Monitor: bool
    Tier: TierType
    ComponentConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkloadResponseTypeDef(BaseModel):
    WorkloadId: str
    WorkloadRemarks: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLogPatternSetsResponseTypeDef(BaseModel):
    ResourceGroupName: str
    AccountId: str
    LogPatternSets: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkloadResponseTypeDef(BaseModel):
    WorkloadId: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeComponentResponseTypeDef(BaseModel):
    ApplicationComponent: ApplicationComponentTypeDef
    ResourceList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListComponentsResponseTypeDef(BaseModel):
    ApplicationComponentList: List[ApplicationComponentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResponseTypeDef(BaseModel):
    ApplicationInfo: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationResponseTypeDef(BaseModel):
    ApplicationInfo: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseModel):
    ApplicationInfoList: List[ApplicationInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(BaseModel):
    ApplicationInfo: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationHistoryResponseTypeDef(BaseModel):
    EventList: List[ConfigurationEventTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationRequestRequestTypeDef(BaseModel):
    ResourceGroupName: Optional[str] = None
    OpsCenterEnabled: Optional[bool] = None
    CWEMonitorEnabled: Optional[bool] = None
    OpsItemSNSTopicArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AutoConfigEnabled: Optional[bool] = None
    AutoCreate: Optional[bool] = None
    GroupingType: Optional[Literal["ACCOUNT_BASED"]] = None
    AttachMissingPermission: Optional[bool] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateLogPatternResponseTypeDef(BaseModel):
    LogPattern: LogPatternTypeDef
    ResourceGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLogPatternResponseTypeDef(BaseModel):
    ResourceGroupName: str
    AccountId: str
    LogPattern: LogPatternTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLogPatternsResponseTypeDef(BaseModel):
    ResourceGroupName: str
    AccountId: str
    LogPatterns: List[LogPatternTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLogPatternResponseTypeDef(BaseModel):
    ResourceGroupName: str
    LogPattern: LogPatternTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeObservationResponseTypeDef(BaseModel):
    Observation: ObservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RelatedObservationsTypeDef(BaseModel):
    ObservationList: Optional[List[ObservationTypeDef]] = None

class DescribeProblemResponseTypeDef(BaseModel):
    Problem: ProblemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProblemsResponseTypeDef(BaseModel):
    ProblemList: List[ProblemTypeDef]
    NextToken: str
    ResourceGroupName: str
    AccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationHistoryRequestRequestTypeDef(BaseModel):
    ResourceGroupName: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventStatus: Optional[ConfigurationEventStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None

class ListProblemsRequestRequestTypeDef(BaseModel):
    AccountId: Optional[str] = None
    ResourceGroupName: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ComponentName: Optional[str] = None
    Visibility: Optional[VisibilityType] = None

class ListWorkloadsResponseTypeDef(BaseModel):
    WorkloadList: List[WorkloadTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProblemObservationsResponseTypeDef(BaseModel):
    RelatedObservations: RelatedObservationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

