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
from aws_resource_validator.pydantic_models.application_insights_constants import *

class WorkloadConfigurationTypeDef(BaseValidatorModel):
    WorkloadName: Optional[str] = None
    Tier: Optional[TierType] = None
    Configuration: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ApplicationComponentTypeDef(BaseValidatorModel):
    ComponentName: Optional[str] = None
    ComponentRemarks: Optional[str] = None
    ResourceType: Optional[str] = None
    OsType: Optional[OsTypeType] = None
    Tier: Optional[TierType] = None
    Monitor: Optional[bool] = None
    DetectedWorkload: Optional[Dict[TierType, Dict[str, str]]] = None


class ApplicationInfoTypeDef(BaseValidatorModel):
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


class ConfigurationEventTypeDef(BaseValidatorModel):
    ResourceGroupName: Optional[str] = None
    AccountId: Optional[str] = None
    MonitoredResourceARN: Optional[str] = None
    EventStatus: Optional[ConfigurationEventStatusType] = None
    EventResourceType: Optional[ConfigurationEventResourceTypeType] = None
    EventTime: Optional[datetime] = None
    EventDetail: Optional[str] = None
    EventResourceName: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CreateComponentRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    ResourceList: Sequence[str]


class DeleteApplicationRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str


class DeleteComponentRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str


class DeleteLogPatternRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str


class DescribeApplicationRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    AccountId: Optional[str] = None


class DescribeComponentConfigurationRecommendationRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    Tier: TierType
    WorkloadName: Optional[str] = None
    RecommendationType: Optional[RecommendationTypeType] = None


class DescribeComponentConfigurationRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    AccountId: Optional[str] = None


class DescribeComponentRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    AccountId: Optional[str] = None


class DescribeLogPatternRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    PatternSetName: str
    PatternName: str
    AccountId: Optional[str] = None


class DescribeObservationRequestTypeDef(BaseValidatorModel):
    ObservationId: str
    AccountId: Optional[str] = None


class ObservationTypeDef(BaseValidatorModel):
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


class DescribeProblemObservationsRequestTypeDef(BaseValidatorModel):
    ProblemId: str
    AccountId: Optional[str] = None


class DescribeProblemRequestTypeDef(BaseValidatorModel):
    ProblemId: str
    AccountId: Optional[str] = None


class ProblemTypeDef(BaseValidatorModel):
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
    Feedback: Optional[Dict[Literal["INSIGHTS_FEEDBACK"], FeedbackValueType]] = None
    RecurringCount: Optional[int] = None
    LastRecurrenceTime: Optional[datetime] = None
    Visibility: Optional[VisibilityType] = None
    ResolutionMethod: Optional[ResolutionMethodType] = None


class DescribeWorkloadRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadId: str
    AccountId: Optional[str] = None


class ListApplicationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class ListComponentsRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class ListLogPatternSetsRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class ListLogPatternsRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    PatternSetName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class ListWorkloadsRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class WorkloadTypeDef(BaseValidatorModel):
    WorkloadId: Optional[str] = None
    ComponentName: Optional[str] = None
    WorkloadName: Optional[str] = None
    Tier: Optional[TierType] = None
    WorkloadRemarks: Optional[str] = None
    MissingWorkloadConfig: Optional[bool] = None


class RemoveWorkloadRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadId: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateApplicationRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    OpsCenterEnabled: Optional[bool] = None
    CWEMonitorEnabled: Optional[bool] = None
    OpsItemSNSTopicArn: Optional[str] = None
    SNSNotificationArn: Optional[str] = None
    RemoveSNSTopic: Optional[bool] = None
    AutoConfigEnabled: Optional[bool] = None
    AttachMissingPermission: Optional[bool] = None


class UpdateComponentConfigurationRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    Monitor: Optional[bool] = None
    Tier: Optional[TierType] = None
    ComponentConfiguration: Optional[str] = None
    AutoConfigEnabled: Optional[bool] = None


class UpdateComponentRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    NewComponentName: Optional[str] = None
    ResourceList: Optional[Sequence[str]] = None


class UpdateProblemRequestTypeDef(BaseValidatorModel):
    ProblemId: str
    UpdateStatus: Optional[Literal["RESOLVED"]] = None
    Visibility: Optional[VisibilityType] = None


class AddWorkloadRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef


class UpdateWorkloadRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    ComponentName: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    WorkloadId: Optional[str] = None


class AddWorkloadResponseTypeDef(BaseValidatorModel):
    WorkloadId: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeComponentConfigurationRecommendationResponseTypeDef(BaseValidatorModel):
    ComponentConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeComponentConfigurationResponseTypeDef(BaseValidatorModel):
    Monitor: bool
    Tier: TierType
    ComponentConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWorkloadResponseTypeDef(BaseValidatorModel):
    WorkloadId: str
    WorkloadRemarks: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLogPatternSetsResponseTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    AccountId: str
    LogPatternSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateWorkloadResponseTypeDef(BaseValidatorModel):
    WorkloadId: str
    WorkloadConfiguration: WorkloadConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeComponentResponseTypeDef(BaseValidatorModel):
    ApplicationComponent: ApplicationComponentTypeDef
    ResourceList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListComponentsResponseTypeDef(BaseValidatorModel):
    ApplicationComponentList: List[ApplicationComponentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationInfo: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationInfo: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListApplicationsResponseTypeDef(BaseValidatorModel):
    ApplicationInfoList: List[ApplicationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationInfo: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListConfigurationHistoryResponseTypeDef(BaseValidatorModel):
    EventList: List[ConfigurationEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateApplicationRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: Optional[str] = None
    OpsCenterEnabled: Optional[bool] = None
    CWEMonitorEnabled: Optional[bool] = None
    OpsItemSNSTopicArn: Optional[str] = None
    SNSNotificationArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AutoConfigEnabled: Optional[bool] = None
    AutoCreate: Optional[bool] = None
    GroupingType: Optional[Literal["ACCOUNT_BASED"]] = None
    AttachMissingPermission: Optional[bool] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class LogPatternTypeDef(BaseValidatorModel):
    pass


class CreateLogPatternResponseTypeDef(BaseValidatorModel):
    LogPattern: LogPatternTypeDef
    ResourceGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLogPatternResponseTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    AccountId: str
    LogPattern: LogPatternTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLogPatternsResponseTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    AccountId: str
    LogPatterns: List[LogPatternTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateLogPatternResponseTypeDef(BaseValidatorModel):
    ResourceGroupName: str
    LogPattern: LogPatternTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeObservationResponseTypeDef(BaseValidatorModel):
    Observation: ObservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RelatedObservationsTypeDef(BaseValidatorModel):
    ObservationList: Optional[List[ObservationTypeDef]] = None


class DescribeProblemResponseTypeDef(BaseValidatorModel):
    Problem: ProblemTypeDef
    SNSNotificationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListProblemsResponseTypeDef(BaseValidatorModel):
    ProblemList: List[ProblemTypeDef]
    ResourceGroupName: str
    AccountId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListConfigurationHistoryRequestTypeDef(BaseValidatorModel):
    ResourceGroupName: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventStatus: Optional[ConfigurationEventStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    AccountId: Optional[str] = None


class ListProblemsRequestTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    ResourceGroupName: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ComponentName: Optional[str] = None
    Visibility: Optional[VisibilityType] = None


class ListWorkloadsResponseTypeDef(BaseValidatorModel):
    WorkloadList: List[WorkloadTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeProblemObservationsResponseTypeDef(BaseValidatorModel):
    RelatedObservations: RelatedObservationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


