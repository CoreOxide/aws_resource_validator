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
from aws_resource_validator.pydantic_models.autoscaling_constants import *

class AcceleratorCountRequestTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class AcceleratorTotalMemoryMiBRequestTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class ActivityTypeDef(BaseModel):
    ActivityId: str
    AutoScalingGroupName: str
    Cause: str
    StartTime: datetime
    StatusCode: ScalingActivityStatusCodeType
    Description: Optional[str] = None
    EndTime: Optional[datetime] = None
    StatusMessage: Optional[str] = None
    Progress: Optional[int] = None
    Details: Optional[str] = None
    AutoScalingGroupState: Optional[str] = None
    AutoScalingGroupARN: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AdjustmentTypeTypeDef(BaseModel):
    AdjustmentType: Optional[str] = None

class AlarmSpecificationOutputTypeDef(BaseModel):
    Alarms: Optional[List[str]] = None

class AlarmSpecificationTypeDef(BaseModel):
    Alarms: Optional[Sequence[str]] = None

class AlarmTypeDef(BaseModel):
    AlarmName: Optional[str] = None
    AlarmARN: Optional[str] = None

class AttachInstancesQueryRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    InstanceIds: Optional[Sequence[str]] = None

class AttachLoadBalancerTargetGroupsTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    TargetGroupARNs: Sequence[str]

class AttachLoadBalancersTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    LoadBalancerNames: Sequence[str]

class TrafficSourceIdentifierTypeDef(BaseModel):
    Identifier: str
    Type: Optional[str] = None

class FilterTypeDef(BaseModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class EnabledMetricTypeDef(BaseModel):
    Metric: Optional[str] = None
    Granularity: Optional[str] = None

class InstanceMaintenancePolicyTypeDef(BaseModel):
    MinHealthyPercentage: Optional[int] = None
    MaxHealthyPercentage: Optional[int] = None

class LaunchTemplateSpecificationTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class SuspendedProcessTypeDef(BaseModel):
    ProcessName: Optional[str] = None
    SuspensionReason: Optional[str] = None

class TagDescriptionTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Key: Optional[str] = None
    Value: Optional[str] = None
    PropagateAtLaunch: Optional[bool] = None

class BaselineEbsBandwidthMbpsRequestTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class FailedScheduledUpdateGroupActionRequestTypeDef(BaseModel):
    ScheduledActionName: str
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchDeleteScheduledActionTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    ScheduledActionNames: Sequence[str]

class EbsTypeDef(BaseModel):
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    Encrypted: Optional[bool] = None
    Throughput: Optional[int] = None

class CancelInstanceRefreshTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str

class CapacityForecastTypeDef(BaseModel):
    Timestamps: List[datetime]
    Values: List[float]

class CompleteLifecycleActionTypeRequestTypeDef(BaseModel):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleActionResult: str
    LifecycleActionToken: Optional[str] = None
    InstanceId: Optional[str] = None

class LifecycleHookSpecificationTypeDef(BaseModel):
    LifecycleHookName: str
    LifecycleTransition: str
    NotificationMetadata: Optional[str] = None
    HeartbeatTimeout: Optional[int] = None
    DefaultResult: Optional[str] = None
    NotificationTargetARN: Optional[str] = None
    RoleARN: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Value: Optional[str] = None
    PropagateAtLaunch: Optional[bool] = None

class InstanceMetadataOptionsTypeDef(BaseModel):
    HttpTokens: Optional[InstanceMetadataHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None

class InstanceMonitoringTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class MetricDimensionTypeDef(BaseModel):
    Name: str
    Value: str

class DeleteAutoScalingGroupTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    ForceDelete: Optional[bool] = None

class DeleteLifecycleHookTypeRequestTypeDef(BaseModel):
    LifecycleHookName: str
    AutoScalingGroupName: str

class DeleteNotificationConfigurationTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    TopicARN: str

class DeletePolicyTypeRequestTypeDef(BaseModel):
    PolicyName: str
    AutoScalingGroupName: Optional[str] = None

class DeleteScheduledActionTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    ScheduledActionName: str

class DeleteWarmPoolTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    ForceDelete: Optional[bool] = None

class DescribeAutoScalingInstancesTypeRequestTypeDef(BaseModel):
    InstanceIds: Optional[Sequence[str]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceRefreshesTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    InstanceRefreshIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None

class LifecycleHookTypeDef(BaseModel):
    LifecycleHookName: Optional[str] = None
    AutoScalingGroupName: Optional[str] = None
    LifecycleTransition: Optional[str] = None
    NotificationTargetARN: Optional[str] = None
    RoleARN: Optional[str] = None
    NotificationMetadata: Optional[str] = None
    HeartbeatTimeout: Optional[int] = None
    GlobalTimeout: Optional[int] = None
    DefaultResult: Optional[str] = None

class DescribeLifecycleHooksTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    LifecycleHookNames: Optional[Sequence[str]] = None

class DescribeLoadBalancerTargetGroupsRequestRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None

class LoadBalancerTargetGroupStateTypeDef(BaseModel):
    LoadBalancerTargetGroupARN: Optional[str] = None
    State: Optional[str] = None

class DescribeLoadBalancersRequestRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None

class LoadBalancerStateTypeDef(BaseModel):
    LoadBalancerName: Optional[str] = None
    State: Optional[str] = None

class MetricCollectionTypeTypeDef(BaseModel):
    Metric: Optional[str] = None

class MetricGranularityTypeTypeDef(BaseModel):
    Granularity: Optional[str] = None

class NotificationConfigurationTypeDef(BaseModel):
    AutoScalingGroupName: Optional[str] = None
    TopicARN: Optional[str] = None
    NotificationType: Optional[str] = None

class DescribeNotificationConfigurationsTypeRequestTypeDef(BaseModel):
    AutoScalingGroupNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribePoliciesTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: Optional[str] = None
    PolicyNames: Optional[Sequence[str]] = None
    PolicyTypes: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeScalingActivitiesTypeRequestTypeDef(BaseModel):
    ActivityIds: Optional[Sequence[str]] = None
    AutoScalingGroupName: Optional[str] = None
    IncludeDeletedGroups: Optional[bool] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTrafficSourcesRequestRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    TrafficSourceType: Optional[str] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None

class TrafficSourceStateTypeDef(BaseModel):
    TrafficSource: Optional[str] = None
    State: Optional[str] = None
    Identifier: Optional[str] = None
    Type: Optional[str] = None

class DescribeWarmPoolTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DetachInstancesQueryRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    ShouldDecrementDesiredCapacity: bool
    InstanceIds: Optional[Sequence[str]] = None

class DetachLoadBalancerTargetGroupsTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    TargetGroupARNs: Sequence[str]

class DetachLoadBalancersTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    LoadBalancerNames: Sequence[str]

class DisableMetricsCollectionQueryRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    Metrics: Optional[Sequence[str]] = None

class EnableMetricsCollectionQueryRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    Granularity: str
    Metrics: Optional[Sequence[str]] = None

class EnterStandbyQueryRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    ShouldDecrementDesiredCapacity: bool
    InstanceIds: Optional[Sequence[str]] = None

class ExecutePolicyTypeRequestTypeDef(BaseModel):
    PolicyName: str
    AutoScalingGroupName: Optional[str] = None
    HonorCooldown: Optional[bool] = None
    MetricValue: Optional[float] = None
    BreachThreshold: Optional[float] = None

class ExitStandbyQueryRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    InstanceIds: Optional[Sequence[str]] = None

class InstanceRefreshLivePoolProgressTypeDef(BaseModel):
    PercentageComplete: Optional[int] = None
    InstancesToUpdate: Optional[int] = None

class InstanceRefreshWarmPoolProgressTypeDef(BaseModel):
    PercentageComplete: Optional[int] = None
    InstancesToUpdate: Optional[int] = None

class MemoryGiBPerVCpuRequestTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class MemoryMiBRequestTypeDef(BaseModel):
    Min: int
    Max: Optional[int] = None

class NetworkBandwidthGbpsRequestTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class NetworkInterfaceCountRequestTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class TotalLocalStorageGBRequestTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class VCpuCountRequestTypeDef(BaseModel):
    Min: int
    Max: Optional[int] = None

class InstanceReusePolicyTypeDef(BaseModel):
    ReuseOnScaleIn: Optional[bool] = None

class InstancesDistributionTypeDef(BaseModel):
    OnDemandAllocationStrategy: Optional[str] = None
    OnDemandBaseCapacity: Optional[int] = None
    OnDemandPercentageAboveBaseCapacity: Optional[int] = None
    SpotAllocationStrategy: Optional[str] = None
    SpotInstancePools: Optional[int] = None
    SpotMaxPrice: Optional[str] = None

class LaunchConfigurationNameTypeRequestTypeDef(BaseModel):
    LaunchConfigurationName: str

class LaunchConfigurationNamesTypeRequestTypeDef(BaseModel):
    LaunchConfigurationNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None

class PredefinedMetricSpecificationTypeDef(BaseModel):
    PredefinedMetricType: MetricTypeType
    ResourceLabel: Optional[str] = None

class PredictiveScalingPredefinedLoadMetricTypeDef(BaseModel):
    PredefinedMetricType: PredefinedLoadMetricTypeType
    ResourceLabel: Optional[str] = None

class PredictiveScalingPredefinedMetricPairTypeDef(BaseModel):
    PredefinedMetricType: PredefinedMetricPairTypeType
    ResourceLabel: Optional[str] = None

class PredictiveScalingPredefinedScalingMetricTypeDef(BaseModel):
    PredefinedMetricType: PredefinedScalingMetricTypeType
    ResourceLabel: Optional[str] = None

class ProcessTypeTypeDef(BaseModel):
    ProcessName: str

class PutLifecycleHookTypeRequestTypeDef(BaseModel):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleTransition: Optional[str] = None
    RoleARN: Optional[str] = None
    NotificationTargetARN: Optional[str] = None
    NotificationMetadata: Optional[str] = None
    HeartbeatTimeout: Optional[int] = None
    DefaultResult: Optional[str] = None

class PutNotificationConfigurationTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    TopicARN: str
    NotificationTypes: Sequence[str]

class StepAdjustmentTypeDef(BaseModel):
    ScalingAdjustment: int
    MetricIntervalLowerBound: Optional[float] = None
    MetricIntervalUpperBound: Optional[float] = None

class RecordLifecycleActionHeartbeatTypeRequestTypeDef(BaseModel):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleActionToken: Optional[str] = None
    InstanceId: Optional[str] = None

class RollbackInstanceRefreshTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str

class ScalingProcessQueryRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    ScalingProcesses: Optional[Sequence[str]] = None

class ScheduledUpdateGroupActionTypeDef(BaseModel):
    AutoScalingGroupName: Optional[str] = None
    ScheduledActionName: Optional[str] = None
    ScheduledActionARN: Optional[str] = None
    Time: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Recurrence: Optional[str] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    DesiredCapacity: Optional[int] = None
    TimeZone: Optional[str] = None

class SetDesiredCapacityTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    DesiredCapacity: int
    HonorCooldown: Optional[bool] = None

class SetInstanceHealthQueryRequestTypeDef(BaseModel):
    InstanceId: str
    HealthStatus: str
    ShouldRespectGracePeriod: Optional[bool] = None

class SetInstanceProtectionQueryRequestTypeDef(BaseModel):
    InstanceIds: Sequence[str]
    AutoScalingGroupName: str
    ProtectedFromScaleIn: bool

class TerminateInstanceInAutoScalingGroupTypeRequestTypeDef(BaseModel):
    InstanceId: str
    ShouldDecrementDesiredCapacity: bool

class ActivitiesTypeTypeDef(BaseModel):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ActivityTypeTypeDef(BaseModel):
    Activity: ActivityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelInstanceRefreshAnswerTypeDef(BaseModel):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountLimitsAnswerTypeDef(BaseModel):
    MaxNumberOfAutoScalingGroups: int
    MaxNumberOfLaunchConfigurations: int
    NumberOfAutoScalingGroups: int
    NumberOfLaunchConfigurations: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAutoScalingNotificationTypesAnswerTypeDef(BaseModel):
    AutoScalingNotificationTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLifecycleHookTypesAnswerTypeDef(BaseModel):
    LifecycleHookTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTerminationPolicyTypesAnswerTypeDef(BaseModel):
    TerminationPolicyTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DetachInstancesAnswerTypeDef(BaseModel):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnterStandbyAnswerTypeDef(BaseModel):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExitStandbyAnswerTypeDef(BaseModel):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackInstanceRefreshAnswerTypeDef(BaseModel):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartInstanceRefreshAnswerTypeDef(BaseModel):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAdjustmentTypesAnswerTypeDef(BaseModel):
    AdjustmentTypes: List[AdjustmentTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RefreshPreferencesOutputTypeDef(BaseModel):
    MinHealthyPercentage: Optional[int] = None
    InstanceWarmup: Optional[int] = None
    CheckpointPercentages: Optional[List[int]] = None
    CheckpointDelay: Optional[int] = None
    SkipMatching: Optional[bool] = None
    AutoRollback: Optional[bool] = None
    ScaleInProtectedInstances: Optional[ScaleInProtectedInstancesType] = None
    StandbyInstances: Optional[StandbyInstancesType] = None
    AlarmSpecification: Optional[AlarmSpecificationOutputTypeDef] = None
    MaxHealthyPercentage: Optional[int] = None

class RefreshPreferencesTypeDef(BaseModel):
    MinHealthyPercentage: Optional[int] = None
    InstanceWarmup: Optional[int] = None
    CheckpointPercentages: Optional[Sequence[int]] = None
    CheckpointDelay: Optional[int] = None
    SkipMatching: Optional[bool] = None
    AutoRollback: Optional[bool] = None
    ScaleInProtectedInstances: Optional[ScaleInProtectedInstancesType] = None
    StandbyInstances: Optional[StandbyInstancesType] = None
    AlarmSpecification: Optional[AlarmSpecificationTypeDef] = None
    MaxHealthyPercentage: Optional[int] = None

class PolicyARNTypeTypeDef(BaseModel):
    PolicyARN: str
    Alarms: List[AlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AttachTrafficSourcesTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    TrafficSources: Sequence[TrafficSourceIdentifierTypeDef]

class DetachTrafficSourcesTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    TrafficSources: Sequence[TrafficSourceIdentifierTypeDef]

class AutoScalingGroupNamesTypeRequestTypeDef(BaseModel):
    AutoScalingGroupNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeTagsTypeRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None

class AutoScalingGroupNamesTypeDescribeAutoScalingGroupsPaginateTypeDef(BaseModel):
    AutoScalingGroupNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAutoScalingInstancesTypeDescribeAutoScalingInstancesPaginateTypeDef(BaseModel):
    InstanceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLoadBalancerTargetGroupsRequestDescribeLoadBalancerTargetGroupsPaginateTypeDef(BaseModel):
    AutoScalingGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLoadBalancersRequestDescribeLoadBalancersPaginateTypeDef(BaseModel):
    AutoScalingGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNotificationConfigurationsTypeDescribeNotificationConfigurationsPaginateTypeDef(BaseModel):
    AutoScalingGroupNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePoliciesTypeDescribePoliciesPaginateTypeDef(BaseModel):
    AutoScalingGroupName: Optional[str] = None
    PolicyNames: Optional[Sequence[str]] = None
    PolicyTypes: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScalingActivitiesTypeDescribeScalingActivitiesPaginateTypeDef(BaseModel):
    ActivityIds: Optional[Sequence[str]] = None
    AutoScalingGroupName: Optional[str] = None
    IncludeDeletedGroups: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTagsTypeDescribeTagsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeWarmPoolTypeDescribeWarmPoolPaginateTypeDef(BaseModel):
    AutoScalingGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LaunchConfigurationNamesTypeDescribeLaunchConfigurationsPaginateTypeDef(BaseModel):
    LaunchConfigurationNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class AutoScalingInstanceDetailsTypeDef(BaseModel):
    InstanceId: str
    AutoScalingGroupName: str
    AvailabilityZone: str
    LifecycleState: str
    HealthStatus: str
    ProtectedFromScaleIn: bool
    InstanceType: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    WeightedCapacity: Optional[str] = None

class InstanceTypeDef(BaseModel):
    InstanceId: str
    AvailabilityZone: str
    LifecycleState: LifecycleStateType
    HealthStatus: str
    ProtectedFromScaleIn: bool
    InstanceType: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    WeightedCapacity: Optional[str] = None

class TagsTypeTypeDef(BaseModel):
    Tags: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchDeleteScheduledActionAnswerTypeDef(BaseModel):
    FailedScheduledActions: List[FailedScheduledUpdateGroupActionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutScheduledUpdateGroupActionAnswerTypeDef(BaseModel):
    FailedScheduledUpdateGroupActions: List[FailedScheduledUpdateGroupActionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BlockDeviceMappingTypeDef(BaseModel):
    DeviceName: str
    VirtualName: Optional[str] = None
    Ebs: Optional[EbsTypeDef] = None
    NoDevice: Optional[bool] = None

class CreateOrUpdateTagsTypeRequestTypeDef(BaseModel):
    Tags: Sequence[TagTypeDef]

class DeleteTagsTypeRequestTypeDef(BaseModel):
    Tags: Sequence[TagTypeDef]

class MetricExtraOutputTypeDef(BaseModel):
    Namespace: str
    MetricName: str
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None

class MetricOutputTypeDef(BaseModel):
    Namespace: str
    MetricName: str
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None

class MetricTypeDef(BaseModel):
    Namespace: str
    MetricName: str
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None

class DescribeLifecycleHooksAnswerTypeDef(BaseModel):
    LifecycleHooks: List[LifecycleHookTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancerTargetGroupsResponseTypeDef(BaseModel):
    LoadBalancerTargetGroups: List[LoadBalancerTargetGroupStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeLoadBalancersResponseTypeDef(BaseModel):
    LoadBalancers: List[LoadBalancerStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMetricCollectionTypesAnswerTypeDef(BaseModel):
    Metrics: List[MetricCollectionTypeTypeDef]
    Granularities: List[MetricGranularityTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotificationConfigurationsAnswerTypeDef(BaseModel):
    NotificationConfigurations: List[NotificationConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeScheduledActionsTypeDescribeScheduledActionsPaginateTypeDef(BaseModel):
    AutoScalingGroupName: Optional[str] = None
    ScheduledActionNames: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScheduledActionsTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: Optional[str] = None
    ScheduledActionNames: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None

class GetPredictiveScalingForecastTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    PolicyName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class PutScheduledUpdateGroupActionTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    ScheduledActionName: str
    Time: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Recurrence: Optional[str] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    DesiredCapacity: Optional[int] = None
    TimeZone: Optional[str] = None

class ScheduledUpdateGroupActionRequestTypeDef(BaseModel):
    ScheduledActionName: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Recurrence: Optional[str] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    DesiredCapacity: Optional[int] = None
    TimeZone: Optional[str] = None

class DescribeTrafficSourcesResponseTypeDef(BaseModel):
    TrafficSources: List[TrafficSourceStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceRefreshProgressDetailsTypeDef(BaseModel):
    LivePoolProgress: Optional[InstanceRefreshLivePoolProgressTypeDef] = None
    WarmPoolProgress: Optional[InstanceRefreshWarmPoolProgressTypeDef] = None

class InstanceRequirementsExtraOutputTypeDef(BaseModel):
    VCpuCount: VCpuCountRequestTypeDef
    MemoryMiB: MemoryMiBRequestTypeDef
    CpuManufacturers: Optional[List[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuRequestTypeDef] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCountRequestTypeDef] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[List[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGBRequestTypeDef] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsRequestTypeDef] = None
    AcceleratorTypes: Optional[List[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCountRequestTypeDef] = None
    AcceleratorManufacturers: Optional[List[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[List[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRequestTypeDef] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsRequestTypeDef] = None
    AllowedInstanceTypes: Optional[List[str]] = None

class InstanceRequirementsOutputTypeDef(BaseModel):
    VCpuCount: VCpuCountRequestTypeDef
    MemoryMiB: MemoryMiBRequestTypeDef
    CpuManufacturers: Optional[List[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuRequestTypeDef] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCountRequestTypeDef] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[List[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGBRequestTypeDef] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsRequestTypeDef] = None
    AcceleratorTypes: Optional[List[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCountRequestTypeDef] = None
    AcceleratorManufacturers: Optional[List[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[List[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRequestTypeDef] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsRequestTypeDef] = None
    AllowedInstanceTypes: Optional[List[str]] = None

class InstanceRequirementsTypeDef(BaseModel):
    VCpuCount: VCpuCountRequestTypeDef
    MemoryMiB: MemoryMiBRequestTypeDef
    CpuManufacturers: Optional[Sequence[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuRequestTypeDef] = None
    ExcludedInstanceTypes: Optional[Sequence[str]] = None
    InstanceGenerations: Optional[Sequence[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCountRequestTypeDef] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[Sequence[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGBRequestTypeDef] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsRequestTypeDef] = None
    AcceleratorTypes: Optional[Sequence[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCountRequestTypeDef] = None
    AcceleratorManufacturers: Optional[Sequence[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[Sequence[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRequestTypeDef] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsRequestTypeDef] = None
    AllowedInstanceTypes: Optional[Sequence[str]] = None

class PutWarmPoolTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    MaxGroupPreparedCapacity: Optional[int] = None
    MinSize: Optional[int] = None
    PoolState: Optional[WarmPoolStateType] = None
    InstanceReusePolicy: Optional[InstanceReusePolicyTypeDef] = None

class WarmPoolConfigurationTypeDef(BaseModel):
    MaxGroupPreparedCapacity: Optional[int] = None
    MinSize: Optional[int] = None
    PoolState: Optional[WarmPoolStateType] = None
    Status: Optional[Literal["PendingDelete"]] = None
    InstanceReusePolicy: Optional[InstanceReusePolicyTypeDef] = None

class ProcessesTypeTypeDef(BaseModel):
    Processes: List[ProcessTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionsTypeTypeDef(BaseModel):
    ScheduledUpdateGroupActions: List[ScheduledUpdateGroupActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AutoScalingInstancesTypeTypeDef(BaseModel):
    AutoScalingInstances: List[AutoScalingInstanceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateLaunchConfigurationTypeRequestTypeDef(BaseModel):
    LaunchConfigurationName: str
    ImageId: Optional[str] = None
    KeyName: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    ClassicLinkVPCId: Optional[str] = None
    ClassicLinkVPCSecurityGroups: Optional[Sequence[str]] = None
    UserData: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    RamdiskId: Optional[str] = None
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    InstanceMonitoring: Optional[InstanceMonitoringTypeDef] = None
    SpotPrice: Optional[str] = None
    IamInstanceProfile: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    PlacementTenancy: Optional[str] = None
    MetadataOptions: Optional[InstanceMetadataOptionsTypeDef] = None

class LaunchConfigurationTypeDef(BaseModel):
    LaunchConfigurationName: str
    ImageId: str
    InstanceType: str
    CreatedTime: datetime
    LaunchConfigurationARN: Optional[str] = None
    KeyName: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    ClassicLinkVPCId: Optional[str] = None
    ClassicLinkVPCSecurityGroups: Optional[List[str]] = None
    UserData: Optional[str] = None
    KernelId: Optional[str] = None
    RamdiskId: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMappingTypeDef]] = None
    InstanceMonitoring: Optional[InstanceMonitoringTypeDef] = None
    SpotPrice: Optional[str] = None
    IamInstanceProfile: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    PlacementTenancy: Optional[str] = None
    MetadataOptions: Optional[InstanceMetadataOptionsTypeDef] = None

class MetricStatExtraOutputTypeDef(BaseModel):
    Metric: MetricExtraOutputTypeDef
    Stat: str
    Unit: Optional[str] = None

class TargetTrackingMetricStatExtraOutputTypeDef(BaseModel):
    Metric: MetricExtraOutputTypeDef
    Stat: str
    Unit: Optional[str] = None

class MetricStatOutputTypeDef(BaseModel):
    Metric: MetricOutputTypeDef
    Stat: str
    Unit: Optional[str] = None

class TargetTrackingMetricStatOutputTypeDef(BaseModel):
    Metric: MetricOutputTypeDef
    Stat: str
    Unit: Optional[str] = None

class MetricStatTypeDef(BaseModel):
    Metric: MetricTypeDef
    Stat: str
    Unit: Optional[str] = None

class TargetTrackingMetricStatTypeDef(BaseModel):
    Metric: MetricTypeDef
    Stat: str
    Unit: Optional[str] = None

class BatchPutScheduledUpdateGroupActionTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    ScheduledUpdateGroupActions: Sequence[ScheduledUpdateGroupActionRequestTypeDef]

class RollbackDetailsTypeDef(BaseModel):
    RollbackReason: Optional[str] = None
    RollbackStartTime: Optional[datetime] = None
    PercentageCompleteOnRollback: Optional[int] = None
    InstancesToUpdateOnRollback: Optional[int] = None
    ProgressDetailsOnRollback: Optional[InstanceRefreshProgressDetailsTypeDef] = None

class LaunchTemplateOverridesExtraOutputTypeDef(BaseModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[str] = None
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecificationTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsExtraOutputTypeDef] = None

class LaunchTemplateOverridesOutputTypeDef(BaseModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[str] = None
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecificationTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsOutputTypeDef] = None

class LaunchTemplateOverridesTypeDef(BaseModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[str] = None
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecificationTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsTypeDef] = None

class DescribeWarmPoolAnswerTypeDef(BaseModel):
    WarmPoolConfiguration: WarmPoolConfigurationTypeDef
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LaunchConfigurationsTypeTypeDef(BaseModel):
    LaunchConfigurations: List[LaunchConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MetricDataQueryExtraOutputTypeDef(BaseModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[MetricStatExtraOutputTypeDef] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None

class TargetTrackingMetricDataQueryExtraOutputTypeDef(BaseModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatExtraOutputTypeDef] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None

class MetricDataQueryOutputTypeDef(BaseModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[MetricStatOutputTypeDef] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None

class TargetTrackingMetricDataQueryOutputTypeDef(BaseModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatOutputTypeDef] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None

class MetricDataQueryTypeDef(BaseModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[MetricStatTypeDef] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None

class TargetTrackingMetricDataQueryTypeDef(BaseModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatTypeDef] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None

class LaunchTemplateExtraOutputTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[List[LaunchTemplateOverridesExtraOutputTypeDef]] = None

class LaunchTemplateOutputTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[List[LaunchTemplateOverridesOutputTypeDef]] = None

class LaunchTemplateTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[Sequence[LaunchTemplateOverridesTypeDef]] = None

class PredictiveScalingCustomizedCapacityMetricExtraOutputTypeDef(BaseModel):
    MetricDataQueries: List[MetricDataQueryExtraOutputTypeDef]

class PredictiveScalingCustomizedLoadMetricExtraOutputTypeDef(BaseModel):
    MetricDataQueries: List[MetricDataQueryExtraOutputTypeDef]

class PredictiveScalingCustomizedScalingMetricExtraOutputTypeDef(BaseModel):
    MetricDataQueries: List[MetricDataQueryExtraOutputTypeDef]

class CustomizedMetricSpecificationExtraOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[List[TargetTrackingMetricDataQueryExtraOutputTypeDef]] = None

class PredictiveScalingCustomizedCapacityMetricOutputTypeDef(BaseModel):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]

class PredictiveScalingCustomizedLoadMetricOutputTypeDef(BaseModel):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]

class PredictiveScalingCustomizedScalingMetricOutputTypeDef(BaseModel):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]

class CustomizedMetricSpecificationOutputTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[List[TargetTrackingMetricDataQueryOutputTypeDef]] = None

class PredictiveScalingCustomizedCapacityMetricTypeDef(BaseModel):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]

class PredictiveScalingCustomizedLoadMetricTypeDef(BaseModel):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]

class PredictiveScalingCustomizedScalingMetricTypeDef(BaseModel):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]

class CustomizedMetricSpecificationTypeDef(BaseModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Metrics: Optional[Sequence[TargetTrackingMetricDataQueryTypeDef]] = None

class MixedInstancesPolicyExtraOutputTypeDef(BaseModel):
    LaunchTemplate: Optional[LaunchTemplateExtraOutputTypeDef] = None
    InstancesDistribution: Optional[InstancesDistributionTypeDef] = None

class MixedInstancesPolicyOutputTypeDef(BaseModel):
    LaunchTemplate: Optional[LaunchTemplateOutputTypeDef] = None
    InstancesDistribution: Optional[InstancesDistributionTypeDef] = None

class MixedInstancesPolicyTypeDef(BaseModel):
    LaunchTemplate: Optional[LaunchTemplateTypeDef] = None
    InstancesDistribution: Optional[InstancesDistributionTypeDef] = None

class PredictiveScalingMetricSpecificationExtraOutputTypeDef(BaseModel):
    TargetValue: float
    PredefinedMetricPairSpecification: Optional[       PredictiveScalingPredefinedMetricPairTypeDef     ] = None
    PredefinedScalingMetricSpecification: Optional[       PredictiveScalingPredefinedScalingMetricTypeDef     ] = None
    PredefinedLoadMetricSpecification: Optional[       PredictiveScalingPredefinedLoadMetricTypeDef     ] = None
    CustomizedScalingMetricSpecification: Optional[       PredictiveScalingCustomizedScalingMetricExtraOutputTypeDef     ] = None
    CustomizedLoadMetricSpecification: Optional[       PredictiveScalingCustomizedLoadMetricExtraOutputTypeDef     ] = None
    CustomizedCapacityMetricSpecification: Optional[       PredictiveScalingCustomizedCapacityMetricExtraOutputTypeDef     ] = None

class TargetTrackingConfigurationExtraOutputTypeDef(BaseModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[       CustomizedMetricSpecificationExtraOutputTypeDef     ] = None
    DisableScaleIn: Optional[bool] = None

class PredictiveScalingMetricSpecificationOutputTypeDef(BaseModel):
    TargetValue: float
    PredefinedMetricPairSpecification: Optional[       PredictiveScalingPredefinedMetricPairTypeDef     ] = None
    PredefinedScalingMetricSpecification: Optional[       PredictiveScalingPredefinedScalingMetricTypeDef     ] = None
    PredefinedLoadMetricSpecification: Optional[       PredictiveScalingPredefinedLoadMetricTypeDef     ] = None
    CustomizedScalingMetricSpecification: Optional[       PredictiveScalingCustomizedScalingMetricOutputTypeDef     ] = None
    CustomizedLoadMetricSpecification: Optional[       PredictiveScalingCustomizedLoadMetricOutputTypeDef     ] = None
    CustomizedCapacityMetricSpecification: Optional[       PredictiveScalingCustomizedCapacityMetricOutputTypeDef     ] = None

class TargetTrackingConfigurationOutputTypeDef(BaseModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecificationOutputTypeDef] = None
    DisableScaleIn: Optional[bool] = None

class PredictiveScalingMetricSpecificationTypeDef(BaseModel):
    TargetValue: float
    PredefinedMetricPairSpecification: Optional[       PredictiveScalingPredefinedMetricPairTypeDef     ] = None
    PredefinedScalingMetricSpecification: Optional[       PredictiveScalingPredefinedScalingMetricTypeDef     ] = None
    PredefinedLoadMetricSpecification: Optional[       PredictiveScalingPredefinedLoadMetricTypeDef     ] = None
    CustomizedScalingMetricSpecification: Optional[       PredictiveScalingCustomizedScalingMetricTypeDef     ] = None
    CustomizedLoadMetricSpecification: Optional[       PredictiveScalingCustomizedLoadMetricTypeDef     ] = None
    CustomizedCapacityMetricSpecification: Optional[       PredictiveScalingCustomizedCapacityMetricTypeDef     ] = None

class TargetTrackingConfigurationTypeDef(BaseModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecificationTypeDef] = None
    DisableScaleIn: Optional[bool] = None

class AutoScalingGroupTypeDef(BaseModel):
    AutoScalingGroupName: str
    MinSize: int
    MaxSize: int
    DesiredCapacity: int
    DefaultCooldown: int
    AvailabilityZones: List[str]
    HealthCheckType: str
    CreatedTime: datetime
    AutoScalingGroupARN: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyOutputTypeDef] = None
    PredictedCapacity: Optional[int] = None
    LoadBalancerNames: Optional[List[str]] = None
    TargetGroupARNs: Optional[List[str]] = None
    HealthCheckGracePeriod: Optional[int] = None
    Instances: Optional[List[InstanceTypeDef]] = None
    SuspendedProcesses: Optional[List[SuspendedProcessTypeDef]] = None
    PlacementGroup: Optional[str] = None
    VPCZoneIdentifier: Optional[str] = None
    EnabledMetrics: Optional[List[EnabledMetricTypeDef]] = None
    Status: Optional[str] = None
    Tags: Optional[List[TagDescriptionTypeDef]] = None
    TerminationPolicies: Optional[List[str]] = None
    NewInstancesProtectedFromScaleIn: Optional[bool] = None
    ServiceLinkedRoleARN: Optional[str] = None
    MaxInstanceLifetime: Optional[int] = None
    CapacityRebalance: Optional[bool] = None
    WarmPoolConfiguration: Optional[WarmPoolConfigurationTypeDef] = None
    WarmPoolSize: Optional[int] = None
    Context: Optional[str] = None
    DesiredCapacityType: Optional[str] = None
    DefaultInstanceWarmup: Optional[int] = None
    TrafficSources: Optional[List[TrafficSourceIdentifierTypeDef]] = None
    InstanceMaintenancePolicy: Optional[InstanceMaintenancePolicyTypeDef] = None

class DesiredConfigurationOutputTypeDef(BaseModel):
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyOutputTypeDef] = None

class CreateAutoScalingGroupTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    MinSize: int
    MaxSize: int
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyTypeDef] = None
    InstanceId: Optional[str] = None
    DesiredCapacity: Optional[int] = None
    DefaultCooldown: Optional[int] = None
    AvailabilityZones: Optional[Sequence[str]] = None
    LoadBalancerNames: Optional[Sequence[str]] = None
    TargetGroupARNs: Optional[Sequence[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    PlacementGroup: Optional[str] = None
    VPCZoneIdentifier: Optional[str] = None
    TerminationPolicies: Optional[Sequence[str]] = None
    NewInstancesProtectedFromScaleIn: Optional[bool] = None
    CapacityRebalance: Optional[bool] = None
    LifecycleHookSpecificationList: Optional[Sequence[LifecycleHookSpecificationTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ServiceLinkedRoleARN: Optional[str] = None
    MaxInstanceLifetime: Optional[int] = None
    Context: Optional[str] = None
    DesiredCapacityType: Optional[str] = None
    DefaultInstanceWarmup: Optional[int] = None
    TrafficSources: Optional[Sequence[TrafficSourceIdentifierTypeDef]] = None
    InstanceMaintenancePolicy: Optional[InstanceMaintenancePolicyTypeDef] = None

class DesiredConfigurationTypeDef(BaseModel):
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyTypeDef] = None

class UpdateAutoScalingGroupTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyTypeDef] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    DesiredCapacity: Optional[int] = None
    DefaultCooldown: Optional[int] = None
    AvailabilityZones: Optional[Sequence[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    PlacementGroup: Optional[str] = None
    VPCZoneIdentifier: Optional[str] = None
    TerminationPolicies: Optional[Sequence[str]] = None
    NewInstancesProtectedFromScaleIn: Optional[bool] = None
    ServiceLinkedRoleARN: Optional[str] = None
    MaxInstanceLifetime: Optional[int] = None
    CapacityRebalance: Optional[bool] = None
    Context: Optional[str] = None
    DesiredCapacityType: Optional[str] = None
    DefaultInstanceWarmup: Optional[int] = None
    InstanceMaintenancePolicy: Optional[InstanceMaintenancePolicyTypeDef] = None

class PredictiveScalingConfigurationExtraOutputTypeDef(BaseModel):
    MetricSpecifications: List[PredictiveScalingMetricSpecificationExtraOutputTypeDef]
    Mode: Optional[PredictiveScalingModeType] = None
    SchedulingBufferTime: Optional[int] = None
    MaxCapacityBreachBehavior: Optional[PredictiveScalingMaxCapacityBreachBehaviorType] = None
    MaxCapacityBuffer: Optional[int] = None

class LoadForecastTypeDef(BaseModel):
    Timestamps: List[datetime]
    Values: List[float]
    MetricSpecification: PredictiveScalingMetricSpecificationOutputTypeDef

class PredictiveScalingConfigurationOutputTypeDef(BaseModel):
    MetricSpecifications: List[PredictiveScalingMetricSpecificationOutputTypeDef]
    Mode: Optional[PredictiveScalingModeType] = None
    SchedulingBufferTime: Optional[int] = None
    MaxCapacityBreachBehavior: Optional[PredictiveScalingMaxCapacityBreachBehaviorType] = None
    MaxCapacityBuffer: Optional[int] = None

class PredictiveScalingConfigurationTypeDef(BaseModel):
    MetricSpecifications: Sequence[PredictiveScalingMetricSpecificationTypeDef]
    Mode: Optional[PredictiveScalingModeType] = None
    SchedulingBufferTime: Optional[int] = None
    MaxCapacityBreachBehavior: Optional[PredictiveScalingMaxCapacityBreachBehaviorType] = None
    MaxCapacityBuffer: Optional[int] = None

class AutoScalingGroupsTypeTypeDef(BaseModel):
    AutoScalingGroups: List[AutoScalingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceRefreshTypeDef(BaseModel):
    InstanceRefreshId: Optional[str] = None
    AutoScalingGroupName: Optional[str] = None
    Status: Optional[InstanceRefreshStatusType] = None
    StatusReason: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    PercentageComplete: Optional[int] = None
    InstancesToUpdate: Optional[int] = None
    ProgressDetails: Optional[InstanceRefreshProgressDetailsTypeDef] = None
    Preferences: Optional[RefreshPreferencesOutputTypeDef] = None
    DesiredConfiguration: Optional[DesiredConfigurationOutputTypeDef] = None
    RollbackDetails: Optional[RollbackDetailsTypeDef] = None

class StartInstanceRefreshTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    Strategy: Optional[Literal["Rolling"]] = None
    DesiredConfiguration: Optional[DesiredConfigurationTypeDef] = None
    Preferences: Optional[RefreshPreferencesTypeDef] = None

class GetPredictiveScalingForecastAnswerTypeDef(BaseModel):
    LoadForecast: List[LoadForecastTypeDef]
    CapacityForecast: CapacityForecastTypeDef
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ScalingPolicyTypeDef(BaseModel):
    AutoScalingGroupName: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyARN: Optional[str] = None
    PolicyType: Optional[str] = None
    AdjustmentType: Optional[str] = None
    MinAdjustmentStep: Optional[int] = None
    MinAdjustmentMagnitude: Optional[int] = None
    ScalingAdjustment: Optional[int] = None
    Cooldown: Optional[int] = None
    StepAdjustments: Optional[List[StepAdjustmentTypeDef]] = None
    MetricAggregationType: Optional[str] = None
    EstimatedInstanceWarmup: Optional[int] = None
    Alarms: Optional[List[AlarmTypeDef]] = None
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationOutputTypeDef] = None
    Enabled: Optional[bool] = None
    PredictiveScalingConfiguration: Optional[PredictiveScalingConfigurationOutputTypeDef] = None

class PutScalingPolicyTypeRequestTypeDef(BaseModel):
    AutoScalingGroupName: str
    PolicyName: str
    PolicyType: Optional[str] = None
    AdjustmentType: Optional[str] = None
    MinAdjustmentStep: Optional[int] = None
    MinAdjustmentMagnitude: Optional[int] = None
    ScalingAdjustment: Optional[int] = None
    Cooldown: Optional[int] = None
    MetricAggregationType: Optional[str] = None
    StepAdjustments: Optional[Sequence[StepAdjustmentTypeDef]] = None
    EstimatedInstanceWarmup: Optional[int] = None
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationTypeDef] = None
    Enabled: Optional[bool] = None
    PredictiveScalingConfiguration: Optional[PredictiveScalingConfigurationTypeDef] = None

class DescribeInstanceRefreshesAnswerTypeDef(BaseModel):
    InstanceRefreshes: List[InstanceRefreshTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PoliciesTypeTypeDef(BaseModel):
    ScalingPolicies: List[ScalingPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

