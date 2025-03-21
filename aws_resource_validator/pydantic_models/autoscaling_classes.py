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
from aws_resource_validator.pydantic_models.autoscaling_constants import *

class AcceleratorCountRequestTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class AcceleratorTotalMemoryMiBRequestTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class ActivityTypeDef(BaseValidatorModel):
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


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AdjustmentTypeTypeDef(BaseValidatorModel):
    AdjustmentType: Optional[str] = None


class AlarmSpecificationOutputTypeDef(BaseValidatorModel):
    Alarms: Optional[List[str]] = None


class AlarmSpecificationTypeDef(BaseValidatorModel):
    Alarms: Optional[Sequence[str]] = None


class AlarmTypeDef(BaseValidatorModel):
    AlarmName: Optional[str] = None
    AlarmARN: Optional[str] = None


class AttachInstancesQueryTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    InstanceIds: Optional[Sequence[str]] = None


class AttachLoadBalancerTargetGroupsTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    TargetGroupARNs: Sequence[str]


class AttachLoadBalancersTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    LoadBalancerNames: Sequence[str]


class FilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class AvailabilityZoneDistributionTypeDef(BaseValidatorModel):
    CapacityDistributionStrategy: Optional[CapacityDistributionStrategyType] = None


class AvailabilityZoneImpairmentPolicyTypeDef(BaseValidatorModel):
    ZonalShiftEnabled: Optional[bool] = None
    ImpairedZoneHealthCheckBehavior: Optional[ImpairedZoneHealthCheckBehaviorType] = None


class EnabledMetricTypeDef(BaseValidatorModel):
    Metric: Optional[str] = None
    Granularity: Optional[str] = None


class InstanceMaintenancePolicyTypeDef(BaseValidatorModel):
    MinHealthyPercentage: Optional[int] = None
    MaxHealthyPercentage: Optional[int] = None


class LaunchTemplateSpecificationTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None


class SuspendedProcessTypeDef(BaseValidatorModel):
    ProcessName: Optional[str] = None
    SuspensionReason: Optional[str] = None


class TagDescriptionTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Key: Optional[str] = None
    Value: Optional[str] = None
    PropagateAtLaunch: Optional[bool] = None


class BaselineEbsBandwidthMbpsRequestTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class FailedScheduledUpdateGroupActionRequestTypeDef(BaseValidatorModel):
    ScheduledActionName: str
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class BatchDeleteScheduledActionTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    ScheduledActionNames: Sequence[str]


class EbsTypeDef(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    Encrypted: Optional[bool] = None
    Throughput: Optional[int] = None


class CancelInstanceRefreshTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str


class CapacityForecastTypeDef(BaseValidatorModel):
    Timestamps: List[datetime]
    Values: List[float]


class CapacityReservationTargetOutputTypeDef(BaseValidatorModel):
    CapacityReservationIds: Optional[List[str]] = None
    CapacityReservationResourceGroupArns: Optional[List[str]] = None


class CapacityReservationTargetTypeDef(BaseValidatorModel):
    CapacityReservationIds: Optional[Sequence[str]] = None
    CapacityReservationResourceGroupArns: Optional[Sequence[str]] = None


class CompleteLifecycleActionTypeTypeDef(BaseValidatorModel):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleActionResult: str
    LifecycleActionToken: Optional[str] = None
    InstanceId: Optional[str] = None


class PerformanceFactorReferenceRequestTypeDef(BaseValidatorModel):
    InstanceFamily: Optional[str] = None


class LifecycleHookSpecificationTypeDef(BaseValidatorModel):
    LifecycleHookName: str
    LifecycleTransition: str
    NotificationMetadata: Optional[str] = None
    HeartbeatTimeout: Optional[int] = None
    DefaultResult: Optional[str] = None
    NotificationTargetARN: Optional[str] = None
    RoleARN: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Value: Optional[str] = None
    PropagateAtLaunch: Optional[bool] = None


class InstanceMetadataOptionsTypeDef(BaseValidatorModel):
    HttpTokens: Optional[InstanceMetadataHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None


class InstanceMonitoringTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None


class MetricDimensionTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class DeleteAutoScalingGroupTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    ForceDelete: Optional[bool] = None


class DeleteLifecycleHookTypeTypeDef(BaseValidatorModel):
    LifecycleHookName: str
    AutoScalingGroupName: str


class DeleteNotificationConfigurationTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    TopicARN: str


class DeletePolicyTypeTypeDef(BaseValidatorModel):
    PolicyName: str
    AutoScalingGroupName: Optional[str] = None


class DeleteScheduledActionTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    ScheduledActionName: str


class DeleteWarmPoolTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    ForceDelete: Optional[bool] = None


class DescribeAutoScalingInstancesTypeTypeDef(BaseValidatorModel):
    InstanceIds: Optional[Sequence[str]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstanceRefreshesTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    InstanceRefreshIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class LifecycleHookTypeDef(BaseValidatorModel):
    LifecycleHookName: Optional[str] = None
    AutoScalingGroupName: Optional[str] = None
    LifecycleTransition: Optional[str] = None
    NotificationTargetARN: Optional[str] = None
    RoleARN: Optional[str] = None
    NotificationMetadata: Optional[str] = None
    HeartbeatTimeout: Optional[int] = None
    GlobalTimeout: Optional[int] = None
    DefaultResult: Optional[str] = None


class DescribeLifecycleHooksTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    LifecycleHookNames: Optional[Sequence[str]] = None


class DescribeLoadBalancerTargetGroupsRequestTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class LoadBalancerTargetGroupStateTypeDef(BaseValidatorModel):
    LoadBalancerTargetGroupARN: Optional[str] = None
    State: Optional[str] = None


class DescribeLoadBalancersRequestTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class LoadBalancerStateTypeDef(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    State: Optional[str] = None


class MetricCollectionTypeTypeDef(BaseValidatorModel):
    Metric: Optional[str] = None


class MetricGranularityTypeTypeDef(BaseValidatorModel):
    Granularity: Optional[str] = None


class NotificationConfigurationTypeDef(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    TopicARN: Optional[str] = None
    NotificationType: Optional[str] = None


class DescribeNotificationConfigurationsTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribePoliciesTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    PolicyNames: Optional[Sequence[str]] = None
    PolicyTypes: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeScalingActivitiesTypeTypeDef(BaseValidatorModel):
    ActivityIds: Optional[Sequence[str]] = None
    AutoScalingGroupName: Optional[str] = None
    IncludeDeletedGroups: Optional[bool] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeTrafficSourcesRequestTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    TrafficSourceType: Optional[str] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class DescribeWarmPoolTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DetachInstancesQueryTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    ShouldDecrementDesiredCapacity: bool
    InstanceIds: Optional[Sequence[str]] = None


class DetachLoadBalancerTargetGroupsTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    TargetGroupARNs: Sequence[str]


class DetachLoadBalancersTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    LoadBalancerNames: Sequence[str]


class DisableMetricsCollectionQueryTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    Metrics: Optional[Sequence[str]] = None


class EnableMetricsCollectionQueryTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    Granularity: str
    Metrics: Optional[Sequence[str]] = None


class EnterStandbyQueryTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    ShouldDecrementDesiredCapacity: bool
    InstanceIds: Optional[Sequence[str]] = None


class ExecutePolicyTypeTypeDef(BaseValidatorModel):
    PolicyName: str
    AutoScalingGroupName: Optional[str] = None
    HonorCooldown: Optional[bool] = None
    MetricValue: Optional[float] = None
    BreachThreshold: Optional[float] = None


class ExitStandbyQueryTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    InstanceIds: Optional[Sequence[str]] = None


class InstanceRefreshLivePoolProgressTypeDef(BaseValidatorModel):
    PercentageComplete: Optional[int] = None
    InstancesToUpdate: Optional[int] = None


class InstanceRefreshWarmPoolProgressTypeDef(BaseValidatorModel):
    PercentageComplete: Optional[int] = None
    InstancesToUpdate: Optional[int] = None


class MemoryGiBPerVCpuRequestTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class MemoryMiBRequestTypeDef(BaseValidatorModel):
    Min: int
    Max: Optional[int] = None


class NetworkBandwidthGbpsRequestTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class NetworkInterfaceCountRequestTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class TotalLocalStorageGBRequestTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class VCpuCountRequestTypeDef(BaseValidatorModel):
    Min: int
    Max: Optional[int] = None


class InstanceReusePolicyTypeDef(BaseValidatorModel):
    ReuseOnScaleIn: Optional[bool] = None


class InstancesDistributionTypeDef(BaseValidatorModel):
    OnDemandAllocationStrategy: Optional[str] = None
    OnDemandBaseCapacity: Optional[int] = None
    OnDemandPercentageAboveBaseCapacity: Optional[int] = None
    SpotAllocationStrategy: Optional[str] = None
    SpotInstancePools: Optional[int] = None
    SpotMaxPrice: Optional[str] = None


class LaunchConfigurationNameTypeTypeDef(BaseValidatorModel):
    LaunchConfigurationName: str


class LaunchConfigurationNamesTypeTypeDef(BaseValidatorModel):
    LaunchConfigurationNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class PredefinedMetricSpecificationTypeDef(BaseValidatorModel):
    PredefinedMetricType: MetricTypeType
    ResourceLabel: Optional[str] = None


class PredictiveScalingPredefinedLoadMetricTypeDef(BaseValidatorModel):
    PredefinedMetricType: PredefinedLoadMetricTypeType
    ResourceLabel: Optional[str] = None


class PredictiveScalingPredefinedMetricPairTypeDef(BaseValidatorModel):
    PredefinedMetricType: PredefinedMetricPairTypeType
    ResourceLabel: Optional[str] = None


class PredictiveScalingPredefinedScalingMetricTypeDef(BaseValidatorModel):
    PredefinedMetricType: PredefinedScalingMetricTypeType
    ResourceLabel: Optional[str] = None


class ProcessTypeTypeDef(BaseValidatorModel):
    ProcessName: str


class PutLifecycleHookTypeTypeDef(BaseValidatorModel):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleTransition: Optional[str] = None
    RoleARN: Optional[str] = None
    NotificationTargetARN: Optional[str] = None
    NotificationMetadata: Optional[str] = None
    HeartbeatTimeout: Optional[int] = None
    DefaultResult: Optional[str] = None


class PutNotificationConfigurationTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    TopicARN: str
    NotificationTypes: Sequence[str]


class StepAdjustmentTypeDef(BaseValidatorModel):
    ScalingAdjustment: int
    MetricIntervalLowerBound: Optional[float] = None
    MetricIntervalUpperBound: Optional[float] = None


class RecordLifecycleActionHeartbeatTypeTypeDef(BaseValidatorModel):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleActionToken: Optional[str] = None
    InstanceId: Optional[str] = None


class RollbackInstanceRefreshTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str


class ScalingProcessQueryRequestTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    ScalingProcesses: Optional[Sequence[str]] = None


class ScalingProcessQueryTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    ScalingProcesses: Optional[Sequence[str]] = None


class ScheduledUpdateGroupActionTypeDef(BaseValidatorModel):
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


class SetDesiredCapacityTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    DesiredCapacity: int
    HonorCooldown: Optional[bool] = None


class SetInstanceHealthQueryTypeDef(BaseValidatorModel):
    InstanceId: str
    HealthStatus: str
    ShouldRespectGracePeriod: Optional[bool] = None


class SetInstanceProtectionQueryTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]
    AutoScalingGroupName: str
    ProtectedFromScaleIn: bool


class TerminateInstanceInAutoScalingGroupTypeTypeDef(BaseValidatorModel):
    InstanceId: str
    ShouldDecrementDesiredCapacity: bool


class ActivitiesTypeTypeDef(BaseValidatorModel):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ActivityTypeTypeDef(BaseValidatorModel):
    Activity: ActivityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CancelInstanceRefreshAnswerTypeDef(BaseValidatorModel):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountLimitsAnswerTypeDef(BaseValidatorModel):
    MaxNumberOfAutoScalingGroups: int
    MaxNumberOfLaunchConfigurations: int
    NumberOfAutoScalingGroups: int
    NumberOfLaunchConfigurations: int
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAutoScalingNotificationTypesAnswerTypeDef(BaseValidatorModel):
    AutoScalingNotificationTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLifecycleHookTypesAnswerTypeDef(BaseValidatorModel):
    LifecycleHookTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTerminationPolicyTypesAnswerTypeDef(BaseValidatorModel):
    TerminationPolicyTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class DetachInstancesAnswerTypeDef(BaseValidatorModel):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class EnterStandbyAnswerTypeDef(BaseValidatorModel):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ExitStandbyAnswerTypeDef(BaseValidatorModel):
    Activities: List[ActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RollbackInstanceRefreshAnswerTypeDef(BaseValidatorModel):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartInstanceRefreshAnswerTypeDef(BaseValidatorModel):
    InstanceRefreshId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAdjustmentTypesAnswerTypeDef(BaseValidatorModel):
    AdjustmentTypes: List[AdjustmentTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RefreshPreferencesOutputTypeDef(BaseValidatorModel):
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
    BakeTime: Optional[int] = None


class RefreshPreferencesTypeDef(BaseValidatorModel):
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
    BakeTime: Optional[int] = None


class PolicyARNTypeTypeDef(BaseValidatorModel):
    PolicyARN: str
    Alarms: List[AlarmTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TrafficSourceIdentifierTypeDef(BaseValidatorModel):
    pass


class AttachTrafficSourcesTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    TrafficSources: Sequence[TrafficSourceIdentifierTypeDef]
    SkipZonalShiftValidation: Optional[bool] = None


class DetachTrafficSourcesTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    TrafficSources: Sequence[TrafficSourceIdentifierTypeDef]


class AutoScalingGroupNamesTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class DescribeTagsTypeTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class AutoScalingGroupNamesTypePaginateTypeDef(BaseValidatorModel):
    AutoScalingGroupNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAutoScalingInstancesTypePaginateTypeDef(BaseValidatorModel):
    InstanceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeLoadBalancerTargetGroupsRequestPaginateTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeLoadBalancersRequestPaginateTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeNotificationConfigurationsTypePaginateTypeDef(BaseValidatorModel):
    AutoScalingGroupNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribePoliciesTypePaginateTypeDef(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    PolicyNames: Optional[Sequence[str]] = None
    PolicyTypes: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeScalingActivitiesTypePaginateTypeDef(BaseValidatorModel):
    ActivityIds: Optional[Sequence[str]] = None
    AutoScalingGroupName: Optional[str] = None
    IncludeDeletedGroups: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeTagsTypePaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeWarmPoolTypePaginateTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class LaunchConfigurationNamesTypePaginateTypeDef(BaseValidatorModel):
    LaunchConfigurationNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class AutoScalingInstanceDetailsTypeDef(BaseValidatorModel):
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


class InstanceTypeDef(BaseValidatorModel):
    InstanceId: str
    AvailabilityZone: str
    LifecycleState: LifecycleStateType
    HealthStatus: str
    ProtectedFromScaleIn: bool
    InstanceType: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    WeightedCapacity: Optional[str] = None


class TagsTypeTypeDef(BaseValidatorModel):
    Tags: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchDeleteScheduledActionAnswerTypeDef(BaseValidatorModel):
    FailedScheduledActions: List[FailedScheduledUpdateGroupActionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchPutScheduledUpdateGroupActionAnswerTypeDef(BaseValidatorModel):
    FailedScheduledUpdateGroupActions: List[FailedScheduledUpdateGroupActionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BlockDeviceMappingTypeDef(BaseValidatorModel):
    DeviceName: str
    VirtualName: Optional[str] = None
    Ebs: Optional[EbsTypeDef] = None
    NoDevice: Optional[bool] = None


class CapacityReservationSpecificationOutputTypeDef(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetOutputTypeDef] = None


class CapacityReservationSpecificationTypeDef(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetTypeDef] = None


class CpuPerformanceFactorRequestOutputTypeDef(BaseValidatorModel):
    References: Optional[List[PerformanceFactorReferenceRequestTypeDef]] = None


class CpuPerformanceFactorRequestTypeDef(BaseValidatorModel):
    References: Optional[Sequence[PerformanceFactorReferenceRequestTypeDef]] = None


class CreateOrUpdateTagsTypeTypeDef(BaseValidatorModel):
    Tags: Sequence[TagTypeDef]


class DeleteTagsTypeTypeDef(BaseValidatorModel):
    Tags: Sequence[TagTypeDef]


class MetricOutputTypeDef(BaseValidatorModel):
    Namespace: str
    MetricName: str
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None


class MetricTypeDef(BaseValidatorModel):
    Namespace: str
    MetricName: str
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None


class DescribeLifecycleHooksAnswerTypeDef(BaseValidatorModel):
    LifecycleHooks: List[LifecycleHookTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLoadBalancerTargetGroupsResponseTypeDef(BaseValidatorModel):
    LoadBalancerTargetGroups: List[LoadBalancerTargetGroupStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeLoadBalancersResponseTypeDef(BaseValidatorModel):
    LoadBalancers: List[LoadBalancerStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeMetricCollectionTypesAnswerTypeDef(BaseValidatorModel):
    Metrics: List[MetricCollectionTypeTypeDef]
    Granularities: List[MetricGranularityTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeNotificationConfigurationsAnswerTypeDef(BaseValidatorModel):
    NotificationConfigurations: List[NotificationConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DescribeScheduledActionsTypePaginateTypeDef(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    ScheduledActionNames: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeScheduledActionsTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: Optional[str] = None
    ScheduledActionNames: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxRecords: Optional[int] = None


class GetPredictiveScalingForecastTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    PolicyName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef


class PutScheduledUpdateGroupActionTypeTypeDef(BaseValidatorModel):
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


class ScheduledUpdateGroupActionRequestTypeDef(BaseValidatorModel):
    ScheduledActionName: str
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Recurrence: Optional[str] = None
    MinSize: Optional[int] = None
    MaxSize: Optional[int] = None
    DesiredCapacity: Optional[int] = None
    TimeZone: Optional[str] = None


class TrafficSourceStateTypeDef(BaseValidatorModel):
    pass


class DescribeTrafficSourcesResponseTypeDef(BaseValidatorModel):
    TrafficSources: List[TrafficSourceStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class InstanceRefreshProgressDetailsTypeDef(BaseValidatorModel):
    LivePoolProgress: Optional[InstanceRefreshLivePoolProgressTypeDef] = None
    WarmPoolProgress: Optional[InstanceRefreshWarmPoolProgressTypeDef] = None


class PutWarmPoolTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    MaxGroupPreparedCapacity: Optional[int] = None
    MinSize: Optional[int] = None
    PoolState: Optional[WarmPoolStateType] = None
    InstanceReusePolicy: Optional[InstanceReusePolicyTypeDef] = None


class WarmPoolConfigurationTypeDef(BaseValidatorModel):
    MaxGroupPreparedCapacity: Optional[int] = None
    MinSize: Optional[int] = None
    PoolState: Optional[WarmPoolStateType] = None
    Status: Optional[Literal["PendingDelete"]] = None
    InstanceReusePolicy: Optional[InstanceReusePolicyTypeDef] = None


class ProcessesTypeTypeDef(BaseValidatorModel):
    Processes: List[ProcessTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ScheduledActionsTypeTypeDef(BaseValidatorModel):
    ScheduledUpdateGroupActions: List[ScheduledUpdateGroupActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AutoScalingInstancesTypeTypeDef(BaseValidatorModel):
    AutoScalingInstances: List[AutoScalingInstanceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateLaunchConfigurationTypeTypeDef(BaseValidatorModel):
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


class LaunchConfigurationTypeDef(BaseValidatorModel):
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


class BaselinePerformanceFactorsRequestOutputTypeDef(BaseValidatorModel):
    Cpu: Optional[CpuPerformanceFactorRequestOutputTypeDef] = None


class BaselinePerformanceFactorsRequestTypeDef(BaseValidatorModel):
    Cpu: Optional[CpuPerformanceFactorRequestTypeDef] = None


class MetricStatOutputTypeDef(BaseValidatorModel):
    Metric: MetricOutputTypeDef
    Stat: str
    Unit: Optional[str] = None


class TargetTrackingMetricStatOutputTypeDef(BaseValidatorModel):
    Metric: MetricOutputTypeDef
    Stat: str
    Unit: Optional[str] = None
    Period: Optional[int] = None


class MetricStatTypeDef(BaseValidatorModel):
    Metric: MetricTypeDef
    Stat: str
    Unit: Optional[str] = None


class TargetTrackingMetricStatTypeDef(BaseValidatorModel):
    Metric: MetricTypeDef
    Stat: str
    Unit: Optional[str] = None
    Period: Optional[int] = None


class BatchPutScheduledUpdateGroupActionTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    ScheduledUpdateGroupActions: Sequence[ScheduledUpdateGroupActionRequestTypeDef]


class RollbackDetailsTypeDef(BaseValidatorModel):
    RollbackReason: Optional[str] = None
    RollbackStartTime: Optional[datetime] = None
    PercentageCompleteOnRollback: Optional[int] = None
    InstancesToUpdateOnRollback: Optional[int] = None
    ProgressDetailsOnRollback: Optional[InstanceRefreshProgressDetailsTypeDef] = None


class DescribeWarmPoolAnswerTypeDef(BaseValidatorModel):
    WarmPoolConfiguration: WarmPoolConfigurationTypeDef
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LaunchConfigurationsTypeTypeDef(BaseValidatorModel):
    LaunchConfigurations: List[LaunchConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class InstanceRequirementsOutputTypeDef(BaseValidatorModel):
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
    BaselinePerformanceFactors: Optional[BaselinePerformanceFactorsRequestOutputTypeDef] = None


class InstanceRequirementsTypeDef(BaseValidatorModel):
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
    BaselinePerformanceFactors: Optional[BaselinePerformanceFactorsRequestTypeDef] = None


class MetricDataQueryOutputTypeDef(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[MetricStatOutputTypeDef] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None


class TargetTrackingMetricDataQueryOutputTypeDef(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatOutputTypeDef] = None
    Label: Optional[str] = None
    Period: Optional[int] = None
    ReturnData: Optional[bool] = None


class MetricDataQueryTypeDef(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[MetricStatTypeDef] = None
    Label: Optional[str] = None
    ReturnData: Optional[bool] = None


class TargetTrackingMetricDataQueryTypeDef(BaseValidatorModel):
    Id: str
    Expression: Optional[str] = None
    MetricStat: Optional[TargetTrackingMetricStatTypeDef] = None
    Label: Optional[str] = None
    Period: Optional[int] = None
    ReturnData: Optional[bool] = None


class LaunchTemplateOverridesOutputTypeDef(BaseValidatorModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[str] = None
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecificationTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsOutputTypeDef] = None


class LaunchTemplateOverridesTypeDef(BaseValidatorModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[str] = None
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecificationTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsTypeDef] = None


class PredictiveScalingCustomizedCapacityMetricOutputTypeDef(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]


class PredictiveScalingCustomizedLoadMetricOutputTypeDef(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]


class PredictiveScalingCustomizedScalingMetricOutputTypeDef(BaseValidatorModel):
    MetricDataQueries: List[MetricDataQueryOutputTypeDef]


class CustomizedMetricSpecificationOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[List[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Period: Optional[int] = None
    Metrics: Optional[List[TargetTrackingMetricDataQueryOutputTypeDef]] = None


class PredictiveScalingCustomizedCapacityMetricTypeDef(BaseValidatorModel):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]


class PredictiveScalingCustomizedLoadMetricTypeDef(BaseValidatorModel):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]


class PredictiveScalingCustomizedScalingMetricTypeDef(BaseValidatorModel):
    MetricDataQueries: Sequence[MetricDataQueryTypeDef]


class CustomizedMetricSpecificationTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    Dimensions: Optional[Sequence[MetricDimensionTypeDef]] = None
    Statistic: Optional[MetricStatisticType] = None
    Unit: Optional[str] = None
    Period: Optional[int] = None
    Metrics: Optional[Sequence[TargetTrackingMetricDataQueryTypeDef]] = None


class LaunchTemplateOutputTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[List[LaunchTemplateOverridesOutputTypeDef]] = None


class LaunchTemplateTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[LaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[Sequence[LaunchTemplateOverridesTypeDef]] = None


class PredictiveScalingMetricSpecificationOutputTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricPairSpecification: Optional[PredictiveScalingPredefinedMetricPairTypeDef] = None
    PredefinedScalingMetricSpecification: Optional[ PredictiveScalingPredefinedScalingMetricTypeDef ] = None
    PredefinedLoadMetricSpecification: Optional[PredictiveScalingPredefinedLoadMetricTypeDef] = None
    CustomizedScalingMetricSpecification: Optional[ PredictiveScalingCustomizedScalingMetricOutputTypeDef ] = None
    CustomizedLoadMetricSpecification: Optional[ PredictiveScalingCustomizedLoadMetricOutputTypeDef ] = None
    CustomizedCapacityMetricSpecification: Optional[ PredictiveScalingCustomizedCapacityMetricOutputTypeDef ] = None


class TargetTrackingConfigurationOutputTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecificationOutputTypeDef] = None
    DisableScaleIn: Optional[bool] = None


class PredictiveScalingMetricSpecificationTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricPairSpecification: Optional[PredictiveScalingPredefinedMetricPairTypeDef] = None
    PredefinedScalingMetricSpecification: Optional[ PredictiveScalingPredefinedScalingMetricTypeDef ] = None
    PredefinedLoadMetricSpecification: Optional[PredictiveScalingPredefinedLoadMetricTypeDef] = None
    CustomizedScalingMetricSpecification: Optional[ PredictiveScalingCustomizedScalingMetricTypeDef ] = None
    CustomizedLoadMetricSpecification: Optional[PredictiveScalingCustomizedLoadMetricTypeDef] = None
    CustomizedCapacityMetricSpecification: Optional[ PredictiveScalingCustomizedCapacityMetricTypeDef ] = None


class TargetTrackingConfigurationTypeDef(BaseValidatorModel):
    TargetValue: float
    PredefinedMetricSpecification: Optional[PredefinedMetricSpecificationTypeDef] = None
    CustomizedMetricSpecification: Optional[CustomizedMetricSpecificationTypeDef] = None
    DisableScaleIn: Optional[bool] = None


class MixedInstancesPolicyOutputTypeDef(BaseValidatorModel):
    LaunchTemplate: Optional[LaunchTemplateOutputTypeDef] = None
    InstancesDistribution: Optional[InstancesDistributionTypeDef] = None


class MixedInstancesPolicyTypeDef(BaseValidatorModel):
    LaunchTemplate: Optional[LaunchTemplateTypeDef] = None
    InstancesDistribution: Optional[InstancesDistributionTypeDef] = None


class LoadForecastTypeDef(BaseValidatorModel):
    Timestamps: List[datetime]
    Values: List[float]
    MetricSpecification: PredictiveScalingMetricSpecificationOutputTypeDef


class PredictiveScalingConfigurationOutputTypeDef(BaseValidatorModel):
    MetricSpecifications: List[PredictiveScalingMetricSpecificationOutputTypeDef]
    Mode: Optional[PredictiveScalingModeType] = None
    SchedulingBufferTime: Optional[int] = None
    MaxCapacityBreachBehavior: Optional[PredictiveScalingMaxCapacityBreachBehaviorType] = None
    MaxCapacityBuffer: Optional[int] = None


class PredictiveScalingConfigurationTypeDef(BaseValidatorModel):
    MetricSpecifications: Sequence[PredictiveScalingMetricSpecificationTypeDef]
    Mode: Optional[PredictiveScalingModeType] = None
    SchedulingBufferTime: Optional[int] = None
    MaxCapacityBreachBehavior: Optional[PredictiveScalingMaxCapacityBreachBehaviorType] = None
    MaxCapacityBuffer: Optional[int] = None


class AutoScalingGroupTypeDef(BaseValidatorModel):
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
    AvailabilityZoneDistribution: Optional[AvailabilityZoneDistributionTypeDef] = None
    AvailabilityZoneImpairmentPolicy: Optional[AvailabilityZoneImpairmentPolicyTypeDef] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecificationOutputTypeDef] = None


class DesiredConfigurationOutputTypeDef(BaseValidatorModel):
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyOutputTypeDef] = None


class DesiredConfigurationTypeDef(BaseValidatorModel):
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyTypeDef] = None


class GetPredictiveScalingForecastAnswerTypeDef(BaseValidatorModel):
    LoadForecast: List[LoadForecastTypeDef]
    CapacityForecast: CapacityForecastTypeDef
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ScalingPolicyTypeDef(BaseValidatorModel):
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


class AutoScalingGroupsTypeTypeDef(BaseValidatorModel):
    AutoScalingGroups: List[AutoScalingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class InstanceRefreshTypeDef(BaseValidatorModel):
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


class CapacityReservationSpecificationUnionTypeDef(BaseValidatorModel):
    pass


class MixedInstancesPolicyUnionTypeDef(BaseValidatorModel):
    pass


class CreateAutoScalingGroupTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    MinSize: int
    MaxSize: int
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyUnionTypeDef] = None
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
    AvailabilityZoneDistribution: Optional[AvailabilityZoneDistributionTypeDef] = None
    AvailabilityZoneImpairmentPolicy: Optional[AvailabilityZoneImpairmentPolicyTypeDef] = None
    SkipZonalShiftValidation: Optional[bool] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecificationUnionTypeDef] = None


class UpdateAutoScalingGroupTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    LaunchConfigurationName: Optional[str] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    MixedInstancesPolicy: Optional[MixedInstancesPolicyUnionTypeDef] = None
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
    AvailabilityZoneDistribution: Optional[AvailabilityZoneDistributionTypeDef] = None
    AvailabilityZoneImpairmentPolicy: Optional[AvailabilityZoneImpairmentPolicyTypeDef] = None
    SkipZonalShiftValidation: Optional[bool] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecificationUnionTypeDef] = None


class PoliciesTypeTypeDef(BaseValidatorModel):
    ScalingPolicies: List[ScalingPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TargetTrackingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PredictiveScalingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutScalingPolicyTypeTypeDef(BaseValidatorModel):
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
    TargetTrackingConfiguration: Optional[TargetTrackingConfigurationUnionTypeDef] = None
    Enabled: Optional[bool] = None
    PredictiveScalingConfiguration: Optional[PredictiveScalingConfigurationUnionTypeDef] = None


class DescribeInstanceRefreshesAnswerTypeDef(BaseValidatorModel):
    InstanceRefreshes: List[InstanceRefreshTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DesiredConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class RefreshPreferencesUnionTypeDef(BaseValidatorModel):
    pass


class StartInstanceRefreshTypeTypeDef(BaseValidatorModel):
    AutoScalingGroupName: str
    Strategy: Optional[Literal["Rolling"]] = None
    DesiredConfiguration: Optional[DesiredConfigurationUnionTypeDef] = None
    Preferences: Optional[RefreshPreferencesUnionTypeDef] = None


